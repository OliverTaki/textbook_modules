# -*- coding: utf-8 -*-
"""
run_module_gen.py -- KnowledgeMapProject module generation runner
Qwen (via Ollama) generates a module draft based on MODULE_SCHEMA.md

Usage:
  python scripts/run_module_gen.py --module HS-FUNC-002 --title "二次関数"
  python scripts/run_module_gen.py --module HS-CALC-001 --title "微分の基礎" --model qwen3.5:9b

Output: textbook-modules/high-school-math/modules/proposals/{module_id}_{timestamp}.md
"""

import asyncio, argparse, time, sys
from datetime import datetime, timezone
from pathlib import Path
from openai import AsyncOpenAI

# --- Config ---
OLLAMA_HOST  = "http://localhost:11434"
PROJECT_ROOT = Path(__file__).parent.parent
PROPOSALS    = PROJECT_ROOT / "textbook-modules" / "high-school-math" / "modules" / "proposals"
SCHEMA_FILE  = PROJECT_ROOT / "textbook-modules" / "high-school-math" / "MODULE_SCHEMA.md"
DEFAULT_MODEL = "qwen3:1.7b"  # override with --model for better quality

client = AsyncOpenAI(base_url=f"{OLLAMA_HOST}/v1", api_key="ollama")

SYSTEM_PROMPT = """You are an expert mathematics educator and textbook author.
You write clear, accurate, pedagogically sound mathematics content.
You always use LaTeX notation for formulas ($...$ inline, $$...$$ block).
You write in Japanese with English mathematical terms in parentheses.
You never copy text directly from existing textbooks — all content is original.
You always include the full YAML frontmatter as specified."""


def build_task(module_id: str, title: str, objective: str, concepts: list[str]) -> str:
    concepts_str = "\n".join(f"- {c}" for c in concepts) if concepts else "（スキーマ参照）"
    return f"""以下のスキーマに従って、高校数学モジュールの完全な初稿を生成してください。

MODULE_ID: {module_id}
TITLE: {title}
LEVEL: 高校数学（国際標準）
OBJECTIVE: {objective}
CORE_CONCEPTS:
{concepts_str}

要件:
1. MODULE_SCHEMA.md に定義された YAML frontmatter を含む完全なファイルを生成する
2. 数式は LaTeX 記法 ($..$ / $$..$$) を使用する
3. 例題は最低2問（基礎1問・応用1問）、解答付き
4. 練習問題は最低3問、答え付き
5. よくある間違い（common_misunderstandings）を2点以上記載する
6. 参照元は OpenStax または CK-12 の該当セクションを仮定して記載する
7. 著作権クリーンな独自文章のみ（既存教科書のコピー禁止）
8. 日本語で記述し、数学用語は英語も括弧書きで併記する
9. curriculum_coverage に日本・UK・IB・シンガポール・米国の対応を記載する"""


async def run(model: str, module_id: str, title: str, objective: str, concepts: list[str]):
    PROPOSALS.mkdir(parents=True, exist_ok=True)

    task = build_task(module_id, title, objective, concepts)
    print(f"\n[{model}] Generating module: {module_id} — {title}")
    t0 = time.time()

    try:
        resp = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": task},
            ],
            temperature=0.3,
        )
        elapsed = time.time() - t0
        text = resp.choices[0].message.content
        print(f"[{model}] Done in {elapsed:.1f}s / {len(text)} chars")

        ts  = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
        out = PROPOSALS / f"{module_id}_{ts}.md"
        out.write_text(text, encoding="utf-8")
        print(f"[saved] {out}")
        return out

    except Exception as e:
        elapsed = time.time() - t0
        print(f"[ERROR] {elapsed:.1f}s: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(description="Generate a KnowledgeMap module via Qwen/Ollama")
    parser.add_argument("--module",    required=True,  help="Module ID, e.g. HS-FUNC-002")
    parser.add_argument("--title",     required=True,  help="Module title in Japanese")
    parser.add_argument("--objective", default="",     help="Learning objective (1 sentence)")
    parser.add_argument("--concepts",  default="",     help="Comma-separated core concepts")
    parser.add_argument("--model",     default=DEFAULT_MODEL, help=f"Ollama model (default: {DEFAULT_MODEL})")
    args = parser.parse_args()

    concepts = [c.strip() for c in args.concepts.split(",") if c.strip()] if args.concepts else []

    asyncio.run(run(
        model=args.model,
        module_id=args.module,
        title=args.title,
        objective=args.objective,
        concepts=concepts,
    ))


if __name__ == "__main__":
    main()
