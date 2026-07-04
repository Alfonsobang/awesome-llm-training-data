# 60-Second Quickstart

This repo is most useful as a small financial agent evaluation starter kit. It gives you runnable tasks, synthetic fixtures, deterministic verifier tests, source-governance metadata, and example reports.

The current direction is documented in:

- `docs/README.md`
- `docs/financial-agent-eval-positioning.md`
- `docs/finagentbench-seed-spec.md`

## Run The Passing Reference Suite

```bash
python examples/financial-agent-eval-seed/run_finance_eval.py
python examples/financial-agent-eval-seed/aggregate_trial_reports.py
python tools/validate_financial_benchmark_card.py
```

Expected result:

```text
Pass rate: 10/10 (1.0)
Repeated-trial report: 10 tasks, 20 task trials
Validated financial benchmark card with 10 task specs.
```

The command writes:

- `examples/financial-agent-eval-seed/results/latest-report.json`
- `examples/financial-agent-eval-seed/results/latest-report.md`
- `examples/financial-agent-eval-seed/results/repeated-trial-example-report.json`
- `examples/financial-agent-eval-seed/results/repeated-trial-example-report.md`

## Run A Known-Bad Candidate

This shows what the verifier catches when an agent output is unsafe, weakly grounded, or numerically wrong.

```bash
python examples/financial-agent-eval-seed/run_finance_eval.py --artifact-root examples/financial-agent-eval-seed/candidate-artifacts/bad-finance-agent
```

Expected result: the command exits non-zero and reports failed tasks.

See the stable bad-candidate report:

- `examples/financial-agent-eval-seed/results/bad-finance-agent-report.md`

## What The Seed Currently Checks

- Compliance refusal for guaranteed-return, personalized-advice, and private-data requests.
- Public-source search with official-source selection and weak-source rejection.
- Exact financial data lookup with units, citations, and numeric types.
- Finance RAG citation checks that fail unsupported citations.
- Filing-grounded margin explanation with calculation evidence.
- Toy backtesting with cutoff discipline and non-advice framing.
- Forecasting cutoff checks for future-data leakage.
- Risk calculation for drawdown, volatility, units, and data windows.
- Financial tool-use trace checks for tool order and observation linkage.
- Portfolio-boundary refusal for personalized rebalancing and private-data minimization.
- Source governance for public references, synthetic fixtures, citation fields, and redistribution boundaries.

## What To Customize First

1. Add one new task under `examples/financial-agent-eval-seed/task-specs/`.
2. Add a matching Harbor-style template under `examples/financial-agent-eval-seed/harbor-template/`.
3. Write deterministic tests against the expected `answer.json`.
4. Register allowed public sources in `examples/financial-agent-eval-seed/data-sources/source-manifest.json`.
5. Run `python examples/financial-agent-eval-seed/run_finance_eval.py`.

Safety boundary: the included examples use synthetic fixtures and public-source patterns. They do not contain private company data, real user data, investment advice, trading signals, or proprietary workflows.
