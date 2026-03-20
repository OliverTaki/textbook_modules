# textbook_modules

A database of modularized teaching content — organized by concept, openly licensed, built to be reused.

---

## What this is

A structured collection of actual teaching material, broken into self-contained modules.

Each module contains real instructional content: explanation, worked examples, practice problems, scoring notes, and problem-generation rules. The goal is a database that can support problem generation, assessment, curriculum mapping, and cultural comparison — but those are downstream uses. The current task is building the content database itself.

---

## What a module is

A module is a modularized piece of actual teaching material.

It is not:
- a concept label
- an empty knowledge node
- a metadata stub with thin content

It is a complete unit of instruction covering one concept, with enough content to teach from directly.

---

## Data structure

```
math/
  modules/        ← published modules (primary content)
  references/     ← source curriculum documents
  MODULE_SCHEMA.md
```

Inside each module, the data hierarchy is:

| Priority | Data | Description |
|---|---|---|
| 1 | Teaching content | The module body — explanation, examples |
| 2 | Source references | Where the content comes from |
| 3 | Practice problems | Stored problem items with answers |
| 4 | Problem gen rules | How to generate new problems |
| 5 | Scoring rules | How answers are evaluated |
| 6 | Module links | Prerequisites and next modules |
| 7 | Cultural notes | Country/framing variations |
| 8 | Wiki notes | Supplementary structured information |

**Modules are primary. All other data is secondary.**

---

## Concept domains

| Prefix | Domain |
|---|---|
| `FUNC` | Functions |
| `ALG` | Algebra |
| `TRIG` | Trigonometry |
| `CALC` | Calculus |
| `STAT` | Statistics & Probability |
| `GEO` | Geometry |
| `VEC` | Vectors |
| `LOGIC` | Logic & Proof |

Modules are identified by concept domain only — no grade level, no country encoding.

---

## Module status

| Module ID | Concept | Status |
|---|---|---|
| FUNC-002 | 二次関数 | reviewed |
| ALG-001 | 多項式の展開と因数分解 | in progress |
| FUNC-001 | 関数の概念・定義域・値域 | planned |
| TRIG-001 | 三角関数の定義 | planned |
| CALC-001 | 微分の基礎・導関数 | planned |
| ALG-002 | 方程式と不等式 | planned |
| GEO-001 | 平面図形の基礎・合同と相似 | planned |
| CALC-002 | 積分の基礎・面積計算 | planned |
| VEC-001 | ベクトルの基礎・演算 | planned |
| STAT-001 | 確率の基礎・事象と確率 | planned |

---

## License

All module content is **CC BY 4.0** unless otherwise noted in the module frontmatter.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).
