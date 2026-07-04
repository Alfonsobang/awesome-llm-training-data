# Repository Metadata Update

The public GitHub repository metadata should match the current project direction. The repository started as a generic Awesome list, but the strongest current asset is the runnable Financial Agent Eval Seed.

## Desired Description

```text
Public-safe financial LLM agent evaluation seed with runnable tasks, verifiers, governance, and Harbor-style templates.
```

## Desired Topics

```text
agent-evaluation
data-governance
evaluation
financial-ai
harbor
llm
openclaw
rag-evaluation
synthetic-data
training-data
```

## Why This Matters

The first GitHub screen currently describes the repo as a curated list. That weakens conversion because the repo has become a runnable finance-agent evaluation seed with task specs, deterministic verifiers, repeated-trial reporting, source governance, benchmark-card metadata, and Harbor-style templates.

The target description should make the value clear in one glance without overclaiming.

## What Not To Claim

- Official Harbor support.
- Production readiness.
- Investment advice.
- Trading signals.
- Adoption numbers.
- Private-domain expertise or employer-specific workflows.

## Validation

Validate the local metadata specification:

```bash
python tools/validate_repo_metadata.py
```

After repository settings are updated on GitHub, validate the live metadata:

```bash
python tools/validate_repo_metadata.py --live
```

The live check is intentionally not part of CI yet because the current integration can push code but does not expose repository-settings write access.
