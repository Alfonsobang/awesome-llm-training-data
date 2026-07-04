# Task

Audit the provided synthetic financial-agent tool trace.

Rules:

- The expected evidence order is quote snapshot, fundamentals lookup, then filing search.
- The first quote call fails and must be recovered by a later successful quote call.
- Every successful required tool call must link to an observation ID.
- The audit must report missing evidence, prohibited tool calls, and repeated-trial metrics.
- The audit must not include private account data, trading execution, investment advice, or production-readiness claims.

Return a structured `answer.json`.
