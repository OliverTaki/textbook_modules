# Module Design Notes

This document describes the conceptual structure of a textbook module.

The schema described here is **provisional** and should evolve through real implementation.

---

## Module Concept

A module represents a **single learning unit**.

Examples:

- Solving linear equations
- Fraction addition
- Newton's second law
- Photosynthesis basics

A module should correspond to something that a learner can **understand, practice, and verify mastery of**.

---

## Module Granularity

Modules should be derived primarily from **curriculum learning objectives**, not textbook chapter divisions.

Textbooks often organize content for narrative flow rather than conceptual independence.

Using curriculum objectives helps ensure:

- consistent granularity
- cross-textbook compatibility
- clear learning outcomes

---

## Initial Schema Philosophy

The project will begin with an **intentionally verbose schema**.

The goal is to capture as much structured information as possible during early module creation.

After enough modules are implemented, the schema will be simplified by removing fields that prove unnecessary.

---

## Example Provisional Schema

This is an exploratory schema and may change.


module_id
title
subject
domain
level

learning_objective

prerequisites
next_modules

core_concepts
key_terms

common_misunderstandings

examples
exercises

source_textbooks
source_sections
license

notes
revision_history


---

## Curriculum vs Textbook Roles

### Curriculum

Defines:

- module boundaries
- learning objectives
- dependency structure

### Textbooks

Provide:

- explanations
- examples
- exercises
- diagrams

Multiple textbooks may populate a single module.

---

## Early Implementation Strategy

1. Choose one subject area.
2. Choose one curriculum standard.
3. Implement multiple modules.
4. Observe schema usage patterns.
5. Simplify schema later.

This prevents premature schema design.

---

## Future Considerations

Potential future improvements:

- module dependency graphs
- concept networks
- multiple difficulty layers
- AI-readable semantic structure