# Harbor Finance Task Pack Blueprint

Harbor is a fast-moving framework for evaluating and optimizing agents. Its public README describes support for evaluating arbitrary agents, building and sharing benchmarks and environments, running experiments in many environments, and generating rollouts for RL optimization.

This page defines the finance-specific layer this repository can contribute: public-safe task packs that make financial-agent failures inspectable through sources, tool traces, verifier outputs, and governance metadata.

Checked against the public [harbor-framework/harbor](https://github.com/harbor-framework/harbor) repository page on 2026-07-04. The page showed Harbor as a framework for evaluating and improving agents, with a latest release listed as `v0.17.1` on 2026-07-03. Harbor moves quickly, so implementation details should be confirmed before upstream work.

## Positioning

This is not an official Harbor adapter. It is a public-safe blueprint for shaping financial-agent evaluation tasks so they can be adapted to Harbor-style benchmark packaging.

The useful contribution is domain structure:

- task families that reflect real financial-agent failure modes,
- source manifests and redistribution boundaries,
- deterministic verifiers where possible,
- trajectory-aware checks for tool use and process safety,
- repeated-trial metrics for stability,
- and non-advice language boundaries.

## Proposed Task-Pack Shape

```text
finance-agent-eval/
  dataset.yaml
  README.md
  source-manifest.json
  tasks/
    public-source-search/
      task.yaml
      fixture.json
      reference-answer.json
      verifier.py
    exact-data-lookup/
      task.yaml
      fixture.json
      reference-answer.json
      verifier.py
    filing-citation-check/
      task.yaml
      fixture.json
      reference-answer.json
      verifier.py
    toy-backtest-moving-average/
      task.yaml
      fixture.json
      reference-answer.json
      verifier.py
  reports/
    example-report.md
    source-governance-report.md
```

## Required Metadata

| Field | Purpose |
| --- | --- |
| `task_id` | Stable task identity for reports and repeated trials. |
| `task_family` | Search, lookup, filing QA, backtesting, forecasting, tool use, refusal, or governance. |
| `allowed_sources` | Source IDs from the source manifest. |
| `prohibited_sources` | Private, paywalled, unsupported, or post-cutoff sources that must not be used. |
| `information_cutoff` | Time boundary for forecasting, backtesting, or retrieval tasks. |
| `required_artifacts` | Expected answer JSON, citation map, calculation table, code output, or trace file. |
| `verifier` | Deterministic script or scoped judge rule used to evaluate the task. |
| `safety_boundary` | Non-advice, private-data, and prohibited-action rules. |

## Finance-Specific Verifier Checks

| Check | Example |
| --- | --- |
| Source identity | The selected document must match an allowed source ID. |
| Period integrity | Fiscal year, quarter, and statement period must match the task. |
| Unit integrity | Currency, scale, percentage points, and split-adjusted fields must be explicit. |
| Citation support | Each material claim must map to a cited section or field path. |
| Cutoff integrity | No post-cutoff observations may affect the answer. |
| Tool boundary | No private-data, trading-execution, or account-level tool may appear in the trace. |
| Non-advice language | Backtesting and forecasting tasks must not become recommendations. |
| Missing evidence | Failed or missing traces should be counted, not silently dropped. |

## Repeated-Trial Metrics

Finance-agent evaluation should report more than a single pass rate:

- `pass_rate`: share of attempts that pass all required checks.
- `pass_at_k`: whether at least one attempt passes within `k` tries.
- `pass_power_k`: whether all `k` attempts pass.
- `missing_evidence_rate`: share of attempts without usable artifacts or trace evidence.
- `cutoff_violation_rate`: share of attempts using post-cutoff evidence.
- `prohibited_tool_call_rate`: share of attempts that call disallowed tools.

The repo already includes a small [Harbor repeated-trial metric example](../examples/harbor-repeated-trial-metric).

## Upstream-Friendly Contribution Path

1. Keep the local examples runnable and small.
2. Add a clean task-pack README that explains the public-data boundary.
3. Open a focused Harbor discussion or PR only after the task format is stable.
4. Ask maintainers whether a finance-domain example belongs as docs, an example task pack, or an external benchmark reference.
5. Avoid claiming official support until maintainers explicitly accept it.

## Related Assets

- [Financial Agent Evaluation Task Matrix](financial-agent-evaluation-task-matrix.md)
- [Harbor, OpenClaw, and ATIF for Financial Agent Evaluation](harbor-openclaw-atif-financial-evaluation.md)
- [Financial Agent Eval Seed](../examples/financial-agent-eval-seed)
- [Harbor-style Financial Task Templates](../examples/financial-agent-eval-seed/harbor-template)
- [Harbor OpenClaw Financial Trajectory Audit](../examples/harbor-openclaw-finance-trajectory-audit)
