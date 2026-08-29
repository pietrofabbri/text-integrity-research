# R06 — Transformation and Preservation Research

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Scientific research domain
**Parent:** docs/02-research/RESEARCH-MAP.md
**Methodology:** docs/02-research/R01-literature-research-methodology.md

---

# 1. Purpose

This document defines research concerning textual transformation and the
preservation of properties that should remain unchanged.

---

# 2. Core Problem

A textual transformation may modify surface form while preserving some
properties and damaging others.

The project therefore treats preservation as multidimensional.

---

# 3. Preservation Dimensions

At minimum consider:

- semantic;
- factual;
- structural;
- linguistic;
- stylistic;
- terminological;
- numerical;
- entity-level;
- formatting.

---

# 4. Minimality

Minimality is a measurable research problem.

It must not be defined merely as:

"the output looks similar."

---

# 5. Transformation Magnitude

Potential measures include:

- character-level changes;
- token-level changes;
- word-level changes;
- sentence-level changes;
- structural changes.

---

# 6. Semantic Preservation

Evaluate whether the output preserves the meaning of the input.

---

# 7. Factual Preservation

Evaluate whether factual assertions remain unchanged.

---

# 8. Numerical Preservation

Numbers must receive explicit treatment.

---

# 9. Entity Preservation

Names, organizations, places, products and other entities should be
preserved where required.

---

# 10. Terminology Preservation

Technical terminology should not be unnecessarily altered.

---

# 11. Structural Preservation

Investigate preservation of:

- paragraphs;
- headings;
- lists;
- quotations;
- tables;
- ordering;
- document structure.

---

# 12. Formatting Preservation

Where formatting is part of the input representation, define whether it must
be preserved.

---

# 13. Linguistic Preservation

Evaluate:

- grammar;
- syntax;
- morphology;
- lexical characteristics;
- punctuation.

---

# 14. Stylistic Preservation

Where relevant, investigate:

- register;
- tone;
- sentence rhythm;
- vocabulary;
- discourse style.

---

# 15. Human-Likeness vs Style

Do not equate human-like detector behavior with preservation of the original
author's style.

These are separate properties.

---

# 16. Transformation Families

Potential transformation families include:

- lexical;
- syntactic;
- punctuation;
- formatting;
- sentence-level;
- paragraph-level;
- structural;
- multilingual;
- controlled combinations.

---

# 17. Controlled Transformations

Controlled transformations are useful for causal experiments.

Each transformation should be explicitly defined.

---

# 18. Transformation Intensity

Experiments should distinguish transformation intensity.

---

# 19. Transformation Budget

Where appropriate define a maximum acceptable transformation budget.

---

# 20. Pareto Analysis

Analyze trade-offs between:

- transformation magnitude;
- semantic preservation;
- linguistic preservation;
- structural preservation;
- detector response;
- watermark response.

---

# 21. Failure Modes

Potential failures include:

- meaning alteration;
- factual alteration;
- omission;
- addition;
- hallucination;
- entity substitution;
- number modification;
- register drift;
- grammatical degradation;
- structural damage.

---

# 22. Automated Evaluation

Automated metrics may be used but must be interpreted within their known
limitations.

---

# 23. Human Evaluation

Human evaluation may be necessary for semantic or stylistic properties that
automated metrics cannot adequately capture.

---

# 24. Human Evaluation Blinding

Where possible, evaluators should not know which condition produced a text.

---

# 25. Pairwise Evaluation

Input/output pairwise evaluation may be useful.

---

# 26. Absolute Evaluation

Absolute quality ratings may complement pairwise comparison.

---

# 27. Metric Diversity

No single similarity metric should define preservation universally.

---

# 28. Metric Failure

Metrics can fail in language-specific or domain-specific conditions.

---

# 29. Language Effects

Transformation behavior must be evaluated separately by language.

---

# 30. Translation Effects

Translation is not automatically equivalent to ordinary textual transformation.

---

# 31. Human Editing

Human editing should be treated as a separate experimental condition.

---

# 32. Repeated Transformation

Repeated transformations may accumulate changes.

This should be evaluated where relevant.

---

# 33. Transformation Composition

Combining transformations can create interactions not predicted by individual
transformations.

---

# 34. Minimal Necessary Change

The scientific objective is to investigate the smallest transformation
consistent with the experimental requirement.

---

# 35. No Unnecessary Generation

Where a transformation can be achieved without generating additional text,
generation should not be assumed necessary.

---

# 36. Content Addition

Unnecessary addition of new content is a fidelity risk.

---

# 37. Content Deletion

