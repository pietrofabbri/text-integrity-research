# R09 — Local Deployment Feasibility Research

**Status:** ACTIVE — confirmed as the project's ninth research domain per
`docs/00-project/DECISION-LOG.md` DEC-013 (2026-09-12). The identifier
`R09` and this domain's addition to `RESEARCH-MAP.md`'s diagram (§2) and
domain-status table (§34) are now confirmed, not proposed. (This file was
originally written and circulated as a proposal; DEC-013 records the
owner's approval. No content changed as a result of confirmation — only
this status language.)
**Version:** 0.2
**Document type:** Scientific research domain
**Parent:** docs/02-research/RESEARCH-MAP.md
**Methodology:** docs/02-research/R01-literature-research-methodology.md
**Trigger:** `docs/00-project/OPEN-QUESTIONS.md` Q-008

---

# 1. Purpose

This document defines the scientific research scope for the question R01-R08
explicitly left unaddressed (OPEN-QUESTIONS.md Q-008, confirmed as a gap in
all eight prior literature-research passes): which locally-deployable models
can provide sufficient validation quality for this project's tasks within
its local storage/resource budget (KB-007, ~30GB).

This is a different kind of question from R01-R08. Those domains study the
external scientific literature on watermarking, detection, transformation
and evaluation *in the abstract*. This domain studies a project-specific
engineering-feasibility question: given the tasks 03-scientific-specification
already implies the project needs to perform locally (semantic-similarity
scoring, factual-consistency checking, AI-text detection), what concrete,
currently-available local model options exist, at what verified disk size,
and with what evidenced quality.

---

# 2. Relationship to R01-R08

This domain does not duplicate R02-R05's detection/watermarking literature
review. It is downstream of it: R04's detector taxonomy (§3) and R08's
storage-footprint findings (§69.2) are prerequisites this domain builds on
rather than re-derives. Where this domain's findings materially update or
qualify an R01-R08 finding — e.g. concrete open-detector storage costs
that R08 §69.2 flagged as "inconsistently published" — the cross-reference
is made explicitly in the relevant subsection below rather than silently
restated as new.

---

# 3. Scope — Three Validation Sub-Tasks

