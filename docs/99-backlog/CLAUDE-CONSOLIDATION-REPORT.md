# Claude Consolidation Report

**Document type:** Post-inventory consolidation report
**Status:** ACTIVE — FIRST PASS (scoped)
**Date:** 2026-08-22
**Produced per:** `docs/99-backlog/CLAUDE-CONSOLIDATION-INSTRUCTIONS.md`,
`docs/99-backlog/CLAUDE-CONSOLIDATION-QUEUE.md`
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
