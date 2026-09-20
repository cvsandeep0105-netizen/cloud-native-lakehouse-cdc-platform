# Project 02 Cost Model & Workload Assumptions

## Purpose

This document defines the workload assumptions used for Project 02 AWS cost modeling.

## Current Validated Data Baseline

- Olist source datasets: 9
- Source records: 1,550,? — exact dataset-level counts remain authoritative in Area 07.
- Raw storage measured locally: 126,187,259 bytes
- Bronze storage measured locally: 55,491,948 bytes
- Iceberg storage measured locally: 37,614,555 bytes
- Gold storage measured locally: 20,692,089 bytes

## Cost Modeling Workload Scenarios

### Development

- Purpose: engineering and controlled validation.
- Data volume: representative subset or controlled full-data test.
- CDC volume: low.
- Query volume: low.
- Compute: short-lived execution where possible.
- Monitoring: essential operational metrics and logs only.

### Staging

- Purpose: integration and deployment validation.
- Data volume: representative production-shaped workload.
- CDC volume: moderate.
- Query volume: controlled integration and analytical testing.
- Compute: scheduled/on-demand processing.
- Monitoring: operational monitoring with bounded retention.

### Production

- Purpose: continuous operational data platform.
- Data volume: real business workload.
- CDC volume: continuously generated source changes.
- Query volume: business and operational analytics.
- Compute: workload-dependent managed processing.
- Monitoring: production observability with defined retention.

## Primary Cost Variables

- S3 storage GB-month.
- S3 object request volume.
- Data transfer volume.
- Glue processing duration and capacity.
- Glue crawler/catalog activity where applicable.
- Athena data scanned per query.
- Athena query frequency.
- KMS key and API usage.
- CloudWatch log ingestion.
- CloudWatch log retention.
- CloudWatch metrics and alarms.

## Growth Scenarios

- Baseline: current validated dataset footprint.
- 2x: two times the baseline data/CDC workload.
- 5x: five times the baseline data/CDC workload.
- 10x: ten times the baseline data/CDC workload.
- Growth modeling must separately consider storage growth, CDC growth, query growth, and observability growth.

## Cost Model Rules

- Every estimate must state its workload assumptions.
- Storage estimates must distinguish source, processed, quarantine, metadata, and retained historical data.
- Athena estimates must use estimated data scanned rather than raw table size alone.
- Glue estimates must use execution duration and capacity assumptions.
- Monitoring estimates must account for ingestion and retention.
- Estimates must be recalculated when workload assumptions change.

## Boundary

- These are planning assumptions, not actual AWS usage measurements.
- No AWS resources are created in Area 38-C.
- No AWS bill or actual spend is claimed.
- Final deployment measurements occur in Area 39.
