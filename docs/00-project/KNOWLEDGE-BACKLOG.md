# Knowledge Backlog

## Purpose

This document captures potentially relevant ideas, observations,
hypotheses, concerns, research findings and design proposals that have
not yet been fully classified or incorporated into the project.

Nothing important should be lost merely because its final location
is not yet known.

---

# Statuses

Each item may have one of the following statuses:

- UNTRIAGED
- TRIAGED
- INCORPORATED
- DUPLICATE
- REJECTED
- SUPERSEDED
- DEFERRED

---

# Priority

- CRITICAL
- HIGH
- MEDIUM
- LOW

---

# Item Template

## KB-XXX — Title

### Source

Where the idea originated.

### Observation

What was observed.

### Proposal / Hypothesis

What might follow from the observation.

### Potential Impact

Which parts of the project may be affected.

### Candidate Areas

Potential documentation areas.

### Related Research

Relevant research identifiers.

### Related Decisions

Relevant decision identifiers.

### Status

UNTRIAGED

### Priority

MEDIUM

### Required Action

What should eventually happen.

---

# Current Items

## KB-001 — Effectiveness Must Be Versioned

### Observation

The scientific landscape around watermarking, provenance and AI-content
detection changes over time.

### Proposal

Effectiveness must be defined through versioned evaluation profiles rather
than through a permanent binary claim.

### Potential Impact

- Research
- Scientific Specification
- Validation
- Certification
- Release Governance

### Status

TRIAGED

### Priority

CRITICAL

---

## KB-002 — External Detector Results Are Evidence, Not Truth

### Observation

Third-party detectors may change behavior, thresholds or implementations.

### Proposal

External detector output must be represented as versioned evidence with
provider, timestamp, configuration and provenance metadata where possible.

### Potential Impact

- Validation
- External Evidence
- Research Registry
- Reproducibility

### Status

TRIAGED

### Priority

HIGH

---

## KB-003 — Capability Lifecycle Must Include Removal

### Observation

A continuously evolving system can accumulate obsolete components.

### Proposal

Every major component must have a lifecycle including deprecation,
retirement and removal.

### Potential Impact

- Architecture
- Development
- Operations
- Certification

### Status

TRIAGED

### Priority

HIGH

---

## KB-004 — Documentation Must Be Incrementally Maintainable

### Observation

New knowledge may invalidate or affect documents created earlier.

### Proposal

Use a project map, knowledge backlog, decision log, assumption registry,
open-question registry and documentation change queue.

### Status

TRIAGED

### Priority

CRITICAL

---

## KB-005 — Agent Must Perform Impact Analysis

### Observation

A new change may affect documents and components not explicitly named
in the original task.

### Proposal

Claude Code must perform repository-wide impact analysis before closing
a substantive change.

### Status

TRIAGED

### Priority

CRITICAL

---

## KB-006 — Runtime Must Be Independent of Generative AI Services

### Observation

The production runtime is intended to execute without requiring an
external generative AI service.

### Proposal

Separate development/maintenance intelligence from runtime execution.

### Status

TRIAGED

### Priority

CRITICAL

---

## KB-007 — Local Storage Is a Hard Constraint

### Observation

The project has approximately 30 GB available for local project assets.

### Proposal

Treat storage as a first-class engineering constraint.

### Status

TRIAGED

### Priority

HIGH

---

## KB-008 — Multilingual AI-Detection Evidence Is Thin for Most Target Languages

### Source

R04 literature research pass, 2026-08-23
(`docs/02-research/R04-ai-generated-text-detection-research.md` §39.4).

### Observation

Of the project's 13 target languages (SPECIFICATION-MAP.md §20), no
independently verified, non-vendor detection study was found during this
research pass for German, Italian, Portuguese, Russian, Japanese, Polish,
Dutch, Turkish, or Indonesian (9 of 13). The only multilingual-by-design
benchmarks found (M4, R-0019; BLUFF, R-0021) either lack extracted
per-language detail or have unverified figures. Commercial vendors claim
broad coverage without publishing checkable per-language studies.

### Proposal / Hypothesis

