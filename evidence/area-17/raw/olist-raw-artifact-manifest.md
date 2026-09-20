# Area 17 — Raw Olist Artifact Manifest

## Source
Olist Brazilian E-Commerce Public Dataset

## Artifact Count
9 CSV files

## Integrity Manifest

| File | Size Bytes | SHA256 |
|---|---:|---|
| olist_customers_dataset.csv | 9033957 | 983A422239E1712DED753B3BF9ECF47DC73F144D306029DCFA99E70A226883D2 |
| olist_geolocation_dataset.csv | 61273883 | B514F6FC991B9566AEBA02AA5D67E2C3630F034B60A0E05AA0D082A3B66D88D6 |
| olist_order_items_dataset.csv | 15438671 | 0BC4D068C4FE38CBB01BD90E8746E3C613FE7B4BAEF75FAB7B0E329701C3E279 |
| olist_order_payments_dataset.csv | 5777138 | 4F713964F2815DBBAA40B9488268C55AAC3627BFCE5AA96CF58D1F3616DE3CC0 |
| olist_order_reviews_dataset.csv | 14451670 | 012B61C7593E34F51FA614EFDF802B9C7056CE6AAE5307DDB93236E7CFC797D7 |
| olist_orders_dataset.csv | 17654914 | 8DF58EF3D2D7E9944010F7BEECD9B75367F5588EC6E3C91CEC19AE3345EF9ECF |
| olist_products_dataset.csv | 2379446 | 3E6569628A17FBC75FD206EE357B59E20364B9AFA90F5B6CD5B4D624C58AA9CC |
| olist_sellers_dataset.csv | 174703 | 1F643D2B950373B85735E7794B20986F528D7A000432E7C6F9BCBB44D0846A0E |
| product_category_name_translation.csv | 2613 | A81F0D1F27B27E7293F761BC79E3CE8F348EE39C4B3ED3E49BDE38F478586278 |

## Immutability Boundary
These source artifacts are treated as immutable acquisition artifacts.

## AWS Boundary
This manifest validates local source artifacts. It does not claim that the artifacts have been uploaded to AWS S3.

## Source Boundary
The original Olist dataset remains static historical source data. It does not provide a native CDC stream.
