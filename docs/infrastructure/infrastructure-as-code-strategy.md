# Infrastructure as Code Strategy

## Purpose

Define the Infrastructure as Code strategy for the Cloud-Native Lakehouse, CDC & AI-Ready Data Platform.

## Objectives

- Define AWS infrastructure declaratively.
- Keep infrastructure definitions version controlled.
- Make infrastructure reproducible.
- Separate environments.
- Apply least-privilege security.
- Protect Terraform state.
- Keep secrets outside Terraform source.
- Validate infrastructure before deployment.
- Maintain auditable infrastructure changes.

## Managed Infrastructure Domains

- Amazon S3 data lake
- AWS KMS encryption
- AWS Glue Data Catalog
- Amazon Athena
- AWS IAM
- Amazon CloudWatch
- Supporting AWS security configuration

## Environment Model

The intended environments are:

- dev
- stage
- prod

Environment-specific configuration must be supplied through controlled variables.

## State Management

Terraform state is sensitive infrastructure metadata.

Production state must use protected remote state with controlled access and state locking where supported by the selected backend architecture.

Local development may use local Terraform state during initial validation.

Terraform state must never contain intentionally embedded plaintext secrets.

## Change Management

Infrastructure changes follow:

1. Change definition
2. Terraform formatting
3. Terraform initialization
4. Terraform validation
5. Security review
6. Terraform plan
7. Human approval
8. Controlled apply
9. Post-deployment validation
10. Evidence capture

## Security

- Least privilege is mandatory.
- Public S3 access is blocked.
- Encryption is enabled.
- IAM policies must be scoped.
- Secrets are not hard-coded.
- Production infrastructure must not be changed manually when Terraform owns the resource.

## Deployment Boundary

Area 35 begins Infrastructure as Code implementation.

Terraform configuration can be developed and validated locally.

Actual AWS resource creation requires an explicit controlled deployment operation and is not claimed merely because Terraform configuration exists.