Multilingual detector capability states (SPECIFICATION-MAP.md §22) for
most of the 13 target languages should default to RESEARCH_ONLY or
NOT_SUPPORTED rather than any validated tier, until language-specific
evidence is found or produced. This is a literature-confirmed gap, not
merely an internal project assumption.

### Potential Impact

- Scientific Specification §20-22 (realistic initial capability-state
  assignment per language)
- Research (R05 — prioritize search effort on the 9 under-evidenced
  languages, or commission targeted evaluation)
- Certification (no language should be certified beyond what evidence
  supports)

### Candidate Areas

03-scientific-specification, 02-research (R05), 10-certification

### Related Research

R-0019, R-0021, R-0029

### Related Decisions

None yet — this is evidence, not a decision.

### Status

TRIAGED

### Priority

HIGH

### Required Action

When R05 (Multilingual and Linguistic Research) is populated, cross-check
against this gap; when 03-scientific-specification assigns initial
per-language capability states, do not assign beyond RESEARCH_ONLY for the
9 languages listed here without new evidence.

### Correction (2026-08-24, R05 literature pass)

The R05 pass (`docs/02-research/R05-multilingual-linguistic-research.md`
§47.1) found this observation **no longer holds as originally stated for
AI-text detection**: dedicated or benchmark-level detection evidence now
exists for all 13 target languages (see R-0046 through R-0060 for the
specific per-language sources). What still holds: evidence *depth* varies
enormously (mostly single-study or benchmark-inclusion-level, not
English-scale multi-lab convergence), and **watermarking** evidence (as
distinct from detection) remains thin for nearly every non-English
language — no dedicated per-language watermarking study was found for
German, Italian, Portuguese, Russian, Japanese, Polish, Dutch, or Turkish.
The original observation and proposal below are left intact for
traceability; they should be read together with this correction, not
in place of it. The practical revision: capability-state defaults
(SPECIFICATION-MAP.md §20-22) should be assessed per-language against the
specific evidence in R05 §47.1 rather than applying a uniform
RESEARCH_ONLY/NOT_SUPPORTED default across all 9 originally-flagged
languages — but watermarking capability states specifically should stay
conservative for nearly all non-English languages regardless of this
correction.

### Status (updated)

TRIAGED — corrected, not resolved; still requires 03-scientific-
specification action per DCQ-006.

---

## KB-009 — Unverified Secondary-Sourced Figures From R04 Literature Pass

### Source

R04 literature research pass, 2026-08-23
(`docs/02-research/R04-ai-generated-text-detection-research.md` §39.5).

### Observation

Several specific numeric claims surfaced during the R04 literature pass
could only be traced to secondary sources (e.g. Wikipedia, education-press
summaries) rather than confirmed directly against the primary paper's own
tables/body text: the R-0022 "61.3% false-positive rate" figure, a claimed
91.3%→27.8% accuracy drop after a humanizer tool, and a claim that Black
students are markedly more likely to be falsely flagged (attributed to a
Common Sense Media report not directly located). Additionally, BLUFF
(R-0021) has internally inconsistent language-count figures across
sources, and one paper (arXiv:2603.23146) was confirmed to exist but its
content could not be extracted.

### Proposal / Hypothesis

None of these should be cited as established fact in any normative
document (specification, validation, certification) until directly
verified against their primary source.

### Potential Impact

Research Registry accuracy; any future document citing R-0021/R-0022 or
these unverified figures.

### Candidate Areas

02-research, 00-project/RESEARCH-REGISTRY.md

### Related Research

R-0021, R-0022

### Resolution Update (2026-08-24, R05 literature pass)

The R-0022 "61.3% false-positive rate" item is now RESOLVED: the R05 pass
fetched the Liang et al. paper directly and confirmed the correct figure
is **61.22%** (the "61.3%" figure was a secondary-source rounding
artifact, not a fabrication, but was unconfirmed until this pass). See
the updated R-0022 registry entry.

