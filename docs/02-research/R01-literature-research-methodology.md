# R01 — Literature Research Methodology

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Research methodology
**Parent:** docs/02-research/RESEARCH-MAP.md
**Authority:** Research
**Review trigger:** Material change in research methodology or project scope

---

# 1. Purpose

This document defines the methodology used to identify, collect, evaluate,
compare and maintain scientific literature relevant to the project.

The purpose is not merely to collect papers.

The purpose is to construct a traceable and continuously maintainable body of
evidence from which scientific hypotheses, requirements, experiments and
validation criteria can be derived.

---

# 2. Core Principle

The project must not begin with an implementation and search retrospectively
for literature supporting it.

The intended direction is:

LITERATURE
→ EVIDENCE
→ HYPOTHESIS
→ REQUIREMENT
→ EXPERIMENT
→ RESULT
→ VALIDATION
→ CERTIFICATION

---

# 3. Research Questions

Before beginning a major literature review, define the research questions.

A research question should identify:

- subject;
- property being investigated;
- population or language scope;
- relevant conditions;
- desired evidence.

---

# 4. Research Question Types

Research questions may be:

- descriptive;
- comparative;
- causal;
- methodological;
- robustness-oriented;
- measurement-oriented;
- replication-oriented;
- engineering-oriented.

---

# 5. Primary Research Questions

The project should investigate, among others:

1. What watermarking methodologies exist for generated text?
2. What detection methodologies exist for such watermarks?
3. How robust are these methods under textual transformation?
4. What methods exist for detecting AI-generated text?
5. How reliable are such detectors across languages and domains?
6. Which linguistic transformations preserve meaning?
7. Which transformations preserve factual content?
8. Which transformations preserve authorial and stylistic characteristics?
9. How can textual change be measured?
10. Which evaluation methodologies are scientifically defensible?
11. Which benchmarks are suitable for the intended experiments?
12. What known limitations invalidate naive evaluation?
13. How do results vary across languages?
14. How do results change under distribution shift?
15. What emerging methodologies may materially alter the evaluation framework?

This list is extensible.

---

# 6. Research Question Registry

Material research questions should be recorded in:

docs/00-project/OPEN-QUESTIONS.md

Once resolved, the question should remain historically traceable.

---

# 7. Search Strategy

Literature searches should use multiple complementary strategies.

At minimum consider:

- keyword search;
- citation chaining;
- related-work discovery;
- author discovery;
- venue discovery;
- benchmark discovery;
- implementation discovery;
- replication discovery;
- criticism discovery.

---

# 8. Search Sources

Potential sources include:

- arXiv;
- Semantic Scholar;
- Google Scholar;
- Crossref;
- ACL Anthology;
- publisher repositories;
- conference proceedings;
- journal databases;
- institutional repositories;
- official project repositories.

The source list is not exhaustive.

---

# 9. Source Hierarchy

When possible, prioritize primary sources for scientific claims.

Examples:

- original paper;
- original dataset publication;
- original benchmark publication;
- original software repository;
- official technical report.

Secondary sources may be used for discovery and contextualization.

---

# 10. Secondary Sources

Secondary sources may include:

- surveys;
- review papers;
- systematic reviews;
- technical summaries;
- scholarly discussions.

They should not replace primary evidence when the primary source is
available.

---

# 11. Search Broadly Before Searching Narrowly

Initial searches should establish the landscape.

Do not prematurely optimize for one implementation or one methodology.

---

# 12. Search Taxonomy

Search terms should cover multiple dimensions.

Examples:

- text watermark;
- language model watermark;
- watermark detection;
- robust watermark;
- watermark removal;
- watermark attack;
- AI text detection;
- generated text detection;
- machine-generated text;
- human text detection;
- multilingual AI detection;
- stylometry;
- text paraphrasing;
- semantic preservation;
- textual similarity;
- controlled text transformation.

The exact vocabulary should evolve with the literature.

---

# 13. Synonym Expansion

Search terms should include relevant synonyms and historical terminology.

A methodology may be described differently across research communities.

---

# 14. Terminology Drift

Scientific terminology changes over time.

The research process should periodically update the search vocabulary.

---

