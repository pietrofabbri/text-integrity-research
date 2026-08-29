# R04 — AI-Generated Text Detection Research

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Scientific research domain
**Parent:** docs/02-research/RESEARCH-MAP.md
**Methodology:** docs/02-research/R01-literature-research-methodology.md

---

# 1. Purpose

This document defines the scientific research scope for methods attempting
to distinguish human-written, machine-generated and mixed-origin text.

---

# 2. Fundamental Distinction

The project must distinguish:

- human authorship;
- human-like linguistic properties;
- AI-generation likelihood;
- detector classification.

These concepts are related but not identical.

---

# 3. Detection Families

Potential families include:

- classifier-based detection;
- perplexity-based detection;
- likelihood-based detection;
- stylometric detection;
- statistical detection;
- linguistic-feature detection;
- model-based detection;
- ensemble detection;
- metadata-based approaches;
- future approaches.

---

# 4. Human Baseline

Human-written controls must represent the relevant population.

A generic corpus of human text is not necessarily a valid baseline for every
experiment.

---

# 5. AI Baseline

Generated controls must document:

- model;
- version;
- prompt;
- generation parameters;
- date;
- language;
- domain.

---

# 6. Human-Edited AI Text

Human-edited generated text should be evaluated separately.

---

# 7. Hybrid Text

Mixed-origin documents should be considered where relevant.

---

# 8. Translation

Translated text should be treated as a separate condition.

---

# 9. Paraphrasing

Paraphrased generated text should be treated as a separate condition.

---

# 10. Detector Generalization

Evaluate whether detector performance transfers across:

- models;
- languages;
- domains;
- authors;
- lengths;
- prompts;
- generation settings.

---

# 11. False Positives

False-positive rates on human text are a primary metric.

---

# 12. False Negatives

False-negative behavior on generated text must also be measured.

---

# 13. Calibration

Where a detector produces scores or probabilities, calibration should be
investigated.

---

# 14. Threshold Dependence

Record detector thresholds and decision rules.

---

# 15. Detector Drift

AI detectors may evolve over time.

Record detector version and test date.

---

# 16. Model Drift

Generation models evolve.

Research must therefore distinguish model generations.

---

# 17. Language Coverage

Evaluate languages separately.

English results must not be generalized automatically to other languages.

---

# 18. Language-Specific Bias

Investigate whether linguistic properties create systematic false positives
or false negatives.

---

# 19. Domain Shift

Evaluate domains separately where relevant.

---

# 20. Document Length

Detection performance may vary strongly with text length.

Evaluate multiple length ranges.

---

# 21. Writing Style

Investigate variation caused by:

- formal writing;
- informal writing;
- academic writing;
- technical writing;
- journalism;
- creative writing;
- non-native writing.

---

# 22. Author Variation

Human writing varies substantially between authors.

A detector must not equate unusual human writing with machine generation.

---

# 23. Non-Native Writing

Where relevant, evaluate whether non-native language use affects false-positive
rates.

---

# 24. Editing Effects

Evaluate detector behavior after controlled editing.

---

# 25. Distribution Shift

Investigate changes caused by:

- new models;
- new domains;
- new languages;
- new generation strategies;
- new human editing patterns.

---

# 26. Adversarial Evaluation

Where scientifically appropriate, controlled transformations may be used to
investigate detector robustness.

---

# 27. Detector-Specific Effects

A transformation that changes one detector's result does not establish a
general property of AI-generated text.

---

# 28. Cross-Detector Evaluation

Use multiple methodologies where possible.

---

# 29. Independent Detectors

Prioritize methodological diversity over simple detector count.

---

# 30. Human Evaluation

Where detector outputs conflict with human judgments, investigate the source
of disagreement rather than assuming either side is automatically correct.

---

# 31. Ground Truth

Ground truth must be defined explicitly.

Potential labels include:

- human;
- generated;
- human-edited generated;
- translated generated;
- mixed;
- unknown.

---

# 32. Label Uncertainty

Some real-world documents cannot be assigned reliable ground truth.

These should not be silently forced into binary categories.

---

# 33. Benchmark Quality

AI-detection benchmarks must be evaluated for:

- source quality;
- generation diversity;
- human diversity;
- language coverage;
- domain coverage;
- contamination;
- temporal validity.

---

# 34. Benchmark Contamination

Repeated detector development against the same benchmark may reduce its
validity.

---

# 35. Temporal Robustness

A detector trained or evaluated at one point in time may behave differently
against newer models.

---

# 36. Research Outputs

This research area should produce:

- detector taxonomy;
- evidence matrix;
- language matrix;
- benchmark assessment;
- robustness findings;
- false-positive analysis;
- detector portfolio;
- open questions.

---

