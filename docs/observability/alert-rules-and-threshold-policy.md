# Alert Rules & Threshold Policy

## Purpose

Define deterministic operational alert conditions for the observability metrics catalog.

## Severity

- INFO: operational information and auditability.
- WARNING: operational review required.
- HIGH: investigation and controlled recovery required.
- CRITICAL: affected downstream processing is blocked pending resolution or explicit review.

## Threshold Boundary

Thresholds are deterministic and configurable. Production threshold approval and final SLO/SLA targets are deferred to Area 32.

## Safety

Alerts do not autonomously mutate production data or infrastructure.

## Recovery

Failure alerts map to the recovery and checkpoint controls established in Areas 29 and 30.

## AWS

Production AWS alert execution is not claimed by this Area.
