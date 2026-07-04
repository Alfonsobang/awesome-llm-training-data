# Impact Backlog

This backlog turns the project's multi-track pages into concrete artifacts. It is intentionally small, public-safe, and biased toward runnable work.

The repository has not shown strong external feedback yet. The response is not to add more generic pages. The response is to convert each promising page into a task, verifier, schema, report, or issue that other practitioners can reuse.

Machine-readable source: [`impact/impact-backlog.json`](../impact/impact-backlog.json)

## Current Priorities

| Priority | Status | Track | Artifact | Why it matters |
| --- | --- | --- | --- | --- |
| P0 | Completed | Financial agent eval | Public-source search task | Search is the first tool-use failure surface in many financial agents. |
| P0 | Completed | Financial RAG eval | Citation verifier | Unsupported citations are common, concrete, and easy to evaluate. |
| P1 | Completed | Data governance | Source-governance report | Makes source policy visible to data leads and reviewers. |
| P1 | Completed | Synthetic data | Synthetic fixture validator | Keeps public examples useful without fake realism. |
| P1 | Completed | Annotation/preference | Finance preference-review rubric schema | Prevents preference data from rewarding unsupported confidence. |
| P2 | Completed | Distribution | Public launch note | Gives the project a crisp narrative for outreach. |
| P1 | Completed | Financial agent eval | Task-family matrix | Turns the big topic into multiple reusable task surfaces. |
| P1 | Completed | Harbor/OpenCLAW | Harbor-style finance task-pack blueprint | Connects the finance track to a visible agent-evaluation framework without claiming official support. |
| P1 | Completed | Financial agent eval | Forecasting / pastcasting cutoff task | Tests one of the most important finance-specific leakage risks. |
| P1 | Completed | Harbor/OpenCLAW | Financial tool-use trace task | Makes tool order, observation linkage, and missing evidence measurable. |
| P1 | Planned | Financial agent eval | Risk calculation task | Adds deterministic finance math beyond lookup, RAG, forecasting, and backtesting. |

## Why This Backlog Exists

The project should not rely on a single bet. FinAgentBench Seed is the anchor, but several adjacent assets can attract different audiences:

- agent-eval engineers,
- RAG engineers,
- data-governance leads,
- synthetic-data builders,
- annotation and preference-data teams,
- and agent-framework maintainers.

Each item in the backlog must have:

- a source page,
- a next artifact path,
- a reason it matters,
- and concrete acceptance criteria.

## Next Best Issue To Open

Next:

> Add a public-safe financial risk calculation task

The public-source search task, finance RAG citation verifier, source-governance report, synthetic fixture validator, finance preference-review schema, public launch note, task matrix, Harbor task-pack blueprint, forecasting cutoff task, and financial tool-use trace task are now implemented. The next highest-leverage item is a risk calculation task that adds deterministic drawdown or volatility checks without turning the project into a trading leaderboard.
