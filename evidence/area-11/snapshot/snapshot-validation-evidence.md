# Area 11 — Initial Snapshot Pipeline Evidence

## Status
Initial snapshot pipeline locally implemented and validated.

## Source
Olist Brazilian E-Commerce Public Dataset — static historical source.

## Target
PostgreSQL project02 schema.

## Source-to-Target Row Counts

| Table | Rows |
|---|---:|
| customers | 99,441 |
| products | 32,951 |
| sellers | 3,095 |
| category_translation | 71 |
| orders | 99,441 |
| order_items | 112,650 |
| order_payments | 103,886 |
| order_reviews | 99,224 |
| geolocation | 1,000,163 |

## Validation Results
- Source transformation preparation: PASS
- Source/target column compatibility: PASS
- Nullable integer preservation: PASS
- Timestamp conversion: PASS
- Generated identity handling: PASS
- Populated-target write protection: PASS
- Full isolated 9-table snapshot write: PASS
- Isolated source-to-target row reconciliation: PASS
- Primary-key uniqueness: PASS
- Foreign-key integrity: PASS
- Real project02 row-count reconciliation: PASS
- Real target structural integrity: PASS
- Temporary test schema cleanup: PASS

## Safety Boundary
The validated project02 snapshot was never overwritten by the isolated full-snapshot test.

## Claim Boundary
This evidence verifies the initial snapshot pipeline locally against PostgreSQL. It does not claim AWS execution, AWS DMS execution, or production deployment.