# 37. New Detection Methodologies

New detector families must be incorporable without redesigning the research
architecture.

---

# 38. Final Principle

AI-detection research must measure detector behavior, not assume that a
detector's classification is equivalent to ground truth about authorship.

---

# 39. Literature Findings (2026-08-23)

The sections above (§1-38) define the research *methodology* for this
domain. This section records actual literature findings gathered against
that methodology. Every claim below is registered in
`docs/00-project/RESEARCH-REGISTRY.md` under the cited `R-XXXX` identifier;
consult the registry entry for full citation, methodology, and limitations
before relying on any claim here. Per `docs/99-backlog/NO-INVENTION-RULES.md`,
claims are marked EVIDENCE (independently corroborated or primary-source
confirmed), AUTHOR-REPORTED (from the source's own abstract/claims, not
independently replicated), VENDOR (commercial source, treat cautiously),
or UNVERIFIED (a specific number found only in a secondary source and not
confirmed against the primary source).

This is a first literature pass, not a claim of research completeness per
§35 (Research Completion Criteria). It has not yet been reviewed for
consistency against 03-scientific-specification through 10-certification —
that propagation step (RESEARCH-MAP.md §20-21) is separate follow-up work.

## 39.1 Detector Taxonomy — Populated

Confirms and populates the families listed in §3 with real, currently
existing methods:

- **Statistical / zero-shot** (no training on labeled AI/human text):
  GLTR (R-0002), DetectGPT (R-0003), Fast-DetectGPT (R-0004), Binoculars
  (R-0005). These require access to one or more reference language models
  at detection time but not to labeled training data, and are the
  detector family most naturally compatible with the project's offline-core
  requirement (DEC-001).
- **Trained classifiers**: the OpenAI RoBERTa GPT-2 detector (R-0006, now
  obsolete for modern LLMs — EVIDENCE), OpenAI's 2023 general classifier
  (R-0007, publicly withdrawn for low accuracy — EVIDENCE), RADAR (R-0008,
  adversarially trained for paraphrase robustness — EVIDENCE).
- **Commercial/product detectors**: GPTZero (R-0009), Pangram (R-0010),
  and — found to exist but not methodologically verified in this pass —
  Originality.ai, Copyleaks, Turnitin, Winston AI. All commercial-detector
  accuracy and robustness claims in this domain are VENDOR unless
  independently corroborated (see §39.3 for the independent studies that
  do corroborate or contradict specific vendor claims).
