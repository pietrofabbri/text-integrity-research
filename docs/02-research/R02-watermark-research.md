# R02 — Text Watermarking Research

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Scientific research domain
**Parent:** docs/02-research/RESEARCH-MAP.md
**Methodology:** docs/02-research/R01-literature-research-methodology.md

---

# 1. Purpose

This document defines the research scope for textual watermarking.

The purpose is to identify, classify, reproduce where feasible, and evaluate
scientific watermarking methodologies relevant to generated text.

The document does not assume that any particular watermarking methodology is
currently dominant or universally applicable.

---

# 2. Research Objective

The research program must determine:

- what textual watermarking mechanisms exist;
- how they operate;
- what assumptions they require;
- what statistical or linguistic signals they introduce;
- how they are detected;
- how robust they are to ordinary textual transformations;
- what known limitations exist;
- what emerging approaches could materially change the evaluation framework.

---

# 3. Watermark Taxonomy

The taxonomy must remain extensible.

Potential categories include:

- token-selection watermarking;
- probabilistic watermarking;
- distributional watermarking;
- statistical watermarking;
- semantic watermarking;
- cryptographic watermarking;
- model-integrated watermarking;
- post-generation watermarking;
- metadata-associated watermarking;
- hybrid methodologies;
- future methodologies not yet represented.

---

# 4. Watermark Mechanism

For every relevant methodology determine, where possible:

- insertion mechanism;
- information carrier;
- secret/key requirements;
- generation-time requirements;
- detection-time requirements;
- statistical assumptions;
- linguistic assumptions;
- model assumptions.

---

# 5. Detectability

Research should distinguish:

- watermark existence;
- theoretical detectability;
- practical detectability;
- detector confidence;
- statistical significance;
- false-positive behavior.

---

# 6. Robustness

Investigate robustness under relevant transformations, including:

- truncation;
- insertion;
- deletion;
- lexical substitution;
- syntactic modification;
- paraphrasing;
- translation;
- formatting changes;
- human editing;
- model rewriting.

The exact threat model must come from the source methodology and subsequent
research rather than being assumed.

---

# 7. Attack Models

Relevant literature should be classified by attack model.

Potential categories include:

- no transformation;
- benign transformation;
- automated transformation;
- adversarial transformation;
- adaptive attack;
- detector-aware transformation.

---

# 8. Statistical Foundations

For statistical watermarking, investigate:

- null hypothesis;
- alternative hypothesis;
- test statistic;
- expected distribution;
- assumptions;
- threshold;
- significance level;
- power;
- calibration.

---

# 9. False Positives

False-positive behavior is a first-class research variable.

A watermark detector that identifies ordinary human text as watermarked may
have unacceptable statistical properties even if it detects genuine
watermarks effectively.

---

# 10. False Negatives

False-negative behavior must also be evaluated.

---

# 11. Key and Secret Management

Where a methodology uses a secret key or equivalent mechanism, research:

- key generation;
- key distribution;
- key secrecy;
- detector requirements;
- key compromise;
- reproducibility implications.

---

# 12. Model Dependence

Determine whether the watermark depends on:

- specific model architecture;
- tokenizer;
- vocabulary;
- decoding algorithm;
- model version;
- inference parameters.

---

# 13. Tokenizer Dependence

Tokenizer behavior may materially affect watermarking.

Research must identify tokenizer assumptions explicitly.

---

# 14. Language Dependence

Investigate whether watermark effectiveness changes across languages.

The project must not assume that a watermark demonstrated in English behaves
identically in other languages.

---

# 15. Script Dependence

Investigate effects associated with:

- Latin scripts;
- Cyrillic;
- Japanese scripts;
- Chinese characters;
- mixed-script text;
- right-to-left scripts where relevant to future scope.

---

# 16. Length Dependence

Watermark detectability may depend on document length.

Experiments should therefore evaluate multiple lengths where scientifically
relevant.

---

# 17. Domain Dependence

Investigate effects across relevant domains and genres.

---

# 18. Human Editing

Human editing may alter watermark signals.

Research should investigate this explicitly.

---

# 19. Translation

Translation may alter or destroy watermark signals.

Research should distinguish:

- translation preserving watermark;
- translation weakening watermark;
- translation destroying watermark;
- translation introducing other detectable signals.

---

# 20. Paraphrasing

Paraphrasing methodologies should be treated as distinct experimental
conditions.

---

# 21. Semantic Robustness

Determine whether watermark detection survives transformations that preserve
semantic content.

---

# 22. Linguistic Robustness

Determine whether watermark signals depend on linguistic structures that may
naturally vary during editing.

---

# 23. Detector Assumptions

For each watermark detector identify assumptions about:

- text origin;
- model;
- tokenizer;
- generation process;
- language;
- length;
- decoding.

---

# 24. Detector Availability

Record whether a detector is:

- public;
- reproducible;
- partially reproducible;
- API-only;
- unavailable.

---

# 25. Reproduction

