# textbook_modules

**A free, open-source, modular mathematics textbook — built collaboratively from the world's best open educational resources.**

---

## What is this?

This project collects open-licensed curriculum materials from around the world and assembles them into a single, structured, modular textbook hosted on GitHub.

Every module is self-contained: it covers one concept, has clear learning objectives, worked examples, practice problems, and citations to its sources. All content is CC BY 4.0 or CC0 — free to use, remix, and redistribute.

Current focus: **High School Mathematics (日本の高校数学相当)**

---

## Module Status

| module_id    | タイトル                        | ステータス   |
|--------------|---------------------------------|--------------|
| HS-FUNC-002  | 二次関数                        | in review    |
| HS-ALG-001   | 多項式の展開と因数分解          | planned      |
| HS-FUNC-001  | 関数の概念・定義域・値域        | planned      |
| HS-TRIG-001  | 三角関数の定義                  | planned      |
| HS-CALC-001  | 微分の基礎・導関数              | planned      |

Full module plan → [`MODULE_QUEUE.md`](MODULE_QUEUE.md)

---

## Repository Structure

```
textbook-modules/
  high-school-math/
    MODULE_SCHEMA.md          ← module format definition
    modules/final/            ← published modules (CC BY 4.0)
    modules/drafts/           ← work in progress
    modules/reviews/          ← review notes
    curriculum-analysis/      ← source curriculum comparisons
roles/                        ← agent role definitions (Researcher, Editor, etc.)
sources/                      ← source registries per module
MODULE_QUEUE.md               ← planned modules with priority
SOURCE_REGISTRY.md            ← all adopted sources with license info
CONTRIBUTING.md               ← how to contribute
```

---

## How It's Made

Modules are generated and reviewed by a multi-role pipeline:

**Researcher → Editor → Professor → Critical Thinker → Editor-in-Chief → PM**

Each role is defined as a plain Markdown file in `roles/`. The pipeline runs locally using [Ollama](https://ollama.com/) with open-weight models. Claude provides an external audit layer.

---

## License

All module content in `modules/final/` is released under **CC BY 4.0** unless otherwise noted in the module's frontmatter.

Source code in `scripts/` is MIT licensed.

---

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). All contributions are welcome — reviews, new problems, translations, and new modules.
