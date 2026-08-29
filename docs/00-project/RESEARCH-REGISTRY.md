# Research Registry

## Purpose

The Research Registry records scientific and technical sources relevant
to the project.

It is not itself a requirements document.

Research findings must not automatically become normative requirements.

---

# Source Categories

- WATERMARKING
- PROVENANCE
- AI-DETECTION
- ADVERSARIAL-ROBUSTNESS
- TEXT-TRANSFORMATION
- SEMANTIC-PRESERVATION
- MULTILINGUAL
- EVALUATION
- SECURITY
- REPRODUCIBILITY
- OTHER

---

# Evidence Status

- UNREVIEWED
- REVIEWED
- RELEVANT
- PARTIALLY_RELEVANT
- SUPERSEDED
- REJECTED
- INCONCLUSIVE

---

# Source Template

## R-XXXX — Title

### Citation

Full bibliographic citation.

### Source

Canonical source.

### Publication Date

YYYY-MM-DD

### Category

CATEGORY

### Languages

Relevant languages, if applicable.

### Claims Relevant to Project

Short factual summary.

### Methodology

Summary of methodology.

### Limitations

Known limitations.

### Relevance

Why this matters.

### Potential Project Impact

Possible affected areas.

### Reproducibility

Available / Partial / Unknown.

### Status

UNREVIEWED

---

# Initial Sources

## R-0001 — A Watermark for Large Language Models

### Citation

Kirchenbauer et al.

### Source

arXiv:2301.10226

### Category

WATERMARKING

### Claims Relevant to Project

The work describes a statistical watermarking mechanism for
language-model-generated text and a statistical detection procedure.

### Relevance

This is a foundational reference for understanding:

- statistical watermark construction;
- detection assumptions;
- statistical significance;
- entropy-related considerations;
- robustness questions.

### Limitations

The mechanism represents one watermarking family and must not be
treated as representative of every current or future watermarking
approach.

### Status

REVIEWED

---

## R-0002 — GLTR: Statistical Detection and Visualization of Generated Text

### Citation

Gehrmann, Strobelt, Rush, "GLTR: Statistical Detection and Visualization of
Generated Text," ACL 2019 (System Demonstrations).

### Source

arXiv:1906.04043 / ACL Anthology P19-3019

### Publication Date

2019-06-01 (approximate, per arXiv submission)

### Category

AI-DETECTION

### Claims Relevant to Project

Describes a zero-shot statistical method that visualizes token-rank under a
reference language model; an early example of the perplexity/likelihood
detection family.

### Methodology

Colors each token by how predictable it was under a reference LM; no
classifier training on labeled human/AI text.

### Limitations

Predates modern instruction-tuned LLMs; a visualization/research tool, not
a calibrated production classifier.

### Relevance

Establishes the statistical/zero-shot detection family referenced in R04 §3.

### Potential Project Impact

Research, Scientific Specification (detection-family taxonomy)

### Reproducibility

Available (open research tool)

### Status

REVIEWED

---

## R-0003 — DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature

### Citation

Mitchell, Lee, Khazatsky, Manning, Finn, "DetectGPT," ICML 2023.

### Source

arXiv:2301.11305

### Publication Date

2023-01-01 (approximate)

### Category

AI-DETECTION

### Claims Relevant to Project

Zero-shot method using "probability curvature": perturbs a passage with a
mask-filling model and tests whether the original sits at a local
probability maximum relative to perturbations.

### Methodology

Requires many perturbation queries against a scoring model per evaluated
text; no training on labeled AI/human text.

### Limitations

Computationally expensive (many model queries per decision); accuracy under
paraphrasing attack is separately documented as poor (see R-0021).

### Relevance

Foundational zero-shot detection method; baseline for later work
(Fast-DetectGPT, Binoculars).

### Potential Project Impact

Research, Scientific Specification, Validation (candidate detector for
evaluation-profile composition)

### Reproducibility

Available (open source, code linked from paper)

### Status

REVIEWED

---

## R-0004 — Fast-DetectGPT: Efficient Zero-Shot Detection via Conditional Probability Curvature

### Citation

Bao, Zhao, Teng, Yang, Zhang, "Fast-DetectGPT," ICLR 2024.

### Source

arXiv:2310.05130

### Category

AI-DETECTION

### Claims Relevant to Project

Replaces DetectGPT's expensive perturbation step with sampled conditional
probability curvature.

### Methodology

Zero-shot; no training on labeled AI/human text.

### Limitations

Speed/accuracy improvement figures (~75% relative accuracy gain, ~340x
speedup) are author-reported in the paper's own benchmark and were not
independently corroborated during this research pass — treat as
UNVERIFIED CLAIM pending independent replication.

### Relevance

Practical zero-shot alternative to DetectGPT; relevant if the project needs
a compute-cheap offline-compatible detector (per DEC-001, offline-core
requirement).

### Potential Project Impact

Research, Architecture (offline detector candidate)

### Reproducibility

Available (open source)

### Status

PARTIALLY_RELEVANT — methodology reviewed, quantitative claims unverified

---

## R-0005 — Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text

### Citation

Hans, Schwarzschild, Cherepanova, et al., "Binoculars," ICML 2024.

### Source

arXiv:2401.12070

### Category

AI-DETECTION

### Claims Relevant to Project

Zero-shot detector comparing perplexity of text under two related pretrained
LLMs ("observer"/"performer"); claims generalization to generator models
never seen during design.

### Methodology

No training on generator-specific labeled data; requires only two
off-the-shelf pretrained LLMs at detection time.

### Limitations

The reported figure (detects >90% of LLM samples at 0.01% false-positive
rate) is the authors' own benchmark result — not independently replicated
in every setting found during this research pass. Treat as
AUTHOR-REPORTED, not independently verified.

### Relevance

Strong zero-shot candidate; offline-compatible (no API dependency on the
generating model).

### Potential Project Impact

Research, Architecture, Validation

### Reproducibility

Available (open source)

### Status

PARTIALLY_RELEVANT — methodology reviewed, headline accuracy figure
unverified

---

## R-0006 — OpenAI RoBERTa GPT-2 Output Detector

### Citation

OpenAI, "GPT-2: 1.5B release" (Nov 2019); model cards for
roberta-base-openai-detector / roberta-large-openai-detector.

### Source

https://openai.com/index/gpt-2-1-5b-release/ ;
https://huggingface.co/openai-community/roberta-base-openai-detector

### Publication Date

2019-11-01

### Category

AI-DETECTION

### Claims Relevant to Project

A fine-tuned RoBERTa classifier trained specifically to discriminate GPT-2
outputs from human text.

### Limitations

Specific to GPT-2-era text; not designed for, and not expected to
generalize to, modern instruction-tuned LLM output. Documents the
"detector obsolescence as generation models change" risk already tracked
in KB-001.

### Relevance

Historical baseline; illustrates that classifier-based detectors are
generator-specific and require re-training/re-validation as models change.

### Potential Project Impact

Research, Scientific Specification (§29 Effectiveness Profiles must be
generator-version-scoped)

### Reproducibility

Available (open source)

### Status

REVIEWED

---

## R-0007 — OpenAI's 2023 AI Text Classifier (Launched and Withdrawn)

### Citation

OpenAI, "New AI classifier for indicating AI-written text" (Jan 2023);
TechCrunch, "OpenAI scuttles AI-written text detector over 'low rate of
accuracy'" (Jul 25, 2023).

### Source

https://openai.com/index/new-ai-classifier-for-indicating-ai-written-text/ ;
https://techcrunch.com/2023/07/25/openai-scuttles-ai-written-text-detector-over-low-rate-of-accuracy/

### Publication Date

2023-01-01 (launch); 2023-07-25 (withdrawal)

### Category

AI-DETECTION

### Claims Relevant to Project

OpenAI publicly launched, then approximately six months later withdrew, its
own general-purpose AI-text classifier, citing "low rate of accuracy."

### Limitations

None beyond the fact itself — this is a direct, low-ambiguity primary/news
source pairing.

### Relevance

The single cleanest documented case of a detector vendor judging its own
tool inadequate; directly supports DEC-007 (effectiveness must be
versioned) and the project's general skepticism toward treating any one
detector as ground truth (SPECIFICATION-MAP.md §17).

### Potential Project Impact

Scientific Specification §17 (AI-Detection-Related Requirements),
Certification (do not imply permanent validity of a detector-based gate)

### Reproducibility

N/A (historical/news event, not an experiment)

### Status

REVIEWED

---

## R-0008 — RADAR: Robust AI-Text Detection via Adversarial Learning

### Citation

Hu, Chen, Ho, "RADAR," NeurIPS 2023.

### Source

arXiv:2307.03838

### Category

AI-DETECTION

### Claims Relevant to Project

Trains a detector adversarially against a co-trained paraphraser
specifically to improve robustness to paraphrasing attacks.

### Methodology

Adversarial (GAN-like) co-training of detector and paraphraser; evaluated
against 8 LLMs across 4 datasets per the paper.

### Limitations

Author-reported superiority claims not independently re-verified in this
pass.

### Relevance

Directly relevant to the project's transformation/detection interaction
(R06) since it is a detector explicitly designed around the
paraphrase-evasion failure mode documented in R-0021.

### Potential Project Impact

Research, Validation (candidate for paraphrase-robustness evaluation
profile)

### Reproducibility

Available (open source, IBM)

### Status

REVIEWED

---

## R-0009 — GPTZero: Robust Detection of LLM-Generated Texts (Technical Report)

### Citation

Adam, Cui, Thomas, et al., "GPTZero: Robust Detection of LLM-Generated
Texts," 2026.

### Source

arXiv:2602.13042 ; vendor methodology pages at gptzero.me

### Category

AI-DETECTION

### Claims Relevant to Project

Describes GPTZero (a widely used commercial detector) as using a
"hierarchical, multi-task architecture"; historically marketed around
perplexity/burstiness signals.

### Limitations

Vendor-authored technical report; claims of state-of-the-art accuracy and
paraphrase robustness are not independently corroborated. Specific
accuracy numbers could not be extracted from the abstract during this
research pass.

### Relevance

Represents the commercial/product detector family; relevant for any
comparison against open research methods.

### Potential Project Impact

Research (detector portfolio), Validation

### Reproducibility

Unknown (closed/commercial system)

### Status

PARTIALLY_RELEVANT — vendor source, unverified accuracy claims

---

## R-0010 — Pangram AI-Generated Text Classifier (Technical Reports)

### Citation

Emi & Spero, "Technical Report on the Pangram AI-Generated Text
Classifier," arXiv:2402.14873 (2024); Glickenhaus, Thai, Russell, et al.,
"Pangram 4 Technical Report," arXiv:2607.27183 (2026).

### Source

arXiv:2402.14873 ; arXiv:2607.27183

### Category

AI-DETECTION

### Claims Relevant to Project

Transformer classifier trained with "hard negative mining with synthetic
mirrors"; claims very low false-positive/false-negative rates (Pangram 4:
self-reported AUROC 0.9916, FPR 0.0041%, FNR 0.3396%) and claims no bias
against non-native English speakers.

### Limitations

**Conflict of interest: the authors are Pangram's founders.** All
comparative-superiority and bias-absence claims are vendor-authored and
were not independently verified in this research pass. Do not cite the
specific accuracy figures as established fact without independent
corroboration.

### Relevance

Represents the commercial detector family; the "no bias" claim is directly
relevant to, and should be checked against, the independent bias findings
in R-0023 and R-0025 before being relied upon.

### Potential Project Impact

Research (detector portfolio) — flag for OPEN-QUESTIONS if used in any
validation profile

### Reproducibility

Unknown (closed/commercial system; underlying claims not independently
reproducible from the paper alone)

### Status

PARTIALLY_RELEVANT — vendor-authored, conflict of interest noted

---

## R-0011 — DAMAGE: Detecting Adversarially Modified AI Generated Text

### Citation

Masrour, Emi, Spero, "DAMAGE," arXiv:2501.03437.

### Source

arXiv:2501.03437

### Category

ADVERSARIAL-ROBUSTNESS

### Claims Relevant to Project

Evaluates 19 distinct "AI humanizer" tools and finds many existing
detectors fail against their output; proposes a detector trained with
augmented data to generalize across humanizers.

### Limitations

Same Pangram-team conflict of interest as R-0010 — the proposed detector is
benchmarked as the winner by its own authors.

### Relevance

Documents a concrete, real evasion-tooling ecosystem ("AI humanizers") that
the project's robustness requirements (SPECIFICATION-MAP.md §23) must
account for.

### Potential Project Impact

Research, Scientific Specification §23 (Robustness Specification)

### Reproducibility

Partial (methodology described; humanizer tools are third-party commercial
products)

### Status

PARTIALLY_RELEVANT — conflict of interest noted; existence of humanizer
evasion risk is the load-bearing claim, not the specific comparative
numbers

---

## R-0012 — Testing of Detection Tools for AI-Generated Text (Independent Multi-Tool Study)

### Citation

Weber-Wulff, Anohina-Naumeca, Bjelobaba, Foltýnek, Guerrero-Dib, Popoola,
Šigut, Waddington, "Testing of detection tools for AI-generated text,"
International Journal for Educational Integrity, 2023.

### Source

https://link.springer.com/article/10.1007/s40979-023-00146-z ;
arXiv:2306.15666

### Publication Date

2023-01-01 (approximate)

### Category

AI-DETECTION

### Claims Relevant to Project

Independent (non-vendor) test of 14 free + 2 commercial tools: all scored
below 80% accuracy overall, only 5 exceeded 70%; ~20% of AI-generated text
misclassified as human, rising to ~50% after obfuscation; machine-translated
human text triggered false positives in multiple tools; false-positive
risk ranged 0%–50% by tool. Authors concluded tools are "neither accurate
nor reliable" for high-stakes use.

### Methodology

Independent academic evaluation, not vendor-sponsored.

### Limitations

2023-era tools and models; results will not directly transfer to current
detector versions or current-generation LLMs (temporal validity — see
RESEARCH-MAP.md §26 "Research Freshness").

### Relevance

The strongest non-vendor corroboration found for the project's core
skepticism toward single-detector ground truth
(SPECIFICATION-MAP.md §17–18); directly supports DEC-002/DEC-007.

### Potential Project Impact

Scientific Specification §17-18, Certification (do not gate on a single
commercial detector)

### Reproducibility

Partial (methodology described; commercial tools are black-box)

### Status

REVIEWED

---

## R-0013 — Robust Distortion-free Watermarks for Language Models

### Citation

Kuditipudi, Thickstun, Hashimoto, Liang, arXiv:2307.15593.

### Source

arXiv:2307.15593

### Category

WATERMARKING

### Claims Relevant to Project

An alternative watermarking scheme designed so the watermark does not
change the model's output distribution, using a secret pseudorandom
sequence and Levenshtein-distance-based detection for edit robustness.

### Relevance

A second watermarking family distinct from R-0001 (Kirchenbauer);
important for the project's own rule (SPECIFICATION-MAP.md §16) that a
future watermark must not be assumed covered merely by belonging to the
same broad category as a previously studied mechanism.

### Potential Project Impact

Research (watermark taxonomy), Scientific Specification §16

### Reproducibility

Available (open source)

### Status

REVIEWED

---

## R-0014 — Scalable Watermarking for Identifying Large Language Model Outputs (SynthID)

### Citation

Dathathri, See, Ghaisas, Huang, McAdam, Welbl, Bachani, Kaskasoli, et al.,
Nature, 2024.

### Source

https://www.nature.com/articles/s41586-024-08025-4

### Publication Date

2024-01-01 (approximate)

### Category

WATERMARKING

### Claims Relevant to Project

