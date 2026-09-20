# Observability Runtime & Metrics Collection

## Purpose

Provide a local read-only observability collector that consumes existing deterministic project evidence and emits structured operational metrics.

## Collection Boundary

The collector reads existing evidence only. It does not mutate PostgreSQL, Iceberg, Silver, Gold, source data, checkpoints, or AWS resources.

## Runtime Signals

- Data-quality evidence availability
- Reconciliation evidence availability
- AI operational evidence availability
- Orchestration evidence availability
- Recovery evidence availability
- Deterministic control evidence
- Production mutation during collection

## Collection Mode

READ_ONLY

## Production Boundary

Production mutation is prohibited during observability collection.

## AWS Boundary

Production AWS telemetry collection is not executed by this Area.
