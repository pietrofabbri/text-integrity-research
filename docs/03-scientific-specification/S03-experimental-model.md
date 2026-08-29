# S03 — Experimental Model & Measurement Framework

**Status:** NORMATIVE / SCIENTIFIC  
**Version:** 0.1  
**Document type:** Experimental model specification  
**Parent:** `docs/03-scientific-specification/SPECIFICATION-MAP.md`  
**Depends on:** `S01-system-objectives.md`, `S02-scientific-requirements.md`

---

# 1. Purpose

This document defines the abstract experimental model used by the
scientific system.

It establishes:

- experimental units;
- variables;
- conditions;
- controls;
- transformations;
- measurements;
- observations;
- derived metrics;
- comparisons;
- statistical analysis;
- provenance;
- reproducibility boundaries.

The purpose is to ensure that experiments can be described consistently
before implementation details are selected.

---

# 2. Fundamental Experimental Unit

The fundamental unit of experimentation is an **Experiment**.

An Experiment consists of:

1. source material;
2. experimental configuration;
3. execution environment;
4. optional transformation pipeline;
5. measurement instruments;
6. raw observations;
7. derived measurements;
8. statistical analysis;
9. provenance metadata.

An Experiment must have a unique identifier.

---

# 3. Text Sample

A Text Sample is a uniquely identifiable textual artifact used by an
experiment.

A sample shall have, where applicable:

- sample identifier;
- source identifier;
- language;
- domain;
- provenance;
- creation date;
- text version;
- character count;
- token count under the declared tokenizer;
- sentence count;
- paragraph count;
- source condition.

The exact text shall be preserved whenever licensing and data-handling
constraints permit.

---

# 4. Source Conditions

A source sample shall have an explicit origin classification.

Possible classifications include:

- human-authored;
- AI-generated;
- mixed-origin;
- transformed;
- synthetic benchmark;
- unknown;
- other documented category.

The classification must not be silently inferred from detector output.

---

# 5. Experimental Variables

Variables shall be divided into:

### Independent Variables

Variables intentionally manipulated by the experiment.

Examples include:

- language;
- generation method;
- watermark condition;
- transformation;
- transformation configuration;
- text length;
- domain;
- detector;
- detector configuration.

### Dependent Variables

Measurements observed as experimental outcomes.

Examples include:

- detector score;
- watermark detection result;
- semantic similarity;
- structural similarity;
- linguistic metrics;
- stylistic metrics;
- readability;
- length change.

### Controlled Variables

Variables held constant to reduce confounding.

Examples include:

- source corpus;
- generation configuration;
- evaluation protocol;
- tokenizer;
- benchmark version.

### Nuisance Variables

Variables that may affect measurements but cannot always be controlled.

Examples include:

- external-service changes;
- provider-side model updates;
- dataset artifacts;
- infrastructure variation.

Nuisance variables shall be documented when known.

---

# 6. Experimental Condition

An Experimental Condition is the complete declared state under which a
sample is evaluated.

A condition may include:

- language;
- source type;
- generation method;
- watermark methodology;
- transformation pipeline;
- detector;
- evaluation parameters;
- dataset version.

Two observations shall not be treated as directly comparable if a
scientifically relevant condition differs unless the difference is
explicitly modeled.

---

# 7. Baseline

Every comparative experiment should define an explicit baseline.

A baseline represents the reference condition against which changes are
measured.

Examples include:

- untransformed source;
- control corpus;
- non-watermarked generation;
- reference detector configuration.

The baseline must be identified by an immutable experiment or sample
identifier.

---

# 8. Control Conditions

Where scientifically appropriate, an experiment should include one or more
control conditions.

Controls may be used to estimate:

- detector false-positive behaviour;
- measurement noise;
- transformation-independent variation;
- language-specific effects;
- dataset effects.

The absence of a control shall be documented when a control is impractical.

---

# 9. Transformation Model

A transformation is modeled as:

Source
→ Transformation Configuration
→ Result

A transformation must not overwrite the identity of the source.

