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

---

## DEC-012 — Disposition of Q001 Audit's Human-Decision-Required Items

### Date

2026-08-29

### Status

ACCEPTED

### Decision

Four items the Q001 cross-area audit left as HUMAN DECISION REQUIRED
(`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`, SECOND PASS, §13S) are
resolved as follows:

1. **Vocabulary reconciliation timing** (lifecycle-state
   `SPECIFICATION-MAP.md` §5 / `S02-scientific-requirements.md` §24;
   network-mode `SECURITY-MAP.md` §14 / `OPERATIONS-MAP.md` §136;
   release-status `VALIDATION-MAP.md` §57 / `CERTIFICATION-MAP.md` §3):
   deferred until 04-architecture through 10-certification leave
   structural-definition phase. The cross-references added 2026-08-29
   stand as the interim state — divergence documented and traceable, not
   unified.
2. **Release-readiness checklists and human-approval-gate lists**
   (`OPERATIONS-MAP.md` §183, `DATA-MAP.md` §117,
   `DEVELOPMENT-MAP.md` §108, `CERTIFICATION-MAP.md` §149;
   `SECURITY-MAP.md` §19/§77, `DEVELOPMENT-MAP.md` §14/§20): remain
   separate, area-specific documents, cross-referenced rather than
   consolidated into a single authoritative list.
3. **DCQ-007 execution timing** (non-native-writer detection bias
   R-0022; base-rate/prevalence argument for FPR R-0086): remains
   `PENDING`, matching DCQ-006's treatment — deferred until the relevant
   03-10 areas are past definition phase, including
   03-scientific-specification despite that area already being out of
   structural-definition phase generally.
4. **`docs/03-scientific-specification/_to_delete/` housekeeping** (the
   two superseded S02/S03 files parked there 2026-08-22): left in place
   indefinitely as an informal historical record. No removal required by
   any project rule.

### Rationale

All four choices match the audit report's own recommendations
(§14S), given as the owner's explicit answer to a direct question rather
than inferred from proceeding silently, per this log's own rule that "a
decision must not be inferred solely from implementation."

### Alternatives Considered

For (1): reconciling now, or declaring the vocabularies permanently
distinct. For (2): consolidating into single authoritative documents now.
For (3): executing DCQ-007 immediately against
03-scientific-specification, which — unlike 04-10 — is already past
definition phase. For (4): scheduling manual deletion, or reminding the
owner to do so later. All rejected in favor of deferral/status quo, to
avoid document churn while 04-10 are still being drafted.

### Consequences

No further action needed on these four items until 04-10 leave
definition phase. The cross-references added 2026-08-29 remain the
authoritative record of the known divergence in the meantime.

### Affected Areas

`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md` (§13S/§14S);
`docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md` (DCQ-007, stays PENDING).

### Related Research

R-0022, R-0086.

### Related Questions

None — this decision concerns audit-finding disposition, not a tracked
open question.

---

## DEC-013 — R09 (Local Deployment Feasibility Research) Confirmed as a New Research Domain

### Date

2026-09-12

### Status

ACCEPTED

### Decision

`docs/02-research/R09-local-deployment-feasibility-research.md`, written to
answer `OPEN-QUESTIONS.md` Q-008's confirmed research gap, is accepted as a
permanent ninth research domain under the identifier `R09`. Its addition
to `RESEARCH-MAP.md`'s domain diagram (§2) and domain-status table (§34) is
now confirmed, not proposed. The document's own status is changed from
`PROPOSED` to `ACTIVE`.

### Rationale

The owner approved the proposal as presented (`RESEARCH-MAP.md` §38,
2026-09-12), matching this project's own recommendation that R09 was the
best-supported option given the depth and citation quality of the research
already completed (20 sources, R-0102-R-0121, each independently verified
against primary repository/benchmark sources). No structural alternative
(merging into an existing R0x domain, or scoping it differently) was
requested.

### Alternatives Considered

Per `RESEARCH-MAP.md` §38's original proposal: merging these findings into
an existing domain (rejected — the findings are project-specific
deployment-engineering questions, not literature review of the kind R01-R08
perform, per §2 of the R09 document itself); leaving the findings
unstructured in the registry alone (rejected — would violate
`RESEARCH-MAP.md` §4's requirement that research domains have a defined
relationship to the rest of the project).

