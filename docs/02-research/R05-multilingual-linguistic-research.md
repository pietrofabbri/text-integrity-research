# R05 — Multilingual and Linguistic Research

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Scientific research domain
**Parent:** docs/02-research/RESEARCH-MAP.md
**Methodology:** docs/02-research/R01-literature-research-methodology.md

---

# 1. Purpose

This document defines research requirements concerning multilingual text,
linguistic variation and language-specific behavior.

---

# 2. Initial Language Scope

The initial research portfolio includes:

- English;
- Spanish;
- German;
- Japanese;
- French;
- Portuguese;
- Russian;
- Italian;
- Dutch;
- Polish;
- Turkish;
- Chinese;
- Indonesian.

---

# 3. No Uniformity Assumption

The project must not assume that one linguistic methodology behaves equally
across all languages.

---

# 4. Language Profiles

Each language should eventually have a profile covering relevant:

- writing system;
- morphology;
- syntax;
- tokenization;
- segmentation;
- punctuation;
- orthography;
- inflection;
- compounding;
- register;
- discourse conventions.

---

# 5. Script

Record script characteristics.

Potential categories include:

- Latin;
- Cyrillic;
- Chinese characters;
- Japanese mixed scripts;
- other scripts relevant to future scope.

---

# 6. Tokenization

Tokenization may materially affect:

- watermarking;
- detection;
- similarity metrics;
- transformations;
- semantic evaluation.

---

# 7. Segmentation

Languages differ in word and sentence segmentation.

Evaluation methodologies must account for this.

---

# 8. Morphology

Morphologically rich languages may behave differently under lexical
transformation.

---

# 9. Syntax

Syntactic flexibility may influence transformation and detection behavior.

---

# 10. Word Order

Different degrees of word-order flexibility should be considered.

---

# 11. Compounding

Compounding may affect tokenization and lexical transformation.

---

# 12. Inflection

Inflectional changes may affect both minimality and semantic preservation.

---

# 13. Punctuation

Punctuation conventions differ across languages and genres.

---

# 14. Orthography

Orthographic variation must not automatically be interpreted as semantic or
authorship variation.

---

# 15. Register

Evaluate relevant differences between:

- formal;
- informal;
- technical;
- academic;
- journalistic;
- conversational;
- creative.

---

# 16. Native vs Non-Native Writing

Where relevant, distinguish native and non-native writing.

---

# 17. Human Baselines

Human baseline corpora should be linguistically appropriate.

---

# 18. AI Baselines

AI-generated baselines must use documented language conditions.

---

# 19. Translation

Translated text should be studied as a distinct condition.

---

# 20. Cross-Language Transfer

Investigate whether methods trained or designed for one language transfer
to another.

---

# 21. Multilingual Models

Research should consider multilingual model effects.

---

# 22. Language Imbalance

Unequal training or benchmark representation can create systematic
performance differences.

---

# 23. Data Availability

Some languages have less available high-quality research data.

This must be treated as a limitation rather than hidden.

---

# 24. Language-Specific Components

The project may introduce language-specific processing when evidence
indicates that a shared approach is insufficient.

---

# 25. Shared Core

A shared multilingual core should be preferred where it satisfies the
scientific requirements without unacceptable degradation.

---

# 26. Language Exclusion

A language may be excluded from a particular shared methodology if justified
by evidence.

The exclusion must be documented.

---

# 27. Language Certification

Certification must be evaluated per language or clearly defined language
group.

---

# 28. Cross-Language Metrics

Metrics must be interpreted carefully across languages.

A metric with identical numerical values may not represent identical linguistic
properties.

---

# 29. Human Evaluation

Human evaluators should understand the language being evaluated.

---

# 30. Machine Translation in Evaluation

Machine translation may be useful for discovery or auxiliary analysis but
should not automatically replace native-language evaluation.

---

# 31. Semantic Evaluation

Semantic equivalence must be evaluated within the relevant language.

---

# 32. Cultural and Pragmatic Effects

Where relevant, research should consider:

- idioms;
- pragmatics;
- politeness;
- discourse conventions;
- culturally specific expressions.

---

