# Statistical Validation Methodology

**Status:** ACTIVE  
**Version:** 0.1  
**Document type:** Validation methodology and experimental protocol (Tranche 1)  
**Authority:** Validation (Primary for statistical methods, controls, and uncertainty estimation)  
**Parent:** `docs/05-validation/VALIDATION-MAP.md` §28–33, §44–47, §66  
**Research basis:** `docs/02-research/R07-evaluation-statistical-methodology.md` (R-0086 through R-0101)  
**Requirements basis:** `docs/03-scientific-specification/S02-scientific-requirements.md` (`REQ-STAT-001` through `REQ-STAT-008`)  
**Architectural basis:** `docs/04-architecture/EVALUATION-ARCHITECTURE.md` (§7–10), `docs/04-architecture/VALIDATION-ARCHITECTURE.md` (§8, §14)  

---

# 1. Purpose & Scope

This document formalizes the experimental design, statistical testing, and uncertainty quantification standards required for all validation and evaluation activities within the project.

It exists to enforce `VALIDATION-MAP.md` §2 ("Fundamental Validation Principle") and `R07` §2 ("Evaluation Philosophy"): **a measurement is valid only relative to a defined objective, methodology, and acceptance criterion; no convenient metric or external observation may be substituted for ground truth.**

This document governs:
1. The primary metric convention for detector and watermark validation (TPR@Fixed-FPR under prevalence constraints);
2. Experimental unit definitions and rules against pseudoreplication;
3. Paired evaluation, control group architecture, and baseline management;
4. Confounder control, including non-native-writer detection bias and length effects;
5. Uncertainty quantification, bootstrap confidence intervals, and calibration;
6. The Minimum Experiment Record schema.

---

# 2. Primary Metric Convention: TPR@Fixed-FPR

## 2.1 Rejection of Unconstrained Accuracy and Headline AUROC

Per `R07` §80.1 (`R-0027`, `R-0086`) and `S02-scientific-requirements.md` `REQ-STAT-001`, **unconstrained classification accuracy and unconstrained AUROC must not be used as primary acceptance criteria for AI-text detection or watermark detection.**

* **The Accuracy Fallacy:** Under real-world class imbalance where the true prevalence of AI-generated or watermarked text $\alpha$ is low (e.g. $\alpha \le 0.05$), a naive classifier labeling all documents as human achieves $>95\%$ accuracy while possessing zero detection capability ($TPR = 0$).
* **The High-FPR AUROC Fallacy:** AUROC integrates over the full false-positive rate spectrum $[0, 1.0]$. A detector with impressive AUROC ($>0.90$) may achieve that score entirely in high false-positive regions ($FPR > 0.10$), while exhibiting near-zero true positive rate at forensic operating points ($FPR \le 0.01$).

## 2.2 Standard Operating Points

All detector and watermark evaluation experiments must report as primary performance metrics:
1. **$TPR@1\%FPR$:** The true positive rate achieved when the decision threshold is fixed such that the empirical false-positive rate on human, unwatermarked controls is exactly $\le 0.010$ ($1.0\%$).
2. **$TPR@0.1\%FPR$ (Forensic Standard):** For capabilities evaluated for forensic or certification-relevant integrity assessment, performance at $FPR \le 0.001$ ($0.1\%$) must also be measured and reported.

## 2.3 Base-Rate / Prevalence Sensitivity Analysis

Per `R07` §80.1 (`R-0086`, Bassett et al., 2026) and `OPEN-QUESTIONS.md` `Q-003`, a measured false-positive rate cannot be interpreted without specifying the target population prevalence.

By Bayes' theorem, the Positive Predictive Value ($PPV$, or real-world precision) of a positive flag is:

$$PPV = \frac{TPR \cdot \alpha}{TPR \cdot \alpha + FPR \cdot (1 - \alpha)}$$

Where:
* $TPR$ is the detector sensitivity at threshold $\tau$;
* $FPR$ is the detector false alarm rate at threshold $\tau$;
* $\alpha \in (0, 1)$ is the population prevalence of machine-generated text.

**Mandatory Requirement:** Every validation report evaluating a detector must tabulate or plot the expected $PPV$ across a standard sensitivity spectrum:
$$\alpha \in \{0.01, 0.05, 0.10, 0.25, 0.50\}$$
No detector may be characterized as "reliable" without explicitly citing the prevalence range under which $PPV \ge 0.90$ holds.

---

# 3. Experimental Unit & Anti-Pseudoreplication Rules

