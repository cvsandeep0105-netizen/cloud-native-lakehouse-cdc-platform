# SLO/SLA Measurement Model

## Purpose

Define deterministic measurement semantics for the operational SLOs established in Area 32-A.

## Measurement Principles

- Numerator and denominator are explicitly defined.
- Zero eligible population is NOT MEASURED, never automatically successful.
- Missing evidence produces INVALID measurement status.
- Retries remain part of the same logical run unless a new run is explicitly created.
- Checkpoint measurements use the last successfully committed position.
- Blocking deterministic DQ and reconciliation controls remain authoritative.
- Incident duration uses recorded operational timestamps.

## Evidence

Every measurement must retain the measurement ID, time window, numerator, denominator or duration, status, and evidence reference.

## Status Values

- MEETS
- BREACH
- NOT MEASURED
- INVALID

## Production Boundary

This model defines measurement semantics only. It does not mutate production systems.

## AWS Boundary

AWS production telemetry is not executed or claimed by this Area.
