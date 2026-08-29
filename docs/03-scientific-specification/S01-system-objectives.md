# S01 — System Objectives

**Status:** NORMATIVE / FOUNDATIONAL  
**Version:** 0.1  
**Document type:** Scientific system objectives  
**Parent:** `docs/03-scientific-specification/SPECIFICATION-MAP.md`

---

# 1. Purpose

This document defines the normative scientific objectives of the Text
Integrity Research system.

The system is intended to provide a reproducible experimental framework
for studying:

- textual watermarking;
- watermark detection;
- AI-generated-text detection;
- multilingual linguistic effects;
- textual transformations;
- preservation of textual properties;
- detector and watermark robustness;
- temporal evolution of detection technologies;
- statistical evaluation of experimental results.

The system is a scientific research and evaluation platform.

It must not assume that any currently known detector, watermark or
evaluation methodology is permanent or universally valid.

---

# 2. Primary Scientific Objective

The primary objective is to establish a reproducible methodology for
measuring how textual transformations affect:

1. linguistic characteristics;
2. semantic content;
3. stylistic characteristics;
4. authorship-related signals;
5. watermark detectability;
6. AI-generation detection signals;
7. readability and naturalness;
8. cross-language behaviour;
9. robustness under changing evaluation methods.

The system must distinguish measured evidence from interpretation.

---

# 3. Research Questions

The system shall support investigation of at least the following questions.

### RQ-01 — Watermark Behaviour

How do different textual watermarking families behave across languages,
domains, text lengths and transformation conditions?

### RQ-02 — Detection Behaviour

How reliably can known watermark detectors identify corresponding
watermarks under controlled experimental conditions?

### RQ-03 — AI-Detection Behaviour

How do AI-generated-text detectors behave across languages, models,
domains, text lengths and transformation conditions?

### RQ-04 — Multilingual Effects

Which linguistic properties cause materially different behaviour between
languages?

### RQ-05 — Transformation Effects

Which transformations alter measurable textual properties, and to what
extent?

### RQ-06 — Preservation

How much semantic, factual, stylistic and structural information is
preserved after a transformation?

### RQ-07 — Detector Dependence

To what extent are experimental conclusions dependent on a particular
detector, detector version, watermark family or evaluation protocol?

### RQ-08 — Temporal Stability

How stable are experimental conclusions as detectors, watermarking
methods, language models and evaluation methodologies evolve?

### RQ-09 — False Positives and False Negatives

What false-positive and false-negative behaviour occurs under controlled
conditions?

### RQ-10 — Reproducibility

Can independent execution of the same experiment reproduce the reported
result within predefined statistical tolerances?

---

# 4. Scientific Non-Goals

The system shall not define scientific success as:

- defeating a particular detector;
- producing text guaranteed to evade detection;
- proving that a text is permanently undetectable;
- proving that a detector is universally reliable;
- optimizing against a single detector while ignoring others;
- treating one detector's output as ground truth;
- treating one watermark family as representative of all watermarking
  methodologies.

A detector result is an observation produced by a specific instrument,
version and protocol.

---

# 5. Measurement Principle

Every experimental result shall be associated, where applicable, with:

- source text identifier;
- language;
- text origin;
- generation method;
- transformation configuration;
- watermark condition;
- detector identity;
- detector version;
- detector configuration;
- dataset version;
- experiment version;
- timestamp;
- evaluation protocol;
- statistical method;
- confidence or uncertainty information.

A result without sufficient provenance shall not be treated as fully
reproducible evidence.

---

# 6. Separation of Concerns

The scientific system shall distinguish at least:

### 6.1 Text Generation

Creation of controlled source material.

### 6.2 Text Transformation

Application of a defined transformation to experimental material.

### 6.3 Text Evaluation

Measurement of linguistic, semantic, stylistic and structural properties.

### 6.4 Watermark Evaluation

Measurement of behaviour associated with a defined watermark methodology.

### 6.5 AI-Detection Evaluation

Measurement of behaviour associated with a defined AI-text detector.

### 6.6 Statistical Evaluation

Aggregation and interpretation of experimental observations.

### 6.7 Reporting

Generation of reproducible experimental reports.

No component shall silently combine these responsibilities in a way that
makes causal interpretation impossible.

---

# 7. Multilingual Objective

The system shall support multilingual experimentation without assuming
that an identical methodology produces equivalent results across
languages.

The initial language set shall include:

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

Additional languages shall be addable without redesigning the scientific
core.

Language-specific findings shall be represented explicitly rather than
being hidden inside aggregate metrics.

---

# 8. Language Qualification

A language shall not be considered scientifically supported merely because
the system can process its characters.

For each supported language, the research framework should establish,
where evidence exists:

- tokenizer behaviour;
- segmentation behaviour;
- normalization requirements;
- morphology-related considerations;
- script characteristics;
- punctuation conventions;
- sentence-length characteristics;
- available datasets;
- available detectors;
- available watermark research;
- known benchmark limitations.

