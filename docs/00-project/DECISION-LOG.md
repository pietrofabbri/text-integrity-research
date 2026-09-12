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

---

## DEC-015 — Scope Decision for Multilingual Factual/Claim Validation (Unblocks Tranche 2)

### Date

2026-09-12

### Status

ACCEPTED

### Decision

`ARCHITECTURE-MAP.md` §64.3 identified KB-013 (no evidence-backed
multilingual factual-consistency option) as the blocker for drafting
`VALIDATION-ARCHITECTURE.md`. This is resolved by splitting factual
validation into two distinct capability categories rather than treating
it as one:

1. **`VALIDATE-FACTUAL-STRUCTURED`** — deterministic checks against
   `S04-fidelity-requirements.md` FID-003's explicit scope (names,
   entities, dates, quantities, units, identifiers, citations). This is
   not blocked by KB-013: it does not depend on MiniCheck- or
   mDeBERTa-style holistic factual-consistency models, only on
   per-language entity/number extraction, which is a separate (and, per
   this decision, separately tracked) evidence question.
2. **`VALIDATE-FACTUAL-CLAIM`** — claim/proposition-level consistency
   checking (`S04-fidelity-requirements.md` FID-002, the holistic
   factual-consistency territory R09 actually researched). For English,
   MiniCheck (R-0109) is a well-evidenced candidate eligible to pursue
   `CAPABILITY-ARCHITECTURE.md`'s Activation Gate. For all 12 other
   target languages, no capability may reach `VALIDATED` on this
   dimension: mDeBERTa-v3-xnli (R-0111) may be registered only as
   `EXPERIMENTAL`, explicitly ineligible for `VALIDATED` until a bridging
   study addresses its task-fit, per KB-013.
3. Per `S04-fidelity-requirements.md` FID-043 (Missing Evidence): any
   validation run for a language/capability pair without a `VALIDATED`
   `VALIDATE-FACTUAL-CLAIM` capability must report that dimension as
   `not measurable` or `unsupported`, never silently omit it or default
   to a pass.

### Rationale

FID-003's own scope is already narrower than "factual consistency" in
the general sense R09 researched — it lists concrete, largely
deterministic categories (entities, dates, quantities) distinct from
FID-002's claim/proposition-level scope. Recognizing this distinction
means KB-013's gap (which is specifically about holistic,
entailment-style factual-consistency checking) does not need to block
architecture work on the deterministic half of factual validation, which
has no comparable evidence gap. This avoids both overclaiming evidence
(adopting an unverified-task-fit model as a production default) and
unnecessarily blocking unrelated architecture work.

### Alternatives Considered

