"""
run_loop.py — Qwen autonomous relay loop for KnowledgeMapProject
Relay: Researcher -> Editor -> Professor -> Critical Thinker -> Editor-in-Chief
"""
import asyncio, re, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
from openai import AsyncOpenAI
sys.path.insert(0, str(Path(__file__).parent))
import discord_notify as discord
import audit_modules as auditor
import curriculum_planner
import web_search

BASE = Path(r"C:\Users\punch\Desktop\KnowledgeMapProject")
OLLAMA_HOST = "http://localhost:11434"

MODELS = {
    "Researcher":       "qwen3.5:9b",
    "Librarian":        "qwen3.5:9b",
    "Editor":           "qwen3.5:9b",
    "Professor":        "qwen3.5:9b",
    "Critical Thinker": "qwen3.5:9b",
    "Fact Checker":     "qwen3.5:9b",
    "Editor-in-Chief":  "qwen3.5:9b",
}
RELAY_ORDER = ["Researcher", "Librarian", "Editor", "Professor", "Critical Thinker", "Fact Checker", "Editor-in-Chief"]

client = AsyncOpenAI(base_url=f"{OLLAMA_HOST}/v1", api_key="ollama")

def ts():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")

def rfile(path):
    try: return Path(path).read_text(encoding="utf-8")
    except: return ""

def wfile(path, content):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(content, encoding="utf-8")

def detect_foreign_language(text):
    """
    Detect non-Japanese foreign script characters in text.
    Returns a list of violation samples (empty list = clean).
    Japanese kanji (CJK) overlaps with Chinese so we only flag
    unambiguous non-Japanese scripts: Thai, Korean (Hangul), Arabic.
    """
    violations = []
    seen = set()
    for ch in text:
        cp = ord(ch)
        label = None
        if 0x0E00 <= cp <= 0x0E7F:
            label = f"タイ語: {ch!r} U+{cp:04X}"
        elif 0xAC00 <= cp <= 0xD7A3 or 0x1100 <= cp <= 0x11FF or 0x3130 <= cp <= 0x318F:
            label = f"韓国語: {ch!r} U+{cp:04X}"
        elif 0x0600 <= cp <= 0x06FF:
            label = f"アラビア語: {ch!r} U+{cp:04X}"
        if label and label not in seen:
            violations.append(label)
            seen.add(label)
    return violations

def log(task_id, role, status, note=""):
    entry = f"{ts()} | {task_id} | {role} | {status} | {note}\n"
    with open(BASE / "RUN_LOG.md", "a", encoding="utf-8") as f:
        f.write(entry)
    safe = entry.encode("cp932", errors="backslashreplace").decode("cp932")
    print(safe.strip(), flush=True)

def errlog(task_id, role, msg):
    with open(BASE / "ERROR_LOG.md", "a", encoding="utf-8") as f:
        f.write(f"{ts()} | {task_id} | {role} | ERROR | {msg[:400]}\n")

def set_state(status, task="none", role="none", module="none"):
    wfile(BASE / "SYSTEM_STATE.md",
          f"# SYSTEM_STATE\nstatus: {status}\nlast_updated: {ts()}\nupdated_by: run_loop\n"
          f"current_task: {task}\ncurrent_role: {role}\ncurrent_module: {module}\n")

def get_state():
    m = re.search(r"status:\s*(\w+)", rfile(BASE / "SYSTEM_STATE.md"))
    return m.group(1) if m else "idle"

LEVEL_LABELS = {
    "elementary": ("小学校", "算数"),
    "middle":     ("中学校", "数学"),
    "high":       ("高校",   "数学"),
}
GRADE_AGE = {
    "1": "6〜7歳（小1）", "2": "7〜8歳（小2）", "3": "8〜9歳（小3）",
    "4": "9〜10歳（小4）", "5": "10〜11歳（小5）", "6": "11〜12歳（小6）",
    "7": "12〜13歳（中1）", "8": "13〜14歳（中2）", "9": "14〜15歳（中3）",
    "10": "15〜16歳（高1）", "11": "16〜17歳（高2）", "12": "17〜18歳（高3）",
}

