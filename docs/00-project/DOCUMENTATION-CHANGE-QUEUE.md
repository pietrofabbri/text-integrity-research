# Documentation Change Queue

## Purpose

This queue records known changes that must be propagated through the
documentation and project knowledge graph.

It is a work queue for Claude Code.

It prevents new knowledge from being captured in one document while
remaining absent from affected documents.

---

# Rule

A change is not considered fully incorporated until:

1. affected documents have been identified;
2. required updates have been performed;
3. references have been checked;
4. contradictions have been checked;
5. traceability has been checked;
6. the queue item has been closed.

---

# Statuses

- PENDING
- IN_PROGRESS
- BLOCKED
- VERIFIED
- CLOSED

---

# Priority

- CRITICAL
- HIGH
- MEDIUM
- LOW

---

# Template

## DCQ-XXX — Title

### Trigger

What caused the documentation change.

### Source

Research / Decision / Backlog / Question / Implementation.

### Required Updates

List known affected documents.

### Potentially Affected Areas

Areas that must be searched even if not explicitly listed.

### Required Verification

Checks to perform.

### Status

PENDING

### Notes

---

# Initial Queue

## DCQ-001 — Establish Layered Documentation Architecture

### Trigger

Project governance design.

### Required Updates

- Project Map
- Governance
- Development
- Certification

### Required Verification

- all references resolve;
- no conflicting hierarchy;
- governance authority is consistent;
- documentation lifecycle is defined.

### Status

PENDING

---

## DCQ-002 — Introduce Capability Lifecycle

### Trigger

Maintainability requirement.

### Required Updates

- Architecture
- Development
- Operations
- Certification
- Project Map

### Required Verification

Verify that all major capability types have:

- lifecycle;
- version;
- status;
- dependencies;
- validation status;
- retirement path.

### Status

PENDING

---

## DCQ-003 — Introduce Versioned Effectiveness Profiles

### Trigger

Scientific uncertainty and evolving detection methodologies.

### Required Updates

- Research
- Scientific Specification
- Validation
- Certification

### Status

PENDING

---

## DCQ-004 — Introduce External Evidence Boundary

### Trigger

Decision to permit cloud detector/evidence services while preserving
offline core execution.

### Required Updates

- Architecture
- Security
- Validation
- Operations
- Data

### Status

PENDING

---

## DCQ-005 — Resolve Duplicate S02/S03 Identifiers in Scientific Specification

### Trigger

Documentation consolidation review (2026-08-22) found that
`docs/03-scientific-specification` contains two documents each labeled
`S02` and two each labeled `S03`:

- `S02-scientific-requirements.md` (Status: NORMATIVE) and
  `S02-fidelity-requirements.md` (Status: NORMATIVE / DRAFT FOR
  CONSOLIDATION);
- `S03-experimental-model.md` (Status: NORMATIVE / SCIENTIFIC) and
  `S03-transformation-requirements.md` (Status: NORMATIVE / DRAFT FOR
  CONSOLIDATION).

`SPECIFICATION-MAP.md` does not currently reference the two "DRAFT FOR
CONSOLIDATION" documents anywhere, including in its §44 list of candidate
future specification documents. Their content does not appear redundant
with the non-draft S02/S03 documents — `S02-fidelity-requirements.md`
covers content-preservation requirements and `S03-transformation-requirements.md`
covers transformation-minimality requirements, both distinct boundary
categories listed in `SPECIFICATION-MAP.md` §3 — but this has not been
confirmed by a full content review, and the identifier collision itself
has not been resolved by anyone.

### Source

Documentation consolidation review — see
`docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`.

### Required Updates

- `docs/03-scientific-specification/SPECIFICATION-MAP.md`
- `docs/03-scientific-specification/S02-fidelity-requirements.md`
- `docs/03-scientific-specification/S03-transformation-requirements.md`
- `docs/99-backlog/DOCUMENT-AUTHORITY-MATRIX.md` (if the resolution
  establishes a general rule for future ID collisions)

### Potentially Affected Areas

- 04-architecture, 05-validation (both list `03-scientific-specification`
  as a supporting/primary authority and may reference S02/S03 by ID)

### Required Verification

- every document that cites "S02" or "S03" resolves unambiguously to one
  file;
