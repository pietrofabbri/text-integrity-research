from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
TARGET = PROJECT_ROOT / "docs" / "02-research" / "RESEARCH-MAP.md"

CONTENT = """# Research Map

**Status:** ACTIVE  
**Version:** 0.1  
**Document type:** Cumulative research map  
**Parent:** `docs/00-project/PROJECT-MAP.md`

---

# 1. Purpose

This document is the cumulative map of the project's scientific research.

It defines:

- the research domains;
- the relationship between research domains;
- the expected outputs of each domain;
- the dependencies between domains;
- the route by which new scientific evidence enters the project;
- the relationship between research and the rest of the project documentation.

This document is intentionally high-level.

Detailed scientific evidence belongs in the corresponding research documents,
research registry and evidence records.

---

# 2. Research Architecture

The research layer is organized into the following domains:

```text
R01
Literature Research Methodology
        │
        ├──────────────┐
        │              │
        ▼              ▼
R02                    R04
Watermark Research     AI-Generated Text Detection
        │              │
        ▼              │
R03                    │
Watermark Detection ──┤
        │              │
        └──────┬───────┘
               ▼
R05
Multilingual & Linguistic Research
               │
               ▼
R06
Transformation & Preservation
               │
               ▼
R07
Evaluation & Statistical Methodology
               │
               ▼
R08
Benchmark & Dataset Research
               │
               └───────────────┐
                               ▼
                    Scientific Validation
```

The diagram is conceptual rather than a strict execution order.

Research domains may be investigated in parallel.

---

# 3. R01 — Literature Research Methodology

**File:**

`docs/02-research/R01-literature-research-methodology.md`

## Purpose

Defines how scientific literature is discovered, evaluated, classified,
recorded and incorporated into the project.

## Key outputs

- search methodology;
- source hierarchy;
- evidence quality criteria;
- inclusion/exclusion criteria;
- research traceability;
- literature update procedure.

## Dependencies

R01 is foundational to all other research domains.

---

# 4. R02 — Watermark Research

**File:**

`docs/02-research/R02-watermark-research.md`

## Purpose

Studies textual watermarking methodologies and their underlying mechanisms.

## Key outputs

- watermark taxonomy;
- methodology inventory;
- mechanism classification;
- robustness evidence;
- language/model dependencies;
- future-watermark monitoring requirements.

## Feeds

- R03;
- R05;
- R06;
- R07;
- security research;
- scientific specification.

---

# 5. R03 — Watermark Detection Research

**File:**

`docs/02-research/R03-watermark-detection-research.md`

## Purpose

Studies methods capable of identifying or statistically testing textual
watermarks.

## Key outputs

- detector taxonomy;
- detector inventory;
- detector version registry;
- detector limitations;
- false-positive/false-negative evidence;
- cross-detector methodology.

## Depends on

- R02;
- R01.

## Feeds

- validation;
- certification;
- future detector integration.

---

# 6. R04 — AI-Generated Text Detection Research

**File:**

`docs/02-research/R04-ai-generated-text-detection-research.md`

## Purpose

Studies methodologies attempting to distinguish human-written,
AI-generated and mixed-origin text.

## Key outputs

- AI-detector taxonomy;
- detector evidence;
- benchmark analysis;
- language-specific findings;
- robustness findings;
- detector drift requirements.

## Depends on

- R01.

## Interacts with

- R03;
- R05;
- R06;
- R07;
- R08.

---

# 7. R05 — Multilingual and Linguistic Research

**File:**

`docs/02-research/R05-multilingual-linguistic-research.md`

## Purpose

Studies language-specific properties that can influence watermarking,
detection, transformation and preservation.

## Initial languages

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

This list is not immutable.

Additional languages may be added when justified by evidence or project
requirements.

## Key outputs

- language profiles;
- language-specific risks;
- tokenization findings;
- linguistic transformation findings;
- multilingual evaluation methodology;
- language-specific limitations.

---

# 8. R06 — Transformation and Preservation Research

**File:**

`docs/02-research/R06-transformation-preservation-research.md`

## Purpose

Studies textual transformation while measuring preservation of relevant
properties.

## Core preservation dimensions

- semantic;
- factual;
- structural;
- linguistic;
- stylistic;
- terminological;
- numerical;
- entity-level;
- formatting.

## Key outputs

- transformation taxonomy;
- minimality methodology;
- preservation metrics;
- failure taxonomy;
- transformation intensity model;
- multilingual preservation methodology.

## Interacts with

- R02;
- R03;
- R04;
- R05;
- R07.

---

# 9. R07 — Evaluation and Statistical Methodology

**File:**

`docs/02-research/R07-evaluation-statistical-methodology.md`

## Purpose

Defines how experimental results should be measured and interpreted.

## Key outputs

- metric definitions;
- statistical methodology;
- uncertainty methodology;
- experimental design principles;
- reproducibility requirements;
- robustness methodology.

## Feeds

All validation and certification work.

---

# 10. R08 — Benchmark and Dataset Research

**File:**

`docs/02-research/R08-benchmark-dataset-research.md`

## Purpose

Studies the datasets and benchmarks required to support scientifically
meaningful experimentation.

## Key outputs

- dataset registry requirements;
- benchmark registry requirements;
- provenance methodology;
- contamination methodology;
- benchmark validity criteria;
- dataset quality standards.

## Interacts with

All research domains.

---

# 11. Cross-Domain Dependencies

Research findings must not remain isolated inside individual documents.

The following relationships are particularly important.

---

## 11.1 Watermark → Detector

A watermark methodology may require a corresponding detection methodology.

Therefore:

```text
R02 → R03
```

---

## 11.2 Watermark → Language

A watermark may behave differently across languages.

Therefore:

```text
R02 → R05
```

---

## 11.3 Detector → Language

A detector may exhibit language-specific performance.

Therefore:

```text
R03 → R05
R04 → R05
```

---

## 11.4 Transformation → Detector

Textual transformations may modify detector behavior.

Therefore:

```text
R06 → R03
R06 → R04
```

---

## 11.5 Transformation → Watermark

Textual transformations may modify watermark detectability.

Therefore:

```text
R06 → R02
```

---

## 11.6 Dataset → Everything

The validity of experimental conclusions depends on the validity of the
datasets used.

Therefore:

```text
R08 → R02
R08 → R03
R08 → R04
R08 → R05
R08 → R06
R08 → R07
```

---

## 11.7 Statistical Methodology → Everything

Experimental conclusions depend on appropriate statistical methodology.

Therefore:

```text
R07 → validation
R07 → certification
```

---

# 12. Research Evidence Flow

Scientific evidence should move through the following conceptual pipeline:

```text
SOURCE
  ↓
DISCOVERY
  ↓
SCREENING
  ↓
SOURCE REGISTRATION
  ↓
EVIDENCE EXTRACTION
  ↓
QUALITY ASSESSMENT
  ↓
RESEARCH DOMAIN
  ↓
CROSS-DOMAIN IMPACT
  ↓
EXPERIMENTAL REQUIREMENT
  ↓
VALIDATION
  ↓
PROJECT DECISION
```

The research process must preserve traceability across these stages.

---

# 13. Source of Truth Hierarchy

The project distinguishes between:

1. primary scientific sources;
2. official technical documentation;
3. reproducible implementations;
4. secondary scientific literature;
5. credible technical analyses;
6. community discussions;
7. informal observations.

Lower-level evidence must not silently override higher-quality evidence.

---

# 14. Research Registry

The authoritative index of research sources is:

`docs/00-project/RESEARCH-REGISTRY.md`

Every material source should be registered there.

---

# 15. Knowledge Backlog

Research questions that cannot yet be resolved should be recorded in:

`docs/00-project/KNOWLEDGE-BACKLOG.md`

They must not be silently converted into assumptions.

---

# 16. Open Questions

Questions requiring explicit project-level decisions belong in:

`docs/00-project/OPEN-QUESTIONS.md`

---

# 17. Assumptions

Scientific assumptions must be recorded in:

`docs/00-project/ASSUMPTION-REGISTRY.md`

An assumption is not equivalent to established evidence.

---

# 18. Decisions

Decisions based on research findings must be recorded in:

`docs/00-project/DECISION-LOG.md`

---

# 19. Documentation Change Queue

When research produces a finding that requires modification of an existing
document, the required change must be recorded in:

`docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md`

This prevents newly discovered knowledge from being lost.

---

# 20. Research-to-Documentation Rule

A new scientific finding must be propagated to all materially affected
documents.

Potentially affected areas include:

- scientific specification;
- architecture;
- validation;
- security;
- data;
- development;
- operations;
- certification.

The discovery document is not necessarily the final location of the
requirement.

---

# 21. Research Change Protocol

When new evidence materially changes an existing conclusion:

1. register the source;
2. record the evidence;
3. identify affected research domains;
4. identify affected assumptions;
5. identify affected decisions;
6. identify affected specifications;
7. add required documentation changes to the change queue;
8. update affected documents;
9. re-evaluate dependent experiments;
10. record the resulting decision.

---

# 22. Contradictory Evidence

Contradictory scientific evidence must be preserved.

The project must not resolve contradictions by deleting inconvenient
evidence.

Instead record:

- competing findings;
- methodological differences;
- dataset differences;
- language differences;
- model differences;
- statistical differences;
- confidence in each conclusion.

---

# 23. Negative Results

Negative results are first-class research outputs.

Examples include:

- a detector that fails;
- a watermark that is not detectable under a condition;
- a transformation that damages semantics;
- a language where a method performs poorly;
- a benchmark that proves invalid.

---

# 24. Reproducibility

Important findings should be reproducible from:

- source;
- methodology;
- data;
- configuration;
- software version;
- experiment manifest.

Where full reproduction is impossible, the limitation must be documented.

---

# 25. External Services

External/cloud services may be used for research where justified.

Their results must be recorded as external observations.

The project must distinguish:

```text
locally reproducible evidence
```

from:

```text
externally observed evidence
```

---

# 26. Temporal Validity

Some research findings are inherently time-sensitive.

Examples include:

- detector behavior;
- model behavior;
- benchmark performance;
- public APIs;
- available implementations.

Such findings should include dates and versions.

---

# 27. Research Freshness

The research program must periodically reassess whether previously important
evidence remains current.

---

# 28. New Methodology Rule

A materially new methodology must not be forced into an existing category if
doing so would conceal an important difference.

Instead:

1. identify the new methodology;
2. determine whether the taxonomy remains adequate;
3. update the taxonomy if required;
4. record the change;
5. propagate the consequences.

---

# 29. Deprecation

Research categories, methodologies and datasets may become obsolete.

Deprecation must preserve:

- historical identity;
- reason for deprecation;
- final version;
- known conclusions;
- references to successor methodologies where applicable.

---

# 30. Research Completeness

The research layer must not be considered complete merely because all files
exist.

Completion requires evidence that:

- relevant scientific areas have been investigated;
- major methodologies have been identified;
- relevant limitations have been recorded;
- contradictions have been investigated;
- experimental consequences have been propagated.

---

# 31. Research Gap

A research gap is explicitly recorded when:

- evidence is insufficient;
- methodology is unavailable;
- data is unavailable;
- reproduction is impossible;
- contradictory evidence cannot yet be resolved.

A research gap is preferable to an unsupported assumption.

---

# 32. Future Research

The architecture must permit new research domains to be introduced.

New domains should receive new identifiers rather than repurposing an
existing identifier in a way that destroys historical traceability.

---

# 33. Research Domain Status

Each research domain should use one of the following statuses:

- `PLANNED`
- `ACTIVE`
- `PARTIALLY COMPLETE`
- `BLOCKED`
- `DEPRECATED`
- `SUPERSEDED`

---

# 34. Current Domain Status

| Domain | Status |
|---|---|
| R01 Literature Research Methodology | ACTIVE |
| R02 Watermark Research | ACTIVE |
| R03 Watermark Detection Research | ACTIVE |
| R04 AI-Generated Text Detection Research | ACTIVE |
| R05 Multilingual & Linguistic Research | ACTIVE |
| R06 Transformation & Preservation Research | ACTIVE |
| R07 Evaluation & Statistical Methodology | ACTIVE |
| R08 Benchmark & Dataset Research | ACTIVE |

---

# 35. Research Completion Criteria

The research layer may only be considered mature when:

- source discovery methodology is operational;
- major watermark families have been reviewed;
- major watermark detection families have been reviewed;
- major AI-detection families have been reviewed;
- relevant multilingual risks have been investigated;
- transformation and preservation literature has been reviewed;
- evaluation methodology has been established;
- benchmark methodology has been established;
- important research gaps are explicitly recorded;
- findings have been propagated to dependent project areas.

---

# 36. Important Limitation

No research map can guarantee that every future scientific development will
be discovered.

The project therefore relies on:

- continuous literature monitoring;
- explicit research gaps;
- detector/watch registries;
- versioned evidence;
- periodic reassessment.

---

# 37. Final Principle

The research layer is not a static collection of papers.

It is a continuously maintained evidence system that connects scientific
knowledge to project requirements, experiments, validation and decisions.
"""

def main():
    TARGET.parent.mkdir(parents=True, exist_ok=True)

    if TARGET.exists():
        backup = TARGET.with_name(TARGET.name + ".bak")
        backup.write_text(TARGET.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"Backup created: {backup}")

    TARGET.write_text(CONTENT, encoding="utf-8")

    print(f"Updated: {TARGET}")
    print(f"Lines: {len(CONTENT.splitlines())}")
    print("Research map written successfully.")

if __name__ == "__main__":
    main()