The result receives its own identity and provenance relationship.

---

# 10. Transformation Chain

Multiple transformations form an ordered chain:

T0
→ T1
→ T2
→ ...
→ Tn

For each transformation the system shall preserve:

- transformation identifier;
- version;
- configuration;
- input identifier;
- output identifier;
- execution metadata.

This permits each transformation's effect to be analyzed separately.

---

# 11. Measurement Instrument

A Measurement Instrument is any mechanism that produces an observation
about an experimental artifact.

Examples include:

- watermark detectors;
- AI-text detectors;
- semantic similarity measures;
- linguistic analyzers;
- readability metrics;
- structural analyzers;
- human evaluation protocols.

An instrument is not equivalent to ground truth.

---

# 12. Instrument Identity

Every instrument measurement shall identify:

- instrument identifier;
- implementation/provider;
- version where available;
- configuration;
- timestamp;
- input artifact;
- output representation.

For external services, service metadata shall be retained whenever
available.

---

# 13. Raw Observation

A Raw Observation is the direct output of a measurement instrument before
scientific interpretation.

Raw observations shall be preserved separately from derived metrics.

Examples include:

- detector score;
- detector label;
- probability-like value;
- watermark detection statistic;
- similarity score;
- linguistic measurement;
- API response.

---

# 14. Derived Measurement

A Derived Measurement is calculated from one or more raw observations.

Examples include:

- mean;
- median;
- variance;
- confidence interval;
- effect size;
- false-positive rate;
- false-negative rate;
- correlation;
- language-specific aggregate.

Every derived measurement shall be traceable to the observations from which
it was calculated.

---

# 15. Ground Truth

Ground truth shall be explicitly defined for each experiment where
possible.

Possible categories include:

- experimentally controlled condition;
- verified corpus provenance;
- known generation condition;
- manually established reference;
- unavailable.

Detector output shall not automatically become ground truth.

When ground truth is uncertain, uncertainty shall be represented explicitly.

---

# 16. Observation vs Interpretation

The system shall distinguish:

**Observation**

What an instrument actually returned.

**Measurement**

A quantified property derived from observations.

**Interpretation**

A scientific conclusion drawn from measurements.

**Hypothesis**

A proposition requiring further testing.

**Assumption**

A proposition accepted provisionally for the experiment.

These categories shall not be silently conflated.

---

# 17. Comparison Model

Comparisons shall explicitly identify:

- comparison groups;
- baseline;
- dependent variable;
- independent variable;
- relevant controls;
- statistical method;
- effect measure.

A comparison without sufficient metadata shall be classified as incomplete.

---

# 18. Multilingual Experimental Model

Language is an explicit experimental variable.

Experiments involving multiple languages shall permit analysis at both:

1. language-specific level;
2. cross-language aggregate level.

Aggregate results must disclose the languages contributing to the result.

Language imbalance shall be measurable and reported where relevant.

---

# 19. Text Length

Text length shall be treated as an explicit experimental variable when
detector or watermark performance may depend on it.

Length should be represented using multiple measures where appropriate:

- characters;
- words;
- tokens;
- sentences.

The tokenizer used for token-based measurements must be recorded.

---

# 20. Domain

Text domain shall be represented explicitly where domain may influence
experimental behaviour.

Possible domains include:

- academic;
- journalistic;
- technical;
- literary;
- conversational;
- instructional;
- general web text.

The domain taxonomy may evolve.

---

# 21. Replication Model

The system shall distinguish:

### Technical Replication

Repeating an experiment using the same configuration and environment.

### Independent Replication

Repeating the experiment using independently prepared material or an
independent implementation.

### Cross-Method Replication

Testing whether the observed relationship persists using another valid
methodology.

Replication type shall be recorded.

---

# 22. Randomization

Where randomization is used, the system shall record:

- randomization method;
- random seed where applicable;
- randomized variables;
- allocation procedure.

If randomization is not used, that fact should be documented when it
affects interpretation.

---

# 23. Sampling

