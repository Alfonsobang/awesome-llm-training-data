# Synthetic Financial Evaluation Data Playbook

Synthetic fixtures are useful for public examples, but they can also create false confidence. This playbook explains how to use synthetic financial data responsibly in evaluation tasks.

## Good Uses

- Demonstrating verifier logic.
- Testing unit, scale, period, and citation handling.
- Creating safe known-bad examples.
- Exercising cutoff discipline in toy backtests.
- Publishing task templates without private data.

## Bad Uses

- Claiming production realism.
- Comparing investment strategies.
- Publishing synthetic examples as if they represent real issuers.
- Hiding missing source governance behind "synthetic" labels.
- Using synthetic data to imply model performance in live markets.

## Fixture Requirements

Every synthetic fixture should include:

- clear synthetic label,
- small inspectable size,
- source file path,
- fields required by the verifier,
- known limitations,
- and a non-advice boundary.

## Example Fixture Types

| Fixture | What it can test |
| --- | --- |
| Financial statement excerpt | Exact lookup, unit handling, fiscal period. |
| Management discussion excerpt | Filing-grounded explanation and citation support. |
| Toy price series | Cutoff discipline and future-data leakage. |
| Unsafe request text | Compliance refusal and safe alternative. |
| Tool trace JSON | Observation linkage and trajectory audit. |

## Verifier Principles

- Check exact values where possible.
- Require citations or field paths.
- Fail missing limitations.
- Fail investment advice language.
- Fail future-data leakage.
- Keep the test small enough for humans to inspect.

## Current Examples

The current seed includes synthetic fixtures for:

- exact data lookup,
- filing margin explanation,
- toy moving-average backtest,
- and compliance refusal.

See [Financial Agent Eval Seed](../examples/financial-agent-eval-seed).
