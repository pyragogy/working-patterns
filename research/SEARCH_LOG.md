# Search Log

## Purpose

Working Patterns is currently an **exploratory evidence-mapping project**, not a completed systematic review. This log exists so future evidence cycles can be audited at the level of actual searches rather than reconstructed from memory.

A search log records **how evidence was looked for**. It is distinct from the source registry, which records sources that entered the corpus.

## Retrospective limitation — cycles 0.1 and 0.2

Research Maps 0.1 and 0.2 were produced before a prospective search log was part of the method.

The repository preserves the sources, locators, verification status, research families, claims, cases, genealogy notes, and known gaps from those cycles. It does **not** contain a complete reproducible record of every query string, search engine/database, result count, screening decision, or exclusion reason used during those cycles.

Those details will not be retroactively invented.

Therefore:

> **The 0.1/0.2 corpus is auditable at the source/claim level, but not reproducible as a systematic search.**

This is a methodological limitation of the current corpus.

## Prospective rule — cycle 0.3 onward

Every substantive search intended to add, remove, promote, downgrade, or materially reinterpret a claim should record, where applicable:

- date;
- research cycle;
- pattern / component / question;
- source system or database;
- exact query string;
- filters or date/language limits;
- result count if exposed by the source;
- records screened;
- records included;
- material exclusions and exclusion reasons;
- operator / reviewer;
- access level (`FT`, `ABS`, `PR`, etc.);
- notes about duplicate datasets, shared samples, or lineage;
- commit or research artifact in which the search affected the corpus.

Absence of a result must not be rewritten as evidence of absence.

## Log

| Date | Cycle | Target | Source / database | Exact query or route | Result / access | Corpus consequence |
|---|---|---|---|---|---|---|
| 2026-09-14 | 0.3-prep | `WP-C002-A` / S03 | public web + SAGE landing page | `"Do Team and Individual Debriefs Enhance Performance? A Meta-Analysis" pdf full text` | Publisher abstract located; methods-level full-text audit not completed | Keep `corroborated` explicitly **provisional** |
| 2026-09-14 | 0.3-prep | `WP-C002-A` / S04 | public web + PubMed + APA supplemental material | `"A meta-analysis of the effectiveness of the after-action review" pdf full text` | PubMed abstract and APA supplemental-material landing page located; main full-text methods not audited | Keep `corroborated` explicitly **provisional** |
| 2026-09-14 | 0.3-prep | `WP-C002-D` / S05 | public web + Springer/JSTOR/ResearchGate metadata | `"A Meta-Analysis of Task and Training Characteristics that Contribute to or Attenuate the Effectiveness of the After-Action Review" pdf full text` | Article metadata/abstract and partial full-text representations located; complete methods audit not recorded | Do not treat S05 as an independent replication of S04 |

## Exclusion reasons vocabulary

Use a short controlled vocabulary when possible:

- `wrong-intervention`
- `wrong-outcome`
- `wrong-unit-of-analysis`
- `protocol-only`
- `problem-evidence-only`
- `duplicate-publication`
- `shared-dataset`
- `insufficient-method-detail`
- `not-accessible-for-verification`
- `outside-scope`
- `language-access-limitation`

Add free-text explanation when a code would hide an important judgment.

## Screening and reviewer independence

At present, most screening and coding has been performed by a single researcher with AI-assisted research workflows. That is a source of correlated judgment error.

A second-reader procedure is specified in [`../docs/SECOND_READER_PROTOCOL.md`](../docs/SECOND_READER_PROTOCOL.md). Until independent recoding is actually completed, the repository must not imply dual screening or inter-rater agreement.

## What this log is not

This file is not a PRISMA claim and does not make the existing corpus systematic by declaration.

Its purpose is narrower: make the next research cycle **more reproducible than the previous one**.