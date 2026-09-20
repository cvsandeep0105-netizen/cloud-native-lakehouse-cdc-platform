# Cost Optimization Controls & Guardrails

## Purpose

This document defines cost controls and guardrails for Project 02 AWS deployment.

## S3 Controls

- Use Parquet and Iceberg to reduce unnecessary storage and scan volume.
- Avoid duplicate copies of the same dataset unless required by an explicit data-layer boundary.
- Apply lifecycle policies according to documented retention requirements.
- Monitor object count and storage growth.
- Avoid unnecessary cross-Region data transfer.

## Athena Controls

- Use partition pruning where applicable.
- Prefer columnar formats and selective column projection.
- Avoid unrestricted exploratory queries against large datasets.
- Use workgroup-level controls where appropriate.
- Monitor bytes scanned and query frequency.

## Glue Controls

- Use the minimum appropriate processing capacity.
- Avoid unnecessarily frequent crawlers.
- Prefer deterministic metadata registration where suitable.
- Monitor processing duration and capacity consumption.
- Stop or disable unused processing resources where applicable.

## KMS Controls

- Avoid unnecessary customer-managed keys.
- Reuse keys when security boundaries permit.
- Monitor cryptographic API usage.
- Retain required encryption controls regardless of cost.

## CloudWatch Controls

- Use defined log-retention periods.
- Avoid excessive high-volume debug logging in production.
- Keep metrics focused on operationally meaningful signals.
- Review alarms and remove obsolete monitoring.
- Monitor log ingestion and retention growth.

## Infrastructure Controls

- Use Terraform as the infrastructure source of truth.
- Review Terraform plan before deployment.
- Require human approval before production apply.
- Avoid deploying unused AWS services.
- Use environment-specific configuration.
- Apply deletion protection and retention controls where required.

## Budget and Alert Guardrails

- Establish a planned monthly budget before production deployment.
- Configure billing/cost alerts when supported by the deployment design.
- Investigate unexpected cost increases before expanding workloads.
- Treat sustained cost variance as an operational issue requiring review.

## Optimization Safety Rules

- Cost reduction must not bypass IAM controls.
- Cost reduction must not weaken encryption.
- Cost reduction must not remove required audit evidence.
- Cost reduction must not violate retention requirements.
- Cost reduction must not compromise data quality.
- Cost reduction must not violate recovery objectives.

## Deployment Boundary

- These controls are architecture and deployment guardrails.
- AWS resources are not created in Area 38-E.
- Terraform apply remains deferred to Area 39.
- Actual cost behavior will be validated after deployment.