# 33. Terminology

Technical terminology must be preserved appropriately.

---

# 34. Named Entities

Named entities require special consideration because seemingly minor
transformations can alter factual identity.

---

# 35. Numbers and Units

Numbers, dates, measurements and units require explicit preservation
criteria.

---

# 36. Unicode

The system must support correct Unicode handling.

---

# 37. Encoding

Encoding transformations must not silently alter text.

---

# 38. Normalization

Unicode normalization should be documented because it can change underlying
representation without obvious visual changes.

---

# 39. Directionality

Where future languages require it, bidirectional text must be considered.

---

# 40. Mixed-Language Text

Documents containing multiple languages should be treated as a separate
condition.

---

# 41. Code-Switching

Code-switching should be considered where relevant.

---

# 42. Language Detection

If language identification is used, its errors must be considered in the
overall evaluation.

---

# 43. Language Identification Errors

Misclassification of language can cascade into incorrect processing.

---

# 44. Research Outputs

This area should produce:

- language profiles;
- language-specific risks;
- multilingual benchmark requirements;
- cross-language comparison methodology;
- language-specific validation requirements.

---

# 45. Future Languages

New languages should be addable without redesigning the architecture.

---

# 46. Final Principle

Multilingual support is not demonstrated by accepting multiple input
languages.

It is demonstrated by scientifically evaluating behavior in each relevant
language.

---

# 47. Literature Findings (2026-08-24)

Populates §2-§45 above with real cross-lingual evidence for AI-text
detection, watermarking, and watermark evasion across the project's 13
target languages. Every claim is registered in
`docs/00-project/RESEARCH-REGISTRY.md` under the cited `R-XXXX`
identifier. Confidence markers (EVIDENCE / AUTHOR-REPORTED / VENDOR /
UNVERIFIED) follow the convention established in R04 §39. This is a first
literature pass, not a claim of research completeness.

## 47.1 Correction to the Prior Multilingual-Evidence-Gap Finding (KB-008)

The R04 pass (2026-08-23) concluded that 9 of the project's 13 target
languages (German, Italian, Portuguese, Russian, Japanese, Polish, Dutch,
Turkish, Indonesian) had no independently verified, non-vendor AI-detection
or watermarking study, and recorded this as KB-008. **This R05 pass finds
that conclusion no longer holds as originally stated for AI-text
detection specifically.** Dedicated or benchmark-level detection evidence
was found touching all 13 target languages:

- **German, Dutch, Portuguese, Russian**: MULTITuDE (R-0049, EMNLP
  peer-reviewed, 11 languages).
- **German, Italian, Russian**: SemEval-2024 Task 8 / M4GT-Bench (R-0047,
  R-0048; 62-team shared task).
- **Indonesian**: M4 (R-0046), SemEval-2024 Task 8 (R-0048).
- **Polish**: PolEval 2025 (R-0052, first dedicated Polish shared task).
- **Japanese**: Zaitsu & Jin (R-0057, peer-reviewed PLOS ONE, 100% LOO
  accuracy).
- **Portuguese**: PT-Detect (R-0058, dedicated study beyond
  benchmark-inclusion).
- **Turkish**: Ozdemir (R-0060, first dedicated Turkish study).
- **Italian**: Puccetti et al. (R-0059) — note this is a *negative*
  finding (no practical in-the-wild detection method currently exists for
  Italian against an unknown closed-API model), which is evidence of a
  different kind than "detection works," but is still direct, dedicated,
  peer-quality evidence *about* Italian, not an absence of evidence.

**What still holds**: evidence *depth* and *independence* vary enormously.
Most of the above is single-study or benchmark-inclusion-level, not the
multi-year, multi-lab convergence that exists for English. **Watermarking**
evidence (as opposed to detection) remains much thinner than detection
evidence for nearly every non-English language — no dedicated
per-language watermarking study was found for German, Italian, Portuguese,
Russian, Japanese, Polish, Dutch, or Turkish; watermarking-robustness
papers that include these languages (R-0063, R-0064, R-0066, R-0067,
R-0069) each test only 3-6 languages, never the full 13, with no
consistent coverage across papers. Dutch has no dedicated standalone
detection study either (only benchmark-inclusion via R-0049/R-0050).

