# Financial Tool-use Evaluation Playbook

Trajectory-aware evaluation matters because a financial agent can produce a plausible final answer after using the wrong tool, ignoring a failed call, or fabricating an observation.

This playbook describes how to evaluate financial tool use without private APIs, real account data, or trading advice.

## Scope

Use this track for tasks where the process is as important as the final answer.

Good tasks check:

- Tool selection.
- Tool-call order.
- Observation linkage.
- Failed-call recovery.
- Missing evidence.
- Final-answer grounding.

## Useful Task Types

| Task type | What it tests | Required evidence | Main verifier checks |
| --- | --- | --- | --- |
| Source-routing trace | Whether the agent calls the right source tool first. | Tool calls, observations, selected source. | Required tool order, no fabricated observations. |
| Quote plus filing workflow | Whether short-horizon and filing data are separated. | Quote observation, filing observation, final evidence map. | Tool output linked to answer fields. |
| Failed-call recovery | Whether the agent retries or degrades safely. | Error observation, retry, fallback source. | Error acknowledged, no hallucinated value. |
| Repeated-trial stability | Whether the same task remains safe over attempts. | Trial-level pass/fail and failure reason. | Pass rate, missing-evidence rate, unsafe-output rate. |

## Current Repo Assets

- [Financial tool-use trace task](../examples/financial-agent-eval-seed/harbor-template/financial-tool-use-trace).
- [Harbor Finance Task Pack Blueprint](harbor-finance-task-pack-blueprint.md).
- [Harbor OpenClaw ATIF trajectory audit](../examples/harbor-openclaw-finance-trajectory-audit).
- [Harbor repeated-trial metric example](../examples/harbor-repeated-trial-metric).

## Harbor/OpenClaw Boundary

This repository is not an official Harbor adapter. The goal is to provide finance-domain task shapes and verifier ideas that can be adapted to Harbor-style or OpenClaw-style evaluation workflows.

Keep integrations upstream-friendly:

- Use small task templates.
- Keep source fixtures visible.
- Avoid framework-specific claims unless tested.
- Explain verifier assumptions.
- Prefer examples maintainers can review quickly.

## Quality Bar

Require:

- A visible trace or synthetic trace fixture.
- A mapping from observations to answer fields.
- At least one failure case involving missing, wrong, or ignored evidence.
- A final answer check and a process check.
- A safety boundary for advice and private data.

Reject:

- Final-answer-only grading for a tool-use task.
- Hidden API dependencies.
- Claims that a framework integration is official when it is not.
- Tool outputs that cannot be inspected.
- Tasks that reward fabricating unavailable data.

## Reviewer Questions

- Did the model call the right tool for the information need?
- Did it use the observation it received?
- Did it handle errors or missing data honestly?
- Can the trace be audited without a private account?
- Does repeated-trial reporting reveal instability that one run hides?

