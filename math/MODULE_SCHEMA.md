# Module Schema

A module is a **modularized piece of actual teaching material**.  
It is not a concept label, not an empty knowledge node, not a policy document.  
The body is the primary object. All other fields are supporting data.

---

## YAML Frontmatter (supporting metadata)

```yaml
---
module_id: FUNC-002
title: 二次関数
domain: functions
concept_tags: [quadratic, parabola, vertex, standard-form]
prerequisites: [FUNC-001]
next_modules: [FUNC-003, CALC-001]
source_references:
  - id: SRC-001
    title: "学習指導要領 高等学校数学II"
    url: "https://www.mext.go.jp/..."
    license: "CC BY"
license: CC BY 4.0
status: draft        # draft | reviewed | published
---
```

**Field notes:**
- `module_id` — domain prefix + number only. No grade level, no country code.
- `domain` — concept domain: `functions` / `algebra` / `geometry` / `trigonometry` / `calculus` / `statistics` / `logic`
- `prerequisites` / `next_modules` — module-to-module links. IDs only.
- `source_references` — openly licensed sources only (CC BY, CC BY-SA, CC0)

---

## Body Structure (primary content)

The body is the teaching content. It must be substantive, not thin.

```markdown
## 概念説明

[The actual instructional content. Clear, complete explanation of the concept.
This is the core of the module — do not make it a summary or stub.]

## 例題

### 例題 1
[Full worked example with all steps shown]

### 例題 2
[Second worked example, different angle or difficulty]

## 練習問題

### 問題 1
[Problem statement]

**解答:** [Full answer]
**採点基準:** [What a correct answer must contain]

### 問題 2
...

### 問題 3
...

## 問題生成ルール

[Rules for generating new problems of this type.
e.g. "Vary the value of a, h, k in y=a(x-h)²+k. Ensure a≠0.
For max/min problems, use a<0 or a>0 explicitly."]

## 各国・文化的差異

[How this concept is framed differently across countries/curricula, if relevant.
e.g. "US: vertex form emphasized. Japan: standard form → vertex form conversion emphasized.
IB: both required with proof."]

## 補足ノート

[Structured supplementary notes. Common misconceptions, historical context,
connections to other domains, etc.]
```

---

## Data hierarchy

```
1. Module body          ← PRIMARY (teaching content)
2. Source references    ← where the content comes from
3. Practice problems    ← stored problem items
4. Problem gen rules    ← how to generate new problems
5. Scoring rules        ← how answers are evaluated
6. Module links         ← prerequisites / next
7. Cultural notes       ← country/framing variations
8. Wiki notes           ← supplementary structured info
```

**Do not invert this.** Rich metadata with thin teaching content defeats the purpose.

---

## File naming

`{DOMAIN}-{NNN}.md`

Examples: `FUNC-002.md`, `CALC-001.md`, `TRIG-003.md`

No country code, no grade level, no language code.