### Consequences

`RESEARCH-MAP.md` §2 and §34 are updated to include R09 as a confirmed
domain. `docs/00-project/OPEN-QUESTIONS.md` Q-008,
`docs/00-project/KNOWLEDGE-BACKLOG.md` KB-007/KB-013/KB-014/KB-015, and
`docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md` DCQ-008 are updated to
refer to R09 as confirmed rather than proposed. No document's substantive
findings changed as a result of this decision — only their status
language.

### Affected Areas

`docs/02-research/RESEARCH-MAP.md`;
`docs/02-research/R09-local-deployment-feasibility-research.md`;
`docs/00-project/OPEN-QUESTIONS.md` (Q-008);
`docs/00-project/KNOWLEDGE-BACKLOG.md` (KB-007, KB-013, KB-014, KB-015);
`docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md` (DCQ-008).

### Reversal Conditions

If a future review finds R09's scope should be merged, split, or
retired, that would itself require a new decision (per RESEARCH-MAP.md
§29, Deprecation) rather than a silent edit.

### Related Research

R-0102 through R-0121.

### Related Questions

Q-008.

---

## DEC-014 — 04-Architecture Begins Exiting Definition Phase (Tranche 1)

### Date

2026-09-12

### Status

ACCEPTED

### Decision

The owner approved the Tranche 1 plan proposed in
`docs/04-architecture/ARCHITECTURE-MAP.md` §64. Two new architecture
sub-documents are created: `docs/04-architecture/CAPABILITY-ARCHITECTURE.md`
(formalizing `ARCHITECTURE-MAP.md` §23-26) and
`docs/04-architecture/DATA-MODEL.md` (formalizing `ARCHITECTURE-MAP.md`
§32-33). 04-architecture is no longer a single-MAP-document area.

### Rationale

Both documents formalize generic mechanisms (a capability record schema
and lifecycle state machine; a data/model layer interface contract) that
do not depend on which specific detector, watermark scheme, model or
algorithm the project eventually adopts — matching `ARCHITECTURE-MAP.md`
§64.1's readiness criterion and `ARCHITECTURE-MAP.md` §2's principle that
no single algorithm should define the architecture. Neither document
selects a specific technical component; both explicitly list what they do
not decide (`CAPABILITY-ARCHITECTURE.md` §15, `DATA-MODEL.md` §12).

### Alternatives Considered

Per `ARCHITECTURE-MAP.md` §64: drafting `VALIDATION-ARCHITECTURE.md`
instead or in addition (deferred to Tranche 2 — still blocked on a scoping
decision for KB-013's multilingual factual-consistency gap); drafting
`ANALYSIS-ARCHITECTURE.md` or `LANGUAGE-ARCHITECTURE.md` (deferred to
Tranche 3 — premature until DCQ-006/007/008 resolve per-language
capability-state questions); doing no architecture work until 03-10
fully resolve their pending items (rejected — Tranche 1's two documents
do not depend on those resolutions).

### Consequences

`docs/04-architecture/ARCHITECTURE-MAP.md` §58 and §62 are updated to
record that these two documents now exist. `docs/00-project/START-HERE.md`
should be corrected the next time it is revised, since its "04-architecture
through 10-certification" summary line no longer accurately describes
04-architecture specifically. Tranche 2 (`VALIDATION-ARCHITECTURE.md`)
and Tranche 3 remain not started, pending the scoping decisions
`ARCHITECTURE-MAP.md` §64.3-§64.4 describe.

### Affected Areas

`docs/04-architecture/ARCHITECTURE-MAP.md` (§58, §62);
`docs/04-architecture/CAPABILITY-ARCHITECTURE.md` (new);
`docs/04-architecture/DATA-MODEL.md` (new);
`docs/00-project/START-HERE.md` (now stale on this point).

### Reversal Conditions

If either document is found to have implicitly made a technical decision
it disclaims (contrary to its own §15/§12 respectively), that content
should be removed and, if a real decision is needed, recorded separately
in this log rather than left implicit in an architecture document.

### Related Research

R-0102 through R-0121 (illustrative examples only, per both documents'
explicit non-adoption disclaimers).

### Related Questions

None directly — this decision concerns architecture-document creation,
not resolution of a tracked open question.