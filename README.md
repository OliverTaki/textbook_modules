# textbook_modules

A free, open-licensed, modular library of mathematics content — built from the world's best open educational resources.

Every module is a self-contained Markdown file covering one concept: what it is, why it matters, worked examples, and practice problems. The format is designed so that humans and AI systems can read, reference, and build on it equally well.

---

## Why this exists

When someone asks an AI to help them learn mathematics, the AI draws on whatever it was trained on — which may be incomplete, inconsistent, or locked behind copyright. This library aims to be a clean, citable, openly-licensed reference that anyone (or any AI) can use freely.

---

## Coverage

**Current: High School Mathematics**

| Module ID | Topic | Status |
|---|---|---|
| HS-FUNC-001 | 関数の概念・定義域・値域 | planned |
| HS-FUNC-002 | 二次関数 | in progress |
| HS-ALG-001 | 多項式の展開と因数分解 | planned |
| HS-TRIG-001 | 三角関数の定義 | planned |
| HS-CALC-001 | 微分の基礎・導関数 | planned |

Elementary and middle school mathematics will follow.

---

## Module format

Each module is a single Markdown file with YAML frontmatter.

```yaml
---
module_id: HS-FUNC-002
title: 二次関数
subject: mathematics
level: high-school
learning_objective: "..."
prerequisites: [HS-FUNC-001]
license: CC BY 4.0
source_references: [...]
---
```

Full schema: [`high-school-math/MODULE_SCHEMA.md`](high-school-math/MODULE_SCHEMA.md)

---

## Sources

All content is drawn from openly-licensed curriculum documents and textbooks (CC BY, CC BY-SA, or CC0). Source details are recorded in each module's frontmatter.

Curriculum reference used for scope and sequencing: [`high-school-math/CURRICULUM_COMPARISON.md`](high-school-math/CURRICULUM_COMPARISON.md) — a comparison of high school mathematics curricula from 10 countries and the IB.

---

## License

All module content is **CC BY 4.0** unless otherwise noted in the module's frontmatter. You are free to use, share, and adapt with attribution.

---

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Contributions of any kind are welcome: corrections, new problems, translations, new modules, or better source references.
