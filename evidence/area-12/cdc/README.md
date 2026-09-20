# Area 12 CDC Capture Evidence

## Evidence
- Native PostgreSQL logical replication capture using pgoutput.
- Capture file: area12_pgoutput.bin
- Capture size: 322 bytes.
- Controlled operations: INSERT, UPDATE, DELETE.
- PostgreSQL source table: project02.project02_area12_cdc_test.
- Publication: project02_area12_publication.
- Logical slot: project02_area12_slot.

## Verification
- pgoutput relation metadata was captured.
- INSERT message was captured.
- UPDATE message was captured.
- DELETE message was captured.
- COMMIT message was captured.

## Truth Boundary
- This is genuine local PostgreSQL logical CDC.
- The Olist dataset itself remains a static historical dataset.
- Any historical Olist change stream remains CDC simulation/replay.
- AWS DMS execution is not claimed.

## Cleanup
- Area 12 logical replication slot removed.
- Area 12 publication removed.
- Area 12 CDC test table removed.
- Project02 operational table count remained 9.
