# R07 — Evaluation and Statistical Methodology

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Scientific research domain
**Parent:** docs/02-research/RESEARCH-MAP.md
**Methodology:** docs/02-research/R01-literature-research-methodology.md

---

# 1. Purpose

This document defines research principles for designing, executing and
interpreting project experiments.

---

# 2. Evaluation Philosophy

Evaluation must measure the property actually claimed.

A convenient metric must not silently become a substitute for the intended
scientific property.

---

# 3. Primary Objectives

Evaluation should quantify, where relevant:

- detection behavior;
- watermark response;
- semantic preservation;
- factual preservation;
- linguistic preservation;
- transformation magnitude;
- robustness;
- generalization.

---

# 4. Primary Metrics

Every experiment should identify primary metrics before final result
interpretation where practical.

---

# 5. Secondary Metrics

Secondary metrics may provide additional context.

---

# 6. Composite Metrics

Composite metrics must have an explicit definition.

---

# 7. Metric Weighting

Weights must be justified.

---

# 8. Baselines

Important experiments should use appropriate baselines.

---

# 9. Controls

Experiments should include appropriate positive and negative controls.

---

# 10. Experimental Conditions

Record:

- input;
- language;
- domain;
- model;
- detector;
- transformation;
- parameters;
- version;
- date.

---

# 11. Randomness

Record random seeds where practical.

---

# 12. Replication

Stochastic experiments should use sufficient repetitions where meaningful.

---

# 13. Sample Size

Sample sizes should be justified.

---

# 14. Statistical Power

For confirmatory experiments, consider statistical power where applicable.

---

# 15. Confidence Intervals

Use confidence intervals or other uncertainty estimates where appropriate.

---

# 16. Effect Size

Report practical effect size in addition to statistical significance where
appropriate.

---

# 17. Hypothesis Testing

Where hypothesis tests are used, define:

- null hypothesis;
- alternative hypothesis;
- test;
- threshold;
- interpretation.

---

# 18. Multiple Comparisons

When many hypotheses or metrics are tested, account for multiple comparisons
where appropriate.

---

# 19. P-Values

P-values must not be interpreted as direct probabilities that a hypothesis is
true.

---

# 20. Statistical Assumptions

Statistical tests require assumptions.

Check relevant assumptions before interpreting results.

---

# 21. Non-Parametric Methods

Where assumptions of parametric tests are not justified, consider appropriate
non-parametric methods.

---

# 22. Paired Evaluation

Where input/output pairs are naturally matched, paired analysis may be
preferable to independent analysis.

---

# 23. Stratification

Results should be stratified by relevant variables.

Potential dimensions:

- language;
- domain;
- length;
- model;
- detector;
- transformation.

---

# 24. Aggregation

Aggregate metrics must not hide major subgroup failures.

---

# 25. Macro vs Micro Metrics

Where multiple languages or groups are involved, consider both:

- macro-level aggregation;
- micro-level aggregation.

---

# 26. Worst-Case Performance

Report relevant worst-case subgroup behavior.

---

# 27. Distribution Shift

Evaluate generalization outside the development distribution.

---

# 28. Holdout Data

Holdout data should remain independent from tuning whenever possible.

---

# 29. Test Set Leakage

Potential leakage must be investigated.

---

# 30. Benchmark Reuse

Repeated optimization against a test set reduces its independence.

---

# 31. Cross-Validation

Cross-validation may be used where appropriate but does not automatically
solve all leakage problems.

---

# 32. Bootstrap

Bootstrap methods may be useful for estimating uncertainty where
appropriate.

---

# 33. Correlation

Correlations between metrics should not automatically be interpreted as
causation.

---

# 34. Metric Redundancy

Highly correlated metrics may provide little additional information.

---

# 35. Statistical vs Practical Significance

A statistically significant effect may be practically negligible.

A practically important effect may fail to reach significance with an
insufficient sample.