- `SPECIFICATION-MAP.md` §44 reflects the true state (these documents
  already exist, in draft form, rather than being only "candidate future
  documents");
- no requirement content is altered as a side effect of renumbering.

### Status

VERIFIED

### Notes

Resolved 2026-08-22 per Option A (owner-approved): renamed
`S02-fidelity-requirements.md` → `S04-fidelity-requirements.md` and
`S03-transformation-requirements.md` → `S05-transformation-requirements.md`,
changed their status from `DRAFT FOR CONSOLIDATION` to `NORMATIVE`, updated
internal cross-references, and added an index (§44.1) of existing
specification documents to `SPECIFICATION-MAP.md`. No requirement content
(FID-xxx / TRN-xxx items) was altered. Decision recorded as `DEC-011` in
`docs/00-project/DECISION-LOG.md`. The old `S02-fidelity-requirements.md`
and `S03-transformation-requirements.md` filenames no longer exist —
references to them elsewhere in the repository should be updated to the
new filenames when encountered.

---

## DCQ-006 — Propagate R02/R03/R04/R05 Literature Findings Beyond the Research Layer

### Trigger

A first literature-research pass populated real findings into
`docs/02-research/R04-ai-generated-text-detection-research.md` §39,
`docs/02-research/R02-watermark-research.md` §37, and
`docs/02-research/R03-watermark-detection-research.md` §43 (2026-08-23),
registering 44 new sources (`R-0002`-`R-0045`) in
`docs/00-project/RESEARCH-REGISTRY.md`. Per `RESEARCH-MAP.md` §20
(Research-to-Documentation Rule), "a new scientific finding must be
propagated to all materially affected documents" and "the discovery
document is not necessarily the final location of the requirement." This
propagation has not yet been performed — the findings currently exist
only within the research layer itself.

**Update (2026-08-24)**: a second pass populated
`docs/02-research/R05-multilingual-linguistic-research.md` §47, adding
28 further sources (`R-0046`-`R-0073`) and two findings that widen this
item's scope: (a) a correction to KB-008 — detection evidence now exists
for all 13 target languages, though depth varies and watermarking
evidence remains thin (see R05 §47.1, KB-008's Correction note); (b) a
new attack class, translation-based watermark/detector evasion, distinct
from the paraphrasing evasion already noted below (see R05 §47.3,
KB-011).

### Source

Research (R02 §37, R03 §43, R04 §39, R05 §47); Knowledge Backlog (KB-008,
KB-009, KB-010, KB-011).

### Required Updates

Not yet performed — listed here as required, not as completed:

- `docs/03-scientific-specification/SPECIFICATION-MAP.md` §20-22
  (per-language capability-state defaults should reflect the corrected
  KB-008 picture — evidence exists for all 13 languages at varying depth,
  detection evidence is generally ahead of watermarking evidence, and
  capability states should be assessed per-language rather than via a
  uniform default);
- `docs/03-scientific-specification` generally, for any requirement that
  implicitly assumes watermark-based or classifier-based detection is
  reliable after paraphrasing (contradicted by R-0039: detection rate
  <0.3 after one paraphrase pass for all evaluated schemes) or after
  translation (KB-011: R-0065/R-0066/R-0068/R-0069, AUC/F1 dropping to
  0.55-0.82 depending on scheme and language pair), or assumes a single
  detector/watermark family is sufficient (contradicted by §29/§13
  independence concerns, R02 §37.1, R03 §43.5);
- R02 §37.2 and R03 §43.4 themselves should eventually be amended to name
  translation-based evasion as a distinct attack category alongside
  paraphrasing (KB-011) — a research-layer-internal update, lower
  priority than the cross-area propagation below;
- 06-security (currently MAP-only): the oracle-query / public-detection-API
  attack surface noted in R03 §43.4 and R02 §37.2 (R-0040), and the
  translation-evasion attack surface (KB-011), are concrete, citable
  findings for whenever 06-security moves past its definition phase;
- 10-certification (currently MAP-only): no capability should be
  certified for a language or against a threat model beyond what R02/R03/
  R04/R05's evidence currently supports.

### Potentially Affected Areas

04-architecture, 05-validation, 06-security, 10-certification — all
currently single-MAP-document definition-phase areas (per their own MAP
documents); this item records that they must be revisited once each area
moves out of pure definition phase, not that they need updating today.

### Required Verification

- each affected document, once drafted, cites the specific `R-XXXX`
  identifier it relies on rather than restating the finding unsourced;
- no affected document asserts confidence beyond what its cited registry
  entry's evidence class (EVIDENCE / AUTHOR-REPORTED / VENDOR / UNVERIFIED)
  supports;
- KB-008 and KB-010's proposed capability-state defaults are checked
  against whatever per-language states 03-scientific-specification
  eventually assigns.

### Status

PENDING

### Notes

Deliberately left PENDING rather than executed in this pass: 04-architecture,
05-validation, 06-security, and 10-certification are all still in the
structural-definition phase (their own MAP documents say so), so there is
not yet a concrete document to edit in most of them. This entry exists so
the obligation is not lost once those areas are developed further, per
`RESEARCH-MAP.md` §20's rule that a finding's home document is not
necessarily where it was discovered.