KB-008 has been updated (not deleted) to record this correction — see
project knowledge backlog. The practical consequence for
SPECIFICATION-MAP.md §20-22 is narrower than KB-008 originally proposed:
rather than defaulting most of the 13 languages to RESEARCH_ONLY/
NOT_SUPPORTED uniformly, capability states should now be assessed
per-language against the specific evidence found here — some languages
(Japanese detection, Polish detection) have real if narrow dedicated
evidence; watermarking capability states should stay conservative for
nearly all non-English languages regardless.

## 47.2 Tokenizer and Script Effects on Watermark Robustness — Populated

Addresses §6 (Tokenization) and R02 §14-15 (Language/Script Dependence):

- Three independent groups now converge on the same outcome, though not
  yet on independent replication of the same causal mechanism: **STEAM**
  (R-0044/R-0062, tokenizer subword-fragmentation mechanism claim,
  AUTHOR-REPORTED, unreplicated), **MULTITuDE** (R-0049, EVIDENCE-tier
  script/resource clustering effect — Cyrillic languages transfer well to
  each other, Arabic/Chinese comparatively harder), and the **SynthID
  robustness study** (R-0069, EVIDENCE-tier per-language F1 numbers:
  Chinese 0.711 worst, Japanese 0.819 best under round-trip translation).
- **Open tension, preserved rather than resolved** (per RESEARCH-MAP.md
  §22, Contradictory Evidence): Japanese is the *best*-surviving language
  in the SynthID study (R-0069) but is treated as one of the linguistically
  *hardest* languages in LUNA/STELA's typological watermark-design
  analysis (R-0063, R-0064). Both can be true simultaneously (translation
  *quality* vs. watermark *design difficulty* are different variables),
  but the project should not silently pick one framing.
- Turkish agglutinative tokenization fragmentation is independently
  documented at the tokenization-mechanics level (R-0071, background
  paper, does not itself test watermarking/detection) — consistent with,
  but not itself confirming, the STEAM mechanism claim for Turkish
  specifically.

## 47.3 Translation-Based Watermark and Detector Evasion — New Attack Class, Populated

Not previously captured in the R02/R03 research pass (2026-08-23), which
documented monolingual paraphrasing (R-0039) as the dominant evasion
method. This pass found **translation-based evasion is a distinct and
well-evidenced attack class**, materially relevant to R02 §6-7
(Robustness/Attack Models) and R03 §25 (Editing Evaluation):

- **CWRA / X-SIR** (R-0065): cross-lingual translation attack drops
  watermark AUC from 0.95 to 0.67 against KGW/Unigram-style watermarks.
- **Uncovering the Hidden Threat** (R-0066): tests both "symmetric"
  (round-trip) and "asymmetric" (translate-and-edit, more realistic)
  attacks across 4 watermark schemes and EN/AR/ZH/ID; AUC falls as low as
  0.55-0.57; directionality finding — translations *into* English survive
  better than translations *out of* English.
- **CLSA** (R-0067, single-author unreplicated preprint, INCONCLUSIVE):
  claims near-chance AUROC collapse when translation is combined with
  abstractive summarization — the most dramatic numbers found, but
  explicitly flagged as unreplicated and not peer-reviewed; do not treat
  as more reliable than the peer-reviewed R-0039 paraphrasing finding.
- **ESPERANTO** (R-0068, peer-reviewed ACM HT 2025): extends the
  translation-evasion finding from watermarking to plain AI-text
  detection — multi-pivot round-trip translation significantly reduces
  true-positive rate across 9 detectors.
- **SynthID round-trip translation** (R-0069): F1 0.711 (Chinese) to
  0.819 (Japanese) under round-trip translation — directly relevant since
  SynthID is the mechanism behind Anthropic's own deployed watermarking
  (R-0042, R02 §37.3).

**Recommendation carried to DOCUMENTATION-CHANGE-QUEUE.md**: R02 §37.2
(Robustness and Attack Evidence) should eventually be amended to name
translation-based evasion as a distinct attack category alongside
paraphrasing, once 03-scientific-specification or 06-security moves past
definition phase — recorded as part of DCQ-006 rather than executed here,
consistent with how DCQ-006 already defers cross-area propagation.