**Second resolution (2026-08-24, R07 literature pass):** arXiv:2603.23146
was fetched and fully read (Pudasaini, Miralles-Pechuán, Lillis, Llorens
Salvador, "Why AI-Generated Text Detection Fails: Evidence from
Explainable AI Beyond Benchmark Accuracy") — now registered as R-0089.
Its content is no longer unextracted: it documents a leaderboard-
competitive detector (F1=0.9734) failing under cross-domain/cross-
generator evaluation via SHAP analysis. See R07 §80.2.

The remaining items (humanizer 91.3%→27.8% drop, the Common Sense Media
claim, BLUFF's inconsistent counts) remain unresolved.

### Status

TRIAGED — two of four unverified items resolved; two remain open

### Priority

MEDIUM

### Required Action

A follow-up research pass should fetch and directly read: (1) the Liang et
al. paper's results tables, (2) the BLUFF paper's full body text, (3) the
primary Common Sense Media report if it exists, (4) arXiv:2603.23146's
full text. Update RESEARCH-REGISTRY.md entries and this item's status once
done.

---

## KB-010 — Watermarking Field Confirms the Multilingual Evidence Gap (KB-008) and Adds Unverified Figures of Its Own

### Source

R02/R03 literature research pass, 2026-08-23
(`docs/02-research/R02-watermark-research.md` §37.4-37.5,
`docs/02-research/R03-watermark-detection-research.md` §43.6).

### Observation

The watermarking/watermark-detection literature pass independently confirms
KB-008's finding (evidence for multilingual robustness is thin for most of
the project's 13 target languages) via a different source: R-0044 found
existing multilingual watermarking methods fail to remain robust under
translation attacks in medium/low-resource languages, root-caused to
tokenizer subword fragmentation, with no verified logographic-script
(Chinese/Japanese) benchmark found. Separately, this pass surfaced its own
set of AUTHOR-REPORTED, not-yet-independently-verified numeric claims:
R-0040's specific attack-success percentages (piggyback spoofing >90%,
key-based removal 97%+, oracle attack ~3 queries/token), R-0041's
perplexity/MMLU cost figures (9%-2000%+ range, technique-specific), and
R-0044's proposed-fix improvement figures (+0.23 AUC, +37% TPR@1%FPR).
Additionally, two "detection without prior key knowledge" papers and four
other papers (WaterMax, a cross-lingual watermarking fairness audit,
BanglaLorica, an EMNLP 2025 tokenization-inconsistency paper) were
confirmed to exist and be on-topic but were not deep-read in this pass.

### Proposal / Hypothesis

(1) KB-008's proposed default (RESEARCH_ONLY/NOT_SUPPORTED capability
states pending language-specific evidence) should apply to watermarking
and watermark-detection capability states as well as AI-text-detection
ones — this is now a two-source-confirmed gap, not a single-domain
observation. (2) None of the R-0040/R-0041/R-0044 specific figures listed
above should be cited as established fact in any normative document until
independently verified against primary sources.

### Potential Impact

- Scientific Specification §20-22 (per-language capability states,
  watermarking-specific)
- Research (R03 §43.2 follow-up on key-agnostic detection; a dedicated
  pass to read the four not-yet-deep-read papers)
- Research Registry accuracy (R-0040, R-0041, R-0044)

### Candidate Areas

03-scientific-specification, 02-research (R02, R03, R05), 00-project/RESEARCH-REGISTRY.md

### Related Research

R-0040, R-0041, R-0044

### Related Decisions

None yet — this is evidence, not a decision.

### Status

TRIAGED

### Priority

MEDIUM

### Required Action

When R05 is populated, cross-check against this item alongside KB-008. A
follow-up pass should independently verify the R-0040/R-0041/R-0044
figures and deep-read the four identified-but-unread papers listed above
before any of their specific claims are relied upon.

---

## KB-011 — Translation-Based Evasion Is a Distinct, Materially Significant Attack Class Not Yet Reflected in R02/R03

### Source

R05 literature research pass, 2026-08-24
(`docs/02-research/R05-multilingual-linguistic-research.md` §47.3).

### Observation

The R02/R03 literature pass (2026-08-23) documented monolingual
paraphrasing (R-0039) as the dominant watermark-evasion method. The R05
pass found that translation-based evasion (round-trip translation,
translate-and-edit, or translation combined with summarization) is a
separately evidenced attack class, converged on by four independent
sources: CWRA/X-SIR (R-0065, AUC 0.95→0.67), "Uncovering the Hidden
Threat" (R-0066, AUC as low as 0.55-0.57, with a directionality effect —
into-English survives better than out-of-English), ESPERANTO (R-0068,
peer-reviewed, extends the finding to plain AI-detection, not just
watermarking), and the SynthID robustness study (R-0069, F1 0.711-0.819
depending on language). A fifth source, CLSA (R-0067), reports even more
dramatic near-chance AUROC collapse but is a single-author, non-peer-
reviewed, unreplicated preprint and should be weighted accordingly (kept
at INCONCLUSIVE status in the registry).

