# FinAgentBench Seed Spec

FinAgentBench Seed is the proposed next shape of this repository: a small, runnable, public-safe benchmark seed for financial LLM agents.

It is intentionally a seed, not a leaderboard. The goal is to help teams design stronger financial-agent evaluations without private data, proprietary workflows, investment advice, or trading signals.

## Problem

Most finance-evaluation demos over-focus on final answers. Real financial agents fail through process mistakes:

- using the wrong source,
- mixing fiscal periods,
- losing units or scale,
- leaking future data into a backtest,
- making unsafe investment claims,
- failing to cite evidence,
- and producing tool trajectories that cannot be audited.

FinAgentBench Seed should make these failures visible.

## Benchmark Contract

Every task should define:

- `task_id`
- `family`
- `source_refs`
- `risk_level`
- `instruction`
- `allowed_sources`
- `allowed_tools`
- `prohibited_actions`
- `required_evidence`
- `metrics`
- `known_failure_modes`
- expected `answer.json` schema
- deterministic verifier tests
- at least one known-bad candidate artifact

## Task Families

| Family | What it tests | Common failure |
| --- | --- | --- |
| Search | Find the correct public source or filing page. | Hallucinated or weak source selection. |
| Lookup | Extract exact values with unit and period discipline. | Wrong scale, wrong period, missing citation. |
| Filing QA | Answer from grounded disclosure evidence. | Unsupported explanation or missing citation chain. |
| Backtest Discipline | Run a toy strategy with explicit cutoff. | Future-data leakage and overstated result. |
| Compliance Boundary | Refuse unsafe requests while offering safe alternatives. | Guaranteed-return claims or personalized advice. |
| Trajectory Audit | Inspect tool calls, observations, and evidence. | Final answer passes but trace is unsafe or unauditable. |

## Minimum Viable Benchmark

The minimum attractive benchmark should include:

- 8 to 12 tasks,
- at least 2 known-bad artifacts per family,
- deterministic verifier coverage for every task,
- one repeated-trial aggregation example,
- one ATIF / trajectory audit example,
- one source-governance manifest,
- one Markdown report and one JSON report,
- CI that runs all validators and tests.

## Scoring Philosophy

The score should not be a model leaderboard at first.

Recommended first metrics:

- task pass rate,
- pass@k task rate,
- all-attempts-pass rate,
- missing-evidence rate,
- source-citation failure rate,
- cutoff-violation rate,
- prohibited-financial-claim rate,
- prohibited-tool-call rate,
- trajectory-linkage failure rate.

## Why This Can Be Attractive

This is a useful niche because it sits at the intersection of:

- agent evaluation,
- financial-domain reliability,
- tool-use / browser-use workflows,
- public-source governance,
- and AI safety/compliance evidence.

A small but well-maintained benchmark seed in that intersection is more memorable than a broad awesome list.

## Non-Goals

FinAgentBench Seed should not:

- rank production models,
- provide investment advice,
- publish trading signals,
- include private company data,
- include real user data,
- scrape sources whose terms are unclear,
- or imply regulatory approval.

## Next Three Milestones

1. Add one real search-style task scaffold with a synthetic/public-safe fixture and verifier.
2. Add a repeated-trial report that combines task verifier results and trajectory audit failures.
3. Create a standalone repo or repo alias with clearer naming once the seed has enough runnable substance.
