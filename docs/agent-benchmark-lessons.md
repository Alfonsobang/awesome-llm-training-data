# Agent Benchmark Lessons

This page summarizes what this project should learn from influential agent and finance benchmarks. It is not a ranking and does not claim that these projects are directly comparable.

## Reference Projects

| Project | Useful lesson for this repo |
| --- | --- |
| [SWE-bench](https://github.com/swe-bench/SWE-bench) | Concrete tasks plus executable evaluation are more memorable than broad commentary. |
| [WebArena](https://github.com/web-arena-x/webarena) | Realistic tool-use environments make agent evaluation more compelling than static prompts. |
| [OSWorld](https://github.com/xlang-ai/OSWorld) | Open-ended computer-use tasks need setup, execution, and evaluation infrastructure. |
| [FinanceBench](https://github.com/patronus-ai/financebench) | Finance QA needs evidence strings and public-document grounding, but agent evaluation should go beyond final answers. |

## What To Copy

- Clear benchmark contract.
- Runnable setup.
- Small starter subset.
- Reproducible examples.
- Reports and artifacts.
- Public issue discussions.
- Conservative claims.

## What Not To Copy Blindly

- Leaderboard-first positioning before the task suite is mature.
- Claims of production readiness.
- Broad scope without maintainable fixtures.
- Large data dependency before governance is clear.
- Final-answer scoring without trace inspection.

## Local Design Implications

FinAgentBench Seed should emphasize:

- task specs,
- deterministic verifiers,
- known-bad candidate artifacts,
- source-governance manifest,
- repeated-trial metrics,
- ATIF / trajectory audit examples,
- and machine-readable reports.

## Why This Is A Multi-Track Strategy

The repo should expose several useful surfaces:

- benchmark seed for agent-eval engineers,
- RAG evaluation page for retrieval teams,
- governance page for data leads,
- synthetic fixture playbook for public-safe examples,
- annotation/preference page for data-quality teams,
- and Harbor/OpenClaw notes for trajectory-eval users.

That gives the project more routes to discovery without diluting the core thesis.
