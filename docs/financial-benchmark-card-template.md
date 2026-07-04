# Financial Benchmark Card Template

Use this template when adding a new financial-agent evaluation task, task pack, dataset slice, or report.

The goal is to make each benchmark artifact understandable before someone reads the code.

## Benchmark Card

```yaml
name:
version:
owner:
status: draft | active | deprecated
last_reviewed:

purpose:
  summary:
  intended_users:
  out_of_scope:

task_scope:
  task_families:
  required_capabilities:
  prohibited_behaviors:
  safety_boundary:

data:
  source_type: public_source | synthetic_fixture | mixed
  source_manifest_refs:
  redistribution_policy:
  private_data_used: false
  real_user_data_used: false
  proprietary_workflow_used: false

temporal_controls:
  cutoff_date:
  evidence_window:
  known_leakage_risks:
  revision_policy:

evaluation:
  answer_schema:
  verifier:
  metrics:
  tolerance_policy:
  known_failure_modes:

reports:
  passing_report:
  known_bad_report:
  source_governance_report:

limitations:
  benchmark_limits:
  domain_limits:
  non_advice_statement:
```

## Required Narrative

Each benchmark card should answer these questions in plain English:

- What failure does this task catch?
- What evidence is visible to reviewers?
- What private or proprietary data is explicitly excluded?
- What does the verifier check?
- What does the verifier not prove?
- How can a contributor add a new case safely?

## Minimum Quality Bar

Do not publish a financial benchmark artifact unless it has:

- A task spec or schema.
- A visible fixture or public-source reference.
- A passing reference answer.
- A known-bad answer or negative example.
- A deterministic verifier, schema validator, or documented manual review rubric.
- A limitation statement.
- A non-advice statement.

## Current Examples

- [Financial Agent Eval Seed dataset card](../examples/financial-agent-eval-seed/dataset-card.md).
- [Financial Agent Eval Seed benchmark card](../examples/financial-agent-eval-seed/benchmark-card.yml).
- [Financial Agent Eval Seed reports](../examples/financial-agent-eval-seed/results/example-report.md).
- [Financial Agent Eval Seed repeated-trial report](../examples/financial-agent-eval-seed/results/repeated-trial-example-report.md).
- [Source governance report](../examples/financial-agent-eval-seed/results/source-governance-report.md).
- [Finance preference-review schema](../schemas/finance-preference-review.schema.json).
