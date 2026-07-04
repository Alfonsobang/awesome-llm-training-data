# Harbor-style Public Source Search Template

This template evaluates whether an agent can choose the correct public-safe financial source from a controlled candidate set. It is designed to catch wrong-source and citation-theater failures before numeric extraction begins.

## What It Tests

- Selection of the official source for the requested issuer and fiscal period.
- Rejection of stale, unofficial, or weakly grounded sources.
- Citation of the selected fixture path.
- Avoidance of investment advice, trading signals, and production-readiness claims.

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
python -m unittest discover -s examples/financial-agent-eval-seed/harbor-template/public-source-search/tests -p "test_*.py"
```

## Safety Boundary

The fixture is synthetic and small enough to inspect manually. It should be replaced only with public sources that have clear usage rights.
