# Start Here

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Orientation guide (non-authoritative)
**Project:** Text Integrity Research
**Date:** 2026-09-12

---

# 1. Purpose

This document orients a new reader — human or AI — arriving at this
repository with no prior context. It answers: what is this project,
how is the documentation organized, what is the current state, and
where do I go for X.

This document is **not authoritative**. Every claim below is a pointer
to the document that actually governs that topic, per
`docs/99-backlog/DOCUMENT-AUTHORITY-MATRIX.md`. If this guide and a
linked document disagree, the linked document wins, and this guide is
out of date and should be corrected.

---

# 2. What this project is

Text Integrity Research is a scientific research and evaluation
platform for four related problems: textual watermarking, watermark
detection, AI-generated-text detection, and controlled textual
transformation. It is explicitly **not** a single "AI detector" — see
`docs/00-project/DECISION-LOG.md` DEC-001/DEC-002 and
`docs/03-scientific-specification/S01-system-objectives.md` §4: no
single detector, watermark family, or metric is treated as ground
truth anywhere in the design.

The production runtime is required to run fully offline/local (no
mandatory dependency on an external generative-AI service — DEC-001),
targets 13 languages initially, and has a local storage budget of
roughly 30GB (`docs/00-project/KNOWLEDGE-BACKLOG.md` KB-006/KB-007).

Full statement of objectives: `docs/00-project/PROJECT-MAP.md`,
`docs/03-scientific-specification/S01-system-objectives.md`.

---

# 3. How the documentation is organized

Eleven numbered areas (`docs/00-project` through `docs/10-certification`)
plus a working-queue area (`docs/99-backlog`). The authoritative map of
this structure is `docs/00-project/PROJECT-MAP.md`; this section is a
one-line-per-area summary only.

- **00-project** — project-wide registries: decisions, open questions,
  assumptions, the research-source registry, the knowledge backlog, the
  documentation-change queue. Read this area first for "what has
  already been decided or discovered."
- **01-governance** — `P00-project-governance.md`: authority hierarchy,
  autonomy boundaries for AI-assisted development, the tranche model.
  The most fully developed single document in the corpus.
- **02-research** — R01 (methodology) through R08 (benchmarks/datasets):
  literature research, each with a registered, evidence-tagged
  "Literature Findings" section. 101 sources registered as of this
  writing. See §5 below for the evidence-tagging convention.
- **03-scientific-specification** — S01 (objectives) through S05
  (transformation requirements), plus `SPECIFICATION-MAP.md`. Out of
  structural-definition phase; the only specification area with
  populated normative requirements (`REQ-*`, `FID-*`, `TRN-*` families).
- **04-architecture through 10-certification** — each area was originally
  a single MAP document (e.g. `ARCHITECTURE-MAP.md`, `SECURITY-MAP.md`),
  explicitly in structural-definition phase: no sub-documents, concepts
  defined but not all thresholds/algorithms chosen. **As of 2026-09-12/13
  (`DECISION-LOG.md` DEC-014, DEC-020, DEC-021, DEC-022), 04-architecture
  is the exception**: it now also has `CAPABILITY-ARCHITECTURE.md`,
  `DATA-MODEL.md`, `VALIDATION-ARCHITECTURE.md`, `ANALYSIS-ARCHITECTURE.md`,
  `LANGUAGE-ARCHITECTURE.md`, `CORE-ARCHITECTURE.md` and
  `EXTERNAL-INTEGRATION-ARCHITECTURE.md`, per a tranche plan in
  `ARCHITECTURE-MAP.md` §64. All seven formalize generic mechanisms only
  and still select no specific detector, model, tokenizer, interface
  technology, external provider or algorithm, so 04-architecture remains
  in definition phase in substance even though it is no longer
  single-document. 05-validation through 10-certification are unaffected
  by this update. Do not read a MAP document's (or these seven
  sub-documents') existence as implying the capability it describes is
  implemented, tested, validated, or certified —
  `docs/99-backlog/DOCUMENT-AUTHORITY-MATRIX.md` and
  `CLAUDE-CONSOLIDATION-INSTRUCTIONS.md` Phase 9 are explicit that these
  states must never be conflated.
