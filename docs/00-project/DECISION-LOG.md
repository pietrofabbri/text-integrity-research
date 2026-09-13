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

---

## DEC-018 — Per-Language Capability-State Assignment Populated in SPECIFICATION-MAP.md §22.1

### Date

2026-09-12

### Status

ACCEPTED

### Decision

The owner approved (`"va bene se procedi con quello"`) the candidate
follow-up `DEC-017` identified: populating real per-language,
per-capability state values in `SPECIFICATION-MAP.md` §22, grounded in
the evidence DCQ-006/007/008 already propagated (`DEC-016`). This is now
done as `SPECIFICATION-MAP.md` §22.1, covering three capabilities with
sufficient per-language literature detail: AI-generated-text detection,
watermarking, and factual/claim-consistency validation
(`VALIDATE-FACTUAL-CLAIM`, per `DEC-015`). Semantic-similarity validation
is explicitly excluded from this assignment: the available evidence
(R-0103/R-0106) supports a general multilingual capability claim but was
not found broken down per specific target language, and assigning 13
differentiated states for it would invent detail the evidence does not
contain — this is recorded in §22.1 as a scope limitation, not silently
defaulted.

Every assigned state is `RESEARCH_ONLY` or `NOT_SUPPORTED` only —
`EXPERIMENTAL`, `VALIDATED`, `ACTIVE`, `DEGRADED`, `DEPRECATED` and
`RETIRED` all describe a capability's standing *within this project*,
which does not yet exist for anything in the table (no capability has
been implemented or run through `CAPABILITY-ARCHITECTURE.md`'s Activation
Gate). This follows `KNOWLEDGE-BACKLOG.md` KB-008's own original proposal.
For factual/claim-consistency specifically, the 12 non-English languages
are marked `NOT_SUPPORTED` rather than `RESEARCH_ONLY`, even though a
candidate model (mDeBERTa-v3-xnli, R-0111) exists, because its task-fit is
itself unverified and `KNOWLEDGE-BACKLOG.md` KB-013 found no
evidence-backed option exists for those languages — a candidate existing
is not the same as an evidence-backed capability existing.

### Rationale

`ARCHITECTURE-MAP.md` §64.4.1 (`DEC-017`) identified this exact gap as
the actual prerequisite for Tranche 3 architecture documents, and framed
it as a distinct, substantive content decision requiring explicit owner
direction before being started — which the owner then gave. Doing this
now, using only the two states that require no project-level
implementation evidence (`RESEARCH_ONLY`/`NOT_SUPPORTED`), keeps the
assignment strictly within what the already-registered research supports,
consistent with `NO-INVENTION-RULES.md` and `DEC-005` (requirements must
not be weakened, nor evidence overstated, to obtain a result).

### Alternatives Considered

Assigning `EXPERIMENTAL` states to the strongest candidates (e.g. English
factual-consistency via MiniCheck, or Japanese detection via R-0057)
(rejected — `EXPERIMENTAL` per `CAPABILITY-ARCHITECTURE.md`'s lifecycle
implies a project-registered candidate under evaluation, which does not
yet exist for anything in this project); marking mDeBERTa-v3-xnli's 12
non-English languages `RESEARCH_ONLY` since a candidate model is
documented (rejected — would overstate KB-013's own finding that no
evidence-backed option exists, conflating "a candidate exists" with "the
capability is evidenced"); including a semantic-similarity row using
general multilingual claims applied uniformly across all 13 languages
(rejected — would invent per-language detail the cited evidence, R-0103/
R-0106, does not contain).

### Consequences

`SPECIFICATION-MAP.md` §22.1 (new) and `S02-scientific-requirements.md`
REQ-LANG-006 are updated. `ARCHITECTURE-MAP.md` §64.4.1's identified
prerequisite for Tranche 3 is now partially satisfied for two of its
three capability families (detection, watermarking) and the factual-
consistency family already had architecture-level treatment via
`DEC-015` — whether this is now sufficient to reopen Tranche 3 readiness
is a separate question, not decided here, and should be assessed
explicitly if and when Tranche 3 is next considered.

### Affected Areas

`docs/03-scientific-specification/SPECIFICATION-MAP.md` (§22.1, new);
`docs/03-scientific-specification/S02-scientific-requirements.md`
(REQ-LANG-006).

### Reversal Conditions

Any cell in §22.1 should be revised (not silently left stale) once: (a)
a capability is actually registered and evaluated under
`CAPABILITY-ARCHITECTURE.md`'s Activation Gate for that language, moving
it beyond `RESEARCH_ONLY`/`NOT_SUPPORTED`; or (b) new research evidence is
registered that changes a language's evidence tier (e.g. a dedicated
watermarking study for a currently `NOT_SUPPORTED` language, or a
bridging study resolving mDeBERTa-v3-xnli's task-fit per KB-013's required
action).

### Related Research

R-0019, R-0021, R-0046 through R-0073, R-0109 through R-0118.

### Related Questions

Q-003, Q-008.

---

## DEC-019 — Tranche 3 Re-Reassessed Post-DEC-018: ANALYSIS-ARCHITECTURE.md and LANGUAGE-ARCHITECTURE.md Now Structurally Ready; TRANSFORMATION-ARCHITECTURE.md Still Premature

### Date

2026-09-13

### Status

ACCEPTED

### Decision

Following the owner's approval to proceed with `DEC-017`'s identified
follow-up (executed as `DEC-018`), the owner asked that Tranche 3
readiness be reassessed a second time. Re-running `ARCHITECTURE-MAP.md`
§64.1's readiness test against `SPECIFICATION-MAP.md` §22.1's new
per-language state assignments:

1. **`ANALYSIS-ARCHITECTURE.md`** and **`LANGUAGE-ARCHITECTURE.md`**:
   their specific blocker (no per-language/per-capability state
   assignments existed for detection or watermarking) is now resolved by
   `DEC-018`. Both are reassessed as **structurally ready to draft** —
   as generic-mechanism documents that reference `SPECIFICATION-MAP.md`
   §22.1 for current per-language readiness, in the same non-invention
   style as `CAPABILITY-ARCHITECTURE.md`/`DATA-MODEL.md`/
   `VALIDATION-ARCHITECTURE.md`.
2. **`TRANSFORMATION-ARCHITECTURE.md`** remains premature: it needs
   validation families with actual `VALIDATED` capabilities to check
   transformations against, not merely a documented default state.
   `DEC-018` assigned only `RESEARCH_ONLY`/`NOT_SUPPORTED` states, by
   design, because no capability in this project has been implemented or
   passed `CAPABILITY-ARCHITECTURE.md`'s Activation Gate. This is a
   different kind of blocker than `ANALYSIS-ARCHITECTURE.md`'s, and no
   documentation update can resolve it — only actual implementation and
   evaluation work can.
3. Per `DEC-004` (human approval required at macro-tranche boundaries)
   and this project's practice for Tranches 1-2, this decision records
   the reassessment only. Drafting `ANALYSIS-ARCHITECTURE.md` and
   `LANGUAGE-ARCHITECTURE.md` requires a further, separate owner
   confirmation before it begins.

### Rationale