# 15. Search Logging

Important searches should be recorded when they materially influence the
research program.

A search record may include:

- date;
- source;
- query;
- filters;
- purpose;
- notable results.

---

# 16. Reproducibility of Searches

Where practical, searches should be reproducible.

Search engines may change results over time, so exact reproducibility is not
always possible.

---

# 17. Search Date

Each literature search should have an associated date.

---

# 18. Research Snapshot

A major literature review should produce a dated snapshot of the evidence
available at that time.

---

# 19. Discovery Phase

The discovery phase seeks breadth.

Its purpose is to identify:

- foundational papers;
- major methodologies;
- important datasets;
- benchmarks;
- competing approaches;
- known limitations;
- important controversies.

---

# 20. Collection Phase

The collection phase obtains the relevant primary sources.

---

# 21. Screening Phase

The screening phase determines whether a source is relevant enough to enter
the project's research corpus.

---

# 22. Full-Text Phase

Where possible, important sources should be evaluated using the full text
rather than title or abstract alone.

---

# 23. Extraction Phase

Extract:

- research question;
- methodology;
- dataset;
- languages;
- model;
- metrics;
- experimental conditions;
- results;
- limitations;
- conclusions.

---

# 24. Critical Appraisal

A paper should not be treated as authoritative merely because it reports a
positive result.

Evaluate the methodology critically.

---

# 25. Methodological Questions

For an important paper ask:

- Is the research question clearly defined?
- Is the methodology appropriate?
- Is the dataset appropriate?
- Is the sample size adequate?
- Are baselines appropriate?
- Are metrics appropriate?
- Are statistical methods appropriate?
- Are limitations acknowledged?
- Is the result reproducible?
- Does the evidence justify the conclusion?

---

# 26. Dataset Questions

Investigate:

- source;
- sampling;
- language;
- domain;
- document length;
- authorship;
- generation method;
- annotation;
- contamination;
- duplication.

---

# 27. Model Questions

For model-based research identify where possible:

- model family;
- model version;
- model size;
- tokenizer;
- decoding strategy;
- temperature;
- sampling method;
- prompt conditions.

---

# 28. Detector Questions

For detector research identify:

- detector type;
- training data;
- evaluation data;
- threshold;
- calibration;
- language coverage;
- domain;
- known limitations.

---

# 29. Watermark Questions

For watermark research identify:

- watermark mechanism;
- generation integration;
- detection mechanism;
- statistical assumptions;
- key or secret requirements;
- robustness conditions;
- attack model;
- false-positive behavior;
- false-negative behavior.

---

# 30. Transformation Questions

For transformation research identify:

- transformation mechanism;
- input assumptions;
- output assumptions;
- magnitude of modification;
- semantic evaluation;
- linguistic evaluation;
- detector evaluation;
- watermark evaluation;
- failure conditions.

---

# 31. AI-Detection Questions

For AI-detection research identify:

- definition of AI-generated text;
- generation source;
- human baseline;
- domain;
- language;
- document length;
- editing conditions;
- detector methodology;
- threshold;
- false-positive rate;
- false-negative rate.

---

# 32. Inclusion Criteria

A source should normally be included when it:

- directly addresses a project-relevant question;
- provides meaningful empirical or theoretical evidence;
- establishes a relevant methodology;
- provides a relevant dataset or benchmark;
- provides important criticism or replication;
- materially affects a project assumption.

---

# 33. Exclusion Criteria

A source may be excluded when:

- it is irrelevant;
- it provides no meaningful evidence;
- it duplicates another source without additional value;
- its provenance cannot be established;
- its claims cannot be interpreted reliably.

Exclusion should not be based solely on disagreement with project assumptions.

---

# 34. Borderline Sources

Borderline sources should be marked as such rather than silently included or
excluded.

---

# 35. Evidence Classification

Each important source should receive an evidence classification.

Suggested categories:

THEORETICAL
EMPIRICAL
BENCHMARK
METHODOLOGICAL
REPLICATION
CRITIQUE
SURVEY
ENGINEERING

A source may have multiple categories.

---

# 36. Evidence Strength

Evidence strength should be evaluated separately from source type.

Suggested levels:

