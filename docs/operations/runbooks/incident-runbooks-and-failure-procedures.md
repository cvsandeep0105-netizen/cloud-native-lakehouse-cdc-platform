# Operational Incident Runbooks

## Standard Incident Lifecycle

DETECT -> CLASSIFY -> CONTAIN -> PRESERVE -> RECOVER -> VALIDATE -> RESUME -> RECORD -> ESCALATE

## RB-01 Pipeline Failure

1. Confirm alert and run identifier.
2. Identify failed orchestration stage.
3. Inspect structured operational events.
4. Preserve the last committed checkpoint.
5. Classify the failure using Area 30.
6. Retry only when the failure class permits retry.
7. Otherwise restart, replay, backfill, quarantine, or escalate according to the recovery matrix.
8. Validate DQ and reconciliation gates.
9. Resume downstream stages only after dependency gates pass.
10. Record incident evidence.

## RB-02 CDC Capture or Ordering Failure

1. Confirm CDC capture alert.
2. Inspect source position and event ordering.
3. Reject invalid ordering rather than silently applying it.
4. Preserve the committed checkpoint.
5. Validate duplicate and idempotency controls.
6. Replay from the last valid checkpoint when permitted.
7. Validate event ordering before downstream processing.

## RB-03 Checkpoint Failure

1. Confirm checkpoint commit failure.
2. Do not advance the checkpoint.
3. Record the checkpoint before failure.
4. Restart from the last committed position.
5. Reprocess uncommitted events.
6. Commit only after successful processing.
7. Verify persisted checkpoint after recovery.

## RB-04 Data Quality Failure

1. Confirm deterministic DQ rule failure.
2. Identify dataset, rule, and observed value.
3. Block affected downstream stages.
4. Investigate source/transformation cause.
5. Correct through controlled change management.
6. Re-run DQ validation.
7. Resume only after blocking rules pass.

## RB-05 Reconciliation Failure

1. Confirm reconciliation discrepancy.
2. Identify affected source and downstream layers.
3. Block dependent Gold products.
4. Compare authoritative source, Raw, Bronze, Silver, and Gold evidence.
5. Preserve existing valid state.
6. Correct only the identified failing component.
7. Re-run reconciliation.
8. Resume downstream processing after trust is restored.

## RB-06 Schema Compatibility Failure

1. Stop affected processing or deployment.
2. Identify schema change.
3. Determine additive versus breaking change.
4. Apply Area 23 compatibility controls.
5. Require human review for breaking changes.
6. Validate migration and CDC compatibility.
7. Resume only after compatibility gates pass.

## RB-07 Gold or Lakehouse Failure

1. Confirm Gold/lakehouse failure.
2. Identify affected product/table.
3. Preserve authoritative Silver state.
4. Validate file layout and Iceberg table state.
5. Rebuild or replay only the affected product.
6. Validate grain, row counts, metrics, DQ, and reconciliation.
7. Publish downstream output only after validation.

## RB-08 Recovery and Escalation

Retryable failures follow approved retry policy.

Non-retryable failures require controlled investigation.

Critical failures require human review before resumption.

Repeated SLO breaches require engineering remediation rather than indefinite retries.

## RB-09 Incident Closure

An incident may close only after:

- Root failure class recorded.
- Checkpoint state verified.
- Recovery action recorded.
- DQ gates validated.
- Reconciliation gates validated.
- Downstream dependency state validated.
- SLO impact recorded.
- Evidence stored.
- Required escalation completed.

## Safety

No runbook permits bypassing deterministic CDC, checkpoint, DQ, reconciliation, schema, security, or governance controls.

Production mutation must remain limited to the explicitly approved recovery action.

## AWS Boundary

AWS production execution is not claimed by this Area.
