# Evidence-aware query contract

This document is a **future interface contract**, not an implemented MCP specification.

Its purpose is to prevent a later API, RAG layer, or agent from flattening the corpus into generic recommendations.

## Input

A useful organisational query should eventually provide or elicit:

- concrete problem;
- unit of analysis (team, cooperative, community, network, decision episode, etc.);
- organisational scale;
- affected people/subgroups;
- current practice and implementation;
- decision/task type;
- reversibility;
- urgency/time horizon;
- communication mode;
- relevant language/access constraints;
- available facilitation/review capacity;
- authority: who can decide, stop, revise, or revoke;
- desired outcomes;
- unacceptable costs/risks.

Missing values should remain missing until asked or established.

## Output contract

A future evidence-aware advisor should return these sections in roughly this order.

### 1. Problem interpretation

State what problem the system believes it is addressing and what remains ambiguous.

Separate:

- user-reported facts;
- system interpretation;
- assumptions required to continue.

### 2. Missing context that could change the answer

Ask only for variables that materially affect transfer or choice among interventions.

### 3. Candidate interventions

Return a small set of relevant interventions, not an unranked catalogue.

For each candidate include:

- pattern/component ID;
- intervention in observable terms;
- why it matches the stated problem;
- evidence scope;
- current maturity;
- alternatives addressing the same problem.

### 4. Evidence

For each material claim expose:

- claim ID;
- source/study;
- locator;
- relation (`supports`, `complicates`, `contradicts`, `context-only`);
- unit/context;
- verification state;
- limitation.

The interface should never imply that source count equals independent confirmation.

### 5. Counterevidence and failure modes

Negative/mixed evidence should be visible without requiring a special “show criticism” action.

Failure modes must preserve their status:

- observed;
- reported;
- inferred;
- hypothetical.

### 6. Boundary conditions

Show conditions that limit transfer. Distinguish observed moderators/conditions from hypotheses.

### 7. Costs and distribution

Include time, facilitation, cognitive load, emotional labour, coordination, training, administration, compute/tooling where relevant — and **who pays each cost**.

### 8. What the corpus cannot currently tell you

Explicitly name unknowns.

Examples:

> “The evidence shows this protocol is used; it does not establish that it outperforms delegation.”

> “14 participants appears in observed decision episodes; it is not an efficacy threshold.”

### 9. Bounded local experiment

When causal transfer is uncertain, propose a reversible local test rather than a universal prescription.

A local experiment should specify:

- intervention;
- duration/decision class;
- expected outcome;
- comparison or baseline where feasible;
- cost measures;
- affected subgroups;
- stop/reversal condition;
- follow-up date;
- what result would change the recommendation.

### 10. Provenance

The answer should remain traceable to corpus version and claim IDs.

## AI-specific extension

For AI-mediated patterns additionally expose:

- model/agent role;
- permissions and mandate;
- accountable human/governance body;
- reversibility;
- human review point;
- memory scope;
- source/retrieval dependence;
- multi-agent independence dimensions;
- compute and review cost;
- whether the AI statement is observation, interpretation, or recommendation.

## Forbidden shortcut

The future interface should not produce:

```text
Best pattern: X
Confidence: 91%
```

unless a future research method can justify those exact constructs and their calibration. Nothing in schema v0.1 does.
