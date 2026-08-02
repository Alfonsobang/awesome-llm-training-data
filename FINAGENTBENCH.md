# FinAgentBench Mini

FinAgentBench Mini is the runnable part of this repository: a public-safe starter benchmark for financial-agent evaluation.

It is designed for teams that need to test whether an agent can use public financial evidence, preserve units and periods, avoid future-data leakage, handle tool trajectories, and respect regulated-domain advice boundaries.

It is not a trading benchmark, a model ranking, or a production-readiness claim.

## Run In One Minute

```bash
python finagent_eval.py demo
```

The command runs 10 deterministic verifier tasks and writes:

- `examples/financial-agent-eval-seed/results/latest-report.json`
- `examples/financial-agent-eval-seed/results/latest-report.md`
- `examples/financial-agent-eval-seed/results/latest-scorecard.json`
- `examples/financial-agent-eval-seed/results/latest-scorecard.md`

To create a candidate artifact layout for your own agent:

```bash
python finagent_eval.py init-candidate tmp/my-finance-agent
python finagent_eval.py run --artifact-root tmp/my-finance-agent
```

## What It Tests

| Track | Example task | Primary failure mode |
| --- | --- | --- |
| Financial search | `public-source-search` | Selecting weak or mismatched sources |
| Exact lookup | `exact-data-lookup` | Wrong unit, period, or field |
| Filing QA | `filing-citation-check` | Unsupported citation or invented evidence |
| Filing reasoning | `filing-margin-explanation` | Ungrounded calculation or missing limitation |
| Tool trajectory | `financial-tool-use-trace` | Broken call order, missing observation, unrecovered failure |
| Risk calculation | `risk-calculation-drawdown` | Incorrect deterministic finance math |
| Backtesting | `toy-backtest-moving-average` | Lookahead bias or undisclosed assumptions |
| Forecasting | `forecasting-cutoff-check` | Future-data leakage or overconfident framing |
| Portfolio boundary | `portfolio-boundary-refusal` | Personalized advice without user/account safeguards |
| Compliance boundary | `compliance-refusal` | Guaranteed-return or private-data unsafe response |

## Useful Files

- [Evaluate Your Own Finance Agent](docs/evaluate-your-finance-agent.md)
- [Submission and Leaderboard Policy](docs/submission-and-leaderboard-policy.md)
- [Harbor Task-pack Compatibility Note](docs/harbor-task-pack-compatibility-note.md)
- [Machine-readable task index](examples/financial-agent-eval-seed/tasks.jsonl)
- [Submission template](examples/financial-agent-eval-seed/submission-template.json)
- [Benchmark card](examples/financial-agent-eval-seed/benchmark-card.yml)
- [Harbor-style task-pack manifest](examples/financial-agent-eval-seed/harbor-template/task-pack-manifest.json)

## Design Boundary

The benchmark seed uses public-safe examples and synthetic fixtures. It does not contain private company data, real user data, proprietary workflows, investment advice, trading signals, or evidence that any agent is production-ready.
