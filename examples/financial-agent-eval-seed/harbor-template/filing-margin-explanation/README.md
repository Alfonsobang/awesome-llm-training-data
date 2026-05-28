# Harbor-style Financial Filing Task Template

This is a minimal Harbor-style task template for financial agent evaluation. It uses a synthetic public-filing-style fixture, a fixed instruction, and deterministic verifier tests. The goal is to show how financial agent tasks can require evidence, calculations, and compliance-safe wording without using private data or investment advice.

This template is intentionally small. Treat it as a starting point for converting the broader task specs in `../../task-specs` into executable agent-evaluation tasks.

## What It Tests

- Whether the agent reads the provided filing-style fixture instead of inventing numbers.
- Whether the agent calculates operating margin correctly.
- Whether the agent explains the year-over-year change with source-grounded evidence.
- Whether the agent avoids investment advice, return guarantees, private data claims, and production-readiness claims.
- Whether the output is auditable JSON rather than free-form prose only.

## Expected Agent Artifact

The agent should write:

```text
/logs/artifacts/answer.json
```

For local verifier development, the tests default to the included reference output:

```text
solution/answer.json
```

## Local Verification

```bash
python -m unittest discover -s examples/financial-agent-eval-seed/harbor-template/filing-margin-explanation/tests -p "test_*.py"
```

## Safety Boundary

This template uses synthetic fixture data. It is not a trading benchmark, investment-advice benchmark, or claim that an agent is ready for regulated production use.
