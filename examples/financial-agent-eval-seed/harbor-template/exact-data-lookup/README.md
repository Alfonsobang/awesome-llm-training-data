# Harbor-style Exact Financial Data Lookup Template

This template evaluates whether an agent can extract exact financial values from a controlled filing-style fixture and return auditable JSON. It is designed for public-data or synthetic-data financial agent evaluation.

## What It Tests

- Exact extraction of revenue, net income, diluted shares, currency, and fiscal year.
- Citation of the fixture section used as evidence.
- Refusal to infer unsupported values.
- Avoidance of investment advice, private-data claims, and production-readiness claims.

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
python -m unittest discover -s examples/financial-agent-eval-seed/harbor-template/exact-data-lookup/tests -p "test_*.py"
```

## Safety Boundary

The fixture is synthetic. It should be replaced only with public data that has clear usage rights.
