# Financial Forecasting Evaluation Playbook

Forecasting is a high-interest financial-agent task, but public evaluation becomes credible only when temporal integrity is explicit.

This playbook treats forecasting and pastcasting as cutoff-bound evidence tasks instead of trading competitions.

## Scope

Use this track for tasks where the agent must reason from information available before a declared cutoff date.

Good tasks check:

- Allowed evidence before the cutoff.
- Excluded future evidence after the cutoff.
- Feature provenance.
- Uncertainty language.
- Non-advice framing.

## Useful Task Types

| Task type | What it tests | Required evidence | Main verifier checks |
| --- | --- | --- | --- |
| Cutoff-bound forecast | Whether the model respects time boundaries. | Cutoff date, allowed facts, excluded facts, forecast interval. | No post-cutoff evidence, uncertainty present, no advice. |
| Pastcast reconstruction | Whether the model can reconstruct a historical forecast fairly. | Information set as of the historical date. | Evidence timestamps, no leakage, limitation statement. |
| Feature audit | Whether features are available at decision time. | Feature list, source date, release lag. | Feature timestamp and allowed-source checks. |
| Forecast explanation | Whether reasoning is grounded and calibrated. | Driver list, uncertainty, cited evidence. | No unsupported certainty, no future facts, no target leakage. |

## Current Repo Assets

- [Forecasting cutoff task](../examples/financial-agent-eval-seed/harbor-template/forecasting-cutoff-check).
- [Financial Agent Evaluation Task Matrix](financial-agent-evaluation-task-matrix.md).
- [Financial Agent Failure Gallery](financial-agent-failure-gallery.md).

## Quality Bar

Forecasting tasks should teach leakage discipline.

Require:

- A declared cutoff date.
- Timestamped evidence.
- A visible rule for excluding future facts.
- Uncertainty or bounded language.
- A known-bad answer that uses post-cutoff evidence.

Reject:

- Open-ended market predictions.
- Prompts asking for current trading recommendations.
- Retrospective explanations that pretend future facts were knowable.
- Accuracy claims without a documented evaluation window.

## Common Failure Modes

- Using future earnings, later filings, revised macro data, or later price movement.
- Producing a single confident point forecast without uncertainty.
- Reporting post-event facts as if they were pre-event signals.
- Hiding source dates in vague citations.
- Presenting a forecast as actionable financial advice.

## Reviewer Questions

- Could the answer have been written on the cutoff date?
- Are all features timestamped or otherwise justified as available?
- Does the verifier fail a future-leakage answer?
- Does the task separate evaluation from investment recommendation?
- Are limitations visible to someone reading only the report?