Insufficient evidence shall be recorded as a research limitation.

---

# 9. Preservation Objectives

For every transformation experiment, preservation shall be evaluated
independently across multiple dimensions.

At minimum:

- semantic preservation;
- factual preservation;
- structural preservation;
- stylistic preservation;
- linguistic preservation;
- readability;
- length variation;
- lexical variation.

No single similarity score shall be considered sufficient evidence of
overall preservation.

---

# 10. Minimal-Change Objective

Where a transformation is experimentally evaluated, the preferred
transformation objective is:

> achieve the experimental condition with the smallest measurable change
> to the source text consistent with the predefined experimental protocol.

"Minimal" must be operationalized through measurable metrics.

The system shall not use an undefined qualitative notion of minimality.

---

# 11. Human-Text Characteristics

The project may investigate characteristics associated with human-authored
and AI-generated text.

However, no universal definition of "human-like" shall be assumed.

Human-authored corpora shall be treated as empirical reference material,
subject to:

- corpus provenance;
- demographic and domain limitations;
- temporal limitations;
- editorial effects;
- contamination risks;
- sampling bias.

---

# 12. Detector as Measurement Instrument

Detectors shall be treated as measurement instruments rather than
authoritative truth sources.

For every detector, the system should record:

- identity;
- version;
- provider or implementation;
- interface;
- input constraints;
- supported languages;
- output format;
- scoring interpretation;
- calibration information;
- known limitations;
- observed failure modes;
- date of evaluation.

Detector outputs shall not be silently converted into binary truth labels.

---

# 13. Watermark as Experimental Condition

Watermarks shall be represented as experimental conditions with explicit
metadata.

Where possible, the system shall record:

- watermark family;
- implementation;
- generation model;
- configuration;
- detector;
- detection threshold;
- generation parameters;
- text length;
- language;
- source corpus;
- experimental version.

The existence of a watermark shall not be inferred solely from the
absence or presence of a detector response.

---

# 14. Multi-Instrument Principle

Important scientific conclusions shall not depend unnecessarily on a
single detector or single metric.

Where multiple independent instruments exist, experiments should compare
them.

Disagreement between instruments is itself a scientific observation and
shall be retained rather than normalized away.

---

# 15. Temporal Validity

Scientific conclusions are time-dependent.

The system shall therefore support:

- detector versioning;
- watermark versioning;
- dataset versioning;
- benchmark versioning;
- experiment versioning;
- dated results;
- supersession relationships.

A new detector or watermark methodology shall not silently overwrite
historical results.

Historical observations must remain identifiable.

---

# 16. Experimental Reproducibility

A completed experiment shall be reproducible from its recorded:

- inputs;
- configuration;
- software version;
- dependency versions;
- detector metadata;
- dataset versions;
- random seeds where applicable;
- evaluation protocol;
- statistical procedure.

If exact reproduction is impossible because an external service changed,
the limitation shall be explicitly recorded.

---

# 17. Offline Core

The scientific core shall be designed so that the main experimental
pipeline can execute without mandatory dependence on generative AI.

External services may be used for specifically defined measurements,
including detector evaluation, provided that:

- their role is explicitly documented;
- transmitted data is controlled;
- the service response is preserved where legally and technically
  possible;
- the service identity and version/date are recorded;
- external failure does not corrupt local experimental state.

---

# 18. Data Budget

The complete local project shall be designed to operate within an
approximately 30 GB data budget unless a later architectural decision
explicitly changes this constraint.

The budget includes, where applicable:

- datasets;
- derived datasets;
- model artifacts;
- detector metadata;
- benchmark material;
- experiment outputs;
- logs;
- reproducibility artifacts.

Large external resources should not be duplicated locally unless their
scientific value justifies the storage cost.

---

# 19. Zero-Cost Research Tooling

The research framework should prefer freely available tooling and public
scientific resources.

A component shall not be selected solely because it is free.

Selection must also consider:

- scientific validity;
- reproducibility;
- licensing;
- maintenance;
- data provenance;
- compatibility;
- security;
- long-term availability.

Commercial or paid services may be evaluated as external instruments when
scientifically justified, but they shall not become an implicit mandatory
dependency of the offline scientific core.

---

# 20. Extensibility Objective

The architecture shall allow new:

- languages;
- datasets;
- detectors;
- watermark methodologies;
- transformations;
- evaluation metrics;
- statistical methods;
- benchmark suites;
- external measurement services.

to be introduced without rewriting unrelated components.

Experimental capabilities should be registered and versioned.

---

# 21. Deprecation Objective

Research methodologies may become obsolete.

The system shall therefore support:

DISCOVERED
→ EXPERIMENTAL
→ VALIDATED
→ ACTIVE
→ DEPRECATED
→ RETIRED

Retirement shall preserve historical evidence.

Removing an obsolete component from active execution must not erase the
scientific record showing why it was retired.

---