def get_module_meta(module_id):
    """CURRICULUM_MAP から level / grade を返す"""
    for line in rfile(BASE / "CURRICULUM_MAP.md").split("\n"):
        if f"| {module_id} |" in line:
            parts = [p.strip() for p in line.split("|")]
            parts = [p for p in parts if p]
            if len(parts) >= 3:
                return {"level": parts[1], "grade": parts[2]}
    return {"level": "high", "grade": "10"}

def get_next_task():
    for line in rfile(BASE / "TASK_QUEUE.md").split("\n"):
        s = line.strip()
        if s.startswith("[ ]") and "|" in s:
            parts = [p.strip() for p in s.replace("[ ]", "").split("|")]
            if len(parts) >= 4:
                mid  = parts[1]
                meta = get_module_meta(mid)
                level, grade = meta["level"], meta["grade"]
                school, subject = LEVEL_LABELS.get(level, ("高校", "数学"))
                age = GRADE_AGE.get(grade, "")
                return {
                    "task_id":    parts[0],
                    "module_id":  mid,
                    "title":      parts[2],
                    "start_role": parts[3],
                    "level":      level,
                    "grade":      grade,
                    "school":     school,
                    "subject":    subject,
                    "age":        age,
                }
    return None

def update_task_line(task_id, old_m, new_m):
    path = BASE / "TASK_QUEUE.md"
    lines = rfile(path).split("\n")
    wfile(path, "\n".join(
        line.replace(f"{old_m} {task_id}", f"{new_m} {task_id}", 1)
        if f"{old_m} {task_id}" in line else line for line in lines))

def hold_task(task_id, reason):
    update_task_line(task_id, "[>]", "[H]")
    update_task_line(task_id, "[ ]", "[H]")
    with open(BASE / "HOLD_QUEUE.md", "a", encoding="utf-8") as f:
        f.write(f"\n[H] {task_id} | {reason} | {ts()} | awaiting review\n")
    set_state("hold")
    discord.notify_hold(task_id, reason)

def git_commit_module(module_id, title):
    try:
        branch = f"task/{module_id}"
        subprocess.run(["git", "checkout", "-b", branch], cwd=BASE, capture_output=True)
        subprocess.run(["git", "add", "math/modules/"], cwd=BASE, capture_output=True)
        msg = BASE / ".git" / "COMMIT_MSG.txt"
        msg.write_text(f"add module: {module_id} {title}\n", encoding="utf-8")
        subprocess.run(["git", "commit", "-F", str(msg)], cwd=BASE, capture_output=True)
        subprocess.run(["git", "checkout", "main"], cwd=BASE, capture_output=True)
        subprocess.run(["git", "merge", "--no-ff", branch], cwd=BASE, capture_output=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=BASE, capture_output=True)
        log(module_id, "git", "pushed")
        discord.notify_published(module_id, title)
        return True
    except Exception as e:
        errlog(module_id, "git", str(e))
        return False

async def qwen(role, system_prompt, user_prompt):
    resp = await client.chat.completions.create(
        model=MODELS[role],
        messages=[{"role": "system", "content": system_prompt},
                  {"role": "user",   "content": user_prompt}],
        timeout=600)
    return resp.choices[0].message.content

async def role_researcher(task):
    m, t = task["module_id"], task["title"]
    prompt = (
        f"【モジュールID: {m}】【タイトル: {t}】のソース調査を行う。\n\n"
        f"このタスクは {m}「{t}」専用である。他のモジュールの内容を生成してはならない。\n\n"
        f"SOURCE_REGISTRY(既登録):\n{rfile(BASE / 'SOURCE_REGISTRY.md')}\n\n"
        "上記に登録されていないCC BY / CC0ライセンスのソースを新たに列挙すること。\n"
        "各ソースにID・タイトル・URL・ライセンスを記載。日本語で出力。"
    )
    result = await qwen("Researcher", rfile(BASE / "roles" / "ROLE_RESEARCHER.md"), prompt)
    wfile(BASE / "sources" / f"{m}_sources.md", result)

