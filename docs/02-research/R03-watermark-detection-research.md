# R03 — Watermark Detection Research

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Scientific research domain
**Parent:** docs/02-research/RESEARCH-MAP.md
**Methodology:** docs/02-research/R01-literature-research-methodology.md

---

# 1. Purpose

This document defines research concerning methods for detecting textual
watermarks.

The goal is to understand what can be measured, under which conditions, with
what uncertainty and with what limitations.

---

# 2. Detection Taxonomy

Potential detection categories include:

- statistical detectors;
- token-based detectors;
- distributional detectors;
- semantic detectors;
- model-based detectors;
- classifier-based detectors;
- cryptographic verification;
- metadata verification;
- hybrid detectors;
- future detection methodologies.

---

# 3. Detector Identity

Every detector used in research should be uniquely identified.

Record where possible:

- name;
- organization;
- publication;
- implementation;
- version;
- access method;
- date tested.

---

# 4. Detector Versioning

Detector updates create new evaluation conditions.

Historical detector results must remain associated with the detector version
used.

---

# 5. Detector Inputs

Record:

- text;
- language;
- length;
- encoding;
- formatting;
- preprocessing;
- relevant metadata.

---

# 6. Detector Outputs

Record the raw output whenever possible.

Examples:

- binary classification;
- probability;
- score;
- p-value;
- confidence;
- detection decision.

---

# 7. Thresholds

If a detector uses a threshold, record the threshold.

Different thresholds can produce materially different results.

---

# 8. Calibration

Where applicable investigate whether detector scores are calibrated.

---

# 9. False Positives

Measure detector behavior on appropriate human-written controls.

---

# 10. False Negatives

Measure detector behavior on appropriate generated or otherwise relevant
positive controls.

---

# 11. Detection Power

Where statistically meaningful, evaluate sensitivity to the expected signal.

---

# 12. Statistical Significance

For statistical detectors record:

- null hypothesis;
- test statistic;
- p-value;
- significance threshold;
- multiple-testing considerations.

---

# 13. Detector Independence

Different detectors should not automatically be considered independent.

Investigate shared:

- training data;
- algorithms;
- assumptions;
- benchmarks;
- source papers.

---

# 14. Detector Portfolio

The project should maintain a portfolio of relevant detection methodologies.

No single detector should permanently define the entire evaluation strategy.

---

# 15. External Detectors

External detectors may be useful as research instruments.

They must be treated as dated external observations when their implementation
or behavior cannot be independently controlled.

---

# 16. Cloud Detectors

Cloud-based detectors may be evaluated when useful.

The research record must identify:

- provider;
- service;
- date;
- configuration;
- observed output.

---

# 17. Detector Drift

A detector may change without project code changing.

Cloud results must therefore be considered time-dependent.

---

# 18. Detector Reproducibility

Classify detector reproducibility as:

- reproducible locally;
- reproducible with public resources;
- API reproducible;
- partially reproducible;
- not reproducible.

---

# 19. Detector Coverage

The evaluation portfolio should identify:

- covered methodologies;
- partially covered methodologies;
- uncovered methodologies.

---

# 20. Missing Detector

Absence of a detector must never be interpreted as evidence of absence of a
signal.

---

# 21. Detector Contradiction

Contradictory detector results must be preserved.

The project must not automatically select the most favorable result.

---

# 22. Language Evaluation

Detector performance must be evaluated separately by language where relevant.

---

# 23. Domain Evaluation

Detector performance should be evaluated across relevant domains.

---

# 24. Length Evaluation

Detector performance should be evaluated across relevant text lengths.

---

# 25. Editing Evaluation

Evaluate detector behavior after:

- human editing;
- automated editing;
- paraphrasing;
- translation;
- controlled linguistic transformations.

---

# 26. Distribution Shift

Investigate detector performance under changes in:

- model;
- language;
- domain;
- author population;
- generation method;
- time period.

---

# 27. Benchmark Dependence

Determine whether detector conclusions depend heavily on a particular
benchmark.

---

# 28. Benchmark Contamination

Investigate whether detector training or tuning may have involved evaluation
data.

---

# 29. Adversarial Robustness

Where scientifically relevant, evaluate detector behavior under controlled
adversarial conditions.

---

# 30. Detector Overfitting

Distinguish detector-specific adaptation from generalizable linguistic
effects.

---

# 31. Cross-Detector Evaluation

When multiple detectors are available, compare their behavior under identical
experimental conditions.

---

# 32. Cross-Methodology Evaluation

Where possible compare detectors based on fundamentally different approaches.

---

# 33. Human Controls

Human-written controls must be appropriately matched to the experimental
population.

---

# 34. Generated Controls

Positive controls must be generated under documented conditions.

---

# 35. Mixed Documents

Research should include mixed human/AI documents where relevant.

---

# 36. Uncertainty

Detector outcomes should preserve uncertainty where the detector provides it.

---

# 37. Binary Simplification

Do not convert continuous detector outputs into binary conclusions unless a
threshold is explicitly justified.

---

# 38. Evaluation Matrix

Maintain, where practical:

DETECTOR
×
LANGUAGE
×
DOMAIN
×
LENGTH
×
CONDITION
×
RESULT

---

# 39. Temporal Evaluation

Important detectors should be periodically reassessed because detector
technology changes.

---

# 40. New Detector Protocol

When a new detector becomes relevant:

