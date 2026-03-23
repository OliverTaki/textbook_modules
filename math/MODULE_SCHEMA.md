# Module Schema — math

A module is an **AI-readable instructional knowledge object**.

It is not a concept label, not a stub, not a student-facing page.
The body is the primary content. All other fields are supporting data.

---

## ID format

```
{BAND}-{DOMAIN}-{NNN}
```

Examples: `A-NUM-001`, `B-ALG-003`, `C-FUNC-002`

| BAND | Level |
|------|-------|
| A | Elementary (小学校相当) |
| B | Middle school (中学校相当) |
| C | High school (高校相当) |
| D | University introductory |
| E | University advanced |

Math domains:

| DOMAIN | Meaning |
|--------|---------|
| `NUM`  | Number & numeration |
| `MEAS` | Measurement |
| `OPS`  | Operations (arithmetic) |
| `ALG`  | Algebra |
| `FUNC` | Functions |
| `GEO`  | Geometry |
| `TRIG` | Trigonometry |
| `STAT` | Statistics & probability |
| `CALC` | Calculus |
| `SEQ`  | Sequences |
| `LOG`  | Logarithms & exponentials |
| `COMB` | Combinatorics |
| `MATR` | Matrices |
| `VEC`  | Vectors |

**Do not include subject name or grade level in the ID.**
Subject is determined by directory. Grade placement is metadata, not identity.

Legacy IDs (`ELM-001`, `FUNC-002`, etc.) are being migrated to this format.

---

## File naming

`{BAND}-{DOMAIN}-{NNN}.md`

Examples: `A-NUM-001.md`, `C-FUNC-002.md`

---

## YAML Frontmatter

```yaml
---
module_id: A-NUM-001
title: 数の概念と数え方
band: A
domain: NUM
concept_tags: [counting, natural-numbers, one-to-one-correspondence]
prerequisites: []
next_modules: [A-NUM-002, A-OPS-001]
source_references:
  - id: SRC-001
    title: "学習指導要領 小学校算数"
    url: "https://www.mext.go.jp/..."
    license: "CC BY"
locale_notes:
  ja-JP:
    grade: 1
    curriculum: 学習指導要領
  us-CCSS:
    grade: K
    curriculum: Common Core
language: ja
status: draft        # draft | reviewed | published
license: CC BY 4.0
---
```

**Field notes:**
- `module_id` — BAND-DOMAIN-NNN. No grade, no country code.
- `band` / `domain` — must match the ID prefix exactly.
- `concept_tags` — content keywords, not grade labels.
- `prerequisites` / `next_modules` — module-to-module links. IDs only. Learning order is managed here, not in the ID.
- `source_references` — openly licensed sources only (CC BY, CC BY-SA, CC0).
- `locale_notes` — grade placement and curriculum alignment per country. Kept separate from core content.
- `language` — current language of the body (`ja`, `en`, etc.).
- `status` — `draft` → `reviewed` → `published`.

---

## Body Structure

The body is the teaching content. It must be substantive.

```markdown
## 概念説明
[Core concept explanation. Complete and clear.
This is the primary content — do not make it a summary or stub.
Include background, formal definition, and intuitive framing.]

## 例題
### 例題1
[Full worked example with all steps shown]

### 例題2
[Second worked example — different angle, difficulty, or framing]

## 練習問題
### 問題1
[Problem statement]

**解答:** [Full answer]
**採点基準:** [What a correct answer must include]

### 問題2
...（最低3問）

## 問題生成ルール
[Rules for generating new problems of this type.
Be specific: what parameters vary, what constraints apply, what must be tested.
Example: "Vary n in 'count objects up to n'. Use n ∈ {5,10,20}. Always include
a visual grouping task and a pure counting task."]

## つまずきポイント・誤答パターン
[Common misconceptions and typical errors.
What do students get wrong and why? What does an AI tutor need to watch for?
Include correction strategies where known.]

## 教科横断・カリキュラム差異
[How this concept is framed differently across countries/curricula.
e.g. "Japan: introduced in Grade 1 with concrete objects.
US (CCSS): Kindergarten, emphasis on cardinality.
IB PYP: integrated into transdisciplinary themes."]

## 補足ノート
[Structured supplementary notes:
- Historical or cultural context
- Connections to other domains
- Notation variants
- Edge cases or boundary conditions]
```

---

## Content principles

- Body first. Metadata is supporting data.
- Substantive over brief. A thin module is worse than no module.
- Explicit over implicit. State assumptions, constraints, and edge cases.
- AI-readable. Structured for processing, not just human reading.
- Locale-separated. Country-specific framing goes in `locale_notes` and the
  カリキュラム差異 section, not in the core explanation.

---

## Data hierarchy

```
1. Module body          → PRIMARY (instructional content)
2. Source references    → where the content comes from
3. Practice problems    → worked problem items
4. Problem gen rules    → how to generate new problems
5. Scoring rules        → how answers are evaluated
6. Module links         → prerequisites / next
7. Locale/curriculum    → country/framing variations
8. Supplementary notes  → additional structured info
```

**Do not invert this.** Rich metadata with thin body defeats the purpose.

---

## Quality gate (minimum for `published` status)

- [ ] 1 file = 1 module
- [ ] Frontmatter appears exactly once
- [ ] No other module's content mixed in
- [ ] No review/verdict/log content mixed in
- [ ] No duplicate paragraphs
- [ ] No generation noise or incomplete sentences
- [ ] All required sections present
- [ ] ID references intact
