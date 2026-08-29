# Claude Consolidation Queue

**Document type:** Post-inventory consolidation queue  
**Status:** IN PROGRESS — first pass complete, see
`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md` (2026-08-22)
**Owner:** Claude Code + human review

## Purpose

This file identifies work that should be performed by Claude Code after
the documentation inventory is complete.

The purpose is to analyze, reconcile, and consolidate the existing
documentation without expanding the corpus unnecessarily.

## Scope

Claude Code should review the documentation areas:

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

## Required Analysis

Claude Code should identify:

1. duplicated requirements;
2. contradictory requirements;
3. obsolete statements;
4. overlapping documents;
5. unclear authority between documents;
6. missing cross-references;
7. inconsistent terminology;
8. inconsistent lifecycle states;
9. requirements that appear in multiple areas but differ in meaning;
10. documentation that should be merged rather than expanded;
11. requirements that should be promoted to authoritative specifications;
12. requirements that should remain explicitly experimental or provisional.

## Important Constraint

Do not rewrite the entire documentation corpus automatically.

Do not create large numbers of new documents merely to resolve
organizational issues.

Prefer:

1. existing authoritative documents;
2. small targeted corrections;
3. explicit cross-references;
4. consolidation of duplicates;
5. retirement of obsolete material.

## Authority Analysis

For every significant conflict, determine which document should be
authoritative.

Potential authority layers include:

- project/governance;
- scientific research;
- scientific specification;
- architecture;
- validation;
- security;
- data;
- development;
- operations;
- certification.

Do not resolve authority conflicts silently.

Record consequential decisions in the appropriate project decision log.

## Scientific Integrity

Claude Code must not invent scientific conclusions while consolidating
documentation.

Where scientific uncertainty exists, preserve it and route the issue to
the appropriate research or open-question registry.

## Security

Security requirements must not be weakened merely to simplify
documentation.

Potentially security-sensitive changes require explicit review.

## Historical Integrity

Do not silently delete historical evidence.

Where an existing document or section is obsolete, preserve the relevant
historical information when necessary and document the replacement or
retirement decision.

## Output

Claude Code should produce a concise report containing:

- contradictions found;
- duplicates found;
- authority conflicts;
- terminology inconsistencies;
- missing references;
- recommended consolidations;
- recommended retirements;
- unresolved questions;
- changes requiring human approval.

The report should distinguish clearly between:

- SAFE AUTOMATIC CHANGE;
- REVIEW REQUIRED;
- HUMAN DECISION REQUIRED.

## Human Approval

Claude Code must not autonomously make consequential scientific,
security, certification, or governance decisions.

Those decisions must remain explicitly reviewable by the project owner.

## Completion Condition

This queue is complete when:

- all major documentation areas have been reviewed;
- significant contradictions have been identified;
- duplicate requirements have been mapped;
- authority conflicts have been surfaced;
- unresolved questions have been recorded;
- proposed changes are classified by risk;
- no unexplained mass rewrite has occurred.

## Governing Principle

Consolidation should make the documentation smaller, clearer, and more
authoritative where possible.

It should not make the project appear more certain than the evidence
allows.