1. register it;
2. classify its methodology;
3. assess independence;
4. identify required resources;
5. define evaluation conditions;
6. execute validation;
7. compare with existing evidence;
8. assess certification impact.

---

# 41. Detector Retirement

Obsolete detectors may be retired from active evaluation.

Historical results remain preserved.

---

# 42. Final Principle

Detector testing is evidence.

It is not itself proof of universal absence or presence of a watermark.

---

# 43. Literature Findings (2026-08-23)

Populates §2-§41 above with real detection methodologies and evidence.
Every claim is registered in `docs/00-project/RESEARCH-REGISTRY.md` under
the cited `R-XXXX` identifier. Confidence markers (EVIDENCE /
AUTHOR-REPORTED / VENDOR / UNVERIFIED) follow the R04 §39 convention. This
is a first literature pass, not a claim of research completeness.

## 43.1 Detection Taxonomy and Statistical Foundations — Populated

Addresses §2 (Detection Taxonomy) and §12 (Statistical Significance):

- **Standard statistical detection**: the one-proportion z-test on
  green-list token fraction (R-0001) remains the baseline statistical
  approach.
- **Consolidated statistical framework with low-false-positive
  guarantees** (EVIDENCE, R-0037): provides tests with guarantees valid
  even at false-positive rates below 10⁻⁶ — directly relevant to §9
  (False Positives) as a first-class research variable, and to the
  project's own general preference for conservative false-positive
  behavior over aggregate accuracy (SPECIFICATION-MAP.md §25-26).
- **Multi-key / multi-watermark detection** (EVIDENCE, R-0037): for M
  possible keys, test each independently and report the lowest p-value,
  corrected via global p ≈ 1-(1-p)^M; per-key secret vectors generated as
  circular shifts of one base vector for tractable large-scale testing.
  This directly answers §38's evaluation-matrix need to test "which
  watermark, if any" rather than assuming a single known scheme.
- **Cryptographic verification without exposing the key**: R-0035
  (public-key signature verification) and, from R02, R-0034 answer §2's
  "cryptographic verification" category with two real, structurally
  different mechanisms (public-key vs. computational-indistinguishability
  framings).

## 43.2 Detection Without Prior Knowledge of the Scheme

A capability not explicitly enumerated in §2's taxonomy but directly
relevant to §14 (Detector Portfolio) and §19 (Detector Coverage): can a
detector identify a watermark without knowing which scheme or key was
used?

- Third-party, non-intrusive detection frameworks exist (identified,
  title/abstract-level verification only — not deep-read in this pass)
  that build a reference set of paired watermarked/unwatermarked outputs
  from a provider and train a proxy scoring ensemble, without needing the
  provider's secret key or algorithm details.
- A separate zero-knowledge-proof approach (identified, title/abstract
  level only) lets a verifier confirm a detection result is correct
  without the secret key being revealed, adapting known schemes (including
  Kirchenbauer/R-0001 and SynthID/R-0014) into ZKP-friendly circuits.

These are recorded as an identified capability gap the taxonomy in §2
should eventually name explicitly ("key-agnostic" or "third-party"
detection), pending a deeper read of the underlying papers before their
specific claims are relied upon.

## 43.3 Detection in Mixed / Long Documents — Populated

Addresses §35 (Mixed Documents) and §38 (Evaluation Matrix length
dimension):

- **WaterSeeker** (EVIDENCE, R-0038): a two-stage pipeline (cheap
  anomaly-flagging, then local verification) for localizing watermarked
  segments within long, only-partly-watermarked documents. This is
  materially different from — and more realistic than — a whole-document
  statistical test, since real-world input is often mixed human/AI
  content (R04 §7 Hybrid Text; Turnitin's own disclosed sentence-boundary
  false positives, R-0030).

## 43.4 Detector Robustness and Attack Findings — Populated

Cross-references R02 §37.2 rather than duplicating it: the paraphrasing
near-universal-removal finding (R-0039), the spoofing/piggyback trade-off
findings (R-0040, UNVERIFIED specific figures), and the oracle-query
public-API risk (R-0040) all apply directly to detector design choices —
in particular, the oracle-query finding is a §16 (Cloud Detectors) /
06-security consideration: exposing a public detection API without rate
limiting or access control may itself constitute an attack surface for
watermark stealing (R-0015) or removal.

## 43.5 Detector Independence and Portfolio — Partially Populated

Addresses §13 (Detector Independence) and §14 (Detector Portfolio): the
detector families registered across R-0001, R-0013, R-0014, R-0032
through R-0036 share a common lineage (several build directly on the
green-list/red-list idea) and should NOT be treated as independent
evidence sources without accounting for that shared ancestry, per §13.
Cryptographic detection (R-0034, R-0035) is the most methodologically
distinct family from the statistical ones. A full independence assessment
(which specific pairs of detectors share training data, benchmarks, or
source-paper lineage) was not performed in this pass and remains open.

## 43.6 Items Requiring Follow-Up Before Being Treated as Established

1. The two "detection without prior key knowledge" papers (§43.2) were
   identified but not deep-read — their specific methodology claims
   should be verified directly before being relied upon or given full
   registry entries.
2. A full cross-detector independence analysis (§43.5) has not been
   performed — this is a candidate for the eventual Q001 cross-area audit
   or a dedicated follow-up research task.
3. As in R02 §37.5, all AUTHOR-REPORTED figures cited above (from R-0040,
   R-0041, R-0044) remain unverified pending independent replication.