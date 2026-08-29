# Data Map

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Data architecture and data governance map
**Authority:** Data
**Scope:** Datasets, corpora, benchmarks, models, linguistic resources,
experimental artifacts, provenance, licensing, storage and lifecycle

---

## 1. Purpose

This document defines how project data is acquired, classified, stored,
versioned, validated, used, archived and retired.

The project is expected to work with heterogeneous research material,
including:

- multilingual text corpora;
- human-authored text;
- AI-generated text;
- transformed text;
- watermark research corpora;
- AI-detector evaluation corpora;
- linguistic resources;
- benchmark datasets;
- model files;
- tokenizer files;
- statistical resources;
- experiment outputs;
- metadata;
- evaluation results.

Data must remain traceable and scientifically interpretable throughout its
lifecycle.

---

# 2. Fundamental Data Principle

Data is part of the scientific method.

A result without identifiable data provenance is not considered fully
reproducible.

Every important result must therefore be traceable to:

DATA
→ VERSION
→ PREPROCESSING
→ EXPERIMENT
→ RESULT

---

# 3. Data Categories

The project distinguishes at least:

1. SOURCE_DATA
2. DERIVED_DATA
3. BENCHMARK_DATA
4. TEST_DATA
5. EXPERIMENT_DATA
6. MODEL_ARTIFACT
7. LINGUISTIC_RESOURCE
8. METADATA
9. RESULT_ARTIFACT
10. EXTERNAL_REFERENCE

---

# 4. Source Data

SOURCE_DATA is data obtained from an external source and preserved in its
original form where legally and technically possible.

Examples:

- public corpora;
- published datasets;
- research datasets;
- public benchmark collections.

Source data should not be silently modified.

---

# 5. Derived Data

DERIVED_DATA is produced from another dataset by a documented operation.

Examples:

- normalized text;
- language-filtered corpus;
- deduplicated corpus;
- segmented corpus;
- tokenized representation;
- annotated corpus.

Every derived dataset must identify its parent dataset.

---

# 6. Benchmark Data

BENCHMARK_DATA is a dataset used to compare capabilities or versions.

Benchmark membership must be versioned.

A benchmark should not silently change between two evaluations.

---

# 7. Test Data

TEST_DATA is used primarily for software validation.

Test data may be:

- synthetic;
- public;
- reduced examples;
- adversarial;
- regression fixtures.

Sensitive user data should not be used as ordinary test data.

---

# 8. Experiment Data

EXPERIMENT_DATA includes:

- experiment inputs;
- controlled outputs;
- intermediate artifacts where scientifically useful;
- detector observations;
- measurements;
- experiment metadata.

Experiment data must remain linked to its experiment identifier.

---

# 9. Model Artifacts

Model artifacts include:

- local models;
- tokenizer models;
- embeddings;
- language models;
- classification models;
- auxiliary models.

Each model must have provenance and version metadata.

---

# 10. Linguistic Resources

Linguistic resources may include:

- dictionaries;
- frequency lists;
- morphological resources;
- sentence segmentation resources;
- tokenizers;
- language identification models;
- parsers;
- multilingual embeddings.

Language resources must specify their supported languages.

---

# 11. Metadata

Metadata should be stored separately from large binary artifacts where
practical.

Important metadata includes:

- identifier;
- version;
- source;
- license;
- language;
- domain;
- size;
- checksum;
- acquisition date;
- preprocessing;
- parent dataset;
- intended use;
- restrictions.

---

# 12. Data Identifier

Every important dataset or artifact should receive a stable identifier.

Recommended structure:

DATA-[CATEGORY]-[SHORT-NAME]

Example:

DATA-CORPUS-EN-001

The exact identifier convention may evolve.

---

# 13. Dataset Version

Every dataset must have an explicit version.

A version change is required when the dataset changes in a way that can affect
scientific results.

Examples:

- new documents;
- removed documents;
- changed labels;
- changed preprocessing;
- changed deduplication;
- changed language classification.

---

# 14. Immutable Dataset Versions

Once used for a certified experiment, a dataset version should be treated as
immutable.

Corrections should create a new version.

Historical results should continue to reference the original version.

---

# 15. Checksums

Where practical, calculate cryptographic hashes for important:

- datasets;
- archives;
- model files;
- benchmark packages;
- generated release artifacts.

Checksums provide an integrity reference.

---

# 16. Provenance

Each dataset should document:

- where it came from;
- who published it;
- how it was acquired;
- when it was acquired;
- which version was acquired;
- how it was processed.