- **99-backlog** — the project's own self-audit machinery:
  `NO-INVENTION-RULES.md`, `DOCUMENT-AUTHORITY-MATRIX.md`,
  `CLAUDE-CONSOLIDATION-INSTRUCTIONS.md` (the governing consolidation
  process), `CLAUDE-CONSOLIDATION-REPORT.md` (findings from applying
  it), `POST-INVENTORY-QUEUE.md` (deferred cross-area work).

---

# 4. Where authority lives, by topic

This is a summary of `docs/99-backlog/DOCUMENT-AUTHORITY-MATRIX.md` —
consult it directly for anything not covered here.

| Topic | Authoritative document |
|---|---|
| Project governance, autonomy boundaries | `docs/01-governance/P00-project-governance.md` |
| Decisions actually made | `docs/00-project/DECISION-LOG.md` |
| Unresolved questions | `docs/00-project/OPEN-QUESTIONS.md` |
| Registered research sources | `docs/00-project/RESEARCH-REGISTRY.md` |
| Scientific requirements | `docs/03-scientific-specification/S02-scientific-requirements.md` |
| Fidelity/preservation requirements | `docs/03-scientific-specification/S04-fidelity-requirements.md` |
| Transformation requirements | `docs/03-scientific-specification/S05-transformation-requirements.md` |
| Evidence-invention rules | `docs/99-backlog/NO-INVENTION-RULES.md` |

A requirement ID prefix tells you which document owns it:
`REQ-PRES-*`/`REQ-STAT-*`/`REQ-DOC-*` etc. → S02;
`FID-*` → S04; `TRN-*` → S05.

---

# 5. The two conventions that hold the corpus together

**Evidence tagging** (`docs/99-backlog/NO-INVENTION-RULES.md`): every
research claim is tagged with an evidence class — DOCUMENTED FACT,
IMPLEMENTED FACT, VERIFIED FACT, RESEARCH EVIDENCE, INFERENCE,
PROPOSAL, or UNKNOWN — and, within the research layer specifically,
findings additionally carry EVIDENCE / AUTHOR-REPORTED / VENDOR /
UNVERIFIED confidence markers. A claim without a citation and a class
is not something this project accepts as fact, wherever it appears.

**Inventory → Audit → Change → Verify**
(`docs/99-backlog/POST-INVENTORY-QUEUE.md`, Governing Rule): contradictions
found during an inventory or audit pass are *recorded*, not silently
reconciled. Reconciliation is a separate, deliberate step, and every
change is checked afterward. This is why you will find documents that
knowingly disagree with each other, each carrying a cross-reference to
the other and to the report that found the disagreement, rather than
one being silently "fixed" — see
`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md` for worked examples.

---

# 6. Current state snapshot (2026-09-13, updated)

- **Research**: 121 sources registered (`R-0001`–`R-0121`) across **nine**
  domains, R01–R09 — R09 (Local Deployment Feasibility Research) was
  confirmed 2026-09-12 (`DECISION-LOG.md` DEC-013); each domain document
  has a populated "Literature Findings" section.