§64.1's readiness signal turns on whether drafting a document would
require inventing capability-specific choices the evidence does not
support. `DEC-018` closed exactly the gap `DEC-017` identified for two of
the three Tranche 3 documents. The third document's blocker was
mischaracterized as the same gap in the original §64.4 text but is
actually a distinct, deeper dependency (on actual capability validation,
not on documented per-language defaults) — this decision corrects that
distinction explicitly rather than letting it stay conflated.

### Alternatives Considered

Treating all of Tranche 3 as unblocked together (rejected —
`TRANSFORMATION-ARCHITECTURE.md`'s dependency is not satisfied by
`DEC-018` and treating it as such would misrepresent what `RESEARCH_ONLY`/
`NOT_SUPPORTED` states actually mean); treating none of Tranche 3 as
unblocked, deferring re-evaluation further (rejected — would ignore that
`ANALYSIS-ARCHITECTURE.md`/`LANGUAGE-ARCHITECTURE.md`'s specific,
narrower blocker is genuinely resolved).

### Consequences

`ARCHITECTURE-MAP.md` §64.4 gains a `§64.4.2 Second Reassessment`
subsection. No document is drafted under this decision — drafting
`ANALYSIS-ARCHITECTURE.md`/`LANGUAGE-ARCHITECTURE.md` awaits explicit
owner confirmation, to be sought next.

### Affected Areas

`docs/04-architecture/ARCHITECTURE-MAP.md` (§64.4.2, new).

### Reversal Conditions

If, once drafting is attempted, either document turns out to require an
undocumented technical choice after all, that finding should be recorded
here and the document's readiness downgraded rather than drafted anyway.

### Related Research

R-0022, R-0046 through R-0073, R-0086, R-0109 through R-0121.

### Related Questions

None directly — this decision concerns document-readiness sequencing.

---

## DEC-020 — Tranche 3a Executed: ANALYSIS-ARCHITECTURE.md and LANGUAGE-ARCHITECTURE.md Drafted

### Date

2026-09-13

### Status

ACCEPTED

### Decision

The owner confirmed drafting (`"vai"`), the macro-tranche-boundary
confirmation `DEC-019` said would be sought separately. Two new
architecture sub-documents are created:

1. **`docs/04-architecture/ANALYSIS-ARCHITECTURE.md`** — formalizes
   `ARCHITECTURE-MAP.md` §9-12 (Analysis Layer, Watermark Analysis,
   AI-Generated-Text Assessment, Provenance Analysis). Gives concrete
   architectural treatment to watermark analysis and AI-generation
   assessment (both grounded in `SPECIFICATION-MAP.md` §22.1's
   per-language states) and to provenance analysis (for which it
   explicitly records the absence of any comparable per-language or even
   general evidence, rather than inventing one). Implements
   `S02-scientific-requirements.md` §27 (Scientific Ground-Truth Rule) as
   an architectural output-category tag, and cross-analyzer independence
   per `ARCHITECTURE-MAP.md` §2 and REQ-DET-005/006.
2. **`docs/04-architecture/LANGUAGE-ARCHITECTURE.md`** — formalizes
   `ARCHITECTURE-MAP.md` §34-35 (Language Architecture, Language
   Capability Registry). Defines a language-centric registry view that is
   explicitly *derived* from `CAPABILITY-ARCHITECTURE.md` §10's
   capability-centric per-language states, not a second place where those
   states are recorded — avoiding the kind of duplicated bookkeeping
   `ARCHITECTURE-MAP.md` §57 (No Hidden Scientific State) and
   `DATA-MAP.md` §94 already caution against. Also formalizes tokenizer/
   script-level risk factors (R-0044/R-0049/R-0062/R-0071) as a distinct,
   non-substitutable category from capability-level evidence.

Neither document selects any specific detector, watermark scheme,
tokenizer, or model — both follow the same non-invention discipline as
`CAPABILITY-ARCHITECTURE.md`, `DATA-MODEL.md` and
`VALIDATION-ARCHITECTURE.md` before them, per DEC-009.
`TRANSFORMATION-ARCHITECTURE.md` is not drafted under this decision — its
blocker (needing actually-`VALIDATED` capabilities) is unresolved, per
`DEC-019`.

### Rationale

`DEC-019` established that these two documents' specific readiness
blocker was resolved by `DEC-018`, and that drafting required a separate,
explicit owner confirmation per `DEC-004`. That confirmation was given.
Drafting now, following the established Tranche 1/2 pattern exactly
(generic mechanism, explicit "What This Document Does Not Decide"
section, illustrative non-binding examples), keeps the documents
consistent with the rest of the corpus and avoids inventing any
capability-specific choice the evidence does not support.

### Alternatives Considered

Drafting all of Tranche 3 together, including `TRANSFORMATION-ARCHITECTURE.md`
(rejected — `DEC-019` found its dependency genuinely unresolved; drafting
it now would require assuming which validation families are `VALIDATED`,
which none currently are); deferring drafting further pending a fourth
reassessment (rejected — the owner's confirmation was explicit and
`DEC-019`'s readiness finding for these two documents specifically was
not in question).

### Consequences

`docs/04-architecture/ANALYSIS-ARCHITECTURE.md` and
`docs/04-architecture/LANGUAGE-ARCHITECTURE.md` exist.
`ARCHITECTURE-MAP.md` §58, §62 and §64.4 are updated to record their
creation. 04-architecture now has five sub-documents beyond the MAP
itself, all still in substance within the structural-definition phase per
`ARCHITECTURE-MAP.md` §62's restated principle. `TRANSFORMATION-ARCHITECTURE.md`
and the six unevaluated candidates from §64.4 remain open for a future
tranche.

### Affected Areas

`docs/04-architecture/ANALYSIS-ARCHITECTURE.md` (new);
`docs/04-architecture/LANGUAGE-ARCHITECTURE.md` (new);
`docs/04-architecture/ARCHITECTURE-MAP.md` (§58, §62, §64.4.3).

### Reversal Conditions