async def role_librarian(task):
    m, t = task["module_id"], task["title"]
    ref_dir = BASE / "references" / m
    log(task["task_id"], "Librarian", "collecting", f"{m} {t}")
    try:
        index_text, sources = web_search.collect_references(m, t, ref_dir, max_pages=3)
    except Exception as e:
        # ネットワークエラーでも続行
        errlog(task["task_id"], "Librarian", str(e))
        index_text = f"# References: {m}\n収集失敗: {e}\n"
        sources = []
        (ref_dir / "INDEX.md").write_text(index_text, encoding="utf-8")

    # Qwen で収集資料の要約を生成
    wiki_text = rfile(ref_dir / "wikipedia.txt")[:3000] if (ref_dir / "wikipedia.txt").exists() else ""
    prompt = (
        f"モジュール {m}「{t}」の参照資料を以下に示す。\n\n"
        f"## Wikipedia 抜粋:\n{wiki_text[:2000] if wiki_text else '（取得なし）'}\n\n"
        f"## 収集資料一覧:\n{index_text}\n\n"
        "上記資料の内容を踏まえ、このモジュールで扱う数学的概念の要点を日本語で300字以内にまとめよ。"
        "Editor が教材を書く際の参考情報として使う。"
    )
    summary = await qwen("Librarian", rfile(BASE / "roles" / "ROLE_LIBRARIAN.md"), prompt)
    wfile(ref_dir / "SUMMARY.md", summary)
    wfile(BASE / "references" / f"{m}_summary.md", f"# {m} 資料要約\n\n{summary}\n")

async def role_editor(task):
    m, t = task["module_id"], task["title"]
    schema = rfile(BASE / 'math' / 'MODULE_SCHEMA.md')
    sources = rfile(BASE / 'sources' / f'{m}_sources.md')
    prompt = (
        f"【重要】モジュールID: {m}、タイトル:「{t}」の初稿を作成せよ。\n"
        f"module_id は必ず {m}、title は必ず「{t}」とすること。\n\n"
        f"## 対象読者（厳守）\n"
        f"- 学校種別: {task.get('school','高校')} {task.get('subject','数学')}\n"
        f"- 学年・年齢: {task.get('grade','')}/{task.get('age','高校生')}\n"
        f"- この年齢の学習者が理解できる語彙・概念のみ使用すること。\n"
        f"- 高度すぎる概念（大学・専門レベル）は一切含めてはならない。\n\n"
        "## 出力ルール（厳守）\n"
        "- 出力はモジュール本文のみ。ソース文書・説明コメント・前置きは一切含めない。\n"
        "- 最初の行は必ず `---`（YAMLフロントマター開始）から始める。\n"
        "- frontmatterは```yaml で囲まない。raw `---` で開閉する。\n"
        "- frontmatterの直後に本文セクションを続ける。\n\n"
        f"## YAML frontmatterテンプレート（この形式で出力）\n"
        f"---\n"
        f"module_id: {m}\n"
        f"title: {t}\n"
        "domain: [適切なドメイン]\n"
        "concept_tags: [タグ1, タグ2, ...]\n"
        "prerequisites: []\n"
        "next_modules: []\n"
        "source_references:\n"
        "  - id: [SRC-ID]\n"
        "    title: [タイトル]\n"
        "    license: CC BY\n"
        "license: CC BY 4.0\n"
        "status: draft\n"
        "---\n\n"
        "## 本文セクション（この順で書く）\n"
        "1. ## 概念説明 — 400字以上。定義→性質→グラフ的解釈を説明文で展開。箇条書きのみ禁止。\n"
        "2. ## 例題 — 2件以上。問題文＋全ステップの解答（途中省略禁止）\n"
        "3. ## 練習問題 — 3件以上。各問に完全な解答と採点基準（配点付き）\n"
        "4. ## 問題生成ルール\n"
        "5. ## 各国・文化的差異\n"
        "6. ## 補足ノート\n\n"
        f"## 参照ソース（内容のみ参照し、ソース文書そのものは出力しない）\n{sources}\n\n"
        f"数式は $...$ または $$...$$ で記述。\n"
        f"【絶対厳守】日本語のみ使用。英語・中国語・タイ語・韓国語・アラビア語・その他外国語は一切禁止。\n"
        f"今すぐ {m}「{t}」の初稿を出力せよ。"
    )
    # 差し戻しフィードバックがある場合は末尾に追加
    if task.get("editor_feedback"):
        prompt += f"\n\n{task['editor_feedback']}"
    system = rfile(BASE / "roles" / "ROLE_EDITOR.md")
    for attempt in range(3):
        result = await qwen("Editor", system, prompt)
        # Strip any preamble before the first ---
        if '---' in result:
            result = result[result.find('---'):]
        # Validate module_id in output
        if m not in result[:600]:
            if attempt < 2:
                log(task["task_id"], "Editor", f"retry {attempt+1}/3 — module_id missing")
                continue
            raise ValueError(f"Editor output missing module_id {m} in first 600 chars after 3 attempts")
        # Validate language
        violations = detect_foreign_language(result)
        if violations:
            if attempt < 2:
                log(task["task_id"], "Editor", f"retry {attempt+1}/3 — foreign language: {violations[:3]}")
                continue
            raise ValueError(f"Editor output contains forbidden language after 3 attempts: {violations[:5]}")
        break
    wfile(BASE / "modules" / "drafts" / f"{m}_draft.md", result)
    wfile(BASE / "math" / "modules" / f"{m}_draft.md", result)

