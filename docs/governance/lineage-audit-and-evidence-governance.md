# Lineage, Audit & Evidence Governance

## Lineage

Lineage must connect source data through Raw, Bronze, Silver, and Gold processing stages.

## Evidence Controls
- Evidence must identify its applicable Area and control.
- Evidence must be reproducible.
- Validation results must be attributable.
- Synthetic/local evidence must be clearly distinguished from production evidence.
- AWS execution must never be inferred from local validation.

## Claim Integrity
- Simulated CDC cannot be represented as deployed AWS CDC.
- Architecture design cannot be represented as deployed infrastructure.
- Local execution cannot be represented as AWS execution.
- Formal certification cannot be claimed from portfolio evidence alone.

## Evidence Retention

Final engineering evidence must be retained according to the project evidence policy.