## 3.1 Definition of Experimental Unit

Per `R07` §71–74 (`REQ-STAT-002`):
* An **independent experimental unit** is a document generated from an independent author/source prompt in an independent session.
* Generating multiple completions from the same prompt, or taking multiple paragraph-level excerpts from the same source document, creates **correlated observations**, not independent degrees of freedom.

## 3.2 Anti-Pseudoreplication Constraints

1. **Prompt Clustering:** When a test set contains multiple generations per prompt, statistical tests must employ cluster-robust standard errors or evaluate aggregate document-level metrics rather than treating completions as i.i.d. observations.
2. **Author Correlation:** In human control datasets, multiple documents from the same author must be modeled as a clustered unit or downsampled to prevent single-author stylistic quirks from biasing the false-positive estimate.
3. **Model & Seed Stratification:** Variations across random seeds for stochastic transformations or generative watermarks must be explicitly partitioned into within-seed and between-seed variance components.

---

# 4. Paired Evaluation & Control Group Architecture

## 4.1 Matched-Pair Transformation Testing

Per `VALIDATION-MAP.md` §29 and `S05-transformation-requirements.md` (`TRN-001`):
* Any evaluation measuring the effect of a transformation (paraphrase, perturbation, translation, summarization) must use **matched-pair design**:
  $$\text{Pair}_i = \left( T_{\text{orig}}^{(i)}, T_{\text{trans}}^{(i)} \right)$$
* Both elements of the pair must be evaluated through the identical analysis pipeline under identical configuration parameters.
* The differential impact is measured as:
  $$\Delta M_i = M\left(T_{\text{trans}}^{(i)}\right) - M\left(T_{\text{orig}}^{(i)}\right)$$
  where $M$ is the detector score, watermark z-score, or fidelity metric.

## 4.2 Control Group Standards

Per `VALIDATION-MAP.md` §30:
1. **Positive Controls:**
   * Pure AI-generated text from target generator models with verified ground truth provenance.
   * Watermarked text with verified, intact keys and seeds.
2. **Negative Controls:**
   * Authentic human text authored prior to the public availability of large language models (pre-2022 cutoff) to guarantee zero AI contamination.
   * Unwatermarked text generated from the identical base language model.
3. **Adversarial / Perturbed Controls:**
   * Human text subjected to the identical transformation pipeline to isolate transformation artifacts from watermark/detection decay.

---

# 5. Confounder Control & Stratified Validation

## 5.1 Non-Native Writer Bias Mitigation

Per `RESEARCH-REGISTRY.md` `R-0022` (Liang et al.), `DCQ-007`, and `S02-scientific-requirements.md` `REQ-AID-004`:
* Classifiers relying on perplexity, burstiness, or subword n-gram statistics exhibit severe false-positive inflation on text authored by non-native English writers (up to 61.22% FPR on TOEFL essays).
* **Protocol Requirement:** Any AI-detection capability undergoing validation must be evaluated on at least two distinct human control cohorts:
  * Cohort A: Verified native speakers in standard formal/informal registers.
  * Cohort B: Verified non-native/L2 English speakers (e.g. standard TOEFL/IELTS corpora).
* A detector that passes the $FPR \le 0.01$ threshold on Cohort A but exhibits $FPR > 0.05$ on Cohort B must be flagged as `BIASED_NON_NATIVE` and barred from unconstrained production release.

## 5.2 Text Length Stratification

Per `R04` §39 and `R07` §76:
* Text length (in tokens and characters) is a dominant confounder for both perplexity-based AI detection and statistical watermarking (e.g. Green/Red list z-scores scale with $\sqrt{N}$).
* Validation runs must report performance binned across standard token-length strata:
  * Stratum 1 (Short): $50 - 150$ tokens;
  * Stratum 2 (Medium): $151 - 500$ tokens;
  * Stratum 3 (Long): $501 - 1500$ tokens;
  * Stratum 4 (Extended): $> 1500$ tokens.
* Minimum length floors below which detection is undefined or suppressed must be explicitly validated and enforced.

## 5.3 Multilingual Stratification

Per `SPECIFICATION-MAP.md` §22.1 and `LANGUAGE-ARCHITECTURE.md`:
* Evaluation metrics from English must never be assumed to generalize cross-lingually (`KB-011`, `KB-013`, `KB-014`).
* Validation must be executed and reported independently for each of the 13 supported languages.
* Cross-lingual translation attack suites (e.g. `R-0065`, `R-0066`) must be applied to evaluate evasion vulnerability across language boundaries.

