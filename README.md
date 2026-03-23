# textbook_modules

An open database of modular instructional knowledge, designed for AI systems.

Openly licensed. Concept-first. Structured for reuse across subjects and curricula.

---

## What this is

`textbook_modules` is an **AI-readable instructional knowledge database**.

This is not a student-facing textbook and not a finished learning app.
It is a structured collection of knowledge objects that AI systems can use to:
- Generate explanations and worked examples
- Create and score practice problems
- Compare concepts across curricula and cultures
- Sequence learning pathways via prerequisite graphs
- Translate and localize instructional content

Each module is one concept — complete enough to be useful, structured enough to be processed.

---

## Scope

**Current subject: `math/`** — elementary through high school mathematics.

This repository is designed for cross-subject expansion.
Future subjects may include physics, chemistry, history, language, and others.
Each subject gets its own directory. The structure and schema principles are shared.

---

## Structure

```
math/
  modules/         published modules
  references/      verified source reference records per module
  MODULE_SCHEMA.md
CURRICULUM_SCOPE.md
CONTRIBUTING.md
CHANGELOG.md
LICENSE
```

---

## Module format

All modules follow `math/MODULE_SCHEMA.md`.

YAML frontmatter + structured Markdown body. The body is the primary object.

Current modules are written in **Japanese** (the primary working language).
English is the planned canonical language for future modules.
Locale-specific framing (grade placement, curriculum terminology) is kept
in a separate section and not mixed into the core concept explanation.

---

## ID format

Current modules use a legacy format (`ELM-001`, `FUNC-002`, etc.).

Modules are being migrated to:

```
{BAND}-{DOMAIN}-{NNN}
```

| BAND | Level |
|------|-------|
| A | Elementary |
| B | Middle school |
| C | High school |
| D | University introductory |
| E | University advanced |

Domain examples for math: `NUM`, `MEAS`, `ALG`, `FUNC`, `GEO`, `STAT`, `CALC`

Subject is identified by directory (`math/`, `physics/`...), not by ID prefix.

---

## Feedback and contributions

External feedback is welcome via **GitHub Issues**.

If you find a factual error, a missing concept, a curriculum discrepancy,
or a structural problem in any module, please open an issue.

Issues are reviewed and triaged before being incorporated.
Not all feedback will be accepted as-is — editorial judgment is applied.

For contribution guidelines, see `CONTRIBUTING.md`.

---

## License

All module content is **CC BY 4.0** unless otherwise noted in the module frontmatter.
Every `source_references` entry must point to a document with an open license (CC BY, CC BY-SA, or CC0).

See `LICENSE` for the full license text.