async def role_professor(task):
    m = task["module_id"]
    draft = rfile(BASE/"math"/"modules"/f"{m}_draft.md") or rfile(BASE/"modules"/"drafts"/f"{m}_draft.md")
    if not draft: raise FileNotFoundError(f"draft not found: {m}")
    # Pass only the concept explanation + examples section (first 2500 chars)
    # to avoid exceeding 4096 token context window
    draft_excerpt = draft[:2500]
    prompt = (
        f"数学モジュール {m}「{task['title']}」の初稿を Professor としてレビューせよ。\n"
        f"対象: {task.get('school','高校')} {task.get('grade','')}年生（{task.get('age','高校生')}）\n\n"
        f"初稿（抜粋）:\n{draft_excerpt}\n\n"
        "確認事項:\n"
        "1. 数式・定義・計算ステップの正確性\n"
        "2. 【学年適切性】この年齢の学習者に不適切な高度概念が含まれていないか\n"
        "   （例: 小1モジュールにUTC/TAI・原子時計が出てくるのはNG）\n"
        "出力形式（必須）:\n"
        "verdict: OK | NG | REQUIRE_REVISION\n"
        "issues:\n"
        "- [具体的な誤りがあれば列挙。なければ「なし」]\n"
        "日本語で出力。200字以内で簡潔に。"
    )
    try:
        result = await asyncio.wait_for(
            qwen("Professor", rfile(BASE/"roles"/"ROLE_PROFESSOR.md"), prompt),
            timeout=180
        )
    except asyncio.TimeoutError:
        result = "verdict: REQUIRE_REVISION\nissues:\n- Professor review timed out. Proceeding with CT review."
    wfile(BASE/"modules"/"reviews"/f"{m}_professor_review.md", result)
    return result

async def role_critical_thinker(task):
    m = task["module_id"]
    draft = rfile(BASE/"math"/"modules"/f"{m}_draft.md") or rfile(BASE/"modules"/"drafts"/f"{m}_draft.md")
    prof  = rfile(BASE/"modules"/"reviews"/f"{m}_professor_review.md")
    # Limit draft to 2000 chars to fit within 4096 token context
    draft_excerpt = draft[:2000]
    prof_excerpt  = prof[:500]
    prompt = (
        f"数学モジュール {m} の初稿（抜粋）を Critical Thinker としてレビューせよ。\n\n"
        f"初稿（抜粋）:\n{draft_excerpt}\n\n"
        f"Professor レビュー:\n{prof_excerpt}\n\n"
        "確認事項: 論理の穴・定義の飛躍・曖昧な説明に集中する。\n"
        "出力形式（必須）:\n"
        "verdict: OK | REQUIRE_REVISION\n"
        "high_count: N  (深刻な問題の件数)\n"
        "issues:\n"
        "- [問題点を列挙。なければ「なし」]\n"
        "日本語で出力。300字以内で簡潔に。"
    )
    try:
        result = await asyncio.wait_for(
            qwen("Critical Thinker", rfile(BASE/"roles"/"ROLE_CRITICAL_THINKER.md"), prompt),
            timeout=180
        )
    except asyncio.TimeoutError:
        result = "verdict: REQUIRE_REVISION\nhigh_count: 1\nissues:\n- CT review timed out."
    wfile(BASE/"modules"/"reviews"/f"{m}_ct_review.md", result)
    return result

