# 60-Second Quickstart

This repo is most useful as a small financial agent evaluation starter kit. It gives you runnable tasks, synthetic fixtures, deterministic verifier tests, source-governance metadata, and example reports.

## Run The Passing Reference Suite

```bash
python examples/financial-agent-eval-seed/run_finance_eval.py
```

Expected result:

```text
Pass rate: 4/4 (1.0)
```

The command writes:

- `examples/financial-agent-eval-seed/results/latest-report.json`
- `examples/financial-agent-eval-seed/results/latest-report.md`

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
- Exact financial data lookup with units, citations, and numeric types.
- Filing-grounded margin explanation with calculation evidence.
- Toy backtesting with cutoff discipline and non-advice framing.
- Source governance for public references, synthetic fixtures, citation fields, and redistribution boundaries.

## What To Customize First

1. Add one new task under `examples/financial-agent-eval-seed/task-specs/`.
2. Add a matching Harbor-style template under `examples/financial-agent-eval-seed/harbor-template/`.
3. Write deterministic tests against the expected `answer.json`.
4. Register allowed public sources in `examples/financial-agent-eval-seed/data-sources/source-manifest.json`.
5. Run `python examples/financial-agent-eval-seed/run_finance_eval.py`.

Safety boundary: the included examples use synthetic fixtures and public-source patterns. They do not contain private company data, real user data, investment advice, trading signals, or proprietary workflows.
