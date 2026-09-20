# Area 14 — CDC Deduplication Strategy

## Objective
Prevent repeated delivery of the same CDC event from being applied more than once.

## Strategy
1. Establish deterministic event identity.
2. Detect whether the identity has already been processed.
3. Ignore or quarantine repeated delivery according to processing policy.
4. Preserve the original source event identity for auditability.

## Duplicate Definition
A duplicate is the same source event delivered more than once with the same deterministic event identity.

## Non-Duplicate Rule
Two events affecting the same business key are not automatically duplicates. Distinct source changes remain distinct events.

## Scope
Deduplication applies to event delivery. It does not replace source ordering or business-state reconciliation.
