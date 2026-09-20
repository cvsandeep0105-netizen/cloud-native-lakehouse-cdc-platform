# Project 02 — Source Data-Quality Contracts

## Contract Status
Status: Draft — Area 09

## Quality Contract Principles
- Data-quality rules must be deterministic, auditable, and reproducible.
- Source truth must be preserved; quality controls must not silently rewrite source values.
- A detected anomaly must be classified as a contract violation, an accepted source characteristic, or an observation requiring review.

## Structural Quality
- Required datasets must be present.
- Required columns must be present.
- Unexpected or missing columns must be detected.
- Data types must remain compatible with the column-level contract.

## Nullability Quality
- Contractually non-null fields must not contain null values.
- Contractually nullable fields may contain null values.
- Null observations in source data must not be replaced with fabricated defaults.

## Key Quality
- Contracted primary or composite keys must be complete and valid.
- Contracted unique identifiers must not contain unexpected duplicates.
- Source identifiers that are explicitly non-unique must not be incorrectly promoted to unique keys.

## Referential Quality
- Contracted foreign-key relationships must resolve to parent records.
- Orphan references are contract violations for the operational representation.
- Referential failures must be reported rather than silently repaired.

## Numeric Quality
- Numeric values must preserve source precision and semantic meaning.
- Negative values are invalid where the business contract explicitly prohibits them.
- Non-positive payment values and installments are retained as observed source anomalies because Area 07 established them as source characteristics requiring downstream policy rather than silent correction.

## Timestamp Quality
- Timestamp fields must be parseable when populated.
- Contractually required timestamps must not be null.
- Source timestamp values must not be silently shifted or rewritten.

## Domain Quality
- Review scores must remain within the documented 1–5 domain.
- Geographic coordinates must remain within valid latitude and longitude ranges.
- Status and categorical domains should be monitored for unexpected values rather than silently normalized.

## Duplicate Quality
- Exact duplicate source rows must be detected.
- Duplicates that are valid source characteristics must be preserved in the immutable raw boundary.
- Geolocation exact duplicates are preserved because they are observed source characteristics.
- Duplicate review_id values are preserved because review_id is not contractually unique.

## Failure Handling
- Structural, key, and referential contract violations should block affected processing or route affected records to quarantine.
- Accepted source characteristics should remain traceable and be reported.
- Quality results must include rule, dataset, affected-record count, and processing outcome.

## Baseline Evidence
- Area 07 established the initial source-quality baseline.
- Area 08 validated the loaded operational representation against that baseline.
- Future source deliveries must be evaluated against the contract rather than assumed to match the historical baseline.

## Change Control
Quality-rule changes require documented rationale, impact assessment, validation, and approval.
