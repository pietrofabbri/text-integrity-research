# Claude Consolidation Report

**Document type:** Post-inventory consolidation report
**Status:** ACTIVE — TWO PASSES RECORDED (first pass scoped; second pass is
the Q001 cross-area audit)
**Date:** 2026-08-22 (first pass); 2026-08-29 (second pass, Q001)
**Produced per:** `docs/99-backlog/CLAUDE-CONSOLIDATION-INSTRUCTIONS.md`,
`docs/99-backlog/CLAUDE-CONSOLIDATION-QUEUE.md`,
`docs/99-backlog/POST-INVENTORY-QUEUE.md` Q001
**Scope note:** This is a first consolidation pass, not the full 18-point
cross-area audit defined in `docs/99-backlog/POST-INVENTORY-QUEUE.md`
Q001. Q001 requires tracing individual requirements across 04-architecture
through 10-certification (coverage mapping, requirement→test→evidence
traceability) and has not been performed. This report covers Phase
1–6 of `CLAUDE-CONSOLIDATION-INSTRUCTIONS.md` (inventory confirmation,
authority mapping, duplication, contradiction, terminology, cross-reference)
at the depth the reviewed documents support, plus the findings that
motivated it. Where evidence was insufficient, this report says so
explicitly rather than completing the picture — per
`docs/99-backlog/NO-INVENTION-RULES.md`.

---

## 1. Executive Summary

The documentation corpus is a well-designed governance and requirements
*scaffold* — registries, a documentation-authority matrix, a no-invention
rule set, a specification taxonomy — sitting on very little populated
scientific content. Two concrete inconsistencies were found and corrected
as mechanical fixes (see §9). One structural issue — duplicate `S02`/`S03`
document identifiers in `03-scientific-specification` — was found,
recorded, and left for a human decision (see §13), since resolving it
requires choosing a permanent document-identity scheme, which
`docs/99-backlog/DOCUMENT-AUTHORITY-MATRIX.md` explicitly reserves for
human judgment. The largest gap is not an inconsistency but an absence:
`docs/02-research` specifies research *methodology* in detail but contains
almost no actual literature findings (one registered source in
`RESEARCH-REGISTRY.md`), even though `03-scientific-specification` through
`10-certification` are all designed to build on "validated research
knowledge" that does not yet exist in the repository.

---

## 2. Area-by-Area Findings

- **00-project** — registries exist and are structurally complete
  (correct templates, correct statuses) but contain only seed content: 3
  assumptions, 10 decisions, 4 change-queue items (now 5, see §9/§13), 7
  knowledge-backlog items, 9 open questions, 1 registered research source.
- **01-governance** (`P00-project-governance.md`) — the most fully
  developed document: authority hierarchy, autonomy boundaries, invariants,
  tranche model.
- **02-research** — R01–R08 are extensive but are process specifications
  (how to search/classify/evaluate literature), not a literature review.
  No watermark family, detector, or benchmark is actually named or
  compared anywhere in the reviewed files.
- **03-scientific-specification** — extensive requirement taxonomies
  (S01–S03, `SPECIFICATION-MAP.md`), explicitly in "structural-definition
  phase" (`SPECIFICATION-MAP.md` §46) with no thresholds or algorithms
  chosen yet, by design. Contains the S02/S03 identifier collision — see
  §4 and §13.
- **04-architecture through 10-certification** — each area is a single
  "MAP" document, conceptually detailed but explicitly stating it is in a
  definition phase with no sub-documents yet created. `SPECIFICATION-MAP.md`
  §44 lists twelve candidate sub-documents that do not exist; the other
  MAPs follow the same pattern (confirmed by file listing; sub-document
  content itself was not deep-read in this pass beyond the MAP files).
- **99-backlog** — this is the project's own self-audit machinery
  (inventory status, consolidation queue/instructions, authority matrix,
  no-invention rules, document-authority matrix). Before this pass, that
  machinery had never been applied to the corpus it governs.

---

## 3. Authority Conflicts

None found at the area-to-area level (the level `DOCUMENT-AUTHORITY-MATRIX.md`
governs) in the documents reviewed. This does not confirm their absence —
a full cross-area audit (Q001) has not been run. The S02/S03 duplication
in §4 is a document-identity conflict within a single area, not an
area-authority conflict, so it is tracked separately.

---

## 4. Duplications

