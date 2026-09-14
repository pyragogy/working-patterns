# Working Patterns

**Evidence-aware organisational patterns: what appears to work, where, why, at what cost, and where it breaks.**

Working Patterns is an open research project for studying organisational practices used by teams, cooperatives, open-source projects, communities, networks, and other groups trying to work together.

It is not a catalogue of universal best practices.

The core research question is:

> **Which organisational patterns appear to work, for which problems, under which conditions, according to what evidence — and where do they stop working?**

The project treats a pattern as an investigable intervention rather than a slogan. The basic unit of evaluation is:

**problem → intervention → implementation → outcome → evidence → conditions**

A source can document a protocol, observe its use, compare it with an alternative, measure an outcome, or propose a mechanism. These are not treated as equivalent forms of support.

## Research principles

Working Patterns separates:

- what is **claimed**;
- what is **observed**;
- what is **supported**;
- what is **complicated or contradicted**;
- what remains **unknown**.

A source existing is not the same as a source supporting a claim. A practice being adopted is not the same as it being implemented. Evidence that a problem exists is not evidence that a proposed solution solves it.

The project deliberately keeps multiple outcomes separate, including operational capacity, decision quality, participation, power distribution, sustainability, learning, legitimacy, and continuity. A practice may improve one while worsening another.

## Current research status

The first two research cycles were completed on **14 September 2026**.

### Research Map 0.1 — field mapping

The first cycle mapped 19 research families, extracted Richard D. Bartlett's *Patterns for Decentralised Organising* as Seed Corpus 001, established a provisional problem taxonomy, and tested the first candidate-pattern records.

### Research Map 0.2 — deep evidence cycle

The second cycle tested seven high-priority pattern families:

| ID | Pattern family | Current assessment |
|---|---|---|
| `WP-C001` | Explicit norms and enforcement | documented · narrow-context · context-limited |
| `WP-C002` | Structured retrospectives / debriefs with follow-up | debrief core corroborated; full package documented |
| `WP-C003` | Explicit distribution of care work | documented · narrow-context |
| `WP-C004` | Informal power and mandates | documented · narrow-context |
| `WP-C005` | Consensus / consent / lazy consensus | documented · narrow-context |
| `WP-C006` | Asynchronous decision-making | documented · narrow-context · context-limited |
| `WP-C007` | Conflict and dissent | contested as a general pattern |

The strongest methodological result is that a whole family such as “consensus”, “care”, or “conflict” cannot responsibly receive one reputation. Evaluation must attach to a specific intervention, implementation, context, and outcome.

## Evidence relations

Claims can have multiple evidence links. Each link describes what a source does **for that specific claim**:

- `supports`
- `complicates`
- `contradicts`
- `context-only`

These relations are not assigned globally to an entire source or pattern.

## Pattern maturity

Working Patterns currently uses:

- `candidate`
- `documented`
- `corroborated`
- `contested`
- `revised`
- `retired`

`documented` means that an intervention is sufficiently described to study. It does **not** mean that it has been shown to be effective.

Evidence scope is tracked separately, for example `narrow-context`, `multi-context`, or `cross-domain`.

## Repository structure

```text
working-patterns/
├── README.md
├── METHODOLOGY.md
├── CONTRIBUTING.md
├── LICENSING.md
├── CITATION.cff
├── research/
│   ├── research-map-0.1.md
│   └── research-map-0.2.md
├── data/
│   ├── patterns/
│   ├── claims/
│   ├── cases/
│   ├── sources/
│   └── schema/v0.1/
├── scripts/
│   └── validate_corpus.py
└── .github/workflows/
    └── validate.yml
```

## Why structured data

The research corpus is intended to remain readable by humans while also being reusable by software. Stable IDs and explicit relations are therefore first-class parts of the method.

The schema is being designed so the same corpus can eventually support several outputs without rewriting the research:

**open research corpus → handbook → evidence-aware MCP/advisor**

No MCP, RAG system, recommendation engine, or website is part of the initial research infrastructure. Product architecture follows the evidence, not the reverse.

## Future advisory behaviour

A future machine interface should not answer:

> “Use consensus.”

It should be able to answer questions such as:

> “We are a remote team of 14 people. Synchronous decisions exclude several members. Which patterns are relevant, what evidence supports them, under which conditions, what alternatives exist, and what could go wrong?”

A responsible answer should expose uncertainty, counterevidence, implementation requirements, costs, and missing contextual information before recommending a local experiment.

## Seed corpus

The first seed is Richard D. Bartlett's [Patterns for Decentralised Organising](https://github.com/rdbartlett/patterns), originally produced from work with Enspiral and Loomio. The seed is CC0, but Bartlett, Loomio, and Enspiral are treated as a connected provenance line rather than independent confirmations.

Working Patterns expands beyond this seed into organisational research, team science, cooperative governance, peer production, facilitation, commons governance, deliberation, and related fields.

## Research integrity

Working Patterns is currently an exploratory evidence-mapping project, **not a completed systematic review**. Search coverage, full-text access, dataset overlap, publication bias, implementation fidelity, and survivorship bias are tracked as limitations rather than silently converted into confidence.

In particular:

> **Unknown does not mean zero, absent, ineffective, or disproven.**

## Licensing

There is deliberately no blanket assumption that everything cited or studied here can be commercially republished. Research notes, quotations, reusable licensed material, and original Working Patterns prose are tracked separately.

See [`LICENSING.md`](LICENSING.md).

## Relationship to Pyragogy

Working Patterns is a project of the [Pyragogy](https://github.com/pyragogy) research ecosystem. It shares the principle that evidence, interpretation, counterevidence, and revision should remain distinguishable.

Its aim is practical but not prescriptive:

> **A consultation grounded in evidence and uncertainty, not an automatic selector of best practices.**
