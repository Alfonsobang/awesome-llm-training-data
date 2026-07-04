# Harbor Upstream Discussion Brief

This is a maintainer-facing brief for a possible discussion with the Harbor project. It is not an official Harbor adapter, and it should not be presented as accepted upstream work.

## Short Version

I am building a small public-safe financial-agent evaluation seed with Harbor-style task templates. The goal is to make finance-specific agent failures inspectable through task specs, synthetic fixtures, deterministic verifiers, source-governance metadata, benchmark-card fields, repeated-trial reports, and a task-pack manifest.

The question for Harbor maintainers:

> Would a small public-safe finance task-pack example be useful as external reference material, documentation, or an example contribution? If yes, what format would be easiest to review?

## Why This Might Fit Harbor

Financial agents fail in ways that final-answer-only grading can miss:

- wrong public source,
- wrong unit or fiscal period,
- unsupported filing citation,
- future-data leakage,
- toy backtest look-ahead bias,
- unsafe personalized advice,
- private-data collection,
- fabricated or ignored tool observations,
- unstable behavior across repeated attempts.

Harbor-style evaluation is a good place to explore these failures because the useful evidence is not only the final answer. It also includes fixtures, verifier output, tool traces, repeated attempts, and task metadata.

## Current Public-safe Assets

All assets are in this repository and use synthetic fixtures or public-source references. They do not contain private company data, real user data, proprietary workflows, investment advice, or trading signals.

- Financial Agent Eval Seed: [`../examples/financial-agent-eval-seed`](../examples/financial-agent-eval-seed)
- Harbor-style task templates: [`../examples/financial-agent-eval-seed/harbor-template`](../examples/financial-agent-eval-seed/harbor-template)
- Task-pack manifest: [`../examples/financial-agent-eval-seed/harbor-template/task-pack-manifest.json`](../examples/financial-agent-eval-seed/harbor-template/task-pack-manifest.json)
- Benchmark card: [`../examples/financial-agent-eval-seed/benchmark-card.yml`](../examples/financial-agent-eval-seed/benchmark-card.yml)
- Passing report: [`../examples/financial-agent-eval-seed/results/example-report.md`](../examples/financial-agent-eval-seed/results/example-report.md)
- Known-bad report: [`../examples/financial-agent-eval-seed/results/bad-finance-agent-report.md`](../examples/financial-agent-eval-seed/results/bad-finance-agent-report.md)
- Repeated-trial report: [`../examples/financial-agent-eval-seed/results/repeated-trial-example-report.md`](../examples/financial-agent-eval-seed/results/repeated-trial-example-report.md)
- Source-governance report: [`../examples/financial-agent-eval-seed/results/source-governance-report.md`](../examples/financial-agent-eval-seed/results/source-governance-report.md)

## Current Task Coverage

The seed currently has 10 runnable task templates:

| Task | Failure surface |
| --- | --- |
| `public-source-search` | Official-source selection, weak-source rejection, citation path. |
| `exact-data-lookup` | Exact value, unit, period, citation, numeric type. |
| `filing-citation-check` | Supported filing citation and no citation theater. |
| `filing-margin-explanation` | Filing-grounded explanation with calculation evidence. |
| `forecasting-cutoff-check` | Future-data leakage and uncertainty framing. |
| `risk-calculation-drawdown` | Drawdown, volatility, data window, formula convention. |
| `toy-backtest-moving-average` | Look-ahead bias, fixed rule, non-advice framing. |
| `financial-tool-use-trace` | Tool order, observation linkage, failed-call recovery. |
| `portfolio-boundary-refusal` | Personalized portfolio advice and private-data boundary. |
| `compliance-refusal` | Guaranteed-return, private-data, and unsafe-advice refusal. |

## Local Verification Commands

From the repository root:

```bash
python examples/financial-agent-eval-seed/run_finance_eval.py
python examples/financial-agent-eval-seed/aggregate_trial_reports.py
python examples/financial-agent-eval-seed/validate_task_pack_manifest.py
python tools/validate_financial_benchmark_card.py
python examples/financial-agent-eval-seed/validate_harbor_templates.py
```

Expected high-level signals:

- Reference suite: `10/10`
- Known-bad suite: `0/10`
- Repeated-trial report: `pass@2 = 1.0`, `Pass^2 = 0.0` for the checked-in reference-plus-known-bad demonstration
- Task-pack manifest: 10 tasks
- Benchmark card: 10 task specs

## What I Would Ask Maintainers

I would not ask maintainers to accept a large benchmark immediately. A smaller and easier question is:

> Is there a preferred Harbor-compatible shape for external task-pack examples that include task metadata, fixtures, verifiers, source-governance notes, and repeated-trial metrics?

Possible paths:

- Keep this as an external reference and ask for format feedback only.
- Contribute a short documentation note about finance-domain evaluation task design.
- Contribute a minimal example task pack if maintainers want domain examples.
- Keep the integration outside Harbor and align naming/metadata with maintainer guidance.

## What This Is Not

- Not an official Harbor adapter.
- Not a claim that Harbor endorses this task pack.
- Not a finance benchmark leaderboard.
- Not investment advice.
- Not a trading strategy benchmark.
- Not a private data release.
- Not a claim of production readiness.

## Suggested Discussion Text

```markdown
Hi Harbor maintainers,

I am working on a small public-safe financial-agent evaluation seed and would appreciate guidance on the best shape for external task-pack examples.

The current seed has 10 Harbor-style task templates covering source search, exact lookup, filing citations, cutoff discipline, risk calculation, toy backtesting, tool-use traces, and financial safety/refusal boundaries. It includes synthetic fixtures, deterministic verifiers, a task-pack manifest, a benchmark card, source-governance metadata, passing/known-bad reports, and a repeated-trial report.

This is not an official Harbor adapter and I am not asking for endorsement. My question is narrower: if a finance-domain task-pack example like this is useful to Harbor users, would maintainers prefer it as external reference material, documentation, or a minimal example task pack? Are there specific metadata fields or task-pack conventions I should align with before considering any PR?

Relevant assets:

- Task-pack manifest: `examples/financial-agent-eval-seed/harbor-template/task-pack-manifest.json`
- Benchmark card: `examples/financial-agent-eval-seed/benchmark-card.yml`
- Repeated-trial report: `examples/financial-agent-eval-seed/results/repeated-trial-example-report.md`
- Local verifier: `python examples/financial-agent-eval-seed/run_finance_eval.py`

The examples are synthetic/public-safe and do not contain private company data, real user data, proprietary workflows, investment advice, or trading signals.
```

## Preconditions Before Opening The Discussion

- Confirm the latest Harbor task-pack or dataset conventions from current upstream docs.
- Keep the ask small: format feedback first, not acceptance.
- Link to stable files on the repository default branch.
- Do not claim official Harbor/OpenClaw support.
- Be ready to close the loop by updating the manifest or docs based on maintainer feedback.
