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

BASE = Path(r"C:\Users\punch\Desktop\KnowledgeMapProject")
OLLAMA_HOST = "http://localhost:11434"

MODELS = {
    "Researcher":       "qwen3.5:9b",
    "Editor":           "qwen3.5:9b",
    "Professor":        "qwen3.5:9b",
    "Critical Thinker": "qwen3.5:9b",
    "Editor-in-Chief":  "qwen3.5:9b",
}
RELAY_ORDER = ["Researcher", "Editor", "Professor", "Critical Thinker", "Editor-in-Chief"]

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
    print(entry.strip(), flush=True)

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

def get_next_task():
    for line in rfile(BASE / "TASK_QUEUE.md").split("\n"):
        s = line.strip()
        if s.startswith("[ ]") and "|" in s:
            parts = [p.strip() for p in s.replace("[ ]", "").split("|")]
            if len(parts) >= 4:
                return {"task_id": parts[0], "module_id": parts[1],
                        "title": parts[2], "start_role": parts[3]}
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

async def role_editor(task):
    m, t = task["module_id"], task["title"]
    schema = rfile(BASE / 'math' / 'MODULE_SCHEMA.md')
    sources = rfile(BASE / 'sources' / f'{m}_sources.md')
    prompt = (
        f"【重要】モジュールID: {m}、タイトル:「{t}」の初稿を作成せよ。\n"
        f"module_id は必ず {m}、title は必ず「{t}」とすること。\n\n"
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
        f"数学モジュール {m} の初稿（概念説明・例題部分）を Professor としてレビューせよ。\n\n"
        f"初稿（抜粋）:\n{draft_excerpt}\n\n"
        "確認事項: 数式・定義・計算ステップの正確性のみ確認する。\n"
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
    prof_summary = prof_raw[-1000:].strip() if prof_raw else "（Professor レビューなし）"
    ct_summary   = ct_raw[-1000:].strip()   if ct_raw   else "（CT レビューなし）"

    prompt = (
        f"モジュールID: {m}「{t}」の最終稿を新規作成してください。\n\n"
        f"## レビュー指摘（すべて反映必須）\n\n"
        f"### Professor レビュー（抜粋）:\n{prof_summary}\n\n"
        f"### Critical Thinker レビュー（抜粋）:\n{ct_summary}\n\n"
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
    for attempt in range(3):
        raw = await qwen("Editor-in-Chief", system, prompt)
        raw = re.sub(r"<think>.*?</think>", "", raw, flags=re.DOTALL).strip()
        violations = detect_foreign_language(raw)
        if violations:
            if attempt < 2:
                log(task["task_id"], "Editor-in-Chief", f"retry {attempt+1}/3 — foreign language: {violations[:3]}")
                continue
            # On final attempt: log and write anyway, but flag it
            errlog(task["task_id"], "Editor-in-Chief",
                   f"Foreign language persists after 3 attempts: {violations[:5]}")
        result = raw
        break

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
            elif role == "Editor":          await role_editor(task)
            elif role == "Professor":
                result = await role_professor(task)
                if "verdict: NG" in result:
                    log(tid, role, "NG — holding")
                    hold_task(tid, "Professor NG"); return False
            elif role == "Critical Thinker":
                result = await role_critical_thinker(task)
                hc = re.search(r"high_count:\s*(\d+)", result)
                if hc and int(hc.group(1)) >= 3:
                    log(tid, role, f"high_count={hc.group(1)} — holding")
                    hold_task(tid, f"CT high_count={hc.group(1)}"); return False
            elif role == "Editor-in-Chief":
                await role_editor_in_chief(task)
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