Sampling procedures shall be explicit.

The system should record:

- population;
- sampling frame;
- inclusion criteria;
- exclusion criteria;
- sample size;
- sampling method;
- known selection limitations.

Convenience samples shall not be represented as universally
representative samples.

---

# 24. Statistical Comparison

Statistical comparison shall be selected according to:

- variable type;
- experimental design;
- sample structure;
- distributional assumptions;
- dependence between observations;
- research question.

The framework shall avoid choosing a statistical method solely because it
produces a preferred result.

---

# 25. Multiple Testing

When multiple hypotheses or detector comparisons are evaluated, the
experiment shall record the multiplicity structure.

Where scientifically appropriate, the analysis shall apply a suitable
multiple-comparison methodology.

---

# 26. Effect Size

Where comparison is meaningful, effect size should be reported in addition
to statistical significance.

A small p-value alone shall not be treated as evidence of practical
importance.

---

# 27. Confidence and Uncertainty

Measurements shall report uncertainty using an appropriate representation
where applicable.

Possible representations include:

- confidence intervals;
- credible intervals;
- bootstrap intervals;
- standard errors;
- measurement ranges.

The chosen representation shall be documented.

---

# 28. Missing Data

Missing observations shall not silently become zeros or negative results.

The experiment shall distinguish:

- not measured;
- unavailable;
- failed measurement;
- excluded;
- genuinely zero.

Missing-data handling shall be recorded.

---

# 29. External Service Experiments

An external detector or measurement service may be used as an experimental
instrument.

Its observations shall be treated as time-dependent measurements.

The system should preserve:

- request metadata;
- response;
- timestamp;
- service identity;
- configuration;
- failure information.

If the service cannot provide stable historical reproduction, the result
shall retain that limitation.

---

# 30. Detector Ensemble Model

Where multiple detectors are available, the system may construct an
ensemble of observations.

An ensemble shall not automatically be interpreted as a superior ground
truth.

The system should preserve individual detector results before calculating
ensemble metrics.

---

# 31. Watermark Evaluation Model

Watermark evaluation shall distinguish at least:

1. watermark generation condition;
2. text artifact;
3. detector;
4. detector configuration;
5. observed detection result;
6. statistical interpretation.

A detection result shall always be linked to the exact experimental artifact
and detector condition.

---

# 32. AI-Detection Evaluation Model

AI-text detector evaluation shall distinguish:

- known source condition;
- detector;
- detector version;
- detector configuration;
- detector output;
- threshold, if applicable;
- reference condition;
- statistical interpretation.

Detector classification shall not be treated as an intrinsic property of
the text independent of the detector.

---

# 33. Preservation Evaluation Model

Transformation experiments shall evaluate preservation independently across
multiple dimensions.

At minimum:

- semantic;
- factual;
- structural;
- stylistic;
- linguistic;
- readability;
- lexical;
- length.

The dimensions shall remain independently inspectable.

---

# 34. Minimal-Change Measurement

When studying transformations described as minimal, the system shall
measure change rather than rely on the label "minimal".

Possible measurements include:

- character edit distance;
- token edit distance;
- sentence-level changes;
- lexical replacement rate;
- syntactic changes;
- semantic distance;
- structural changes.

No single metric shall define minimality universally.

---

# 35. Human Evaluation

Human evaluation may be used where automated metrics are insufficient.

A human-evaluation protocol shall specify:

- evaluator population;
- instructions;
- sample presentation;
- blinding;
- randomization;
- rating scale;
- aggregation;
- inter-rater agreement;
- exclusion rules.

Human evaluation shall be treated as a measurement methodology with its
own uncertainty and biases.

---

# 36. Cross-Language Comparability

Cross-language comparisons shall be justified rather than assumed.

Before comparing two languages, the experiment should assess:

- comparable sampling;
- comparable text length;
- domain compatibility;
- detector support;
- metric validity;
- translation effects, if any;
- script-related differences.

A metric that behaves differently across languages shall not automatically
be interpreted as evidence of a linguistic effect.