E0 — no useful evidence
E1 — theoretical or conceptual support
E2 — limited empirical evidence
E3 — controlled empirical evidence
E4 — strong empirical evidence
E5 — replicated or independently supported evidence

These levels are descriptive rather than absolute.

---

# 37. Evidence Scope

Evidence must always be interpreted within its experimental scope.

A strong result on a narrow dataset may still have narrow applicability.

---

# 38. Generalization

Do not infer generalization beyond the evaluated population without evidence.

---

# 39. Language Generalization

Evidence for English must not automatically be interpreted as evidence for
all languages.

---

# 40. Domain Generalization

Evidence from one domain must not automatically be generalized to another.

---

# 41. Model Generalization

Evidence from one model family must not automatically be generalized to
other model families.

---

# 42. Detector Generalization

Evidence against one detector does not automatically establish behavior
against other detectors.

---

# 43. Watermark Generalization

Evidence against one watermark mechanism does not automatically establish
behavior against all watermark mechanisms.

---

# 44. Human-Editing Generalization

Results on unedited generated text should not automatically be generalized
to human-edited text.

---

# 45. Translation Generalization

Results obtained after translation should not automatically be generalized
to original-language text.

---

# 46. Paraphrase Generalization

Results obtained after one paraphrasing methodology should not automatically
be generalized to all paraphrasing methods.

---

# 47. Evidence Matrix

Important research areas should eventually have an evidence matrix.

Example:

| Research area | Evidence | Languages | Dataset | Method | Replication | Limitations |
|---|---|---|---|---|---|---|
| Watermarking | ... | ... | ... | ... | ... | ... |
| Watermark detection | ... | ... | ... | ... | ... | ... |
| AI detection | ... | ... | ... | ... | ... | ... |
| Semantic preservation | ... | ... | ... | ... | ... | ... |

---

# 48. Contradictory Evidence Matrix

Where meaningful, maintain a separate matrix for contradictory findings.

Fields may include:

- claim;
- source A;
- source B;
- methodological difference;
- dataset difference;
- language difference;
- possible explanation;
- unresolved status.

---

# 49. Research Consensus

Consensus should not be inferred simply from paper count.

Ten papers using the same flawed methodology do not necessarily outweigh one
well-designed contradictory study.

---

# 50. Methodological Independence

When counting supporting evidence, consider whether studies are
methodologically independent.

---

# 51. Citation Dependence

Multiple papers may derive their assumptions from the same foundational
result.

This should be considered when assessing evidence diversity.

---

# 52. Publication Bias

Positive results may be more likely to be published or cited.

The research process should actively seek:

- negative results;
- failed experiments;
- critiques;
- replications.

---

# 53. Survivorship Bias

Highly visible methodologies may not represent the full research landscape.

---

# 54. Selection Bias

Search strategy should avoid selecting only papers that support current
project assumptions.

---

# 55. Confirmation Bias

Researchers and AI systems must explicitly search for evidence that could
invalidate current assumptions.

---

# 56. Falsification Search

For every important project hypothesis, attempt to identify evidence that
would falsify or weaken it.

---

# 57. Research Controversies

Important controversies should be documented rather than collapsed into a
single conclusion.

---

# 58. Claim Extraction

Each important paper should produce explicit claims.

A claim should be as precise as practical.

---

# 59. Claim Types

Claims may be:

- methodological;
- empirical;
- statistical;
- causal;
- comparative;
- robustness-related;
- linguistic;
- operational.

---

# 60. Claim Provenance

Every important claim must be traceable to its source.

---

# 61. Claim Scope

Record the scope under which the claim was established.

---

# 62. Claim Confidence

Where useful, classify confidence as:

LOW
MODERATE
HIGH

This must be justified by evidence.

---

# 63. Claim Status

Claims may be:

- PROPOSED;
- SUPPORTED;
- PARTIALLY_SUPPORTED;
- CONTRADICTED;
- SUPERSEDED;
- UNRESOLVED.

---

# 64. Superseded Claims

When later research supersedes an earlier claim, preserve the historical claim
and link it to the newer evidence.

---

# 65. Research Synthesis

A synthesis should not simply concatenate paper summaries.

It should identify:

