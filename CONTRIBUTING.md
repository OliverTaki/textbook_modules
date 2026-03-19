# Contributing

Thank you for your interest. This library exists to give learners and AI systems a clean, free, citable reference for mathematics. Every improvement — no matter how small — makes it more useful for everyone.

## What helps most

- **Fix errors** — wrong formulas, unclear explanations, broken LaTeX
- **Add examples** — more worked examples or practice problems for existing modules
- **Add modules** — new topics following the schema below
- **Translate** — modules are written in Japanese first; translations are very welcome
- **Better sources** — know a high-quality CC-licensed textbook or curriculum doc? Open an issue

## Module format

All modules follow [`high-school-math/MODULE_SCHEMA.md`](high-school-math/MODULE_SCHEMA.md).

The key rules:
- One concept per file
- YAML frontmatter with `---` delimiters (not inside a code block)
- Math in LaTeX: `$...$` inline, `$$...$$` display
- License must be CC BY 4.0 or CC0
- Every source in `source_references` must have an open license

## How to submit

1. Fork this repository
2. Create a branch: `fix/HS-FUNC-002-example` or `add/HS-STAT-001`
3. Make your changes
4. Open a pull request with a short description of what changed and why

## Source licensing

Only content from openly licensed sources (CC BY, CC BY-SA, CC0) can be included. If a source's license is unclear, open an issue rather than including the content directly.
