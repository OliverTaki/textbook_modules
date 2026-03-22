# textbook_modules

A database of modularized mathematics teaching content.
Openly licensed. Concept-first. Structured for reuse.

---

## What this is

A structured collection of complete instructional modules covering mathematics
from elementary school arithmetic through high school calculus and statistics.

Each module covers one concept and contains:
- Explanation of the concept
- Worked examples (minimum 2)
- Practice problems with answer keys (minimum 3)
- Problem generation rules
- Source references with license information
- Prerequisite and next-module links

Modules are not stubs. They are complete instructional units a teacher or AI system
can work from directly.

---

## Structure

```
math/
  modules/        — published modules (primary content)
  references/     — verified source reference records per module
  MODULE_SCHEMA.md
CURRICULUM_SCOPE.md
CONTRIBUTING.md
LICENSE
CHANGELOG.md
```

---

## Module format

All modules follow `math/MODULE_SCHEMA.md`.

Each module file is a Markdown document with YAML frontmatter:

```yaml
---
module_id: FUNC-002
title: 二次関数
level: high
grade: 10
license: CC BY 4.0
source_references:
  - url: https://example.org/...
    title: "..."
    license: CC BY 4.0
prerequisites:
  - FUNC-001
status: reviewed
---
```

Source references in the frontmatter point to the corresponding record in
`math/references/{module_id}/INDEX.md` where full source details are documented.

---

## Concept domains

| Prefix | Domain |
|--------|--------|
| `ELM`  | Elementary arithmetic |
| `MID`  | Middle school mathematics |
| `ALG`  | Algebra |
| `FUNC` | Functions |
| `TRIG` | Trigonometry |
| `CALC` | Calculus |
| `STAT` | Statistics & Probability |
| `GEO`  | Geometry |
| `VEC`  | Vectors |
| `SEQ`  | Sequences |
| `LOG`  | Logarithms & Exponentials |
| `COMB` | Combinatorics |
| `PROB` | Probability |
| `MATR` | Matrices |
| `CURV` | Curves & Coordinate Geometry |

Modules are identified by concept domain only — no grade-level or country encoding
in the ID. The same concept appears once, with notes where framing differs across curricula.

---

## Scope

The database currently covers elementary school through high school mathematics
following the Japanese national curriculum (学習指導要領), with curriculum
comparison notes where relevant.

See `CURRICULUM_SCOPE.md` for the full list of 101 planned modules with prerequisite links.

---

## License

All module content is **CC BY 4.0** unless otherwise noted in the module frontmatter.
Every `source_references` entry must point to a document with an open license (CC BY, CC BY-SA, or CC0).

See `LICENSE` for the full license text.

---

## Contributing

See `CONTRIBUTING.md`.
