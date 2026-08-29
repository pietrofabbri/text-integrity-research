# Claude Code — Post-Inventory Consolidation Instructions

## Status

IN PROGRESS — a first pass (Phases 1–6, scoped) is complete; see
`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md` (2026-08-22). The full
Phase 1–11 treatment, including the Q001 cross-area audit, remains open.

## Objective

Review the existing documentation corpus after completion of the inventory.

The objective is NOT to generate more documentation.

The objective is to determine whether the existing documentation is:

- internally coherent;
- non-duplicative;
- correctly layered;
- sufficiently cross-referenced;
- explicit about uncertainty;
- ready to support implementation.

## Source Areas

Review:

- `docs/00-project`
- `docs/01-governance`
- `docs/02-research`
- `docs/03-scientific-specification`
- `docs/04-architecture`
- `docs/05-validation`
- `docs/06-security`
- `docs/07-data`
- `docs/08-development`
- `docs/09-operations`
- `docs/10-certification`

Also review:

- `docs/99-backlog/POST-INVENTORY-QUEUE.md`
- `docs/99-backlog/INVENTORY-STATUS.md`
- `docs/99-backlog/CLAUDE-CONSOLIDATION-QUEUE.md`

## Phase 1 — Inventory Confirmation

Confirm that the expected documentation areas and principal files exist.

Do not create replacements for files that already exist.

## Phase 2 — Authority Mapping

Determine which document is authoritative for each major category:

- project governance;
- research methodology;
- scientific requirements;
- architecture;
- validation;
- security;
- data;
- development;
- operations;
- certification.

Record authority conflicts instead of silently resolving them.

## Phase 3 — Duplication Analysis

Identify requirements or principles repeated across documents.

For each significant duplicate determine:

- whether repetition is intentional;
- whether one occurrence should become authoritative;
- whether the other occurrence should become a reference;
- whether terminology differs.

Do not automatically delete duplicated material.

## Phase 4 — Contradiction Analysis

Search specifically for contradictions involving:

- offline operation;
- external services;
- AI-assisted development;
- autonomous work;
- human approval;
- experimental capabilities;
- certification;
- validation;
- security;
- privacy;
- data provenance;
- language support;
- model dependencies;
- dataset dependencies;
- versioning;
- lifecycle states;
- release gates.

Every consequential contradiction must be reported.

## Phase 5 — Terminology Analysis

Identify inconsistent terminology for:

- capability;
- component;
- module;
- model;
- dataset;
- benchmark;
- experiment;
- validation;
- verification;
- certification;
- release;
- experimental;
- active;
- deprecated;
- retired;
- unavailable;
- offline;
- external;
- provenance.

Do not normalize terminology automatically when the difference may represent
a real conceptual distinction.

## Phase 6 — Cross-Reference Analysis

Identify documents that clearly depend on concepts defined elsewhere but
lack an explicit reference.

Recommend cross-references rather than duplicating definitions.

## Phase 7 — Scientific Integrity

Do not manufacture scientific conclusions.

Do not convert:

- hypotheses into requirements;
- experimental observations into guarantees;
- proposed metrics into accepted metrics;
- research assumptions into validated facts.

Preserve uncertainty explicitly.

## Phase 8 — Security Boundary

Do not weaken security requirements during consolidation.

Changes involving:

- credentials;
- external transmission;
- network access;
- executable artifacts;
- subprocesses;
- plugins;
- autonomous execution;
- sensitive data;

must be classified as requiring review unless clearly mechanical and
non-semantic.

## Phase 9 — Certification Boundary

Do not imply certification merely because documentation exists.

Certification-related changes must preserve the distinction between:

- documented;
- implemented;
- tested;
- validated;
- experimentally supported;
- certified.

## Phase 10 — Proposed Changes

Classify every proposed change as:

### SAFE AUTOMATIC CHANGE

Mechanical, non-semantic, low-risk changes such as:

- typo fixes;
- formatting;
- broken internal references;
- obvious duplicate headings;
- unambiguous cross-reference additions.

### REVIEW REQUIRED

Changes affecting:

- terminology;
- document authority;
- interfaces;
- lifecycle states;
- requirements;
- validation procedures;
- operational behavior.

### HUMAN DECISION REQUIRED

Changes affecting:

- scientific claims;
- security boundaries;
- certification criteria;
- governance;
- project scope;
- major architecture;
- external data policy;
- irreversible deletion of historical material.

## Phase 11 — Minimal Modification Principle

Prefer this order:

1. leave correct material unchanged;
2. add a cross-reference;
3. correct an obvious inconsistency;
4. consolidate duplicated material;
5. retire obsolete material;
6. create a new document only when no existing document can serve the
   required purpose.

Do not perform mass rewrites.

## Phase 12 — Output

Create a report in:

`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`

The report must contain:

1. Executive Summary
2. Area-by-Area Findings
3. Authority Conflicts
4. Duplications
5. Contradictions
6. Terminology Issues
7. Missing Cross-References
8. Scientific Uncertainties
9. Security-Sensitive Findings
10. Certification-Sensitive Findings
11. Proposed Automatic Changes
12. Proposed Review Changes
13. Human Decisions Required
14. Recommended Next Actions

## Change Discipline

Before modifying any substantive document:

- identify the exact reason;
- identify the affected authority;
- identify dependent documents;
- classify the change;
- preserve historical information where appropriate.

Do not silently rewrite large documents.

## Completion Criterion

The task is complete when the report gives the human reviewer enough
information to decide what should actually change.

The report is the primary output.

The absence of a proposed change is acceptable.

## Final Principle

The purpose of consolidation is to reduce ambiguity, not to increase the
size of the documentation corpus.

A smaller coherent documentation set is preferable to a larger redundant one.
