# Cost Estimation & Scenario Analysis

## Purpose

This document defines a reproducible framework for estimating Project 02 AWS operating cost across development, staging, production, and growth scenarios.

## Estimation Method

- S3: estimate storage, request, and applicable transfer components separately.
- Glue: estimate processing duration multiplied by applicable capacity/pricing assumptions.
- Athena: estimate query frequency multiplied by estimated data scanned per query.
- KMS: estimate applicable key and API usage.
- CloudWatch: estimate log ingestion, retention, metrics, and alarms.
- Estimates must use the AWS Region selected for deployment.

## Scenario Structure

| Scenario | Data Growth | CDC Growth | Query Growth | Purpose |
|---|---:|---:|---:|---|
| Development | Baseline | Baseline | Low | Engineering |
| Staging | 2x | 2x | Moderate | Integration |
| Production | 5x | 5x | Production-shaped | Operational |
| Growth | 10x | 10x | 10x | Capacity planning |

## Cost Components

- S3 storage cost
- S3 request cost
- S3 data-transfer cost where applicable
- Glue processing cost
- Glue catalog/crawler cost where applicable
- Athena query cost
- KMS cost
- CloudWatch logs cost
- CloudWatch metrics and alarms cost

## Estimation Rules

- Use official AWS pricing inputs at the time of deployment.
- Do not treat local filesystem size as an AWS invoice amount.
- Do not assume every local processing stage will map directly to an AWS managed-service charge.
- Separate fixed-like infrastructure costs from usage-based costs.
- Recalculate estimates when workload or architecture changes.
- Record pricing date, Region, units, quantity, and calculation formula for every estimate.

## Financial Safety Boundary

- This analysis is a planning model only.
- It does not represent actual AWS expenditure.
- No AWS resources are created by Area 38-D.
- Terraform apply remains deferred to Area 39.
- Actual deployed-service usage will be measured after deployment.

## Decision Boundary

- Cost optimization must not compromise data correctness.
- Cost optimization must not bypass security controls.
- Cost optimization must not weaken governance or auditability.
- Cost optimization must preserve recovery requirements.