---

# 6. Uncertainty Quantification & Calibration

## 6.1 Bootstrap Confidence Intervals

Per `REQ-STAT-005` and `R07` §80.7:
* All reported point estimates for $TPR@1\%FPR$, $AUROC$, and fidelity retention scores must be accompanied by **95% two-sided non-parametric bootstrap confidence intervals**.
* Resampling must be performed at the level of the independent experimental unit (§3.1) with at least $B = 2,000$ bootstrap replicates.
* For paired evaluations (§4.1), resampling must preserve the matched pair pairing.

## 6.2 Confidence Calibration & Reliability Diagrams

Per `R07` §80.5 (`R-0090`):
* Commercial and open detectors frequently output raw confidence values that are wildly uncalibrated (e.g. clustering at extreme ends despite incorrect predictions).
* All probabilistic detectors must be evaluated for calibration using:
  1. **Expected Calibration Error (ECE):**
     $$\text{ECE} = \sum_{m=1}^{M} \frac{|B_m|}{N} \left| \text{acc}(B_m) - \text{conf}(B_m) \right|$$
     with $M = 10$ equally spaced probability bins.
  2. **Reliability Diagrams:** Visualizing observed empirical accuracy against mean predicted confidence per bin.
* Uncalibrated heuristic scores must be tagged as raw uncalibrated observations (`UNCALIBRATED_OBSERVATION`) in all validation reports, per `REPORTING-ARCHITECTURE.md` §6.

---

# 7. Minimum Experiment Record Schema

Every experiment executed within the validation or evaluation framework must generate a machine-readable record conforming to this schema (satisfying `VALIDATION-MAP.md` §66 and `EVALUATION-ARCHITECTURE.md` §7):

```yaml
experiment_manifest:
  schema_version: "0.1.0"
  experiment_id: "EXP-YYYYMMDD-XXXX"
  timestamp_utc: "2026-10-01T12:00:00Z"
  git_commit_sha: "3d63607..."
  evaluation_profile:
    name: "standard-adversarial-detection"
    version: "1.0.0"
  
  environment:
    hardware_target: "local-workstation"
    os: "darwin-arm64"
    runtime_versions:
      python: "3.11.9"
    random_seed: 42

  dataset_provenance:
    dataset_name: "RAID-sample-eval"
    version: "1.1.0"
    license: "MIT"
    languages: ["en", "de", "it"]
    split: "test"
    unit_count: 1000

  evaluated_capabilities:
    - capability_id: "DET-BINOCULARS-LOCAL"
      version: "0.2.0"
      lifecycle_state: "EXPERIMENTAL"
      parameters:
        quantization: "Q4_K_M"
        threshold: 0.852

  controls:
    positive_control_verified: true
    pre_2022_human_control_verified: true
    non_native_cohort_included: true

  primary_metrics:
    tpr_at_1pct_fpr:
      point_estimate: 0.784
      ci_95_bootstrap: [0.751, 0.812]
      resample_count: 2000
    tpr_at_01pct_fpr:
      point_estimate: 0.512
      ci_95_bootstrap: [0.468, 0.556]
    prevalence_sensitivity:
      ppv_at_alpha_0_05: 0.622
      ppv_at_alpha_0_10: 0.778
      ppv_at_alpha_0_50: 0.987

  confounder_analysis:
    non_native_fpr_ratio: 1.45  # FPR_non_native / FPR_native
    length_stratum_breakdown:
      short_50_150: { tpr_1pct: 0.420, fpr: 0.012 }
      medium_151_500: { tpr_1pct: 0.760, fpr: 0.009 }
      long_501_1500: { tpr_1pct: 0.895, fpr: 0.008 }

  verification_status: "VALIDATED_UNDER_DECLARED_CONDITIONS"
```

---

# 8. Governance & Traceability

1. **No Silent Methodological Drift:** An experiment's primary metrics, thresholds, and statistical tests must be declared before running evaluation passes. Changing primary metrics post-hoc to highlight favorable outcomes is strictly prohibited under `P00-project-governance.md` §9 (`I-001`).
2. **Rejection of Circular Evidence:** No detector under evaluation may use training data derived from the evaluation benchmark itself, nor may an evaluation metric rely on the model being tested (`VALIDATION-MAP.md` §71).
3. **Preservation of Raw Measurements:** Aggregated scores must never replace raw per-document prediction values, which must be archived in the project storage tier (`EVALUATION-ARCHITECTURE.md` §9).