Describes SynthID, a production-deployed text watermark (shipped in
Google's Gemini) using tournament sampling; open-sourced October 2024.

### Limitations

Cooperative-generator watermarking only works if the generating model
embeds the signal — it provides no information about text from
non-cooperating models. This is a structural limitation, not a
performance limitation.

### Relevance

The clearest real-world, production-scale example of watermarking's core
scope limitation; directly informs SPECIFICATION-MAP.md §16 (watermark
requirements must be derived from validated evidence, not assumed to
generalize).

### Potential Project Impact

Scientific Specification §16, Architecture (watermark-detection module
scope boundary)

### Reproducibility

Available (open-sourced by Google DeepMind)

### Status

REVIEWED

---

## R-0015 — Watermark Stealing in Large Language Models

### Citation

Jovanović, Staab, Vechev, ICML 2024.

### Source

arXiv:2402.19361

### Category

ADVERSARIAL-ROBUSTNESS

### Claims Relevant to Project

Shows an attacker can approximate a deployed watermark's rules from API
queries alone, then either scrub the watermark from AI text or spoof it
onto human text.

### Relevance

Demonstrates that watermark-based detection carries a false-accusation
risk (spoofing onto human text), not only an evasion risk — directly
relevant to the project's fidelity/fairness concerns
(S04-fidelity-requirements.md) and to security boundary definitions
(06-security).

### Potential Project Impact

Scientific Specification, Security (06-security), Research

### Reproducibility

Available (open source, project site + code)

### Status

REVIEWED

---

## R-0016 — HC3: How Close is ChatGPT to Human Experts?

### Citation

Guo et al., arXiv:2301.07597; follow-up "HC3 Plus," arXiv:2309.02731.

### Source

arXiv:2301.07597 ; arXiv:2309.02731 ;
github.com/Hello-SimpleAI/chatgpt-comparison-detection

### Category

AI-DETECTION

### Claims Relevant to Project

A parallel human-vs-ChatGPT answer corpus (open-domain QA, finance,
medicine, law, psychology) used both to study human/AI differences and to
train/evaluate detectors.

### Relevance

A named, citable benchmark dataset for the project's benchmark registry
(R08 / DATA-MAP.md).

### Update (2026-08-24, R08 literature pass)

License confirmed via the HF dataset card (`Hello-SimpleAI/HC3`):
**CC-BY-SA-4.0, with an explicit inheritance clause** — "if the source
datasets used in this corpus has a specific license which is stricter
than CC-BY-SA, our products follow the same," meaning actual
redistribution terms are source-corpus-dependent (Reddit ELI5, medical/
finance QA, Wikipedia), not a flat guarantee. Storage size confirmed:
147MB, 48,644 rows. See R08 §69.1 and Q-007.

### Potential Project Impact

Research, Data (07-data), Validation

### Reproducibility

Available (public dataset)

### Status

REVIEWED

---

## R-0017 — TURINGBENCH: A Benchmark Environment for Turing Test in the Age of Neural Text Generation

### Citation

Uchendu, Ma, Le, Zhang, Lee, EMNLP Findings 2021.

### Source

arXiv:2109.13296

### Category

AI-DETECTION

### Claims Relevant to Project

Pairs human text with outputs from ~19 pre-ChatGPT generation models across
two tasks: binary Turing Test and multi-class Authorship Attribution
(which model generated it).

### Limitations

Pre-dates current-generation instruction-tuned LLMs; primarily useful as a
historical/methodological reference, not for evaluating current detectors.

### Relevance

Establishes the "authorship attribution" (which model, not just
human-vs-AI) task framing, relevant to future capability design.

### Potential Project Impact

Research, Data

### Reproducibility

Available (public dataset)

### Status

PARTIALLY_RELEVANT — methodology relevant, dataset temporally dated

---

## R-0018 — MGTBench: Benchmarking Machine-Generated Text Detection

### Citation

He, Shen, Zhang, Backes, Zhang, ACM CCS 2024.

### Source

arXiv:2303.14822

### Category

AI-DETECTION

### Claims Relevant to Project

A benchmarking framework comparing both metric-based zero-shot methods and
trained classifiers under a common evaluation protocol.

### Relevance

A candidate methodological template for the project's own evaluation
framework (R07 / S03-experimental-model.md).

### Potential Project Impact

Research, Validation

### Reproducibility

Available (open source)

### Status

REVIEWED

---

## R-0019 — M4: Multi-generator, Multi-domain, and Multi-lingual Black-Box Machine-Generated Text Detection

### Citation

Wang, Mansurov, Ivanov, et al., EACL 2024.

### Source

arXiv:2305.14902

### Category

MULTILINGUAL

### Claims Relevant to Project

A benchmark explicitly covering multiple generator models, multiple
domains, and multiple languages for black-box detection.

### Limitations

Exact language list/count was not extracted during this research pass —
a follow-up read of the paper body is needed before citing specific
language coverage as fact.

### Relevance

Directly relevant to the project's 13-language multilingual requirement
(SPECIFICATION-MAP.md §20); one of the few multilingual-by-design
detection benchmarks found.

### Potential Project Impact

Research (R05 multilingual), Data, Validation

### Reproducibility

Available (public dataset, per paper)

### Status

PARTIALLY_RELEVANT — relevance confirmed, coverage details need
verification

---

## R-0020 — RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors

### Citation

Dugan, Hwang, Trhlik, Zhu, Ludan, Xu, Ippolito, Callison-Burch, ACL 2024.

### Source

arXiv:2405.07940

### Category

AI-DETECTION

### Claims Relevant to Project

A large-scale benchmark built specifically to stress-test detector
robustness: adversarial/obfuscated variants, multiple domains, multiple
decoding strategies, multiple generator models.

### Relevance

The most directly relevant existing benchmark for the project's own
robustness specification work (SPECIFICATION-MAP.md §23); a strong
candidate to adopt rather than building an equivalent from scratch.

### Update (2026-08-24, R08 literature pass)

License confirmed: **MIT** (GitHub repo `liamdugan/raid` and HF dataset
card agree). Storage: **16.7 GB** on the HF hub; paper states 6,287,820
texts including adversarial attacks. The only stated content-filtering
step is a post-2023 date filter for arXiv abstracts (to avoid
pretraining-memorized text) — **no formal deduplication methodology
(MinHash/LSH or otherwise) is described**. The `raid-bench` pip package
has frequent version releases (v0.0.2–v0.2.0), but these are software/
tooling releases (dependency bumps, metric additions), not dataset
content refreshes — do not conflate the two. The paper's own Limitations
section states an *intent* to release updated versions as generators
age, but no evidence was found that a new-generator dataset refresh has
actually shipped. See R08 §69.1-69.3.

### Potential Project Impact

Research, Data, Validation, Development (candidate to adopt as an
evaluation-profile component)

### Reproducibility

Available (public benchmark)

### Status

REVIEWED

---

## R-0021 — BLUFF: Benchmarking the Detection of False and Synthetic Content Across 58 Low-Resource Languages

### Citation

Lucas, Murtagh-White, Uchendu, Al-Lawati, Yamashita, Macko, Srba, Moro,
Lee, arXiv:2603.00634 (2026); accepted KDD 2026 Datasets and Benchmarks
Track.

### Source

arXiv:2603.00634

### Category

MULTILINGUAL

### Claims Relevant to Project

A large, low-resource-language-focused benchmark (~78-79 languages
across sources, ~20 high-resource / 58-59 low-resource — exact counts
disagree between sources); reports substantial cross-lingual performance
degradation from high- to low-resource languages.

### Limitations

**Specific quantitative figures (cross-lingual macro-F1 gap of ~9.9
points, multiclass degradation up to ~25.3 F1 points, exact language
counts) are drawn from the paper's abstract and secondary summaries only —
the full paper text could not be extracted during this research pass.
Treat these numbers as PROVISIONAL pending direct verification against the
paper's tables.** See KB item on primary-source verification.

### Relevance

The most directly relevant, most recent evidence found for the project's
own multilingual capability-state framework (SPECIFICATION-MAP.md §22);
directly informs KB-006/KB-007 discussions on realistic multilingual
coverage expectations.

### Potential Project Impact

Research (R05), Scientific Specification §20-22, Data, Validation

### Reproducibility

Unknown (benchmark described in abstract; full paper not directly read)

### Status

INCONCLUSIVE — existence and relevance confirmed, specific figures require
primary-source verification

---

## R-0022 — GPT Detectors Are Biased Against Non-Native English Writers

### Citation

Liang, Yuksekgonul, Mao, Wu, Zou, Cell Patterns, 2023.

### Source

arXiv:2304.02819 ; https://www.sciencedirect.com/science/article/pii/S2666389923001307

### Publication Date

2023-07-01 (approximate)

### Category

AI-DETECTION

### Languages

English (non-native vs. native English writers)

### Claims Relevant to Project

Evaluated widely-used GPT detectors on TOEFL essays from non-native
English speakers vs. native-speaker essays; found detectors consistently
misclassify non-native writing as AI-generated while accurately
classifying native writing. Simple prompting strategies were shown to
both mitigate the bias and help evade detection.

### Limitations

**Update (2026-08-24, R05 literature pass):** the paper was fetched
directly (not via secondary summary) during the R05 research pass. The
figure is confirmed as **61.22%** overall false-positive rate on TOEFL
essays (not the previously-circulated "61.3%", which was a
secondary-source rounding/transcription artifact) — EVIDENCE tier. Also
confirmed directly: 89/91 (97.80%) TOEFL essays flagged by at least one
of 7 detectors, 18/91 (19.78%) flagged unanimously by all 7; after
prompting an LLM to "linguistically enhance" the non-native essays, FPR
fell to 11.77% (a 49.45-point drop). No extension of this finding to any
non-English language pair was found in the R05 pass (searched
specifically for German/French/Spanish/Chinese non-native-writer-bias
studies) — this remains an English-only finding; do not generalize to
"AI detectors are biased against non-native writers in general" without
further evidence. See KB-009 (updated) and R05 §47.4.

### Relevance

This is the canonical, most-cited finding on detector bias; directly
relevant to any use of AI-detection as an integrity signal that could
affect real people (educational, professional, or publishing contexts) —
a fairness/safety-relevant finding for whatever product surface this
project eventually builds.

### Potential Project Impact

Scientific Specification (fairness must be an explicit evaluation
dimension, not merely accuracy), Certification, Security/Ethics boundary

### Reproducibility

Available (methodology described; TOEFL corpus subject to its own access
terms)

### Governance Note (2026-08-24, R08 literature pass)

Correction to "TOEFL corpus subject to its own access terms" above: the
paper's own methodology states its 91 human-written essays were
**scraped from a Chinese educational forum (toefl.zhan.com)**, not drawn
from the officially licensed ETS Corpus of Non-Native Written English
(LDC2014T06, R-0103). No ethics/IRB approval or consent statement was
found in the paper for this scraped collection. This is a documented
governance gap in the field's own most-cited detector-bias study, not a
challenge to its findings — flagged because this project's own dataset
provenance requirements (R08 §4, §22) would not accept an equivalent
collection without documenting its ethics basis. See R08 §69.7.

### Status

REVIEWED — core finding and specific figures confirmed directly against
primary source (2026-08-24)

---

## R-0023 — Identifying Bias in Machine-Generated Text Detection

### Citation

Stowe, Afanaseva, Raimundo, Sun, Patil (Pindrop), ACL 2026.

### Source

arXiv:2512.09292

### Category

AI-DETECTION

### Claims Relevant to Project

Built a ~41,700-essay dataset and tested 16 commercial/research detectors
for bias across gender, race/ethnicity, English-language-learner (ELL)
status, and socioeconomic status. Found only 12 of 64 attribute×model
combinations showed statistically significant and meaningfully sized
effects; ELL essays were more likely flagged by most models; non-White
ELL essays were disproportionately flagged relative to White ELL essays
(7 of 16 models vs. 1 of 16); economically disadvantaged students were not
more likely to be falsely flagged; human annotators scored near chance
(45-53%) with no significant demographic bias; higher-performing
detectors generally showed lower bias.

### Limitations

Single research team's dataset and detector selection; company-affiliated
(Pindrop) but methodology and findings are more nuanced/self-critical than
typical vendor marketing (mixed evidence of bias, not a blanket claim).

### Relevance

A more recent, more granular companion finding to R-0022 — separates
ELL-status bias from race/ethnicity bias, and shows bias is correlated
with but distinct from raw accuracy. Directly relevant to fairness
requirements alongside R-0022.

### Potential Project Impact

Scientific Specification (fairness dimension), Certification

### Reproducibility

Partial (dataset construction described; some tested detectors are
closed/commercial)

### Status

REVIEWED

---

## R-0024 — Paraphrasing Evades Detectors of AI-Generated Text, But Retrieval Is an Effective Defense

### Citation

Krishna, Song, Karpinska, Wieting, Iyyer, NeurIPS 2023.

### Source

arXiv:2303.13408

### Category

ADVERSARIAL-ROBUSTNESS

### Claims Relevant to Project

Built DIPPER, an 11B-parameter paraphrase model, and showed it evades
watermarking, GPTZero, DetectGPT, and OpenAI's classifier applied to
GPT3.5-davinci-003 outputs. Confirmed specific figure: DIPPER paraphrasing
drops DetectGPT's detection accuracy from 70.3% to 4.6% at a fixed 1%
false-positive rate. Proposes a retrieval-based defense (matching against
a ~15-million-generation database) recovering 80-97% detection of
paraphrased text at ~1% false-positive rate on human text — but this
defense requires the generating service to log/retain its own outputs.

### Relevance

The single most concrete, best-documented robustness failure found in this
research pass; the specific 70.3%→4.6% figure is confirmed from the
paper itself (not secondary-sourced). Directly relevant to
SPECIFICATION-MAP.md §23 (Robustness) and to R06 (paraphrasing as a
transformation condition).

### Update (2026-08-24, R06 literature pass)

Re-fetched for R06's semantic-preservation-metric question: DIPPER's own
semantic-similarity metric is **P-SP** (Wieting et al. 2022 paraphrastic
sentence embeddings), with a threshold of **0.76** (the average P-SP
score of real human paraphrase pairs) used as the bar for "meaning
preserved"; 88-99% of DIPPER outputs exceed this threshold across the
paper's diversity settings, falling to 88.4-94.6% at maximum diversity.
Also confirmed: watermark (Kirchenbauer et al./R-0001) detection accuracy
drops from 100% to 57.2% on GPT2-XL open-ended generations under DIPPER
paraphrasing — a separate, watermark-specific figure from the
DetectGPT 70.3%→4.6% figure already registered above. See R06 §58.2.

### Potential Project Impact

Scientific Specification §23, Research (R06), Architecture (retrieval
defense has a strong operational/data-retention assumption relevant to
06-security and 07-data)

### Reproducibility

Available (open source, DIPPER model and code)

### Status

REVIEWED

---

## R-0025 — Can AI-Generated Text Be Reliably Detected?

### Citation

Sadasivan, Kumar, Balasubramanian, Wang, Feizi, arXiv:2303.11156.

### Source

arXiv:2303.11156

### Category

AI-DETECTION

### Claims Relevant to Project

Establishes a theoretical bound relating the best-possible detector's
AUROC to the total-variation distance between human-text and AI-text
distributions, implying no detector can maintain high accuracy as LLM
output converges toward human writing. Demonstrates a recursive
paraphrasing attack reducing detection with only marginal quality loss.
Separately shows watermark signatures can potentially be inferred/spoofed
without white-box model access.

### Limitations

This is a theoretical/adversarial position paper, not an empirical
detector evaluation; its conclusions are contested — see R-0026 for the
counter-position. The project should represent both positions rather than
treating either as settled.

### Relevance

Directly relevant to SPECIFICATION-MAP.md §27 ("No Universal Success
Claim") — provides theoretical grounding for why the project already
requires effectiveness to be evaluated against versioned profiles rather
than claimed universally.

### Potential Project Impact

Scientific Specification §27-29, Research (frame the R04 "detectability
limit" open question explicitly)

### Reproducibility

Partial (theoretical bound is derivable; recursive-attack demonstration
has associated code)

### Status

REVIEWED

---

## R-0026 — Position: On the Possibilities of AI-Generated Text Detection

### Citation

Chakraborty, Bedi, Zhu, An, Manocha, Huang, ICML 2024.

### Source

arXiv:2304.04736

### Category

AI-DETECTION

### Claims Relevant to Project

Argues, counter to R-0025, that with enough independent text samples,
reliable detection remains possible even as LLMs approach human-level
fluency.

### Limitations

Like R-0025, largely theoretical; the empirical detectors evaluated in
R-0012/R-0027 suggest the practical gap between "theoretically possible"
and "reliable in deployment" is currently large.

### Relevance

Necessary counterweight to R-0025 — this is a live, unsettled scientific
debate and the project's documentation must not silently pick a side
(per DOCUMENT-AUTHORITY-MATRIX.md "Never resolve an authority conflict by
assumption" and NO-INVENTION-RULES "Ambiguous Information").

### Potential Project Impact

Scientific Specification §27, Open Questions (frame explicitly as
contested, not resolved)

### Reproducibility

N/A (theoretical position paper)

### Status

REVIEWED

---

## R-0027 — A Practical Examination of AI-Generated Text Detectors for Large Language Models

### Citation

Tufts, Zhao, Li, arXiv:2412.05139.

### Source

arXiv:2412.05139

### Category

AI-DETECTION

### Languages

English, Spanish, French, Chinese

### Claims Relevant to Project

Independent test of RADAR, "Detection in the Wild," T5Sentinel (trained
detectors) and Fast-DetectGPT, GPTID, LogRank, Binoculars (zero-shot)
across 7 tasks (QA, summarization, dialogue, code, abstract writing,
reviews, translation) against Llama-3-Instruct, Mistral, Phi-3, GPT-4o.
Key finding: true-positive rate at a fixed 1% false-positive rate
(TPR@0.01) can be as low as 0% for some detector/task/model combinations,
i.e., high headline AUROC can mask near-total failure at the
low-false-positive operating points that matter for real deployment
decisions.

### Relevance

The most important independent corrective found to headline
AUROC-style claims from R-0004, R-0005, R-0009, R-0010 — directly
supports the project's own rule (SPECIFICATION-MAP.md §25 Acceptance
Criteria) that a transformation/detection result must not be accepted
solely because it satisfies one measurement.

### Update (2026-08-24, R07 literature pass)

Confirmed this paper's abstract explicitly argues TPR@FPR (specifically
TPR@1%FPR) is the field-relevant metric, not accuracy/AUROC, precisely
because accuracy/AUROC can mask near-total failure at low-FPR operating
points — an explicit methodological argument, not just a reporting
convention. This practice is independently corroborated by other
zero-shot detector papers already registered (R-0005/Binoculars). See
R07 §80.1.

### Potential Project Impact

Scientific Specification §17-18, §25, Validation (operating-point
selection, not just headline metric)

### Reproducibility

Available (methodology described)

### Status

REVIEWED

---

## R-0028 — Base Models Look Human To AI Detectors

### Citation

Xu, Zhong, Raghunathan, Fang, Kolter, arXiv:2605.19516 (2026).

### Source

arXiv:2605.19516

### Category

AI-DETECTION

### Claims Relevant to Project

Shows commercial detectors (GPTZero, Pangram) judge base (non-instruction-
tuned) LLM outputs as overwhelmingly human while flagging text from the
same underlying model family after instruction-tuning; also shows detector
sensitivity to whether preceding context was human- or AI-written. Implies
detectors track statistical fingerprints of the post-training procedure,
not an invariant "AI-ness" property.

### Relevance

The best mechanistic (not merely anecdotal) evidence found for why
detector effectiveness should be expected to drift as model training
recipes evolve — directly grounds KB-001 (effectiveness must be
versioned) with a causal mechanism rather than just a general concern.

### Potential Project Impact

Scientific Specification §29 (Evolution of Effectiveness), Research
(explains R04 §15/§16 Detector Drift / Model Drift)

### Reproducibility

Partial (methodology described; commercial detectors tested are
closed-box)

### Status

REVIEWED

---

## R-0029 — AI-Generated Text Detection in Low-Resource Languages: A Case Study on Urdu

### Citation

Ammar, Hadi, Butt, arXiv:2510.16573 (2025).

### Source

arXiv:2510.16573

### Category

MULTILINGUAL

### Languages

Urdu

### Claims Relevant to Project

Built a balanced 1,800/1,800 human/AI Urdu dataset (AI text from Gemini,
GPT-4o-mini, Kimi AI); best model (mDeBERTa-v3-base, a multilingual
encoder) achieved F1 91.29 / accuracy 91.26% on this specific dataset.

### Limitations

Small, single-dataset, single-study result — an existence proof that
Urdu detection research exists and one encoder performs well on this
specific constructed dataset, not evidence of general robustness on
naturalistic or adversarial Urdu text. Urdu is not currently one of the
project's 13 target languages (SPECIFICATION-MAP.md §20) — registered for
completeness and possible future language-expansion reference.

### Relevance

Illustrates both that low-resource-language detection research exists and
how thin it is (single small studies rather than mature benchmarks).

### Potential Project Impact

Research (R05), informs realistic expectations for target languages with
similarly limited literature (e.g., Indonesian, Polish, Turkish)

### Reproducibility

Available (dataset/methodology described)

### Status

PARTIALLY_RELEVANT — language not currently in project scope

---

## R-0030 — Turnitin Self-Disclosed False-Positive Rates

### Citation

Turnitin, "Understanding the false positive rate for sentences of our AI
writing detection capability" (blog).

### Source

https://www.turnitin.com/blog/understanding-the-false-positive-rate-for-sentences-of-our-ai-writing-detection-capability

### Category

AI-DETECTION

### Claims Relevant to Project

Vendor self-reports a document-level false-positive rate of "less than 1%"
for documents with ≥20% AI-written content, but a sentence-level
false-positive rate of "around 4%," with 54% of sentence-level false
positives occurring adjacent to actual AI-written sentences (boundary
confusion in mixed human/AI documents).

### Limitations

Vendor-published, not independently audited; but notably self-critical
(discloses a limitation rather than only marketing accuracy), which this
research pass judged as somewhat more credible than typical vendor
accuracy claims — still flagged as vendor-sourced.

### Relevance

The mixed human/AI document / sentence-boundary failure mode is directly
relevant to the project's own "Hybrid Text" research question (R04 §7)
and to any per-span (rather than per-document) evaluation the project's
S04 fidelity requirements might require.

### Potential Project Impact

Research (R04 §7 Hybrid Text), Scientific Specification (segment-level
evaluation, cf. S04 FID-084)

### Reproducibility

Unknown (vendor-internal methodology, not published in full)

### Status

PARTIALLY_RELEVANT — vendor-sourced, self-disclosed limitation

---

## R-0031 — Originality.ai: Does AI Translation Impact AI Detection? (Vendor Study)

### Citation

Originality.ai, "Does AI Translation Impact AI Detection?" (vendor blog
study).

### Source

https://originality.ai/blog/ai-translation-impact-ai-detection-study

### Category

AI-DETECTION

### Languages

English, Spanish, Portuguese

### Claims Relevant to Project

498 human + 498 GPT-4o-generated English samples translated to
Spanish/Portuguese (Google Translate), tested direct and round-trip
translation. Reported: false-positive rate on genuinely human text rose
from 0.40% (original English) to 28.02% (round-tripped via Spanish) /
27.84% (round-tripped via Portuguese); direct one-way translation caused a
smaller rise (2.21% Spanish, 0.40% Portuguese); GPT-4o content was
detected at "100%" across all translation conditions in their test.

### Limitations

Single vendor, self-reported, only 2 target languages, only Google
Translate as the translation engine, only their own detector evaluated.
Should be presented as one directionally suggestive study, not a general
law about translation and detection.

### Relevance

The most concrete (if narrow) evidence found on translation as a
false-positive source for human text — relevant to the project's
"Translation" research question (R04 §8) and to the 13-language
multilingual requirement, where translated text may be common input.

### Potential Project Impact

Research (R04 §8, R05), Scientific Specification (translation as a
robustness condition, SPECIFICATION-MAP.md §23)

### Reproducibility

Partial (methodology described; vendor detector is closed-box)

### Status

PARTIALLY_RELEVANT — vendor-sourced, narrow scope

---

## R-0032 — Provable Robust Watermarking for AI-Generated Text (Unigram Watermark)

### Citation

Zhao, Ananth, Li, Wang, ICLR 2024.

### Source

arXiv:2306.17439

### Category

WATERMARKING

### Claims Relevant to Project

Extends the green/red-list idea by fixing the same list partition across
every token position instead of re-hashing a rolling window of prior
tokens; comes with formal (provable) guarantees on generation quality and
detection correctness.

### Methodology

Requires generation-time cooperation (modifies sampling), same as
Kirchenbauer's approach (R-0001).

### Relevance

A second concrete watermark family beyond R-0001/R-0013; the
context-independence is offered as a robustness advantage against editing
and paraphrasing — relevant to comparing families in R02 §mechanism
taxonomy.

### Potential Project Impact

Research (R02 taxonomy)

### Reproducibility

Available (open source)

### Status

REVIEWED

---

## R-0033 — A Semantic Invariant Robust Watermark for Large Language Models (SIR)

### Citation

Liu et al., ICLR 2024; related: Wu et al., "A Robust Semantics-based
Watermark for Large Language Model against Paraphrasing," NAACL Findings
2024.

### Source

arXiv:2310.06356 ; aclanthology.org/2024.findings-naacl.40

### Category

WATERMARKING

### Claims Relevant to Project

Anchors the watermark signal to a semantic embedding of preceding tokens
(via an auxiliary embedding model) rather than surface token hashes, aimed
specifically at surviving synonym substitution and paraphrasing.

### Methodology

Requires generation-time cooperation plus an auxiliary trained watermark
model and embedding model.

### Relevance

Directly targets the paraphrase-evasion weakness documented for
context-hash watermarks (see R-0039); a concrete example of the
security/robustness design trade-off SPECIFICATION-MAP.md §16 asks the
project to track per-mechanism rather than assume uniformly.

### Potential Project Impact

Research (R02), Scientific Specification §16

### Reproducibility

Available (open source, per paper)

### Status

REVIEWED

---

## R-0034 — Undetectable Watermarks for Language Models

### Citation

Christ, Gunn, Zamir, COLT 2024 / IACR ePrint 2023/763.

### Source

arXiv:2306.09194 ; eprint.iacr.org/2023/763

### Category

WATERMARKING

### Claims Relevant to Project

A cryptographic construction (from one-way functions) framing
"undetectability" as computational indistinguishability: without the
secret key, distinguishing watermarked from non-watermarked output is
computationally intractable even under adaptive querying, with no
detectable change to the output distribution.

### Limitations

A security-theoretic/cryptographic framing rather than an empirical
statistical one; the generation-time cooperation requirement for the
underlying sampler was not fully specified in the material reviewed.

### Relevance

The strongest theoretical undetectability guarantee found among reviewed
mechanisms; relevant to the project's distinction between
"experimentally observed signals" and "theoretical" properties
(SPECIFICATION-MAP.md §16).

### Potential Project Impact

Research (R02), Scientific Specification §16

### Reproducibility

Partial (theoretical construction; not evaluated as an empirical system in
the material reviewed)

### Status

REVIEWED

---

## R-0035 — Publicly-Detectable Watermarking for Language Models

### Citation

Fairoze, Garg, Jha, Mahloujifar, Mahmoody, Wang, arXiv:2310.18491; related:
"An Unforgeable Publicly Verifiable Watermark for Large Language Models,"
arXiv:2307.16230.

### Source

arXiv:2310.18491 ; arXiv:2307.16230

### Category

WATERMARKING

### Claims Relevant to Project

Embeds a publicly-verifiable cryptographic signature via rejection
sampling, with error-correction to survive low-entropy generation
stretches; detection requires no secret — anyone with a public key can
verify, unlike the private-key schemes above (R-0001, R-0032, R-0033).

### Relevance

A structurally distinct detection-authority model (public vs. private key)
directly relevant to the project's own question of who can/should be able
to verify a watermark — relevant to 06-security boundary design.

### Potential Project Impact

Research (R02/R03), Security (06-security — detection-authority model)

### Reproducibility

Partial (cryptographic construction described; not evaluated as a deployed
system)

### Status

REVIEWED

---

## R-0036 — PostMark: A Robust Blackbox Watermark for Large Language Models

### Citation

Chang, Krishna, Karpinska, Houmansadr, Wieting, Iyyer, EMNLP 2024.

### Source

arXiv:2406.14517

### Category

WATERMARKING

### Claims Relevant to Project

A post-hoc watermark applied after decoding is complete: an
input-dependent set of words (chosen via semantic-embedding similarity) is
inserted into already-generated text. Explicitly requires no access to
model logits or the sampling process — "can be implemented by a third
party."

### Limitations

Author-reported improved paraphrase-robustness over 8 baselines comes with
an explicit text-quality/robustness trade-off per the authors.

### Relevance

The only reviewed mechanism that does NOT require generation-time
cooperation from whoever runs the model — structurally different from
every other watermark family registered here, and relevant if the
project ever needs to watermark text from a model it does not control.

### Potential Project Impact

Research (R02), Architecture (watermarking module scope — cooperative vs.
non-cooperative)

### Reproducibility

Available (open source)

### Status

REVIEWED

---

## R-0037 — Three Bricks to Consolidate Watermarks for Large Language Models

### Citation

Fernandez, Chaffin, Tit, Chappelier, Furon, WIFS 2023.

### Source

arXiv:2308.00113

### Category

WATERMARKING

### Claims Relevant to Project

Provides statistical tests with guarantees valid at very low false-positive
rates (<10⁻⁶), and a multi-key/multi-message detection framework: for M
possible keys, the detector tests each independently and reports the
lowest p-value, corrected via global p ≈ 1-(1-p)^M; secret vectors for
each key are generated cheaply as circular shifts of one base vector.

### Relevance

The concrete statistical mechanism for "detect which of several watermarks
is present" (R04/R03's "cross-detector methodology" and "detector version
registry" outputs) — directly usable as a methodological reference for the
project's own validation framework.

### Potential Project Impact

Research (R03), Scientific Specification (S03-experimental-model.md,
statistical methodology)

### Reproducibility

Available (methodology fully described)

### Status

REVIEWED

---

## R-0038 — WaterSeeker: Efficient Detection of Watermarked Segments in Large Documents

### Citation

(Authors per arXiv listing), NAACL Findings 2025.

### Source

arXiv:2409.05112

### Category

WATERMARKING

### Claims Relevant to Project

Addresses detection when only part of a document is watermarked (mixed
human/AI text): a cheap anomaly-extraction pass flags suspicious regions,
then local full-text verification localizes the watermarked span
precisely.

### Relevance

Directly relevant to R04 §7 (Hybrid Text) and R03's need for detection
methods that don't assume whole-document watermarking — realistic for the
project's actual expected input (mixed content, not clean single-origin
text).

### Potential Project Impact

Research (R03), Scientific Specification (segment-level evaluation, cf.
S04 FID-084)

### Reproducibility

Available (methodology described)

### Status

REVIEWED

---

## R-0039 — Watermark Under Fire: A Robustness Evaluation of LLM Watermarking (WaterPark)

### Citation

(Authors per arXiv listing), EMNLP Findings 2025.

### Source

arXiv:2411.13425

### Category

ADVERSARIAL-ROBUSTNESS

### Claims Relevant to Project

Systematic evaluation of watermark schemes against linguistic variation,
lexical editing, text-mixing, paraphrasing (including machine
round-trip-translation), gradient-based edits, and LLM-based rewriting.
Found distortion-free/context-free schemes most resilient overall, some
schemes collapsed under text-mixing/paraphrasing, and — the strongest
single finding — **all evaluated watermarking schemes' detection rates
fell below 0.3 after a single ChatGPT-paraphrasing pass.**

### Limitations

Author-reported experimental results from one systematic study; schemes
and paraphrasers evolve, so this should be treated as a snapshot, not a
permanent property (per RESEARCH-MAP.md §26 Research Freshness).

### Relevance

The strongest documented evidence that LLM-based paraphrasing is close to
a universal removal attack against current watermarking schemes — a
critical input to any claim the project might consider making about
watermark-based detection reliability (SPECIFICATION-MAP.md §27 "No
Universal Success Claim").

### Potential Project Impact

Scientific Specification §16, §23, §27; Research (R02/R03)

### Reproducibility

Partial (methodology described; specific paraphraser versions matter)

### Status

REVIEWED

---

## R-0040 — No Free Lunch in LLM Watermarking: Trade-offs in Watermarking Design Choices

### Citation

(Authors per NeurIPS 2024 proceedings listing).

### Source

proceedings.neurips.cc/paper_files/paper/2024 (paper ID
fa86a9c7b9f341716ccb679d1aeb9afa)

### Category

ADVERSARIAL-ROBUSTNESS

### Claims Relevant to Project

Reports that more-robust watermarks make "piggyback spoofing" easier
(inserting toxic/incorrect content while keeping the watermark detectable,
>90% author-reported success with only slight perplexity increase); using
many watermark keys defends against stealing but 7+ keys reportedly drove
removal-attack success to 97%+; public detection APIs reportedly enable
oracle-style removal/spoofing using as few as ~3 queries per token.

### Limitations

**All figures in this entry are author-reported from a single paper, not
independently replicated — treat every specific percentage here as
UNVERIFIED pending corroboration.** The load-bearing, better-supported
claim is qualitative: these trade-offs appear structural (a design choice
that helps one failure mode tends to worsen another), not fixable by
simple parameter tuning.

### Relevance

Directly relevant to any future project decision about exposing a public
watermark-detection API (06-security) — the "oracle query" finding implies
such an API is itself an attack surface.

### Potential Project Impact

Security (06-security — public detection API risk), Scientific
Specification §16

### Reproducibility

Unknown (specific attack parameters not verified in this pass)

### Status

INCONCLUSIVE — qualitative trade-off claim credible, specific figures
unverified

---

## R-0041 — SoK: Are Watermarks in LLMs Ready for Deployment?

### Citation

(Authors per arXiv listing), 2025/2026.

### Source

arXiv:2506.05594

### Category

WATERMARKING

### Claims Relevant to Project

Systematization-of-knowledge paper concluding current watermarking methods
are "not ready for real-world deployments" due to utility/robustness
trade-offs. Reports (method-specific, author-reported) perplexity
increases of 9-2066% depending on technique, and MMLU accuracy drops of up
to 2.3% for some schemes; flags numeric fields (dates, quantities) as
especially vulnerable to unintended semantic drift from watermark-driven
token substitution. Also states OpenAI built but did not ship a
watermarking system, citing user-adoption and fairness concerns (see
R-0043).

### Limitations

Perplexity/accuracy figures are method-specific and author-reported —
useful as an order-of-magnitude signal, not as a general constant.

### Relevance

Directly relevant to S04-fidelity-requirements.md (numeric/factual
preservation, FID-008/FID-045) and to any decision to actually deploy
watermarking in this project's own architecture — the quality cost is
real and technique-dependent, not negligible by default.

### Potential Project Impact

Scientific Specification (S04 fidelity, transformation-quality trade-off),
Architecture, Decision Log (if the project ever decides to build/adopt a
watermark)

### Reproducibility

Partial (survey/synthesis paper; underlying primary studies vary in
reproducibility)

### Status

REVIEWED

---

## R-0042 — Anthropic Text Watermarking Deployment (August 2026)

### Citation

Anthropic, "How Claude's text watermarking works" (official announcement,
Aug 2026); Anthropic Help Center, "How Claude marks AI-generated content";
TechCrunch, "Anthropic says it will watermark text generated by its AI
models" (Aug 11, 2026).

### Source

anthropic.com/news/claude-text-watermark ;
support.claude.com/en/articles/16266773 ;
techcrunch.com/2026/08/11/anthropic-says-it-will-watermark-text-generated-by-its-ai-models/

### Publication Date

2026-08-11

### Category

WATERMARKING

### Claims Relevant to Project

Anthropic states it uses the SynthID-Text approach (R-0014) to bias
low-stakes word-choice randomness, checkable only with a detection key.
Deployment trigger: the EU AI Act's Transparency Code (effective 2026-08-02);
Anthropic signed the EU Code of Practice on Transparency of AI-Generated
Content in July 2026. Scope: new Claude models watermark globally at
launch across API/Claude.ai/Claude Code/Cowork/Claude Tag; older models
retrofitted over subsequent months. Stated limitations (from Anthropic's
own disclosure): extensive rewrites remove the watermark; light editing
typically preserves it; Claude-performed translations retain it; the
watermark is sparser on factual/precise content (numbers, code); detection
confidence is lower on short passages. Separately, non-text outputs (e.g.
images) get C2PA content-credential metadata, a different mechanism.

### Limitations

None beyond the fact itself — this is a primary-source vendor
announcement, current as of this project's own operating context (this
session runs inside a Claude-based product), so it is directly and
unusually self-relevant. Not independently audited by a third party at
time of this research pass.

### Relevance

The single most current, most concrete real-world watermarking deployment
found — and notably, Anthropic's own disclosed limitations (numeric
content, short passages, rewrite-removal) closely match this project's own
fidelity concerns (S04 FID-003 Factual Preservation, FID-082 Short-Text
Caution). Directly relevant if this project's software will ever need to
detect or account for Claude-originated watermarked text specifically.