---

# 17. Provenance Chain

Derived data should form a traceable chain.

Example:

SOURCE
→ CLEANED
→ LANGUAGE_FILTERED
→ DEDUPLICATED
→ BENCHMARK
→ EXPERIMENT

Each step should be identifiable.

---

# 18. Preprocessing Registry

Preprocessing operations must be documented.

Examples:

- Unicode normalization;
- whitespace normalization;
- sentence segmentation;
- tokenization;
- language filtering;
- deduplication;
- HTML removal;
- markup normalization.

Preprocessing can influence scientific results and must therefore be
versioned.

---

# 19. Raw vs Processed Data

Raw data and processed data should remain conceptually separate.

The project should never imply that a processed corpus is identical to its
source corpus.

---

# 20. Reversible Processing

Where practical, preprocessing should preserve enough metadata to understand
what was changed.

Lossy processing must be explicitly identified.

---

# 21. Language Metadata

Each textual dataset should record language information where available.

At minimum:

- primary language;
- language confidence if available;
- multilingual status;
- language distribution.

---

# 22. Target Languages

The initial research scope includes:

1. English
2. Spanish
3. German
4. Japanese
5. French
6. Portuguese
7. Russian
8. Italian
9. Dutch
10. Polish
11. Turkish
12. Chinese
13. Indonesian

The project must not assume that all components have equivalent quality in
all languages.

---

# 23. Language Variants

Where relevant, distinguish:

- language;
- script;
- regional variant;
- writing system;
- orthographic convention.

Examples may include regional variants of English, Spanish, Portuguese and
Chinese.

---

# 24. Text Length Metadata

Dataset metadata should include length distributions.

Useful measures include:

- characters;
- tokens;
- sentences;
- paragraphs;
- documents.

Length is an important experimental variable.

---

# 25. Domain Metadata

Where feasible, classify documents by domain.

Potential domains include:

- news;
- academic;
- technical;
- fiction;
- conversational;
- web;
- legal;
- business;
- educational.

Domain classification must not be presented as objective if the underlying
labels are uncertain.

---

# 26. Author Metadata

Where legally and scientifically appropriate, metadata may distinguish:

- known human authorship;
- synthetic generation;
- unknown origin;
- mixed authorship.

Sensitive personal information must not be unnecessarily retained.

---

# 27. Authorship Labels

Authorship labels are research metadata, not universal ground truth.

A label such as HUMAN or AI_GENERATED must include information about how the
label was established.

---

# 28. Generation Metadata

For synthetic text, where available, record:

- model family;
- model version;
- generation configuration;
- date;
- prompt provenance where legally and scientifically appropriate;
- generation procedure.

Missing metadata must be marked as unknown rather than guessed.

---

# 29. Transformation Metadata

For controlled transformations, record:

- transformation identifier;
- version;
- configuration;
- input dataset;
- output dataset;
- language;
- timestamp;
- validation results.

The original source must remain identifiable.

---

# 30. Watermark Research Data

Watermark-related datasets should record:

- watermark family;
- implementation;
- generation model;
- configuration;
- text source;
- language;
- document length;
- watermark status if known;
- detector methodology;
- version.

The project must distinguish experimentally embedded or suspected
watermarks from independently verified watermark status.

---

# 31. Detector Research Data

Detector evaluation data should record:

- detector identifier;
- provider;
- version;
- interface;
- date;
- language;
- input characteristics;
- result;
- threshold;
- configuration.

External detector results are observations and must not be treated as
universal authorship truth.

---

# 32. Detector Result Storage

Where legally permissible, retain:

- raw detector response;
- normalized result;
- request metadata;
- error information.

If raw responses cannot be retained, preserve sufficient metadata to
interpret the normalized result.

---

# 33. External Service Data

When text is sent to an external service, the project must record:

- service;
- purpose;
- timestamp;
- configuration;
- data category;
- returned result.

The system must not silently transmit text.

---

# 34. Privacy Classification

Data should be classified according to sensitivity.

Recommended categories:

PUBLIC
RESEARCH_RESTRICTED
PRIVATE
SENSITIVE
PROHIBITED_FOR_EXTERNAL_TRANSFER

The exact legal classification depends on the applicable jurisdiction and
dataset license.

---

# 35. External Transfer Eligibility

Every dataset should declare whether it may be sent to external services.

Possible states:

ALLOWED
CONDITIONALLY_ALLOWED
LOCAL_ONLY
PROHIBITED
UNKNOWN

