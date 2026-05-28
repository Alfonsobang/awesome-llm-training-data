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
├── README.md
├── dataset-card.md
├── validate_specs.py
├── rubrics/
│   └── trajectory-finance-safety.toml
└── task-specs/
    ├── compliance-refusal-guaranteed-return.json
    ├── exact-data-lookup-public-filing.json
    ├── filing-grounded-margin-explanation.json
    ├── public-filing-search.json
    └── toy-backtest-moving-average.json
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

## How To Use This Seed

1. Review the task specs and adapt them to public data sources your team is allowed to use.
2. Convert each task into a Harbor task directory with an environment, instruction, verifier, and artifact requirements.
3. Run each task with repeated attempts.
4. Use the [Harbor repeated-trial metric example](../harbor-repeated-trial-metric) for pass@k, Pass^k, and missing-evidence reporting.
5. Add a trajectory-aware judge rubric for finance-specific process safety.

## What This Seed Is Not

- Not an investment-advice benchmark.
- Not a trading-strategy leaderboard.
- Not a private financial data release.
- Not a claim that any model or agent is production-ready.
