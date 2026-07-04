# Roadmap Issue Drafts

These drafts are ready to open as GitHub issues when issue-write permission is available.

The repository currently has runnable financial-agent evaluation tasks, source-governance reports, and known-good / known-bad reports. The next useful issues should turn that seed into a more inspectable and reusable benchmark artifact.

## Issue 4: Prepare A Harbor Upstream Discussion Brief

Status: implemented in-repo. Keep this draft as provenance for the maintainer-facing discussion brief.

### Why

The finance task pack now has runnable tasks, a task-pack manifest, a benchmark card, and repeated-trial reports. Before opening an upstream Harbor discussion, the ask should be narrow, respectful, and useful to maintainers.

### Scope

Add a short brief that can be used to ask Harbor maintainers whether this finance-domain example belongs as external reference material, docs, or a minimal example task pack.

### Proposed Artifact

- `docs/harbor-upstream-discussion-brief.md`

### Acceptance Criteria

- States that this is not an official Harbor adapter.
- Links task-pack manifest, benchmark card, repeated-trial report, source-governance report, and verifier commands.
- Asks a specific maintainer-friendly format question.
- Avoids promotional language, adoption claims, private data, investment advice, and production-readiness claims.

## Issue 1: Add Benchmark-card Validator And Generated Seed Benchmark Card

Status: implemented in-repo. Keep this draft as provenance for why the benchmark card exists and as a checklist for future benchmark-card changes.

### Why

The financial-agent eval seed now has runnable tasks, source-governance reports, and known-good / known-bad reports. A benchmark card would make the artifact easier for evaluation engineers and governance reviewers to inspect quickly.

### Scope

Add a benchmark card for `examples/financial-agent-eval-seed` based on `docs/financial-benchmark-card-template.md`.

### Proposed Artifacts

- `examples/financial-agent-eval-seed/benchmark-card.yml`
- `tools/validate_financial_benchmark_card.py`
- README links from the main README, `docs/README.md`, and the seed README.
- CI coverage for the validator.

### Acceptance Criteria

- Card includes intended use, out-of-scope use, source policy, private-data boundary, leakage controls, verifier coverage, reports, and limitations.
- Validator fails when required governance or safety fields are missing.
- The generated card links the 10 current runnable tasks and stable reports.
- No investment advice, trading signals, private company data, real user data, or proprietary workflows are introduced.

## Issue 2: Add Repeated-trial Reporting For The Financial-agent Eval Seed

Status: implemented in-repo. Keep this draft as provenance for why repeated-trial reporting exists and as a checklist for future stability metrics.

### Why

Single-run pass/fail reports are useful, but financial-agent evaluation should also show stability across repeated attempts. Repeated-trial reporting is especially useful for tool use, cutoff discipline, refusal boundaries, and missing evidence.

### Scope

Add a small repeated-trial report generator that can aggregate multiple `run_finance_eval.py` outputs.

### Proposed Artifacts

- `examples/financial-agent-eval-seed/aggregate_trial_reports.py`
- `examples/financial-agent-eval-seed/results/repeated-trial-example-report.md`
- A short section in the seed README showing how to run repeated trials.

### Acceptance Criteria

- Report includes pass rate, pass@k, Pass^k, missing-evidence rate, and unsafe-output rate where applicable.
- Works on a small checked-in example input without network access.
- Does not rank models or claim production readiness.
- Keeps finance-specific safety boundaries visible in the report.

## Issue 3: Add A Harbor-style Task-pack Export Manifest

Status: implemented in-repo. Keep this draft as provenance for why the task-pack manifest exists and as a checklist for future task-pack changes.

### Why

The repo has Harbor-style task directories, but a task-pack manifest would make them easier for agent-framework maintainers to inspect, adapt, or discuss upstream.

### Scope

Add a manifest that lists each current Harbor-style task, its fixture, expected answer, verifier path, source refs, and safety boundary.

### Proposed Artifacts

- `examples/financial-agent-eval-seed/harbor-template/task-pack-manifest.json`
- `examples/financial-agent-eval-seed/validate_task_pack_manifest.py`
- README link from `docs/harbor-finance-task-pack-blueprint.md`.

### Acceptance Criteria

- Manifest lists all 10 current Harbor-style tasks.
- Validator fails if a task directory is missing a fixture, solution, tests, or task metadata.
- Manifest includes source refs and non-advice/private-data boundaries.
- The task-pack is explicitly positioned as a public-safe example, not an official Harbor adapter.
