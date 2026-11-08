# Detector Validation Protocol

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Validation methodology and experimental protocol (Tranche 3)
**Authority:** Validation (Primary for watermark/detector measurement protocols)
**Parent:** `docs/05-validation/VALIDATION-MAP.md` §22–27, §36, §48–50
**Research basis:** `docs/02-research/R02-watermark-research.md` §37, `docs/02-research/R03-watermark-detection-research.md` §43, `docs/02-research/R04-ai-generated-text-detection-research.md` §39, `docs/02-research/R08-benchmark-dataset-research.md` §69 (cited selectively below)
**Requirements basis:** `docs/03-scientific-specification/S02-scientific-requirements.md` §5 (`REQ-WM-001`–`006`), §6 (`REQ-DET-001`–`007`), §7 (`REQ-AID-001`–`004`), §15 (`REQ-EXTSVC-001`–`004`), §19 (`REQ-TEMP-001`–`003`), plus `REQ-STAT-004`/`005`
**Architectural basis:** `docs/04-architecture/VALIDATION-ARCHITECTURE.md` §9 (Missing-Evidence Reporting), §12 (Regression Validation), `docs/04-architecture/EVALUATION-ARCHITECTURE.md` §5 (Benchmark Execution and Detector/Transformation Comparison)
**Related decisions:** `docs/00-project/DECISION-LOG.md` DEC-002 (external detectors are optional evidence sources), DEC-022, DEC-032 (Evaluation Layer), DEC-036 (Tranche roadmap), DEC-037 (Tranche 2 precedent), DEC-038 (this document's execution)

---

# 1. Purpose & Scope

This document formalizes the empirical measurement protocols required to validate watermark mechanisms and AI-text detectors used by this project, satisfying `VALIDATION-MAP.md` §22–27 (Watermark Measurement, Watermark Families, Detector Registry, Detector Independence, Cloud Detector Validation, Detector Drift), §36 (Evaluation Against AI Detectors), and §48–50 (Robustness Testing, Distribution Shift, Longitudinal Validation).

It extends `EVALUATION-ARCHITECTURE.md` §5, which deliberately defers "which specific benchmark corpus, task, or scoring method" to the research layer and does not select one itself. This document is where that deferred selection is made, grounded in the research registry, per `NO-INVENTION-RULES.md`.

It inherits the primary metric convention already established by Tranche 1 (`STATISTICAL-VALIDATION-METHODOLOGY.md`, DEC-036): TPR at a fixed, low FPR, never unconstrained accuracy or headline AUROC alone. `R04-ai-generated-text-detection-research.md` §39.3 (`R-0027`) is the direct justification specific to this document's domain: *"true-positive rate at a fixed 1% false-positive rate can collapse to 0% for some detector/model/task combinations even when the same detector reports high AUROC."* Any detector or watermark result reported under this protocol must use that convention.

Per `NO-INVENTION-RULES.md`'s Missing Information protocol, this document records several named evidence gaps rather than inventing methodology to close them. A summary table is given in §9 before the Governance section.

---

# 2. Watermark Measurement and Watermark Families (§22–23)

Every watermark experiment must record, per `VALIDATION-MAP.md` §22 and `REQ-WM-001`–`003`: watermark family, implementation, version, configuration, language, corpus, text length, transformation, measurement, and uncertainty.

**Family taxonomy** (`REQ-WM-005`, extensibility without redesign) is grounded across token-level/statistical, semantic, cryptographic, and no-cooperation-required families:

- Green-list/red-list statistical schemes (`R-0001`) and the fixed-partition Unigram variant trading context-sensitivity for robustness (`R-0032`);
- Distributional/distortion-free schemes that do not alter the model's output distribution (`R-0013`);
- Semantic-embedding-anchored schemes designed to survive synonym substitution and paraphrasing (SIR, `R-0033`);
- Cryptographic families: undetectable watermarks (`R-0034`) and publicly-detectable, signature-based watermarks requiring no secret for verification (`R-0035`);
- No-generation-time-cooperation watermarking (PostMark, `R-0036`);
- Deployed implementations: SynthID (`R-0014`), Anthropic's own deployed text watermarking (`R-0042`, deployed August 2026).

**Robustness/attack evidence directly measurable under this protocol:**

- `R-0039`: *"a systematic evaluation found detection rates for all evaluated watermarking schemes fell below 0.3 after a single LLM-based paraphrasing pass"* — the strongest single robustness finding in-domain; paraphrase-attack measurement is a required condition for any watermark robustness claim.
- `R-0038` (WaterSeeker): a two-stage anomaly-then-verification approach for localizing watermarked segments in long, partially-watermarked documents — relevant to any mixed-document watermark measurement.
- `R-0041`: a real, technique-dependent detectability/robustness/quality trade-off, with reported perplexity increases ranging from 9% to over 2000% depending on scheme and configuration — any watermark measurement must record which point on this trade-off a given configuration occupies, not merely whether detection succeeded.
- `R-0040`/`R-0015`: spoofing/forgery is a confirmed, structurally-linked attack class; specific percentage figures in `R-0040` are flagged `UNVERIFIED` in the research registry and must not be reported as settled quantities.
- `R-0044`: watermark robustness under translation attack degrades specifically in medium- and low-resource languages, evaluated across 133 languages — directly relevant to this project's 13-language scope; no logographic-script-specific (Chinese/Japanese) benchmark was found and this remains an open gap, not an assumption.

**Scope note:** this is the measurement protocol for whether watermark/detector mechanisms work. It is distinct from, and does not duplicate, `FIDELITY-VALIDATION-PROTOCOL.md` (which governs whether a transformation preserved the text being watermarked).

---

# 3. Detector Registry (§24)

Per `VALIDATION-MAP.md` §24 and `REQ-DET-001`–`004`/`007`, every detector used for research must have a registry entry recording: detector ID, provider, version, interface, language coverage, input constraints, output format, score interpretation, threshold, limitations, date tested, reproducibility status.

The individual detectors this project has research evidence for are registered as `R-XXXX` entries in their own right: zero-shot methods (GLTR `R-0002`, DetectGPT `R-0003`, Fast-DetectGPT `R-0004`, Binoculars `R-0005`); trained classifiers (OpenAI RoBERTa `R-0006`, obsolete; OpenAI's 2023 classifier `R-0007`, withdrawn; RADAR `R-0008`); commercial services (GPTZero `R-0009`, Pangram `R-0010`); watermark-based detectors (`R-0001`, `R-0013`, `R-0014`).

**Evidence gap, recorded rather than filled:** `R03-watermark-detection-research.md` §43's Literature Findings define the *methodology* for what a registry entry should record (identity, versioning — §3–4 of that document), but register no `R-XXXX` citation specifically studying detector-registry practice as its own object of research (as distinct from the detector methods themselves, which are well-grounded individually above). This document does not invent such a citation; detector registry entries are populated per the methodology already specified, without a dedicated empirical study of registry practice to cite.

---

# 4. Detector Independence (§25)

Per `VALIDATION-MAP.md` §25 and `REQ-DET-005`: where multiple detectors are used, results must remain separate, and the system must not silently collapse "Detector A = positive, Detector B = negative" into "overall = uncertain" without preserving the original observations. Aggregation logic, where used, must be explicit and versioned.

**Grounded, qualitatively:** `R03-watermark-detection-research.md` §43.5 states explicitly: *"the detector families registered across R-0001, R-0013, R-0014, R-0032 through R-0036 share a common lineage (several build directly on the green-list/red-list idea) and should NOT be treated as independent evidence sources without accounting for that shared ancestry."* Cryptographic detection (`R-0034`, `R-0035`) is the most methodologically distinct family from the statistical ones and is the preferred second, independent signal when a multi-detector comparison is required.

**Evidence gap, recorded rather than filled:** the same section states directly, in its own words: *"A full independence assessment (which specific pairs of detectors share training data, benchmarks, or source-paper lineage) was not performed in this pass and remains open."* This protocol therefore requires that any claim of "independent" detector agreement be qualified as resting on the lineage-grouping above, not on a quantitative pairwise independence analysis — which does not yet exist in the research layer. This is a candidate for a dedicated follow-up research task (flagged, not performed, by `R03` itself); this document does not add it to `KNOWLEDGE-BACKLOG.md` unilaterally.

---

# 5. Cloud Detector Validation (§26)

Per `VALIDATION-MAP.md` §26 and `REQ-EXTSVC-001`–`004`: for every cloud/external detector request, record where possible: service, endpoint/product, version, request configuration, timestamp, language, text length, returned score, returned classification, errors. Cloud results are observations from a changing external system, never a local capability's substitute (`DECISION-LOG.md` DEC-002: *"External detectors may be integrated through explicit adapters but are not part of the mandatory offline core"*).

**Evidence gap, recorded rather than filled:** the only research-layer grounding found for cloud/external detector behavior specifically is the oracle-query / API-attack-surface concern (`R03` §43.4, tied to `R-0015` and `R-0040`'s spoofing-via-API-query findings) — i.e., evidence about exposing a detection API as an attack surface, not evidence about cloud-detector-service measurement behavior or drift over time. No `R-XXXX` citation measuring cloud-detector-service drift specifically was found in the research layer available to this document. `REQ-EXTSVC-003` (failure isolation) and `REQ-REPRO-005` (external-service mutability may make exact reproduction impossible) remain the governing normative requirements for this gap; this document does not invent a cloud-drift-measurement study to fill it.

---

# 6. Detector Drift (§27)

Per `VALIDATION-MAP.md` §27: external detectors may change without notice; the project should periodically evaluate score distribution, threshold behavior, language behavior, response format, and API behavior. A detector update may invalidate direct comparisons with earlier results.

**Grounded:** `R04-ai-generated-text-detection-research.md` §39.3 (`R-0028`) supplies the mechanistic cause most directly relevant to drift measurement: *"detectors have been shown to respond to statistical fingerprints of a model's post-training procedure... rather than an invariant 'AI-ness' property — the same underlying base model scores as 'human' before instruction-tuning and 'AI' after."* This means a detector's measured behavior can shift not only because the detector changed, but because the population of generating models it is tested against changed — both must be tracked as separate, explicit variables per `REQ-TEMP-001`–`003` (observation timestamp, methodology temporal context, historical stability).

`VALIDATION-ARCHITECTURE.md` §12 (Regression Validation) supplies the architectural mechanism this document reuses: a detector's previously-passing measurement outcomes must be re-checked, by language and dimension, before any claim of continued validity is relied upon after a detector or model-population change.

---

# 7. Evaluation Against AI Detectors (§36)

Per `VALIDATION-MAP.md` §36: AI detector results may be included as research measurements but must not be treated as definitive evidence of authorship — represented as `OBSERVATION`, never `GROUND TRUTH` (`REQ-DET-005`).

This principle is the same one that grounds this document's adoption of TPR@fixed-FPR (§1, `R-0027`) and extends it to the interpretation layer: a detector classification is an observation about a text sample under a specific detector/version/configuration, never a settled determination of how the sample was produced. `REQ-AID-003` (document what detector output represents before statistical use) and `REQ-AID-004` (preserve detector uncertainty/calibration where available) govern this; `REQ-AID-004`'s own note records that non-native-writer detection bias (`R-0022`) is a known, evidenced confounder that must not be ignored when interpreting a detector's classification as evidence.

---

# 8. Robustness Testing, Distribution Shift, and Longitudinal Validation (§48–50)

## 8.1 Robustness Testing (§48)

Robustness experiments test controlled changes: punctuation, spelling, formatting, sentence boundaries, translation, back-translation, editing, length changes — the transformation under study must be clearly defined (`REQ-TRANS-001`–`006`).

**Paraphrase robustness — strongly grounded:** `R-0024` (`R04` §39.3): *"DIPPER paraphrasing drops DetectGPT's detection accuracy from 70.3% to 4.6% at a fixed 1% false-positive rate... confirmed directly from the primary paper."* Cross-references `R02`'s `R-0039` (§2 above). Paraphrase-attack measurement is accordingly a required, not optional, robustness condition for any detector or watermark claim.

**Translation robustness — grounded, with a status caveat that must be carried forward accurately.** `R04` §39.3 grounds translation as a false-positive source for AI-text detection directly in its own domain (`R-0031`, corroborated by `R-0012`: *"round-trip machine translation raised false-positive rates on genuinely human text from ~0.4% to ~28%"*). However, the more specific watermark/detector translation-evasion findings that `VALIDATION-MAP.md` §76 itself names for this Tranche (CWRA/X-SIR, "Uncovering the Hidden Threat," ESPERANTO, the SynthID robustness study — referenced in the roadmap as `R-0065`/`R-0066`) are not yet present as native citations inside `R02`/`R03`'s own Literature Findings sections. They currently exist in the corpus only via `KNOWLEDGE-BACKLOG.md` KB-011, which is explicitly status `TRIAGED` and states its own required propagation into `R02`/`R03` *"remains not yet performed."* Per `NO-INVENTION-RULES.md`'s Ambiguous/Missing-Information protocol, this document records that status accurately rather than citing those findings as if they were already native `R02`/`R03` evidence: translation-evasion measurement for watermarks specifically should be treated as **evidenced in the corpus but not yet fully integrated into the research layer this document otherwise draws from** — a standing item for KB-011's own required action, not something this document resolves.

## 8.2 Distribution Shift (§49)

Validation must consider whether results generalize across domains, authors, text lengths, languages, topics, and document types (`REQ-LANG-001`–`003`). A result on one narrow corpus must not automatically generalize.

**Grounded for writer-population shift:** non-native-writer false-positive bias (`R-0022`) and race/ELL bias (`R-0023`, *"non-White ELL essays disproportionately flagged... in 7 of 16 tested detectors vs. 1 of 16 for the reverse"*) are both confirmed confounders requiring stratified reporting, consistent with Tranche 1's confounder-control framework.

**Evidence gap, recorded rather than filled:** cross-language distribution shift specifically is confirmed thin by the research layer itself — `R04` §39.4: *"the only language-specific academic study found was a small Urdu case study (R-0029), not one of the project's 13 target languages. No independently verified, non-vendor study was found for German, Italian, Portuguese, Russian, Japanese, Polish, Dutch, Turkish, or Indonesian"* — nine of this project's thirteen target languages. Any cross-language detector/watermark generalization claim made under this protocol for those nine languages must be reported as `not measurable`/`unsupported` per `VALIDATION-ARCHITECTURE.md` §9's missing-evidence discipline, not inferred from the four languages with evidence.

## 8.3 Longitudinal Validation (§50)

Important capabilities should be evaluated over time where practical, particularly for external detectors, watermark implementations, language models, cloud services, and changing datasets; historical measurements should remain available (`REQ-TEMP-003`).

**Evidence gap, recorded rather than filled:** no dedicated longitudinal-study `R-XXXX` citation (i.e., a study specifically measuring detector or watermark decay over calendar time) was found in `R02`, `R03`, or `R04`. Grounding is indirect only: the drift mechanism (`R-0028`, §6 above) explains *why* longitudinal decay should be expected, and `REQ-TEMP-001`–`003` plus `VALIDATION-ARCHITECTURE.md` §12 supply the normative/architectural mechanism for tracking it, but no study measuring the actual rate or shape of that decay over time exists in the research layer available to this document. This protocol requires historical measurement retention (per `REQ-TEMP-003`) precisely because this gap exists — the absence of a longitudinal study is itself the reason not to discard old measurements.

---

# 9. Benchmark Evaluation and Dataset Governance

Standardized benchmark evaluation is grounded primarily through `R04-ai-generated-text-detection-research.md` §39.2: named, citable benchmarks include HC3 (`R-0016`), TuringBench (`R-0017`, temporally dated), MGTBench (`R-0018`), M4 (`R-0019`, multilingual by design), RAID (`R-0020`, purpose-built for robustness stress-testing), and BLUFF (`R-0021`, low-resource-language-focused, flagged `INCONCLUSIVE` pending primary-source verification). `R04` §39.2 states directly: *"RAID (R-0020) is the strongest existing candidate to adopt for the project's own robustness evaluation profile rather than building an equivalent benchmark from scratch."* This document adopts that recommendation: RAID is this protocol's preferred standardized benchmark where a benchmark-level robustness evaluation is required.

**Citation-precision note, recorded rather than smoothed over:** `VALIDATION-MAP.md` §76 names "RAID, M4GT-Bench" together as the benchmarks this Tranche governs. RAID has its own `R-0020` entry; **M4GT-Bench does not** — it appears in the corpus only as M4's (`R-0019`) successor shared-task lineage (`R08-benchmark-dataset-research.md` §69.5: *"M4's lineage into M4GT-Bench/SemEval-2024 Task 8 functions as a new benchmark built on the original's methodology rather than an in-place refresh"*), without an independent research-registry citation of its own. This document treats M4GT-Bench accordingly: usable via its M4 lineage, but not yet independently evidenced at the same citation standard as RAID — a gap for the research layer to close with its own `R-XXXX` entry, not one this document closes by assertion.

**Dataset versioning — one real example, not a general pattern:** `R08` §69.5 finds exactly one confirmed benchmark refresh with a stated rationale: MULTITuDE → MULTITuDEv2 (`R-0049`, 2023-10 → 2024-09-27, adding ten authorship-obfuscation methods). RAID's own tooling package has frequent releases, but these are confirmed to be software/tooling releases, not dataset content refreshes — the two must not be conflated.

**Train/test separation for detector evaluation — zero grounding, recorded as a gap:** `R08`'s own methodology scope (§31–40) covers train/test/holdout separation practice, but its populated Literature Findings (§69) contains no corresponding citation addressing this specific sub-topic for AI-detection benchmarks. This document does not invent a train/test-separation finding to fill that gap; benchmark evaluations under this protocol must apply `VALIDATION-MAP.md` §8's general train/test separation principle without a domain-specific citation to ground the practice beyond that general principle.

**Deduplication and contamination — confirmed gaps, inherited from `R08`:** no evidence was found of formal near-duplicate detection in RAID, MGTBench, M4, or DetectRL; no evidence was found of n-gram or embedding-overlap contamination detection having been applied to any named AI-detection benchmark (`R08` §69.3–69.4). Where this protocol relies on one of these benchmarks, the absence of a confirmed deduplication/contamination pass on that benchmark must be disclosed alongside any result, not silently assumed clean.

**Summary of named evidence gaps this document records rather than fills (consolidated from §3–9 above):**

| Area | Status |
|---|---|
| Detector-registry-as-practice | No dedicated `R-XXXX` citation; methodology-only |
| Detector independence (pairwise/quantitative) | Qualitative lineage grounded; quantitative analysis confirmed "not performed" by `R03` itself |
| Cloud/external detector drift | Only attack-surface evidence found; no drift-measurement study |
| Cross-language distribution shift | Confirmed thin for 9 of 13 target languages (`R04` §39.4) |
| Longitudinal/temporal detector decay | No dedicated study; mechanism-only grounding via `R-0028` |
| M4GT-Bench as an independent benchmark | No own `R-XXXX`; available only via M4's (`R-0019`) lineage |
| Train/test separation for detector benchmarks | No populated citation in `R08` §69 |
| Watermark translation-evasion in `R02`/`R03` natively | Evidenced in corpus via `KNOWLEDGE-BACKLOG.md` KB-011 only; propagation into `R02`/`R03` confirmed not yet performed |

These are candidates for future `KNOWLEDGE-BACKLOG.md` entries or dedicated follow-up research tasks; this document flags them and does not add them to that backlog unilaterally, consistent with the practice established in `DECISION-LOG.md` DEC-037 for Tranche 2's own evidence gap.

---

# 10. Governance & Traceability

No threshold, benchmark selection, or detector-comparison result produced under this protocol may be selected post-hoc to favor a particular conclusion (`NO-INVENTION-RULES.md` Forbidden Behaviors; `S01-system-objectives.md`/`P00-project-governance.md` discipline already cited by Tranches 1–2).

Raw detector/watermark observations must be preserved separately from any derived or aggregated score, per `REQ-DET-004` and `EVALUATION-ARCHITECTURE.md` §6 (*"derived scores must never replace the underlying observations"*).

A detector classification or watermark detection result is `OBSERVATION`, never `GROUND TRUTH` (§7 above), and must be reported using the `PASS`/`FAIL`/`INCONCLUSIVE`/`UNAVAILABLE` confidence states of `VALIDATION-MAP.md` §46, with missing evidence reported as `not measurable`/`unsupported` rather than omitted, per `VALIDATION-ARCHITECTURE.md` §9.

Any named evidence gap in §3–9 above that is later closed by new research must update this document's citations explicitly; it must not be silently assumed closed because a later document references the dimension in passing.

This document feeds `VALIDATION-GATES.md` (Tranche 4): the Capability Validation Gate's requirement that "its benchmark is defined" and "its evidence is documented" (`VALIDATION-MAP.md` §55) for any detector- or watermark-dependent capability is satisfied by this document's protocol, not restated by it.