- **Watermark-based detection** (distinct family — requires the
  *generating* model's cooperation, unlike the three families above): the
  project's existing R-0001 (Kirchenbauer green/red-list), plus newly
  registered R-0013 (distortion-free watermarking) and R-0014 (SynthID,
  production-deployed in Gemini). Watermarking is not a substitute for
  post-hoc detection — it says nothing about text from non-cooperating
  models, and R-0015 documents that a deployed watermark's rules can be
  approximated from API queries alone and then scrubbed or spoofed.

## 39.2 Benchmark Datasets — Populated

Real, named, citable benchmarks now exist in the registry for future
validation-profile design (§33 Benchmark Quality, §34 Benchmark
Contamination): HC3 (R-0016), TuringBench (R-0017, temporally dated),
MGTBench (R-0018), M4 (R-0019, multilingual by design), RAID (R-0020,
purpose-built for robustness stress-testing), and BLUFF (R-0021,
low-resource-language-focused, 2026, INCONCLUSIVE pending primary-source
verification of its specific figures).

RAID (R-0020) is the strongest existing candidate to adopt for the
project's own robustness evaluation profile (§33) rather than building an
equivalent benchmark from scratch, per RESEARCH-MAP.md's general
preference against unnecessary duplication.

## 39.3 Robustness and False-Positive Findings — Populated

Addresses §11 (False Positives), §21/§23 (Writing Style / Non-Native
Writing), §26 (Adversarial Evaluation), §35 (Temporal Robustness):

- **Non-native-speaker bias** (EVIDENCE, R-0022): detectors consistently
  misclassify non-native-English TOEFL essays as AI-generated while
  correctly classifying native-speaker essays. A frequently repeated
  "61.3% false-positive rate" figure is UNVERIFIED — found only in a
  secondary source, not confirmed against the primary paper's own tables.
- **Race/ELL-status bias** (EVIDENCE, R-0023): a more recent, more
  granular study found non-White English-language-learner essays were
  disproportionately flagged relative to White ELL essays in 7 of 16
  tested detectors (vs. 1 of 16 for the reverse), while purely
  economically-disadvantaged status showed no such effect. Bias and raw
  accuracy were correlated but distinct.
- **Paraphrasing attacks** (EVIDENCE, R-0024): the best-documented single
  robustness failure found — DIPPER paraphrasing drops DetectGPT's
  detection accuracy from 70.3% to 4.6% at a fixed 1% false-positive
  rate. This number is confirmed directly from the primary paper, not
  secondary-sourced.
- **Translation as a false-positive source** (VENDOR, R-0031, narrow
  scope): a single-vendor study found round-trip machine translation
  raised false-positive rates on genuinely human text from ~0.4% to
  ~28%, while direct one-way translation caused a much smaller rise.
  Independently, R-0012 (non-vendor) also found machine-translated human
  text triggered false positives across multiple tools, without
  vendor-study-level precision on magnitude.
- **Mixed human/AI document boundaries** (VENDOR, R-0030): Turnitin
  self-discloses a sentence-level false-positive rate of ~4% (vs. <1% at
  document level), concentrated at boundaries between human- and
  AI-written sentences — relevant to §7 (Hybrid Text).
- **Whether reliable detection is even theoretically possible is
  contested, not settled** (R-0025 vs. R-0026): one theoretical analysis
  argues detection accuracy is fundamentally bounded by how distinguishable
  AI and human text distributions are and will degrade as they converge;
  a counter-position argues reliable detection remains possible with
  enough independent samples. Per DOCUMENT-AUTHORITY-MATRIX.md, this
  project does not pick a side — both positions are registered.
- **Mechanistic evidence for detector drift** (EVIDENCE, R-0028):
  detectors have been shown to respond to statistical fingerprints of a
  model's post-training procedure (e.g., instruction-tuning) rather than
  an invariant "AI-ness" property — the same underlying base model scores
  as "human" before instruction-tuning and "AI" after. This gives a causal
  mechanism for why detector effectiveness should be expected to drift as
  training recipes evolve, directly supporting KB-001.
- **Headline accuracy metrics can be misleading** (EVIDENCE, R-0027): an
  independent cross-detector study found true-positive rate at a fixed
  1% false-positive rate can collapse to 0% for some detector/model/task
  combinations even when the same detector reports high AUROC — a
  concrete argument against accepting any single aggregate metric (already
  the project's position per SPECIFICATION-MAP.md §25).

## 39.4 Multilingual Coverage — Populated, and Confirmed Thin

Directly relevant to KB-006/KB-007 and OPEN-QUESTIONS.md Q-004: the
evidence base for multilingual AI-text detection is thin. Beyond M4
(R-0019) and BLUFF (R-0021, figures unverified), the only
language-specific academic study found was a small Urdu case study
(R-0029, not one of the project's 13 target languages). No independently
verified, non-vendor study was found for German, Italian, Portuguese,
Russian, Japanese, Polish, Dutch, Turkish, or Indonesian — all of which
are project target languages (SPECIFICATION-MAP.md §20). Commercial
vendors claim broad language coverage (e.g., "18+ languages") without
publishing per-language accuracy studies that could be independently
checked in this pass.

**This should be read as a finding in itself**: multilingual detector
robustness is not merely undocumented in this project's own files — it
appears to be genuinely under-researched in the wider field, for at least
9 of the project's 13 target languages. This raises the bar of what
"validated" can mean for non-English language capability states (§22)
in the near term.

## 39.5 Items Requiring Follow-Up Before Being Treated as Established

Recorded per NO-INVENTION-RULES "Missing Information" — these are known
gaps, not filled with plausible assumptions:

1. BLUFF (R-0021) exact language counts and cross-lingual F1 figures need
   direct verification against the paper's own tables/body text.
2. The R-0022 "61.3% false-positive rate" figure needs direct verification
   against the Liang et al. paper's own tables.
3. A repeated claim that a humanizer tool dropped one vendor's detector
   accuracy from 91.3% to 27.8% was traced only to a secondary aggregator
   (Wikipedia) and could not be traced to a primary study in this pass —
   do not cite this figure until traced to a primary source.
4. A claim that Black students are markedly more likely to have work
   falsely flagged (repeated across education-press secondary sources,
   attributed to a Common Sense Media report) could not be traced to and
   read from that primary report in this pass.
5. arXiv:2603.23146 ("Why AI-Generated Text Detection Fails...") was
   confirmed to exist and be on-topic but its content could not be
   extracted — not yet registered in RESEARCH-REGISTRY.md pending content
   verification.
6. Arabic-language detector research (a ScienceDirect paper) was confirmed
   to exist by title only — not yet registered pending content review.

---

# 40. Final Principle (Restated)

Populating this domain with real literature does not change §38: AI-
detection research still measures detector behavior, not ground truth
about authorship. If anything, §39.3's findings (drift, bias, paraphrase
fragility, contested theoretical limits) reinforce §38 rather than
qualify it.