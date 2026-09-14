# Contributing to Working Patterns

Working Patterns welcomes contributions that improve the **traceability, specificity, or falsifiability** of the corpus.

Agreement is not the goal. Useful contributions include evidence that narrows, complicates, contradicts, or revises an existing interpretation.

## Before contributing

Read [`METHODOLOGY.md`](METHODOLOGY.md).

The most important rule is:

> **Do not attach evidence to a pattern in general when it only supports a specific claim, component, context, or outcome.**

## Good contributions

Examples include:

- a study directly evaluating one intervention component;
- a negative or mixed case;
- evidence from people who left or stopped using a practice;
- a better source locator;
- identification of dataset reuse or shared provenance;
- a correction to a licence record;
- a boundary condition that materially changes transferability;
- an alternative intervention for the same organisational problem;
- evidence that adoption and implementation diverged;
- a revision that preserves the previous interpretation.

## Evidence submissions

For each proposed evidence link, provide as much of the following as possible:

- claim ID or proposed claim text;
- source title, author, year, URL/DOI;
- exact locator (page, section, table, figure, paragraph, timestamp, commit, etc.);
- evidence/study type;
- unit of analysis and context;
- relation: `supports`, `complicates`, `contradicts`, or `context-only`;
- limitations;
- whether the full text was actually inspected;
- known dataset or case overlap with existing records.

## Negative cases

A failed organisation is not automatically evidence that a pattern caused the failure. Record the observed outcome separately from causal interpretation.

Do not replace missing direct counterevidence with generic criticism.

## New patterns

A candidate pattern should identify:

1. the organisational problem;
2. the intervention in observable terms;
3. proposed mechanism(s);
4. relevant context and unit of analysis;
5. intended outcome(s);
6. known alternatives;
7. initial provenance.

Broad labels such as “use consensus” or “build trust” are not sufficiently specific.

## Data changes

Structured records use persistent IDs. Do not silently reuse or renumber IDs.

If a concept is split or materially revised, add a revision record rather than rewriting its history as if the earlier interpretation never existed.

Run:

```bash
python scripts/validate_corpus.py
```

before submitting structured-data changes.

## Licensing and third-party material

Do not paste substantial copyrighted text, figures, tables, or proprietary material into this repository merely because it is available online.

Research notes, quotations, reusable licensed material, and original Working Patterns prose are separate categories. See [`LICENSING.md`](LICENSING.md).

## Tone

Prefer precise claims over advocacy. State what the evidence permits and what it does not.

“Unknown” is an acceptable and often valuable result.
