# Harbor-style Filing Citation Check Template

This template evaluates whether an agent can answer a finance RAG-style question with citations that actually support the answer. It is designed to catch citation theater: plausible citations that do not support the claim.

## What It Tests

- Structured answer with explicit citation objects.
- Citation source, section, and support note.
- Use of supported evidence in the final answer.
- Rejection of unsupported investment claims.
- Visible synthetic-data and non-advice boundaries.

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
python -m unittest discover -s examples/financial-agent-eval-seed/harbor-template/filing-citation-check/tests -p "test_*.py"
```

## Safety Boundary

The fixture is synthetic and only intended to test citation-support behavior. It should not be used as financial evidence or investment guidance.