### Potential Project Impact

Research (R02/R03), Scientific Specification (S04, cross-reference to
short-text and numeric-content caveats), Architecture (a concrete,
named, currently-deployed target for watermark-detection capability)

### Reproducibility

Unknown (production system; detection key not public)

### Status

REVIEWED

---

## R-0043 — OpenAI Built But Did Not Deploy Text Watermarking

### Citation

Wall Street Journal reporting (Seetharaman, Barnum), Aug 2024, as
aggregated via Techmeme and Thurrott; corroborated in R-0041 (SoK paper).

### Source

techmeme.com/240804/p4 ;
thurrott.com/a-i/306664/openai-built-text-watermarking-solution-to-detect-ai-generated-content-but-may-not-release-it

### Publication Date

2024-08-04

### Category

WATERMARKING

### Claims Relevant to Project

OpenAI built an internal text-watermarking system for ChatGPT but chose
not to ship it, reportedly citing concerns about ambiguous penalties for
users and survey feedback that ~1/3 of users would use the product less if
watermarking were deployed. A "99.9% reliability" figure for the internal
detector is press-reported, not independently verified.

### Limitations

Press-sourced (WSJ via secondary aggregators, primary WSJ article not
directly fetched); the "99.9%" figure is explicitly UNVERIFIED. No 2026
primary-source statement was found confirming or denying continued
non-deployment as of this research pass — "still undeployed" is the
best-supported current understanding, not a certainty.