---

# 37. Confounding

Potential confounders shall be identified before interpreting causal
relationships.

Examples include:

- language;
- text length;
- domain;
- generation model;
- generation parameters;
- dataset;
- detector;
- transformation;
- source quality.

Where possible, experiments should control, stratify or model relevant
confounders.

---

# 38. Causal Interpretation

The system shall distinguish correlation from causation.

A change observed after a transformation does not by itself prove that the
transformation caused the change if other experimental variables also
changed.

Causal claims require an experimental design capable of supporting them.

---

# 39. Benchmark Model

A benchmark shall define:

- task;
- dataset;
- version;
- metrics;
- evaluation protocol;
- expected output;
- acceptance criteria;
- known limitations.

Benchmark results shall remain associated with the benchmark version under
which they were obtained.

---

# 40. Experimental Matrix

Complex studies should use an explicit experimental matrix.

Possible dimensions include:

- language;
- source type;
- domain;
- text length;
- watermark condition;
- detector;
- transformation;
- transformation configuration;
- replication.

The matrix shall make missing combinations visible.

---

# 41. Coverage

Scientific coverage shall be measured against the declared experimental
matrix.

A conclusion shall not be generalized beyond the combinations actually
tested without explicit justification.

---

# 42. Experiment Status

Experiments shall have a lifecycle:

PLANNED
→ CONFIGURED
→ RUNNING
→ COMPLETED
→ ANALYZED
→ REPORTED
→ SUPERSEDED

Failed experiments shall additionally support:

BLOCKED
FAILED
INVALIDATED

Historical experiment records shall remain identifiable.

---

# 43. Invalid Experiment

An experiment shall be classified as INVALIDATED when a problem makes its
results scientifically unreliable.

Examples include:

- corrupted source material;
- incorrect detector configuration;
- broken provenance;
- invalid dataset;
- implementation defect affecting measurements;
- protocol violation.

Invalidated experiments shall not be silently deleted.

---

# 44. Reproducibility Package

A reproducibility package should contain, where legally and technically
possible:

- experiment configuration;
- input identifiers;
- dataset versions;
- software version;
- dependency information;
- random seeds;
- raw observations;
- derived metrics;
- analysis configuration;
- report metadata.

---

# 45. Provenance Graph

The scientific system should be representable as a provenance graph:

Source
→ Experimental Condition
→ Transformation
→ Artifact
→ Measurement
→ Raw Observation
→ Derived Measurement
→ Statistical Analysis
→ Report

Every edge should be traceable.

---

# 46. Auditability

A researcher should be able to answer:

- where did this text originate?
- what happened to it?
- which transformations were applied?
- which instruments evaluated it?
- which versions were used?
- what raw observations were produced?
- how was the reported result calculated?

If the system cannot answer these questions, the corresponding result is
not fully auditable.

---

# 47. Scientific Update

When new research changes an experimental concept, the system shall:

1. record the new evidence;
2. identify affected concepts;
3. assess historical compatibility;
4. update the relevant model;
5. preserve previous definitions;
6. identify affected experiments;
7. update validation requirements.

Historical results shall not be silently reinterpreted as if the newer
methodology had always existed.

---

# 48. Completion Criteria

S03 is complete when:

- the experiment is formally modeled;
- variables are defined;
- baselines and controls are defined;
- transformations are modeled;
- measurement instruments are separated from ground truth;
- raw and derived observations are separated;
- multilingual experimentation is specified;
- replication is defined;
- statistical comparison principles are defined;
- missing data are addressed;
- external measurements are modeled;
- preservation is multidimensional;
- provenance is represented;
- experimental lifecycle is defined;
- reproducibility is explicitly modeled.

---

# 49. Final Principle

An experiment is not merely a script that produces a number.

It is a traceable chain connecting source material, controlled conditions,
measurements, observations, analysis and scientific interpretation.

The framework shall preserve that chain so that results can be examined,
challenged, reproduced and updated as scientific knowledge evolves.