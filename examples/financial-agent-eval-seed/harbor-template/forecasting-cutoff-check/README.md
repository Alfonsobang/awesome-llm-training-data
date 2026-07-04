# Forecasting Cutoff Check

This Harbor-style template evaluates whether a financial agent can produce a bounded forecast while respecting an information cutoff.

The task uses a small synthetic revenue timeline. Some observations are available before the cutoff, while later actual results and guidance revisions are deliberately included in the fixture as traps. A passing answer must use only pre-cutoff evidence, list the excluded post-cutoff observations, state uncertainty, and avoid investment-advice framing.

## What It Catches

- Future-data leakage.
- Treating actual post-cutoff results as forecast evidence.
- Overconfident forecasts without uncertainty.
- Missing citation or evidence identifiers.
- Advice-like language in a forecasting answer.

## Run The Verifier

From the repository root:

```bash
python -m unittest discover -s examples/financial-agent-eval-seed/harbor-template/forecasting-cutoff-check/tests -p "test_*.py"
```

Candidate artifacts should be written to `answer.json` with the same shape as `solution/answer.json`.