async def role_fact_checker(task):
    m, t = task["module_id"], task["title"]
    draft = rfile(BASE/"math"/"modules"/f"{m}_draft.md") or rfile(BASE/"modules"/"drafts"/f"{m}_draft.md")
    draft_excerpt = draft[:2000]

    # ── ウェブ検索（4クエリ）──────────────────────────────────
    queries = [
        f"{t} よくある誤解 つまずき",
        f"{t} 学習指導要領 文部科学省",
        f"{t} 指導法 教え方 注意点",
        f"{t} 前提知識 つながり",
    ]
    search_results = []
    for q in queries:
        try:
            results = web_search.search_ddg(q, max_results=3)
            snippets = "\n".join(
                f"- [{r['title']}]({r['url']}): {r['snippet']}" for r in results
            )
            search_results.append(f"### クエリ: {q}\n{snippets}")
        except Exception as e:
            search_results.append(f"### クエリ: {q}\n検索失敗: {e}")

    web_evidence = "\n\n".join(search_results)

    # ── Qwen で問題提起レポートを生成 ─────────────────────────
    prompt = (
        f"モジュール {m}「{t}」の Fact Check を実施せよ。\n\n"
        f"## 初稿（抜粋）:\n{draft_excerpt}\n\n"
        f"## ウェブ調査結果:\n{web_evidence}\n\n"
        "上記の調査結果を根拠に、以下の観点で問題を**能動的に**提起せよ：\n"
        "1. よくある誤解・つまずきポイントへの対応不足\n"
        "2. 学習指導要領・文部科学省の方針との不整合\n"
        "3. 教育的妥当性の問題（教え方・順序・例の適切さ）\n"
        "4. 前提知識・前後関係の問題\n\n"
        "出力フォーマット（必須）:\n"
        "# Fact Check: {module_id}\n"
        "## 調査クエリ\n- [クエリ一覧]\n"
        "## 発見した問題・懸念点\n### [問題タイトル]\n- 根拠: [URL]\n- 内容: [指摘]\n- 重要度: HIGH/MEDIUM/LOW\n"
        "## 問題なし確認済み項目\n- [裏付けが取れた点]\n"
        "## EiC への推奨事項\n- [EiC が対処すべき事項]\n\n"
        "問題が見つからない場合でも「なぜ問題なしと判断したか」を根拠付きで示せ。"
        "日本語のみで出力せよ。"
    )
    try:
        result = await asyncio.wait_for(
            qwen("Fact Checker", rfile(BASE/"roles"/"ROLE_FACT_CHECKER.md"), prompt),
            timeout=180
        )
    except asyncio.TimeoutError:
        result = f"# Fact Check: {m}\n## 発見した問題・懸念点\n- タイムアウト。レビューをスキップ。\n## EiC への推奨事項\n- Fact Check 未完了のため、EiC が自己判断で対処すること。"

    wfile(BASE/"modules"/"reviews"/f"{m}_factcheck.md", result)
    return result

