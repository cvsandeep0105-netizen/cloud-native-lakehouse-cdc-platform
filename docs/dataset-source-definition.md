# Project 02 — Dataset Source Definition

## Dataset
Brazilian E-Commerce Public Dataset by Olist

## Publisher
Olist

## Distribution Source
Kaggle — olistbr/brazilian-ecommerce

## Dataset Characteristics
- Approximately 100,000 orders.
- Historical data covering 2016–2018.
- Real commercial data provided by Olist.
- Data has been anonymized.
- Multiple related relational datasets are provided as CSV files.

## Project Role
The dataset is the historical operational source for Project 02. It will be represented in PostgreSQL and used as the basis for snapshot ingestion and reproducible incremental CDC simulation/replay scenarios.

## CDC Boundary
The published Olist dataset is static historical data. It is not itself a live CDC feed.
Any change events generated from the historical dataset will be explicitly classified as CDC simulation/replay.
Genuine local PostgreSQL CDC was independently verified in Area 02.
AWS DMS execution will not be claimed unless AWS runtime evidence is obtained.

## License
CC BY-NC-SA 4.0 — Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International.

## Attribution
Data provided by Olist and distributed through the Olist Brazilian E-Commerce Public Dataset on Kaggle.

## Acquisition Boundary
The dataset will be acquired from the identified Kaggle distribution source. Downloaded source files will be preserved as immutable acquisition evidence and will not be committed to Git.

## Source Integrity
Dataset identity, file inventory, sizes, hashes, schema, and acquisition metadata will be verified after download before downstream processing begins.

## Reference
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
