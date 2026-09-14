# Versioning

Working Patterns versions the **research corpus and schema**, not truth.

The project uses semantic-style versions for repository releases:

- **PATCH** — corrections that do not change IDs or interpretation materially: typos, broken URLs, clearer locators, metadata fixes.
- **MINOR** — additive or interpretive research changes: new patterns/claims/cases/sources, new evidence relations, a pattern status revision with preserved history, backwards-compatible schema fields.
- **MAJOR** — incompatible data-model or identifier-policy changes.

## Research-map versions

Research Maps (`0.1`, `0.2`, …) are named research cycles and remain immutable historical snapshots except for clearly marked clerical corrections.

## Schema versions

Structured records declare `schema_version`. Schema changes should be documented in the changelog and, once consumers exist, accompanied by migration notes.

## Pattern IDs

Persistent IDs are not version numbers. `WP-C002` remains `WP-C002` when its assessment changes. Splits, merges, or retirement should be represented through revision/genealogy records rather than silent ID reuse.