Framed around the three concrete local-validation needs the project's
existing documentation already implies (S02/S04/S05 requirements;
RESEARCH-MAP.md's own domain list):

- **Semantic-similarity scoring** — measuring whether a transformation
  preserved meaning (relevant to Q-001, R06 §3's preservation dimensions).
- **Factual-consistency checking** — measuring whether a transformation
  introduced factual drift (relevant to KB-012's factuality gap).
- **AI-text detection** — a locally-runnable detection capability, distinct
  from the external/cloud detectors DEC-002 already permits as optional
  evidence sources.

A fourth cross-cutting variable — **quantization** — affects the storage
cost of any of the above and is treated separately (§6).

---

# 4. Local Storage Constraint (Restated)

Per `docs/00-project/KNOWLEDGE-BACKLOG.md` KB-007 and
`docs/02-research/R08-benchmark-dataset-research.md` §9, the project's full
local data environment should target approximately 30GB. This domain treats
that figure as a hard external constraint, not something to be revisited
here.

---

# 5. Task Decomposition Is Not Optional

A single model or metric must not be assumed adequate for all three
sub-tasks in §3 merely because a single "validation model" would be
architecturally simpler. Each sub-task has a different evidence base,
different quality ceiling, and — critically — a different multilingual
evidence gap (§7).

---

# 6. Quantization as a Cross-Cutting Variable

Any candidate model's on-disk footprint can potentially be reduced via
quantization (for LLM-style models, GGUF k-quants; for encoder models,
ONNX/OpenVINO int8). This domain treats quantized-size and
quantized-quality as claims requiring their own evidence, separate from a
model's native fp16/fp32 footprint — a quantization technique's speed and
accuracy-retention claims do not, by themselves, establish a specific
resulting disk size (see §11.5).

---

# 7. Multilingual Considerations Are Cross-Cutting, Not a Fourth Sub-Task

Per DEC-001/S01, the project targets 13 languages. Each of the three
sub-tasks in §3 has an independent multilingual evidence question:
semantic similarity, factual consistency, and detection do not share a
single multilingual evidence base, and a finding for one must not be
assumed to transfer to another (§11 develops this per sub-task).

---

# 8. Research Outputs

This domain should produce:

- a per-sub-task candidate model shortlist with verified disk sizes;
- an explicit statement of which sub-tasks have a validated multilingual
  option and which do not;
- a quantization-tradeoff reference usable when 04-architecture leaves
  definition phase;
- an explicit list of research gaps (per RESEARCH-MAP.md §31) rather than
  an assumption where evidence is missing.

---

# 9. Final Principle

A model's on-disk footprint fitting within budget is a necessary condition
for its use, not a sufficient one. This domain's findings (§11) show the
opposite failure mode is also live: at least one sub-task (AI-text
detection) is bounded by accuracy under adversarial/cross-lingual
conditions, not by storage, and no amount of remaining storage budget
resolves that limitation on its own.

---

# 10. Literature Findings (2026-09-12)

This is a first, targeted research pass (a single `general-purpose` research
agent, `model: opus`), not a claim of research completeness per
RESEARCH-MAP.md §35. Every claim below is registered in
`docs/00-project/RESEARCH-REGISTRY.md` under the cited `R-01xx` identifier
(R-0102 through R-0121); consult the registry entry for full citation,
methodology and limitations before relying on any claim here. Confidence
markers follow the R04 §39 convention: EVIDENCE (independently corroborated
or primary-source confirmed — for disk sizes, generally verified directly
against a model repository's own file-tree metadata), AUTHOR-REPORTED (from
the source's own claims, not independently replicated), VENDOR (commercial
source, treat cautiously), UNVERIFIED (a claim found but not confirmed
against a primary source).

Per this project's `NO-INVENTION-RULES.md`, the research agent that produced
this pass explicitly declined to cite several "how much fits in 20-30GB"
informal/SEO-style sources it found while searching, on the grounds that
citing them would import fabrication risk into the registry. Nothing in
this section rests on such a source.

## 10.1 Overall Synthesis — Storage Is Not the Single Binding Constraint

The composite question as posed in Q-008 ("which local models fit the
budget") does not have one answer, because the three sub-tasks in §3 are
bounded by different things:

- **Semantic similarity** is comfortably solved within a small storage
  footprint, and (per R-0106) a *smaller* model is not a quality
  compromise here — see §11.2.
- **Factual consistency** is well-solved for English within a small
  footprint (R-0109), but has no evidence-backed open multilingual
  solution — the storage question is almost moot next to the evidence gap
  — see §11.3.
- **AI-text detection** is bounded by accuracy and adversarial/cross-
  lingual robustness, not storage: the best-evidenced open detector
  (R-0117, Binoculars) is accurate but costs nearly the entire ~30GB
  budget by itself, while smaller/cheaper open detectors either target an
  obsolete generator (R-0114) or have unverified accuracy (R-0115,
  R-0116) — see §11.4.

An illustrative (not decided, not exhaustive) combination using only
components with an EVIDENCE-tagged disk size — multilingual-e5-large-
instruct for semantic similarity (R-0103, ~1.14GB), mDeBERTa-v3-xnli for
multilingual factual/entailment signal (R-0111, ~0.58GB, task-fit
unverified — see §11.3), and a Q4_K_M-quantized general-purpose 8B model
as a local fallback for tasks the specialist models don't cover (R-0121,
~4.92GB) — totals under 7GB, leaving over 20GB of the ~30GB budget
unused. This illustrates that storage comfortably accommodates a
lightweight multi-task stack; it is not a proposed architecture, and it
deliberately excludes any detection component, since §11.4 shows detection
cost varies by more than 4x depending on which open detector is chosen and
none of the cheap options currently has solid evidence behind it.

## 10.2 Semantic-Similarity Sub-Task — Populated

Addresses §3 (semantic similarity) and Q-001 (semantic-equivalence metric):

- **multilingual-e5-large-instruct** (R-0103, ~1.14GB deployable, fp16) is
  independently ranked #1 among publicly available models on MMTEB
  (R-0106, EVIDENCE — third-party benchmark, not self-reported), ahead of
  7B-class models GritLM-7B and e5-mistral-7b-instruct. R-0106 is itself
  the single strongest piece of evidence in this pass that, for semantic
  similarity, a larger local model is not better per gigabyte.
- **multilingual-e5-large** (R-0102, ~2.24GB, fp32) is the non-instruct,
  non-fp16 sibling; Mr. TyDi MRR@10 70.5 is AUTHOR-REPORTED.
- **multilingual-e5-small** (R-0104, ~0.49GB) is a lower-footprint option
  with quality UNVERIFIED at this specific size — EVIDENCE covers size
  only.
- **BGE-M3** (R-0105, ~2.29GB) is the only candidate with 8192-token
  context (16x E5's 512-token limit), relevant if the project's actual
  documents exceed E5's window; its multi-vector/ColBERT mode has an
  unquantified separate index-storage cost.
- **Qwen3-Embedding-8B** (R-0107, ~15.15GB) illustrates the cost of the
  "one large embedder" option: roughly half the entire ~30GB budget for
  one sub-task, for a quality claim (AUTHOR-REPORTED, 70.58 MTEB
  Multilingual) that is both unverified and, per its own publication date,
  stale relative to this research.
- **Quantized-size gap** (R-0108): Sentence-Transformers' own documentation
  reports strong speed (3.2-5.3x) and quality-retention (>99.5%) figures
  for ONNX/OpenVINO int8 quantization of embedding models, but **no
  evidence was found of the resulting on-disk size** for any specific
  multilingual embedding model — the commonly assumed ~4x reduction is an
  inference, not a sourced fact, and would need to be measured directly by
  the project rather than assumed.

## 10.3 Factual-Consistency Sub-Task — Populated, Multilingual Gap Confirmed

Addresses §3 (factual consistency) and KB-012 (factual-consistency metrics
unvalidated for this project's use case):

- **MiniCheck-FT5** (R-0109, 770M params) reaches 74.7% average balanced
  accuracy on LLM-AggreFact, within 0.6 points of GPT-4 (75.3%) at over
  400x lower inference cost (EVIDENCE — peer-reviewed, evaluates GPT-4 on
  a shared benchmark). This is the strongest single piece of evidence in
  this pass that a small specialist model can match a much larger
  general-purpose model on one of the project's specific sub-tasks.
  **However, the authors explicitly state their models are trained
  exclusively on English data** and name the absence of a human-annotated
  non-English factual-consistency dataset as an open limitation.
- **Vectara HHEM-2.1-Open** (R-0110, ~0.44GB) is a smaller alternative,
  also English-only (VENDOR quality claims) — its multilingual sibling
  (HHEM-2.3) exists only as a commercial product, which would violate
  DEC-001's no-mandatory-external-service constraint if adopted.
- **mDeBERTa-v3-xnli** (R-0111, ~0.58GB) is the only genuinely
  multilingual, openly-licensed candidate found — fine-tuned on 27
  languages, XNLI accuracy 0.744-0.871 across 15 languages
  (AUTHOR-REPORTED). Its task-fit is unverified: XNLI is sentence-pair
  entailment, a substantially easier and different task than document-
  level factual-consistency checking, and its accuracy range is not
  directly comparable to R-0109's LLM-AggreFact figures.
- **mFACT** (R-0112, peer-reviewed, EVIDENCE) is a direct negative result
  against the assumption that an English-trained factual-consistency
  checker can simply be used cross-lingually: English faithfulness
  metrics do not transfer well to other languages, and multilingual LLMs
  hallucinate more often outside English. This is adjacent evidence
  (studies summarization, not this project's transformation task) but
  directly undermines relying on R-0109/R-0110 outside English without
  further validation.

**Net finding**: factual consistency has a strong, cheap, well-evidenced
solution for English and no evidence-backed solution for the project's
other 12 target languages. Storage is not the constraint here; validated
multilingual evidence is.

## 10.4 AI-Text-Detection Sub-Task — Accuracy, Not Storage, Is the Constraint

Addresses §3 (detection) and directly extends R04 §39's detector-taxonomy
findings with concrete local-deployment figures R04 did not investigate:

- **RAID** (R-0113, peer-reviewed, EVIDENCE) found accuracy at FPR=5%
  ranging from 85.0% (a closed commercial detector) down to 79.6%
  (Binoculars, the best open detector) to 70.9% (RADAR), with severe
  generalization collapse for some detectors (RoBERTa-Large: 96.3% on
  GPT-2 greedy decoding, 33.8% on GPT-4) and adversarial fragility
  (homoglyph attacks cost Binoculars 41.9 points, Originality 75.7
  points).
- **Binoculars** (R-0117, peer-reviewed method + independent RAID
  corroboration) is the best-evidenced open detector, but running it as
  published requires both Falcon-7B and Falcon-7B-Instruct: verified
  (EVIDENCE, primary repository metadata) at 14.43GB each, **~28.87GB
  combined — effectively the project's entire ~30GB budget for this one
  sub-task alone**. Its multilingual behavior is explicitly weaker ("poor
  recall" on Bulgarian and Urdu per the authors), and **no evidence was
  found on whether a quantized Falcon-7B pair preserves detection
  quality** — the method depends on fine-grained inter-model perplexity
  differences that quantization noise could plausibly disrupt. This is
  flagged as a concrete, low-cost experiment the project could run itself
  rather than a known fact either way.
- **roberta-base-openai-detector** (R-0114, ~0.50GB) is cheap but
  targets an obsolete generator (GPT-2); its own authors' card states it
  is "not high enough accuracy for standalone detection," and R-0113
  independently confirms severe accuracy collapse for architecturally
  similar RoBERTa-based detectors on modern generators.
  **Desklib ai-text-detector-v1.01** (R-0115, ~1.74GB) claims a top RAID
  leaderboard position, but this pass could not independently confirm it
  — the only corroboration found was the vendor's own promotional post,
  so this claim is UNVERIFIED and requires direct leaderboard confirmation
  before any reliance. **SuperAnnotate ai-detector-low-fpr** (R-0116) has
  no extractable accuracy figure in this pass and carries a non-standard
  license (SAIPL) requiring separate legal review.
- **M4GT-Bench** (R-0118, peer-reviewed, EVIDENCE) directly quantifies the
  multilingual generalization failure mode for detection, covering 9 of
  the project's 13 target languages: leave-one-language-out accuracy
  collapses toward chance (~53%) for Bulgarian, Russian and Indonesian,
  with the detector degenerating into labeling nearly everything as
  machine-generated (recall near 100%, precision near 51-53%) — a failure
  mode worse than having no detector at all for those languages.

**Net finding**: no amount of remaining storage budget resolves this
sub-task's core problem. The best open detector is accurate but nearly
consumes the entire budget by itself and has an unstudied
quantization-compatibility question; the cheap alternatives are either
obsolete, unverified, or license-encumbered; and independent evidence
shows severe, near-chance failure on several of the project's target
languages regardless of which detector is chosen. This directly extends
R04 §39.4's multilingual-detection-gap finding and RAID/M4GT-Bench should
be read alongside it, not in isolation.

## 10.5 Quantization — General Reference, Multilingual Interaction Unstudied

Addresses §6 (Quantization as a Cross-Cutting Variable):

- **llama.cpp k-quant reference** (R-0119): the canonical LLaMA-7B-class
  size/perplexity table (Q4_K_M 3.80GB / +0.0535 perplexity vs. F16
  13.00GB baseline; maintainers recommend Q4_K_M/Q5_K_S/Q5_K_M as balanced
  choices). Sizes independently corroborated by R-0121's real GGUF file
  sizes for a different model; perplexity deltas are AUTHOR-REPORTED,
  single-source.
- **"Which Quantization Should I Use?"** (R-0120, 2026, EVIDENCE —
  independent, peer-reviewed-track evaluation on standard downstream
  benchmarks, not perplexity alone) found that moving from F16 to Q4_K_M
  (~3.1x disk reduction) costs only ~1.07 MMLU points and leaves GSM8K
  statistically flat for Llama-3.1-8B-Instruct, with visible degradation
  only appearing at Q3_K_M. **All evaluated benchmarks are English-only**,
  and the paper explicitly does not test whether quantization degrades
  multilingual performance faster than English — a materially open
  question for this project's 13-language target, since quantization is
  known to affect distribution tails most, and non-English capability
  often lives in that tail.
- **Meta-Llama-3.1-8B-Instruct GGUF real file sizes** (R-0121, EVIDENCE,
  primary repository metadata): Q2_K 3.18GB, Q3_K_M 4.02GB, Q4_K_M
  4.92GB, Q5_K_M 5.73GB, Q6_K 6.60GB, Q8_0 8.54GB, f32 32.13GB —
  cross-consistent with R-0119/R-0120's figures for a different model
  family, and used as the concrete size basis for the illustrative
  composite in §10.1.

**Net finding**: quantization is a well-evidenced, low-cost way to shrink
a general-purpose local LLM's footprint with minimal English-benchmark
quality loss, but its interaction with the project's 13-language
requirement — and with Binoculars' specific detection mechanism (§10.4)
— is an explicit, confirmed research gap, not something this pass can
resolve by inference from English-only benchmarks.

## 10.6 Proposed Refinement of Q-008 (Not a Resolution)

This pass's overall finding is that Q-008 as originally posed — a single
composite question about "which local models fit the budget" — combines
two questions with very different answers. This is offered to the owner as
a **proposed refinement**, not a resolution (per DEC-009, a research
finding does not itself decide anything):

- **A storage sub-question**, which this pass answers with reasonable
  confidence: yes, a multi-task validation stack fits comfortably within
  the ~30GB budget, *provided* the AI-text-detection component chosen is
  not Binoculars run at full precision (§10.1, §10.4).
- **One or more quality sub-questions**, which remain genuinely open:
  whether any evidence-backed multilingual factual-consistency option
  exists (§10.3 — currently none does), and whether any local detection
  option combines acceptable accuracy, acceptable multilingual robustness,
  and acceptable storage cost simultaneously (§10.4 — currently no
  candidate satisfies all three).

Whether to formally split Q-008 into separate tracked questions, keep it
as one question with this evidence appended, or handle it some other way
is left to the owner/project's own open-question governance
(`docs/00-project/OPEN-QUESTIONS.md`) — see that document's own Q-008
entry, updated alongside this file.

## 10.7 Items Requiring Follow-Up Before Being Treated as Established

Recorded per `NO-INVENTION-RULES.md` "Missing Information" — known gaps,
not filled with plausible assumptions:

1. Whether a quantized Falcon-7B/Falcon-7B-Instruct pair preserves
   Binoculars' detection quality is untested (§10.4) — a concrete,
   relatively low-cost experiment the project could run itself.
2. Actual on-disk size after ONNX/OpenVINO int8 quantization of any of
   R-0102/R-0103/R-0105 has not been measured or sourced anywhere found in
   this pass (§10.2) — the assumed ~4x reduction is an inference.
3. Desklib's (R-0115) claimed top-RAID-leaderboard position needs direct
   confirmation against the live leaderboard before any reliance.
4. mDeBERTa-v3-xnli's (R-0111) and BGE-M3's (R-0105) task-fit for this
   project's *specific* factual-consistency and long-document-comparison
   use cases (as opposed to XNLI/MIRACL-style benchmark tasks) has not
   been measured.
5. Whether quantization degrades multilingual capability faster than
   English capability (§10.5) is, per R-0120's own stated limitation, an
   entirely open question — no source in this pass measured it in either
   direction.

---

# 11. Status of This Domain — Confirmed

The identifier `R09`, this file's place as a node in `RESEARCH-MAP.md`'s
diagram (§2 of that document), and its row in the domain-status table
(§34 of that document) are confirmed per
`docs/00-project/DECISION-LOG.md` DEC-013 (2026-09-12). This section
previously read "Proposed Status... Awaiting Owner Decision"; it is kept
(rather than deleted) so the resolution remains traceable, per this
project's general practice of recording rather than silently erasing a
prior state. Note that §10.6's proposed refinement of Q-008 (splitting
it into a storage sub-question and quality sub-questions) is a separate,
still-open decision — DEC-013 confirms only this domain's identity and
structural placement, not that refinement.