- **S02/S03 identifier collision** (`docs/03-scientific-specification`):
  `S02-scientific-requirements.md` and `S02-fidelity-requirements.md` both
  claim the `S02` identifier; `S03-experimental-model.md` and
  `S03-transformation-requirements.md` both claim `S03`. The two
  "duplicate" files are both marked `Status: NORMATIVE / DRAFT FOR
  CONSOLIDATION` and use a `Related:` field instead of the `Depends on:`
  field the non-draft S02/S03 use — suggesting they were written as
  drafts awaiting a numbering/consolidation decision that was never made.
  Their content does not read as redundant with the non-draft documents:
  fidelity/transformation requirements map onto distinct boundary
  categories already listed in `SPECIFICATION-MAP.md` §3 ("content-preservation
  requirements", "transformation-minimality requirements"). Filed as
  DCQ-005; see §13 for proposed resolution options.
- **CLAUDE-CONSOLIDATION-INSTRUCTIONS.md vs CLAUDE-CONSOLIDATION-QUEUE.md**:
  near-duplicate documents, both `Status: QUEUED`, both describing the same
  consolidation task with overlapping but not identical structure
  (INSTRUCTIONS is a 12-phase procedure; QUEUE is a shorter scope/output
  spec). Not contradictory, but redundant. No action taken — flagged as
  REVIEW REQUIRED (§12): consider whether QUEUE should become a pointer to
  INSTRUCTIONS rather than a parallel document.

---

## 5. Contradictions

- **INVENTORY-STATUS.md vs POST-INVENTORY-QUEUE.md Q002** (found and
  corrected — see §9): `INVENTORY-STATUS.md` (later edit) recorded all
  areas 00–10 as `INVENTORIED`; `POST-INVENTORY-QUEUE.md` Q002 (earlier
  edit) still showed areas 00–05 unchecked and status `IN PROGRESS`. The
  two files disagreed about whether inventory was complete. Corrected by
  syncing Q002 to the later, already-decided status in
  `INVENTORY-STATUS.md` — no new inventory judgment was made; see the
  reconciliation note left in `POST-INVENTORY-QUEUE.md` itself.

No other contradictions were confirmed in this pass. The full contradiction
sweep specified in `CLAUDE-CONSOLIDATION-INSTRUCTIONS.md` Phase 4 (offline
operation, human approval, certification, security, versioning, etc.
across all areas) requires reading 04–10 at sub-document depth, which this
pass did not do.

---

## 6. Terminology Issues

Not assessed at the depth `CLAUDE-CONSOLIDATION-INSTRUCTIONS.md` Phase 5
requires (a term-by-term pass across all areas for words like *capability*,
*experimental*, *active*, *deprecated*, etc.). `UNKNOWN — INSUFFICIENT
PROJECT EVIDENCE` for this phase; recommend it be run together with the
full Q001 audit rather than piecemeal, since terminology consistency is
easiest to judge with all areas open at once.

---

## 7. Missing Cross-References

- `SPECIFICATION-MAP.md` §44 ("Required Detailed Specification Documents")
  lists candidate future documents but does not reference
  `S02-fidelity-requirements.md` or `S03-transformation-requirements.md`,
  which already exist in draft form. Once DCQ-005 is resolved,
  `SPECIFICATION-MAP.md` should be updated to reflect their actual state.

---

## 8. Scientific Uncertainties

The dominant uncertainty is structural rather than a specific unresolved
number: `RESEARCH-REGISTRY.md` contains one registered source
(Kirchenbauer et al., watermarking) while `03-scientific-specification`
through `10-certification` are designed on the premise that requirements,
thresholds and architecture decisions will be derived from "validated
research knowledge" (`SPECIFICATION-MAP.md` §1). Until the research layer
is populated, every downstream area's substantive content is necessarily
provisional — which the documents themselves acknowledge (e.g.
`SPECIFICATION-MAP.md` §46 "structural-definition phase"). This is not a
contradiction to resolve; it is the project's actual current state, and
`docs/00-project/OPEN-QUESTIONS.md` / `KNOWLEDGE-BACKLOG.md` already track
pieces of it (Q-001, Q-003, Q-007, Q-008; KB items on versioned
effectiveness and the storage budget).

---

## 9. Security-Sensitive Findings

None identified in this pass. `docs/06-security/SECURITY-MAP.md` was
reviewed only at the level of an earlier status summary, not re-audited
here for this report. No security-relevant document was modified.

---

## 10. Certification-Sensitive Findings

`docs/10-certification/CERTIFICATION-MAP.md` is, like the other MAP
documents, a single conceptual document with no sub-documents and no
recorded certification of any capability. Per
`docs/99-backlog/DOCUMENT-AUTHORITY-MATRIX.md` ("Certification"), its
existence must not be read as implying any capability is certified — none
is claimed to be, and this report does not introduce any such claim.

---

## 11. Proposed Automatic Changes — APPLIED

Both classified `SAFE AUTOMATIC CHANGE` per
`CLAUDE-CONSOLIDATION-INSTRUCTIONS.md` Phase 10 (mechanical, non-semantic,
no requirement content altered):

1. **`docs/99-backlog/POST-INVENTORY-QUEUE.md`** — Q002 checklist and
   status synced to match the later-dated `INVENTORY-STATUS.md`
   conclusion (see §5). A reconciliation note was left in place explaining
   the change and pointing to this report.
2. **`docs/02-research/RESEARCH-MAP.md`** — removed a trailing, unfinished
   fragment of Italian conversational text (an unclosed code block
   starting `## 2. Perché questo è il passo giusto...`) appended after the
   document's own "## 37. Final Principle" conclusion. This was a
   copy-paste artifact, not project content — the document's real content
   was already complete at §37.

---

## 12. Proposed Review Changes

- Consider whether `CLAUDE-CONSOLIDATION-QUEUE.md` should be retired in
  favor of `CLAUDE-CONSOLIDATION-INSTRUCTIONS.md` (or vice versa), since
  they overlap almost entirely (§4). Not executed here — retiring a
  process document is a structural decision, not a mechanical one.
- Both consolidation documents' `Status` fields still read `QUEUED`. They
  are more accurately `IN PROGRESS` now that a first pass exists. Left
  unchanged pending your confirmation this report is accepted as that
  first pass — happy to update them once you've reviewed this.

---

## 13. Human Decisions Required

- **DCQ-005 — S02/S03 identifier collision.** Recorded in
  `docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md`. Proposed resolution
  options, not yet applied:
  - **Option A (recommended):** renumber the two draft documents to the
    next free identifiers (`S04-fidelity-requirements.md`,
    `S05-transformation-requirements.md`), update their status from
    `DRAFT FOR CONSOLIDATION` to `NORMATIVE`, update their `Related:`
    fields to `Depends on:` where appropriate, and add them to
    `SPECIFICATION-MAP.md` §44/relationship sections. This treats them as
    genuinely distinct, additional specifications rather than duplicates
    of S02/S03 — supported by their content covering boundary categories
    not covered by the non-draft S02/S03 documents.
  - **Option B:** merge their content into
    `S02-scientific-requirements.md` and `S03-experimental-model.md`
    respectively, and retire the draft files (with historical information
    preserved per `DOCUMENT-AUTHORITY-MATRIX.md` "Historical Documents").
    Appropriate only if a full content comparison (not done in this pass)
    shows genuine overlap rather than complementary scope.
  - Neither option was applied — this is exactly the class of change
    `CLAUDE-CONSOLIDATION-INSTRUCTIONS.md` Phase 10 classifies as
    affecting "document authority" / "interfaces", requiring review rather
    than automatic execution.
- **Populating the research layer** (§8) is not a documentation defect to
  fix mechanically — it is substantive research work requiring a decision
  about scope, sourcing, and how much time to invest before moving to
  implementation.
- **Running the full Q001 cross-area audit** (04-architecture through
  10-certification, 18 checks) is a separate, larger undertaking than this
  pass and should be scheduled as its own piece of work if you want it
  before implementation begins.

---

## 14. Recommended Next Actions

1. Review and accept/reject the two applied automatic changes (§9) and
   this report.
2. Decide between Option A and Option B for DCQ-005 (§13); recommend
   Option A given the content-boundary evidence found.
3. Decide whether to run the full Q001 cross-area audit next, or to
   prioritize populating `02-research` with actual literature findings
   first — both were identified as blockers in the earlier project status
   report (`text-integrity-research-status.md`) and neither was addressed
   in this pass, which was scoped to inconsistencies only.
4. Once 2–3 are decided, update `CLAUDE-CONSOLIDATION-QUEUE.md` and
   `CLAUDE-CONSOLIDATION-INSTRUCTIONS.md` status fields from `QUEUED` to
   reflect this report's existence.

---

## Resolution Log

**2026-08-22 — DCQ-005 resolved, Option A applied (owner-approved).**
`S02-fidelity-requirements.md` → `S04-fidelity-requirements.md`;
`S03-transformation-requirements.md` → `S05-transformation-requirements.md`;
both promoted from `DRAFT FOR CONSOLIDATION` to `NORMATIVE`.
`SPECIFICATION-MAP.md` §44.1 added as an index of existing S0x documents.
Recorded as `DEC-011` in `docs/00-project/DECISION-LOG.md`. DCQ-005 status
set to `VERIFIED`. Remaining items in §13/§14 (research-layer population,
full Q001 audit) are unaffected and still open.

---

# SECOND PASS — Q001 Cross-Area Consistency Audit (2026-08-29)

**Scope:** the full 18-point audit defined in
`docs/99-backlog/POST-INVENTORY-QUEUE.md` Q001, covering
04-architecture through 10-certification and their cross-area
dependencies, run after the research layer (R01–R08) was populated with
101 registered sources (`docs/00-project/RESEARCH-REGISTRY.md`).
**Method:** the corpus was read by a dedicated audit pass; the Executive
Summary (§1S) and Recommended Next Actions (§14S) below were authored
directly, after independent verification of the single most consequential
claim the audit pass returned (§3S.1). This method note is included
because that verification changed the audit's own conclusion on that
item — see §3S.1.

## 1S. Executive Summary (second pass)

The audit found real cross-area drift — mainly duplicated, non-identical
vocabularies (lifecycle states, network-mode and release-status enums,
capability enumerations) and two scientific-integrity gaps not yet
tracked anywhere (non-native-writer detection bias; the base-rate/
prevalence argument for reading false-positive rates) — but **the single
finding the audit itself flagged as most consequential does not hold up**.
The audit pass reported that `S02-fidelity-requirements.md` and
`S03-transformation-requirements.md` still exist on disk, unchanged,
contradicting DCQ-005/DEC-011's record that they were renamed to S04/S05.
Independent verification directly against the live repository (not the
staged copy the audit pass read) found this to be false: DCQ-005/DEC-011
are accurate as recorded. The apparent duplication traced to two stale
files left over in this session's own upload cache from before the
2026-08-22 rename, never refreshed when the rest of the corpus was
re-staged on 2026-08-29 — a defect in this session's working copy, not in
the project. See §3S.1 for the full verification trail. That cache has
been cleared.

Because one flagged "human decision required" item turned out to be a
stale-cache artifact, the remaining findings below should be treated as
audit-pass output requiring the same "verify fourth" discipline
(`POST-INVENTORY-QUEUE.md`, Governing Rule) before any document is
changed on their basis — not as pre-verified fact. A targeted check
(comparing file modification times of the 04–10 MAP documents against
the audit's staged snapshot) found no similar staleness for those files:
none of `ARCHITECTURE-MAP.md`, `VALIDATION-MAP.md`, `SECURITY-MAP.md`,
`DATA-MAP.md`, `DEVELOPMENT-MAP.md`, `OPERATIONS-MAP.md`, or
`CERTIFICATION-MAP.md` has been modified since 2026-08-17/18, before
either staging pass — so the vocabulary and gap findings below are not
suspected of the same defect, but have not each been independently
re-read line-by-line the way §3S.1 was.

The corpus's two clean points from the first pass still hold at this
depth: certification-boundary discipline (documented / implemented /
tested / validated / certified are not conflated anywhere found) and
autonomous-execution governance are both intact.

## 2S. Area-by-Area Findings (second pass)

04-architecture through 10-certification remain single-MAP-document,
definition-phase areas, as recorded in the first pass — no sub-documents
have been created in any of them since 2026-08-22. The audit read each
MAP document in full (not only at map-level summary, unlike the first
pass) and cross-referenced them against each other and against
03-scientific-specification and 02-research. This deeper read is what
surfaced the vocabulary drift and gaps in §5S–§8S below, none of which
were visible at the shallower depth of the first pass.

## 3S. Authority Conflicts (second pass)

### 3S.1 — S02/S03 identifier collision: audit claim not confirmed (corrected)

**Audit pass claim:** `S02-fidelity-requirements.md` and
`S03-transformation-requirements.md` still exist at their original paths
in `docs/03-scientific-specification`, dated 2026-08-22, still showing
`Status: NORMATIVE / DRAFT FOR CONSOLIDATION`, alongside `S04`/`S05`
(dated 2026-08-29) — implying DCQ-005/DEC-011's resolution never actually
happened on disk.

**Verification performed (this pass, direct to the Mac):**

- `device_list_dir` on the live
  `docs/03-scientific-specification/` directory shows exactly: `S01`,
  `S02-scientific-requirements.md`, `S03-experimental-model.md`, `S04`,
  `S05`, `SPECIFICATION-MAP.md`, and a `_to_delete/` subfolder. No
  `S02-fidelity-requirements.md` or `S03-transformation-requirements.md`
  exists at the active path.
- `_to_delete/` contains
  `S02-fidelity-requirements.md.superseded-by-S04` and
  `S03-transformation-requirements.md.superseded-by-S05` — the original
  files, renamed with an explicit superseded-by suffix and moved aside,
  dated 2026-08-22 (consistent with the DCQ-005 Notes date). This is the
  established workaround this session uses for file removal, since
  `device_bash` cannot delete files on the linked Mac and instead moves
  files to a `_to_delete/` subfolder.
- A grep across the live repository for both old filenames found six
  remaining mentions — `SPECIFICATION-MAP.md`, `S04-fidelity-requirements.md`,
  `S05-transformation-requirements.md`,
  `docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md`,
  `docs/00-project/DECISION-LOG.md`, and this report — and every one is an
  explicit "Identifier history" / historical note (e.g. S04's own header:
  "Originally drafted as `S02-fidelity-requirements.md` under status
  `NORMATIVE / DRAFT FOR CONSOLIDATION`. Renumbered to `S04` on
  2026-08-22..."), not a live cross-reference to a still-active document.
- Root cause found: this session's own container upload cache
  (`/mnt/user-data/uploads/.../docs/03-scientific-specification/`) held
  leftover copies of the two old files from an 2026-08-22 staging, dated
  before the rename, that were never cleared when the rest of the corpus
  was re-staged on 2026-08-29 for this audit. The audit pass read that
  stale cache, not the live Mac filesystem. The stale files have now been
  removed from the cache.

**Conclusion:** DCQ-005 and DEC-011 are accurate. The rename completed
correctly and no live document contains an unresolved reference to the
old filenames. No document change is required. This is downgraded from
"human decision required" (as the audit pass framed it) to no action,
with one optional housekeeping note in §14S.

### 3S.2 — Other authority conflicts

None found at the area-to-area level beyond the vocabulary drift recorded
as duplications/terminology issues below (§5S/§6S), which are not
authority conflicts in `DOCUMENT-AUTHORITY-MATRIX.md`'s sense (no two
documents claim to be *authoritative* for the same category — they use
different terms for related concepts without either claiming primacy).

## 4S. Duplications (second pass)

**Corrected by follow-up verification (2026-08-29, after this pass's
findings were first drafted) — see the Fixes Applied Addendum at the end
of this document for the full verification and the cross-reference
edits made as a result:**

- Fidelity/transformation-preservation dimensions are restated, without a
  requirement-ID cross-reference, in **13 sections across 4 documents**
  (`SPECIFICATION-MAP.md` §9/§10/§11/§12/§15;
  `S02-scientific-requirements.md` §10's REQ-PRES-001–006;
  `ARCHITECTURE-MAP.md` §14/§17/§18/§19/§20;
  `VALIDATION-MAP.md` §13/§15/§18/§20) — not "approximately five" as
  first estimated. All 13 now carry an added cross-reference to the
  authoritative FID-xxx/TRN-xxx requirement in
  `S04-fidelity-requirements.md`/`S05-transformation-requirements.md`
  (or an explicit "no exact counterpart" note where none exists).
- Four independent "release readiness" checklists exist across the
  corpus with no cross-reference between them
  (`OPERATIONS-MAP.md` §183, `DATA-MAP.md` §117,
  `DEVELOPMENT-MAP.md` §108, `CERTIFICATION-MAP.md` §149) — confirmed as
  stated. All four now cross-reference the other three.
- Human-approval-gate lists: **four lists in two documents**
  (`SECURITY-MAP.md` §19 and §77; `DEVELOPMENT-MAP.md` §14 and §20), not
  "three divergent lists" across three documents as first estimated. All
  four now cross-reference the other three.

These are duplication findings, not contradictions: the audit pass did
not report that any two of these restatements conflict in substance, only
that they are repeated without a single authoritative source and a
cross-reference, which is exactly the condition
`CLAUDE-CONSOLIDATION-INSTRUCTIONS.md` Phase 3/Phase 6 asks to be
recorded rather than silently fixed.

## 5S. Contradictions (second pass)

- **Lifecycle-state vocabulary**: `SPECIFICATION-MAP.md` §5 and
  `S02-scientific-requirements.md` §24 use non-identical sets of
  lifecycle-state terms for what appears to be the same underlying
  concept (capability/requirement lifecycle).
- **Network-mode enum**: `SECURITY-MAP.md` §14 and `OPERATIONS-MAP.md`
  §136 define non-identical network-mode enumerations.
- **Release-status vocabulary**: `VALIDATION-MAP.md` §57 and
  `CERTIFICATION-MAP.md` use non-identical release-status vocabularies.
- Beyond these three specific pairs, the audit pass counted 8–10
  non-identical capability-lifecycle enumerations scattered across the
  corpus (exact set not itemized file-by-file in this write-up).

None of these were classified by the audit as a scientific or security
contradiction (no document asserts something a second document denies);
they are terminology/vocabulary drift between documents describing
related but not always identical state machines. Per
`CLAUDE-CONSOLIDATION-INSTRUCTIONS.md` Phase 5, this report does not
normalize this terminology automatically, since some of the divergence
may represent genuine conceptual distinctions (e.g. a network-mode
concept at the security boundary is not necessarily the same concept as
a network-mode concept at the operations boundary) rather than accidental
drift.

## 6S. Terminology Issues (second pass)

The vocabulary mismatches in §5S are the terminology findings for this
pass — lifecycle states, network modes, release status, and capability
enumerations are the four term families found to have multiple
non-identical definitions in force across the corpus simultaneously. No
single document is authoritative for any of the four term families
today.

## 7S. Missing Cross-References (second pass)

The four release-readiness checklists and three human-approval-gate
lists in §4S each lack a cross-reference to the others. Recommended
treatment per Phase 11 (minimal modification, prefer cross-reference over
consolidation): add cross-references between the existing lists rather
than merging them, since 04–10 are still in definition phase and a merge
now could be premature.

## 8S. Scientific Uncertainties (second pass)

Two scientific-integrity gaps were found that are not currently tracked
by any `DOCUMENTATION-CHANGE-QUEUE.md` or `KNOWLEDGE-BACKLOG.md` item:

- **Non-native-writer detection bias** (`RESEARCH-REGISTRY.md` R-0022,
  a well-confirmed research finding — see also
  `docs/02-research/R04-ai-generated-text-detection-research.md`) is
  entirely absent from 03-scientific-specification through
  10-certification, despite detection false-positive behavior being
  squarely within their scope.
- **The base-rate/prevalence argument for interpreting FPR** (R-0086,
  see `docs/00-project/OPEN-QUESTIONS.md` Q-003) is entirely absent from
  03-scientific-specification through 10-certification, despite FPR/FNR
  being the primary metrics named throughout those areas.

Neither gap is a contradiction — nothing in 03–10 asserts something these
findings would contradict. They are absences: known, registered research
findings that have not yet been connected to the requirements/
architecture/certification layers that depend on the concepts they bear
on.

## 9S. Security-Sensitive Findings (second pass)

The Network-Modes enum mismatch (§5S, `SECURITY-MAP.md` §14 vs
`OPERATIONS-MAP.md` §136) touches network access, which
`CLAUDE-CONSOLIDATION-INSTRUCTIONS.md` Phase 8 requires be classified as
requiring review rather than treated as mechanical. No security
requirement was found to be weakened by the mismatch itself (both
documents remain internally consistent; they simply enumerate the
concept differently) — flagged as REVIEW REQUIRED, not HUMAN DECISION
REQUIRED, on that basis, but see §13S.

## 10S. Certification-Sensitive Findings (second pass)

The Release-Status vocabulary mismatch (§5S, `VALIDATION-MAP.md` §57 vs
`CERTIFICATION-MAP.md`) is certification-adjacent. Consistent with the
first pass's finding, no capability is claimed to be certified anywhere
in the corpus, and this audit does not change that. The
documented/implemented/tested/validated/certified distinction
(`CLAUDE-CONSOLIDATION-INSTRUCTIONS.md` Phase 9) was checked across
04–10 during this pass and found intact — no document conflates these
states.

## 11S. Proposed Automatic Changes — APPLIED (second pass)

One `SAFE AUTOMATIC CHANGE` applied as part of processing this audit:

1. **This session's own container upload cache** — removed two stale,
   pre-rename copies of `S02-fidelity-requirements.md` and
   `S03-transformation-requirements.md` that caused the false §3S.1
   finding. This is a fix to this session's working environment, not to
   the project repository, and is recorded here only for traceability of
   why §3S.1's conclusion differs from the audit pass's original claim.

No change was made to any project document as an "automatic" change in
this pass — every substantive finding above (§4S–§8S) is classified
REVIEW REQUIRED or HUMAN DECISION REQUIRED below, consistent with
`CLAUDE-CONSOLIDATION-INSTRUCTIONS.md` Phase 10 (terminology and
lifecycle-state changes are explicitly listed as REVIEW REQUIRED, not
automatic).

## 12S. Proposed Review Changes (second pass)

- Reconcile or explicitly cross-reference the lifecycle-state,
  network-mode, and release-status vocabularies (§5S) — each pair should
  either adopt one shared term set or explicitly document why the
  concepts differ across the area boundary.
- Add cross-references between the four release-readiness checklists and
  the three human-approval-gate lists (§7S).
- Add requirement-ID cross-references to the ~5 restated fidelity/
  transformation-preservation dimension descriptions (§4S) rather than
  leaving them as independent prose restatements.

None of these were applied automatically, per Phase 11's preference for
cross-referencing over consolidation and Phase 10's classification of
terminology/lifecycle changes as REVIEW REQUIRED.

## 13S. Human Decisions Required (second pass)

**Resolved 2026-08-29 — see `DEC-012` in `docs/00-project/DECISION-LOG.md`.**
Owner confirmed all four items below by explicit answer, matching this
report's own recommendations: defer vocabulary reconciliation; keep the
checklists/approval-gate lists separate and only cross-referenced; keep
DCQ-007 PENDING (matching DCQ-006); leave `_to_delete/` in place.

- **Non-native-writer detection bias and the base-rate/prevalence
  argument (§8S)** — both are confirmed research findings with no home in
  03-scientific-specification through 10-certification yet. Recommend
  adding both as an entry to `docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md`
  (a new DCQ) rather than editing 03-10 directly, since those areas are
  still in definition phase and DCQ-006 already establishes the pattern
  of deferring propagation into definition-phase areas until they are
  drafted. This is a scope/priority decision, not a mechanical edit.
- **Vocabulary reconciliation timing (§5S/§12S)** — whether to reconcile
  the lifecycle-state / network-mode / release-status vocabularies now,
  or defer until 04–10 leave definition phase (at which point there will
  be more content to reconcile at once, but also more places the drift
  could compound). Recommend deferring to match the definition-phase
  status of the affected areas, but this is the human owner's call, not
  a mechanical one.
- ~~S02/S03 identifier collision~~ — resolved; see §3S.1. No longer a
  human decision item (superseded by direct verification in this pass).

## 14S. Recommended Next Actions (second pass)

1. Accept or reject this pass's one applied change (§11S — cache cleanup
   only, no project document was altered).
2. Decide whether to open a new DCQ for the two scientific-integrity gaps
   in §8S (non-native-writer bias, base-rate/prevalence), scoped the same
   way DCQ-006 is scoped (recorded now, executed once the relevant 03-10
   areas leave definition phase).
3. Decide the timing for reconciling the three vocabulary mismatches in
   §5S (now vs. deferred to post-definition-phase) — recommend deferring,
   consistent with the areas' own stated definition-phase status.
4. Optional housekeeping: `docs/03-scientific-specification/_to_delete/`
   on the Mac still holds the two superseded S02/S03 files (renamed,
   harmless, out of the active tree). `device_bash` cannot delete files,
   so removing that folder — if wanted — needs to be done manually on the
   Mac, or left in place indefinitely as an informal historical record;
   neither choice requires further action from this project's own
   governance rules.
5. Update `docs/99-backlog/POST-INVENTORY-QUEUE.md` Q001 status from
   `QUEUED` to `COMPLETE` (done alongside this report — see that file).
6. Given one of this audit's own findings (§3S.1) did not survive direct
   verification, apply the same spot-check discipline before acting on
   §5S/§8S if any of those items look surprising once you look at the
   cited sections yourself — this report's confidence in §5S/§8S rests on
   file-mtime evidence that the audit read unmodified source files (see
   §1S), not on a second independent re-read of each citation.

---

## Fixes Applied Addendum (2026-08-29, same day as SECOND PASS)

Owner authorized proceeding directly from audit to fixes ("procediamo con
l'audit e gli eventuali fix che ne conseguono"). Before applying any fix,
every §4S/§5S item was independently re-read at file+section level (a
dedicated verification pass, not a re-use of the original audit pass's
own citations), per the "verify fourth" discipline this report itself
recommends in §14S.6 — necessary because §3S.1 already showed the
original audit pass could be wrong. That verification corrected two
counts (§4S, above) and confirmed all three vocabulary pairs and their
exact section numbers (§5S) exactly as the audit pass first reported —
no further staleness or citation errors were found.

**Fixes applied — all classified SAFE AUTOMATIC CHANGE (mechanical,
additive cross-references; per Phase 10, "unambiguous cross-reference
additions") or, for the three vocabulary pairs, the minimal step Phase 11
ranks above correction/consolidation ("add a cross-reference"), with the
actual vocabulary unification left as the HUMAN DECISION REQUIRED item
recorded in §13S — no requirement content, term set, or checklist item
was altered or merged:**

- 20 cross-references added at the 13 fidelity/transformation-preservation
  restatement locations found in §4S (some locations map to two IDs, e.g.
  Minimality → FID-021 + TRN-007, hence 20 edits for 13 locations),
  pointing each restatement to its authoritative FID-xxx/TRN-xxx
  requirement in `S04-fidelity-requirements.md` /
  `S05-transformation-requirements.md`, or noting explicitly where no
  exact counterpart exists (`S02-scientific-requirements.md`
  REQ-PRES-006).
- 6 cross-references added between the three vocabulary-mismatch pairs
  (§5S): `SPECIFICATION-MAP.md` §5 ↔ `S02-scientific-requirements.md` §24;
  `SECURITY-MAP.md` §14 ↔ `OPERATIONS-MAP.md` §136; `VALIDATION-MAP.md`
  §57 ↔ `CERTIFICATION-MAP.md` §3. Each note states both vocabularies,
  what's shared vs. divergent, and points to this report for the human
  decision on which (if either) should become authoritative.
  `SPECIFICATION-MAP.md` §5's note also flags § 33 "Capability Lifecycle"
  as a distinct, possibly more apt comparandum if capability-level (not
  requirement-level) reconciliation is what's eventually wanted.
- 4 cross-references added between the four release-readiness checklists
  (§4S): `OPERATIONS-MAP.md` §183, `DATA-MAP.md` §117,
  `DEVELOPMENT-MAP.md` §108, `CERTIFICATION-MAP.md` §149 — each now names
  the other three.
- 4 cross-references added between the four human-approval-gate lists
  (§4S, corrected count): `SECURITY-MAP.md` §19 and §77,
  `DEVELOPMENT-MAP.md` §14 and §20 — each now names the other three.
- **DCQ-007** registered in `docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md`
  for the two scientific-integrity gaps found in §8S (non-native-writer
  detection bias, R-0022; base-rate/prevalence argument for FPR, R-0086),
  scoped the same way as DCQ-006 (recorded now, deliberately left
  PENDING execution until the relevant 03-10 areas are past
  definition phase).

**Not applied — remain HUMAN DECISION REQUIRED, per §13S:**

- Which vocabulary (if either) becomes authoritative for the three
  reconciled pairs in §5S — the cross-references make the divergence
  visible and traceable but do not resolve it.
- Whether to consolidate the four release-readiness checklists or the
  four human-approval-gate lists into single authoritative documents —
  cross-referenced, not merged, per Phase 11's preference for the
  smallest sufficient change.
- Whether/when to execute DCQ-007's actual content changes to 03-10 (as
  opposed to registering the queue item, which is done).
