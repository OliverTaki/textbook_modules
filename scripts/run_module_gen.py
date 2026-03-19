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

SYSTEM_PROMPT = """あなたは数学の専門家であり、教科書の著者です。
必ず日本語で記述してください。英語での回答は禁止です。
数式は必ず LaTeX 記法を使用してください（インライン: $...$、ブロック: $$...$$）。
数学用語は日本語を主とし、英語を括弧書きで併記してください（例: 判別式 (discriminant)）。
既存教科書の文章を直接コピーしてはいけません。すべてオリジナルの文章で書いてください。
YAML frontmatter は必ず --- 区切りで始め、指定されたフィールドをすべて含めてください。
コードブロック（```yaml）で frontmatter を囲んではいけません。"""


def build_task(module_id: str, title: str, objective: str, concepts: list[str]) -> str:
    concepts_str = "\n".join(f"- {c}" for c in concepts) if concepts else "（スキーマ参照）"
    return f"""以下の仕様に従い、高校数学モジュールの完全な初稿を日本語で生成してください。
英語での回答は禁止です。必ず日本語で書いてください。

【出力形式】
ファイルの先頭は必ず以下の形式の YAML frontmatter で始めること（---区切り、コードブロック禁止）:

---
module_id: {module_id}
title: "{title}"
subject: mathematics
domain: functions
level: high-school
learning_objective: >
  （ここに学習目標を日本語で記述）
prerequisites:
  - HS-FUNC-001
core_concepts:
  - （コアコンセプトを列挙）
key_terms:
  - （用語を「日本語 (英語)」形式で列挙）
common_misunderstandings:
  - （よくある誤解を列挙）
source_references:
  - title: "OpenStax Algebra and Trigonometry"
    url: "https://openstax.org/books/algebra-and-trigonometry/pages/1-introduction-to-prerequisites"
    license: "CC BY 4.0"
license: "CC BY 4.0"
status: draft
---

【MODULE_ID】: {module_id}
【タイトル】: {title}
【学習目標】: {objective}
【コアコンセプト】:
{concepts_str}

【本文の必須セクション（日本語で記述）】:
1. 学習目標（箇条書き）
2. 概念説明（定義・性質・直感的説明）
3. 例題 最低2問（基礎1問・応用1問、解答付き）
4. よくある間違い 2点以上
5. 練習問題 最低3問（解答付き）
6. 次のステップ

数式は必ず LaTeX 記法で書くこと。数学用語は「日本語 (英語)」形式で併記。"""


async def run(model: str, module_id: str, title: str, objective: str, concepts: list[str]):
    PROPOSALS.mkdir(parents=True, exist_ok=True)

    task = build_task(module_id, title, objective, concepts)
    print(f"\n[{model}] Generating module: {module_id} / {title}")
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