Unnecessary deletion is also a fidelity risk.

---

# 38. Sentence Rewriting

Sentence-level rewriting should be measured as a larger intervention than
minor lexical or punctuation changes when that distinction is scientifically
appropriate.

---

# 39. Paragraph Rewriting

Paragraph-level rewriting requires explicit justification because of its
larger potential impact.

---

# 40. Structural Rewriting

Structural changes should be treated as high-impact transformations unless
the experiment explicitly permits them.

---

# 41. Factual Consistency

Factual consistency must be evaluated independently from semantic similarity.

---

# 42. Entailment

Where appropriate, evaluate whether the output is entailed by the input and
vice versa.

---

# 43. Contradiction

Explicit contradiction is a critical failure condition where factual
preservation is required.

---

# 44. Omission Detection

Evaluate important information that may have disappeared.

---

# 45. Addition Detection

Evaluate unsupported information introduced by the transformation.

---

# 46. Numerical Integrity

Use exact or appropriately tolerant comparison for numerical content.

---

# 47. Named-Entity Integrity

Named entities should be compared explicitly where relevant.

---

# 48. Terminology Integrity

Domain-specific terminology should be protected.

---

# 49. Readability

Readability may be measured but should not replace semantic or factual
evaluation.

---

# 50. Fluency

Fluency is a quality dimension, not proof of human authorship.

---

# 51. Detector Response

Detector response should be evaluated separately from preservation.

---

# 52. Watermark Response

Watermark response should likewise be evaluated separately.

---

# 53. Multi-Objective Evaluation

The project should treat transformation as a multi-objective optimization
problem where appropriate.

---

# 54. Objective Conflict

Improving one objective may damage another.

These trade-offs must be measured rather than hidden.

---

# 55. Transformation Selection

The final transformation methodology should be evidence-driven.

---

# 56. Research Outputs

This area should produce:

- transformation taxonomy;
- preservation metrics;
- minimality methodology;
- failure taxonomy;
- multilingual preservation methodology;
- evaluation protocols.

---

# 57. Final Principle

The value of a transformation is not determined solely by what it changes.

It must also be evaluated by what it preserves.

---

# 58. Literature Findings (2026-08-24)

Populates §3-§56 above with real transformation/preservation research,
concentrated on the detector-evasion and watermark-removal paraphrasing
literature since that is where this project's own transformation
questions are most directly tested. Every claim is registered in
`docs/00-project/RESEARCH-REGISTRY.md` under the cited `R-XXXX`
identifier. Confidence markers follow the R04 §39 convention. This is a
first literature pass, not a claim of research completeness.

## 58.1 Minimality as a Hard Constraint, Not Only a Soft Trade-off — Populated

Addresses §4-5 (Minimality, Transformation Magnitude): DEPO (R-0074)
frames semantic preservation as an explicit constraint (BERTScore ≥ 0.85)
in a constrained optimization, rather than a scalarized soft objective,
and shows naive linear-weighting baselines fail to satisfy the
constraint. **No evidence found** of any paper whose stated objective is
literally "minimize edit distance subject to evasion success" — the
closest work uses a semantic-similarity floor or an explicit deletion-
percentage knob (R-0075) instead of edit-distance minimization per se.

## 58.2 Semantic Preservation Metrics — Populated, Metric Heterogeneity Confirmed

Addresses §6 (Semantic Preservation) and §27 (Metric Diversity): DIPPER
(R-0024, updated) uses P-SP with a 0.76 threshold; DEPO (R-0074) uses
BERTScore F1; StealthRL (R-0076) uses E5 cosine similarity *and* an
LLM-as-judge Likert scale that visibly diverges from the embedding metric
on the same outputs (0.901 similarity vs. 2.64/5 LLM-judge rating). No
single standardized semantic-preservation metric exists in this
literature — P-SP, BERTScore, T5/E5 embeddings, and LLM-as-judge all
appear across different papers, sometimes disagreeing on the same system.
This is direct empirical confirmation of §27's principle ("no single
similarity metric should define preservation universally"), not merely a
design assumption.

## 58.3 Factual Consistency — Confirmed Gap

Addresses §7 (Factual Preservation) and §41-43 (Factual Consistency,
Entailment, Contradiction): an established factuality-metric toolkit
exists for summarization (FactCC, SummaC, QAFactEval, AlignScore —
R-0085, EVIDENCE tier for existence). **No evidence found** of any of
these, or an LLM-as-judge factuality protocol, being applied specifically
to detector-evasion or watermark-removal paraphrasing — a genuine,
confirmed gap between an available toolkit and this project's actual use
case, not a search failure. A related but distinct finding: certainty/
hedging distortion during rewriting (R-0078) is explicitly *not*
factuality measurement by its own authors' framing, and should not be
conflated with it — see §58.6.