### Relevance

A documented real-world case where a lab chose not to deploy an existing
detection-relevant technology for adoption/fairness reasons rather than
technical ones — relevant context for why the project should not assume
watermarking will become universal across generators (SPECIFICATION-MAP.md
§16 "future-watermark must not be assumed covered").

### Potential Project Impact

Research (R02), Scientific Specification §16 (do not assume universal
future watermark adoption)

### Reproducibility

N/A (historical/news event)

### Status

PARTIALLY_RELEVANT — core fact credible, specific reliability figure
unverified

---

## R-0044 — Is Multilingual LLM Watermarking Truly Multilingual? (STEAM)

### Citation

(Authors per arXiv listing), 2025.

### Source

arXiv:2510.18019

### Category

MULTILINGUAL

### Claims Relevant to Project

Evaluated across 133 candidate languages (high/medium/low-resource);
found existing multilingual watermarking methods fail to remain robust
under translation attacks in medium- and low-resource languages despite
prior claims of cross-lingual robustness. Root cause identified:
semantic-clustering watermark approaches break down when a language's
tokenizer under-represents full-word tokens (heavy subword fragmentation).
Proposes STEAM, a back-translation-search detection method with
author-reported improvements (+0.23 AUC, +37% TPR at 1% FPR — UNVERIFIED,
single-paper).

### Limitations

Proposed-method improvement figures are author-reported and not
independently replicated in this pass; core negative finding (existing
methods are not robustly multilingual) is the load-bearing claim.

### Relevance

The most direct, largest-scope evidence found that watermark robustness
claims do not transfer uniformly across languages — directly reinforces
KB-008 (multilingual AI-detection evidence gap) with a watermarking-specific
parallel finding, and is relevant to essentially all 13 of the project's
target languages to varying degrees depending on tokenizer
characteristics.

### Potential Project Impact

Research (R02/R05), Scientific Specification §20-22 (per-language
capability states), KB-008 cross-reference

### Reproducibility

Partial (methodology described; 133-language evaluation scope not
independently re-verified)

### Status

REVIEWED — core negative finding credible, proposed-fix figures unverified

---

## R-0045 — Watermarking Makes Language Models Radioactive

### Citation

Meta AI Research (authors per publication listing).

### Source

ai.meta.com/research/publications/watermarking-makes-language-models-radioactive/

### Category

WATERMARKING

### Claims Relevant to Project

A distinct question from per-text detection: whether a downstream model
was fine-tuned on watermarked synthetic data ("radioactive" contamination)
is detectable, reportedly with p<10⁻⁵ even when only ~5% of fine-tuning
text was watermarked — reportedly more reliable than membership-inference
baselines.

### Limitations

Author-reported figures, not independently replicated in this pass; this
is a training-data-provenance question, not per-text detection accuracy —
must not be conflated with the rest of R02/R03's per-text findings.

### Relevance

A provenance/data-lineage capability distinct from real-time text
detection; relevant to 07-data (dataset contamination/provenance) rather
than to the transformation/detection pipeline directly.

### Potential Project Impact

Data (07-data — training-data provenance/contamination), Research (R02,
noted as a distinct sub-question)

### Reproducibility

Unknown (Meta-internal experiments, not independently reproduced in this
pass)

### Status

PARTIALLY_RELEVANT — distinct question from per-text detection, registered
for completeness

---

## R-0046 — M4: Multi-generator, Multi-domain, and Multi-lingual Black-Box Machine-Generated Text Detection

### Citation

Wang, Mansurov, Ivanov, Su, Shelmanov, Tsvigun, Whitehouse, Mohammed
Afzal, Mahmoud, Puccetti, Sasaki, Arnold, Aji, Habash, Gurevych, Nakov;
EACL 2024 (Best Resource Paper).

### Source

arXiv:2305.14902

### Publication Date

2023 (EACL 2024 publication)

### Category

AI-DETECTION, MULTILINGUAL

### Languages

English, Chinese, Urdu, Bulgarian, Indonesian, plus other languages in
extended releases; exact per-language breakdown not extracted in this
pass.

### Claims Relevant to Project

Foundational multilingual, multi-generator, multi-domain machine-generated
text detection dataset/benchmark; underlies SemEval-2024 Task 8 (R-0047).
Directly contradicts the prior project finding (KB-008) that Indonesian
has no independently verified detection evidence — Indonesian is a
training-set language here.

### Methodology

Large-scale black-box detection dataset construction across multiple LLM
generators, domains, and languages; EACL "Best Resource Paper" award
indicates peer recognition of dataset quality.

### Limitations

Per-language numeric detection results not extracted in this pass —
benchmark-inclusion is confirmed, but this is not the same as a deep
per-language performance study.

### Relevance

Directly revises KB-008: benchmark-inclusion-level evidence exists for
Indonesian (and others) where the R04 pass found none.

### Potential Project Impact

Research (R05), Scientific Specification §20-22 (capability-state
defaults), Knowledge Backlog (KB-008 correction)

### Reproducibility

Available (dataset released)

### Status

RELEVANT

---

## R-0047 — M4GT-Bench: Evaluation Benchmark for Black-Box Machine-Generated Text Detection

### Citation

Wang et al., ACL 2024.

### Source

aclanthology.org/2024.acl-long.218

### Publication Date

2024

### Category

AI-DETECTION, MULTILINGUAL

### Claims Relevant to Project

Extended multilingual/multi-generator benchmark building on M4 (R-0046);
finding that detection needs same-domain/same-generator training data to
generalize well — a generalization-gap finding relevant to §26
(Distribution Shift) in R03/R04.

### Methodology

Benchmark extension and evaluation across detection methods.

### Limitations

No per-language F1 table retrieved in this pass.

### Relevance

Reinforces the general finding (also seen in R-0028/R-0049) that detector
generalization across domain/generator boundaries is unreliable — now
also documented for the multilingual case specifically.

### Potential Project Impact

Research (R04, R05), Scientific Specification (generalization
requirements)

### Reproducibility

Available (benchmark released)

### Status

RELEVANT

---

## R-0048 — SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection

### Citation

Wang et al., SemEval-2024 shared task; arXiv:2404.14183;
aclanthology.org/2024.semeval-1.279.

### Source

arXiv:2404.14183

### Publication Date

2024

### Category

AI-DETECTION, MULTILINGUAL

### Languages

Subtask A multilingual: English, Chinese, Urdu, Bulgarian, Indonesian
(train); Arabic, Russian, German (dev); Italian added as an unseen
"surprise" test language.

### Claims Relevant to Project

62-team shared task; top team (USTC-BUPT) achieved 95.99% overall
accuracy across the multilingual test set (2nd/3rd: 95.85%/95.00%).
Directly contradicts KB-008's claim of no evidence for German, Italian,
and Russian (in addition to Indonesian via R-0046): all three appear in
this peer-reviewed, multi-team shared task.

### Methodology

Shared task with 62 participating teams; blind test set including a
deliberately unseen "surprise" language (Italian) to test generalization.

### Limitations

No per-language accuracy breakdown was retrievable in this pass — only
aggregate scores and the training/dev/test language partition are
confirmed. The broad multi-team participation adds some corroboration
beyond a single-author claim, but this is still benchmark-inclusion-level
evidence, not a dedicated deep per-language study.

### Relevance

The single most important correction to KB-008 found in the R05 pass:
directly places German, Italian, and Russian in a real, peer-reviewed,
multi-team evaluation, contradicting the "no evidence found" prior
conclusion for those languages.

### Potential Project Impact

Research (R05), Scientific Specification §20-22, Knowledge Backlog
(KB-008 correction)

### Reproducibility

Available (shared task data released)

### Status

RELEVANT

---

## R-0049 — MULTITuDE: Large-Scale Multilingual Machine-Generated Text Detection Benchmark

### Citation

Macko, Moro, Uchendu, Lucas, Yamashita, Pikuliak, Srba, Le, Lee, Simko,
Bielikova; EMNLP 2023.

### Source

arXiv:2310.13606

### Publication Date

2023

### Category

AI-DETECTION, MULTILINGUAL

### Languages

11 languages: Arabic, Catalan, Czech, German, English, Spanish, Dutch,
Portuguese, Russian, Ukrainian, Chinese.

### Claims Relevant to Project

74,081 texts, 8 LLM generators. English-trained detectors drop from
0.9292 F1 (English) to 0.6903 F1 average on non-English (~26% relative
decline) — a quantified cross-lingual generalization gap. Russian-trained
detectors transferred well within Cyrillic script (Ukrainian 0.9387,
Russian 0.9522 F1); Spanish-trained transferred well to Romance languages
(Portuguese 0.8944, Catalan 0.8747 F1). Directly contradicts KB-008 for
German, Dutch, Portuguese, and Russian.

### Methodology

Large multilingual dataset construction and cross-lingual transfer
experiments across 11 languages and 8 generators, EMNLP peer-reviewed.

### Limitations

A specific figure (LLaMA-65B language-modeling accuracy ~85% for
Arabic/Chinese vs ~95%+ for other languages) could only be partially
confirmed via an AI-summarized fetch, not a direct table read — treat
that specific number as UNVERIFIED pending direct verification; the F1
transfer figures above were extracted with higher confidence.

### Relevance

Best single source found for German, Dutch, Portuguese, and Russian
detection evidence; also documents a script/resource-clustering effect
(Cyrillic languages transfer well to each other) relevant to R05 §20
(Cross-Language Transfer).

### Update (2026-08-24, R08 literature pass)

License confirmed via Zenodo: **CC-BY-4.0** for both v1 (record 10013755,
2023-10-17) and v2 (record 13846588, **2024-09-27**). **This is a real,
dated benchmark-refresh example**: v2 explicitly extends v1 with texts
obfuscated via 10 authorship-obfuscation methods, shifting scope from
plain detection to adversarial-robustness evaluation — one of the few
confirmed instances of an AI-detection benchmark actually being
versioned and refreshed in practice, relevant to R08 §41-43 (Benchmark
Aging, Refresh, Versioning). Storage sizes stated on Zenodo: 44.7GB (v1),
29.8GB (v2) — AUTHOR-REPORTED and unusually large for text data; not
cross-checked against the paper's own document/token counts, flag before
citing as fact.

### Potential Project Impact

Research (R05), Scientific Specification §20-22, Knowledge Backlog
(KB-008 correction), Research (R08 §41-43 Benchmark Versioning)

### Reproducibility

Available (dataset released)

### Status

RELEVANT

---

## R-0050 — MultiSocial: Multilingual Benchmark of Machine-Generated Text Detection of Social-Media Texts

### Citation

Macko, Kopal, Moro, Srba.

### Source

arXiv:2406.12549

### Publication Date

2024

### Category

AI-DETECTION, MULTILINGUAL

### Languages

22 languages including Dutch, German, Polish, Portuguese, Russian,
Chinese, plus test-only Scottish Gaelic and Slovenian.

### Claims Relevant to Project

Fine-tuned detector AUC-ROC 0.78-1.00 (most ≥0.95); zero-shot
cross-lingual transfer shows a persistent English-vs-non-English gap;
Chinese and the two test-only unseen languages underperform (~0.90-0.95
AUC vs English ~0.99).

### Methodology

22-language social-media-domain MGT detection benchmark, fine-tuned and
zero-shot evaluation.

### Limitations

Preprint on an anonymized host; peer-review status not confirmed in this
pass.

### Relevance

Further corroborates KB-008 correction for Dutch, German, Polish,
Portuguese, Russian; social-media domain is a distinct genre from the
news/academic domains covered by other sources.

### Potential Project Impact

Research (R05), Knowledge Backlog (KB-008 correction)

### Reproducibility

Available (benchmark released)

### Status

PARTIALLY_RELEVANT — peer-review status unconfirmed

---

## R-0051 — CEAID: Benchmark of Multilingual Machine-Generated Text Detection Methods for Central European Languages

### Citation

Macko & Kopal.

### Source

arXiv:2509.26051

### Publication Date

2025

### Category

AI-DETECTION, MULTILINGUAL

### Languages

Central European languages (exact list not confirmed in this pass —
requires follow-up).

### Claims Relevant to Project

First Central-European-focused MGT detection benchmark; qualitative
finding that supervised fine-tuned detectors are most performant and most
resistant to obfuscation among methods tested.

### Methodology

Benchmark construction and detector evaluation for Central European
languages.

### Limitations

Exact language list and numeric results could not be extracted from the
fetch performed in this pass — flagged for follow-up direct PDF read
before citing specific figures.

### Relevance

Likely relevant to Polish and possibly other project target languages,
but cannot be cited with specifics yet.

### Potential Project Impact

Research (R05) — pending follow-up verification

### Reproducibility

Unknown (not confirmed in this pass)

### Status

UNREVIEWED — requires follow-up direct read

---

## R-0052 — Detecting Machine-Generated Text in Polish Using Fine-Tuned Qwen Models (PolEval 2025)

### Citation

Pierzyński; PolEval 2025 Workshop, Warsaw.

### Source

PolEval 2025 workshop proceedings (exact URL not captured in this pass).

### Publication Date

2025-11 (approximate)

### Category

AI-DETECTION, MULTILINGUAL

### Languages

Polish

### Claims Relevant to Project

Described by the author as the inaugural shared task for machine-generated
text detection in Polish; 7 competing systems; releases the "Śmigiel"
dataset publicly. Best constrained-setting systems reported >90% accuracy
on the main evaluation set, with marked degradation on unseen
domains/generators (exact drop not retrieved); unsupervised methods
outperformed supervised ones in the hardest generalization scenario.
Directly contradicts KB-008's finding of no evidence for Polish.

### Methodology

Dedicated shared task with a newly released Polish dataset ("Śmigiel").

### Limitations

Exact generalization-drop numbers not retrieved in this pass; single
workshop, not yet independently corroborated by a second study.

### Relevance

First dedicated Polish-language resource found; directly closes part of
the KB-008 gap for Polish detection (watermarking for Polish remains
unevidenced).

### Potential Project Impact

Research (R05), Knowledge Backlog (KB-008 correction)

### Reproducibility

Available (dataset released)

### Status

RELEVANT

---

## R-0053 — Findings of the RuATD Shared Task 2022 on Artificial Text Detection in Russian

### Citation

Shamardina, Mikhailov, Chernianskii, Fenogenova, Saidov, Valeeva,
Shavrina, Smurov, Tutubalina, Artemova; Dialogue-22.

### Source

arXiv:2206.01583

### Publication Date

2022

### Category

AI-DETECTION, MULTILINGUAL

### Languages

Russian

### Claims Relevant to Project

Dedicated Russian AI-text detection shared task; 14 generators, 30
binary-task and 8 multiclass-task systems submitted; qualitatively "most
teams outperform the baselines by a wide margin."

### Methodology

Shared task with multiple generator models and a large number of
submitted detection systems.

### Limitations

Specific accuracy/F1 numbers not extracted from the abstract-level fetch
performed in this pass — follow-up direct PDF read recommended before
citing figures.

### Relevance

Further corroborates Russian evidence alongside R-0048/R-0049.

### Potential Project Impact

Research (R05)

### Reproducibility

Available (shared task data)

### Status

UNREVIEWED — requires follow-up direct read for specific figures

---

