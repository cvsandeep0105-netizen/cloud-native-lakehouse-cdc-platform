# Area 28-B — AI-Assisted Data Quality & Anomaly Insight Design

## Purpose

Define a controlled AI-assisted layer for interpreting deterministic Data Quality and reconciliation evidence.

## Authoritative Evidence

- Area 25 Data Quality rule results
- Area 26 reconciliation results
- Dataset metadata from Area 27
- Column metadata from Area 27
- Technical lineage from Area 27
- Pipeline execution metadata

## AI Input Contract

Each AI analysis request must contain structured evidence rather than unrestricted raw datasets.

Required evidence fields:

- rule_id
- dataset
- layer
- check_status
- observed_value
- expected_value
- discrepancy_type
- lineage_context
- execution_timestamp

Sensitive values, credentials, connection strings, and unrestricted customer records are excluded.

## AI Analysis Tasks

### 1. Anomaly Explanation

Explain why a deterministic rule may have failed using the supplied evidence and metadata.

### 2. Impact Analysis

Identify downstream datasets or Gold products potentially affected by a confirmed discrepancy using lineage metadata.

### 3. Investigation Guidance

Produce suggested engineering investigation steps based on the evidence.

### 4. Severity Context

Provide contextual reasoning for investigation priority, while preserving the deterministic severity assigned by the DQ framework.

## AI Output Contract

AI output must contain:

- finding
- evidence_reference
- affected_dataset
- affected_layer
- lineage_impact
- suggested_investigation
- confidence_statement
- human_review_required

AI output is advisory.

## Decision Boundary

AI MAY:
- explain evidence
- summarize discrepancies
- identify possible downstream impact
- suggest investigation steps

AI MUST NOT:
- change DQ status
- alter reconciliation results
- modify source data
- modify lakehouse data
- advance CDC checkpoints
- execute schema changes
- approve production deployment

## Deterministic Precedence

Deterministic engineering evidence has precedence over AI interpretation.

If AI output conflicts with a deterministic rule or reconciliation result, the deterministic result remains authoritative and the conflict becomes an investigation item.

## Human Review

Any AI recommendation that could lead to production action requires human engineering review and explicit approval.

## Auditability

AI-assisted analysis should preserve:

- input evidence identifiers
- analysis timestamp
- AI component/version when implemented
- output
- reviewer
- resulting engineering action

## Local Implementation Boundary

Area 28-B defines the contract only.
No external AI service is invoked.
No AWS Bedrock execution is claimed.
No production lakehouse mutation is permitted.

## Acceptance Gates

- Structured DQ evidence input defined: PASS
- Reconciliation evidence input defined: PASS
- Metadata and lineage context defined: PASS
- AI output contract defined: PASS
- Deterministic precedence defined: PASS
- Human review boundary defined: PASS
- Auditability requirements defined: PASS
- Production mutation prohibited: PASS