---

# 36. Missing Data

Missing measurements must be documented.

---

# 37. Failed Runs

Failed experiments must be recorded.

---

# 38. Outliers

Outlier handling must be predefined where possible.

---

# 39. Post-Hoc Exclusion

Data must not be excluded solely because it produces an unfavorable result.

---

# 40. Pre-Registration Principle

Important confirmatory experiments should define hypotheses and primary
analysis before inspecting final results where practical.

---

# 41. Exploratory Analysis

Exploratory analysis is allowed and useful.

It must be labeled as exploratory.

---

# 42. Hypothesis Generation

Exploratory results may generate hypotheses for later confirmatory testing.

---

# 43. Repeated Tuning

Repeated tuning against the same evaluation set creates scientific risk.

---

# 44. Ablation

Ablation studies should be used where necessary to identify causal
contributions of components.

---

# 45. Sensitivity Analysis

Evaluate how conclusions change under reasonable parameter variations.

---

# 46. Robustness Analysis

Evaluate whether conclusions survive relevant changes in:

- language;
- domain;
- length;
- model;
- detector;
- transformation.

---

# 47. Negative Controls

Negative controls help establish whether an observed effect is specific.

---

# 48. Positive Controls

Positive controls establish whether the evaluation methodology can detect an
expected effect.

---

# 49. Blind Evaluation

Where possible, evaluators should be blinded to expected outcomes.

---

# 50. Independent Evaluation

Important results should be independently checked where practical.

---

# 51. Raw Results

Preserve raw evaluation results where feasible.

---

# 52. Derived Results

Derived metrics must be reproducible from raw results.

---

# 53. Analysis Code

Certification-relevant analysis code should be versioned.

---

# 54. Experiment Manifest

Each important experiment should have a manifest describing:

- inputs;
- configuration;
- versions;
- metrics;
- outputs.

---

# 55. Reproducibility

Important experiments should be reproducible from documented artifacts.

---

# 56. Statistical Software

Record statistical software and versions where relevant.

---

# 57. Numerical Precision

Numerical results should preserve sufficient precision for independent
verification.

---

# 58. Rounding

Rounding must not materially alter conclusions.

---

# 59. Confidence Reporting

Confidence information should accompany major quantitative claims.

---

# 60. Uncertainty

Uncertainty must not be hidden behind single-number reporting when it is
scientifically material.

---

# 61. Threshold Analysis

Where a detector uses a threshold, evaluate relevant threshold sensitivity.

---

# 62. ROC Analysis

Where appropriate, evaluate ROC-related metrics.

---

# 63. Precision and Recall

Where classification is involved, consider precision and recall alongside
accuracy.

---

# 64. Class Imbalance

Accuracy may be misleading under class imbalance.

---

# 65. False-Positive Rate

False-positive rate should be explicitly evaluated when relevant.

---

# 66. False-Negative Rate

False-negative rate should also be explicitly evaluated.

---

# 67. Calibration

Probability outputs should be assessed for calibration where appropriate.

---

# 68. Cross-Language Statistics

Statistical aggregation across languages should preserve meaningful
language-level differences.

---

# 69. Multiple Detectors

When evaluating multiple detectors, report detector-specific results.

---

# 70. Ensemble Results

If an ensemble is used, define exactly how results are combined.

---

# 71. Statistical Independence

Do not assume observations are independent when they share:

- authors;
- documents;
- prompts;
- generation sessions;
- models;
- datasets.

---

# 72. Hierarchical Structure

Where data have hierarchical dependencies, consider appropriate statistical
models.

---

# 73. Experimental Unit

Define the correct experimental unit before statistical analysis.

---

# 74. Pseudoreplication

Do not treat repeated measurements from the same underlying unit as fully
independent observations without justification.

---

# 75. Causal Interpretation

Observational correlations should not automatically be interpreted as causal
effects.

---

# 76. Confounding

