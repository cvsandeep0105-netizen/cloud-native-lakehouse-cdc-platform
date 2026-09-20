# AWS Service Cost Drivers & Pricing Inputs

## Pricing Verification Boundary

- Pricing inputs are based on current AWS official pricing documentation reviewed for Area 38.
- Final deployment-time pricing must be revalidated for the selected AWS Region.
- Project 02 target AWS Region: ap-south-1.
- No AWS resources are created by this subarea.

## Amazon S3

- Primary drivers: storage volume, object requests, data transfer, and applicable storage-class/lifecycle behavior.
- Project relevance: raw, bronze, silver, gold, quarantine, and metadata lake storage.
- Cost-control inputs: Parquet/Iceberg storage efficiency, file layout, lifecycle policy, and unnecessary duplicate copies.

## AWS Glue

- Primary drivers: ETL/DPU execution time, crawler usage, Data Catalog metadata usage, and applicable Glue features.
- Glue ETL and crawler usage is billed based on service usage; pricing varies by Region.
- Project relevance: Glue Data Catalog and potential managed processing.
- Cost-control inputs: job duration, DPU allocation, crawler frequency, and metadata footprint.

## Amazon Athena

- SQL query cost driver: data scanned under the per-query pricing model.
- Athena documentation notes that compression, partitioning, and columnar formats can reduce scanned data.
- Project relevance: querying Iceberg/Parquet data stored in S3.
- Cost-control inputs: partition pruning, column projection, Parquet/Iceberg layout, query limits, and workgroup controls.

## AWS KMS

- Primary drivers: customer-managed key existence and applicable API usage.
- Project relevance: encryption architecture for protected AWS resources.
- Cost-control inputs: minimize unnecessary customer-managed keys and avoid unnecessary cryptographic API calls.

## Amazon CloudWatch

- Primary drivers: log ingestion, log storage/retention, metrics, alarms, and other enabled observability features.
- Project relevance: platform monitoring and operational evidence.
- Cost-control inputs: log retention, useful metric selection, alert design, and avoidance of unnecessary high-volume logging.

## IAM

- Standard IAM usage has no direct service charge.
- IAM remains a security/control-plane dependency rather than a primary cost driver.

## Pricing Input Register

| Service | Primary Cost Driver | Project Usage | Regional Revalidation Required |
|---|---|---|---|
| S3 | Storage, requests, transfer | Data lake | YES |
| Glue | DPU/job/crawler/catalog usage | Catalog/processing | YES |
| Athena | Data scanned or compute model | Analytics queries | YES |
| KMS | Key and API usage | Encryption | YES |
| CloudWatch | Logs, metrics, alarms | Observability | YES |
| IAM | No standard direct charge | Access control | YES |

## Evidence Boundary

- Pricing documentation source: official AWS pricing documentation.
- No AWS bill is represented.
- No actual AWS spend is represented.
- No AWS deployment is claimed.
- Terraform apply remains deferred to Area 39.
