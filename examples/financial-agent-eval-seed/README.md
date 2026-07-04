# Financial Agent Evaluation Seed

This is a small public-data-only benchmark seed for financial agent evaluation. It is a runnable starter kit: task specs, synthetic fixtures, Harbor-style task templates, deterministic verifiers, source-governance metadata, and a local report runner.

Run the starter suite from the repository root:

```bash
python examples/financial-agent-eval-seed/run_finance_eval.py
```

The command writes:

- `examples/financial-agent-eval-seed/results/latest-report.json`
- `examples/financial-agent-eval-seed/results/latest-report.md`

The repository also includes a stable [example report](results/example-report.md) generated from the reference solutions.

It also includes a known-bad candidate so you can inspect what the verifier catches:

```bash
python examples/financial-agent-eval-seed/run_finance_eval.py --artifact-root examples/financial-agent-eval-seed/candidate-artifacts/bad-finance-agent
```

The stable failure summary is available at [bad-finance-agent-report.md](results/bad-finance-agent-report.md).

To score your own candidate artifacts, write one `answer.json` per task under `<artifact-root>/<task-id>/answer.json`, then run:

```bash
python examples/financial-agent-eval-seed/run_finance_eval.py --artifact-root path/to/artifacts
```

The seed focuses on eight task families:

- public filing search,
- exact financial data lookup,
- filing citation support,
- filing-grounded explanation,
- financial tool-use trace auditing,
- toy backtesting,
- forecasting cutoff discipline,
- compliance-boundary refusal.

It deliberately avoids private company data, real user data, internal workflows, investment advice, trading signals, and production-readiness claims.

## Directory Layout

```text
examples/financial-agent-eval-seed/
|-- README.md
|-- dataset-card.md
|-- generate_source_governance_report.py
|-- run_finance_eval.py
|-- validate_specs.py
|-- validate_harbor_templates.py
|-- validate_sources.py
|-- data-sources/
|   `-- source-manifest.json
|-- candidate-artifacts/
|   `-- bad-finance-agent/
|-- harbor-template/
|   |-- README.md
|   |-- compliance-refusal/
|   |-- exact-data-lookup/
|   |-- filing-citation-check/
|   |-- filing-margin-explanation/
|   |-- financial-tool-use-trace/
|   |-- forecasting-cutoff-check/
|   |-- public-source-search/
|   `-- toy-backtest-moving-average/
|-- rubrics/
|   `-- trajectory-finance-safety.toml
|-- results/
|   |-- bad-finance-agent-report.json
|   |-- bad-finance-agent-report.md
|   |-- example-report.json
|   |-- example-report.md
|   |-- source-governance-report.json
|   `-- source-governance-report.md
`-- task-specs/
    |-- compliance-refusal-guaranteed-return.json
    |-- exact-data-lookup-public-filing.json
    |-- financial-tool-use-trace.json
    |-- forecasting-cutoff-check.json
    |-- filing-grounded-margin-explanation.json
    |-- public-filing-search.json
    `-- toy-backtest-moving-average.json
```

## Task Spec Shape

Each task spec is a JSON object with:

- `task_id`
- `family`
- `risk_level`
- `instruction`
- `allowed_sources`
- `allowed_tools`
- `prohibited_actions`
- `required_evidence`
- `metrics`
- `known_failure_modes`

Run the local validator:

```bash
python examples/financial-agent-eval-seed/validate_specs.py
python examples/financial-agent-eval-seed/validate_sources.py
```

Validate all Harbor-style example verifiers against the included reference outputs:

```bash
python examples/financial-agent-eval-seed/validate_harbor_templates.py
```

Current Harbor-style templates:

- [Compliance refusal](harbor-template/compliance-refusal)
- [Exact data lookup](harbor-template/exact-data-lookup)
- [Filing citation check](harbor-template/filing-citation-check)
- [Filing margin explanation](harbor-template/filing-margin-explanation)
- [Financial tool-use trace](harbor-template/financial-tool-use-trace)
- [Forecasting cutoff check](harbor-template/forecasting-cutoff-check)
- [Public source search](harbor-template/public-source-search)
- [Toy moving-average backtest](harbor-template/toy-backtest-moving-average)

Review the governed [financial data-source manifest](data-sources/source-manifest.json) before adding or adapting tasks.

Generate the stable source-governance report:

```bash
python examples/financial-agent-eval-seed/generate_source_governance_report.py
```

See [source-governance-report.md](results/source-governance-report.md).

## What It Measures

The current seed is intentionally narrow, but each task checks a real failure mode in financial agents:

- source-grounded public filing search,
- exact numeric lookup with units and citations,
- citation support checks for finance RAG answers,
- filing-grounded explanation with calculation evidence,
- tool-use trace auditing with failed-call recovery and observation linkage,
- cutoff-safe toy backtesting,
- forecasting cutoff integrity and uncertainty framing,
- refusal of guaranteed-return, personalized-advice, and private-data requests.

## How To Use This Seed

1. Review the task specs and adapt them to public data sources your team is allowed to use.
2. Start from the [Harbor-style task templates](harbor-template) when converting a task into an executable task directory.
3. Write candidate outputs as structured `answer.json` artifacts.
4. Run `run_finance_eval.py --artifact-root path/to/artifacts`.
5. Use the generated JSON and Markdown reports as CI artifacts or review attachments.
6. Run each task with repeated attempts and combine the outputs with the [Harbor repeated-trial metric example](../harbor-repeated-trial-metric).
7. Add a trajectory-aware judge rubric for finance-specific process safety.

## What This Seed Is Not

- Not an investment-advice benchmark.
- Not a trading-strategy leaderboard.
- Not a private financial data release.
- Not a claim that any model or agent is production-ready.
