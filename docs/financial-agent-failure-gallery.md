# Financial Agent Failure Gallery

Financial agents often look correct in a final answer while failing in the process. This gallery collects failure modes that are useful for designing public-safe evaluation tasks.

The goal is not to publish private examples. The goal is to turn common failure patterns into synthetic fixtures, deterministic verifiers, and known-bad candidate artifacts.

## Failure Modes

| Failure | What it looks like | What to test |
| --- | --- | --- |
| Wrong source | Uses a blog, stale snapshot, or hallucinated filing instead of an official disclosure. | Require source URL, source type, date, and citation field. |
| Wrong unit scale | Reports millions as raw units or mixes USD thousands and USD millions. | Require numeric value, unit, scale, and extraction note. |
| Wrong fiscal period | Mixes fiscal year, quarter, trailing twelve months, or calendar year. | Require fiscal period and statement context. |
| Future-data leakage | Uses data after the cutoff in a backtest or forecast task. | Require cutoff date, rows used, and no-future-data evidence. |
| Citation theater | Provides citations that do not support the answer. | Check source, section, quote/field path, and support claim. |
| Unsafe advice | Gives guaranteed-return, personalized trading, or insider-information guidance. | Require refusal and safe alternative. |
| Missing limitation | Presents a synthetic or tiny fixture as production-ready. | Require limitations and non-advice boundary. |
| Tool-trace gap | Final answer has no linked observation or tool-call evidence. | Require trace linkage between tool call, observation, and answer field. |
| Repeated-attempt instability | Passes once but fails frequently across retries. | Track pass@k and all-attempts-pass rates. |

## Turning Failures Into Tasks

Each failure should become a small benchmark unit:

- a task spec,
- a synthetic or public-safe fixture,
- a reference `answer.json`,
- a known-bad `answer.json`,
- deterministic verifier tests,
- and a report entry that explains the failure.

## Current Examples

The existing [bad finance agent report](../examples/financial-agent-eval-seed/results/bad-finance-agent-report.md) demonstrates:

- unsafe guaranteed-return language,
- weak citation,
- wrong numeric value,
- wrong margin calculation,
- future-row leakage,
- and production-readiness overclaiming.

## Safety Boundary

Use synthetic examples or public-source references. Do not include private company data, customer examples, internal workflows, investment advice, or trading signals.
