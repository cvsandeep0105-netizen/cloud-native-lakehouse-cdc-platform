# Incident Communication, Escalation & Handoff

## Communication Model

CRITICAL incidents require immediate human escalation.

HIGH incidents require stage-owner escalation.

WARNING incidents require operational review when recurring.

INFO events are retained for auditability.

## Incident Timeline

Detection -> Acknowledgement -> Classification -> Containment -> Recovery Start -> Recovery Validation -> Resume or Block -> Closure

## Handoff Requirements

Every unresolved incident handoff records incident ID, run ID, stage, severity, timestamps, current state, checkpoint position, failure class, last action, next action, owner, escalation status, SLO impact, and evidence reference.

## SLO/SLA Communication

Every SLO breach records the affected measurement, time window, observed result, and evidence.

RPO communication records the committed checkpoint and any committed-event loss.

RTO communication records detection, recovery-start, and recovery-completion timestamps.

## Checkpoint Safety

Checkpoint advancement cannot be used to hide an unresolved incident.

## Downstream Dependencies

Blocked downstream stages remain blocked until upstream validation and dependency gates pass.

## Human Control

Autonomous incident remediation is disabled.

## AWS Boundary

Production AWS notification execution is not claimed by this Area.