If either document is found to have implicitly made a technical decision
it disclaims (contrary to its own §10/§9 "What This Document Does Not
Decide" sections respectively), that content should be removed and, if a
real decision is needed, recorded separately in this log rather than left
implicit in an architecture document — the same reversal condition
`DEC-014` set for Tranche 1.

### Related Research

R-0022, R-0039, R-0044, R-0046 through R-0073, R-0086, R-0109 through
R-0121.

### Related Questions

None directly — this decision concerns architecture-document creation.

---

## DEC-021 — Tranche 4: CORE-ARCHITECTURE.md Drafted; Remaining Candidates Triaged

### Date

2026-09-13

### Status

ACCEPTED

### Decision

Following the owner's request for a recommendation on the next priority,
and having completed Tranches 1, 2 and 3a, `ARCHITECTURE-MAP.md` §64.4's
six previously-unevaluated candidates (`CORE-ARCHITECTURE.md`,
`PIPELINE-ARCHITECTURE.md`, `EXTERNAL-INTEGRATION-ARCHITECTURE.md`,
`CONFIGURATION-ARCHITECTURE.md`, `REPORTING-ARCHITECTURE.md`,
`PLUGIN-ARCHITECTURE.md`) were triaged against whether
`ARCHITECTURE-MAP.md` already contains enough conceptual definition to
formalize without inventing new software-architecture concepts — a
different readiness test than §64.1's evidence-sufficiency signal, since
none of these six depend on per-language or per-model research evidence
at all.

1. **`docs/04-architecture/CORE-ARCHITECTURE.md`** is drafted, formalizing
   `ARCHITECTURE-MAP.md` §3-8 (High-Level Architecture, Architectural
   Layers, Interface Layer, Orchestration Layer, Text Representation
   Layer, Preservation Snapshot) — the execution backbone every capability
   document drafted so far (`CAPABILITY-ARCHITECTURE.md`, `DATA-MODEL.md`,
   `VALIDATION-ARCHITECTURE.md`, `ANALYSIS-ARCHITECTURE.md`,
   `LANGUAGE-ARCHITECTURE.md`) assumes exists. It selects no interface
   technology, data format, or algorithm, and explicitly leaves open
   whether a separate `PIPELINE-ARCHITECTURE.md` is warranted beyond its
   own §6 (Orchestration Layer) treatment.
2. **`EXTERNAL-INTEGRATION-ARCHITECTURE.md`** (§29-31) is assessed as
   likely similarly ready (well-specified, evidence-independent, grounded
   in DEC-001) but not drafted in this pass — recorded as the next
   candidate, not begun unilaterally.
3. **`CONFIGURATION-ARCHITECTURE.md`** (§36) and
   **`REPORTING-ARCHITECTURE.md`** (§38) are noted as reasonably specified
   but were not evaluated to the same depth.
4. **`PLUGIN-ARCHITECTURE.md`** has no parent section in
   `ARCHITECTURE-MAP.md` defining a plugin mechanism at all — triaged as
   **not assessable** without first scoping what "plugin" would mean in
   this architecture, which this decision does not attempt, per
   `NO-INVENTION-RULES.md`.

### Rationale

`ARCHITECTURE-MAP.md` §64.4's original text deferred these six
candidates purely for pacing ("would extend this proposal beyond what the
current research/specification base can actually support... revisit
after Tranches 1-2"), not because of any evidence gate like §64.1's. With
Tranches 1-3a complete, revisiting is due. `CORE-ARCHITECTURE.md` is the
strongest candidate precisely because its readiness never depended on
research evidence — it is arguably less blocked than any prior tranche
document, and its absence was becoming a real gap: five sub-documents
already assume an orchestration/preservation-snapshot layer that nothing
had formalized.

### Alternatives Considered

Drafting all six remaining candidates in one pass (rejected —
`PLUGIN-ARCHITECTURE.md` has no source material to formalize without
inventing one, and `PIPELINE-ARCHITECTURE.md`'s relationship to
`CORE-ARCHITECTURE.md` §6 needed to be resolved by drafting the latter
first, not decided in the abstract); starting technical implementation
instead of continuing documentation-layer work (considered as an
alternative next priority but not chosen — the architecture remains in
definition phase in substance, per `ARCHITECTURE-MAP.md` §62, and jumping
to implementation would require the specific technical choices §64.5
explicitly defers).

### Consequences

`docs/04-architecture/CORE-ARCHITECTURE.md` exists. `ARCHITECTURE-MAP.md`
§58, §62 and a new §64.6 record its creation and the triage outcome for
the other five candidates. `EXTERNAL-INTEGRATION-ARCHITECTURE.md` is the
recorded next candidate should the owner want to continue this line of
work.

### Affected Areas

`docs/04-architecture/CORE-ARCHITECTURE.md` (new);
`docs/04-architecture/ARCHITECTURE-MAP.md` (§58, §62, §64.6).

### Reversal Conditions

If `CORE-ARCHITECTURE.md` is found to have implicitly made a technical
decision it disclaims (contrary to its own §10), that content should be
removed and, if a real decision is needed, recorded separately in this
log — the same reversal condition set for every prior tranche document.
If `PIPELINE-ARCHITECTURE.md` is later drafted and found to duplicate
`CORE-ARCHITECTURE.md` §6 rather than add distinct content, that
duplication should be resolved by merging rather than left standing.

### Related Research

None — this decision concerns software-architecture mechanics
independent of the research layer.

### Related Questions

None directly — this decision concerns architecture-document creation.

---

## DEC-022 — EXTERNAL-INTEGRATION-ARCHITECTURE.md Drafted

### Date

2026-09-13

### Status

ACCEPTED

### Decision

Following the owner's explicit confirmation to proceed with the next
candidate DEC-021 identified, `docs/04-architecture/
EXTERNAL-INTEGRATION-ARCHITECTURE.md` is drafted, formalizing
`ARCHITECTURE-MAP.md` §29-31 (External Integration Layer, External Data
Boundary, Cloud Detector Integration). It defines: the adapter isolation
principle (§3, narrowing §27's general Dependency Isolation to the exact
boundary where data or a request crosses outside the local system); a
distinction between outbound integrations (user text sent externally) and
inbound-only ones (an artifact fetched, nothing of the user's sent) that
the earlier sections did not separately name; the concrete obligations
§30's external-data-boundary requirements impose at that adapter boundary
specifically, rather than left to interface-layer convention; how a cloud
detector's result must be tagged and reported as an external observation
per `ANALYSIS-ARCHITECTURE.md` §7, never substituted for a local
capability's own result (§31); a fifth failure/availability state
("external boundary unreachable") that extends `CORE-ARCHITECTURE.md`
§9's four-state taxonomy, distinguishing "the boundary itself was
unreachable" from "the capability ran and failed"; and the single
crossing point at which `ARCHITECTURE-MAP.md` §49's security controls for
downloaded artifacts must attach. It selects no specific external
provider, protocol, data format, or security-control mechanism.

### Rationale

`DECISION-LOG.md` DEC-021 already assessed this document as "likely
ready" on the same evidence-independent test that made
`CORE-ARCHITECTURE.md` draftable — §29-31 describe boundary and isolation
mechanics, not a scientific claim requiring per-language or per-model
evidence — and identified it as the recorded next candidate. The owner's
confirmation to proceed with that recommendation is the authorization
this decision executes.

### Alternatives Considered

Drafting `CONFIGURATION-ARCHITECTURE.md` or `REPORTING-ARCHITECTURE.md`
instead (rejected for this pass — DEC-021 assessed both as "reasonably
specified but not evaluated to the same depth," meaning a diligent
drafting pass would need to start with that evaluation, not proceed
straight to drafting as `EXTERNAL-INTEGRATION-ARCHITECTURE.md` could);
attempting `PLUGIN-ARCHITECTURE.md` (rejected — DEC-021 found no parent
section exists for it at all, so drafting it now would mean inventing a
scope, contrary to `NO-INVENTION-RULES.md`).

### Consequences

`docs/04-architecture/EXTERNAL-INTEGRATION-ARCHITECTURE.md` exists,
formalizing generic adapter/boundary mechanics only.
`ARCHITECTURE-MAP.md` §58, §62 and §64.6 should be updated to record its
creation. `CONFIGURATION-ARCHITECTURE.md` and `REPORTING-ARCHITECTURE.md`
remain the next candidates if the owner wants to continue this line of
work, still pending the deeper evaluation DEC-021 deferred for both.

### Affected Areas

`docs/04-architecture/EXTERNAL-INTEGRATION-ARCHITECTURE.md` (new);
`docs/04-architecture/ARCHITECTURE-MAP.md` (§58, §62, §64.6).

### Reversal Conditions

If `EXTERNAL-INTEGRATION-ARCHITECTURE.md` is found to have implicitly
selected a specific provider, protocol, or security mechanism contrary to
its own §10, that content should be removed and, if a real decision is
needed, recorded separately in this log — the same reversal condition set
for every prior tranche document. If the outbound/inbound-only
distinction (§4) proves not to match how `CAPABILITY-ARCHITECTURE.md`
capabilities actually use external integrations once implemented, that
distinction should be revised rather than left standing as a mismatch.

### Related Research

None — this decision concerns software-architecture mechanics
independent of the research layer.

### Related Questions

None directly — this decision concerns architecture-document creation.

---

## DEC-023 — REPORTING-ARCHITECTURE.md Assessed Ready; CONFIGURATION-ARCHITECTURE.md Found Blocked by an Unrecorded Scoping Overlap

### Date

2026-09-13

### Status

ACCEPTED

### Decision

Following the owner's confirmation to proceed with the deeper evaluation
DEC-021 deferred, `CONFIGURATION-ARCHITECTURE.md` (§36) and
`REPORTING-ARCHITECTURE.md` (§38) were each evaluated against §64.6's
readiness test. Findings, recorded in `ARCHITECTURE-MAP.md` §64.7:

1. **`REPORTING-ARCHITECTURE.md`** is assessed **structurally ready**.
   Its obligations are already scattered concretely across every
   sub-document drafted so far (`CORE-ARCHITECTURE.md` §9,
   `ANALYSIS-ARCHITECTURE.md` §7, `VALIDATION-ARCHITECTURE.md` §9,
   `EXTERNAL-INTEGRATION-ARCHITECTURE.md` §5-7), plus §38's own content
   list and the reinforcing principles in §21, §51 and §56. Drafting it
   would unify already-required obligations, not invent new ones. It is
   **not drafted by this decision** — only assessed — pending the
   owner's separate confirmation to draft, consistent with this
   project's macro-tranche-boundary practice (`DEC-004`).
2. **`CONFIGURATION-ARCHITECTURE.md`** is assessed **not yet ready**, for
   a reason distinct from any prior tranche document's blocker: this
   evaluation found that §36's content list substantially overlaps §37's
   (Evaluation Profiles) content list, and `ARCHITECTURE-MAP.md` nowhere
   states whether an Evaluation Profile is a specialization of
   Configuration, a separate parallel concept, or the same thing under
   two names. This gap was previously unrecorded. Per
   `docs/99-backlog/POST-INVENTORY-QUEUE.md`'s Governing Rule and
   `NO-INVENTION-RULES.md`, this decision does not resolve the
   relationship — it records the gap and leaves
   `CONFIGURATION-ARCHITECTURE.md` undrafted pending a scoping decision.

### Rationale

The owner asked specifically for the deeper evaluation DEC-021 had
deferred for both documents — "not evaluated to the same depth" as
`CORE-ARCHITECTURE.md` and `EXTERNAL-INTEGRATION-ARCHITECTURE.md`.
Applying that same depth surfaced a real, previously unnoticed
overlap for one of the two candidates — exactly the kind of finding
`docs/99-backlog/CLAUDE-CONSOLIDATION-INSTRUCTIONS.md`'s
Inventory → Audit → Change → Verify discipline exists to catch before it
gets baked into a new document silently. Drafting
`CONFIGURATION-ARCHITECTURE.md` around the overlap (by picking either
reading of the Configuration/Evaluation-Profile relationship without
recording the choice) would have repeated the exact failure mode
`NO-INVENTION-RULES.md` exists to prevent — an unrecorded structural
decision presented as if it were already settled.

### Alternatives Considered

Drafting `CONFIGURATION-ARCHITECTURE.md` anyway, treating Evaluation
Profiles as a subset of Configuration or vice versa (rejected — either
choice is a real scoping decision, not something this evaluation is
authorized to make silently); deferring the `REPORTING-ARCHITECTURE.md`
evaluation until `CONFIGURATION-ARCHITECTURE.md`'s overlap was resolved,
on the theory the two should proceed together (rejected — the two
documents' readiness turned out to be independent, and gating one on the
other would delay a document that is genuinely ready without cause).

### Consequences

`ARCHITECTURE-MAP.md` §64.6's `CONFIGURATION-ARCHITECTURE.md`/
`REPORTING-ARCHITECTURE.md` bullet and a new §64.7 record these findings.
`REPORTING-ARCHITECTURE.md` becomes the recorded next candidate for
drafting, pending separate confirmation.
`CONFIGURATION-ARCHITECTURE.md` is blocked until a scoping decision on
its relationship to Evaluation Profiles (§37) is proposed and recorded in
this log in its own right.

### Affected Areas

`docs/04-architecture/ARCHITECTURE-MAP.md` (§64.6, new §64.7). No new
sub-document created by this decision.

### Reversal Conditions

If the Configuration/Evaluation-Profile scoping decision, once made,
finds the overlap was illusory (e.g. the two lists were always intended
to describe the same object under two names, and no real ambiguity
existed), this decision's characterization of `CONFIGURATION-ARCHITECTURE.md`
as blocked should be revised and the document drafted without further
delay.

### Related Research

None — this decision concerns software-architecture mechanics
independent of the research layer.

### Related Questions

None directly — this decision concerns architecture-document evaluation
and a documentation-scoping gap, not a scientific question.

---

## DEC-024 — REPORTING-ARCHITECTURE.md Drafted

### Date

2026-09-13

### Status

ACCEPTED

### Decision

Following the owner's explicit confirmation to proceed with the
candidate DEC-023 assessed as structurally ready,
`docs/04-architecture/REPORTING-ARCHITECTURE.md` is drafted, formalizing
`ARCHITECTURE-MAP.md` §38 (Reporting Layer) together with §21 (Evaluation
Layer). Rather than formalizing a section range no other document yet
touched (as `CORE-ARCHITECTURE.md` and `EXTERNAL-INTEGRATION-ARCHITECTURE.md`
did), this document's task was to consolidate reporting obligations
already required, individually, by four documents already drafted:
`CORE-ARCHITECTURE.md` §9's failure/eligibility taxonomy (extended to a
fifth state by `EXTERNAL-INTEGRATION-ARCHITECTURE.md` §7);
`ANALYSIS-ARCHITECTURE.md` §7's output-category tagging;
`VALIDATION-ARCHITECTURE.md` §9's missing-evidence states (`FID-043`),
generalized in this document to every dimension a report covers, not
only validation; and `EXTERNAL-INTEGRATION-ARCHITECTURE.md` §5-6's
external-observation tagging and data-transfer logging. It organizes the
report schema into an observation tier (individual, unaggregated results
with every field the source documents already require intact) and a
summary tier (any human-readable rollup, required to be derived from,
and traceable back to, the observation tier — never an independent,
potentially divergent record). It selects no specific serialization
format, storage technology, or rendering/UI, and explicitly does not
resolve the `CONFIGURATION-ARCHITECTURE.md`/Evaluation-Profile scoping
overlap `DECISION-LOG.md` DEC-023 recorded.

### Rationale

`DECISION-LOG.md` DEC-023 already assessed this document as structurally
ready, finding its content already scattered across every sub-document
drafted so far rather than merely conceptually available in
`ARCHITECTURE-MAP.md`. The owner's confirmation to proceed is the
authorization this decision executes, consistent with this project's
macro-tranche-boundary practice (`DEC-004`) of drafting only after
separate, explicit confirmation distinct from the evaluation step itself.

### Alternatives Considered

Waiting for the `CONFIGURATION-ARCHITECTURE.md` scoping question to
resolve before drafting this document (rejected — DEC-023 already found
the two documents' readiness to be independent, and this document's own
§2 and §11 make explicit that it depends on neither the existence nor the
resolution of that overlap, only on being able to record whichever
configuration/evaluation-profile information exists); inventing a
concrete serialization format or UI to make the document feel more
"complete" (rejected — `ARCHITECTURE-MAP.md` §43 reserves this for
Development, and doing so here would violate the same discipline every
prior tranche document has followed).

### Consequences

`docs/04-architecture/REPORTING-ARCHITECTURE.md` exists, the eighth
sub-document in 04-architecture. `ARCHITECTURE-MAP.md` §58, §62 and §64.7
should be updated to record its creation.
`CONFIGURATION-ARCHITECTURE.md` remains the last of Tranche 4's original
six candidates still blocked, pending its own scoping decision;
`PIPELINE-ARCHITECTURE.md` and `PLUGIN-ARCHITECTURE.md` remain open
scoping questions as before.

### Affected Areas

`docs/04-architecture/REPORTING-ARCHITECTURE.md` (new);
`docs/04-architecture/ARCHITECTURE-MAP.md` (§58, §62, §64.7).

### Reversal Conditions

If `REPORTING-ARCHITECTURE.md` is found to have implicitly selected a
specific serialization format, storage technology, or certification
criterion contrary to its own §11, that content should be removed and, if
a real decision is needed, recorded separately in this log — the same
reversal condition set for every prior tranche document. If the
observation-tier/summary-tier split (§3) proves unworkable once a
concrete schema is implemented, that split should be revised rather than
left standing as a mismatch.

### Related Research

None — this decision concerns software-architecture mechanics
independent of the research layer.

### Related Questions

None directly — this decision concerns architecture-document creation.

---

## DEC-025 — Configuration/Evaluation-Profile Scoping Resolved; CONFIGURATION-ARCHITECTURE.md Drafted

### Date

2026-09-13

### Status

ACCEPTED

### Decision

Resolving the scoping question `DECISION-LOG.md` DEC-023 recorded (an
unrecorded overlap between `ARCHITECTURE-MAP.md` §36's Configuration
Layer content list and §37's Evaluation Profile content list): the two
are distinct, composable concepts, not the same object under two names,
and not a strict subset relationship either.

- **Configuration** (§36) governs a single request/run's operational
  settings — what a specific execution actually does (language, pipeline,
  enabled capabilities, transformation constraints, which profile(s)
  apply, external services, resource limits, output format, logging
  level).
- **An Evaluation Profile** (§37) is a versioned, named, explicitly-scoped
  bundle of techniques, detectors, languages, datasets, transformations,
  metrics, thresholds, date, and evidence baseline — grounded not only in
  §37 but, decisively, in `docs/03-scientific-specification/
  SPECIFICATION-MAP.md` §27 ("No Universal Success Claim": "effectiveness
  is evaluated against a versioned, explicitly defined evaluation
  profile") and §28 (Effectiveness Profiles: baseline, conservative,
  multilingual, research, regression, release certification). Its purpose
  is scientific/evidentiary — scoping an effectiveness claim to an
  explicit, reproducible basis — not operational.

The overlap in field names (languages, transformations, detectors/
analyzers, thresholds) reflects composition, not duplication: a
Configuration selects *which* Evaluation Profile (by name/version)
governs a given run's effectiveness framing; the Evaluation Profile is
the versioned definition being selected. This is the same relationship
already implicit, but never made explicit until now, in
`ARCHITECTURE-MAP.md` §5 and `CORE-ARCHITECTURE.md` §5 (both already list
"configuration" and "evaluation profile" as two separate, coexisting
interface inputs) and in `ARCHITECTURE-MAP.md` §40 (Reproducibility, which
already lists "configuration" and "evaluation profile" as two separate
reproducibility inputs, side by side).

With this resolved, `docs/04-architecture/CONFIGURATION-ARCHITECTURE.md`
is drafted, formalizing §36 and its now-explicit relationship to §37.

### Rationale

This resolution does not invent a relationship between the two concepts;
it makes explicit a distinction the corpus's own cross-references already
assumed. Three independent places in the already-existing corpus treat
Configuration and Evaluation Profile as separate: `ARCHITECTURE-MAP.md`
§5 and its restatement in `CORE-ARCHITECTURE.md` §5 (an interface accepts
both, as two distinct selections), `ARCHITECTURE-MAP.md` §40 (both listed
as separate reproducibility inputs), and, most decisively,
`SPECIFICATION-MAP.md` §27-28 — an authoritative scientific-specification
document, not merely an architectural one — which defines an evaluation
profile's purpose as preventing an unscoped, universal effectiveness
claim. That purpose has no operational-configuration analogue: a single
production run's Configuration does not itself make a scientific
effectiveness claim, so treating the two as the same concept would have
required ignoring §27-28's own stated rationale for the term.

### Alternatives Considered

Treating Configuration and Evaluation Profile as the same concept under
two names (rejected — directly contradicted by §5/`CORE-ARCHITECTURE.md`
§5 and §40 already listing both as separate, coexisting items; if they
were one concept, listing both would be redundant, and the corpus does
not otherwise duplicate list items this way); treating Evaluation Profile
as a strict subset of Configuration (rejected — `SPECIFICATION-MAP.md`
§27-28 grounds Evaluation Profile in the scientific/evidentiary layer,
with named profiles such as "release certification" that a single
request's operational Configuration would not itself define or version);
leaving `CONFIGURATION-ARCHITECTURE.md` blocked indefinitely pending
further evidence (rejected — the ambiguity was resolvable from evidence
already in the corpus; further deferral would have been avoidable delay,
not genuine caution).

### Consequences

`docs/04-architecture/CONFIGURATION-ARCHITECTURE.md` exists, the ninth
sub-document in 04-architecture and the last of Tranche 4's original six
candidates to be resolved one way or another (`PIPELINE-ARCHITECTURE.md`
and `PLUGIN-ARCHITECTURE.md` remain open scoping questions, unaffected by
this decision). `ARCHITECTURE-MAP.md` §58, §62 and §64.7 should be updated
to record both the scoping resolution and the document's creation.
Separately, this evaluation noted that §36's own term "validation
profile" is not itself defined by `VALIDATION-ARCHITECTURE.md` or any
other document — a smaller, distinct gap this decision does not resolve;
`CONFIGURATION-ARCHITECTURE.md` treats it as an open field name pending
its own definition rather than inventing a meaning for it.

### Affected Areas

`docs/04-architecture/CONFIGURATION-ARCHITECTURE.md` (new);
`docs/04-architecture/ARCHITECTURE-MAP.md` (§58, §62, §64.7).

### Reversal Conditions

If a future document finds that Configuration and Evaluation Profile were
in fact intended as a single concept (contrary to the reading in this
decision), or that the composition relationship described here does not
match how `CAPABILITY-ARCHITECTURE.md` capabilities or
`VALIDATION-ARCHITECTURE.md` validators actually consume a Configuration
once implemented, this decision should be revisited and revised rather
than left standing as a mismatch. If `CONFIGURATION-ARCHITECTURE.md` is
found to have implicitly selected a specific configuration format,
schema, or storage mechanism contrary to its own "What This Document Does
Not Decide" section, that content should be removed and, if a real
decision is needed, recorded separately in this log.

### Related Research

None — this decision concerns software-architecture and scientific-
specification cross-referencing, not new research evidence.

### Related Questions

None directly — this decision concerns architecture-document scoping and
creation.

---

## DEC-026 — PIPELINE-ARCHITECTURE.md Resolved as Not Needed; Evaluation Layer Gap Recorded

### Date

2026-09-13

### Status

ACCEPTED

### Decision

Resolving the last readily-resolvable scoping question from Tranche 4's
original six candidates: `PIPELINE-ARCHITECTURE.md` is **not needed as a
separate document**. Its full plausible scope — pipeline construction,
stage execution order, dispatch flow — is already formalized by
`docs/04-architecture/CORE-ARCHITECTURE.md` §6 (Orchestration Layer,
including a concrete 7-step dispatch flow) and §3 (High-Level Pipeline,
restated from `ARCHITECTURE-MAP.md` §3). An exhaustive search of
`ARCHITECTURE-MAP.md` for any pipeline concept beyond this single, fixed,
linear flow — composition, branching, multiple pipeline "shapes," a
versioned pipeline registry, conditional or parallel stage execution —
found none: the terms do not appear anywhere in the corpus. Drafting a
separate `PIPELINE-ARCHITECTURE.md` would therefore either duplicate
`CORE-ARCHITECTURE.md` §6 verbatim or invent pipeline concepts the corpus
does not support — both contrary to `NO-INVENTION-RULES.md`.

Separately, this evaluation surfaced a genuine, distinct, and previously
unflagged gap: `ARCHITECTURE-MAP.md` §21-22 (Evaluation Layer,
Experimental Matrix) — the pipeline's EVALUATION stage — is not
formalized by any current or candidate document.
`docs/04-architecture/CORE-ARCHITECTURE.md` §3 explicitly disclaims
formalizing it beyond result-aggregation; `REPORTING-ARCHITECTURE.md`
formalizes only the reporting of results, not the evaluation/benchmarking
mechanics themselves (benchmark execution, detector comparison,
regression analysis, statistical analysis, per §21). This decision does
not add a new candidate document to resolve that gap — proposing a new
§58 candidate that was never on the original list would itself be a
structural decision beyond what this evaluation was asked to do — it only
records the gap for the owner's future consideration.

### Rationale

The same evidence-based method that resolved DEC-025's Configuration/
Evaluation-Profile overlap applies here: before treating a scoping
question as blocked indefinitely, check whether the corpus's own text
already resolves it. Here it does, but in the opposite direction from
DEC-025 — rather than finding a real, distinct scope that merely needed
articulating, this evaluation found no distinct scope exists at all.
Recording "not needed" is itself a real scoping decision (per this
project's standing practice that structural/scope decisions must be
proposed and recorded, not silently skipped) — it prevents a future
contributor from treating `PIPELINE-ARCHITECTURE.md`'s continued absence
from `docs/04-architecture/` as an oversight rather than a considered
conclusion.

### Alternatives Considered

Drafting a placeholder `PIPELINE-ARCHITECTURE.md` anyway, restating
`CORE-ARCHITECTURE.md` §6 under a different title (rejected — pure
duplication serves no purpose and risks the two documents silently
drifting apart over time, the exact failure `ARCHITECTURE-MAP.md` §57 and
`LANGUAGE-ARCHITECTURE.md` §5 warn against for other duplicated-bookkeeping
cases); silently leaving the Evaluation Layer gap unrecorded now that
`PIPELINE-ARCHITECTURE.md` is resolved (rejected —
`docs/99-backlog/POST-INVENTORY-QUEUE.md`'s Governing Rule requires a gap
found during an audit be recorded, not silently dropped because it fell
outside the specific question being resolved); unilaterally proposing a
new `EVALUATION-ARCHITECTURE.md` candidate to close that gap (rejected —
adding a candidate document not on the original `§58` list is itself a
scope decision the owner should weigh in on, not something to decide
unilaterally while resolving an unrelated question).

### Consequences

`ARCHITECTURE-MAP.md` §58's candidate list and §64.6/§64.7 should mark
`PIPELINE-ARCHITECTURE.md` as resolved ("not needed — see
`CORE-ARCHITECTURE.md` §6") rather than a pending candidate.
`CORE-ARCHITECTURE.md` §2 and §10's "left open" language about
`PIPELINE-ARCHITECTURE.md` should be updated to reflect the resolution.
The Evaluation Layer (§21-22) gap is recorded as an open finding, not
resolved by this decision. `PLUGIN-ARCHITECTURE.md` remains the only
genuinely unresolved scoping question among Tranche 4's original six
candidates — unlike `PIPELINE-ARCHITECTURE.md` and
`CONFIGURATION-ARCHITECTURE.md`, its blocker is a total absence of any
corpus text to reason from, not an overlap or duplication question this
kind of evidence-based analysis can resolve; it requires the owner's own
scoping input on what "plugin" should mean for this project, if anything.

### Affected Areas

`docs/04-architecture/ARCHITECTURE-MAP.md` (§58, §64.6, §64.7, new
§64.8); `docs/04-architecture/CORE-ARCHITECTURE.md` (§2, §10). No new
sub-document created by this decision.

### Reversal Conditions

If a future need arises for a pipeline concept `ARCHITECTURE-MAP.md`
does not currently describe (e.g. conditional branching, multiple
named pipeline topologies), that need should be proposed and recorded as
its own decision — at which point `PIPELINE-ARCHITECTURE.md` (or an
equivalent) may become genuinely necessary, and this decision's "not
needed" conclusion should be revisited rather than treated as permanent.

### Related Research

None — this decision concerns software-architecture document scoping.

### Related Questions

None directly — the Evaluation Layer gap noted above is an architecture-
documentation gap, not a research question, and is recorded in
`ARCHITECTURE-MAP.md` rather than `OPEN-QUESTIONS.md` for that reason,
consistent with how the `PIPELINE-ARCHITECTURE.md`/`PLUGIN-ARCHITECTURE.md`
scoping questions have been recorded throughout Tranche 4.

---

## DEC-027 — Cross-Reference Consolidation Pass Over `docs/04-architecture/`

### Date

2026-09-13

### Status

ACCEPTED

### Decision

With Tranche 4 concluded (DEC-021 through DEC-026), `docs/04-architecture/`
now holds ten files (nine sub-documents plus `ARCHITECTURE-MAP.md`), most
written or edited in rapid succession over a few days. Following this
project's own precedent (`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`,
which performed the same kind of pass over `00-project` through early
`03-scientific-specification`), this decision records a consolidation
pass scoped to `docs/04-architecture/` alone: a check for stale
cross-references, contradictions, duplication, terminology drift, and
missing cross-references among the ten files, per
`docs/99-backlog/CLAUDE-CONSOLIDATION-INSTRUCTIONS.md` Phases 1-6. Per
that document's Phase 10, only changes classified as mechanical (no new
scope or content judgment) were applied directly; anything else is
recorded below for the owner rather than resolved.

**Mechanical fixes applied directly** (cross-reference additions and
citation corrections only — no requirement, schema, or scope content was
changed):

1. `CORE-ARCHITECTURE.md` §9 — its four-state failure taxonomy was
   presented as closed even though `EXTERNAL-INTEGRATION-ARCHITECTURE.md`
   §7 (drafted afterward, DEC-022) adds a fifth state, restated by
   `REPORTING-ARCHITECTURE.md` §4. Added a forward pointer; also replaced
   the placeholder "a Reporting Layer document, §10" with a direct
   pointer to `REPORTING-ARCHITECTURE.md`.
2. `CORE-ARCHITECTURE.md` §9 and `REPORTING-ARCHITECTURE.md` §4 both
   cited "`CAPABILITY-ARCHITECTURE.md` §10's `NOT_SUPPORTED` state" — but
   that section defines only the per-language map structure, not the
   state itself. Corrected both citations to `SPECIFICATION-MAP.md` §22,
   the state's actual origin, matching the attribution
   `LANGUAGE-ARCHITECTURE.md` §3 already used correctly.
3. `CAPABILITY-ARCHITECTURE.md` §13 cited "`ARCHITECTURE-MAP.md` §2 and
   §29 (Independent Detectors)" — verified that `ARCHITECTURE-MAP.md` §29
   is "External Integration Layer," not "Independent Detectors," and
   that the "Independent Detectors" heading exists only in
   `docs/02-research/R04-ai-generated-text-detection-research.md` §29.
   Corrected the citation to name that document.
4. `CAPABILITY-ARCHITECTURE.md` §6 — its `DEGRADED`-state reporting
   requirement pointed only at `ARCHITECTURE-MAP.md` §38; added a pointer
   to `REPORTING-ARCHITECTURE.md`, which now formalizes that requirement
   concretely.
5. `CAPABILITY-ARCHITECTURE.md` §10 — added a note that
   `CONFIGURATION-ARCHITECTURE.md` §3 depends on this section's
   eligibility rule and was drafted after this document, previously
   unreferenced here.
6. `VALIDATION-ARCHITECTURE.md` §9 — added a pointer from its
   missing-evidence discipline to `REPORTING-ARCHITECTURE.md` §5, which
   generalizes it to every report dimension.
7. `VALIDATION-ARCHITECTURE.md` §14 — added an acknowledgment that
   `CONFIGURATION-ARCHITECTURE.md` §5 names this document as owning the
   still-undefined "validation profile" field; not resolved, only
   acknowledged on both sides now.
8. `ANALYSIS-ARCHITECTURE.md` §7 — added a pointer from Output Category
   Tagging to `REPORTING-ARCHITECTURE.md` §6, which requires the tag
   travel into the report schema.
9. `LANGUAGE-ARCHITECTURE.md` §9 — its "does not resolve DCQ-006/007/008"
   language was stale now that all three (External Integration,
   Reporting, Configuration) are resolved by name; updated, and added a
   pointer from its `validation_status: mixed` discipline to
   `REPORTING-ARCHITECTURE.md` §5.
10. `DATA-MODEL.md` §2 — added the reverse of a relationship
    `EXTERNAL-INTEGRATION-ARCHITECTURE.md` §2 already stated one-way
    (the boundary-crossing vs. post-arrival distinction between the two
    documents).
11. `CONFIGURATION-ARCHITECTURE.md` §3 — its restatement of
    `ARCHITECTURE-MAP.md` §36's field list had silently replaced §36's
    literal "validation profile" with "which profile(s) apply" without
    flagging that this folds in DEC-025's separate Evaluation Profile
    concept. Clarified the attribution: §36 itself names only "validation
    profile"; the Evaluation Profile reference comes from DEC-025, not
    from §36's own text.

**Recorded, not resolved — requires owner decision:**

`CAPABILITY-ARCHITECTURE.md` §6 defines a capability's *own* lifecycle
enum (`DISCOVERED → EXPERIMENTAL → VALIDATED → ACTIVE → DEGRADED →
DEPRECATED → RETIRED`) and §10 states that a capability's per-language
`languages` map holds "a map from language code to lifecycle state (§6)."
But `LANGUAGE-ARCHITECTURE.md`, `ANALYSIS-ARCHITECTURE.md`, and
`REPORTING-ARCHITECTURE.md` (all drafted after `CAPABILITY-ARCHITECTURE.md`)
populate that same per-language map with `RESEARCH_ONLY` and
`NOT_SUPPORTED` — values that are not members of §6's enum and that
originate instead in `SPECIFICATION-MAP.md` §22's separate default
vocabulary. No document states whether `NOT_SUPPORTED`/`RESEARCH_ONLY`
should become additional members of §6's own enum, or remain a distinct
vocabulary layered on top of it. This is the same class of "lifecycle-
state vocabulary drift" `docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`
already found and deferred once at the cross-area level (§5/§13 there);
it now reproduces inside `04-architecture`'s own sub-documents. A note
recording this gap, without resolving it, was added to
`CAPABILITY-ARCHITECTURE.md` §10.

### Rationale

The same discipline applied throughout Tranche 4 — apply what the
evidence already settles, record rather than guess at what it does not —
extends naturally to consolidation work: additive cross-references and
citation corrections change no requirement or scope and are safe to
apply directly, per `CLAUDE-CONSOLIDATION-INSTRUCTIONS.md` Phase 10's own
"safe automatic change" category and the precedent already set by
`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md` §11. The one genuine
content question found (the lifecycle-enum/per-language-vocabulary
relationship) involves a real choice among plausible resolutions and is
therefore left for the owner, exactly as DCQ-005 was in the prior
consolidation pass.

### Alternatives Considered

Silently reconciling the lifecycle-enum/vocabulary gap by picking one of
the plausible resolutions unilaterally (rejected — this is a content
decision about a formal enum's membership, not a mechanical fix, and
`NO-INVENTION-RULES.md` and this project's standing practice both require
such decisions to be proposed and recorded, not silently made);
performing the full Q001 cross-area audit instead of a scoped
04-architecture-only pass (deferred — Q001 remains a separate, larger
undertaking per the prior consolidation report §13/§14, not something to
fold into this pass without being asked); leaving the stale
cross-references uncorrected on the grounds that no reader had yet been
confused by them (rejected — the prior consolidation report's own
precedent already established mechanical fixes as safe to apply
proactively rather than waiting for a symptom).

### Consequences

The ten `docs/04-architecture/` files are more internally consistent and
their cross-references reflect the documents that actually exist as of
DEC-026, rather than the state each was written in. No requirement,
schema field, taxonomy, or scope decision was changed by this pass — only
pointers and citations. The lifecycle-enum/vocabulary gap remains open
and is now visible in `CAPABILITY-ARCHITECTURE.md` §10 itself, not only
in this log entry.

### Affected Areas

`docs/04-architecture/CORE-ARCHITECTURE.md` (§9),
`docs/04-architecture/CAPABILITY-ARCHITECTURE.md` (§6, §10, §13),
`docs/04-architecture/VALIDATION-ARCHITECTURE.md` (§9, §14),
`docs/04-architecture/ANALYSIS-ARCHITECTURE.md` (§7),
`docs/04-architecture/LANGUAGE-ARCHITECTURE.md` (§9),
`docs/04-architecture/DATA-MODEL.md` (§2),
`docs/04-architecture/REPORTING-ARCHITECTURE.md` (§4),
`docs/04-architecture/CONFIGURATION-ARCHITECTURE.md` (§3). No new
sub-document created; no existing requirement or scope changed.

### Reversal Conditions

If the owner resolves the lifecycle-enum/vocabulary gap in a future
decision, the note in `CAPABILITY-ARCHITECTURE.md` §10 should be replaced
with whatever concrete rule that decision establishes, rather than left
alongside it.

### Related Research

None — this decision concerns documentation cross-reference consistency,
not scientific content.

### Related Questions

None new — the lifecycle-enum/vocabulary gap is an architecture-
documentation gap in the same family as the Evaluation Layer gap DEC-026
recorded, not a research question for `OPEN-QUESTIONS.md`.

---

## DEC-028 — Correct a Mislabeled DCQ Cross-Reference in Three `docs/04-architecture/` Documents

### Date

2026-09-13

### Status

ACCEPTED

### Decision

While applying DEC-027's consolidation fixes, a further, more
significant citation error was found and is corrected by this decision:
`CORE-ARCHITECTURE.md` §10, `EXTERNAL-INTEGRATION-ARCHITECTURE.md` §10,
and (introduced by DEC-027's own edit, then corrected in the same pass)
`LANGUAGE-ARCHITECTURE.md` §9 all stated that the External Integration,
Reporting, and Configuration Layers being undefined was tracked as
`DCQ-006`, `DCQ-007`, and/or `DCQ-008` in
`docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md`, and that drafting
`EXTERNAL-INTEGRATION-ARCHITECTURE.md`, `REPORTING-ARCHITECTURE.md`, and
`CONFIGURATION-ARCHITECTURE.md` resolved those items.

This is factually wrong. `DOCUMENTATION-CHANGE-QUEUE.md`'s actual
DCQ-006 ("Propagate R02/R03/R04/R05 Literature Findings Beyond the
Research Layer"), DCQ-007 ("Propagate Two Scientific-Integrity Gaps
Found by the Q001 Audit"), and DCQ-008 ("Propagate Q-008/R09
Local-Deployment Findings to Architecture and Specification") are all
about propagating specific research findings into per-language
capability states and requirements — the same items `DEC-016` through
`DEC-019` already correctly used to explain why `ANALYSIS-` and
`LANGUAGE-ARCHITECTURE.md` (Tranche 3) were blocked. None of the eight
items in `DOCUMENTATION-CHANGE-QUEUE.md` is about the External
Integration, Reporting, or Configuration Layers specifically — the
closest match is `DCQ-004` ("Introduce External Evidence Boundary,"
still `PENDING`), whose "Required Updates" list includes "Architecture,"
and which genuinely is the subject `EXTERNAL-INTEGRATION-ARCHITECTURE.md`
addresses. No DCQ item exists at all for Reporting or Configuration
Layer creation — those gaps were simply never filed in
`DOCUMENTATION-CHANGE-QUEUE.md`, and the "DCQ-006/007/008" label attached
to them in the three documents above appears to have been an
unverified restatement, not a citation to anything that actually says
that.

Corrected: `CORE-ARCHITECTURE.md` §10 and `EXTERNAL-INTEGRATION-ARCHITECTURE.md`
§10 now state plainly that DCQ-006/007/008 are unrelated
research-propagation items, and separately that the External
Integration/Reporting/Configuration Layers are formalized by their own
three documents with no DCQ item ever tracking that fact — except for
the External Integration Layer specifically, where `DCQ-004` is now
named as the actual (still-`PENDING`) matching item, recorded in
`DOCUMENTATION-CHANGE-QUEUE.md` itself with a note, not marked resolved.
`LANGUAGE-ARCHITECTURE.md` §9's version of the same error, introduced
minutes earlier in this same consolidation pass (DEC-027), is corrected
identically.

### Rationale

`NO-INVENTION-RULES.md` requires that a citation actually say what it is
cited for; a governance document that confidently cites the wrong
tracking item is worse than one that cites nothing, because it looks
verified when it is not. This was caught only because DEC-027's own
verification step — reading the actual target of every citation before
trusting a sub-agent's cross-reference audit — was applied to a citation
outside that audit's original findings list, on the general principle
that a consolidation pass should follow every citation it touches back
to its stated source, not just the ones flagged by the tool that
produced the initial findings.

### Alternatives Considered

Leaving the error in place since it does not affect any requirement or
technical decision (rejected — a governance log whose own citations are
unverified undermines the traceability this project's documentation
exists to provide, per `docs/01-governance/P00-project-governance.md`'s
authority hierarchy and `NO-INVENTION-RULES.md`'s evidentiary discipline
generally); marking `DCQ-004` `VERIFIED` or `CLOSED` now that
`EXTERNAL-INTEGRATION-ARCHITECTURE.md` exists (rejected — DCQ-004's
Required Updates list five areas, only one of which,
Architecture, has anything drafted against it; declaring the whole item
resolved would overstate what has actually been done, and deciding
whether a partially-addressed item's status should change is a content
judgment for the owner, not a mechanical fix).

### Consequences

`CORE-ARCHITECTURE.md`, `EXTERNAL-INTEGRATION-ARCHITECTURE.md`, and
`LANGUAGE-ARCHITECTURE.md` no longer misattribute a documentation-gap
resolution to DCQ items that do not track it.
`docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md` DCQ-004 carries a note
identifying `EXTERNAL-INTEGRATION-ARCHITECTURE.md` as addressing its
Architecture line, without changing its `PENDING` status. No requirement
or scope content was changed.

### Affected Areas

`docs/04-architecture/CORE-ARCHITECTURE.md` (§10),
`docs/04-architecture/EXTERNAL-INTEGRATION-ARCHITECTURE.md` (§10),
`docs/04-architecture/LANGUAGE-ARCHITECTURE.md` (§9),
`docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md` (DCQ-004, note added).

### Reversal Conditions

If the owner decides `DCQ-004` should be marked resolved, partially
resolved, or re-scoped now that its Architecture line has a document
against it, that decision should be recorded as its own entry rather
than inferred from this one.

### Related Research

None — this decision concerns a documentation citation error, not
scientific content.

### Related Questions

None — this is a citation-accuracy correction, not a new open question.