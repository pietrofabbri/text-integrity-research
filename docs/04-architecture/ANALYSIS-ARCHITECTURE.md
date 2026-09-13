# Analysis Architecture

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Architecture sub-document (Tranche 3a)
**Authority:** Architectural
**Parent:** `docs/04-architecture/ARCHITECTURE-MAP.md` §9-12 (Analysis
Layer, Watermark Analysis, AI-Generated-Text Assessment, Provenance
Analysis)
**Scope:** How analytical capabilities (watermark analysis, AI-generated-
text assessment, provenance analysis) are registered, scoped per
language, and reported, without selecting any specific detector,
watermark family, or model.

---

# 1. Purpose

This document formalizes `ARCHITECTURE-MAP.md` §9-12 into a concrete
model for how analytical components are registered and how their results
are reported. It exists because §58 of that document lists
`ANALYSIS-ARCHITECTURE.md` as a candidate document; §64.4 originally
judged it premature because no per-language, per-capability evidence
record existed for detection or watermarking. `docs/00-project/
DECISION-LOG.md` DEC-018 supplied that record
(`docs/03-scientific-specification/SPECIFICATION-MAP.md` §22.1), and
DEC-019 reassessed this document as structurally ready on that basis.

Like `CAPABILITY-ARCHITECTURE.md`, `DATA-MODEL.md` and
`VALIDATION-ARCHITECTURE.md` before it, this document selects no specific
detector, watermark scheme, or model. It defines the mechanism — capability
categories, per-language state consumption, and result reporting — that
any specific analyzer would need to plug into.

---

# 2. Relationship to Other Documents

- `ARCHITECTURE-MAP.md` §9-12 is the authoritative parent; this document
  elaborates, it does not supersede.