## 58.4 Numerical and Named-Entity Preservation — Thin, Anecdotal Evidence Only

Addresses §8-9 (Numerical Preservation, Entity Preservation): the
clearest evidence found is a single illustrative example (R-0079) of
DIPPER paraphrasing inconsistently transforming a financial figure
("$1.1218") across rounds — directly paralleling the watermark-driven
numeric-drift concern already documented in R02 §37.2 (R-0041), but here
for plain, non-watermark paraphrasing. This is anecdotal, not a
systematic quantified accuracy rate. **No evidence found** of a
dedicated, large-N numeric- or entity-preservation-rate study for
detector-evasion/watermark-removal paraphrasing specifically.

## 58.5 Multi-Objective / Pareto Trade-off Analysis — Strongest Evidence Found

Addresses §20 (Pareto Analysis) and §54 (Objective Conflict) — the
best-evidenced sub-topic in this pass:

- **The Mark Fades** (R-0075, peer-reviewed, Findings of ACL 2026):
  genetic-algorithm Pareto-front optimization of watermark removal;
  near-100% attack success at BERTScore 0.73-0.77 (moderate), ASR ~97%
  but BERTScore collapsing to 0.56 at an aggressive 80%-deletion setting.
- **StealthRL** (R-0076) and **TAROT** (R-0080) each report their own
  method-comparison trade-off tables showing evasion/obfuscation strength
  and preservation moving in opposite directions.
- **Cross-paper pattern (EVIDENCE tier, independently corroborated across
  R-0074/R-0075/R-0076/R-0080 despite each individual number being
  AUTHOR-REPORTED)**: aggressive evasion or obfuscation reliably buys
  detection/evasion success at a measurable, sometimes steep, quality
  cost, and RL/preference-optimization method choice measurably shifts
  the operating point on that trade-off.

## 58.6 Repeated/Iterative Transformation — Populated, Short-Horizon Only

Addresses §32 (Repeated Transformation): PADBen (R-0077) measures 3-round
paraphrase drift (BGE-M3 cosine distance 0.085→0.134); Belem et al.
(R-0078) measures certainty/hedging distortion across 5-round rewriting
chains, finding domain-dependent dynamics — scientific-domain distortion
plateaus after the first rewrite, medical-domain certainty inflation
compounds progressively (20%→40% over 5 iterations for one tested model).
**No evidence found** of a continuous drift curve beyond 5 rounds using
one consistent standard metric — the two studies found are short-horizon
and use incompatible metrics with each other, so they cannot be combined
into a single "meaning half-life" curve. The certainty/hedging dimension
itself (R-0078) is not currently named in §3's preservation-dimension
list — flagged as a candidate addition, not made unilaterally here.

## 58.7 Human Evaluation Protocols — Two Distinct, Non-Comparative Families Found

Addresses §23-26 (Human Evaluation, Blinding, Pairwise/Absolute
Evaluation): Meier et al. (R-0082) uses a two-phase
correctness-classification-plus-best-worst-scaling protocol and finds
automatic success and human preference diverge for some paraphrase types.
Agrawal & Carpuat (R-0083) uses an entirely different, extrinsic
reading-comprehension protocol. **No evidence found** of a methodology
paper directly comparing blinded-pairwise vs. absolute-rating protocols
specifically for paraphrase/transformation preservation — only these two
non-comparative protocol families, each used in isolation in its own
paper.

## 58.8 Items Requiring Follow-Up Before Being Treated as Established

1. StyleRemix (R-0081), JAMDEC, and "Masks and Mimicry" were identified
   as topically on-point for style-transfer preservation trade-offs but
   not deep-read in this pass — specific figures should not be cited
   until a follow-up fetch.
2. R-0079's numeric-drift finding is a single illustrative example, not a
   systematic study — do not generalize its magnitude.
3. The certainty/hedging preservation dimension (R-0078) is a candidate
   addition to §3's preservation-dimension list, not yet incorporated —
   requires a project decision, not a unilateral edit.
4. R-0084 (Meta FAIR post-hoc watermarking) is on the watermark-embedding
   side, not the evasion side that is this project's primary concern —
   should not be conflated with R-0075/R-0076's evasion findings.
5. As with prior passes, all AUTHOR-REPORTED figures cited above remain
   unverified pending independent replication; none should be cited as
   established fact in a normative document without that verification.