UNKNOWN must be treated conservatively.

---

# 36. Personally Identifiable Information

Datasets containing personal information should be minimized and handled
according to applicable law and license restrictions.

The project should avoid collecting personal information when it is not
scientifically necessary.

---

# 37. Sensitive Text

Sensitive text should not be placed in:

- Git repositories;
- public benchmark packages;
- issue trackers;
- ordinary logs;
- public documentation.

---

# 38. Licensing

Every externally sourced dataset should have a recorded license or usage
status.

Possible states:

- OPEN;
- RESEARCH_ONLY;
- COMMERCIAL_RESTRICTED;
- ATTRIBUTION_REQUIRED;
- DERIVATIVE_RESTRICTIONS;
- UNKNOWN;
- PROHIBITED.

---

# 39. License Evidence

Where possible, preserve:

- license name;
- source URL;
- source version;
- acquisition date;
- license text or reference;
- relevant restrictions.

---

# 40. License Uncertainty

Unknown licensing status must not be silently interpreted as permission.

The dataset should remain restricted until its status is clarified.

---

# 41. GitHub Usage

GitHub may be used for:

- source code;
- documentation;
- lightweight metadata;
- small public fixtures;
- benchmark definitions;
- scripts;
- manifests.

Large datasets should not automatically be committed to Git.

---

# 42. Large Artifact Storage

Large artifacts may be stored outside the Git repository when appropriate.

The repository should contain:

- identifier;
- version;
- checksum;
- acquisition instructions;
- provenance;
- license;
- expected size.

---

# 43. Local Storage Budget

The project has a target maximum of approximately:

30 GB

for the complete local research/data environment.

This is an engineering constraint rather than a scientific requirement.

---

# 44. Storage Budget Allocation

The budget should be managed explicitly.

Recommended conceptual allocation:

- datasets;
- models;
- linguistic resources;
- caches;
- experiment artifacts;
- build artifacts;
- backups.

Exact percentages should be established only after actual resource
requirements are measured.

---

# 45. Storage Monitoring

The project should periodically report:

- total usage;
- usage by category;
- largest artifacts;
- obsolete artifacts;
- cache usage;
- recoverable storage.

---

# 46. Storage Alerts

The system should warn before the storage budget is exhausted.

Suggested states:

NORMAL
WARNING
CRITICAL

Thresholds should be configurable.

---

# 47. Cache Policy

Caches must be distinguishable from canonical data.

Caches may be deleted and regenerated.

Canonical datasets must not depend on undocumented cache state.

---

# 48. Reproducible Downloads

Downloaded artifacts should preferably be acquired through reproducible
manifests.

A manifest should identify:

- source;
- version;
- checksum;
- expected size;
- license.

---

# 49. Download Verification

Downloaded files should be checked for:

- expected type;
- expected size;
- checksum where available;
- archive safety;
- provenance.

---

# 50. Data Ingestion

Data ingestion should be a controlled operation.

It should perform:

1. source verification;
2. license check;
3. file validation;
4. checksum calculation;
5. metadata registration;
6. optional preprocessing;
7. validation.

---

# 51. Duplicate Detection

Duplicate or near-duplicate data can distort scientific evaluations.

The project should support duplicate analysis where appropriate.

Deduplication must be versioned.

---

# 52. Benchmark Contamination

Benchmark contamination should be investigated where relevant.

Potential contamination includes:

- benchmark text appearing in training data;
- benchmark text reused during development;
- benchmark-derived tuning;
- accidental leakage between datasets.

---

# 53. Dataset Leakage

Potential leakage must be documented.

A benchmark should not be treated as independent if its contents have
influenced the evaluated capability.

---

# 54. Data Splits

Where applicable, datasets should support:

- development;
- validation;
- test.

The exact split strategy must depend on the scientific task.

---

# 55. Temporal Splits

For research involving evolving systems, temporal splits may be useful.

Examples:

- historical data;
- contemporary data;
- future/holdout data.

Temporal assumptions must be documented.

---

# 56. Multilingual Balance

Aggregated multilingual results must not conceal severe differences between
languages.

Reports should include per-language results.

---

# 57. Language Representation

The project should monitor whether the dataset distribution reflects the
intended research population.

The initial language list is a scope decision, not evidence that the
languages are equally represented in real-world usage.

---

# 58. Dataset Quality

Dataset quality should consider:

- correctness;
- completeness;
- duplication;
- language accuracy;
- labeling quality;
- domain diversity;
- length distribution;
- provenance.

---

