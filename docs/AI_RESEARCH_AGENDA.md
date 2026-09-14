# Working Patterns × AI

## A Pyragogy research track

Working Patterns is not limited to patterns between humans. Groups increasingly delegate interpretation, drafting, coordination, memory, search, recommendation, and action to AI systems and agents.

That creates a second research question:

> **Which patterns help humans and AI systems work together without hiding authority, evidence, dissent, cost, or failure?**

This is a natural Pyragogy problem: not “How can AI make groups more efficient?” but **what forms of human–AI arrangement improve collective capacity without quietly outsourcing judgment?**

## Status

The AI patterns in `data/ai-patterns/candidates.json` are **research candidates**.

They are not presented as validated best practices. They originate from tensions already visible in Working Patterns, UnPeeragogy, and human–AI practice, and must go through the same evidence discipline as every other pattern.

They remain:

```text
pattern_maturity: candidate
evidence_status: research-agenda
```

until a real evidence cycle justifies a change.

## Why human and AI patterns belong in one project

Several organisational problems survive the introduction of AI; the implementation changes.

| Human organisational problem | AI-mediated analogue |
|---|---|
| Informal authority | Agents gain practical authority without a mandate |
| False consensus | AI synthesis erases unresolved dissent |
| Hidden labour | Automation displaces review, correction, prompt, or monitoring work onto a minority |
| Weak traceability | Fluent recommendation hides claim–evidence relations |
| Failed handover | Agent/human handoff drops assumptions and unresolved questions |
| Ritual retrospective | AI advice is consumed but outcomes are never checked |
| Adoption ≠ implementation | “Human in the loop” is declared but the human only rubber-stamps |
| Shared provenance | Several agents are counted as independent despite sharing data/model/retrieval |

The same vocabulary — authority, implementation fidelity, outcome, cost, boundary condition, counterevidence — lets Working Patterns compare these without pretending they are identical.

## Initial research families

### 1. Epistemic integrity

Candidates:

- `WP-AI002` — Provenance Before Persuasion
- `WP-AI007` — Separate Observation, Interpretation, and Recommendation
- `WP-AI010` — Independence Before Multi-Agent Consensus

Research focus: whether interfaces and workflows make it easier for people to detect unsupported claims, source dependence, and interpretive leaps.

### 2. Delegation and authority

Candidates:

- `WP-AI001` — Friction Before Delegation
- `WP-AI003` — Bounded AI Mandate
- `WP-AI005` — Escalation Ladder for Autonomy
- `WP-AI011` — Name the Accountable Human Authority

Research focus: how autonomy is granted, expanded, revoked, and made contestable.

### 3. Reversibility and operational safety

Candidate:

- `WP-AI004` — Reversible Automation

Research focus: whether rollback, staging, bounded blast radius, and traceability improve recovery without creating reckless reliance.

### 4. Dissent and group cognition

Candidate:

- `WP-AI006` — Preserve Dissent Through Synthesis

Research focus: whether AI-mediated facilitation preserves decision-relevant minority information rather than manufacturing consensus or false balance.

### 5. Memory and handoff

Candidates:

- `WP-AI008` — Scoped Memory
- `WP-AI009` — Handoff With Epistemic Debt

Research focus: continuity without hidden context transfer, and agent/human handoffs that preserve unresolved state.

### 6. Learning loops

Candidate:

- `WP-AI012` — Close the AI Advice Loop

Research focus: turning AI advice into local experiments whose outcomes can update future reliance and the shared pattern corpus.

## The critical distinction: AI pattern vs software feature

A Working Pattern is not merely a feature request.

For example:

> “Add citations”

is a feature.

> “Expose claim-level provenance before persuasive recommendation, so a group can distinguish evidence from interpretation; measure whether this changes verification and decision quality”

is an investigable organisational/epistemic intervention.

Likewise “human in the loop” is too vague to qualify. We need to know **which human, with what authority, at which point, seeing what information, able to stop what action, and at what cost**.

## Research requirements before promotion

An AI candidate should not move from `candidate` merely because it sounds prudent.

A deep evidence cycle should seek:

1. a precise intervention;
2. measurable outcomes;
3. direct evidence or relevant adjacent evidence;
4. counterevidence and failed implementations;
5. boundary conditions;
6. costs, including human review and emotional/cognitive labour;
7. implementation fidelity;
8. alternatives;
9. independence/genealogy of evidence;
10. explicit unknowns.

## Pyragogy principle

The project should resist two symmetrical errors:

**AI maximalism:** automate because the system can.

**human exceptionalism:** reserve work for humans merely because humans traditionally did it.

Instead:

> **Allocate cognition, authority, and friction where they produce observable value — then check what actually happened.**

That claim itself is a research programme, not a conclusion.