- agreements;
- disagreements;
- methodological differences;
- evidence gaps;
- practical implications.

---

# 66. Research Synthesis Structure

Recommended structure:

1. question;
2. evidence landscape;
3. methodologies;
4. results;
5. contradictions;
6. limitations;
7. implications;
8. unresolved questions.

---

# 67. Review Updates

A synthesis should be updated when material new evidence appears.

---

# 68. Update Triggers

Potential triggers include:

- major new paper;
- major benchmark;
- major detector;
- major watermark;
- replication;
- methodological criticism;
- evidence invalidation.

---

# 69. Incremental Updates

Do not rewrite the entire research history when updating.

Add the new evidence and update the current synthesis.

---

# 70. Historical Preservation

Previous research snapshots should remain identifiable.

---

# 71. Literature Versioning

If a preprint changes substantially, treat the new version as a new evidence
state where appropriate.

---

# 72. Paper Corrections

Corrections, retractions and major author revisions must be tracked.

---

# 73. Retractions

A retracted paper must not continue to be treated as ordinary supporting
evidence.

Its historical role may remain documented.

---

# 74. Reproducibility Status

For important studies record, where known:

- not tested;
- internally reproduced;
- independently reproduced;
- failed reproduction;
- partially reproduced.

---

# 75. Implementation Availability

If an implementation is available, record:

- repository;
- version;
- license;
- reproducibility status.

Availability does not imply scientific validity.

---

# 76. Code-vs-Paper Consistency

Where implementation is available, investigate whether it corresponds
meaningfully to the described methodology.

---

# 77. Hidden Parameters

Important undocumented parameters should be treated as a reproducibility
risk.

---

# 78. External API Research

If a paper relies on an external API or service, record that dependency.

---

# 79. Time-Dependent Research

External APIs and detectors can change.

Results involving them should be treated as dated observations.

---

# 80. Research Environment

Where reproducibility matters, record:

- operating system;
- software versions;
- libraries;
- model versions;
- hardware where relevant.

---

# 81. Research Data Provenance

Datasets should have traceable provenance.

---

# 82. Dataset Integrity

Where feasible, store checksums or equivalent integrity information.

---

# 83. Dataset Duplication

Duplicate datasets should not be treated as independent evidence.

---

# 84. Benchmark Contamination

Investigate whether models or detectors may have encountered benchmark data
during training.

---

# 85. Contamination Impact

Potential contamination should be recorded as a limitation.

---

# 86. Temporal Leakage

Research should consider whether training, tuning and evaluation datasets
overlap temporally.

---

# 87. Author Leakage

Where relevant, shared authors between training and evaluation may create
dependency.

---

# 88. Domain Leakage

Shared domains may produce artificially optimistic results.

---

# 89. Evaluation Leakage

Repeatedly tuning against a benchmark can reduce its independence.

---

# 90. Research Independence

Research decisions should not depend exclusively on the implementation
agent.

---

# 91. AI-Assisted Literature Review

AI systems may be used to accelerate:

- search;
- paper triage;
- metadata extraction;
- claim extraction;
- comparison;
- contradiction detection;
- document consistency checks.

---

# 92. AI Verification

AI-generated interpretations must be verified against source material before
being used as authoritative evidence.

---

# 93. Citation Hallucination Prevention

No paper, result, dataset, metric or quotation may be added to the research
registry without source verification.

---

# 94. Primary Source Requirement

Claims that materially affect architecture or certification should normally
be supported by primary sources whenever possible.

---

# 95. Secondary Evidence

Secondary evidence may be used when primary evidence is unavailable, but this
limitation must be recorded.

---

# 96. Search Completeness

The project should record known search limitations.

Examples:

- inaccessible database;
- paywalled source;
- language limitation;
- missing full text;
- unavailable implementation.

---

# 97. Language Bias in Literature

The literature itself may be biased toward English.

Research should recognize this limitation when evaluating multilingual claims.

---

# 98. Non-English Literature

Important research should be searched for in relevant languages where
practical.

---

# 99. Translation of Research

Machine translation may assist discovery.

Critical technical interpretation should be checked against the original
where practical.

---

# 100. Research Priority

