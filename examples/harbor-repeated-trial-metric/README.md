# Harbor Repeated-trial Metric Example

This example shows a lightweight `metric.py` for Harbor-style repeated-trial agent evaluation. It is designed for benchmarks where each task may run multiple attempts and each verifier returns a binary reward.

The metric reports both optimistic and conservative signals:

- `mean_reward`: average binary reward across all trials.
- `task_pass_rate`: share of tasks with at least one successful trial.
- `pass_at_k`: probability-style pass@k values.
- `pass_pow_k`: Claw-style all-attempts-pass values, where a task only passes if every trial in the first `k` attempts succeeds.
- `missing_reward_rate`: share of trials with no reward object.

This is a generic public example. It does not contain private data, proprietary workflows, or benchmark results.

## Usage

Copy `metric.py` into a Harbor dataset and reference it from the dataset metadata according to Harbor's custom metric workflow.

Harbor's metric runner passes:

```bash
python metric.py --input-path rewards.jsonl --output-path metrics.json
```

Each line in `rewards.jsonl` is expected to be a JSON object. This example accepts either a simple reward object:

```json
{"reward": 1}
```

or a reward object with task metadata:

```json
{"task_name": "task-a", "reward": 1}
```

When `task_name` is missing, the script treats each line as its own task, which is useful for quick local smoke tests but less useful for real benchmark reporting.

## Why This Matters

For agent evaluations, one successful run can hide instability. `Pass@k` answers whether the agent can solve the task at least once in `k` tries. `Pass^k` or all-attempts-pass answers a stricter question: whether success is consistent across repeated tries. Both views are useful, and neither should be confused with production readiness.
