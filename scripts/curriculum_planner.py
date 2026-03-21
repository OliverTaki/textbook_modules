"""
curriculum_planner.py — KnowledgeMapProject カリキュラム自動拡張スクリプト
CURRICULUM_MAP.md を読み込み、TASK_QUEUE に未着手のモジュールを自動追加する。

実行: py scripts/curriculum_planner.py
"""

from pathlib import Path
from datetime import datetime, timezone
import re

BASE = Path(r"C:\Users\punch\Desktop\KnowledgeMapProject")

def ts():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")

def rfile(path):
    try: return Path(path).read_text(encoding="utf-8")
    except: return ""

def wfile(path, content):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(content, encoding="utf-8")

# ─────────────────────────────────────────────────────────────
def parse_curriculum():
    """CURRICULUM_MAP.md からモジュール一覧を返す"""
    content = rfile(BASE / "CURRICULUM_MAP.md")
    modules = []
    for line in content.split("\n"):
        line = line.strip()
        if not line.startswith("| ") or line.startswith("| module_id") or line.startswith("|---"):
            continue
        parts = [p.strip() for p in line.split("|")]
        parts = [p for p in parts if p]   # 空要素除去
        if len(parts) >= 4:
            modules.append({
                "module_id": parts[0],
                "level":     parts[1],
                "grade":     parts[2],
                "title":     parts[3],
                "prereqs":   parts[4] if len(parts) > 4 else ""
            })
    return modules

def get_existing_module_ids():
    """TASK_QUEUE.md に登録済みのモジュールIDを返す"""
    ids = set()
    for line in rfile(BASE / "TASK_QUEUE.md").split("\n"):
        m = re.search(r"\|\s*([\w-]+)\s*\|", line)
        if m:
            ids.add(m.group(1).strip())
    return ids

def get_completed_module_ids():
    """math/modules/ に存在する（生成済み）モジュールIDを返す"""
    return {f.stem for f in (BASE / "math" / "modules").glob("*.md")
            if "_draft" not in f.name}

def get_next_task_number():
    """TASK_QUEUE の最大タスク番号 + 1 を返す"""
    max_n = 0
    for line in rfile(BASE / "TASK_QUEUE.md").split("\n"):
        m = re.search(r"TASK-(\d+)", line)
        if m:
            max_n = max(max_n, int(m.group(1)))
    return max_n + 1

# ─────────────────────────────────────────────────────────────
def add_missing_tasks():
    """
    CURRICULUM_MAP に存在し TASK_QUEUE に未登録のモジュールを
    TASK_QUEUE の pending セクションに追加する。
    """
    curriculum  = parse_curriculum()
    in_queue    = get_existing_module_ids()
    completed   = get_completed_module_ids()
    already_known = in_queue | completed

    missing = [m for m in curriculum if m["module_id"] not in already_known]

    def safe(s):
        return s.encode("cp932", errors="backslashreplace").decode("cp932")

    if not missing:
        print(safe(f"[{ts()}] curriculum_planner: 新規追加なし（全{len(curriculum)}件登録済み）"),
              flush=True)
        return 0

    today  = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    next_n = get_next_task_number()
    added  = 0

    # 1件ずつ TASK_QUEUE に追記（途中クラッシュでも保存される）
    for mod in missing:
        tid   = f"TASK-{next_n:03d}"
        level_label = {"elementary": "小学校", "middle": "中学校", "high": "高校"}.get(mod["level"], mod["level"])
        line  = (
            f"[ ] {tid} | {mod['module_id']} | {mod['title']} "
            f"| Researcher | {level_label} | {today}\n"
        )
        # 追記モードで1行ずつ書き込む（アトミック）
        with open(BASE / "TASK_QUEUE.md", "a", encoding="utf-8") as f:
            f.write(line)
        print(safe(f"  + {tid}: {mod['module_id']} {mod['title']}"), flush=True)
        next_n += 1
        added  += 1

    print(safe(f"[{ts()}] curriculum_planner: {added}件を TASK_QUEUE に追加しました。"),
          flush=True)
    return added

# ─────────────────────────────────────────────────────────────
def main():
    print(f"[{ts()}] curriculum_planner: スキャン開始", flush=True)
    n = add_missing_tasks()
    print(f"[{ts()}] curriculum_planner: 完了（追加={n}件）", flush=True)

if __name__ == "__main__":
    main()
