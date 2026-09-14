<div align="center">
  <img src="docs/assets/working-patterns-banner.svg" alt="Working Patterns — evidence, conditions, failures, practice" width="100%" />
</div>

<p align="center">
  <strong>What helps groups work together — and where does it stop working?</strong>
</p>

<p align="center">
  <a href="https://github.com/pyragogy/working-patterns/actions/workflows/validate.yml"><img src="https://github.com/pyragogy/working-patterns/actions/workflows/validate.yml/badge.svg" alt="Corpus integrity" /></a>
  <img src="https://img.shields.io/badge/research-exploratory-6e7781" alt="Research status: exploratory" />
  <img src="https://img.shields.io/badge/AI%20track-questions%2C%20not%20answers-d29922" alt="AI track: questions, not answers" />
</p>

---

# Working Patterns

Groups keep running into the same problems:

- decisions get stuck;
- power concentrates informally;
- the same people carry care and maintenance work;
- meetings exclude people who cannot be present;
- conflict becomes personal;
- teams repeat mistakes without learning from them.

There are many books, frameworks, facilitation methods and “best practices” that claim to help.

**Working Patterns asks a simpler question:**

> **What seems to help, for which problem, under which conditions — and where does it fail?**

This repository collects organisational practices and tests them against available evidence, cases, counterexamples and known limits.

It is not a handbook of universal answers.

It is a public research project about **how groups actually work**.

---

## The basic idea

Instead of saying:

> “Consensus works.”

we ask:

- Which kind of consensus?
- For what kind of decision?
- Who can object?
- What happens when somebody stays silent?
- What does it cost in time and attention?
- What evidence do we actually have?

Instead of saying:

> “Retrospectives improve teams.”

we ask:

- Was there really a structured debrief?
- Did the group identify an action?
- Did anybody carry it out?
- Was the result measured?

The research chain is:

```text
problem → intervention → implementation → outcome → evidence → conditions
```

That is the core of Working Patterns.

---

## What is in the repository today?

The first research cycle goes deep on seven organisational areas:

| Pattern family | What we currently know |
|---|---|
| **Explicit norms and enforcement** | documented, but context matters |
| **Structured retrospectives / debriefs** | the strongest current candidate; the core debrief is only **provisionally corroborated** while full-text evidence is still being audited |
| **Distribution of care work** | the problem is clearer than the evidence for the proposed solutions |
| **Informal power and mandates** | formal roles do not automatically remove informal power |
| **Consensus / consent / lazy consensus** | these are different procedures, not one single “consensus pattern” |
| **Asynchronous decision-making** | useful in some contexts, but “async = inclusive” is not established |
| **Conflict and dissent** | the broad claim that “more conflict improves decisions” does not hold up |

The structured corpus currently contains:

- 7 human pattern families;
- 32 research claims;
- 11 cases;
- 21 sources;
- 15 studies or syntheses;
- explicit links showing where evidence may not be independent.

The numbers are inventory, not a score of truth.

---

## Why this may be useful

Imagine a remote team says:

> “Half the group misses synchronous decisions. Should we move decisions async?”

A normal best-practice guide might simply say yes.

Working Patterns should eventually be able to say:

- async may help with time-zone access;
- access does not automatically mean influence;
- written participation creates reading and coordination costs;
- silence needs a clear meaning;
- somebody still needs authority to close the decision;
- consent, lazy consensus, delegation or hybrid meetings may be alternatives;
- here is the evidence we have;
- here is what we still do not know.

That is the project in one example.

---

## The Pyragogy AI track

Groups are also starting to include AI systems that search, summarise, recommend, remember, coordinate and sometimes act.

That creates a new question:

> **What changes when part of the group is AI?**

We have written 12 early research questions around problems such as:

- delegating too much authority to an agent;
- fluent answers hiding weak evidence;
- AI summaries erasing minority positions;
- several agents appearing independent when they share the same model or data;
- automation becoming difficult to reverse;
- “human in the loop” becoming little more than rubber-stamping.

Examples include:

- **Friction Before Delegation**
- **Provenance Before Persuasion**
- **Preserve Dissent Through Synthesis**
- **Independence Before Multi-Agent Consensus**
- **Reversible Automation**
- **Handoff With Epistemic Debt**

These are **questions, not validated patterns**.

They are deliberately marked as `candidate / research-agenda` until evidence says otherwise.

Read more in [`docs/AI_RESEARCH_AGENDA.md`](docs/AI_RESEARCH_AGENDA.md).

---

## What makes the project careful

A few rules matter more than the technology behind the repository:

**A problem is not proof of a solution.**  
Evidence that invisible work exists does not prove that rotating it solves the problem.

**Adoption is not implementation.**  
A group saying “we use consensus” does not tell us what actually happened.

**One outcome is not overall success.**  
Participation may improve while time cost or conflict increases.

**Several papers are not always several independent confirmations.**  
They may use the same dataset, cases or intellectual lineage.

**Unknown means unknown.**  
It does not mean ineffective, absent or disproven.

---

## This is still early research

Working Patterns is exploratory.

The current evidence base is small, mostly anglophone, and many contexts are still missing. Most of the current coding has also been done by one researcher with AI assistance.

That is not hidden, and it is not a reason to inflate the conclusions.

The goal is simply to make every next version **less wrong, more testable and more useful**.

---

## Where it could go

The corpus can eventually support several things:

```text
open research corpus
        ↓
practical handbook / pattern cards
        ↓
evidence-aware organisational advisor
```

The future advisor should not tell a group what to do immediately.

It should first ask enough questions to understand the context, then show:

```text
possible patterns
+ evidence
+ counterevidence
+ costs
+ failure modes
+ alternatives
+ unknowns
```

That is the Pyragogy direction: **AI that helps expose assumptions and disagreement instead of simply producing confident recommendations.**

---

## Explore

- [`METHODOLOGY.md`](METHODOLOGY.md) — how evidence is handled
- [`Research Map 0.2`](research/research-map-0.2.md) — the first deep evidence cycle
- [`data/`](data/) — the machine-readable corpus
- [`docs/AI_RESEARCH_AGENDA.md`](docs/AI_RESEARCH_AGENDA.md) — the human–AI research questions
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — how to bring evidence, counterevidence or a failed case

---

## Contribute friction

A useful contribution does not have to confirm the project.

A failed implementation, counterexample, abandoned practice or source showing that one of our claims is wrong may be more valuable than another success story.

> **Use it. Test it. Contradict it.**

<p align="center">
  <strong>A Pyragogy research project.</strong>
</p>