# 22. Unknown and Emerging Methods

The system shall explicitly support unknown or newly emerging detector and
watermark methodologies.

When a new method becomes known, it shall enter through the research
lifecycle rather than being manually patched into unrelated components.

The lifecycle shall include:

1. discovery;
2. identification;
3. evidence assessment;
4. compatibility assessment;
5. experimental integration;
6. validation;
7. activation;
8. monitoring;
9. deprecation when obsolete.

---

# 23. Statistical Integrity

The system shall distinguish:

- raw observations;
- derived metrics;
- aggregate statistics;
- confidence intervals;
- hypothesis tests;
- exploratory findings;
- confirmatory findings.

Multiple comparisons, selection effects and detector-specific bias shall
be considered where scientifically relevant.

The system shall not report a single aggregate score as proof of universal
performance.

---

# 24. Negative Results

Negative results are first-class scientific evidence.

The project shall preserve findings such as:

- detector failure;
- watermark non-detection;
- unexpected detector disagreement;
- transformation-induced semantic damage;
- language-specific degradation;
- benchmark invalidity;
- inability to reproduce a published result.

Negative results must not be removed merely because they make a system
appear less effective.

---

# 25. Uncertainty

Where a measurement has meaningful uncertainty, the uncertainty shall be
reported.

The system shall avoid presenting:

- estimated values as exact;
- detector scores as universal probabilities;
- benchmark results as universal guarantees;
- experimental observations as permanent truths.

---

# 26. Traceability

Every substantive scientific claim used by the specification should be
traceable to one or more:

- peer-reviewed publications;
- preprints;
- benchmark documentation;
- dataset documentation;
- detector documentation;
- reproducible experiments;
- project-generated evidence.

Claims without adequate evidence shall be marked accordingly.

---

# 27. Scientific Update Rule

New evidence shall not silently rewrite historical conclusions.

Instead:

1. record the new evidence;
2. identify affected claims;
3. assess compatibility;
4. update the relevant specification;
5. record the decision;
6. update affected validation criteria;
7. preserve the historical state.

This creates an auditable evolution of scientific knowledge.

---

# 28. Success Criteria

The scientific system shall be considered successful when it can:

- execute controlled experiments reproducibly;
- compare multiple watermark methodologies;
- compare multiple detection methodologies;
- evaluate multilingual behaviour;
- quantify transformation effects;
- measure preservation across multiple dimensions;
- detect methodological disagreement;
- preserve negative results;
- track temporal changes;
- incorporate new methodologies;
- retire obsolete methodologies without losing historical evidence;
- generate auditable experimental reports.

Success shall be evaluated against explicit validation criteria rather than
subjective impressions.

---

# 29. Known Limitations

The following limitations are expected to remain open research questions:

- no detector can be assumed universally reliable;
- no watermark family can be assumed representative of all future
  watermarking methods;
- language coverage may be asymmetric;
- external detectors may change without notice;
- historical experiments may become difficult to reproduce;
- benchmark datasets may contain biases;
- semantic similarity metrics may disagree with human judgment;
- stylistic similarity is difficult to measure universally;
- detector outputs may be proprietary or insufficiently documented.

These limitations must be represented explicitly in validation reports.

---

# 30. Relationship to Other Specifications

This document provides objectives.

It does not define:

- detailed algorithms;
- implementation architecture;
- specific detector adapters;
- exact benchmark datasets;
- production deployment procedures;
- detailed statistical formulas.

Those belong to downstream specification documents.

---

# 31. Requirement Traceability

The following requirement families shall be traceable from this document
into downstream specifications:

| Requirement family | Identifier |
|---|---|
| Scientific reproducibility | OBJ-REPRO |
| Multilingual evaluation | OBJ-MULTI |
| Watermark research | OBJ-WM |
| Detector research | OBJ-DET |
| Transformation evaluation | OBJ-TRANS |
| Preservation | OBJ-PRES |
| Statistical integrity | OBJ-STAT |
| Temporal evolution | OBJ-TEMP |
| Extensibility | OBJ-EXT |
| Deprecation | OBJ-LIFE |
| Provenance | OBJ-PROV |
| Offline scientific core | OBJ-OFFLINE |

---

# 32. Completion Criteria

S01 is complete when:

- all objective families are defined;
- objectives are testable downstream;
- scientific non-goals are explicit;
- multilingual scope is documented;
- preservation dimensions are defined;
- detector and watermark measurements are separated;
- temporal evolution is addressed;
- reproducibility requirements are explicit;
- extensibility and lifecycle requirements are explicit;
- limitations are recorded;
- downstream traceability identifiers exist.

---

# 33. Final Principle

The project shall optimize for scientific validity, reproducibility,
traceability and long-term adaptability.

No individual detector, watermark methodology, language, dataset,
transformation, metric or external service shall be treated as the final
authority on textual provenance.

The system must remain capable of learning from new evidence without
destroying or rewriting the evidence that came before it.