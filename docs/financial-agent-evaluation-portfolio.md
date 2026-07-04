# Financial Agent Evaluation Portfolio

This project should not depend on one page, one benchmark idea, or one upstream framework. The stronger path is a portfolio of public-safe assets that different audiences can reuse independently.

## Portfolio Thesis

Financial-agent evaluation sits at the intersection of agent trajectories, RAG grounding, numeric verification, regulated-domain safety, benchmark packaging, and data governance. A useful public project should expose each of those surfaces clearly.

The anchor remains the runnable [Financial Agent Eval Seed](../examples/financial-agent-eval-seed/README.md), but the repo should have several entry points:

| Surface | Primary audience | What they should get in 60 seconds | Current asset |
| --- | --- | --- | --- |
| Runnable seed | agent-eval engineers | a local task runner, deterministic verifiers, known-bad reports | [Financial Agent Eval Seed](../examples/financial-agent-eval-seed/README.md) |
| Task design | benchmark builders | finance task families and failure modes | [Task Zoo](financial-agent-evaluation-task-zoo.md) |
| Evaluation governance | data leads and reviewers | source policy, synthetic-data boundaries, benchmark-card checks | [Benchmark Card](../examples/financial-agent-eval-seed/benchmark-card.yml) |
| Harbor/OpenCLAW alignment | framework maintainers | task-pack shape, manifest, repeated-trial report | [Harbor Task Pack Blueprint](harbor-finance-task-pack-blueprint.md) |
| Model/team review | applied teams | a conservative scorecard for comparing agent behavior | [Scorecard](financial-agent-evaluation-scorecard.md) |
| Public positioning | readers and future contributors | why this repo exists and where it is going | [Opportunity Map](financial-agent-evaluation-opportunity-map.md) |

## Why This Is More Attractive

People star repositories for different reasons. Some want runnable code. Some want a clear checklist. Some want an example they can adapt to their own benchmark. Some want a concise map of a fast-moving area.

This repo should satisfy all four without pretending to be a leaderboard, official Harbor adapter, investment tool, or production system.

## Current Bets

| Bet | Why it can work | What would make it stronger |
| --- | --- | --- |
| Financial search and lookup | common agent workflow, easy to verify, easy to explain | more public-source fixtures and citation edge cases |
| Financial RAG citation support | high-value failure mode for finance QA | more extraction and calculation checks |
| Forecasting cutoff checks | directly targets future-data leakage | more pastcasting examples and temporal metadata |
| Tool-use trajectories | aligns with Harbor-style rollout evidence | exportable task-pack format and repeated-trial examples |
| Preference data for finance | connects evaluation to annotation and feedback quality | more sample reviews and adjudication cases |
| Governance-first benchmark cards | credible for regulated-domain teams | CI-enforced cards for every task family |

## Public-Safe Boundaries

- No private company data.
- No real user data.
- No proprietary workflows.
- No investment advice.
- No trading signals.
- No claims of production readiness.
- No claims of official Harbor support unless upstream maintainers explicitly provide it.

## Near-Term Expansion

The next useful pages should become runnable artifacts, not static commentary:

1. Add one more task family with fixture, verifier, passing answer, and known-bad answer.
2. Add scorecard examples for two synthetic candidate agents.
3. Add a small script that produces a scorecard from task reports.
4. Keep the Harbor/OpenCLAW work framed as compatible task design, not official integration.
5. Keep repository metadata aligned with the financial-agent evaluation thesis.
