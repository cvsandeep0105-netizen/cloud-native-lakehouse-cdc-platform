# Area 22-B Integration Evidence

Validation scope: persistent incremental checkpoint integration.

- First bounded batch processed through source position 120.
- Checkpoint 120 persisted to local Iceberg.
- Restart reloaded checkpoint 120.
- Resume began at position 121.
- Second batch advanced checkpoint to 130.
- Simulated failed batch did not advance checkpoint.
- Checkpoint regression was rejected.
- Duplicate event delivery was filtered.
- Temporary test state was removed.

AWS execution is not claimed.