async def role_editor_in_chief(task):
    """
    Editor-in-Chief: corrections-only approach.
    Does NOT pass the full draft — generates fresh from schema + review corrections.
    This keeps the prompt well within the 4096-token context window.
    Reviews are truncated to last 1000 chars (verdict + corrections section only).
    """
    m, t = task["module_id"], task["title"]
    schema = rfile(BASE / "math" / "MODULE_SCHEMA.md")

    # Load reviews — take only the corrections/verdict portion (last 1000 chars)
    prof_raw = rfile(BASE / "modules" / "reviews" / f"{m}_professor_review.md")
    ct_raw   = rfile(BASE / "modules" / "reviews" / f"{m}_ct_review.md")
    fc_raw   = rfile(BASE / "modules" / "reviews" / f"{m}_factcheck.md")
    prof_summary = prof_raw[-1000:].strip() if prof_raw else "（Professor レビューなし）"
    ct_summary   = ct_raw[-1000:].strip()   if ct_raw   else "（CT レビューなし）"
    fc_summary   = fc_raw[-1200:].strip()   if fc_raw   else "（Fact Check なし）"

    prompt = (
        f"モジュールID: {m}「{t}」の最終稿を新規作成してください。\n\n"
        f"## レビュー指摘（すべて反映必須）\n\n"
        f"### Professor レビュー（抜粋）:\n{prof_summary}\n\n"
        f"### Critical Thinker レビュー（抜粋）:\n{ct_summary}\n\n"
        f"### Fact Checker レポート（抜粋）:\n{fc_summary}\n\n"
        f"## MODULE_SCHEMA（フォーマット仕様）:\n{schema}\n\n"
        "上記指摘を反映した完全なモジュールを出力してください。\n"
        "- YAML frontmatter の status を reviewed に\n"
        "- raw --- で frontmatter を囲む（```yaml で囲まない）\n"
        "- 概念説明・例題（2件以上）・練習問題（3件以上、採点基準付き）\n"
        "  問題生成ルール・各国差異・補足ノートのセクションを含める\n"
        "- 【絶対厳守】日本語のみ。英語・中国語・タイ語・韓国語・アラビア語・その他外国語一切禁止。\n"
        "- 最終稿の本文だけ出力（説明コメント不要）"
    )

    system = rfile(BASE / "roles" / "ROLE_EDITOR_IN_CHIEF.md")
    result = None
    critique = ""   # 前回の自己評価フィードバック

    for attempt in range(4):   # 最大4回（初回 + 3回の自己修正）
        attempt_prompt = prompt
        if critique:
            attempt_prompt += (
                f"\n\n## 【自己修正指示 — 試行{attempt}/{3}回目】\n"
                f"前回の出力に以下の問題があった。必ず修正して再生成せよ:\n{critique}"
            )

        try:
            raw = await asyncio.wait_for(
                qwen("Editor-in-Chief", system, attempt_prompt),
                timeout=300
            )
        except asyncio.TimeoutError:
            if attempt < 3:
                log(task["task_id"], "Editor-in-Chief", f"timeout attempt {attempt+1}/4 -- retry")
                critique = "- 前回はタイムアウト。出力をより簡潔にまとめよ。必須セクションのみ出力せよ。"
                continue
            log(task["task_id"], "Editor-in-Chief", "timeout x4 -- holding")
            return "SENDBACK_EDITOR", "EiC 4回タイムアウト"
        raw = re.sub(r"<think>.*?</think>", "", raw, flags=re.DOTALL).strip()

        issues = []

        # ── チェック1: 外国語 ──────────────────────────────────
        violations = detect_foreign_language(raw)
        if violations:
            issues.append(f"外国語混入: {violations[:3]}")

        # ── チェック2: YAMLラッパー ────────────────────────────
        if "```yaml" in raw:
            issues.append("frontmatterが```yaml```で囲まれている。raw ---で囲み直せ。")

        # ── チェック3: 薄すぎる ────────────────────────────────
        if len(raw) < 4500:
            issues.append(f"内容が薄すぎる({len(raw)}字)。概念説明・例題・練習問題を充実させよ。最低4500字。")

        # ── チェック4: 必須セクション欠落 ─────────────────────
        missing_sections = []
        for sec in ["概念説明", "例題", "練習問題"]:
            if sec not in raw:
                missing_sections.append(sec)
        if missing_sections:
            issues.append(f"必須セクション欠落: {missing_sections}")

        # ── チェック5: EiC 自身の差し戻し判定 ──────────────────
        # EiC が "SEND_BACK_TO_EDITOR" と出力したら Editor に差し戻す
        if "SEND_BACK_TO_EDITOR" in raw:
            reason = re.search(r"SEND_BACK_TO_EDITOR[:\s]+(.*)", raw)
            reason_str = reason.group(1)[:200] if reason else "EiCが内容不十分と判断"
            log(task["task_id"], "Editor-in-Chief", f"差し戻し → Editor: {reason_str}")
            return "SENDBACK_EDITOR", reason_str

        if not issues:
            result = raw
            if attempt > 0:
                log(task["task_id"], "Editor-in-Chief", f"自己修正 {attempt}回で合格")
            break

        # 不合格 → 自己批評を蓄積して再試行
        critique = "\n".join(f"- {i}" for i in issues)
        log(task["task_id"], "Editor-in-Chief",
            f"自己評価: 不合格（試行{attempt+1}/4）— {issues}")
        if attempt == 3:
            # 4回試みても合格しない → そのまま書いて ERROR_LOG に記録
            result = raw
            errlog(task["task_id"], "Editor-in-Chief",
                   f"4回試行後も品質基準未達: {issues}")
            log(task["task_id"], "Editor-in-Chief", "4回不合格 — 強制コミット・要人間確認")

    final = BASE / "math" / "modules" / f"{m}.md"
    wfile(final, result)
    print(f"[{ts()}] Written: {final} ({len(result)} chars)", flush=True)

    # Remove draft file to keep repo clean
    draft_f = BASE / "math" / "modules" / f"{m}_draft.md"
    if draft_f.exists():
        draft_f.unlink()

