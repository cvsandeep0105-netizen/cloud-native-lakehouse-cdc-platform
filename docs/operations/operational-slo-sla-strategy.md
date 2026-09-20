# Operational SLO/SLA Strategy

## Purpose

Define measurable operational objectives for the Cloud-Native Lakehouse, CDC & AI-Ready Data Platform.

## Important Boundary

These targets are engineering SLO/SLA design targets for the portfolio platform. They are not claims of an externally contracted AWS production SLA.

## SLO Targets

| SLO | Target | Measurement Boundary | Severity |
|---|---:|---|---|
| Pipeline successful completion | >= 99.0% monthly | Eligible production pipeline runs | HIGH |
| Data freshness | >= 99.0% within 30 minutes | Source-to-Gold eligible workloads | HIGH |
| CDC capture latency | >= 99.0% within 5 minutes | Source change to captured event | HIGH |
| Incremental processing completion | >= 99.0% within 20 minutes | Eligible incremental batches | HIGH |
| DQ gate compliance | 100% blocking rules passed | DQ-controlled datasets | CRITICAL |
| Reconciliation compliance | 100% blocking checks passed | Trust-controlled datasets | CRITICAL |
| Gold product freshness | >= 99.0% within 30 minutes | Published Gold products | HIGH |
| Recovery completion | >= 95% within 60 minutes | Retryable operational incidents | HIGH |
| Critical incident acknowledgement | <= 15 minutes | Critical operational alerts | CRITICAL |
| Critical incident containment | <= 30 minutes | Critical operational alerts | CRITICAL |

## RPO

Target RPO: 0 committed CDC events beyond the last successfully committed checkpoint.

Checkpoint advancement occurs only after successful processing and validation.

## RTO

Target RTO: <= 60 minutes for recoverable pipeline failures.

Non-retryable DQ, reconciliation, schema, or integrity failures require controlled investigation rather than blind retry.

## Error Budget

Each SLO permits a defined error budget. Error-budget consumption must be reviewed when reliability degrades. Repeated SLO breaches require corrective engineering work rather than simply increasing retry frequency.

## SLO Breach Policy

1. Detect through observability metrics.
2. Generate or correlate an alert.
3. Classify the failure.
4. Preserve the committed checkpoint.
5. Apply the Area 30 recovery policy.
6. Validate recovery.
7. Record the incident and SLO impact.
8. Resume downstream processing only when dependency gates pass.

## SLA Thinking

SLA considerations include service availability, freshness commitments, incident response expectations, recovery expectations, data-quality commitments, and communication/escalation obligations.

Actual customer-facing contractual SLA terms are outside the scope of this portfolio implementation.

## Production Safety

SLO/SLA evaluation must not bypass deterministic DQ, reconciliation, schema, CDC, checkpoint, security, or governance controls.

## AWS Boundary

AWS production execution and AWS-managed service SLA claims are not made by this Area.