## 47.4 Non-Native-Writer Bias — Confirmed for English Only

Addresses §16 (Native vs Non-Native Writing):

- R-0022 (Liang et al.) was fetched directly (not via secondary summary)
  during this pass, upgrading it to EVIDENCE tier and correcting a
  previously-circulated "61.3%" figure to the confirmed **61.22%**
  false-positive rate on TOEFL essays; see updated R-0022 registry entry
  and KB-009.
- **No evidence found** extending this finding to any other language
  pair — searched specifically for non-native German/French/Spanish/
  Chinese writers being flagged by detectors calibrated for those
  languages, and found none. Secondary/marketing sources sometimes
  extrapolate the English-only finding to "AI detection is biased against
  non-native writers" generally — this extrapolation is UNVERIFIED and
  should not be treated as established.

## 47.5 Code-Switching and Mixed-Language Text — Confirmed Gap

Addresses §40-41 (Mixed-Language Text, Code-Switching):

- A comprehensive May-2026 survey of code-mixing in the LLM era (R-0072)
  explicitly does not cover AI-detection or watermarking for
  code-switched text at all — read as corroborating evidence of a
  genuine field-wide gap, not merely a search failure on this project's
  part.
- One on-topic lead (R-0073, a DTIC-indexed technical report) could not
  be retrieved (403 error, 2 attempts) — its existence is confirmed, its
  content is not; flagged for manual follow-up rather than cited.
- **No evidence found** for any watermarking study specifically targeting
  code-switched/mixed-language text.

## 47.6 Chinese and Japanese (Logographic/CJK Scripts) — No Longer an Evidence Vacuum

The R04 pass (§39.4) found no quantified logographic-script benchmark.
This no longer holds: Zaitsu & Jin (R-0057, Japanese, peer-reviewed,
EVIDENCE-tier), C-ReD (R-0054, Chinese, dedicated benchmark,
AUTHOR-REPORTED), and the SynthID/LUNA/STELA/CLSA/Hidden-Threat papers
(R-0069, R-0063, R-0064, R-0067, R-0066) all now include Chinese and/or
Japanese as quantified test languages for detection or watermarking
robustness. This is a meaningful improvement over "no evidence," while
still well short of English-language-scale, multi-lab convergence.

## 47.7 Cultural and Pragmatic Effects — Confirmed Absence of Evidence

Addresses §32 (Cultural and Pragmatic Effects): no study was found
connecting idiom density, register, or discourse convention to detection
or watermarking performance in any language. C-ReD (R-0054) makes an
unquantified qualitative claim about Chinese idiom density complicating
detection, but isolates no experimental variable for it. This remains an
explicit, honestly-recorded gap rather than an assumption.

## 47.8 Items Requiring Follow-Up Before Being Treated as Established

1. Per-language numeric tables for SemEval-2024 Task 8 (R-0048), CEAID
   (R-0051), and RuATD 2022 (R-0053) could not be extracted in this pass
   — only aggregate/qualitative findings are confirmed. A follow-up pass
   should fetch and read the full tables directly.
2. R-0067 (CLSA)'s dramatic AUROC-collapse figures are single-author,
   non-peer-reviewed, and unreplicated — must not be cited as
   representative of watermark robustness generally until independently
   verified.
3. R-0073 (the DTIC code-switching report) remains an unretrieved lead —
   requires manual follow-up outside standard web-fetch tooling.
4. The STEAM/R-0044/R-0062 tokenizer-fragmentation causal mechanism has
   not been independently replicated by a second research group using
   the same causal claim — the outcome (weaker robustness for
   low-resource/non-Latin languages) is corroborated across sources, but
   the specific mechanism is not.
5. R-0061 (Indonesian, ShodhKosh) is a low-tier-venue source and should
   not be cited for any specific numeric claim.
6. The Japanese "best vs. hardest" tension (§47.2) has not been resolved
   and should not be silently picked one way in any downstream document.