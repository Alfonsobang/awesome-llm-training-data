# Harbor-style Toy Backtest Template

This template evaluates whether an agent can run a tiny fixed-rule backtest while respecting a cutoff date and avoiding investment-advice framing.

The fixture is synthetic. The task is for evaluation scaffolding only, not strategy research.

## What It Tests

- Use of the provided price fixture only.
- Correct moving-average rule application.
- Clear cutoff-date discipline.
- Reporting of assumptions, limitations, and non-advice framing.

## Expected Agent Artifact

```text
/logs/artifacts/answer.json
```

For local verifier development, tests default to:

```text
solution/answer.json
```

## Local Verification

```bash
python -m unittest discover -s examples/financial-agent-eval-seed/harbor-template/toy-backtest-moving-average/tests -p "test_*.py"
```
