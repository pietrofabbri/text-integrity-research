# Decision Log

## Purpose

This document records project decisions that have been explicitly made.

It is the authoritative historical record of project decisions.

A decision must not be inferred solely from implementation.

---

# Decision States

- PROPOSED
- ACCEPTED
- SUPERSEDED
- REJECTED

---

# Decision Template

## DEC-XXX — Title

### Date

YYYY-MM-DD

### Status

ACCEPTED

### Decision

Clear statement of the decision.

### Rationale

Why the decision was made.

### Alternatives Considered

Alternative approaches.

### Consequences

Expected consequences.

### Affected Areas

Documents/components affected.

### Reversal Conditions

Conditions under which the decision should be reconsidered.

### Related Research

Research IDs.

### Related Questions

Open-question IDs.

---

# Initial Decisions

## DEC-001 — Core Runtime Must Not Depend on Generative AI Services

### Status

ACCEPTED

### Decision

The production runtime must be executable without requiring a remote
generative AI service.

### Rationale

The project requires reproducibility, predictable behavior, cost control
and independence between development-time AI assistance and runtime
execution.

### Consequences

Generative AI may be used during development and maintenance, but runtime
dependencies must be separately specified and validated.

---

## DEC-002 — External Detection Services Are Optional Evidence Sources

### Status

ACCEPTED

### Decision

External detectors may be integrated through explicit adapters but are
not part of the mandatory offline core.

### Rationale

This preserves offline operation while allowing the research and
validation framework to evaluate external evidence.

---

## DEC-003 — Capability Lifecycle Must Include Retirement

### Status

ACCEPTED

### Decision

Every production capability must have a defined lifecycle and a safe
retirement path.

### Rationale

The scientific and technical environment is expected to evolve.

---

## DEC-004 — Human Approval Is Required at Macro-Tranche Boundaries

### Status

ACCEPTED

### Decision

Human approval applies to bounded macro-tranches rather than individual
implementation actions.

### Rationale

This minimizes interruption while retaining meaningful human governance.

---

## DEC-005 — Claude Code May Not Weaken Requirements to Resolve Failures

### Status

ACCEPTED

### Decision

The autonomous development agent may modify implementation, tests or
documentation within its authority, but may not weaken normative
requirements or validation criteria merely to obtain a passing result.

---

## DEC-006 — Documentation Is a First-Class Project Artifact

### Status

ACCEPTED

### Decision

Documentation, registries, specifications and implementation must remain
traceable and mutually consistent.

---

## DEC-007 — Effectiveness Is Versioned

### Status

ACCEPTED

### Decision

Effectiveness must be evaluated through versioned capability/evaluation
profiles rather than treated as a permanent binary property.

---

## DEC-008 — Minimality Is a First-Class Quality Objective

### Status

ACCEPTED

### Decision

Where transformations are performed, unnecessary modification should be
minimized subject to the applicable validation constraints.

---

## DEC-009 — Scientific Claims Must Be Distinguished From Normative Requirements

### Status

ACCEPTED

### Decision

A research finding does not automatically become a system requirement.

A deliberate specification decision is required.

---

## DEC-010 — Project Knowledge Must Not Exist Only in Conversation

### Status

ACCEPTED

### Decision

Important knowledge discovered during project discussion must be recorded
in a persistent project artifact.

---

## DEC-011 — Duplicate S02/S03 Identifiers Resolved by Renumbering

### Date

2026-08-22

### Status

ACCEPTED

### Decision

`S02-fidelity-requirements.md` and `S03-transformation-requirements.md`
(both previously `Status: NORMATIVE / DRAFT FOR CONSOLIDATION`) are
renumbered to `S04-fidelity-requirements.md` and
`S05-transformation-requirements.md` respectively, and promoted to
`Status: NORMATIVE`. `S02-scientific-requirements.md` and
`S03-experimental-model.md` keep their existing identifiers unchanged.

### Rationale

A documentation consolidation review found two documents each claiming
`S02` and two each claiming `S03`. Content review showed the "draft"
documents cover content-preservation and transformation-minimality
requirements — boundary categories already listed in
`SPECIFICATION-MAP.md` §3 that are distinct from S02-scientific-requirements'
general requirement conversion and S03-experimental-model's measurement
framework. Renumbering (rather than merging) was chosen because the
documents are complementary, not redundant.

### Alternatives Considered

Merging the draft documents' content into `S02-scientific-requirements.md`
and `S03-experimental-model.md` and retiring the drafts. Rejected because
a full content comparison found no substantive overlap, and merging would
have produced two very large, less navigable documents.

### Consequences

Any future reference to "S02" or "S03" without a filename is ambiguous
and should be disambiguated. `SPECIFICATION-MAP.md` §44.1 now indexes all
existing S0x documents.

### Affected Areas

`docs/03-scientific-specification` (S02-fidelity-requirements.md,
S03-transformation-requirements.md, SPECIFICATION-MAP.md);
`docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md` (DCQ-005, closed).

### Related Research

None — this is a documentation-identity decision, not a research finding.

### Related Questions

None.