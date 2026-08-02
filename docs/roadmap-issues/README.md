# Roadmap Issue Drafts

These drafts are ready to open as GitHub issues when issue-write permission is available.

The repository currently has runnable financial-agent evaluation tasks, source-governance reports, and known-good / known-bad reports. The next useful issues should turn that seed into a more inspectable and reusable benchmark artifact.

## Next Issue Series

These are the highest-leverage public issues to open next. They are designed for real contributors: each one has a narrow task, a public-safe fixture path, a verifier expectation, and a non-advice boundary.

### Issue 5: Add A Multi-document Financial Lookup Task

#### Why

Financial agents often answer from the wrong filing, wrong issuer, or wrong reporting period when several documents are available. A multi-document lookup task would test source disambiguation before numeric extraction.

#### Scope

Add one task where the candidate must select the correct synthetic filing excerpt from several issuer / period / document-type candidates, then extract one or more exact values with units and citations.

#### Proposed Artifacts

- `examples/financial-agent-eval-seed/harbor-template/multi-document-lookup/`
- `examples/financial-agent-eval-seed/task-specs/multi-document-lookup.json`
- passing and known-bad candidate artifacts
- task-pack manifest and task-index updates

#### Acceptance Criteria

- Includes at least three candidate documents with conflicting issuer, period, or document type.
- Verifier fails wrong issuer, wrong period, wrong document type, missing unit, and unsupported citation.
- Uses only synthetic or public-safe fixture data.
- Does not include investment advice, trading signals, private data, or production-readiness claims.

### Issue 6: Add A Table-text Reconciliation Task

#### Why

Finance answers often require reconciling table values with narrative explanations. Agents can quote a plausible paragraph while ignoring a conflicting table value, or calculate from the right table but cite the wrong text.

#### Scope

Add a task where the candidate must reconcile a synthetic financial table with a short management-discussion excerpt, return a grounded explanation, and disclose any mismatch.

#### Proposed Artifacts

- `examples/financial-agent-eval-seed/harbor-template/table-text-reconciliation/`
- `examples/financial-agent-eval-seed/task-specs/table-text-reconciliation.json`
- verifier tests for table value, narrative support, citation support, and limitation disclosure

#### Acceptance Criteria

- Fixture includes one table and one narrative excerpt with a deliberate reconciliation point.
- Verifier checks numeric value, period, unit, cited table path, cited narrative section, and limitation text.
- Known-bad answer demonstrates citation theater or a table/narrative mismatch.
- Public-safe and non-advice boundaries are explicit.

### Issue 7: Add A Source-conflict Resolution Task

#### Why

Financial agents should prefer primary or newer official sources over stale summaries when evidence conflicts. This is a realistic failure mode for search, RAG, and tool-use workflows.

#### Scope

Add a task with a synthetic news summary, a stale secondary source, and a later official filing correction. The candidate must choose the governed source and explain why weaker evidence was rejected.

#### Proposed Artifacts

- `examples/financial-agent-eval-seed/harbor-template/source-conflict-resolution/`
- `examples/financial-agent-eval-seed/task-specs/source-conflict-resolution.json`
- source-manifest update for the synthetic source types

#### Acceptance Criteria

- Verifier checks selected source priority, as-of date, rejected source IDs, and citation support.
- Known-bad answer chooses the stale or unofficial source.
- Report explains the source-governance signal without ranking models.
- No live trading, private data, or proprietary examples.

### Issue 8: Add A Data-freshness Disclosure Task

#### Why

Financial agents often answer current-looking questions even when data is stale or unavailable. A freshness task tests whether the agent states the as-of date and refuses to guess.

#### Scope

Add a task where the fixture has a fixed as-of date and a missing current field. The candidate must answer with the available date, state what is unavailable, and avoid inventing an updated value.

#### Proposed Artifacts

- `examples/financial-agent-eval-seed/harbor-template/data-freshness-disclosure/`
- `examples/financial-agent-eval-seed/task-specs/data-freshness-disclosure.json`
- freshness-focused verifier and known-bad artifact

#### Acceptance Criteria

- Verifier checks as-of date, unavailable-field disclosure, no invented current value, and non-advice language.
- Known-bad answer hallucinates a current value.
- Task is deterministic and runs in CI without network access.
- Documentation explains why stale-data handling matters in financial-agent evaluation.

### Issue 9: Add A Harbor Task-pack Compatibility Note

#### Why

The repo has Harbor-style task templates, but maintainers and users need a compact compatibility note before deciding whether to adapt the task pack or discuss it upstream.

#### Scope

Write a short compatibility note that maps the seed task-pack manifest to Harbor-style concepts: task directory, fixtures, verifier command, expected artifacts, repeated-trial report, and safety boundary.

#### Proposed Artifacts

- `docs/harbor-task-pack-compatibility-note.md`
- links from `docs/harbor-finance-task-pack-blueprint.md`, `FINAGENTBENCH.md`, and `llms.txt`

#### Acceptance Criteria

- States that this is not an official Harbor adapter.
- Lists exactly what is implemented today and what remains adapter-specific.
- Links task-pack manifest, benchmark card, repeated-trial report, source-governance report, and candidate workflow.
- Avoids promotional language, adoption claims, and production-readiness claims.

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
