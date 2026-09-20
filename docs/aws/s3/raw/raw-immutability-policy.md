# Area 17 — Raw Immutability Policy

## Policy
Once a raw ingestion artifact is accepted, downstream processing must treat it as immutable.

## Prohibited
- Silent overwrite.
- Destructive in-place correction.
- Untracked transformation.
- Removal required only to make a downstream job pass.

## Corrections
Corrections must produce a new controlled artifact or downstream derived state.

## Replay
Immutable raw artifacts remain available as a source for replay and recovery.
