# Project 02 — Engineering Runbook

## Purpose
Operational and interview runbook for the Cloud-Native Lakehouse, CDC & AI-Ready Data Platform on AWS.

## Run the Demo
From the project root:

```powershell
.\scripts\demo.ps1
```

Expected result: `PROJECT 02 DEMO STATUS: READY`

## Demo Validation
- Environment: Python, Terraform, AWS CLI
- Automated tests: 15/15 PASS
- Local Iceberg datasets: 9/9
- AWS deployment: S3, Glue, Athena verified
- AWS Raw datasets: 9/9
- AWS Bronze datasets: 9/9
- Terraform: No changes
- KMS rotation: enabled
- Data Quality: 63/63 PASS
- Reconciliation: 60/60 PASS
- Gold products: 6

## Safety Boundary
The demo is read-only. It does not run Terraform apply, destroy infrastructure, delete AWS data, rebuild Bronze data, or expose credentials or secrets.

## AWS Boundary
S3, KMS, Glue Catalog, Athena, IAM and CloudWatch infrastructure are deployed and validated. Local Apache Iceberg execution was validated separately. AWS-native Iceberg table deployment is not claimed. AWS DMS, Step Functions, EventBridge and Secrets Manager remain evaluated candidates.

## Evidence
Area evidence: `evidence/`
AWS deployment evidence: `evidence/area-39/`

## Engineering Report
`docs/engineering-report/engineering-report.html`

## Repository
https://github.com/cvsandeep0105-netizen/cloud-native-lakehouse-cdc-platform