# 59. Label Quality

Labels should record:

- label source;
- annotation procedure;
- confidence where available;
- disagreements;
- unknown cases.

---

# 60. Unknown Labels

Unknown or uncertain labels must remain explicit.

The system must not force every document into a binary category merely to
simplify processing.

---

# 61. Synthetic Controls

Synthetic data may be useful for controlled experiments.

Synthetic datasets must be clearly distinguished from naturally occurring
data.

---

# 62. Human Controls

Where human-authored controls are required, provenance should be documented
as accurately as possible.

Claims of human authorship must not exceed the available evidence.

---

# 63. Generated Controls

Where model-generated controls are used, record generation metadata.

Different model families should remain distinguishable.

---

# 64. Translation Data

Translated data must be labeled as translated.

Translation can change:

- lexical distributions;
- syntax;
- punctuation;
- discourse structure;
- detector behavior;
- watermark-related measurements.

---

# 65. Back-Translation

Back-translated data must be treated as a distinct experimental condition.

It must not be considered equivalent to the original text.

---

# 66. Data Augmentation

Any augmentation must be versioned.

Examples:

- paraphrase;
- translation;
- sentence recombination;
- controlled perturbation.

The project must preserve the distinction between original and augmented
data.

---

# 67. Experiment Artifacts

Experiment artifacts may include:

- input identifiers;
- output identifiers;
- diffs;
- measurements;
- logs;
- reports.

Large redundant artifacts should not consume storage unnecessarily.

---

# 68. Result Retention

Important scientific results should remain accessible even after a
capability is deprecated.

Retiring a capability does not automatically justify deleting its historical
evidence.

---

# 69. Data Lifecycle

Recommended lifecycle:

DISCOVERED
→ ACQUIRED
→ VERIFIED
→ REGISTERED
→ PROCESSED
→ VALIDATED
→ ACTIVE
→ ARCHIVED
→ RETIRED

---

# 70. Data Retirement

Data may be retired when:

- license expires;
- source disappears;
- replacement is superior;
- benchmark is invalidated;
- storage constraints require removal;
- security concerns arise.

Retirement must preserve metadata about the former artifact.

---

# 71. Data Deletion

Deletion of important scientific data should be documented.

The record should state:

- what was deleted;
- why;
- when;
- who/what authorized it;
- whether results are affected.

---

# 72. Data Migration

Migration to a new format must preserve:

- identifiers;
- versions;
- provenance;
- checksums where meaningful;
- semantic interpretation.

---

# 73. Data Format Policy

Prefer open and well-supported formats where practical.

Textual data should use explicit encoding.

Unicode handling must be deterministic and documented.

---

# 74. Unicode

Because the project is multilingual, Unicode handling is a core data concern.

The system must explicitly define behavior for:

- normalization;
- combining characters;
- invisible characters;
- bidirectional controls;
- homoglyphs;
- zero-width characters.

---

# 75. Unicode Security

Invisible or control characters must not be silently discarded if doing so
could affect scientific interpretation.

If normalization removes or changes them, that operation must be documented.

---

# 76. Script Metadata

Datasets should distinguish scripts where relevant.

Examples:

- Latin;
- Cyrillic;
- Han;
- Kana;
- mixed-script text.

---

# 77. Encoding Errors

Encoding failures must be reported.

Silent replacement of characters is discouraged because it can alter
scientific results.

---

# 78. Text Canonicalization

Canonicalization should be treated as a transformation, not an invisible
implementation detail.

Its version must be recorded when it can affect evaluation.

---

# 79. Data Access Layers

The software should distinguish:

- raw access;
- normalized access;
- benchmark access;
- experiment access.

This reduces accidental mixing of incompatible representations.

---

# 80. Dataset Manifest

Every major dataset should have a manifest containing at least:

- dataset ID;
- version;
- source;
- license;
- languages;
- size;
- checksum;
- preprocessing;
- storage location;
- status.

---

# 81. Model Manifest

Every important model should have a manifest containing:

- model ID;
- version;
- source;
- license;
- format;
- size;
- checksum;
- supported languages;
- intended use;
- status.

---

# 82. Resource Compatibility

A resource should declare compatibility with:

- runtime version;
- tokenizer version;
- language;
- model family where relevant.

Incompatible resources must fail clearly rather than being silently used.

---

# 83. Data Validation Gates

Before a dataset becomes ACTIVE:

1. provenance is known;
2. licensing is recorded;
3. integrity is verified;
4. metadata exists;
5. language information is available where relevant;
6. preprocessing is documented;
7. storage location is known.

