# Cost Observability & Budget Monitoring Design

## Purpose

This document defines how Project 02 will observe AWS cost and detect unexpected spending after deployment.

## Cost Signals

- S3 storage growth
- S3 object/request growth
- Glue processing duration and capacity usage
- Glue crawler/catalog activity
- Athena query count
- Athena data scanned
- KMS key/API usage
- CloudWatch log ingestion
- CloudWatch log storage
- CloudWatch metrics and alarms

## Monitoring Dimensions

- Daily cost trend
- Monthly accumulated cost
- Cost by AWS service
- Cost by environment
- Cost against planned budget
- Cost against workload growth
- Cost anomaly investigation

## Budget Guardrails

- Define an approved monthly budget before production deployment.
- Configure budget alerts at planned warning thresholds.
- Investigate unexpected increases before increasing workload capacity.
- Separate expected growth from anomalous spending.
- Record cost investigations as operational evidence.

## Workload-to-Cost Correlation

- Correlate S3 growth with retained data volume.
- Correlate Glue cost with processing duration and workload size.
- Correlate Athena cost with bytes scanned and query volume.
- Correlate CloudWatch cost with log ingestion and retention.
- Correlate KMS cost with key and API usage.

## Alerting Principles

- Alerts should be actionable.
- Avoid excessive alert noise.
- Critical cost anomalies require investigation.
- Cost alerts must not automatically disable production processing without an approved safety mechanism.
- Financial controls must not bypass data-quality, security, governance, or recovery requirements.

## Operational Review

- Review cost trends regularly after deployment.
- Compare actual usage with Area 38 planning assumptions.
- Update assumptions when workload characteristics materially change.
- Record optimization decisions and their operational impact.

## Deployment Boundary

- This is a design for post-deployment cost observability.
- No AWS resources are created in Area 38-F.
- Actual billing metrics become available only after AWS deployment.
- Terraform apply remains deferred to Area 39.
