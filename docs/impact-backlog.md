# Impact Backlog

This backlog turns the project's multi-track pages into concrete artifacts. It is intentionally small, public-safe, and biased toward runnable work.

The repository has not shown strong external feedback yet. The response is not to add more generic pages. The response is to convert each promising page into a task, verifier, schema, report, or issue that other practitioners can reuse.

Machine-readable source: [`impact/impact-backlog.json`](../impact/impact-backlog.json)

Roadmap issue drafts: [`docs/roadmap-issues/README.md`](roadmap-issues/README.md)

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
| P1 | Completed | Financial agent eval | Risk calculation task | Adds deterministic finance math beyond lookup, RAG, forecasting, and backtesting. |
| P1 | Completed | Financial agent eval | Portfolio boundary refusal task | Tests a realistic regulated-domain boundary without collecting private account data. |
| P1 | Completed | Data governance | Benchmark-card validator and generated card | Makes the seed easier to inspect, cite, and adapt as a benchmark artifact. |
| P1 | Planned | Harbor/OpenCLAW | Repeated-trial reporting | Makes instability, missing evidence, and unsafe behavior visible beyond a single lucky pass. |

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

> Add repeated-trial reporting for the financial-agent eval seed

The public-source search task, finance RAG citation verifier, source-governance report, synthetic fixture validator, finance preference-review schema, public launch note, task matrix, Harbor task-pack blueprint, forecasting cutoff task, financial tool-use trace task, risk calculation task, portfolio-boundary refusal task, and benchmark-card validator are now implemented.

The next highest-leverage item is repeated-trial reporting for the runnable seed. It should make pass@k, Pass^k, missing-evidence rate, and unsafe-output rate visible without turning the repo into a model leaderboard.

Issue-write permission was not available during the latest maintenance pass, so the next issues are kept as ready-to-open drafts in [Roadmap Issue Drafts](roadmap-issues/README.md).