Research priority should consider:

- relevance;
- uncertainty;
- potential impact;
- implementation dependency;
- certification dependency.

---

# 101. Research Risk Matrix

A research topic may be classified using:

| Impact | Uncertainty | Priority |
|---|---|---|
| High | High | Critical |
| High | Medium | High |
| High | Low | Medium |
| Low | High | Medium |
| Low | Low | Low |

This is a prioritization aid, not a scientific metric.

---

# 102. Research Backlog

Research tasks requiring future work should be entered into the project
knowledge backlog.

---

# 103. Research Stop Conditions

A research task may be considered sufficient for the current project phase
when:

- major methodologies are identified;
- relevant evidence has been screened;
- major contradictions are documented;
- important limitations are known;
- remaining gaps are explicitly registered.

---

# 104. No Claim of Absolute Completeness

The project must never claim that it has found all scientific literature.

It should instead describe its search strategy and known coverage.

---

# 105. Research Review Quality Gate

Before a literature synthesis becomes an input to architecture or
certification, verify:

- sources registered;
- primary sources checked;
- important competing methodologies identified;
- contradictory evidence considered;
- limitations recorded;
- claims traceable;
- research gaps documented.

---

# 106. Research Change Queue

If review reveals that an existing document must change, add an item to:

docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md

---

# 107. Research Registry Integration

Every material source should be entered into:

docs/00-project/RESEARCH-REGISTRY.md

---

# 108. Decision Integration

Research-driven decisions must be reflected in:

docs/00-project/DECISION-LOG.md

---

# 109. Assumption Integration

If research changes an assumption, update:

docs/00-project/ASSUMPTION-REGISTRY.md

---

# 110. Knowledge Integration

Unresolved knowledge gaps belong in:

docs/00-project/KNOWLEDGE-BACKLOG.md

---

# 111. Open Question Integration

Questions requiring future resolution belong in:

docs/00-project/OPEN-QUESTIONS.md

---

# 112. Research Map Integration

New research domains should be added to:

docs/02-research/RESEARCH-MAP.md

---

# 113. Research Automation

Claude Code may automate:

- metadata collection;
- duplicate detection;
- registry consistency checks;
- citation checks;
- document cross-reference checks;
- research-gap detection.

---

# 114. Research Automation Limits

Automation must not silently determine scientific truth.

It may organize and analyze evidence, but material scientific conclusions
must remain traceable to the underlying sources and defined methodology.

---

# 115. Change Detection

When new literature is added, automated checks should identify potentially
affected:

- assumptions;
- decisions;
- requirements;
- experiments;
- certification records.

---

# 116. Orphan Detection

Automated validation should identify:

- sources with no research classification;
- claims with no source;
- requirements with no evidence;
- experiments with no scientific rationale.

---

# 117. Broken Traceability

Broken research links should be treated as documentation defects.

---

# 118. Research Debt

Missing literature analysis, unresolved contradictions and undocumented
assumptions constitute research debt.

---

# 119. Research Debt Prioritization

Research debt should be prioritized by its potential effect on:

- scientific validity;
- architecture;
- validation;
- certification.

---

# 120. Research Integrity Gate

Before a major project milestone, verify that no known critical research
question remains silently unresolved.

---

# 121. Research Update Protocol

When important new evidence appears:

1. register the source;
2. classify it;
3. assess evidence quality;
4. identify affected claims;
5. identify affected assumptions;
6. identify affected requirements;
7. identify affected experiments;
8. determine certification impact;
9. update relevant documents;
10. preserve historical traceability.

---

# 122. Future-Proofing

The methodology must support research topics that do not yet exist.

Therefore:

- taxonomies must be extensible;
- detector categories must be extensible;
- watermark categories must be extensible;
- language coverage must be extensible;
- evaluation metrics must be extensible.

---

# 123. Scientific Evolution

The research corpus is expected to change.

The project should optimize for traceability of change rather than artificial
stability.

---

# 124. Final Principle

The objective of the literature process is not to prove that the planned
software is correct.

The objective is to determine, as accurately as practical, what current
scientific evidence supports, what it contradicts, what remains unknown, and
what experiments are necessary to resolve the uncertainty.