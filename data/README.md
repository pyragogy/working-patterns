# Structured corpus

This directory contains the machine-readable Working Patterns research corpus.

The model is deliberately document-oriented. At this stage the project needs stable IDs, traceable relations, and revision discipline more than a database.

## Registries

| Path | Purpose |
|---|---|
| `patterns/patterns.json` | Human organisational pattern families and components |
| `claims/claims.json` | Bounded claims plus source/case relation, locator, verification state, and limitations |
| `cases/cases.json` | Observed/reported organisational or experimental cases and clusters |
| `sources/sources.json` | Retrievable documents, access state, and licence state |
| `studies/studies.json` | Empirical/synthesis study records separated from publication/source identity |
| `genealogy/relations.json` | Dependence and lineage relationships that prevent false replication counts |
| `ai-patterns/candidates.json` | Pyragogy human–AI research candidates; currently research agenda only |
| `schema/v0.1/*.schema.json` | JSON Schema documentation for core record types |

## The key distinction

```text
Source ≠ Study ≠ Dataset ≠ Case ≠ Claim
```

A paper is not a replication. A preprint and journal article can describe the same study. Two meta-analyses can reuse the same primary studies. Two practitioner accounts can descend from the same organisational lineage.

The v0.1 corpus already separates Source and Study and records known genealogy. Dataset normalisation will only be introduced where dataset identity/reuse can be established without invention.

## Evidence relation

Evidence belongs to a claim:

```text
claim ← supports / complicates / contradicts / context-only ← source/study
```

It does **not** belong globally to a pattern.

## Human pattern status

`pattern_maturity`:

- `candidate`
- `documented`
- `corroborated`
- `contested`
- `revised`
- `retired`

`evidence_scope`:

- `narrow-context`
- `multi-context`
- `cross-domain`

No numeric confidence/evidence score is canonical.

## AI pattern status

The initial Pyragogy AI seeds are intentionally constrained to:

```text
pattern_maturity: candidate
evidence_status: research-agenda
```

The integrity gate rejects silent promotion before a research cycle changes those records deliberately.

## Unknown states

These concepts are not interchangeable:

- `unknown`
- `not_reported`
- `not_applicable`
- `not_verified`

Do not fill missing values by plausible inference merely to make records look complete.

## Validation

Run:

```bash
python scripts/validate_corpus.py
```

The validator checks stable IDs, enums, cross-registry references, source-less synthesis claims, AI seed status, genealogy references, and prohibited aggregate scoring fields.

For lightweight inspection:

```bash
python scripts/query.py list
python scripts/query.py pattern WP-C006
python scripts/query.py claim WP-C006-CL03
python scripts/query.py ai WP-AI006
python scripts/query.py source S14
```

These tools expose the corpus. They do not recommend a “best” pattern.
