"""
audit_modules.py — KnowledgeMapProject セルフ監査スクリプト
math/modules/ の全モジュールをスキャンし、品質問題を検出して
TASK_QUEUE に自動再投入する。

検出項目:
  1. 外国語文字（タイ語・韓国語・アラビア語）
  2. YAMLフロントマターの ```yaml``` ラッパー
  3. 薄いコンテンツ（THIN_THRESHOLD 文字未満）

実行: py scripts/audit_modules.py
"""

from pathlib import Path
from datetime import datetime, timezone
import re, sys

BASE = Path(r"C:\Users\punch\Desktop\KnowledgeMapProject")
THIN_THRESHOLD = 4500   # この文字数未満は thin と判断

# ─────────────────────────────────────────────────────────────
def ts():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")

def rfile(path):
    try: return Path(path).read_text(encoding="utf-8")
    except: return ""

def wfile(path, content):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(content, encoding="utf-8")

# ─────────────────────────────────────────────────────────────
def detect_foreign_language(text):
    """タイ語・韓国語・アラビア語文字を検出して返す（重複なし）"""
    violations = []
    seen = set()
    for ch in text:
        cp = ord(ch)
        label = None
        if 0x0E00 <= cp <= 0x0E7F:
            label = f"タイ語:{ch!r}(U+{cp:04X})"
        elif 0xAC00 <= cp <= 0xD7A3 or 0x1100 <= cp <= 0x11FF or 0x3130 <= cp <= 0x318F:
            label = f"韓国語:{ch!r}(U+{cp:04X})"
        elif 0x0600 <= cp <= 0x06FF:
            label = f"アラビア語:{ch!r}(U+{cp:04X})"
        if label and label not in seen:
            violations.append(label)
            seen.add(label)
    return violations

# ─────────────────────────────────────────────────────────────
def scan_modules():
    """math/modules/ 内の全モジュールを検査し、問題一覧を返す"""
    modules_dir = BASE / "math" / "modules"
    results = {}    # module_id -> [issue_str, ...]

    for f in sorted(modules_dir.glob("*.md")):
        if "_draft" in f.name:
            continue
        mid = f.stem
        content = rfile(f)
        issues = []

        # 1. 外国語文字
        violations = detect_foreign_language(content)
        if violations:
            issues.append(f"foreign_language: {violations[:5]}")

        # 2. YAML ```yaml``` ラッパー
        if "```yaml" in content:
            issues.append("yaml_wrapper: frontmatterが```yaml```で囲まれている")

        # 3. 薄いコンテンツ
        char_count = len(content)
        if char_count < THIN_THRESHOLD:
            issues.append(f"thin_content: {char_count}字 (閾値 {THIN_THRESHOLD}字)")

        if issues:
            results[mid] = issues

    return results

# ─────────────────────────────────────────────────────────────
def reset_task_to_eic(module_id, today_str):
    """TASK_QUEUE の該当モジュールを [ ] Editor-in-Chief に戻す"""
    path = BASE / "TASK_QUEUE.md"
    lines = rfile(path).split("\n")
    new_lines = []
    changed = False

    for line in lines:
        s = line.strip()
        # 対象行: [x] または [H] で module_id を含む行
        if (s.startswith("[x]") or s.startswith("[H]")) and f"| {module_id} |" in s:
            # フィールド分解
            body = re.sub(r"^\[.\]\s*", "", s)
            parts = [p.strip() for p in body.split("|")]
            if len(parts) >= 2 and parts[1] == module_id:
                # START_ROLE を Editor-in-Chief に上書き
                while len(parts) < 6:
                    parts.append("")
                parts[3] = "Editor-in-Chief"
                parts[4] = "再処理"
                parts[5] = today_str
                new_line = "[ ] " + " | ".join(parts)
                new_lines.append(new_line)
                changed = True
                continue
        new_lines.append(line)

    if changed:
        wfile(path, "\n".join(new_lines))
    return changed

# ─────────────────────────────────────────────────────────────
def log_to_error_log(module_id, issues):
    with open(BASE / "ERROR_LOG.md", "a", encoding="utf-8") as f:
        for issue in issues:
            f.write(f"{ts()} | {module_id} | audit | FLAGGED | {issue}\n")

# ─────────────────────────────────────────────────────────────
def main():
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    print(f"[{ts()}] audit_modules: スキャン開始", flush=True)

    problems = scan_modules()

    if not problems:
        print("[audit] 問題なし。全モジュールパス。", flush=True)
        return

    def safe(s):
        """cp932で印字できない文字を \\uXXXX にエスケープして返す"""
        return s.encode("cp932", errors="backslashreplace").decode("cp932")

    print(safe(f"[audit] {len(problems)} モジュールに問題を検出:"), flush=True)
    for mid, issues in problems.items():
        print(safe(f"  [{mid}]"), flush=True)
        for iss in issues:
            print(safe(f"    - {iss}"), flush=True)
        log_to_error_log(mid, issues)
        changed = reset_task_to_eic(mid, today)
        status = "→ TASK_QUEUEリセット済み" if changed else "→ TASK_QUEUEに対応タスクなし（手動確認が必要）"
        print(safe(f"  {status}"), flush=True)

    print(f"[{ts()}] audit_modules: 完了", flush=True)

if __name__ == "__main__":
    main()