Important watermark methods should be reproduced where legally and technically
feasible.

Reproduction must preserve the original methodology as closely as practical.

---

# 26. Implementation Fidelity

An implementation of a paper must not automatically be considered equivalent
to the original research implementation.

Differences must be recorded.

---

# 27. Watermark Families

Where multiple papers implement variations of the same underlying idea, group
them into methodological families while preserving individual papers.

---

# 28. Scientific Comparison

Watermark methodologies should be compared using:

- detection capability;
- robustness;
- false-positive behavior;
- false-negative behavior;
- language coverage;
- model dependence;
- computational requirements;
- reproducibility;
- known limitations.

---

# 29. No Single Watermark Assumption

The project must not define "the watermark" as one fixed technology.

The research layer must accommodate multiple watermark families.

---

# 30. Future Watermarks

New watermark methodologies must be addable without redesigning the research
architecture.

---

# 31. Watermark Watch

The project should monitor new publications, benchmarks and implementations
that introduce materially different watermark mechanisms.

---

# 32. Impact Assessment

A new watermark methodology should be assessed for impact on:

- threat model;
- experiments;
- validation;
- architecture;
- certification.

---

# 33. Deprecation

Obsolete watermark methodologies may be deprecated.

Historical research must remain traceable.

---

# 34. Research Outputs

This research area should ultimately produce:

- watermark taxonomy;
- methodology summaries;
- evidence matrix;
- robustness matrix;
- detector matrix;
- language coverage matrix;
- open research questions;
- experimental requirements.

---

# 35. Required Traceability

Important findings must connect to:

- assumptions;
- scientific requirements;
- validation experiments;
- certification criteria.

---

# 36. Final Principle

The project must not optimize against a single known watermark.

It must maintain an evolving scientific evaluation framework capable of
incorporating future watermark methodologies.

---

# 37. Literature Findings (2026-08-23)

Populates §3-§36 above with real, currently existing watermark mechanisms
and evidence. Every claim is registered in
`docs/00-project/RESEARCH-REGISTRY.md` under the cited `R-XXXX`
identifier; consult the registry entry for full citation, methodology,
and limitations. Confidence markers (EVIDENCE / AUTHOR-REPORTED / VENDOR /
UNVERIFIED) follow the convention established in R04 §39. This is a first
literature pass (§35 Research Completion Criteria is not yet satisfied).

## 37.1 Watermark Taxonomy — Populated

Real mechanisms now populate §3's category list:

- **Statistical / token-selection (context-dependent key)**: the
  green-list/red-list scheme (R-0001, already registered) re-hashes a
  rolling window of prior tokens at each position.
- **Statistical / token-selection (context-independent key)**: the
  Unigram watermark (R-0032) fixes the same list partition at every
  position instead, trading context-sensitivity for editing/paraphrase
  robustness, with formal correctness guarantees.
- **Distributional / distortion-free**: R-0013 (already registered) —
  designed so the watermark does not change the model's output
  distribution.
- **Semantic**: SIR (R-0033) anchors the signal to a semantic embedding of
  preceding tokens rather than surface-token hashes, specifically to
  survive synonym substitution and paraphrasing — directly answers §21
  (Semantic Robustness) with a named, real mechanism.
- **Cryptographic**: R-0034 (undetectable watermarks, computational
  indistinguishability framing) and R-0035 (publicly-detectable
  watermarks, signature-based, no secret needed for verification) —
  two structurally different cryptographic approaches, differing on
  whether detection requires a private or public key (relevant to §11
  Key and Secret Management and to 06-security).
- **Post-generation (post-hoc)**: PostMark (R-0036) is the one reviewed
  mechanism requiring no generation-time cooperation at all — inserts an
  input-dependent word set into already-generated text via semantic
  similarity. This is the only family compatible with watermarking text
  from a model the project does not control.
- **Production-deployed**: SynthID (R-0014, already registered),
  Anthropic's own text watermarking (R-0042, deployed August 2026, uses
  the SynthID-Text approach) — see §37.3.

Per §29 (No Single Watermark Assumption), these families are recorded as
alternatives, not a ranked list — no family is asserted superior in
general; robustness/quality trade-offs are family- and even
technique-specific (§37.2).

## 37.2 Robustness and Attack Evidence — Populated

Addresses §6-§7 (Robustness, Attack Models) and §9 (False Positives):

- **Paraphrasing is close to a universal removal attack against current
  schemes** (EVIDENCE, R-0039): a systematic evaluation found detection
  rates for all evaluated watermarking schemes fell below 0.3 after a
  single LLM-based paraphrasing pass. This is the strongest single
  robustness finding in this domain and should weigh heavily on any
  claim about watermark-based detection reliability.
