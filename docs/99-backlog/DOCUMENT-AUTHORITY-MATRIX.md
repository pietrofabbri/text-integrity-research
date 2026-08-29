# Document Authority Matrix

**Document type:** Documentation authority and precedence matrix
**Status:** ACTIVE
**Purpose:** Prevent contradictory interpretation during automated review

## Purpose

This document defines which documentation area should be treated as the
primary authority for different classes of information.

The matrix is an interpretation boundary for automated agents.

It does not create new scientific or engineering requirements.

## Authority Matrix

| Subject | Primary Authority | Supporting Areas |
|---|---|---|
| Project scope and identity | `docs/00-project` | all areas |
| Governance and decision authority | `docs/01-governance` | `00-project` |
| Research methodology and literature | `docs/02-research` | `03-scientific-specification`, `10-certification` |
| Scientific objectives and requirements | `docs/03-scientific-specification` | `02-research`, `04-architecture`, `05-validation` |
| System architecture | `docs/04-architecture` | `03-scientific-specification`, `06-security`, `07-data`, `09-operations` |
| Validation and verification | `docs/05-validation` | `03-scientific-specification`, `06-security`, `10-certification` |
| Security boundaries and controls | `docs/06-security` | `04-architecture`, `07-data`, `08-development`, `09-operations` |
| Data architecture, provenance and lifecycle | `docs/07-data` | `02-research`, `04-architecture`, `06-security`, `09-operations` |
| Development process and engineering workflow | `docs/08-development` | `00-project`, `06-security`, `05-validation` |
| Runtime operation and deployment | `docs/09-operations` | `04-architecture`, `06-security`, `07-data` |
| Certification and scientific certification state | `docs/10-certification` | `02-research`, `05-validation`, `06-security` |
| Post-inventory unresolved issues | `docs/99-backlog` | relevant authoritative area |

## Interpretation Rule

A supporting document must not silently override the primary authority
for a subject.

If a supporting document appears to contradict the primary authority:

1. do not guess which statement is correct;
2. record the contradiction;
3. identify both locations;
4. classify the issue;
5. request or record the required human decision.

## Cross-Area Requirements

Some requirements legitimately span multiple authorities.

Examples include:

- security requirements affecting architecture;
- data requirements affecting operations;
- scientific requirements affecting validation;
- validation requirements affecting certification;
- development controls affecting security.

In these cases, preserve the relationship between the documents rather
than copying the entire requirement into every area.

## Explicit Exceptions

This matrix does not imply that every statement inside a primary area is
automatically correct.

Authority means:

> "This is the first place to resolve the question."

It does not mean:

> "Every statement here is scientifically validated."

## Research vs Requirement

Research documents may establish:

- evidence;
- hypotheses;
- literature findings;
- methodological considerations;
- known limitations.

They do not automatically establish product requirements.

Requirements must be identified in the appropriate specification or
governance layer.

## Experimental vs Validated

Experimental documentation must not be interpreted as validated merely
because it exists in the repository.

The agent must preserve explicit status distinctions.

## Certification

Certification documentation must not be used to infer that a capability
is certified unless the certification state and evidence explicitly support
that conclusion.

## Missing Authority

If no area clearly owns a subject:

- do not invent an authority;
- record the gap in the consolidation report;
- recommend the smallest appropriate resolution.

## Historical Documents

Backup files, `.bak` files, and historical snapshots are not automatically
authoritative.

They may provide historical evidence.

They must not silently replace the current document.

## Final Rule

When authority is ambiguous, ambiguity is itself a finding.

Never resolve an authority conflict by assumption.
