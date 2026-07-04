# Agent Instructions

This repository is safe for coding agents to inspect and modify. Keep changes conservative, reproducible, and public-data-only.

## Project Shape

- `README.md` and `README.zh-CN.md` are the public entry points.
- `QUICKSTART.md` is the fastest path for a human or agent to run the project.
- `examples/financial-agent-eval-seed/` is the main runnable artifact.
- `examples/financial-agent-eval-seed/run_finance_eval.py` runs deterministic verifier tests and writes JSON/Markdown reports.
- `examples/financial-agent-eval-seed/harbor-template/` contains small Harbor-style task templates.
- `examples/financial-agent-eval-seed/data-sources/source-manifest.json` governs public sources and fixture policy.
- `examples/harbor-openclaw-finance-trajectory-audit/` contains a synthetic ATIF-v1.7 trajectory audit.

## Before Submitting Changes

Run:

```bash
python examples/financial-agent-eval-seed/validate_specs.py
python examples/financial-agent-eval-seed/validate_sources.py
python examples/financial-agent-eval-seed/generate_source_governance_report.py
python examples/financial-agent-eval-seed/run_finance_eval.py
python -m unittest discover -s examples/financial-agent-eval-seed -p "test_*.py"
python examples/financial-agent-eval-seed/validate_harbor_templates.py
python -m unittest discover -s examples/harbor-openclaw-finance-trajectory-audit -p "test_*.py"
python tools/audit_resources.py --root .
python tools/validate_synthetic_fixtures.py
python tools/validate_finance_preference_reviews.py
```

## Content Rules

- Do not add fake links or unverifiable adoption claims.
- Do not add private company data, real user data, proprietary workflows, investment advice, trading signals, or non-public financial information.
- Use synthetic fixtures for executable examples unless the task is purely a public-source reference.
- Prefer deterministic tests over prose-only claims.
- Keep financial claims framed as evaluation, governance, source-grounding, or safety analysis.