- **Spoofing/forgery is an active, structurally-linked attack class**
  (EVIDENCE for existence, AUTHOR-REPORTED for specific figures,
  R-0040, and R-0015 already registered): more-robust watermarks can
  make "piggyback spoofing" (inserting harmful content while preserving
  detectability) easier; using multiple keys defends against stealing but
  may itself become an attack surface; public detection APIs may enable
  oracle-style attacks. Treat all specific percentages in R-0040 as
  UNVERIFIED — the qualitative "these trade-offs are structural" claim is
  better supported than any single number.
- **Detectability-robustness-quality trade-off is real and
  technique-dependent** (AUTHOR-REPORTED, R-0041): reported perplexity
  increases range from 9% to over 2000% depending on technique, with some
  schemes showing measurable downstream task-accuracy loss. Numeric/factual
  content was flagged as especially vulnerable to unintended drift from
  watermark-driven token substitution — directly relevant to
  S04-fidelity-requirements.md FID-008 (Quantitative Preservation) and
  FID-003 (Factual Preservation) if this project ever considers applying
  watermarking rather than only detecting it.
- **Localization in partially-watermarked (mixed) documents** (EVIDENCE,
  R-0038): a two-stage anomaly-then-verification approach exists for
  finding watermarked spans within longer, only-partly-AI-generated
  documents — directly relevant to §35 (Mixed Documents, in R03) and to
  R04 §7 (Hybrid Text).

## 37.3 Real-World Deployment Status — Populated

Addresses §31 (Watermark Watch):

- **Google DeepMind / Gemini**: SynthID (R-0014), open-sourced October
  2024 and integrated into Hugging Face `transformers`.
- **Anthropic**: deployed text watermarking as of August 2026 (R-0042),
  using the SynthID-Text approach, triggered by the EU AI Act
  Transparency Code. This is the most current and most self-relevant
  finding in this research pass, since this project's own tooling runs on
  Claude — Anthropic's disclosed limitations (extensive rewrites remove
  the watermark; numeric/precise content is sparser-watermarked; short
  passages have lower detection confidence) are concrete, primary-sourced
  data points for a real deployed system, not a research paper's claims.
- **OpenAI**: built an internal watermarking system for ChatGPT but chose
  not to deploy it (R-0043), reportedly over user-adoption and fairness
  concerns rather than technical failure — evidence that watermark
  adoption is not just a technical question, and that the project should
  not assume watermarking will become universal across generators (§29,
  §30).
- **Meta**: research-only (open codebase "TextSeal"); no evidence found of
  a shipped watermark for Llama/Meta AI outputs.
- **Mistral AI**: no evidence of deployment or announcement found — recorded
  as "no evidence found," not as a confirmed absence (per
  NO-INVENTION-RULES "Unknown is an acceptable and preferred answer").

**Important scope note**: C2PA (content-provenance metadata, used by
Anthropic for non-text outputs) is a different mechanism from in-generation
token-level text watermarking and must not be conflated with it in this
project's documentation.

## 37.4 Language, Script, and Tokenizer Dependence — Populated, Confirmed Thin

Addresses §14-§15 (Language/Script Dependence):

- **Multilingual watermark robustness does not hold uniformly**
  (EVIDENCE for the negative finding, AUTHOR-REPORTED for the proposed
  fix's numbers, R-0044): evaluated across 133 languages, found existing
  multilingual watermarking methods fail to remain robust under
  translation attacks specifically in medium- and low-resource languages,
  root-caused to tokenizers that under-represent full-word tokens
  (heavy subword fragmentation) for semantic-clustering approaches.
- **Low-resource-language-specific design work exists but is narrow**
  (title/abstract-level only, not deep-verified): a Bangla-specific
  watermark study was found to exist, indicating per-language patchwork
  research rather than a general solved problem.
- **No verified logographic-script-specific (Chinese/Japanese) benchmark
  was found** quantifying detection-rate degradation for those scripts
  specifically, despite a plausible mechanistic link (tokenization
  inconsistency) identified in adjacent work. This is recorded as an
  explicit gap, not filled with an assumption.

This parallels KB-008 (recorded from the R04 pass) — watermarking joins
general AI-text detection as an area where the field's own evidence base
is thin for most of the project's 13 target languages.

## 37.5 Items Requiring Follow-Up Before Being Treated as Established

1. R-0040's specific attack-success percentages (piggyback spoofing >90%,
   removal via 7+ keys 97%+, oracle attack ~3 queries/token) need
   independent replication before being cited as fact.
2. R-0041's perplexity/MMLU figures are technique-specific; do not
   generalize to "watermarking costs X% quality" as a project-wide
   constant.
3. R-0044's proposed-method improvement figures (+0.23 AUC, +37%
   TPR@1%FPR) are single-paper and unverified; the negative finding
   (existing methods aren't robustly multilingual) is better supported
   than the proposed fix's numbers.
4. Several identified-but-not-deep-verified papers (WaterMax,
   "Auditing Cross-Lingual Fairness in Language Model Watermarking,"
   BanglaLorica, the tokenization-inconsistency EMNLP 2025 paper) were
   confirmed to exist and be on-topic but not read in full — a follow-up
   pass should read them directly before citing specific findings from
   them.