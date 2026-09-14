# Method and architecture decision log

This log records project-level decisions that materially constrain how Working Patterns should evolve.

## ADR-001 — Evaluate intervention × context × outcome

**Status:** accepted · 2026-09-14

Broad families such as consensus, care, conflict, or async work do not receive a single evidence reputation. The unit of evaluation is a specific intervention as implemented in a context relative to a specified outcome.

**Reason:** Research Map 0.2 showed that evidence often supports only one component while adjacent components remain unknown or contested.

## ADR-002 — Evidence relations belong to claims

**Status:** accepted · 2026-09-14

`supports`, `complicates`, `contradicts`, and `context-only` connect a source/study to a claim, not a whole pattern.

**Reason:** the same source can support one proposition while complicating another.

## ADR-003 — No aggregate evidence score

**Status:** accepted · 2026-09-14

The canonical corpus will not expose a single numeric confidence/evidence/quality score for a pattern.

**Reason:** evidence type, context, implementation fidelity, outcome, dependence, and counterevidence cannot be responsibly collapsed into one scalar without introducing hidden normative weights.

## ADR-004 — Source ≠ study ≠ dataset

**Status:** accepted · 2026-09-14

Documents, empirical studies, and datasets are distinct entities even when v0.1 has not yet fully normalised all three registries.

**Reason:** publication count is not replication count.

## ADR-005 — Preserve historical research maps

**Status:** accepted · 2026-09-14

Research Map 0.1 and 0.2 are snapshots. New evidence revises the live corpus and creates a new cycle; old maps are not silently rewritten to match later interpretations.

## ADR-006 — Corpus before platform

**Status:** accepted · 2026-09-14

No database, vector store, RAG layer, website, or MCP is required to justify the research. Product infrastructure follows a stable corpus.

**Reason:** otherwise software architecture can begin dictating the epistemic model.

## ADR-007 — AI patterns use the same burden of proof

**Status:** accepted · 2026-09-14

Pyragogy AI patterns are first-class research candidates but remain `candidate / research-agenda` until evidence changes their status.

**Reason:** coherence with Pyragogy is not evidence of effectiveness.

## ADR-008 — Commercial outputs cannot close the evidence layer

**Status:** provisional · 2026-09-14

A future paid handbook/advisor may add editorial, design, workflow, and service value while the evidence needed to inspect claims should remain traceable.

**Reason:** recommendation quality depends on contestability; closed provenance would undermine the core method.