Accepting mDeBERTa-v3-xnli provisionally as `ACTIVE` for non-English
`VALIDATE-FACTUAL-CLAIM` (rejected — would violate
`CAPABILITY-ARCHITECTURE.md` §7's Activation Gate, which requires
evidence that is not solely `UNVERIFIED`, and KB-013 found exactly that:
unverified task-fit); deferring all factual-validation architecture work
until KB-013 is fully resolved (rejected — unnecessarily blocks the
deterministic half of factual validation, which is not implicated by
KB-013's finding).

### Consequences

`docs/04-architecture/VALIDATION-ARCHITECTURE.md` may now be drafted
(Tranche 2). `docs/00-project/KNOWLEDGE-BACKLOG.md` KB-013 remains open
and unresolved as a research question — this decision only unblocks the
architecture work, it does not supply the missing multilingual evidence
KB-013 describes.

### Affected Areas

`docs/04-architecture/VALIDATION-ARCHITECTURE.md` (new);
`docs/03-scientific-specification/S04-fidelity-requirements.md`
(FID-002/FID-003 distinction now load-bearing at the architecture level,
no content changed);
`docs/00-project/KNOWLEDGE-BACKLOG.md` (KB-013, unchanged, still open).

### Reversal Conditions

If a future bridging study (per KB-013's own required-action) establishes
mDeBERTa-v3-xnli's (or another candidate's) task-fit for
`VALIDATE-FACTUAL-CLAIM`, that capability may then pursue `VALIDATED`
status through the normal Activation Gate — this decision does not
permanently prohibit it, only withholds `VALIDATED` status absent that
evidence.

### Related Research

R-0109, R-0110, R-0111, R-0112.

### Related Questions

None directly tracked — this decision operationalizes KB-013 rather than
resolving a numbered open question.

---

## DEC-016 — Execute DCQ-006/007/008's 03-Scientific-Specification Propagation Now; Continue Deferring the 04-10 Portions

### Date

2026-09-12

### Status

ACCEPTED

### Decision

The owner instructed ("affrontiamola") that DCQ-006, DCQ-007 and DCQ-008 be
tackled now, rather than continuing the blanket deferral `DEC-012` (point 3)
and the DCQ items' own "Notes" sections had established. This decision
scopes that instruction narrowly rather than treating it as blanket
un-deferral:

1. The portions of DCQ-006, DCQ-007 and DCQ-008 that target
   `docs/03-scientific-specification` (`SPECIFICATION-MAP.md` §17, §19-22,
   §25-26; `S02-scientific-requirements.md`; `S04-fidelity-requirements.md`)
   are executed now. This area left structural-definition phase before this
   session began (`START-HERE.md` §3), so there is a concrete, normative
   document to edit, and `DEC-012` point 3's rationale for not touching it
   earlier no longer applies once the owner has explicitly asked to
   proceed.
2. The portions targeting `docs/04-architecture`, `docs/05-validation`,
   `docs/06-security`, and `docs/10-certification` remain deferred, because
   those areas (with the narrow exception of `CAPABILITY-ARCHITECTURE.md`,
   `DATA-MODEL.md`, `VALIDATION-ARCHITECTURE.md` per `DEC-014`/`DEC-015`,
   which already name no specific detector/model) are still in
   structural-definition phase in substance — there is no concrete
   normative document there yet that could cite a specific `R-XXXX` finding
   without pre-empting a technical choice `DEC-009` reserves for later.
3. Within `docs/04-architecture/ARCHITECTURE-MAP.md` specifically,
   DCQ-008's request that "any local validation/detection component should
   cite the specific candidate models" remains deferred: citing specific
   candidate models in that document would itself be the kind of premature
   technical commitment `ARCHITECTURE-MAP.md` §64.5 and
   `CAPABILITY-ARCHITECTURE.md`/`DATA-MODEL.md`/`VALIDATION-ARCHITECTURE.md`'s
   own "What This Document Does Not Decide" sections all explicitly
   withhold.
4. This decision does not resolve KB-008, KB-011, KB-013 or KB-014, or
   R-0022/R-0086, as open research questions — it only propagates their
   existing findings into the specification layer as required by
   `RESEARCH-MAP.md` §20's propagation rule.

### Rationale

The owner's explicit "affrontiamola" instruction is new information
`DEC-012` did not have when it chose blanket deferral; per this project's
own change-control convention (a decision may be revisited when new
evidence is identified — `S02-scientific-requirements.md` §25 — and an
explicit owner instruction qualifies), that instruction is itself the
trigger for revisiting `DEC-012`'s stance, but only for the parts of it
that are now technically actionable (03-scientific-specification).
Applying the same instruction to areas still in definition phase would not
propagate an evidenced finding into a normative requirement — it would
manufacture a normative document prematurely, which `DEC-009` and every
Tranche-3 architecture document explicitly caution against.

### Alternatives Considered

Treating "affrontiamola" as authorizing all of DCQ-006/007/008 including
their 04-10 portions (rejected — no concrete document exists yet in
05-validation/06-security/10-certification to receive a citation, and
forcing one into existence to satisfy this instruction would itself be an
invented structural decision, contrary to `NO-INVENTION-RULES.md`);
continuing `DEC-012`'s full deferral and treating "affrontiamola" as
referring only to future work (rejected — the instruction was explicit and
immediate, and the 03-scientific-specification portion is genuinely
actionable now).

### Consequences

`SPECIFICATION-MAP.md` §17, §19-22, §25-26; `S02-scientific-requirements.md`;
and `S04-fidelity-requirements.md` receive evidence-cited propagation notes
per DCQ-006/007/008 (see those documents' own change history for
specifics). DCQ-006, DCQ-007 and DCQ-008 move from `PENDING` to a
partially-executed state in `DOCUMENTATION-CHANGE-QUEUE.md`, with their
still-deferred 04-10 portions explicitly restated rather than silently
dropped.

### Affected Areas

`docs/03-scientific-specification/SPECIFICATION-MAP.md`;
`docs/03-scientific-specification/S02-scientific-requirements.md`;
`docs/03-scientific-specification/S04-fidelity-requirements.md`;
`docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md` (DCQ-006/007/008 status);
`docs/00-project/KNOWLEDGE-BACKLOG.md` (affected items' Required Action
status).

### Reversal Conditions

If any of the added propagation notes are found to assert confidence
beyond their cited `R-XXXX` evidence class, or to implicitly make a
technical choice reserved for 04-architecture/05-validation, the note
should be corrected or removed rather than left standing.

### Related Research

R-0022, R-0046 through R-0073, R-0086, R-0109 through R-0121.

### Related Questions

Q-003, Q-008.

---

## DEC-017 — Tranche 3 Reassessed Post-DCQ Propagation; Remains Premature

### Date

2026-09-12

### Status

ACCEPTED

### Decision

Following `DEC-016`'s execution, the owner selected, from a set of
proposed next steps, revisiting whether `ARCHITECTURE-MAP.md` §64.4's
Tranche 3 documents (`ANALYSIS-ARCHITECTURE.md`, `LANGUAGE-ARCHITECTURE.md`,
`TRANSFORMATION-ARCHITECTURE.md`) are now ready to draft, given that
DCQ-006/007/008's evidence has since been propagated into
`03-scientific-specification`. Reassessed against §64.1's readiness
signal, the conclusion is that Tranche 3 **remains premature**: the
propagation added evidence-cited cross-reference notes to
`SPECIFICATION-MAP.md` and related documents, but did not — and explicitly
disclaimed — assigning actual per-language, per-capability states. Those
states, not the underlying research evidence, are what Tranche 3's
documents would need to reference without inventing a capability
assignment themselves. This decision records that reassessment outcome
so it is not re-litigated from scratch later, and identifies the concrete
unblocked next step: populating real per-language/per-capability state
values in `SPECIFICATION-MAP.md` §22 (and the corresponding
`S02-scientific-requirements.md` REQ-LANG-006 evidence record) — itself a
substantive `03-scientific-specification` content decision, proposed here
as a candidate follow-up rather than begun unilaterally.

### Rationale

`ARCHITECTURE-MAP.md` §64.1's own readiness signal distinguishes evidence
existing "elsewhere in the corpus" from a document actually being drafted
against it. DCQ-006/007/008's propagation satisfied the former for
`03-scientific-specification` but not the state-assignment step Tranche 3
actually depends on. Drafting Tranche 3 now would require inventing
per-language capability states as a side effect of writing the
architecture document — exactly what §64.1, §25 (Capability Activation)
and `DEC-005` caution against.

### Alternatives Considered

Treating the DCQ-006/007/008 propagation as sufficient to begin Tranche 3
(rejected — would require inventing capability-state assignments inside
an architecture document rather than sourcing them from
`03-scientific-specification`, contrary to `NO-INVENTION-RULES.md`);
leaving the Tranche 3 blocker's description unchanged from before DEC-016
(rejected — the blocker's actual shape has narrowed now that the evidence
is propagated, and leaving the old, less precise description would
understate what is now known).

### Consequences

`ARCHITECTURE-MAP.md` §64.4 gains a `§64.4.1 Reassessment` subsection
recording this outcome. No architecture document is drafted under this
decision. The candidate follow-up (populating `SPECIFICATION-MAP.md` §22's
real per-language capability states) is proposed, not started, pending
owner direction.

### Affected Areas

`docs/04-architecture/ARCHITECTURE-MAP.md` (§64.4.1, new).

### Reversal Conditions

If the owner instead wants Tranche 3 drafted using provisional or
placeholder capability states, that would need its own explicit decision
recorded here, since it would reverse this decision's core finding that
doing so risks inventing evidence.

### Related Research

R-0022, R-0046 through R-0073, R-0086, R-0109 through R-0121.

### Related Questions

None directly — this decision concerns document-readiness sequencing, not
resolution of a numbered open question.