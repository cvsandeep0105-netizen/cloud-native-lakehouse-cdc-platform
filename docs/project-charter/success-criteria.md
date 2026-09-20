# Project 02 — Success Criteria

## 1. Business Outcome

The platform must demonstrate production-oriented cloud data engineering capabilities using a realistic operational dataset and an AWS-aligned lakehouse architecture.

## 2. Data Engineering Success

- Real-world source data is acquired, profiled, documented, and modeled.
- Initial snapshot ingestion is reproducible.
- Incremental change processing is implemented and testable.
- CDC events have explicit identity, ordering, operation type, and source metadata.
- Duplicate events do not create duplicate logical changes.
- Late events, replay, and backfill scenarios are handled deterministically.

## 3. Lakehouse Success

- Raw data remains replayable and traceable.
- Bronze data is stored in an analytics-efficient columnar format.
- Iceberg lakehouse capabilities are demonstrated where technically appropriate.
- Silver represents trusted, transformed, and incrementally maintained data.
- Gold provides business-ready data products.

## 4. Data Quality & Trust

- Schema, null, uniqueness, referential-integrity, duplicate, and business-rule checks are implemented.
- Data-quality failures are measurable and traceable.
- Invalid records can be isolated or quarantined where appropriate.
- Source-to-target reconciliation demonstrates that downstream data remains trustworthy.

## 5. AWS Engineering Success

- AWS architecture is explicitly documented.
- Security boundaries, IAM, encryption, secrets handling, and data access are defined.
- AWS deployment claims are supported by actual evidence when execution is performed.
- Local implementations are clearly distinguished from AWS-verified implementations.

## 6. Reliability & Operations

- Pipelines support safe reruns.
- Failures, retries, checkpoints, and recovery paths are documented and tested.
- Pipeline execution produces operationally useful logs and metrics.
- Freshness, record counts, CDC counts, data-quality results, and failures can be observed.

## 7. Engineering Quality

- Automated tests cover critical transformations and pipeline behavior.
- CI/CD validates code and engineering quality gates.
- Infrastructure as Code is used where appropriate.
- No credentials or secrets are committed to source control.
- Performance and cost characteristics are measured or transparently estimated.

## 8. AI-Enabled Engineering

- AI capabilities assist data engineering tasks such as anomaly investigation, schema-change analysis, quality interpretation, or incident summarization.
- Deterministic data-quality and correctness rules remain authoritative.
- AI does not replace validation, reconciliation, or engineering controls.

## 9. Portfolio Success

- The completed project demonstrates Senior/Lead-level data engineering breadth.
- Architecture and engineering decisions are documented.
- Quantitative evidence supports major technical claims.
- Limitations and trade-offs are explicitly documented.
- The final project can be presented credibly in interviews and integrated into the existing portfolio.
