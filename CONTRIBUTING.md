# Contributing

This database exists to give AI systems and educators a clean, open, citable
knowledge base for instructional content. Every improvement makes it more useful.

---

## How to give feedback

The primary channel for external feedback is **GitHub Issues**.

Open an issue if you find:
- A factual or mathematical error
- A curriculum discrepancy (e.g. wrong grade placement for a country)
- A concept that is missing or inadequately explained
- A structural problem (broken frontmatter, missing sections)
- A licensing concern with a source reference

Issues are reviewed before being acted on. Feedback is not automatically
incorporated — editorial judgment is applied to all suggestions.

---

## How to contribute content

1. Fork this repository
2. Create a branch: `fix/A-NUM-001-example` or `add/B-ALG-005`
3. Follow `math/MODULE_SCHEMA.md` exactly
4. Open a pull request with a short description of what changed and why

---

## Module rules

- One concept per file
- YAML frontmatter with raw `---` delimiters (not inside a code block)
- Math in LaTeX: `$...$` inline, `$$...$$` display
- License must be CC BY 4.0 or CC0
- Every `source_references` entry must have an open license (CC BY, CC BY-SA, CC0)
- Body must be substantive — not a stub or summary

---

## What this database is for

Modules are **AI-readable instructional knowledge objects**, not student-facing pages.

Good additions:
- Complete concept explanations with worked examples
- Problem generation rules
- Misconception notes and common errors
- Cross-curriculum notes (how this concept differs between Japan, US, IB, etc.)
- Verified open-licensed source references

Not needed:
- Student-facing simplifications
- Navigation UI hints
- Learning management metadata

---

## ID format

New modules should use `{BAND}-{DOMAIN}-{NNN}` format.
See `README.md` for the full BAND and DOMAIN reference table.

Legacy IDs (`ELM-001`, `FUNC-002`, etc.) are being migrated.
Do not create new modules using the legacy format.

---

## Source licensing

Only content from openly licensed sources (CC BY, CC BY-SA, CC0) can be included.
If a source's license is unclear, open an issue rather than including the content directly.
