# Discussion Seed: What Should Agent Evaluation Measure In 2026?

This is a draft discussion starter for GitHub Discussions, LinkedIn, X, or technical communities focused on agent evaluation.

## Short Version

I think agent evaluation in 2026 should move from "final answer looks correct" to "the whole run is trustworthy."

For tool-using agents, I would like to see evaluation reports include:

- completion evidence,
- trajectory evidence,
- process-safety evidence,
- repeated-attempt robustness,
- verifier and artifact evidence,
- missing-evidence rate.

The question I am trying to answer: what is the minimal evidence package that makes an agent benchmark result trustworthy?

## Discussion Questions

1. Should `Pass^k` / all-attempts-pass be reported next to `Pass@k` for agent benchmarks?
2. What process-safety violations should be standardized first?
3. Should trajectory-aware judge rubrics be benchmark-specific, or should there be a common template?
4. How should benchmark authors report missing trajectories, missing rewards, malformed artifacts, and verifier errors?
5. For financial or regulated-domain agents, what should be mandatory evidence before a result is considered publishable?

## My Current Position

I would start with a small, reproducible evidence package:

- task fixture,
- environment definition,
- deterministic verifier where possible,
- `agent/trajectory.json`,
- collected artifacts,
- repeated-trial metric,
- safety rubric,
- clear dataset card.

I wrote a small public sketch here:

- Radar: https://github.com/Alfonsobang/awesome-llm-training-data/blob/main/docs/2026-agent-evaluation-radar.md
- Harbor metric example: https://github.com/Alfonsobang/awesome-llm-training-data/tree/main/examples/harbor-repeated-trial-metric
- Harbor upstream proposal: https://github.com/harbor-framework/harbor/issues/1700

Feedback is welcome, especially from people building or maintaining agent benchmarks.
