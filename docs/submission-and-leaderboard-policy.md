# Submission and Leaderboard Policy

This repository may add a public results table later, but it will not publish a leaderboard until the benchmark is useful enough to compare systems responsibly.

## Current Status

- Public submissions: not open.
- Public leaderboard: not active.
- Model ranking claims: not supported.
- Private data submissions: not allowed.

The current artifacts are a seed benchmark, verifier examples, and review templates.

## Why No Leaderboard Yet

Financial-agent evaluation can become misleading quickly. A leaderboard would need:

- stable task versioning,
- clear source and license policy,
- leakage checks,
- repeated-trial reporting,
- artifact retention rules,
- model and tool disclosure,
- refusal-boundary review,
- and a process for correcting verifier defects.

Until those pieces are mature, the project should prefer reproducible scorecards over rankings.

## Acceptable Submission Shape

Use [submission-template.json](../examples/financial-agent-eval-seed/submission-template.json) when sharing a candidate run.

Required evidence:

- benchmark version or commit SHA,
- candidate name,
- task-level report JSON,
- generated scorecard,
- artifact source policy,
- repeated-trial settings if used,
- known limitations,
- non-advice statement.

## Non-Acceptable Submissions

- private company data,
- real user or account data,
- proprietary workflows,
- investment advice,
- trading signals,
- unverifiable model claims,
- cherry-picked successful traces without failed attempts,
- results from modified tasks without clear disclosure.

## Future Public Table

A future table should be a conservative compatibility matrix, not a hype leaderboard:

| Candidate | Benchmark version | Tasks passed | Red flags | Repeated trials | Artifact link | Notes |
| --- | --- | ---: | ---: | --- | --- | --- |
| Reference solutions | local seed | 10 / 10 | 0 | example only | included | Sanity check, not a model result |

The table should not imply investment quality, production readiness, or general financial reasoning ability.