- **Decisions**: 23 recorded (`DEC-001`–`DEC-023`) in `DECISION-LOG.md`.
  `DEC-016` (2026-09-12) partially executes DCQ-006/007/008 into
  `03-scientific-specification` per the owner's explicit instruction,
  while continuing to defer their 04-10 portions. `DEC-017` (same day)
  reassesses whether that propagation unblocks `ARCHITECTURE-MAP.md` §64.4
  Tranche 3 — conclusion at that point: not yet. `DEC-018` (same day)
  performs the missing per-language capability-state assignment:
  `SPECIFICATION-MAP.md` §22.1 assigns `RESEARCH_ONLY`/`NOT_SUPPORTED`
  states per language for AI-detection, watermarking and factual/claim-
  consistency (semantic-similarity intentionally excluded, insufficient
  per-language evidence). `DEC-019` (2026-09-13) re-reassesses Tranche 3
  in light of `DEC-018`: `ANALYSIS-ARCHITECTURE.md` and
  `LANGUAGE-ARCHITECTURE.md` reassessed as **structurally ready to draft**;
  `TRANSFORMATION-ARCHITECTURE.md` remains premature — it needs
  actually-`VALIDATED` capabilities, which documentation work alone
  cannot supply. `DEC-020` (same day) executes that drafting: both
  documents now exist, per `DEC-004`'s macro-tranche-boundary
  confirmation, given separately and explicitly. `DEC-021` (same day,
  following the owner's request for a recommendation on the next
  priority) triages the six remaining unevaluated `§64.4` candidates
  against a different, evidence-independent readiness test: it executes
  drafting of `CORE-ARCHITECTURE.md` (formalizing §3-8, the execution
  backbone the other five sub-documents already assume);
  `EXTERNAL-INTEGRATION-ARCHITECTURE.md` is assessed as likely similarly
  ready but not drafted; `CONFIGURATION-ARCHITECTURE.md` and
  `REPORTING-ARCHITECTURE.md` are noted but not deeply evaluated;
  `PLUGIN-ARCHITECTURE.md` is triaged as **not assessable** — it has no
  parent section in `ARCHITECTURE-MAP.md` at all. `DEC-022` (same day,
  following the owner's confirmation to proceed with that candidate)
  executes drafting of `EXTERNAL-INTEGRATION-ARCHITECTURE.md`
  (formalizing §29-31: the adapter isolation principle, the external
  data boundary's opt-in/logging/local-fallback requirements, cloud
  detector results as tagged external observations never substituted for
  a local result, and a fifth failure state — "external boundary
  unreachable" — extending `CORE-ARCHITECTURE.md` §9's taxonomy).
  `DEC-023` (same day, following the owner's confirmation to proceed with
  the deeper evaluation `DEC-021` deferred) evaluates
  `REPORTING-ARCHITECTURE.md` and `CONFIGURATION-ARCHITECTURE.md`:
  `REPORTING-ARCHITECTURE.md` is assessed **structurally ready** (its
  obligations are already scattered across every sub-document drafted so
  far); `CONFIGURATION-ARCHITECTURE.md` is found **not yet ready**, for a
  new reason — a previously unrecorded overlap between §36's content list
  and §37's (Evaluation Profiles), which `ARCHITECTURE-MAP.md` does not
  resolve. Per this project's own audit discipline, that gap is recorded
  (`ARCHITECTURE-MAP.md` §64.7) rather than silently resolved by drafting
  around it.
- **Open questions**: 9 (`Q-001`–`Q-009`) in `OPEN-QUESTIONS.md`, all
  `Status: OPEN` — each has literature-backed "Current Evidence," none
  resolved by inference. Q-008 (local models within the storage budget)
  now has a dedicated research pass (R09) — see that document and
  `OPEN-QUESTIONS.md` for why it remains `OPEN` rather than `RESOLVED`.
- **Knowledge backlog**: 15 items (`KB-001`–`KB-015`); KB-008, KB-011,
  KB-013 and KB-014 have 2026-09-12 "Update" notes recording that their
  findings are now propagated into `03-scientific-specification` (still
  `TRIAGED` — propagation is not the same as resolution).
- **Documentation change queue**: 8 items (`DCQ-001`–`DCQ-008`); 4
  (`DCQ-001`–`DCQ-004`) are `PENDING`; 3 (`DCQ-006`–`DCQ-008`) are
  `IN_PROGRESS` as of 2026-09-12 — their `03-scientific-specification`
  portions are executed (`DEC-016`), their 04-10 portions remain
  deliberately deferred per `DEC-012`'s original rationale, which still
  applies to those areas; 1 (`DCQ-005`) is `VERIFIED`.
- **Cross-area audit**: `POST-INVENTORY-QUEUE.md` Q001 (the 18-point
  04→10 consistency audit) is `COMPLETE` — see
  `CLAUDE-CONSOLIDATION-REPORT.md`, SECOND PASS. It found and
  cross-referenced (but did not unify — that's `DEC-012`'s deferral)
  three divergent vocabulary pairs and several duplicated checklists.
- **04-architecture**: no longer single-MAP-document as of 2026-09-12/13
  (`DEC-014`, `DEC-015`, `DEC-020`, `DEC-021`, `DEC-022`) —
  `CAPABILITY-ARCHITECTURE.md`, `DATA-MODEL.md`, `VALIDATION-ARCHITECTURE.md`,
  `ANALYSIS-ARCHITECTURE.md`, `LANGUAGE-ARCHITECTURE.md`,
  `CORE-ARCHITECTURE.md` and `EXTERNAL-INTEGRATION-ARCHITECTURE.md` now
  exist (Tranches 1, 2, 3a and 4 of `ARCHITECTURE-MAP.md` §64's proposed
  exit plan). All seven formalize generic mechanisms only; no specific
  detector, model, tokenizer, interface technology, external provider,
  metric or algorithm has been selected, so the area remains in
  definition phase in substance. `TRANSFORMATION-ARCHITECTURE.md` (the
  remaining Tranche 3 candidate) remains premature: `DEC-019` found its
  blocker is a different, deeper dependency (actually-`VALIDATED`
  capabilities) that `SPECIFICATION-MAP.md` §22.1's per-language
  assignment (`DEC-018`) does not resolve. Of Tranche 4's other four
  candidates: `DEC-023` assessed `REPORTING-ARCHITECTURE.md` as
  **structurally ready** (recorded next candidate, pending separate
  confirmation to draft) and `CONFIGURATION-ARCHITECTURE.md` as
  **blocked** by a newly found, previously unrecorded overlap with §37
  (Evaluation Profiles) — see `ARCHITECTURE-MAP.md` §64.7;
  `PIPELINE-ARCHITECTURE.md`'s scoping relative to `CORE-ARCHITECTURE.md`
  §6 is left open; `PLUGIN-ARCHITECTURE.md` is not assessable — no parent
  section exists for it in `ARCHITECTURE-MAP.md`.
- **05-validation through 10-certification**: still single-MAP-document,
  structural-definition phase. This remains the project's largest gap
  between what's designed conceptually and what's specified in enough
  detail to implement against.
- **Repository**: public on GitHub at
  `github.com/pietrofabbri/text-integrity-research`, in sync as of commit
  `649513a` (2026-09-12) at last check. Files from the DEC-016–DEC-023
  work (`SPECIFICATION-MAP.md`, `S02-scientific-requirements.md`,
  `S04-fidelity-requirements.md`, `DOCUMENTATION-CHANGE-QUEUE.md`,
  `KNOWLEDGE-BACKLOG.md`, `ANALYSIS-ARCHITECTURE.md`,
  `LANGUAGE-ARCHITECTURE.md`, `CORE-ARCHITECTURE.md`,
  `EXTERNAL-INTEGRATION-ARCHITECTURE.md`, `ARCHITECTURE-MAP.md`,
  `DECISION-LOG.md`, this guide) are written locally — check
  `git log`/`git status` rather than assuming sync.

---

# 7. Suggested reading order

For a human or AI encountering this project for the first time:

1. `docs/00-project/PROJECT-MAP.md` — the real map (this guide is a
   supplement, not a replacement).
2. `docs/01-governance/P00-project-governance.md` — what an
   AI-assisted development agent may and may not do here.
3. `docs/99-backlog/NO-INVENTION-RULES.md` — the evidentiary discipline
   that governs every other claim in the corpus.
4. `docs/00-project/DECISION-LOG.md` and `OPEN-QUESTIONS.md` — what's
   settled vs. still genuinely open.
5. `docs/02-research/RESEARCH-MAP.md` §34 (domain status table) — what
   research exists and how complete it is, per domain.
6. Whichever `0X-*-MAP.md` document matches the work at hand.

---

# 8. Where the unresolved work actually is

Do not infer priorities from silence. The explicit, current list of
what's deliberately deferred (and why) lives in:

- `docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md` — DCQ items `PENDING`
  (research propagation waiting on 04-10 to leave definition phase).
- `docs/00-project/OPEN-QUESTIONS.md` — all 9 questions, `Status: OPEN`.
- `docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md` §12S/§13S — audit
  findings classified REVIEW REQUIRED or HUMAN DECISION REQUIRED, with
  their disposition recorded in `DECISION-LOG.md` DEC-012 where a
  decision has since been made.

This document does not restate those lists — restating them here would
create a second, driftable copy of the same information. Read them
directly.
