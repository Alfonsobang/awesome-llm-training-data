# Financial Agent Evaluation: Positioning Thesis

This document defines the direction this project should take after the initial awesome-list phase failed to attract attention.

The core problem is not that the repository needs more links. The core problem is that the market already has too many generic AI lists. A useful project in this space needs to be a runnable evaluation harness with a sharp domain thesis.

## The Sharp Thesis

Financial-agent evaluation should move from static finance Q&A to auditable tool-use evaluation.

The interesting benchmark is not "can the model answer a finance question?" The interesting benchmark is:

- can an agent find the right public source,
- extract the right number with units and fiscal-period discipline,
- avoid future-data leakage,
- cite evidence,
- refuse unsafe investment-advice requests,
- preserve a trace of tool calls and observations,
- stay stable across repeated attempts,
- and produce artifacts that another evaluator can audit?

That is the open-source gap this project should target.

## Public Benchmark Context

The strongest agent-evaluation projects are not just lists. They package tasks, environments, reports, and verification logic.

Useful reference points:

- [SWE-bench](https://github.com/swe-bench/SWE-bench) evaluates agents on real GitHub issue resolution, which made coding-agent evaluation concrete and reproducible.
- [WebArena](https://github.com/web-arena-x/webarena) frames autonomous-agent evaluation around realistic web environments rather than static questions.
- [OSWorld](https://github.com/xlang-ai/OSWorld) focuses on open-ended computer-use tasks in real operating-system environments.
- [FinanceBench](https://github.com/patronus-ai/financebench) is already a major reference point for open-book financial question answering.

The implication for this project is simple: do not build another broad resource list or another finance QA clone. Build the missing middle: a small financial-agent evaluation harness that checks public-source tool use, evidence, cutoffs, compliance boundaries, and trajectories.

## Why The Previous Positioning Was Weak

The original project looked like an awesome list with extra notes. That is not enough to earn stars in a crowded AI market.

Weak signals:

- too much "curated resources" language,
- not enough runnable value on the first screen,
- no memorable project category,
- no strong artifact that other teams can plug into their own eval stack,
- no obvious reason for a Harbor/OpenClaw/agent-eval user to come back.

Strong signals to build instead:

- one-command runnable evaluation,
- passing and failing examples,
- deterministic verifiers,
- task families that map to real financial-agent failures,
- source-governance metadata,
- trajectory / ATIF audit examples,
- machine-readable repo entry points,
- and a clear roadmap toward a small benchmark rather than a link collection.

## The Attractive Project Shape

The project should evolve into:

> A public, synthetic-first evaluation harness for financial LLM agents, focused on tool-use evidence, source grounding, temporal discipline, compliance boundaries, and trajectory audits.

This is more attractive than a generic benchmark because it combines four current demand areas:

- agent evaluation,
- tool-use and browser/search workflows,
- financial-domain reliability,
- and governance / compliance evidence.

## Target Users

The repository should be built for people who might actually star, fork, or cite it:

- LLM evaluation engineers building agent eval suites,
- financial AI teams designing public-safe test tasks,
- data quality leads responsible for source governance and leakage control,
- agent-framework maintainers who need realistic task examples,
- researchers studying trajectory-aware evaluation and repeated-trial metrics,
- coding agents that need machine-readable instructions to extend the repo.

## What Makes It Star-Worthy

People star projects when they believe a repo will save them time later.

For this project, the strongest star triggers are:

- "I can run it in one command."
- "It includes both good and bad examples."
- "It tests failures I actually worry about."
- "It is finance-specific without leaking private data."
- "It gives me task templates I can adapt."
- "It has enough governance language to be safe in a regulated setting."
- "It connects to the agent-eval stack instead of being another static dataset."

## What Makes It AI-Agent-Friendly

AI agents and LLM repo readers are more likely to use a project when it has:

- `llms.txt`,
- `AGENTS.md`,
- stable command snippets,
- clear directory structure,
- small deterministic tests,
- JSON artifacts,
- machine-checkable source manifests,
- and examples of both passing and failing outputs.

This project should optimize for that as a first-class distribution channel.

## The Next Product Surface

The next most attractive artifact is a mini benchmark called:

> FinAgentBench Seed

It should not claim to be a full benchmark yet. It should be a reproducible seed with concrete task families:

1. **Search**: find the correct public filing or disclosure page.
2. **Lookup**: extract exact financial values with units, period, and citation.
3. **Filing QA**: answer a grounded question using only provided/public evidence.
4. **Tool-use Trace**: audit tool order, failed-call recovery, and observation linkage.
5. **Forecasting Cutoff Discipline**: produce bounded forecasts without post-cutoff evidence.
6. **Backtest Discipline**: run a toy strategy without future-data leakage.
7. **Compliance Boundary**: refuse guaranteed-return, personalized-advice, private-data, or insider-information requests.

Each task should eventually include:

- task spec,
- synthetic or public-safe fixture,
- expected artifact schema,
- deterministic verifier,
- known-bad candidate,
- trajectory expectations,
- source-governance metadata,
- and repeated-trial aggregation.

## Differentiation

This project should not compete with general-purpose agent benchmarks. It should be narrower and more practical.

Do not position it as:

- the largest finance benchmark,
- the most comprehensive evaluation suite,
- proof of production readiness,
- a trading leaderboard,
- or a private-domain benchmark.

Position it as:

- small,
- runnable,
- public-safe,
- inspectable,
- finance-specific,
- governance-aware,
- and useful for building better internal evaluations.

## Build Priorities

High priority:

- make the existing seed easy to run and understand,
- add realistic known-bad examples,
- add browser/search task scaffolds,
- add trajectory-level checks,
- add repeated-trial reports,
- publish crisp diagrams and task cards,
- keep README focused on the runnable harness.

Low priority:

- adding more links,
- broad benchmark claims,
- abstract essays,
- large datasets,
- model rankings,
- or anything that smells like investment advice.

## Public Message

The public message should be simple:

> Financial agents fail in ways that normal Q&A benchmarks miss: wrong sources, wrong units, future-data leakage, unsafe advice, missing citations, and unstable tool trajectories. This repo is a public-safe starter harness for testing those failures.

That is the sentence this project should keep earning.
