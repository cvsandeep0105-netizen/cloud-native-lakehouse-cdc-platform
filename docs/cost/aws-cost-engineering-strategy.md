# AWS Cost Engineering Strategy

## Purpose

This document defines the cost-engineering strategy for Project 02 before AWS deployment.

## Cost Engineering Principles

- Measure cost drivers before deployment.
- Separate development, staging, and production cost assumptions.
- Prefer predictable and usage-aligned services.
- Minimize unnecessary data movement and duplicate storage.
- Control Athena query scanning through partitioning and data-layout discipline.
- Apply S3 lifecycle policies where retention requirements permit.
- Monitor CloudWatch log volume and retention.
- Use least-privilege IAM and avoid unnecessary always-on compute.
- Keep AWS deployment reversible and evidence-driven.
- Never trade data correctness, security, governance, or recoverability solely for cost reduction.

## Primary AWS Cost Drivers

- Amazon S3: storage, requests, and data transfer.
- AWS Glue: catalog and data-processing usage.
- Amazon Athena: data scanned by queries.
- AWS KMS: key usage and applicable API operations.
- Amazon CloudWatch: logs, metrics, alarms, and retention.
- IAM: no direct charge for standard IAM usage; associated AWS services may incur charges.
- Terraform: no AWS service charge; infrastructure lifecycle is managed through Terraform.

## Cost-Control Boundaries

- AWS resources are not created in Area 38-A.
- Terraform apply remains deferred to Area 39.
- No production AWS workload is assumed during cost estimation.
- Cost estimates must identify their assumptions and measurement period.
- AWS pricing is region-specific and may change; deployment-time pricing verification is required.

## Capacity Scenarios

- Development: minimal controlled workload for engineering validation.
- Stage: representative workload for integration and operational validation.
- Production: real workload with defined retention, availability, monitoring, and recovery requirements.
- Growth scenarios must account for increasing source data, CDC volume, storage, query volume, and monitoring volume.

## Cost Optimization Decision Framework

1. Identify the measurable cost driver.
2. Establish the baseline assumption.
3. Evaluate architectural alternatives.
4. Estimate operational and financial impact.
5. Validate security, correctness, reliability, and governance impact.
6. Select only reversible and evidence-supported optimizations.

## Evidence Requirements

- AWS pricing assumptions must be documented.
- Workload assumptions must be documented.
- Cost calculations must be reproducible.
- Optimization decisions must identify the affected AWS service.
- No AWS deployment claim may be made without deployment evidence.

## Project Boundary

- Project 02 uses AWS as the target cloud platform.
- Local execution remains the validated engineering environment until Area 39 deployment.
- Area 38 establishes cost engineering readiness; it does not represent an AWS bill or actual production spend.