### Proposal / Hypothesis

R02 §37.2 (Robustness and Attack Evidence) should eventually name
translation-based evasion as a distinct category alongside paraphrasing,
and R03's detector-robustness discussion (§43.4) should note that
detectors and watermarks tested only against monolingual paraphrasing
have not been tested against this separate attack class. This is folded
into DCQ-006's existing scope (propagation pending 03-scientific-
specification/06-security moving past definition phase) rather than
treated as a new queue item.

### Potential Impact

- Research (R02 §6-7, R03 §25 — both currently silent on translation as
  a distinct attack vector)
- Security (06-security, once past definition phase — public
  translation-then-detect pipelines are a realistic, low-effort attack
  surface)

### Candidate Areas

02-research (R02, R03), 06-security

### Related Research

R-0065, R-0066, R-0067, R-0068, R-0069

### Related Decisions

None yet — this is evidence, not a decision.

### Status

TRIAGED

### Priority

MEDIUM

### Required Action

Fold into the R02/R03 update scoped under DCQ-006 when that work is
picked up; until then, any downstream document that asserts watermark or
detector robustness should not assume translation-based evasion has been
accounted for merely because paraphrasing robustness has been discussed.

---

## KB-012 — Factual-Consistency Metrics Are Unvalidated, and Certainty/Hedging Is an Unnamed Preservation Dimension

### Source

R06 literature research pass, 2026-08-24
(`docs/02-research/R06-transformation-preservation-research.md` §58.3,
§58.6).

### Observation

Two distinct gaps surfaced in the R06 pass. (1) An established factual-
consistency metric toolkit exists for summarization (FactCC, SummaC,
QAFactEval, AlignScore — R-0085), but no evidence was found of any of
these, or an LLM-as-judge factuality protocol, being applied specifically
to detector-evasion or watermark-removal paraphrasing — the toolkit and
this project's actual use case have not been bridged by any study found.
(2) A separate, rigorous paper (Belem et al., R-0078) measures certainty/
hedging distortion during LLM rewriting as a dimension explicitly distinct
from factuality — models inflate certainty 1.5-2x more often than they
deflate it, with domain-dependent compounding over iterative rewrites
(medical-domain: 20%→40% over 5 iterations for one tested model). This
dimension (does a rewrite silently change how certain a claim sounds,
independent of whether the claim itself became false) is not currently
named in R06 §3's preservation-dimension list (semantic, factual,
structural, linguistic, stylistic, terminological, numerical,
entity-level, formatting).

### Proposal / Hypothesis

(1) The project should not assume factual-preservation measurement is a
solved problem merely because tools exist elsewhere — a validation study
bridging FactCC/SummaC/QAFactEval/AlignScore (or an LLM-judge protocol)
to this project's transformation/evasion use case is required before any
is adopted as a fidelity metric. (2) Certainty/hedging preservation is a
candidate ninth-or-later preservation dimension for R06 §3 — this is
flagged as a candidate, not incorporated unilaterally, since changing the
project's core preservation-dimension taxonomy is a specification-level
decision.

### Potential Impact

- Research (R06 §7, §41 Factual Consistency; §3 Preservation Dimensions)
- Scientific Specification (S04-fidelity-requirements.md — a candidate
  new fidelity dimension; validation of factuality metrics before
  adoption)

### Candidate Areas

02-research (R06), 03-scientific-specification (S04-fidelity-requirements.md)

### Related Research

R-0078, R-0085

### Related Decisions

None yet — this is evidence, not a decision.

### Status

TRIAGED

### Priority

MEDIUM

### Required Action

When 03-scientific-specification's fidelity requirements (S04) are next
revisited, evaluate whether to add certainty/hedging as a named
preservation dimension, and do not treat FactCC/SummaC/QAFactEval/
AlignScore as validated for this project's use case without a bridging
study.