Identify plausible confounders.

---

# 77. Sensitivity to Confounders

Where practical, test whether conclusions survive reasonable confounding
scenarios.

---

# 78. Research Outputs

This area should produce:

- evaluation protocols;
- statistical protocols;
- metric definitions;
- uncertainty methodology;
- experiment manifests;
- analysis standards.

---

# 79. Final Principle

A result is scientifically useful only when the measurement methodology
supports the conclusion being drawn from it.

---

# 80. Literature Findings (2026-08-24)

Populates §2-§78 above with real evidence of how statistical and
evaluation methodology is actually practiced — and critiqued — in the
AI-text-detection and watermarking literature specifically, rather than
generic statistical principle. Every claim is registered in
`docs/00-project/RESEARCH-REGISTRY.md` under the cited `R-XXXX`
identifier. Confidence markers follow the R04 §39 convention. This is a
first literature pass, not a claim of research completeness.

## 80.1 TPR@Fixed-FPR as the Field's De Facto Standard Metric — Populated

Addresses §4 (Primary Metrics), §63-65 (Precision/Recall, Class
Imbalance, False-Positive Rate): R-0027 (updated) explicitly argues
TPR@1%FPR is the field-relevant metric because headline accuracy/AUROC
can mask near-total failure (TPR as low as 0%) at the low-FPR operating
points that matter for real deployment decisions. R-0086 supplies the
formal justification underneath this practice: a Bayes'-theorem base-rate
argument showing that FPR/accuracy alone is mathematically meaningless
without knowing the (typically unknown, low) real-world prevalence of
AI-generated text — directly grounding this project's own preference for
conservative false-positive behavior (SPECIFICATION-MAP.md §25-26) as a
mathematical necessity, not merely a stylistic choice.

## 80.2 Benchmark Contamination and Construct Validity — Populated

Addresses §29-30 (Test Set Leakage, Benchmark Reuse): R-0087 documents a
concrete, quantified benchmark-artifact contamination failure (DetectRL's
Claude-generated texts carry detectable formulaic markers that detectors
learn as shortcuts — 87.9% of spoofed human text misclassified as a
result). R-0088 documents a distinct construct-validity failure (standard
benchmarks don't represent realistic LLM-revised human text; 60-78 point
detection-rate drop on that condition). R-0089 resolves a previously
unextracted source (KB-009 item 4) and reinforces the same pattern: a
leaderboard-competitive score (F1=0.9734) does not reflect generalizable
detection. **No evidence found** of literal train/test data leakage in
the strict ML sense — the evidence found is about benchmark-construction
artifacts and staleness, a related but distinct failure mode.

## 80.3 Reproducibility Beyond the Already-Known Weber-Wulff/Pangram-DAMAGE Findings — Populated

Addresses §50 (Independent Evaluation): R-0090 is a new (2026),
independent, peer-reviewed multi-tool study (GPTZero, Pangram, Copyleaks,
Turnitin) corroborating the pattern already known from Weber-Wulff et al.
(R-0012) with different tools — vendor-claimed accuracy does not hold up
uniformly under independent testing, and confidence-score calibration
varies enormously and inconsistently by tool. R-0091 adds a large-scale
(15 models × 7 test sets × 3 human datasets) demonstration that published
detector rankings are unreliable across conditions. **No evidence found**
of a formal pooled meta-analysis (PRISMA-style) quantifying a replication
failure rate across the field.

## 80.4 Formal Statistical Guarantees in Watermarking Beyond Three Bricks — Populated

Addresses §12 (in R03, Statistical Significance) and §14-20 (Hypothesis
Testing through Statistical Assumptions): substantial work exists beyond
the already-registered Three Bricks framework (R-0037) —
R-0093 (Annals of Statistics, top-tier peer-reviewed hypothesis-testing
framework with explicit FPR control), R-0094 (anytime-valid e-value
guarantees robust to non-fixed stopping), R-0095 (optimal watermark
generation under explicit Type-I/II constraints), and R-0096 (a formal
impossibility result: "strong" perturbation-robust watermarking is
provably unachievable under natural assumptions — a ceiling on what any
of the above can guarantee).

