# No-Invention Rules for Automated Documentation Work

**Document type:** Agent constraint
**Status:** ACTIVE
**Purpose:** Prevent unsupported assumptions during repository analysis

## Fundamental Rule

An automated agent must not invent project facts.

If the repository does not establish something, the agent must say that it
is not established.

## Evidence Classes

Every substantive conclusion should be understood as belonging to one of
these classes:

### 1. DOCUMENTED FACT

Explicitly stated in an existing project document.

### 2. IMPLEMENTED FACT

Demonstrated by repository code or configuration.

### 3. VERIFIED FACT

Supported by an explicit validation, test, or verification result.

### 4. RESEARCH EVIDENCE

Supported by the project's research documentation or cited literature.

### 5. INFERENCE

A conclusion derived from documented evidence.

Inferences must be labelled as such when consequential.

### 6. PROPOSAL

A suggested future decision or design.

A proposal is not an existing requirement.

### 7. UNKNOWN

The available repository evidence is insufficient.

Unknown is an acceptable and preferred answer when evidence is absent.

## Forbidden Behaviors

The agent must not:

- invent requirements;
- invent APIs;
- invent interfaces;
- invent metrics;
- invent thresholds;
- invent benchmark results;
- invent scientific conclusions;
- invent certification status;
- invent supported languages;
- invent model capabilities;
- invent datasets;
- invent provenance;
- invent licenses;
- invent security guarantees;
- invent performance figures;
- invent deployment guarantees;
- invent external service behavior;
- invent user requirements;
- invent missing architecture;
- invent historical decisions.

## Missing Information

When information is missing:

1. identify the missing information;
2. identify where it would normally belong;
3. record it as an open issue or backlog item;
4. do not fill the gap with a plausible assumption.

## Ambiguous Information

When two documents provide different information:

- preserve both statements;
- identify the locations;
- do not silently select one;
- consult the authority matrix;
- classify the conflict.

## Scientific Claims

The agent must distinguish between:

- hypothesis;
- research observation;
- experimental result;
- validated result;
- general scientific claim;
- project requirement;
- certification claim.

These categories must not be collapsed.

## Numerical Values

Never invent:

- thresholds;
- tolerances;
- sample sizes;
- confidence levels;
- performance targets;
- storage limits;
- latency targets;
- accuracy targets.

If a value is not documented, report it as unspecified.

## Status Values

Do not infer lifecycle state from filenames or directory placement alone.

For example, the existence of a document does not prove that a capability
is:

- implemented;
- validated;
- active;
- certified.

## Code vs Documentation

Documentation does not prove implementation.

Implementation does not prove validation.

Validation does not automatically prove certification.

Certification does not imply universal scientific validity.

Preserve these distinctions.

## External Knowledge

General programming or engineering knowledge may be used to explain a
mechanical observation, but it must not be presented as a project decision.

If external knowledge is necessary to resolve an issue, identify it as
external knowledge rather than silently incorporating it into the project
specification.

## Proposed Changes

When proposing a change, explicitly label it:

`PROPOSAL — NOT CURRENT PROJECT FACT`

Do not modify authoritative requirements merely because a proposed design
appears reasonable.

## File Creation

Do not create a new project document merely because an expected concept is
missing.

First determine whether:

- an existing document already owns the concept;
- the concept belongs in the backlog;
- the concept requires a human decision.

## Historical Integrity

Do not rewrite history to make the repository appear more coherent.

Historical contradictions are evidence and may themselves be important.

## Confidence

When confidence is insufficient, use:

`UNKNOWN — INSUFFICIENT PROJECT EVIDENCE`

rather than a plausible completion.

## Final Rule

The correct automated behavior is:

> Preserve what is known, identify what is unknown, distinguish inference
> from fact, and escalate consequential decisions.

Never optimize for apparent completeness at the expense of truth.
