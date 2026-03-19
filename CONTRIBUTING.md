# Contributing to textbook_modules

Thank you for your interest in contributing! This project aims to build a free, modular, open-source mathematics textbook for high school students worldwide, drawing from open educational resources (OER) across many countries.

## What We Need Help With

- **Reviewing modules** — Are the explanations clear? Are the examples good?
- **Adding problems** — More practice problems are always welcome
- **Translating** — Modules are written in Japanese first; translations to other languages are very welcome
- **New modules** — See `MODULE_QUEUE.md` for what's planned next
- **Source hunting** — Know a great CC-licensed curriculum document or textbook? Open an issue with the link

## Module Format

All modules follow `textbook-modules/high-school-math/MODULE_SCHEMA.md`.

Key rules:
- YAML frontmatter starts with raw `---` (not inside a code block)
- Math is written in LaTeX: `$...$` for inline, `$$...$$` for display
- License must be CC BY 4.0 or CC0
- All sources listed in frontmatter must be CC-compatible

## How to Contribute

1. Fork this repository
2. Create a branch: `git checkout -b fix/HS-FUNC-002-typo` or `feat/HS-STAT-001`
3. Make your changes
4. Open a Pull Request with a short description of what you changed and why

## Source Licensing

We only include content from sources with explicit open licenses (CC BY, CC BY-SA, CC0). If you are unsure about a source's license, please open an issue rather than including it directly.

## Questions?

Open an issue — all questions are welcome.
