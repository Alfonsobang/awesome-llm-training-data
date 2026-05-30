# Harbor OpenClaw Financial Trajectory Audit

This example is a small, dependency-free audit profile for financial-agent trajectories stored in Harbor's Agent Trajectory Interchange Format (ATIF).

It is designed around a synthetic OpenClaw-style financial data lookup trajectory. It does not contain private data, real user data, investment advice, trading signals, or proprietary workflows.

## Why This Exists

Final-answer correctness is not enough for financial agents. A useful evaluation should also ask:

- Was the user instruction retained in the trace?
- Were tool calls linked to their observations?
- Did retrieved evidence identify its public or synthetic source?
- Did any tool argument cross the evaluation cutoff?
- Did the agent call a trading, order-placement, or private-data tool?
- Did the final answer preserve a non-advice boundary?

## Files

```text
examples/harbor-openclaw-finance-trajectory-audit/
|-- README.md
|-- audit_trajectory.py
|-- sample-openclaw-finance-trajectory.json
`-- test_audit_trajectory.py
```

## Run

```bash
python examples/harbor-openclaw-finance-trajectory-audit/audit_trajectory.py \
  examples/harbor-openclaw-finance-trajectory-audit/sample-openclaw-finance-trajectory.json
```

Run tests:

```bash
python -m unittest discover \
  -s examples/harbor-openclaw-finance-trajectory-audit \
  -p "test_*.py"
```

## Example Report

The included synthetic trajectory should produce a `pass` verdict with:

- one retained user step,
- two tool calls,
- two linked observations,
- one source-grounded retrieval result,
- zero cutoff violations,
- zero prohibited tool calls,
- a visible non-investment-advice boundary.

## Relationship To Harbor Validation

This script is a domain-specific audit layer. It does not replace Harbor's ATIF schema validator:

```bash
python -m harbor.utils.trajectory_validator trajectory.json
```

Use Harbor's validator for ATIF schema conformance. Use this example for additional finance-specific evidence checks.

## Safety Boundary

The sample uses synthetic fixture metadata and a `fixture://` source URI. Replace it only with clearly public data that your evaluation is permitted to use.