async def run_relay(task):
    tid, mid = task["task_id"], task["module_id"]
    start = task.get("start_role", "Researcher").strip()
    try:    start_idx = RELAY_ORDER.index(start)
    except: start_idx = 0

    for role in RELAY_ORDER[start_idx:]:
        set_state("running", tid, role, mid)
        log(tid, role, "start")
        discord.notify_start(mid, role)
        try:
            if   role == "Researcher":      await role_researcher(task)
            elif role == "Librarian":       await role_librarian(task)
            elif role == "Editor":          await role_editor(task)
            elif role == "Professor":
                result = await role_professor(task)
                if "verdict: NG" in result:
                    retry_count = task.get("prof_retry", 0) + 1
                    if retry_count >= 3:
                        log(tid, role, f"NG x{retry_count} -- HOLD")
                        hold_task(tid, f"Professor NG x{retry_count}"); return False
                    # 自己解決: NG の理由を Editor に渡して再生成
                    issues = result.replace("verdict: NG", "").strip()[:400]
                    task["prof_retry"]   = retry_count
                    task["editor_feedback"] = (
                        f"【Professor NG 差し戻し {retry_count}/2】\n"
                        f"以下の問題を修正して再生成せよ:\n{issues}"
                    )
                    task["start_role"] = "Editor"
                    log(tid, role, f"NG -- 自己解決: Editor 差し戻し ({retry_count}/2)")
                    discord.send(f"[{mid}] Professor NG -> Editor 差し戻し ({retry_count}/2)")
                    return await run_relay(task)

            elif role == "Critical Thinker":
                result = await role_critical_thinker(task)
                hc = re.search(r"high_count:\s*(\d+)", result)
                if hc and int(hc.group(1)) >= 3:
                    retry_count = task.get("ct_retry", 0) + 1
                    if retry_count >= 3:
                        log(tid, role, f"high_count={hc.group(1)} x{retry_count} -- HOLD")
                        hold_task(tid, f"CT high_count={hc.group(1)} x{retry_count}"); return False
                    issues = result.strip()[:400]
                    task["ct_retry"] = retry_count
                    task["editor_feedback"] = (
                        f"【Critical Thinker 差し戻し {retry_count}/2】\n"
                        f"以下の深刻な問題を修正して再生成せよ:\n{issues}"
                    )
                    task["start_role"] = "Editor"
                    log(tid, role, f"CT high -- 自己解決: Editor 差し戻し ({retry_count}/2)")
                    discord.send(f"[{mid}] CT high -> Editor 差し戻し ({retry_count}/2)")
                    return await run_relay(task)
            elif role == "Fact Checker":
                await role_fact_checker(task)
            elif role == "Editor-in-Chief":
                eic_result = await role_editor_in_chief(task)

                # EiC が Editor 差し戻しを要求した場合
                if isinstance(eic_result, tuple) and eic_result[0] == "SENDBACK_EDITOR":
                    _, reason = eic_result
                    # Editor からやり直す（差し戻し回数を追跡）
                    sendback_count = task.get("sendback_count", 0) + 1
                    if sendback_count >= 3:
                        log(tid, role, f"差し戻し上限(3回)到達 — HOLD")
                        hold_task(tid, f"EiC差し戻し上限: {reason[:100]}")
                        return False
                    task["sendback_count"] = sendback_count
                    task["start_role"] = "Editor"
                    task["eic_feedback"] = reason
                    log(tid, role, f"差し戻し({sendback_count}/3) → Editor: {reason[:80]}")
                    discord.send(f"[{mid}] EiC差し戻し({sendback_count}/3): {reason[:80]}")
                    # ループ内でリレーを Editor から再実行
                    return await run_relay(task)

                # 通常完了 — コミット前に即時品質チェック
                final_path = BASE / "math" / "modules" / f"{mid}.md"
                if final_path.exists():
                    post_issues = auditor.detect_foreign_language(
                        final_path.read_text(encoding="utf-8")
                    )
                    if post_issues:
                        log(tid, role, f"コミット後品質チェック失敗: {post_issues[:3]}")
                        errlog(tid, role, f"post-commit issues: {post_issues[:5]}")
                        # 差し戻し回数が残っていれば EiC 再実行
                        sendback_count = task.get("sendback_count", 0) + 1
                        if sendback_count < 3:
                            task["sendback_count"] = sendback_count
                            task["start_role"] = "Editor-in-Chief"
                            return await run_relay(task)

                git_commit_module(mid, task["title"])
        except FileNotFoundError as e:
            log(tid, role, "error", str(e)); errlog(tid, role, str(e))
            discord.notify_error(tid, role, str(e))
            hold_task(tid, f"{role}: {e}"); return False
        except Exception as e:
            log(tid, role, "error", str(e)[:120]); errlog(tid, role, str(e))
            discord.notify_error(tid, role, str(e))
            raise
        log(tid, role, "done")
        discord.notify_done(mid, role)
    return True

