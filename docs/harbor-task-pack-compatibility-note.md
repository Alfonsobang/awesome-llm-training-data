# Harbor Task-pack Compatibility Note

This note explains how the Financial Agent Eval Seed currently maps to Harbor-style task packaging.

It is not an official Harbor adapter. It is a public-safe compatibility note for maintainers and practitioners who want to inspect, adapt, or discuss finance-domain agent-evaluation tasks.

## What Is Implemented Today

| Harbor-style concept | Current seed artifact |
| --- | --- |
| Task pack manifest | `examples/financial-agent-eval-seed/harbor-template/task-pack-manifest.json` |
| Task directory | `examples/financial-agent-eval-seed/harbor-template/<task-id>/` |
| Task instruction | `<task-id>/instruction.md` |
| Fixture files | `<task-id>/fixtures/` |
| Reference solution | `<task-id>/solution/answer.json` |
| Deterministic verifier | `<task-id>/tests/test_*.py` |
| Candidate artifact | `<artifact-root>/<task-id>/answer.json` |
| Local runner | `python finagent_eval.py run --artifact-root <artifact-root>` |
| Candidate scaffold | `python finagent_eval.py init-candidate tmp/my-finance-agent` |
| Scorecard | `python finagent_eval.py scorecard --report <report.json> --candidate <name> --output-prefix <prefix>` |
| Repeated-trial example | `examples/financial-agent-eval-seed/results/repeated-trial-example-report.md` |
| Benchmark metadata | `examples/financial-agent-eval-seed/benchmark-card.yml` |

## Current Task Families

The seed currently includes 10 task families:

- public-source search,
- exact financial data lookup,
- filing citation support,
- filing-grounded margin explanation,
- financial tool-use trace auditing,
- risk calculation,
- toy moving-average backtesting,
- forecasting cutoff checks,
- portfolio-boundary refusal,
- compliance-boundary refusal.

The compact machine-readable index is available at `examples/financial-agent-eval-seed/tasks.jsonl`.

## What Remains Adapter-specific

This repository does not yet provide:

- an official Harbor task-pack adapter,
- a Harbor environment image,
- a remote rollout runner,
- a standardized Harbor submission object,
- or an upstream-maintained compatibility guarantee.

Those pieces should be discussed with Harbor maintainers before this project claims compatibility beyond the current file layout and verifier workflow.

## Public-safety Boundary

The task pack does not contain private company data, real user data, proprietary workflows, investment advice, trading signals, or production-readiness evidence.

Finance-specific evaluation should preserve these boundaries even when tasks are converted into another framework.

## Suggested Upstream Question

If opening a Harbor discussion, keep the ask narrow:

> I maintain a public-safe finance-agent evaluation seed with task directories, fixtures, candidate artifacts, deterministic verifiers, a benchmark card, and a task-pack manifest. Would a Harbor-style example like this be more useful as external reference material, documentation, or a small adapter-oriented example?

Useful links for that discussion:

- [Harbor finance task-pack blueprint](harbor-finance-task-pack-blueprint.md)
- [Harbor upstream discussion brief](harbor-upstream-discussion-brief.md)
- [FinAgentBench Mini](../FINAGENTBENCH.md)
- [Task-pack manifest](../examples/financial-agent-eval-seed/harbor-template/task-pack-manifest.json)
- [Benchmark card](../examples/financial-agent-eval-seed/benchmark-card.yml)
- [Repeated-trial report](../examples/financial-agent-eval-seed/results/repeated-trial-example-report.md)
- [Source-governance report](../examples/financial-agent-eval-seed/results/source-governance-report.md)
