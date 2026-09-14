# Research provenance

Working Patterns began with two extended research cycles produced on 14 September 2026 and supplied by the project owner as Markdown research reports.

The repository stores **normalised canonical research-map documents** and structured records derived from those reports. Normalisation removes chat/session delivery notes, repairs presentation where necessary, and separates registries into machine-readable files. It must not silently strengthen the evidence status of any claim.

## Source research outputs

| Cycle | Role | Original byte length | SHA-256 |
|---|---|---:|---|
| Research Map 0.1 | Field reconnaissance | 51,624 bytes | `496307c382ccc48fa21ff955a151f8def4919f59a15d90cfbca2befce2f9bf18` |
| Research Map 0.2 | Deep Evidence Cycle | 128,302 bytes | `cce34232b69d2bba30bbc9d770b515715439a10e5fefc1c9c5f4e0592ebe4034` |

Hashes refer to the exact Markdown inputs supplied for repository construction.

## Transformation rules

During normalisation:

1. research findings may be restructured for readability;
2. stable IDs (`WP-C*`, `K*`, `S*`, claim IDs) are preserved;
3. evidence relations are not upgraded;
4. `unknown` remains unknown;
5. practitioner material is not relabelled as experimental evidence;
6. connected provenance lines are not converted into independent confirmations;
7. licensing uncertainty remains explicit;
8. project-authored synthesis remains distinguishable from source-derived claims.

## Canonical layers

The repository contains three complementary layers:

- `research/` — narrative maps and methodological history;
- `data/` — machine-readable working corpus;
- Git history — revision provenance.

The narrative research maps explain **why** records were classified as they were. The structured corpus is the working interface for validation and future software.

## Research-map status

Research Map 0.1 and 0.2 are historical snapshots. Later evidence should revise the structured corpus and create a new research cycle rather than rewriting old snapshots to match current conclusions.