**Critical tension, preserved not resolved** (per RESEARCH-MAP.md §22):
R-0097 empirically tests three real deployed-lineage watermark schemes
(KGW, Unigram, SynthID) against forensic admissibility standards and
finds the formal guarantees above do not survive real perturbation
conditions in practice — 100% conditional watermark removal after
paraphrasing for KGW/Unigram, pre-attack false-negative rates of 70-83%,
and none of the three schemes meeting more than two of five Daubert
legal-admissibility factors. The theory (formal guarantees exist) and the
practice (deployed schemes fail forensic-grade scrutiny) are both real
findings from this pass and should not be collapsed into a single
narrative.

## 80.5 Detector Confidence Calibration — Populated, Thin

Addresses §67 (Calibration): R-0090 provides the clearest evidence found
— tested confidence-score outputs on known-ground-truth AI text and found
systematic, tool-specific miscalibration (Turnitin ~0%, GPTZero median
<20%, Pangram closest to the true 100% value). R-0097 adds a
watermark-specific calibration-adjacent finding (SynthID's own confidence
signal unreliable 80% of the time even on unambiguous ground truth). **No
evidence found** of a formal Expected-Calibration-Error/reliability-
diagram study specific to this field.

## 80.6 Cross-Study Comparability ("Benchmark Fragmentation") — Populated

Addresses §4 (Primary Metrics) directly: R-0020 (RAID, already
registered) was built explicitly because "very few detectors are
evaluated on shared benchmark datasets." R-0091 empirically demonstrates
the consequence (rankings vary by dataset/metric choice). R-0092 (a
peer-reviewed Computational Linguistics survey) names "lack of robust
evaluation framework" as a top field challenge and documents inconsistent
metric usage across studies. This is directly actionable for the
project's own methodology: R07 should fix a primary-metric convention
(TPR@fixed-FPR, per §80.1) before comparing results across its own future
experiments, rather than inheriting the field's fragmentation.

## 80.7 Items With No Field-Specific Evidence Found

Two sub-topics returned no solid evidence specific to this literature,
and are recorded as open gaps rather than filled with inference:

- **Statistical independence / pseudoreplication** (§71-74): no paper
  was found explicitly naming pseudoreplication (treating multiple
  generations from the same prompt/model session as independent samples)
  as a problem in detection/watermarking evaluation specifically. A
  structurally-adjacent finding exists in a neighboring subfield
  (correlated errors among LLM-as-judge evaluation panels) but is
  off-topic and not counted as evidence here.
- **Effect size / practical-significance reporting** (§16, §35): no
  paper or survey was found critiquing point-estimate-only reporting
  (absent confidence intervals/effect sizes) specifically in AI-detection
  or watermarking papers.

This means §71-74 and §16/§35 of this document currently rest on general
statistical principle rather than domain-specific evidence — worth
tracking as a gap, per the project's own preference for evidence over
assumption (RESEARCH-MAP.md §31).

## 80.8 Items Requiring Follow-Up Before Being Treated as Established

1. R-0087's benchmark-contamination finding is specific to one benchmark
   (DetectRL) and has not been shown to generalize to others.
2. R-0094 and R-0095 are very recent, single-lab preprints, not yet
   independently corroborated or compared against each other or against
   R-0037/R-0093.
3. R-0097's specific percentages are from a single unreplicated preprint
   testing specific tool versions — should not be cited as a permanent
   property of KGW/Unigram/SynthID, since these are actively updated
   systems (R03 §17, Detector Drift, applies equally to watermark
   schemes).
4. The §80.4 theory/practice tension has not been reconciled and
   should not be presented as resolved in any downstream document.