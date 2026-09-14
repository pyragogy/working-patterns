# Structured corpus

This directory contains the machine-readable Working Patterns corpus.

The schema is intentionally document-oriented and small. The research programme does not require a database at this stage.

## Registries

- `patterns/patterns.json` — pattern families and intervention components
- `claims/claims.json` — claim-level statements and evidence links
- `cases/cases.json` — observed or reported organisational/research cases
- `sources/sources.json` — source identity, access, study type, and licence state
- `schema/v0.1/corpus.schema.json` — structural contract for the registries

## Core rules

- IDs are persistent.
- A source and a study are conceptually distinct, even where the current v0.1 registry stores study metadata alongside a source.
- Evidence relations apply to a claim, not globally to a pattern.
- `unknown`, `not_reported`, `not_applicable`, and `not_verified` are not interchangeable.
- Pattern maturity is not a numeric confidence score.
- Implementation must not be inferred from the label an organisation uses for itself.

Run `python scripts/validate_corpus.py` to check IDs, enums, and cross-registry references.
