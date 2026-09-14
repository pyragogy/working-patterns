# Second Reader Protocol

## Why this exists

Working Patterns currently has a **single-researcher risk**: most source screening, claim extraction, relation coding, and pattern assessment have been performed in one research workflow, often with AI assistance.

Provenance hashes and validation rules protect record integrity. They do not create independent judgment.

The purpose of a second reader is therefore not ceremonial peer review. It is to test whether another informed reader can reproduce the core epistemic judgments from the cited material.

## Initial target

The first independent pass should recode at least **10 claims**, sampled across `WP-C001`–`WP-C007`, with deliberate inclusion of:

- at least one `supports` claim;
- at least one `complicates` claim;
- at least one `contradicts` claim;
- at least one `context-only` claim;
- at least one abstract-only (`ABS`) claim;
- at least one full-text (`FT`) claim;
- `WP-C002-A`, because it currently carries the strongest maturity label;
- one claim involving evidence that establishes a problem but not the proposed intervention.

This is a minimum credibility check, not a substitute for dual screening of a systematic review.

## What the second reader receives

For each sampled claim, provide:

1. the exact proposition;
2. the cited source and locator;
3. the relevant pattern/component definition;
4. the current verification level;
5. enough source material to inspect the claim directly.

Where practical, do **not** reveal the current evidence relation (`supports`, `complicates`, etc.) until the independent coding has been recorded.

## Independent coding fields

The second reader records:

- `claim_supported_by_source`: `yes | partly | no | cannot-verify`;
- `evidence_relation`: `supports | complicates | contradicts | context-only`;
- `problem_vs_intervention`: `problem | intervention | both | neither`;
- `implementation_observed`: `yes | no | unclear | not-applicable`;
- `outcome_match`: `direct | proxy | adjacent | none`;
- `verification_possible`: `FT | ABS | PR | other | no`;
- `material_limitation_missing`: free text;
- `recommended_change`: `none | wording | relation | verification | maturity | remove`;
- rationale.

## Adjudication

Disagreement is not automatically resolved in favour of the original coding.

For every material disagreement:

1. preserve both judgments;
2. identify whether the disagreement concerns evidence, interpretation, taxonomy, or source access;
3. inspect the relevant passage together if possible;
4. record the adjudicated result and rationale;
5. create a revision record when the live corpus changes.

A disagreement that cannot be resolved should remain visible rather than being averaged into a score.

## Reporting

When the first second-reader pass is complete, publish a small audit table containing:

- sampled claim IDs;
- agreement/disagreement by field;
- material changes made;
- unresolved disagreements;
- reader identity or role if they consent to attribution;
- date and corpus commit reviewed.

Do not report an inter-rater reliability statistic unless the sample and coding design make that statistic meaningful.

## AI assistance

An AI system may help retrieve passages, compare records, or format the audit, but it does **not** count as the independent second reader when it shares the same prompts, corpus, model lineage, or researcher supervision that produced the original coding.

The independence sought here is independent **human judgment** on whether the evidence supports the recorded proposition.

## Success criterion

This protocol succeeds if it can reveal at least one place where the corpus wording, relation, verification level, or maturity judgment should become more precise.

Agreement is not the goal. **Error discovery is.**