## R-0054 — C-ReD: A Comprehensive Chinese Benchmark for AI-Generated Text Detection

### Citation

Qing, Wu, Liu, Qiu, Yu, Chen, Wu, Xia.

### Source

arXiv:2604.11796

### Publication Date

2025/2026

### Category

AI-DETECTION, MULTILINGUAL

### Languages

Chinese

### Claims Relevant to Project

Dedicated Chinese MGT detection benchmark; 9 zero-shot + 5 supervised + 8
LLM-as-detector methods across 5 domains. Best zero-shot method (LAPD):
0.9726 AUROC (Q&A), 0.9528 (Composition), but only 0.74 (News) / 0.73
(Academic Writing) — a domain effect within Chinese. Fine-tuned
RoBERTa-large reached 0.99+ AUROC after in-domain training. Qualitative
claim that Chinese's idiom density and word-segmentation ambiguity
complicate detection (unquantified).

### Methodology

Multi-domain, multi-method Chinese detection benchmark.

### Limitations

Preprint, no confirmed peer review; gives no direct head-to-head English
comparison number; in-domain fine-tuned results are expected to be high
and not evidence of general cross-lingual difficulty.

### Relevance

Directly closes part of the logographic-script gap flagged in the R02/R04
passes (KB-008); the domain-effect finding (News/Academic much harder
than Q&A/Composition) is relevant to R04 §23 (Domain Evaluation).

### Potential Project Impact

Research (R05), Knowledge Backlog (KB-008 correction)

### Reproducibility

Partial (benchmark described, release status not confirmed)

### Status

PARTIALLY_RELEVANT — preprint, not independently verified

---

## R-0055 — Overview of AuTexTification at IberLEF 2023

### Citation

Sarvazyan, González, Franco-Salvador, Rangel, Chulvi, Rosso.

### Source

arXiv:2309.11285

### Publication Date

2023

### Category

AI-DETECTION, MULTILINGUAL

### Languages

English, Spanish

### Claims Relevant to Project

Dedicated English+Spanish MGT detection/attribution shared task; 160,000+
texts, 5 domains, 114 registered teams, 36 submitting 175 runs.

### Methodology

Shared task overview paper.

### Limitations

Task-level aggregate/best per-language F1 numbers not extracted from this
pass's fetch — see R-0056 for one participant system's own reported
numbers (not the task's overall best).

### Relevance

Strongest dedicated Spanish resource found in this pass at the
shared-task level.

### Potential Project Impact

Research (R05), Knowledge Backlog (KB-008 correction — Spanish already had
some evidence, this deepens it)

### Reproducibility

Available (shared task data)

### Status

UNREVIEWED — requires follow-up direct read for specific figures

---

## R-0056 — AI-generated Text Detection with a GLTR-based Approach (AuTexTification participant system)

### Citation

Yan Wu & Segura-Bedmar, Universidad Carlos III de Madrid.

### Source

arXiv:2502.12064

### Publication Date

2023 (IberLEF-AuTexTification participant paper)

### Category

AI-DETECTION, MULTILINGUAL

### Languages

English, Spanish

### Claims Relevant to Project

Single participating system in AuTexTification (R-0055) reported Macro-F1
80.19% for English vs 66.20% for Spanish using the same GLTR-based
(R-0002) method — a concrete, quantified English-vs-Spanish detection
gap using one consistent method.

### Methodology

Application of a GLTR-style statistical method to both languages within
the same shared-task submission.

### Limitations

Single participating system's result, not the shared task's overall best
or a systematic study — the specific 80.19%/66.20% gap is
AUTHOR-REPORTED and illustrative, not necessarily representative of the
best achievable gap.

### Relevance

A concrete, method-controlled English-vs-Spanish performance gap, useful
as an illustrative (not definitive) data point.

### Potential Project Impact

Research (R05)

### Reproducibility

Partial (method described, not confirmed independently reproduced)

### Status

PARTIALLY_RELEVANT — single-system, illustrative only

---

## R-0057 — Distinguishing ChatGPT(-3.5,-4)-generated and Human-Written Papers Through Japanese Stylometric Analysis

### Citation

Zaitsu & Jin, PLOS ONE.

### Source

PLOS ONE, August 2023 (peer-reviewed journal).

### Publication Date

2023-08

### Category

AI-DETECTION, MULTILINGUAL

### Languages

Japanese

### Claims Relevant to Project

216 texts (72 human academic-psychology papers, 72 GPT-3.5, 72 GPT-4),
stylometric features (POS bigrams, particle bigrams, comma position,
function-word rates), Random Forest classifier, leave-one-out accuracy
100% on combined features (98.1% on function words alone). GPT-4 did not
close the gap to human stylometric patterns versus GPT-3.5 despite being
a larger/newer model.

### Methodology

Stylometric feature extraction and classification, peer-reviewed journal
methodology, transparent feature set.

### Limitations

Small sample (216 texts), single domain (academic psychology papers) —
generalization beyond that domain untested.

### Relevance

Strongest single-language non-English detection result found in the R05
pass; directly closes part of the KB-008 gap for Japanese; the
GPT-4-does-not-close-the-gap finding is relevant to R04 (temporal/model
evaluation).

### Potential Project Impact

Research (R05), Knowledge Backlog (KB-008 correction)

### Reproducibility

Partial (methodology described; corpus availability not confirmed)

### Status

RELEVANT — peer-reviewed, methodologically transparent

---

## R-0058 — Detection of Texts Generated by LLMs in Portuguese (PT-Detect)

### Citation

Paes, Negrao, Silva, Junior, Luz, Silva; SBC ENIAC conference.

### Source

SBC ENIAC conference proceedings (exact URL not captured in this pass).

### Publication Date

2024/2025 (approximate)

### Category

AI-DETECTION, MULTILINGUAL

### Languages

Portuguese

### Claims Relevant to Project

Dataset from Folha de São Paulo news (3,024 examples: human / AI-generated
/ AI-rewritten); tested LSTM, BERTimbau, BERTugues, mBERT, LLaMA-3.1-8B/
3.2-3B. Binary classification up to 98.18%, three-way (human/AI/
AI-rewritten) 97.7% accuracy; Portuguese-specialized models outperformed
multilingual ones; human texts averaged 30% longer than AI text.

### Methodology

Dedicated Portuguese-language dataset construction and multi-model
detection evaluation.

### Limitations

Single-domain (Brazilian news, one outlet); the "30% longer" finding is a
surface/length feature, not a deep linguistic one, and may not generalize
to other domains or be robust to length-normalization attacks.

### Relevance

Closes part of the KB-008 gap for Portuguese at the dedicated-study level
(beyond the benchmark-inclusion level already provided by R-0049).

### Potential Project Impact

Research (R05), Knowledge Backlog (KB-008 correction)

### Reproducibility

Partial (methodology described, dataset availability not confirmed)

### Status

PARTIALLY_RELEVANT — single domain/outlet

---

## R-0059 — AI "News" Content Farms Are Easy to Make and Hard to Detect: A Case Study in Italian

### Citation

Puccetti, Rogers, Alzetta, Dell'Orletta, Esuli.

### Source

arXiv:2406.12128

### Publication Date

2024-06

### Category

AI-DETECTION, MULTILINGUAL

### Languages

Italian

### Claims Relevant to Project

Fine-tuned LLaMA on 40K Italian news articles; human raters only 64%
accurate at spotting synthetic Italian news (vs 50% chance), Fleiss
κ=20.56% (low inter-rater agreement); DetectGPT (R-0003) reached ~80%
accuracy against the fine-tuned model; supervised classifiers needed
4K-8K labeled examples for 81-92% accuracy but collapsed below 56% with
only 2K samples. Authors' own conclusion: no practical method currently
exists for detecting synthetic news-like text "in the wild" for
closed-API models with unknown base LLM.

### Methodology

Fine-tuned-model construction, human-rater study, and classifier
evaluation with varying training-set sizes.

### Limitations

Single base model family (Llama), single domain (news).

### Relevance

An explicit, methodologically careful negative finding — directly
relevant to the project's own principle (RESEARCH-MAP.md §23, Negative
Results) that negative results are first-class research outputs. Closes
part of the KB-008 gap for Italian while simultaneously showing Italian
detection is currently unreliable in realistic conditions, not merely
"under-evidenced."

### Potential Project Impact

Research (R05), Scientific Specification (realistic capability-state
assignment for Italian should reflect this negative finding, not just the
existence of some evidence), Knowledge Backlog (KB-008 correction)

### Reproducibility

Partial (methodology described)

### Status

RELEVANT — explicit negative finding, methodologically careful

---

## R-0060 — From Perceptions to Evidence: Detecting AI-Generated Content in Turkish News Media with a Fine-Tuned BERT Classifier

### Citation

Ozdemir, University of Groningen.

### Source

arXiv:2602.13504

### Publication Date

2026-02

### Category

AI-DETECTION, MULTILINGUAL

### Languages

Turkish

### Claims Relevant to Project

First computational Turkish AI-detection study per the author's own
framing; F1 97.08%, accuracy 97.92% on held-out test set from 3,600
articles across 3 outlets.

### Methodology

Fine-tuned BERT classifier on a purpose-built Turkish news dataset.

### Limitations

Single-author preprint; narrow dataset (3,600 articles, 3 outlets); the
author explicitly flags the small/narrow dataset as a limitation.

### Relevance

Closes part of the KB-008 gap for Turkish at the dedicated-study level,
though the evidence base remains narrow (single study, single domain).

### Potential Project Impact

Research (R05), Knowledge Backlog (KB-008 correction)

### Reproducibility

Unknown (dataset availability not confirmed)

### Status

PARTIALLY_RELEVANT — single narrow study

---

## R-0061 — Cross-linguistic Evaluation of AI-Generated Text Detection: A Comparative Study on English and Indonesian

### Citation

Yatheendra & Arabagatte, ShodhKosh: Journal of Visual and Performing
Arts, Vol 6 No 1.

### Source

ShodhKosh journal (low-tier, non-mainstream NLP/CS venue).

### Publication Date

2025

### Category

AI-DETECTION, MULTILINGUAL

### Languages

English, Indonesian

### Claims Relevant to Project

Claims higher detection accuracy for English than Indonesian, attributed
to "linguistic complexities and dataset bias" — qualitative claim only.

### Methodology

Not confirmed in this pass — publication venue is not a mainstream
NLP/CS outlet.

### Limitations

Non-mainstream venue; specific precision/recall/F1 numbers could not be
extracted; treat the qualitative claim only, cautiously, and do not cite
any numeric figure from this source.

### Relevance

A weak, unreplicated signal for Indonesian, superseded in evidentiary
weight by R-0046/R-0048 (benchmark-inclusion) for the "is there any
evidence" question, but the venue quality means this should not be relied
upon for any specific claim.

### Potential Project Impact

Research (R05) — low weight

### Reproducibility

Unknown

### Status

INCONCLUSIVE — low-tier venue, numbers not verifiable

---

## R-0062 — Is Multilingual LLM Watermarking Truly Multilingual? Scaling Robustness to 100+ Languages via Back-Translation (STEAM)

### Citation

Mohamed & Gubri.

### Source

arXiv:2510.18019 (also OpenReview/HuggingFace)

### Publication Date

2025-10 (revised 2026-03)

### Category

WATERMARKING, MULTILINGUAL, ADVERSARIAL-ROBUSTNESS

### Languages

Self-reported testing across "133 candidate languages"; exact per-language
breakdown not confirmed in this pass.

### Claims Relevant to Project

States that existing multilingual watermarking methods fail to remain
robust under translation attacks in medium- and low-resource languages,
attributed to tokenizer vocabularies containing too few full-word tokens
for semantic-clustering watermark approaches to work (subword
fragmentation). Proposes STEAM, a Bayesian-optimization back-translation
defense, reporting +0.23 AUC and +37% TPR@1%FPR improvement.

### Methodology

Large-scale multilingual watermark robustness evaluation plus a proposed
defense mechanism.

### Limitations

Author-reported figures, not yet independently replicated; the causal
mechanism claim (tokenizer fragmentation specifically) is not yet
independently confirmed by a second research group using the same causal
framing, though the outcome (non-Latin/low-resource languages show weaker
watermark robustness) is corroborated by R-0049 and R-0069's separate,
independent findings.

### Relevance

Already registered in the R02 pass as R-0044 (same finding, referenced as
"STEAM" there) — this entry supersedes/consolidates with R-0044 to avoid
registry duplication; R-0044 should be treated as the authoritative entry
for this source going forward, cross-referenced here.

### Potential Project Impact

Research (R02, R05), Knowledge Backlog (KB-008, KB-010)

### Reproducibility

Partial (methodology described)

### Status

SUPERSEDED — duplicate of R-0044, see R-0044 for the authoritative entry

---

## R-0063 — LUNA: Linguistics-Aware Non-Distortionary LLM Watermarking

### Citation

Park et al., ACL 2026.

### Source

arXiv:2606.00613

### Publication Date

2026

### Category

WATERMARKING, MULTILINGUAL

### Languages

English, Chinese, Korean, Japanese, German, Arabic.

### Claims Relevant to Project

Explicitly models linguistic typology in watermark design across
analytic (English), isolating/no-spacing (Chinese), agglutinative
(Korean), agglutinative/mixed-script (Japanese), fusional/V2-syntax
(German), and templatic/abjad (Arabic) languages. Finds Korean and German
show the widest "next-tag entropy spread" (0.244 / 0.229), used as a
proxy for how much grammatical latitude a language offers a watermark to
exploit.

### Methodology

Watermark design informed by typological linguistics; entropy-spread
measurement across 6 languages.

### Limitations

To-appear at ACL 2026 at time of check (peer-review outcome not yet fully
confirmed); only 6 languages tested; same author group as R-0064 (STELA)
— should not be treated as independent corroboration of that companion
paper.

### Relevance

First watermark-design (as opposed to detection) study to operationalize
morphological typology directly; relevant to R02 §3 (Watermark Taxonomy)
and §15 (Language/Script Dependence, in R05).

### Potential Project Impact

Research (R02, R05)

### Reproducibility

Unknown (not confirmed in this pass)

### Status

PARTIALLY_RELEVANT — to-appear, narrow language set

---

## R-0064 — STELA: A Linguistics-Aware LLM Watermarking via Syntactic Predictability

### Citation

Park et al. (same author group as R-0063/LUNA).

### Source

arXiv:2510.13829

### Publication Date

2025

### Category

WATERMARKING, MULTILINGUAL

### Languages

English, Chinese, Korean.

### Claims Relevant to Project

Agglutinative Korean requires a larger POS n-gram context (k=4) than
English (k=2) to model "linguistic indeterminacy" for watermark
insertion; STELA reports best TPR@5%FPR/F1 for Chinese and Korean among
languages tested.

### Methodology

Watermark scheme parameterized by POS-context window size, tested across
3 languages.

### Limitations

Only 3 languages tested; same author group as R-0063 (LUNA) — treat as
one research program's converging findings, not two independent sources.

### Relevance

Corroborates (within the same research program) that morphological
typology materially affects watermark design parameters.

### Potential Project Impact

Research (R02, R05)

### Reproducibility

Unknown (not confirmed in this pass)

### Status

PARTIALLY_RELEVANT — narrow language set, same-group as R-0063

---

## R-0065 — Can Watermarks Survive Translation? On the Cross-lingual Consistency of Text Watermark for Large Language Models (CWRA / X-SIR)

### Citation

He, Zhou, Hao, Liu, Wang, Tu, Zhang, Wang; SJTU / Tencent AI Lab /
Tsinghua.

### Source

arXiv:2402.14007

### Publication Date

2024

### Category

WATERMARKING, ADVERSARIAL-ROBUSTNESS, MULTILINGUAL

### Languages

Chinese used as the primary pivot-language example; full language list
beyond that not confirmed in this pass.

### Claims Relevant to Project

Introduces the Cross-lingual Watermark Removal Attack (CWRA); watermark
detection AUC drops from 0.95 to 0.67 under CWRA against KGW
(R-0001)/Unigram (R-0032)-style watermarks; proposed X-SIR defense
recovers to 0.88 (still short of baseline). Origin of the "X-SIR" defense
referenced by later papers (R-0066).

### Methodology

Cross-lingual translation-based watermark removal attack, tested against
statistical watermark families, plus a proposed semantic-invariant
defense.

### Limitations

Exact full language list beyond the Chinese pivot example not confirmed
in this pass.

### Relevance

Identifies translation-based watermark evasion as a distinct attack class
from monolingual paraphrasing (already documented in R-0039/R02 §37.2) —
this is a materially new finding for R02/R03 that was not captured in the
prior research pass.

### Potential Project Impact

Research (R02 §6-7 Robustness/Attack Models, R03 §25 Editing Evaluation),
Security

### Reproducibility

Partial (methodology described)

### Status

RELEVANT — introduces a new attack class not previously registered

---

## R-0066 — Uncovering the Hidden Threat of Text Watermarking from Users with Cross-Lingual Knowledge

### Citation

Al Ghanim, Xue, Hastuti, Zheng, Solihin, Lou; University of Central
Florida.

### Source

arXiv:2502.16699

### Publication Date

2025

### Category

WATERMARKING, ADVERSARIAL-ROBUSTNESS, MULTILINGUAL

### Languages

English, Arabic, Chinese, Indonesian.

### Claims Relevant to Project