- `docs/04-architecture/CAPABILITY-ARCHITECTURE.md` governs how an
  analytical component is registered, versioned, and gated between
  `EXPERIMENTAL` and `VALIDATED`/`ACTIVE` (that document's §6-7), and how
  its per-language state is represented (§10). This document does not
  redefine that mechanism — it identifies which capability categories
  (§3 below) belong to the analysis layer and how they consume the
  mechanism.
- `docs/03-scientific-specification/SPECIFICATION-MAP.md` §22.1 is the
  current evidence-grounded record of per-language default states for
  AI-generated-text detection (§22.1.1) and watermarking (§22.1.2). This
  document does not restate or re-derive those states — an analyzer's
  `languages` field (`CAPABILITY-ARCHITECTURE.md` §4, §10) should be
  populated consistently with §22.1's documentation defaults until the
  analyzer is actually registered and evaluated, at which point its own
  Activation Gate outcome (`CAPABILITY-ARCHITECTURE.md` §7) governs.
- `docs/03-scientific-specification/S02-scientific-requirements.md` §27
  (Scientific Ground-Truth Rule) is authoritative for the output-category
  distinctions §7 below implements architecturally.
- `docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md` DCQ-006/DCQ-007/DCQ-008
  track the propagation of specific research findings; this document does
  not resolve any of them, and does not itself perform propagation beyond
  what §22.1 already supplies.

---

# 3. Analytical Capability Categories

Restating `ARCHITECTURE-MAP.md` §9's list, this document gives concrete
architectural treatment to the three categories with a populated
per-language evidence record (§22.1) or an explicit architectural
principle already stated in §10-12 of that document:

- **Watermark analysis** (`ARCHITECTURE-MAP.md` §10) — §4 below.
- **AI-generated-text assessment** (`ARCHITECTURE-MAP.md` §11) — §5
  below.
- **Provenance analysis** (`ARCHITECTURE-MAP.md` §12) — §6 below.

The remaining categories §9 lists — language identification, segmentation,
token analysis, linguistic analysis, stylometric analysis, statistical
analysis, structural analysis, semantic analysis — are not given dedicated
treatment here: no research pass in this project has yet produced a
per-language evidence record comparable to §22.1 for them, and drafting
detailed architecture for them now would risk inventing evidence
structure ahead of research, contrary to `NO-INVENTION-RULES.md`. They
remain governed by `ARCHITECTURE-MAP.md` §9 alone until such a record
exists. This is a scope limitation, recorded here rather than silently
implied.

---

# 4. Watermark Analysis

Per `ARCHITECTURE-MAP.md` §10, a watermark analyzer is registered as one
or more `CAP-WATERMARK-*` capabilities (`CAPABILITY-ARCHITECTURE.md` §3,
§5). Each analyzer's capability record must document, per §10's field
list, mapped onto `CAPABILITY-ARCHITECTURE.md` §4's schema:

- required input, assumptions, algorithm/version → `id`, `version`;
- supported languages → `languages` (a per-language state map, never a
  single flag, per `CAPABILITY-ARCHITECTURE.md` §10);
- confidence, limitations, reproducibility, scientific source →
  `known_limitations`, `scientific_sources`.

The architecture must not assume that one watermark detector represents
all possible watermark mechanisms (`ARCHITECTURE-MAP.md` §10) — multiple
`CAP-WATERMARK-*` records may coexist per `CAPABILITY-ARCHITECTURE.md`
§13 (Multiple Candidates per Category).

**Per-language grounding.** `SPECIFICATION-MAP.md` §22.1.2 records that
watermarking evidence is markedly thinner than detection evidence for
nearly every non-English target language, with only Chinese, Japanese,
and Indonesian carrying any dedicated per-language evidence, and Japanese
specifically carrying an unresolved tension between translation-survival
evidence (favorable) and typological watermark-design difficulty
(unfavorable) — both are preserved, per `RESEARCH-MAP.md` §22
(Contradictory Evidence), rather than collapsed into one framing. A
watermark-analysis capability record for a language beyond these three
should not be proposed for `EXPERIMENTAL` status citing a scientific
source, since §22.1.2 records none — it may still be proposed as
`DISCOVERED` (`CAPABILITY-ARCHITECTURE.md` §6) if a project-internal
experiment is planned, which is a different claim than citing existing
evidence.

---

# 5. AI-Generated-Text Assessment

Per `ARCHITECTURE-MAP.md` §11, an AI-generation-assessment component
(local classifier, statistical/linguistic/stylometric measurement, or
externally supplied detector result) is registered as one or more
`CAP-DETECT-*` capabilities. Each result must retain, per §11's field
list mapped onto the Validation Result Schema pattern
(`VALIDATION-ARCHITECTURE.md` §8, restated here for the analysis layer):
analyzer identity, version, configuration, language, text length, score,
confidence, threshold, and timestamp where relevant.

Results must not be silently converted into universal truth
(`ARCHITECTURE-MAP.md` §11) — this is the same principle
`S02-scientific-requirements.md` REQ-DET-005 (Detector Independence) and
REQ-AID-003 (Detector Output Semantics) state at the requirements level,
and §7 below implements it as an explicit output-category tag.

**Per-language grounding.** `SPECIFICATION-MAP.md` §22.1.1 records a
`RESEARCH_ONLY` documentation default for all 13 target languages, but at
markedly different evidence tiers — from dedicated peer-reviewed studies
(Japanese, R-0057) to benchmark-inclusion-only coverage (Dutch, R-0049) to
figures explicitly flagged `UNVERIFIED` (Spanish/French, via BLUFF
R-0021). Critically, for Russian and Indonesian, §22.1.1 records not mere
thinness but an affirmative failure-mode finding: a trained multilingual
detector's leave-one-language-out accuracy collapses toward chance
(~53%), degenerating into labeling nearly everything as machine-generated
(R-0118). An `AI-generated-text assessment` capability record must not
treat this as equivalent to "insufficient data" — `CAPABILITY-ARCHITECTURE.md`
§4's `known_limitations` field must carry the failure-mode finding
itself, not merely note thin coverage, for any capability whose
`languages` map includes Russian or Indonesian at any state above
`DISCOVERED`.

---

# 6. Provenance Analysis

Per `ARCHITECTURE-MAP.md` §12, provenance analysis (embedded metadata,
cryptographic signatures, content credentials, document history) is
architecturally distinct from watermark analysis, and a missing
provenance signal does not prove the absence of provenance.

No research pass in this project has yet produced language-specific or
even general evidence comparable to R02-R09's watermark/detection
findings for provenance-analysis mechanisms specifically. This document
therefore does not attempt a per-language evidence table for this
category — doing so would invent a record `SPECIFICATION-MAP.md` §22
does not contain. A `CAP-PROVENANCE-*` capability record remains
structurally valid under `CAPABILITY-ARCHITECTURE.md`'s schema, but its
`scientific_sources` field would currently have nothing project-specific
to cite beyond general format/standard documentation (e.g. a content-
credentials specification), which is not itself research evidence in the
`R-XXXX` sense. This gap is recorded here as a candidate future research
item, not silently filled.

---

# 7. Output Category Tagging (Implements S02 §27, the Scientific Ground-Truth Rule)

Every analysis-layer result, regardless of category (§3), must be tagged
with which of `S02-scientific-requirements.md` §27's categories it
belongs to:

- known ground truth;
- experimentally established observation;
- detector output;
- inferred classification;
- hypothesis;
- assumption;
- unknown.

These categories must never be silently conflated (§27). In practice, the
overwhelming majority of analysis-layer results in this project are
**detector output** or **inferred classification** — a watermark
analyzer's signal score and an AI-detection classifier's probability are
both detector output, not ground truth about whether a text was
watermarked or AI-generated, however confident the score. This restates,
at the architecture level, what `ARCHITECTURE-MAP.md` §38 (Reporting
Layer) says of derived scores generally: they must never replace or be
presented as equivalent to the underlying observation. `REPORTING-ARCHITECTURE.md`
§6 (drafted after this document, DEC-024) requires this output-category
tag to travel into the report schema itself, not remain an
analysis-layer-only annotation.

---

# 8. Cross-Analyzer Independence

Per `ARCHITECTURE-MAP.md` §2 ("no single algorithm should define the
architecture") and `S02-scientific-requirements.md` REQ-DET-005/
REQ-DET-006, no single watermark analyzer or AI-detection classifier may
be treated as sufficient on its own where multiple are registered for the
same language and category. A disagreement between two `CAP-DETECT-*` or
`CAP-WATERMARK-*` capabilities for the same input is itself a measurable,
reportable result (mirroring `ARCHITECTURE-MAP.md` §21's Evaluation Layer
treatment of multi-detector evaluation) — it must not be silently
resolved by picking one analyzer's output as authoritative.

This is directly grounded in `docs/02-research/R02-watermark-research.md`
§37.1 and `docs/02-research/R03-watermark-detection-research.md` §43.5's
independence concerns, and in the robustness evidence
`SPECIFICATION-MAP.md` §23 already cites (R-0039, R-0065, R-0066, R-0068,
R-0069): a single analyzer's apparent success under one attack condition
must not be generalized to certify robustness generally.

---

# 9. Illustrative Example (Non-Binding)

Using `RESEARCH-REGISTRY.md` entries and `SPECIFICATION-MAP.md` §22.1
already on file, purely to make §5-§7's reporting behavior concrete — not
a decision to adopt any specific analyzer:

```
Input: Russian text, AI-generation-assessment request
CAP-DETECT-EXAMPLE (ru): languages map shows ru: EXPERIMENTAL (illustrative)
  known_limitations: "leave-one-language-out accuracy collapses toward
    chance for Russian (R-0118); do not treat a PASS-like score for this
    language as equivalent to a Japanese or Polish result at the same
    nominal confidence"
  output_category: detector output (S02 §27) — not ground truth, not an
    experimentally established observation for this language
```

The report must make the language-specific reliability gap visible next
to the score, not merely retrievable from a separate document.

---

# 10. What This Document Does Not Decide

This document does not: select any specific watermark scheme, detection
classifier, or provenance mechanism; resolve DCQ-006, DCQ-007 or DCQ-008;
assign capability states beyond what `SPECIFICATION-MAP.md` §22.1 already
records (this document consumes that record, it does not extend it); or
produce the per-language evidence record §6 notes is missing for
provenance analysis. All of these remain separate, later decisions or
research tasks.

---

# 11. Final Principle

An analysis layer is scientifically honest only if its outputs carry
their own epistemic status wherever they travel — a detector score is
never allowed to quietly become "the answer." This document's role is to
make sure that status (§7), the language-specific evidence it actually
rests on (§4-5, sourced from `SPECIFICATION-MAP.md` §22.1), and the
possibility of disagreement between independent analyzers (§8) are
architectural properties, not conventions that depend on each new
component's author remembering to apply them.
