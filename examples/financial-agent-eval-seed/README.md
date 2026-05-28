# Financial Agent Evaluation Seed

This is a small public-data-only benchmark seed for financial agent evaluation. It is not a finished benchmark. It is a concrete starting point for turning the [Financial Agent Evaluation Agenda](../../docs/financial-agent-evaluation-agenda.md) into reusable task specifications.

The seed focuses on five task families:

- public filing search,
- exact financial data lookup,
- filing-grounded explanation,
- toy backtesting,
- compliance-boundary refusal.

It deliberately avoids private company data, real user data, internal workflows, investment advice, trading signals, and production-readiness claims.

## Directory Layout

```text
examples/financial-agent-eval-seed/
|-- README.md
|-- dataset-card.md
|-- validate_specs.py
|-- harbor-template/
|   `-- filing-margin-explanation/
|       |-- instruction.md
|       |-- task.toml
|       |-- fixtures/
|       |-- solution/
|       `-- tests/
|-- rubrics/
|   `-- trajectory-finance-safety.toml
`-- task-specs/
    |-- compliance-refusal-guaranteed-return.json
    |-- exact-data-lookup-public-filing.json
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
```

Validate the Harbor-style example verifier against the included reference output:

```bash
python -m unittest discover -s examples/financial-agent-eval-seed/harbor-template/filing-margin-explanation/tests -p "test_*.py"
```

## How To Use This Seed

1. Review the task specs and adapt them to public data sources your team is allowed to use.
2. Start from the [Harbor-style filing task template](harbor-template/filing-margin-explanation) when converting a task into an executable task directory.
3. Add an environment, instruction, verifier, fixture policy, and artifact requirements for each task.
4. Run each task with repeated attempts.
5. Use the [Harbor repeated-trial metric example](../harbor-repeated-trial-metric) for pass@k, Pass^k, and missing-evidence reporting.
6. Add a trajectory-aware judge rubric for finance-specific process safety.

## What This Seed Is Not

- Not an investment-advice benchmark.
- Not a trading-strategy leaderboard.
- Not a private financial data release.
- Not a claim that any model or agent is production-ready.