async def main():
    print(f"[{ts()}] Qwen relay loop starting.", flush=True)
    discord.send(f"KnowledgeMap ループ起動 {ts()}")

    # ── 起動時セルフ監査 ──────────────────────────────────────
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    problems = auditor.scan_modules()
    if problems:
        summary_lines = []
        for mid, issues in problems.items():
            auditor.log_to_error_log(mid, issues)
            auditor.reset_task_to_eic(mid, today)
            # issues に非ASCII文字が入る可能性があるため ASCII にエスケープ
            safe_issues = [i.encode("ascii", errors="backslashreplace").decode("ascii") for i in issues]
            summary_lines.append(f"{mid}: {', '.join(safe_issues)}")
        msg = f"[audit] {len(problems)}件の問題を検出し再投入:\n" + "\n".join(summary_lines)
        print(msg, flush=True)
        discord.send(msg)
    else:
        print("[audit] 全モジュールパス。問題なし。", flush=True)

    # ── カリキュラム自動拡張 ──────────────────────────────────
    added = curriculum_planner.add_missing_tasks()
    if added:
        discord.send(f"[curriculum] {added}件の新規モジュールを TASK_QUEUE に追加しました。")
    # ─────────────────────────────────────────────────────────

    error_streak = 0

    while True:
        state = get_state()
        if state == "stop":
            discord.send("SYSTEM_STATE=stop — 停止しました。")
            break
        if state == "hold":
            await asyncio.sleep(300); continue

        task = get_next_task()
        if task is None:
            set_state("idle")
            discord.notify_idle()
            print(f"[{ts()}] Queue empty — sleeping 5 min...", flush=True)
            await asyncio.sleep(300); error_streak = 0; continue

        print(f"[{ts()}] Task: {task['task_id']} {task['module_id']} start={task['start_role']}", flush=True)
        update_task_line(task["task_id"], "[ ]", "[>]")

        try:
            ok = await run_relay(task)
            if ok:
                update_task_line(task["task_id"], "[>]", "[x]")
                log(task["task_id"], "relay", "complete", task["module_id"])
                error_streak = 0
            else:
                error_streak += 1
        except Exception as e:
            error_streak += 1
            log(task["task_id"], "relay", "exception", str(e)[:100])
            errlog(task["task_id"], "relay", str(e))
            update_task_line(task["task_id"], "[>]", "[ ]")

        if error_streak >= 3:
            set_state("error")
            discord.send("ERROR x3 — ループ停止。ERROR_LOG を確認してください。")
            break

        await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())