---

# 84. Benchmark Activation Gate

A benchmark becomes ACTIVE only when:

- contents are versioned;
- evaluation methodology is defined;
- leakage risks are considered;
- licensing permits intended use;
- baseline results are available where appropriate.

---

# 85. Model Activation Gate

A model becomes ACTIVE only when:

- provenance is known;
- format is verified;
- license is known;
- compatibility is documented;
- loading behavior is tested;
- security implications are assessed.

---

# 86. Data Quality Flags

Datasets should support flags such as:

- VERIFIED;
- PARTIALLY_VERIFIED;
- LANGUAGE_UNCERTAIN;
- LICENSE_UNCERTAIN;
- DUPLICATES_PRESENT;
- CONTAMINATION_RISK;
- EXTERNAL_TRANSFER_RESTRICTED;
- DEPRECATED.

---

# 87. Data Change Impact

When a dataset changes, determine whether it affects:

- benchmarks;
- baselines;
- experiments;
- scientific claims;
- certification;
- storage;
- licensing.

---

# 88. Automatic Data Checks

Where practical, automate:

- checksums;
- file counts;
- size checks;
- encoding checks;
- language validation;
- duplicate detection;
- manifest validation;
- license metadata presence.

---

# 89. Data Regression

A dataset update should be evaluated for unexpected changes.

For important corpora, compare:

- document count;
- language distribution;
- length distribution;
- duplicate rate;
- metadata distribution.

---

# 90. Data Reproducibility

A new environment should be able to reconstruct required public datasets
from their manifests where the source remains available.

If reconstruction is impossible, the limitation must be recorded.

---

# 91. Offline Data Availability

Core offline functionality should rely only on resources declared as
locally available.

The software must not silently attempt to download missing data.

---

# 92. Optional Resources

Large or specialized resources may be optional.

Their absence must produce an explicit capability state such as:

AVAILABLE
OPTIONAL
MISSING
INCOMPATIBLE
DEPRECATED

---

# 93. Resource Discovery

The system should expose which resources are installed and usable.

This avoids confusing:

"supported"

with:

"currently available."

---

# 94. Data and Capability Registry

Every capability that depends on a dataset or model should declare that
dependency.

This allows the project to determine:

- what breaks if a dataset is removed;
- what needs retesting after an update;
- which capabilities depend on a deprecated resource.

---

# 95. Dependency Graph

The data system should support a conceptual graph:

DATASET
→ PREPROCESSOR
→ RESOURCE
→ CAPABILITY
→ EXPERIMENT
→ RESULT

Changes should propagate through this dependency graph during validation.

---

# 96. Obsolescence

A resource may become obsolete because:

- better data exists;
- source disappears;
- licensing changes;
- methodology changes;
- language coverage improves;
- security concerns emerge.

Obsolete resources should be deprecated before retirement when practical.

---

# 97. Replacement

Every deprecated resource should identify a replacement where one exists.

The replacement must not automatically inherit the old resource's version
or scientific properties.

---

# 98. Data Change Queue

Material data changes should enter the project's documentation change queue.

Examples:

- new benchmark;
- changed corpus;
- new model;
- changed license;
- changed preprocessing;
- retired dataset.

---

# 99. Data Research Registry

The research registry should reference all major datasets.

It should prevent duplicate acquisition of substantially identical resources
without scientific justification.

---

# 100. Data Acquisition Priority

When selecting new resources, prioritize:

1. scientific relevance;
2. provenance quality;
3. licensing clarity;
4. multilingual coverage;
5. reproducibility;
6. storage efficiency;
7. maintenance burden.

---

# 101. Storage Efficiency

Prefer:

- compressed formats where safe;
- deduplicated resources;
- reusable shared datasets;
- manifests instead of duplicate copies;
- derived-on-demand artifacts where practical.

Do not sacrifice reproducibility solely to minimize storage.

---

# 102. 30 GB Constraint

If the project approaches the storage ceiling, the preferred order is:

1. remove regenerable caches;
2. remove duplicate derived artifacts;
3. compress eligible resources;
4. archive rarely used resources;
5. move eligible large public resources outside the local environment;
6. reconsider optional resources.

Canonical research evidence should not be deleted merely to satisfy the
storage target without documenting the scientific impact.

---

# 103. Data Backup

Important metadata and experiment records should be backed up separately
from large regenerable datasets.

---

# 104. Data Integrity Monitoring

Important artifacts should be periodically checked against their recorded
checksums where practical.

