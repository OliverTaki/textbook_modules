# Module Schema

Every module is a single Markdown file with YAML frontmatter followed by body content.

---

## YAML Frontmatter

```yaml
---
module_id: FUNC-002
title: 二次関数
subject: mathematics
domain: functions          # algebra / functions / geometry / trigonometry / calculus / statistics / logic
concept_tags: [quadratic, parabola, vertex]
learning_objective: "放物線の性質を理解し、二次関数のグラフを描き、最大・最小問題を解くことができる。"
prerequisites: [FUNC-001]
next_modules: [FUNC-003, CALC-001]
core_concepts: [放物線, 頂点形式, 標準形, 判別式]
key_terms:
  - term: 頂点
    definition: "放物線の最高点または最低点"
common_misunderstandings:
  - "x^2 の係数の符号と開口方向の混同"
source_references:
  - id: SRC-001
    title: "学習指導要領 高等学校数学"
    url: "https://www.mext.go.jp/..."
    license: "CC BY"
license: CC BY 4.0
status: draft           # draft / reviewed / published
---
```

### Field notes

- `module_id` — domain prefix + number, no grade or country encoding (e.g. `FUNC-002`, not `HS-JP-FUNC-002`)
- `domain` — concept-based grouping, not curriculum-based
- `concept_tags` — free tags for cross-linking and AI retrieval
- `source_references` — only openly-licensed sources (CC BY, CC BY-SA, CC0)
- `status` — `draft` until reviewed; `published` once merged to main

---

## Body structure

```markdown
## 学習目標

## 概念説明

## 例題

### 例題 1
### 例題 2

## よくある間違い

## 練習問題

## 次のステップ
```

---

## Naming convention

`{DOMAIN}-{NNN}.md`

Examples: `FUNC-002.md`, `CALC-001.md`, `TRIG-003.md`

No country code, no grade level, no language code in the filename.