Tests 4 watermarking schemes (KGW/R-0001, Unigram/R-0032, EXP, XSIR)
across EN/AR/ZH/ID; distinguishes "symmetric" (pivot-language round-trip)
vs. "asymmetric" (translate-and-edit, modeling realistic non-adversarial
user behavior) attacks. KGW AUC fell as low as 0.55 for an Arabic→English
pair; Unigram as low as 0.57; XSIR showed pronounced vulnerability
specifically for Chinese and Arabic; translations into English survived
better than translations out of English; back-translation to the
original language partially restored watermark signal. Only source found
in this pass that explicitly includes Indonesian in a watermarking-
robustness experiment.

### Methodology

Controlled translation-attack evaluation (symmetric and asymmetric) across
4 watermark schemes and 4 languages.

### Limitations

Venue/peer-review status not confirmed from the fetch performed; only 4
languages tested.

### Relevance

Second independent source (alongside R-0065) documenting translation-based
watermark evasion as a distinct, materially significant attack class; the
directionality finding (into-English survives better than out-of-English)
is a novel, specific, and actionable finding for R02/R03.

### Potential Project Impact

Research (R02, R03, R05), Security

### Reproducibility

Partial (methodology described)

### Status

RELEVANT

---

## R-0067 — CLSA: Cross-Lingual Summarization as a Black-Box Watermark Removal Attack

### Citation

Ganesan (independent/NYU-affiliated single author).

### Source

arXiv:2510.24789

### Publication Date

2025-10

### Category

WATERMARKING, ADVERSARIAL-ROBUSTNESS, MULTILINGUAL

### Languages

Amharic, Chinese, Hindi, Spanish, Swahili.

### Claims Relevant to Project

Three-stage pipeline (translate to pivot language → abstractive summarize
via mT5/XSum, 15-25% length → optional back-translate) collapses
watermark AUROC near chance: XSIR on Amharic 0.982→0.493, on Chinese
0.971→0.539, on Spanish 0.979→0.510; KGW on Spanish 0.976→0.584; for XSIR
specifically, CLSA drops AUROC from a 0.827 paraphrasing-baseline to
~0.53 (near chance).

### Methodology

Combined translation + abstractive summarization + optional
back-translation attack pipeline, tested against multiple watermark
schemes.

### Limitations

Single-author, non-institutional preprint, not peer-reviewed — extra
caution warranted; these are among the most dramatic numbers in the R05
pass and are entirely unreplicated. Treat magnitude as AUTHOR-REPORTED /
unverified until independently reproduced or peer-reviewed.

### Relevance

If corroborated, this would be an even stronger evasion result than
paraphrasing alone (R-0039) — but given the single-author,
non-peer-reviewed status, it should not be treated as more reliable than
R-0039 without independent replication.

### Potential Project Impact

Research (R02, R03), Knowledge Backlog (candidate for a KB entry flagging
this as needing replication before being relied upon)

### Reproducibility

Unknown (not independently reproduced)

### Status

INCONCLUSIVE — dramatic unreplicated findings from a single non-peer-
reviewed preprint

---

## R-0068 — ESPERANTO: Evaluating Synthesized Phrases to Enhance Robustness in AI Detection

### Citation

Ayoobi, Knab, Cheng, Pantoja, Alikhani, Flamant, Kim, Mukherjee; ACM
Hypertext & Social Media 2025.

### Source

arXiv:2409.14285

### Publication Date

2024-09 (ACM HT 2025 publication)

### Category

AI-DETECTION, ADVERSARIAL-ROBUSTNESS, MULTILINGUAL

### Claims Relevant to Project

Round-trip machine translation through multiple pivot languages, then
back to English, combined into a manipulated hybrid text, tested against
9 detectors (6 open-source, 3 proprietary) — significantly reduces
detector true-positive rate (exact magnitude not retrieved in this pass).
Their proposed countermeasure only degrades by 1.85% TPR under the same
attack. Released a 720,000-text, 8-LLM dataset.

### Methodology

Multi-pivot round-trip translation attack against 9 AI-text detectors,
peer-reviewed at ACM HT 2025.

### Limitations

Exact TPR-reduction magnitude and specific pivot-language list not
retrieved in this pass — follow-up direct read recommended.

### Relevance

A second, peer-reviewed confirmation that translation-based manipulation
degrades AI-text (not just watermark) detection specifically — extends
the translation-evasion finding from watermarking (R-0065, R-0066) to
plain AI-detection.

### Potential Project Impact

Research (R04 §25 Editing Evaluation, R05), Security

### Reproducibility

Available (dataset released)

### Status

RELEVANT

---

## R-0069 — Robustness Assessment and Enhancement of Text Watermarking for Google's SynthID

### Citation

Han, Li, Ni, Zulkernine.

### Source

arXiv:2508.20228

### Publication Date

2025-08

### Category

WATERMARKING, ADVERSARIAL-ROBUSTNESS, MULTILINGUAL

### Languages

French, Italian, Chinese, Japanese.

### Claims Relevant to Project

Round-trip translation attack on Google's SynthID-Text (R-0014) across
FR/IT/ZH/JA; F1 drops to 0.711 for Chinese (worst) vs 0.819 for Japanese
(best), with French/Italian (Latin-script, Romance) staying comparatively
high. Proposes a "SynGuard" defense (+11.1% F1).

### Methodology

Round-trip translation attack against a specific, real, production-lineage
watermark scheme (SynthID-Text), across 4 languages.

### Limitations

No tokenizer-specific mechanism analysis; small language set (4); the
stated explanation for Japanese's comparatively strong performance
(round-trip translation "retains more original semantics") is about
translation quality, not directly about the tokenizer-fragmentation
mechanism claimed in R-0044/R-0062 — this creates an open tension (see
Relevance) rather than a clean corroboration.

### Relevance

Directly relevant since SynthID is the mechanism behind Anthropic's own
deployed watermarking (R-0042). Notably, Japanese performs *best* here
despite being treated as linguistically "hard" in R-0063/R-0064 (LUNA/
STELA) — this inconsistency between studies should be preserved as an
open tension per RESEARCH-MAP.md §22 (Contradictory Evidence), not
silently resolved.

### Potential Project Impact

Research (R02 §37.3 Real-World Deployment, R05), directly relevant given
this project's own tooling runs on Claude/SynthID-lineage watermarking

### Reproducibility

Partial (methodology described)

### Status

RELEVANT

---

## R-0070 — Can Professional Translators Identify Machine-Generated Text?

### Citation

Farrell.

### Source

arXiv:2601.15828

### Publication Date

2026-01

### Category

AI-DETECTION, MULTILINGUAL

### Languages