Unexpected changes must be investigated.

---

# 105. Data Security Boundary

Data permissions must follow the security map.

The data layer must not independently grant:

- network access;
- arbitrary code execution;
- unrestricted filesystem access.

---

# 106. Data and AI-Assisted Development

Claude Code may modify data manifests, ingestion scripts and data
documentation, but it must not silently:

- replace datasets;
- alter benchmark membership;
- change labels;
- delete scientific evidence;
- bypass licensing checks.

Such changes require explicit documentation and appropriate validation.

---

# 107. Automatic Data Maintenance

Routine maintenance may be automated when it is:

- reversible;
- deterministic;
- documented;
- tested.

Examples:

- regenerating caches;
- validating manifests;
- checking checksums;
- producing storage reports.

---

# 108. Data Change Verification

After a data maintenance batch, verify:

- expected files exist;
- unexpected files are absent;
- checksums are correct;
- manifests are valid;
- storage remains within limits;
- dependent tests pass.

---

# 109. Scientific Evidence Preservation

When a capability is retired, preserve enough information to understand
historical results.

At minimum preserve:

- dataset identifier;
- dataset version;
- experiment identifier;
- software version;
- result metadata.

---

# 110. Data Documentation Requirement

Every major dataset must eventually have a dedicated data card or equivalent
documentation containing:

- purpose;
- provenance;
- license;
- composition;
- languages;
- preprocessing;
- known limitations;
- storage requirements;
- scientific uses.

---

# 111. Data Card Status

Data cards may have states:

DRAFT
→ REVIEWED
→ ACTIVE
→ DEPRECATED
→ RETIRED

---

# 112. Data Quality and Scientific Claims

A dataset's limitations must propagate into scientific claims.

For example, a result obtained only on:

- short texts;
- one domain;
- synthetic data;
- one language;

must not automatically be generalized beyond those conditions.

---

# 113. Data Drift

For external or periodically updated datasets, monitor:

- version changes;
- distribution changes;
- label changes;
- language changes;
- licensing changes.

A dataset update may require benchmark revalidation.

---

# 114. External Dataset Availability

If an external dataset disappears, the project should preserve:

- acquisition metadata;
- citation;
- version;
- checksum;
- historical results.

Redistribution must still respect the original license.

---

# 115. Data Provenance and Citations

Scientific use of external datasets should retain appropriate attribution
and citation information.

Citation metadata should be part of the dataset manifest where practical.

---

# 116. Data Quality Gate for Research

Before relying on a dataset for a major scientific claim, verify:

- provenance;
- licensing;
- integrity;
- language;
- domain;
- sample characteristics;
- contamination risk;
- preprocessing;
- version.

---

# 117. Data Quality Gate for Release

Before a release:

- required datasets are available;
- required models are available;
- manifests validate;
- checksums are correct;
- licenses are recorded;
- optional resources are correctly marked;
- storage requirements are known.

---

# 118. Current Data State

The project currently has a data architecture but no requirement that all
datasets be acquired before the software architecture is finalized.

Research acquisition should proceed incrementally.

---

# 119. Data Acquisition Strategy

Initial acquisition should prioritize resources that answer the highest-value
scientific questions.

Do not download large datasets merely because they are available.

---

# 120. Research-First Acquisition

For every proposed large dataset, document:

- research question;
- expected benefit;
- estimated storage;
- licensing status;
- processing cost;
- alternatives.

---

# 121. Avoiding Data Hoarding

Storage capacity must not become a reason to accumulate datasets without a
defined scientific purpose.

Every large resource should have an owner within the research architecture:
a capability, benchmark or research question.

---

# 122. Dataset Retirement Review

Periodically review large resources for:

- continued scientific value;
- replacement availability;
- storage cost;
- license changes;
- security issues;
- reproducibility value.

---

# 123. Data Lifecycle Automation

Where practical, automate:

- manifest checks;
- storage accounting;
- checksum checks;
- stale-cache detection;
- dependency impact detection.

---

# 124. Data Governance Principle

Data decisions should be explicit, reversible where possible, and
scientifically traceable.

---

# 125. Governing Principle

The project should treat data not as passive files but as versioned
scientific dependencies.

The goal is:

TRACEABLE DATA
→ REPRODUCIBLE EXPERIMENTS
→ INTERPRETABLE RESULTS
→ MAINTAINABLE SOFTWARE

A dataset that cannot be identified, reproduced, licensed, validated or
properly interpreted must not silently become foundational to the system.