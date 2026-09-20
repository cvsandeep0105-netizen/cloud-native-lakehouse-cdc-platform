# Area 37-B Acceptance

## Hardware Baseline

- CPU cores: 4
- Logical processors: 8
- RAM: 7.77 GiB

## Software Baseline

- Python: 3.11.9
- Java: 17.0.12 LTS
- Spark Home: C:\p02_pyspark
- PySpark: 3.5.8
- Pandas: 2.3.3
- PyArrow: 22.0.0

## Workload Baseline

- Raw files: 10
- Raw size: 126,187,259 bytes
- Bronze files: 9
- Bronze size: 55,491,948 bytes
- Iceberg files: 90
- Iceberg size: 37,614,555 bytes
- Gold files: 62
- Gold size: 20,692,089 bytes

## Authoritative Dataset Counts

- customers: 99,441
- geolocation: 1,000,163
- orders: 99,441
- order_items: 112,650
- order_payments: 103,886
- order_reviews: 99,224
- products: 32,951
- sellers: 3,095
- category_translation: 71

## Validation

- CSV row counts validated with pandas parsing: PASS
- Review embedded-newline counting issue avoided: PASS
- Area 37-A strategy evidence: PRESENT
- AWS performance claims: NOT CLAIMED
- AWS deployment: NOT EXECUTED

Status: PASS / FROZEN