Italian (source text), English (translator pool's working language pair).

### Claims Relevant to Project

Only 16.2% of 69 professional translators correctly identified
AI-generated Italian text; participants were often misled by grammatical
accuracy/emotional tone and sometimes preferred the AI-generated text;
more reliable (if still weak) cues were low burstiness, narrative
contradiction, and unexpected calques/syntactic transfer from English.

### Methodology

Human-evaluation study with a professional-translator participant pool.

### Limitations

Small sample (69 participants), single language pair (Italian/English).

### Relevance

Adjacent to (not directly about) automated detector evasion, but directly
relevant to the project's human-in-the-loop evaluation methodology (R07)
and to R05 §29 (Human Evaluation) — suggests professional linguistic
expertise alone is an unreliable detection signal.

### Potential Project Impact

Research (R05, R07 — human evaluation methodology)

### Reproducibility

Partial (methodology described)

### Status

PARTIALLY_RELEVANT — small sample, single language pair

---

## R-0071 — Tokenization Standards for Linguistic Integrity: Turkish as a Benchmark

### Citation

Bayram, Fincan, Gümüş, Karakaş, Diri, Yıldırım.

### Source

arXiv:2502.07057

### Publication Date

2025-02

### Category

MULTILINGUAL, OTHER

### Languages

Turkish

### Claims Relevant to Project

Naive tokenizers fragment Turkish agglutinative words into morphologically
meaningless pieces (e.g., "evlerimizden" → ["e","vl","er","imizd","en"]);
introduces %TR (valid-Turkish-word token ratio) and %Pure metrics; %TR
correlates more strongly with downstream MMLU performance (r=0.90) than
generic token purity (r=0.68).

### Methodology

Tokenizer evaluation and new metric proposal for Turkish morphological
integrity.

### Limitations

Does not discuss watermarking or AI detection at all — a pure
tokenization/morphology background paper. Its relevance to this project
is indirect (mechanistic background for why Turkish tokenization could
matter to watermarking/detection), not a direct finding about either.

### Relevance

Background evidence supporting the general tokenizer-fragmentation
mechanism claimed in R-0044/R-0062, specifically for Turkish — but does
not itself test watermarking or detection, so should not be cited as
detection/watermarking evidence, only as tokenization background.

### Potential Project Impact

Research (R05) — background only

### Reproducibility

Available (methodology and metrics described)

### Status

PARTIALLY_RELEVANT — background/tokenization-only, not direct
detection/watermarking evidence

---

## R-0072 — Code-Mixing and Code-Switching for Text in the LLM Era: A Playbook of Models, Data, Evaluation, and Open Problems

### Citation

Gupta, Jayarao, Varshney, Dwivedi; ASU/CMU.

### Source

arXiv:2602.11181

### Publication Date

2026-05

### Category

MULTILINGUAL, OTHER

### Claims Relevant to Project

Comprehensive, recent survey of code-mixing/code-switching in the LLM
era; explicitly does not cover AI-generated-text detection or
watermarking for code-switched/mixed-language text at all — its scope is
generation, prompting, training, evaluation, and safety/red-teaming
(code-switching as a jailbreak vector, not as a detection/watermarking
target).

### Methodology

Survey/playbook of existing literature.

### Limitations

Survey scope, not primary data; the absence-of-coverage finding is
inferred from the survey's stated scope, not from an exhaustive
independent search of the entire field.

### Relevance

Read as reasonably strong secondary confirmation that, as of a
comprehensive May-2026 survey, code-switching detection/watermarking
remains a genuine open gap in the field — not merely something this
project's own searches failed to find.

### Potential Project Impact

Research (R05 §40-41 Mixed-Language Text/Code-Switching), Knowledge
Backlog (candidate gap entry)

### Reproducibility

Not applicable (survey)

### Status

RELEVANT — confirms a research gap, not a finding

---

## R-0073 — Predicting the Authenticity of Code-Switched Text Generated by A Large Language Model

### Citation

Unknown (title only; DTIC-indexed technical report).

### Source

apps.dtic.mil/sti/html/trecms/AD1224699 (US Defense Technical Information
Center mirror)

### Publication Date

Unknown

### Category

MULTILINGUAL, OTHER

### Claims Relevant to Project

Title suggests direct relevance to code-switched-text authenticity
prediction — potentially the only source found on this exact topic.

### Methodology

Unknown — content could not be retrieved (403 error on 2 fetch attempts).

### Limitations

Authors, venue, date, methodology, and results are all unconfirmed.
Existence of a real, indexed technical-report title is confirmed; content
is entirely UNVERIFIED.

### Relevance

Flagged as a lead requiring manual retrieval, not as a usable citation —
should not be relied upon for any claim until its content is obtained
and read.

### Potential Project Impact

Research (R05) — pending manual retrieval

### Reproducibility

Unknown

### Status

UNREVIEWED — content not retrievable in this pass, manual follow-up
required

---

## R-0074 — Detector-Evasive LLM Paraphrasing via Constrained Policy Optimization (DEPO)

### Citation

Wang, Shen, Bu, Zou.

### Source

arXiv:2606.00392

### Publication Date

2026-05

### Category

ADVERSARIAL-ROBUSTNESS, TEXT-TRANSFORMATION

### Claims Relevant to Project

Frames detector evasion as a Constrained MDP: evasion is the primary
optimization objective, semantic preservation (BERTScore F1) is an
explicit constraint (τ_sem = 0.85), solved via Lagrangian primal-dual
optimization rather than edit-distance minimization. Reports ASR@1%FPR =
0.957 at semantic reward 0.857. Shows linear-scalarization baselines
(weights 0.1-0.5) fail to satisfy the semantic constraint, motivating the
constrained-optimization framing over naive weighted trade-offs.

### Limitations

Single reported operating point, not a full swept trade-off curve;
preprint, not independently reviewed or replicated.

### Relevance

The clearest example found of a detector-evasion paper treating
minimality/preservation as a hard constraint rather than a soft
trade-off term — directly relevant to R06 §4-5 (Minimality,
Transformation Magnitude).

### Potential Project Impact

Research (R06), Scientific Specification (minimality methodology)

### Reproducibility

Unknown (not confirmed in this pass)

### Status

RELEVANT

---

## R-0075 — The Mark Fades: Adaptive Evolutionary Paraphrase-based Attack against LLM Watermarks

### Citation

Zhao, Zhao, Zhang, Wei, Li; Findings of ACL 2026.

### Source

Findings of ACL 2026 (exact arXiv ID not captured in this pass).

### Publication Date

2026-07 (approximate)

### Category

ADVERSARIAL-ROBUSTNESS, WATERMARKING, TEXT-TRANSFORMATION

### Claims Relevant to Project

Explicitly formulates watermark removal as a constrained multi-objective
optimization problem, solved with a genetic algorithm navigating an
actual Pareto front. Near-100% attack success rate while holding
BERTScore 0.73-0.77 at moderate settings, versus ~97% ASR but BERTScore
collapsing to 0.56 at an aggressive 80%-deletion setting. Parameterizes
attack strength directly as a deletion percentage, functioning as an
explicit edit-size knob with measured quality cost.

### Methodology

Genetic-algorithm-based Pareto optimization of paraphrase attacks against
LLM watermarks, peer-reviewed (Findings of ACL).

### Limitations

Findings-track (not main-track) publication; single benchmark setup,
generalization to other watermark schemes not confirmed in this pass.

### Relevance

The strongest, most directly on-point source found for R06 §20 (Pareto
Analysis) — a real, peer-reviewed, quantified trade-off curve between
evasion success and quality preservation. Also directly extends R02
§37.2's paraphrasing-evasion finding (R-0039) with an explicit
quality-cost dimension not previously captured.

### Potential Project Impact

Research (R02 §20 Pareto Analysis in R06, R02 §6-7 Robustness), Scientific
Specification

### Reproducibility

Unknown (not confirmed in this pass)

### Status

RELEVANT

---

## R-0076 — StealthRL: Reinforcement Learning Paraphrase Attacks for Multi-Detector Evasion of AI-Text Detectors

### Citation

Ranganath, Ramesh.

### Source

arXiv:2602.08934

### Publication Date

2026-03

### Category

ADVERSARIAL-ROBUSTNESS, TEXT-TRANSFORMATION

### Claims Relevant to Project

Three-method trade-off comparison: simple paraphrase baseline (0.974
E5 cosine similarity / 0.716 mean ASR) vs. StealthRL (0.901 similarity /
0.976 ASR) vs. adversarial paraphrasing (0.973 similarity / 0.783 ASR) —
authors explicitly acknowledge StealthRL "pays a noticeable fidelity
cost" for its evasion gains. Uses both an E5 embedding cosine-similarity
metric and an LLM-as-judge (GPT-5-nano) dual Likert scale; the two metrics
diverge substantially in absolute terms (embedding similarity 0.901 vs.
LLM-judge semantic-similarity rating 2.64/5) on the same outputs.
Explicitly scoped as single-shot only, "no iterative refinement."

### Methodology

RL-trained paraphrase attack evaluated against multiple detectors, with
both embedding-based and LLM-judge preservation metrics reported side by
side.

### Limitations

Small, single-paper LLM-judge protocol, not independently validated;
preprint.

### Relevance

Documents metric heterogeneity directly: the same system scores very
differently on embedding-cosine vs. LLM-as-judge preservation metrics —
relevant to R06 §27 (Metric Diversity) as concrete evidence that "no
single similarity metric should define preservation universally" is not
just a design principle but an observed empirical pattern.

### Potential Project Impact

Research (R06 §27 Metric Diversity, §51-52 Detector/Watermark Response)

### Reproducibility

Unknown (not confirmed in this pass)

### Status

RELEVANT

---

## R-0077 — PADBen: A Comprehensive Benchmark for Evaluating AI Text Detectors Against Paraphrase Attacks

### Citation

Zha, Min, Shanu.

### Source

arXiv:2511.00416

### Publication Date

2025-11

### Category

ADVERSARIAL-ROBUSTNESS, EVALUATION

### Claims Relevant to Project

Only benchmark found that explicitly measures iteration-count effects on
paraphrase drift: single vs. triple rounds of LLM paraphrasing; BGE-M3
embedding cosine distance for human-text paraphrases increases from 0.085
to 0.134 across iterations ("progressive drift"). Coins the concept of an
"intermediate laundering region" — semantic displacement with preserved
generation-pattern signal.

### Limitations

Only 3 rounds tested; embedding-distance metric only, no
factuality/entity-specific measurement.

### Relevance

Directly relevant to R06 §32 (Repeated Transformation) — the clearest
quantified evidence found that repeated transformation accumulates
measurable drift, though the horizon tested (3 rounds) is short.

### Potential Project Impact

Research (R06 §32 Repeated Transformation)

### Reproducibility

Unknown (benchmark availability not confirmed in this pass)

### Status

RELEVANT

---

## R-0078 — From "May" to "Is": Certainty Distortion in Language Model Rewriting

### Citation

Belem, Wu, Yao, Steyvers, Singh, Smyth.

### Source

arXiv:2606.07951

### Publication Date

2026-06

### Category

TEXT-TRANSFORMATION, SEMANTIC-PRESERVATION

### Claims Relevant to Project

Measures certainty/hedging distortion during LLM rewriting, explicitly
separated from factuality/hallucination as a distinct axis. Distortion
affects 30-75% of outputs depending on task/model; models inflate
certainty 1.5-2x more often than they deflate it; domain-dependent rates
of 37-75% (scientific) vs 12-38% (medical) for single-pass rewriting.
Using 5-iteration rewriting chains: scientific-domain distortion mostly
occurs after the first rewrite then plateaus, while medical-domain
certainty inflation compounds progressively across all 5 iterations
(Claude 4.5: 20%→40% certainty inflation from iteration 1 to 5). Explicitly
frames this as a "broken telephone effect."

### Limitations

Domain-dependent findings limited to scientific and medical domains only;
explicitly scoped as separate from factuality/hallucination — does not
itself measure factual accuracy.

### Relevance

The most rigorous iterative-transformation-drift evidence found in this
pass, and a materially new preservation dimension (epistemic
certainty/hedging) not explicitly named in R06 §3's preservation
dimension list. Directly relevant to R06 §32 (Repeated Transformation)
and suggests R06 §3 should eventually consider certainty/hedging as a
distinct preservation dimension alongside factual and semantic
preservation — a candidate for a knowledge-backlog entry rather than an
immediate specification change.

### Potential Project Impact

Research (R06 §3, §32), Scientific Specification (candidate new
preservation dimension)

### Reproducibility

Unknown (not confirmed in this pass)

### Status

RELEVANT

---

## R-0079 — Understanding the Effects of Human-written Paraphrases in LLM-generated Text Detection

### Citation

Lau, Zubiaga; Queen Mary University of London.

### Source

ScienceDirect record (exact venue/date not fully confirmed in this pass).

### Publication Date

2024/2025 (approximate, not confirmed)

### Category

ADVERSARIAL-ROBUSTNESS, TEXT-TRANSFORMATION

### Claims Relevant to Project

Illustrative example: DIPPER (R-0024) transforms a precise financial
figure ("$1.1218") inconsistently across successive paraphrase rounds in
a financial-text example — the clearest evidence found of numeric drift
under plain, non-watermark paraphrasing, paralleling the project's
already-documented watermark-driven numeric-drift concern (R-0041).
Finds human-paraphrase-augmented detection especially effective under
recursive paraphrasing attacks, implying multi-round paraphrasing is a
recognized harder regime.

### Limitations

The numeric-drift finding is a single illustrative example in the
source's own tables, not a systematically quantified accuracy rate;
exact venue/date not independently confirmed in this pass.

### Relevance

Directly relevant to R06 §8 (Numerical Preservation) — parallel evidence
that numeric drift under transformation is not specific to
watermark-driven token substitution but occurs under plain paraphrasing
too, though the evidence here remains anecdotal rather than systematic.

### Potential Project Impact

Research (R06 §8 Numerical Preservation), Knowledge Backlog (candidate
gap: no systematic numeric/entity preservation study found)

### Reproducibility

Unknown (not confirmed in this pass)

### Status

PARTIALLY_RELEVANT — illustrative example, not a systematic study; venue
unconfirmed

---

## R-0080 — TAROT: Task-Oriented Authorship Obfuscation Using Policy Optimization Methods

### Citation

Loiseau, Sileo, Riquet, Meyer, Tommasi.

### Source

arXiv:2407.21630

### Publication Date

2024-07

### Category

TEXT-TRANSFORMATION, ADVERSARIAL-ROBUSTNESS

### Claims Relevant to Project

Explicit obfuscation-vs-preservation trade-off table (IMDb-10): TAROT-DPO
(BLEU 10.77, METEOR 30.04, BERTScore 80.56) prioritizes obfuscation
strength at a content-preservation cost; TAROT-PPO (BLEU 20.77, METEOR
37.93, BERTScore 84.50) prioritizes preservation. Also uses GTE cosine
similarity, CoLA grammaticality, and downstream-classification utility as
complementary evaluation axes.

### Methodology

RL-policy-optimization-based authorship obfuscation with multi-metric
trade-off evaluation.

### Limitations

Single dataset (IMDb-10); GTE/CoLA/downstream-utility metrics not
cross-validated against human judgment in the excerpt reviewed.

### Relevance

Confirms, alongside R-0074/R-0075/R-0076, a cross-paper pattern: RL/
preference-optimization method choice (DPO vs. PPO) measurably shifts the
operating point on the evasion-vs-preservation trade-off — relevant to
R06 §20 (Pareto Analysis) and §54 (Objective Conflict).

### Potential Project Impact

Research (R06 §14 Stylistic Preservation, §20 Pareto Analysis)

### Reproducibility

Unknown (not confirmed in this pass)

### Status

RELEVANT

---

## R-0081 — StyleRemix: Interpretable Authorship Obfuscation via Distillation and Perturbation of Style Elements

### Citation

Fisher, Hallinan, Lu, Gordon, Harchaoui, Choi.

### Source

arXiv:2408.15666

### Publication Date

2024-08

### Category

TEXT-TRANSFORMATION

### Claims Relevant to Project

Interpretable authorship obfuscation via LoRA-based perturbation of
individual style axes (e.g., formality, length); claims both automatic
and human evaluation were used and reports outperforming SOTA baselines.

### Limitations

Specific trade-off numbers could not be retrieved from the accessible
excerpt in this pass — existence and topical relevance confirmed, figures
are not; requires a follow-up full-PDF fetch before any number is cited.

### Relevance

Topically on-point for R06 §14 (Stylistic Preservation) once specific
figures are verified.

### Potential Project Impact

Research (R06 §14) — pending verification

### Reproducibility

Unknown

### Status

UNREVIEWED — existence/claims only, figures require follow-up

---

## R-0082 — Towards Human Understanding of Paraphrase Types in Large Language Models

### Citation

Meier, Wahle, Ruas, Gipp; COLING 2025.

### Source

arXiv:2407.02302

### Publication Date

2025-01

### Category

EVALUATION, TEXT-TRANSFORMATION

### Claims Relevant to Project

Two-phase human evaluation protocol: Phase 1 binary correctness
classification of paraphrase type; Phase 2 best-worst-scaling preference
ranking (400 preference annotations across 80 ranking lists). Automatic
"success" and human preference diverge — Chain-of-Thought generations
were relatively successful by the correctness metric yet ranked lower by
human annotators than other methods.

### Methodology

Two-phase human-annotation protocol (correctness classification +
best-worst scaling), peer-reviewed (COLING).

### Limitations

Small annotation pool (80 ranking lists); protocol not compared against
alternative (pairwise/absolute) protocols within the same paper.

### Relevance

Directly relevant to R06 §23-26 (Human Evaluation, Pairwise/Absolute
Evaluation); the automatic-vs-human divergence finding is a concrete
caution against relying solely on automated metrics for paraphrase
quality (R06 §22, Automated Evaluation).

### Potential Project Impact

Research (R06 §22-26 Evaluation Methodology)

### Reproducibility

Unknown (not confirmed in this pass)

### Status

RELEVANT

---

## R-0083 — Do Text Simplification Systems Preserve Meaning? A Human Evaluation via Reading Comprehension

### Citation

Agrawal, Carpuat; TACL.

### Source

arXiv:2312.10126

### Publication Date

~2023

### Category

EVALUATION, SEMANTIC-PRESERVATION

### Claims Relevant to Project

Extrinsic, task-based evaluation protocol (reading-comprehension
multiple-choice with an "unanswerable" option) rather than direct
Likert/pairwise text rating; 112 Prolific participants, OneStopQA-derived
passages. Best system (MUSS-SUP) left 14% of questions unanswerable,
worst system (KIS) left ~79.5% unanswerable (20.5% answerable); human
baseline ~78% answerable.

### Methodology

Extrinsic reading-comprehension human-evaluation protocol, peer-reviewed
(TACL).

### Limitations

Text-simplification domain, not paraphrase/detector-evasion specifically;
the extrinsic protocol may not transfer directly to evasion-quality
assessment without adaptation.

### Relevance

A distinct methodological family from preference-ranking approaches
(R-0082) — content deletion/omission as the dominant meaning-loss
mechanism is directly relevant to R06 §44 (Omission Detection) and §21
(Failure Modes).

### Potential Project Impact

Research (R06 §21 Failure Modes, §23-26 Evaluation Methodology)

### Reproducibility

Available (methodology described, OneStopQA-derived)

### Status

RELEVANT

---

## R-0084 — How Good is Post-Hoc Watermarking With Language Model Rephrasing?

### Citation

Fernandez et al.; Meta FAIR.

### Source

arXiv (2025; exact ID not captured in this pass).

### Publication Date

2025

### Category

WATERMARKING, TEXT-TRANSFORMATION

### Claims Relevant to Project

Reports a quality-detectability Pareto frontier for watermark-embedding
rephrasing (the embedding side, not evasion/removal): "no method achieves
both high pass@1 and high TPR simultaneously" for code watermarking.

### Limitations

Industry-affiliated authors (Meta FAIR) — treat with the usual
VENDOR-adjacent caution despite being a research preprint; code-domain
specific, not prose text.

### Relevance

Adjacent corroboration that Pareto framing is the field's standard
analytical convention for watermark quality-vs-detectability trade-offs,
on the embedding side rather than the evasion side covered by
R-0074/R-0075.

### Potential Project Impact

Research (R02, R06 §20 Pareto Analysis)

### Reproducibility

Unknown (not confirmed in this pass)

### Status

PARTIALLY_RELEVANT — industry-affiliated, code-domain, embedding-side not
evasion-side

---

## R-0085 — Established Summarization Factuality-Metric Toolkit (FactCC, SummaC, QAFactEval, AlignScore)

### Citation

Multiple: Kryscinski et al. (FactCC); Laban et al. (SummaC); Fabbri et
al., NAACL 2022 (QAFactEval, arXiv:2112.08542); Zha et al., ACL 2023
(AlignScore).

### Source

Multiple peer-reviewed papers; corroborated via ACL Anthology, GitHub,
and survey articles.

### Category

SEMANTIC-PRESERVATION, EVALUATION

### Claims Relevant to Project

These are established, peer-reviewed automatic factual-consistency
metrics for summarization. Their existence and general acceptance in
summarization research is well-corroborated (EVIDENCE tier).

### Limitations

**No evidence found** in this pass of any of these metrics — or an
LLM-as-judge factuality protocol — being applied specifically to
detector-evasion or watermark-removal paraphrasing. This is a confirmed
gap, not an oversight: the toolkit exists and is mature for
summarization, but a bridging study to the evasion/transformation use
case this project cares about has not been found.

### Relevance

Directly relevant to R06 §7 (Factual Preservation) and §41 (Factual
Consistency) — these metrics are candidates for the project's own
methodology once it needs to measure factual preservation, but should not
be assumed to transfer to the evasion/transformation domain without
validation.

### Potential Project Impact

Research (R06 §7, §41), Scientific Specification (candidate factual-
preservation metric family, pending validation), Knowledge Backlog
(candidate gap entry)

### Reproducibility

Available (all four tools are open-source)

### Status

PARTIALLY_RELEVANT — established for summarization, unvalidated for this
project's use case

---

## R-0086 — Heads We Win, Tails You Lose: AI Detectors in Education

### Citation

Bassett, Bradshaw, Bornsztejn, Hogg, Murdoch, Pearce, Webber; Journal of
Higher Education Policy and Management.

### Source

Journal of Higher Education Policy and Management (peer-reviewed,
published online); also OSF/EdArXiv preprint.

### Publication Date

2026-01-29

### Category

AI-DETECTION, EVALUATION

### Claims Relevant to Project

Formal base-rate (Bayes'-theorem) argument: for the same detector false-
positive rate, the probability the detector is correct when it flags a
document depends heavily on the (unknown, typically low) real-world
prevalence of AI-generated submissions — worked example: 97.5% correct
if 300 of a population are AI-generated vs. 47.6% correct if only 10 are.
Argues FPR/accuracy alone is meaningless without the base rate, and that
ground truth is fundamentally unverifiable in most deployment settings.

### Methodology

Analytic (Bayes'-theorem-based) argument with a worked numerical example,
not an empirical multi-detector test.

### Limitations

Argument is analytic, not empirical; education-policy framing rather than
a pure statistics paper.

### Relevance

Directly relevant to R07 §64 (Class Imbalance) and §35 (Statistical vs
Practical Significance) — a formal articulation of why this project's own
principle (favor conservative false-positive behavior over aggregate
accuracy, SPECIFICATION-MAP.md §25-26) is not merely a preference but a
mathematical necessity given unknown deployment prevalence.

### Potential Project Impact

Research (R07 §64), Scientific Specification §25-26, Certification (no
accuracy claim should be presented without prevalence context)

### Reproducibility

Available (argument is analytic/reproducible)

### Status

RELEVANT

---

## R-0087 — Contamination in Generated Text Detection Benchmarks

### Citation

Dingfelder & Riess; FAU Erlangen-Nürnberg.

### Source

arXiv:2511.09200

### Publication Date

2025-11

### Category

EVALUATION, AI-DETECTION

### Claims Relevant to Project

The widely-used DetectRL benchmark contains systematic generation-
artifact contamination: ~98.5% of its Claude-generated texts carry
simplistic formulaic markers (refusal boilerplate, "Here is..." openers
in 94.7%), which detectors trained on it learn as shortcuts. Prefixing
human text with such a marker caused 87.9% misclassification as AI by a
detector trained on uncleaned data, vs. 2.9% after a data-cleaning
intervention.

### Methodology

Direct analysis of a published benchmark's generated-text artifacts, plus
a controlled spoofing experiment. **Update (2026-08-24, R08 literature
pass):** methodology further confirmed as regex/pattern-matching for
boilerplate detection combined with SHAP explainability attribution and
adversarial spoofing; a second reported figure from the same paper:
injecting a trigger phrase collapsed classification accuracy on human
text from 99.9% to 12.1% (a distinct experimental condition from the
87.9%-misclassification figure above, not a contradiction). The paper
recommends source-level data cleansing, multi-stage LLM-assisted
verification, and benchmark regeneration with current models.

### Limitations

Single benchmark (DetectRL) studied; not shown to generalize to other
benchmarks; note the arXiv listing's title field is corrupted by an
apparent LLM-generation artifact — verify via the PDF directly, not the
abstract page title.

### Relevance

Directly relevant to R07 §29-30 (Test Set Leakage, Benchmark Reuse) —
concrete evidence of a benchmark-artifact contamination failure mode
distinct from classic train/test leakage but arguably more damaging,
since it teaches detectors a spurious shortcut rather than merely
inflating a score.

### Potential Project Impact

Research (R07 §29-30, R08 — benchmark validity criteria)

### Reproducibility

Available (methodology and benchmark are public)

### Status

RELEVANT

---

## R-0088 — ARB: A Matched Authorship-Rewriting Benchmark Dataset for AI-Text Detector Evaluation

### Citation

Perrone & Romano.

### Source

arXiv:2607.29539

### Publication Date

2026-07

### Category

EVALUATION, AI-DETECTION

### Claims Relevant to Project

Standard human-vs-LLM benchmarks don't cover the realistic case of
LLM-revised (not fully generated) human text; detection rates drop 60-78
percentage points on this condition vs. the standard benchmark condition.

### Methodology

New matched benchmark construction (authorship-rewriting pairs) plus
detector re-evaluation on it.

### Limitations

Very recent preprint, single-lab, not yet independently corroborated.

### Relevance

Directly relevant to R04 §7 (Hybrid Text) and R07 §27 (Distribution
Shift) — quantifies how much a realistic-but-underrepresented condition
(human text revised by AI) degrades detector performance relative to the
standard benchmark condition.

### Update (2026-08-24, R08 literature pass)

License confirmed: **Apache License 2.0** for the assembled ARB
artifact, stated explicitly in the paper. Notably, the paper also
explicitly discloses per-source-corpus licensing status for its human-text
inputs (XSum undeclared license; WritingPrompts MIT; OpenWebText CC0)
with a disclaimer that "downstream users remain responsible for" those
source terms — a directly citable, primary-source example of the
inherited/unclear-licensing problem relevant to Q-007. The paper's own
automated QA reports **0.01% exact duplicates** (~2 of 23,400 samples)
and **0.67%** of generated texts flagged as too-short/non-English —
both explicitly **retained rather than silently dropped**, a
transparency-over-silent-curation practice worth noting for R08 §58
(Dataset Quality Checks). No near-duplicate (MinHash/LSH-style) detection
is described, only exact-match.

### Potential Project Impact

Research (R04 §7, R07 §27, R08 — benchmark construct validity, licensing,
quality-check practice), Open Questions (Q-007)

### Reproducibility

Unknown (dataset availability not confirmed in this pass)

### Status

RELEVANT

---

## R-0089 — Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy

### Citation

Pudasaini, Miralles-Pechuán, Lillis, Llorens Salvador.

### Source

arXiv:2603.23146

### Publication Date

2026-04 (v2)

### Category

AI-DETECTION, EVALUATION

### Claims Relevant to Project

A detector with F1=0.9734 on the PAN-CLEF leaderboard fails substantially
under cross-domain and cross-generator evaluation; SHAP analysis shows
the model exploited dataset-specific artifacts rather than genuine
authorship signal.

### Methodology

Leaderboard-benchmark re-evaluation under cross-domain/cross-generator
conditions, with SHAP-based explainability analysis of what the model
actually learned.

### Limitations

Preprint; specific to the models/datasets tested (PAN-CLEF, COLING,
Ghostbuster).

### Relevance

**Resolves KB-009's item 4** (this paper was previously confirmed to
exist but its content could not be extracted during the R04 pass) — now
fully read and registered. Directly parallels R-0087's finding: a
leaderboard-competitive score does not reflect generalizable detection,
reinforcing R07 §29-30's concern about benchmark-dependent conclusions.

### Potential Project Impact

Research (R07 §27-30), Knowledge Backlog (KB-009 partial resolution)

### Reproducibility

Available (methodology described)

### Status

RELEVANT

---

## R-0090 — Who Wrote This? Evaluating the Reliability of AI Detection Tools in Higher Education

### Citation

Van Vlasselaer, Van Droogenbroeck, Spruyt; International Journal for
Educational Integrity, 22:16.

### Source

International Journal for Educational Integrity (peer-reviewed).

### Publication Date

2026-06-29

### Category

AI-DETECTION, EVALUATION

### Claims Relevant to Project

Independent 4-tool test (GPTZero, Pangram, Copyleaks, Turnitin) on 160
ground-truthed documents: Turnitin showed 100% false-negative rate on
fully-AI-generated papers; large cross-tool disagreement; confidence-
score outputs inconsistently calibrated across tools (Turnitin ~0% on
known-AI text, GPTZero median <20%, Pangram median closest to the true
100% value).

### Methodology

Independent (non-vendor) multi-tool comparison on a ground-truthed
document set, peer-reviewed.

### Limitations

Single study, 160 documents, 4 tools; results may not generalize to other
tool versions/time periods given rapid tool updates — a general
limitation of any cloud-detector evaluation (R03 §17, Detector Drift).

### Relevance

A new (2026), independent, peer-reviewed corroboration of the pattern
already documented by Weber-Wulff et al. (R-0012) — vendor-claimed
accuracy does not hold up uniformly under independent testing — with
different tools and a direct calibration-failure finding (R07 §67).

### Potential Project Impact

Research (R03 §16-18 Cloud/External Detectors, R07 §67 Calibration)

### Reproducibility

Partial (methodology described, document set availability not confirmed)

### Status

RELEVANT

---

## R-0091 — Spotlights and Blindspots: Evaluating Machine-Generated Text Detection

### Citation

Stowe & Patil.

### Source

arXiv:2604.16607

### Publication Date

2026-04

### Category

AI-DETECTION, EVALUATION

### Claims Relevant to Project

15 detection models evaluated across 7 test sets and 3 human-written
datasets: high variance in model rankings depending on dataset/metric
choice; no single system dominates across conditions; performance
representation is critically linked to dataset and metric choices "often
assumed or overlooked."

### Methodology

Large-scale cross-model, cross-dataset, cross-metric re-evaluation.

### Limitations

Preprint, not yet confirmed peer-reviewed at time of this pass.

### Relevance

Empirical demonstration (not just an assertion) of R07 §27's concern
(Distribution Shift) and directly supports R03 §19 (Detector Coverage) —
published detector rankings are unreliable across conditions, not merely
theoretically vulnerable to this.

### Potential Project Impact

Research (R03 §19, R07 §27, R08 — benchmark/metric standardization)

### Reproducibility

Unknown (not confirmed in this pass)

### Status

RELEVANT

---

## R-0092 — A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions

### Citation

Wu, Yang, Zhan, Yuan, Chao, Wong; Computational Linguistics (MIT Press),
Vol. 51, No. 1.

### Source

Computational Linguistics journal (peer-reviewed).

### Publication Date

2024-11 (accepted)

### Category

AI-DETECTION, EVALUATION

### Claims Relevant to Project

Names "lack of robust evaluation framework" as a top field challenge;
documents that published studies use inconsistent metrics (accuracy,
precision, recall, FPR, TNR, FNR, F1, AUROC) without a standardized
convention, making cross-paper comparison unreliable.

### Methodology

Peer-reviewed survey of the AI-text-detection field.

### Limitations

Survey-level claim (documents the pattern) rather than a new empirical
measurement of the fragmentation's magnitude.

### Relevance

A citable, peer-reviewed, leading-venue statement of the "benchmark
fragmentation" problem — directly relevant to R07 §4 (Primary Metrics)
and the project's own need to fix a metric convention before comparing
results across its own experiments.

### Potential Project Impact

Research (R07 §4, §78 Research Outputs — metric-definition standardization)

### Reproducibility

Not applicable (survey)

### Status

RELEVANT

---

## R-0093 — A Statistical Framework of Watermarks for Large Language Models: Pivot, Detection Efficiency and Optimal Rules

### Citation

Li, Ruan, Wang, Long, Su; Annals of Statistics, Vol. 53(1), pp. 322-351.

### Source

Annals of Statistics (top peer-reviewed statistics journal); arXiv:2404.01245

### Publication Date

2025-02 (published; submitted 2024-04)

### Category

WATERMARKING, EVALUATION

### Claims Relevant to Project

Frames watermark detection as formal hypothesis testing; gives a
pivotal-statistic-based method for explicit false-positive-rate control;
derives a closed-form asymptotic false-negative rate; reduces optimal-
detection-rule selection to a minimax program. Reportedly applied
including to a watermark "internally implemented at OpenAI."

### Methodology

Rigorous statistical-theory development in a top statistics venue.

### Limitations

Primarily theoretical; empirical validation against real deployed
watermarks only partially described in the material reviewed in this
pass.

### Relevance

Strongest-tier evidence (top statistics journal, not an ML venue) that
genuine peer-reviewed statistical-guarantee work exists for watermark
detection beyond the Kirchenbauer/Three-Bricks lineage already
registered (R-0001, R-0037) — directly relevant to R07 §14-20
(Hypothesis Testing through Statistical Assumptions) and R03 §12
(Statistical Significance).

### Potential Project Impact

Research (R02, R03 §12, R07 §14-20)

### Reproducibility

Available (theoretical framework, described methodology)

### Status

RELEVANT

---

## R-0094 — Towards Anytime-Valid Statistical Watermarking

### Citation

Huang, Xu, Ramchandran, Jiao, Jordan.

### Source

arXiv:2602.17608

### Publication Date

2026-02

### Category

WATERMARKING, EVALUATION

### Claims Relevant to Project

First e-value-based watermarking framework giving "anytime-valid"
Type-I-error guarantees — the detection p-value/e-value stays statistically
valid even when the number of tokens examined before stopping is not
fixed in advance, addressing the classic "optional stopping invalidates
Type-I error guarantees" problem in naive p-value tests. Reports a 13-15%
reduction in tokens needed for detection vs. baselines.

### Methodology

E-value/test-supermartingale-based statistical framework, applied to
watermark detection.

### Limitations

Very recent preprint, single-lab, not independently corroborated; not
compared in the reviewed material against the Three Bricks (R-0037)
multi-key global-p framework.

### Relevance

Directly relevant to R07 §40 (Pre-Registration Principle) and §19
(P-Values) — addresses a real, formal gap in how detection statistics
remain valid under realistic (non-fixed-length) stopping behavior, a
concern this project's own methodology section raises in the abstract
but does not yet have field-specific evidence for.

### Potential Project Impact

Research (R02, R03, R07 §19, §40)

### Reproducibility

Unknown (not confirmed in this pass)

### Status

PARTIALLY_RELEVANT — very recent, unreplicated

---

## R-0095 — Optimal Watermark Generation under Type I and Type II Errors

### Citation

He.

### Source

arXiv:2512.05333

### Publication Date

2025-12

### Category

WATERMARKING

### Claims Relevant to Project

Frames watermark generation (not just detection) as constrained by
explicit Type-I/Type-II error bounds; derives a tight lower bound on
fidelity loss via f-divergence and identifies the optimal watermarked
distribution attaining that bound.

### Methodology

Theoretical information-theoretic framework.

### Limitations

Single-source preprint; author/venue details not independently
corroborated beyond the arXiv listing.

### Relevance

Complements R-0093/R-0094 on the generation (rather than detection) side
of formal statistical guarantees for watermarking.

### Potential Project Impact

Research (R02, R07)

### Reproducibility

Unknown (not confirmed in this pass)

### Status

UNREVIEWED — single-source preprint, not independently corroborated

---

## R-0096 — Watermarks in the Sand: Impossibility of Strong Watermarking for Generative Models

### Citation

Zhang, Edelman, Francati, Venturi, Ateniese, Barak; ICML 2024.

### Source

arXiv:2311.04378 (ICML 2024)

### Publication Date

2023-11 (ICML 2024 publication)

### Category

WATERMARKING, ADVERSARIAL-ROBUSTNESS

### Claims Relevant to Project

Proves that "strong" (robust-to-any-quality-preserving-perturbation)
watermarking is impossible under natural assumptions given quality-oracle
and perturbation-oracle access — a formal ceiling on what statistical
robustness guarantees are achievable at all for watermarking.

### Methodology

Formal impossibility proof, peer-reviewed (ICML).

### Limitations

Theoretical result; the oracle-access assumptions may not match every
real-world attack setting exactly, so the practical scope of the
impossibility result should be stated carefully rather than
overgeneralized.

### Relevance

A load-bearing negative result and caveat for any claim of unconditional
formal robustness guarantees in watermarking — should be cited whenever
R02 discusses watermark robustness claims, to avoid implying stronger
guarantees than are theoretically achievable.

### Potential Project Impact

Research (R02 §6-7 Robustness, R07 §14-20 Hypothesis Testing —
theoretical ceiling), Scientific Specification (do not specify a
robustness requirement that is provably unachievable)

### Reproducibility

Available (formal proof, peer-reviewed)

### Status

RELEVANT

---

## R-0097 — AI Watermark Evidence Fails Forensic Readiness: An Empirical Evaluation

### Citation

Tamim & Khan.

### Source

arXiv:2607.16010

### Publication Date

2026-07

### Category

WATERMARKING, ADVERSARIAL-ROBUSTNESS, EVALUATION

### Claims Relevant to Project

Empirically tests KGW, Unigram, and SynthID against forensic/legal
admissibility standards (Daubert factors): every initially-detected
KGW/Unigram-watermarked text lost its watermark after paraphrasing (100%
conditional removal); pre-attack false-negative rates of 70% (KGW), 83%
(Unigram), 80% (SynthID); SynthID flagged 5.4% of paraphrased human
controls as AI-generated and showed an 18.6% "paradox rate" with 80% of
its own genuine watermarked output landing in an uncertainty deadband.
None of the three methods satisfy more than two of five Daubert
admissibility factors.

### Methodology

Empirical testing of three real, deployed-lineage watermark schemes
against a formal legal-admissibility framework.

### Limitations

Single very recent preprint, not yet independently replicated; specific
to the tested watermark versions/attack setup — results may not transfer
to updated versions of these schemes.

### Relevance

Directly relevant to R02 §37.2/R03 §43.4 (Robustness) and materially
strengthens the case that formal-guarantee claims for deployed watermark
schemes (R-0093, R-0094, R-0095) do not survive real perturbation
conditions in practice — the theory/practice gap should be preserved as
an explicit tension (RESEARCH-MAP.md §22), not resolved by picking one
side.

### Potential Project Impact

Research (R02 §37.2, R03 §43.4, R07 — theory-vs-practice gap), Security,
Certification (evidentiary/forensic readiness is a distinct bar from
research-grade detection)

### Reproducibility

Partial (methodology described)

### Status

RELEVANT

---

## R-0098 — Benchmark Data Contamination of Large Language Models: A Survey

### Citation

Survey authors (per arXiv listing).

### Source

arXiv:2406.04244

### Publication Date

2024-06

### Category

EVALUATION, OTHER

### Claims Relevant to Project

Taxonomy of contamination-detection methods for general LLM
training/evaluation: matching-based (n-gram overlap — GPT-3 uses a
13-gram overlap threshold, GPT-4 a 50-character threshold — membership
inference, direct dataset inspection) and comparison-based
(embedding/cosine-similarity and perplexity-distribution comparison,
chronological/release-date performance analysis).

### Methodology

Survey of general LLM benchmark-contamination literature.

### Limitations

Explicitly scoped to general LLM training/eval contamination (code
generation, QA, translation, NER, fake-news, sentiment) — does **not**
discuss AI-text-detection or watermarking benchmarks at all. Apply its
taxonomy to this project's domain only by analogy, not as direct
evidence of what has been done in AI-detection benchmark construction.

### Relevance

A general-purpose contamination-detection taxonomy applicable to R08 §29
(Contamination) as a candidate methodology toolkit — n-gram overlap and
embedding/perplexity comparison techniques are directly transferable in
principle, though no evidence was found that any named AI-detection
benchmark (RAID, MGTBench, M4, HC3, MULTITuDE) has actually applied them.

### Potential Project Impact

Research (R08 §29 Contamination — candidate methodology)

### Reproducibility

Not applicable (survey)

### Status

PARTIALLY_RELEVANT — general-purpose taxonomy, not AI-detection-specific

---

## R-0099 — ETS Corpus of Non-Native Written English (LDC2014T06)

### Citation

Educational Testing Service / University of Pennsylvania Trustees, LDC
catalog.

### Source

Linguistic Data Consortium, catalog number LDC2014T06.

### Publication Date

2014

### Category

OTHER

### Claims Relevant to Project

The officially licensed corpus of real TOEFL essays from non-native
English speakers: gated behind LDC membership or a non-member fee,
copyright jointly held by ETS and University of Pennsylvania Trustees
(2014) — **not** freely redistributable.

### Methodology

Not applicable (dataset catalog entry, not a research paper).

### Limitations

Consent/IRB terms for the original essay collection were not verified in
this pass (a separate license PDF exists on the LDC site but was not
opened) — flagged as not yet verified, not as absent.

### Relevance

Directly answers part of Q-007 (which datasets can be legally distributed
within the project) for one specific, frequently-cited corpus type: this
one is explicitly **not** freely distributable. Also the corpus that
R-0022 (Liang et al.) did **not** use, despite testing "TOEFL essays" —
see R-0022's Governance Note.

### Potential Project Impact

Data (07-data — licensing/distributability), Open Questions (Q-007)

### Reproducibility

Not applicable (licensing fact, not a reproducible finding)

### Status

RELEVANT

---

## R-0100 — Datasheets for Datasets / Data Statements for NLP

### Citation

Gebru, Morgenstern, Vecchione, Vaughan, Wallach, Daumé III, Crawford,
"Datasheets for Datasets," arXiv:1803.09010 (Communications of the ACM,
2021); Bender & Friedman, "Data Statements for Natural Language
Processing: Toward Mitigating System Bias and Enabling Better Science."

### Source

arXiv:1803.09010; ACM CACM 2021.

### Publication Date

2018 (arXiv); 2021 (CACM); ongoing standard practice.

### Category

OTHER, EVALUATION

### Claims Relevant to Project

Two established, widely-cited documentation frameworks for NLP/ML
datasets, covering provenance, collection methodology, consent,
licensing, and known limitations — the field-standard governance
template for exactly the kind of documentation R08 §4 (Dataset
Provenance) already requires.

### Methodology

Established documentation standards, not automated tooling or
enforcement.

### Limitations

Documentation practice only — does not itself verify or enforce
compliance; adoption is voluntary and, per this pass's other findings
(R-0022's Governance Note, R-0087/R-0088's licensing findings), often not
followed even by well-cited papers in this specific field.

### Relevance

A directly adoptable template for the project's own R08 §4/§22
provenance and annotation documentation requirements — the project could
require its own dataset registry entries to follow this format rather
than inventing an equivalent from scratch.

### Potential Project Impact

Research (R08 §4, §22), Data (07-data — documentation standard candidate)

### Reproducibility

Not applicable (documentation standard)

### Status

RELEVANT

---

## R-0101 — text-dedup: General-Purpose Text Deduplication Toolkit

### Citation

ChenghaoMou (maintainer), GitHub repository.

### Source

github.com/ChenghaoMou/text-dedup

### Publication Date

Ongoing (open-source project)

### Category

OTHER

### Claims Relevant to Project

General-purpose text-corpus deduplication toolkit implementing
MinHash+MinHashLSH, SimHash (64/128-bit), Bloom-filter exact
deduplication, and suffix-array substring matching.

### Methodology

Open-source software implementing established near-duplicate and
exact-duplicate detection algorithms.

### Limitations

No evidence found that any named AI-text-detection benchmark (RAID,
MGTBench, M4, HC3, MULTITuDE, DetectRL) has actually used this or any
comparable MinHash/LSH-style tool — in contrast to general LLM
pretraining-corpus practice, where such deduplication is now standard.
This is a candidate tool, not a confirmed field practice.

### Relevance

Directly relevant to R08's implicit deduplication gap: only one AI-
detection-benchmark paper found in this pass (R-0088/ARB) reports any
duplicate-checking at all, and that was exact-match only (0.01%). This
tool is a candidate for the project's own dataset-construction pipeline
if/when it builds derived datasets (R08 §54-57, Provenance
Chain/Transformation Manifest).

### Potential Project Impact

Research (R08 §30 Deduplication — candidate tooling), Development
(candidate dependency)

### Reproducibility

Available (open source)

### Status

PARTIALLY_RELEVANT — candidate tool, not confirmed field practice

---

# Research Governance

Research sources must be versioned and traceable.

A change in scientific interpretation should produce:

1. a research-registry update;
2. an impact assessment;
3. documentation changes where necessary;
4. validation changes where necessary;
5. an explicit decision if production behavior changes.