# Financial Agent Evaluation Issue Backlog

This backlog contains focused issues that can turn the current seed into a larger public task pack. Each issue is scoped to produce a reusable artifact, not just a discussion thread.

## 1. Add Harbor-style exact-data-lookup task template

Goal: create a deterministic task for extracting exact financial values from a public or synthetic filing fixture.

Deliverables:

- `task.toml`
- `instruction.md`
- synthetic filing fixture
- reference `answer.json`
- verifier tests for exact values, citations, and disallowed claims

Safety boundary:

- Synthetic or clearly public fixture data only.
- No investment advice or private-data inference.

## 2. Add toy backtest task with cutoff verifier

Goal: create a small fixed-rule backtesting task that checks whether the agent respects a time cutoff and avoids look-ahead bias.

Deliverables:

- synthetic price fixture
- fixed moving-average or threshold rule
- verifier checks for data window, metrics, and cutoff discipline
- explicit statement that the task is not a trading strategy recommendation

## 3. Add compliance-refusal task template

Goal: evaluate whether a financial agent refuses requests for guaranteed returns, insider-like information, or market manipulation while still offering safe alternatives.

Deliverables:

- unsafe user prompt fixture
- expected safe refusal criteria
- verifier tests for forbidden phrases and safe alternative framing
- examples of acceptable and unacceptable outputs

## 4. Add synthetic financial fixture pack

Goal: provide a small reusable fixture pack for financial agent evaluation without licensing, privacy, or market-data ambiguity.

Deliverables:

- synthetic filing excerpt
- synthetic price series
- synthetic macroeconomic time series
- synthetic tool-call trace
- fixture policy explaining intended and prohibited use

## 5. Add repeated-trial financial agent report example

Goal: show how repeated attempts change interpretation of financial-agent evaluation results.

Deliverables:

- sample run records
- pass@k, Pass^k, missing-evidence rate, and cutoff-violation rate
- short report template
- explanation of why single-run success is insufficient for financial workflows

## 6. Map public finance data source constraints

Goal: document which public data sources are suitable for benchmark examples and what constraints evaluators should check.

Deliverables:

- source list
- license or terms notes
- update cadence
- allowed example use
- constraints that should push a task toward synthetic fixtures

## 7. Add benchmark card template

Goal: make each future financial-agent task pack easier to review and govern.

Deliverables:

- benchmark motivation
- data provenance
- task families
- leakage risks
- safety boundaries
- known limitations
- intended and out-of-scope use

## 8. Add trajectory evidence schema

Goal: define the minimum trace evidence needed to audit a financial-agent run.

Deliverables:

- source retrieval trace fields
- tool-call trace fields
- calculation artifact fields
- verifier output fields
- refusal and safety incident fields

## 9. Add financial forecasting / pastcasting template

Goal: evaluate bounded forecasts with explicit information cutoffs, uncertainty, and no investment advice.

Deliverables:

- pre-cutoff fixture
- instruction with allowed evidence window
- output schema with uncertainty and limitations
- verifier checks for cutoff leakage

## 10. Add financial tool-use recovery template

Goal: evaluate whether an agent can recover from failed financial tool calls or missing fields.

Deliverables:

- synthetic tool API responses
- one missing-field scenario
- required recovery behavior
- verifier checks for tool-call order, error handling, and final evidence
