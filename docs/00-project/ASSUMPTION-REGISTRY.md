# Assumption Registry

## Purpose

This registry records assumptions on which design or scientific decisions
depend.

An assumption is not a fact.

An assumption must be explicitly challengeable and, where practical,
validated.

---

# Statuses

- ACTIVE
- VALIDATED
- CHALLENGED
- INVALIDATED
- SUPERSEDED

---

# Confidence

- LOW
- MEDIUM
- HIGH

---

# Template

## A-XXX — Title

### Assumption

Statement.

### Basis

Why this assumption currently appears reasonable.

### Confidence

LOW / MEDIUM / HIGH

### Impact If False

What breaks or changes.

### Validation Method

How it can be tested.

### Related Research

Research IDs.

### Related Decisions

Decision IDs.

### Status

ACTIVE

---

# Initial Assumptions

## A-001 — External Detector Results Are Not Universal Ground Truth

### Assumption

A detector's result should be interpreted as evidence produced under
its own methodology rather than as an absolute statement about authorship
or text origin.

### Confidence

HIGH

### Validation Method

Comparative evaluation across detector families and controlled corpora.

### Status

ACTIVE

---

## A-002 — Scientific Coverage Will Remain Incomplete

### Assumption

No finite project release can guarantee coverage of every possible future
watermark, provenance mechanism or detection methodology.

### Confidence

HIGH

### Impact If False

Low. The assumption mainly governs how claims are formulated.

### Status

ACTIVE

---

## A-003 — Modularity Reduces Future Update Cost

### Assumption

Explicit component boundaries, registries and interfaces will make future
capability additions and removals safer than tightly coupled implementation.

### Confidence

HIGH

### Validation Method

Architectural dependency analysis and lifecycle exercises.

### Status

ACTIVE