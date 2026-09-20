# Project 02 — Dataset Storage Boundary

## Storage Layout
- data/raw/olist/ — immutable acquired dataset boundary.
- data/raw/olist/brazilian-ecommerce.zip — original downloaded archive.
- data/raw/olist/extracted/ — extracted source files used for controlled processing.
- evidence/area-06/acquisition/ — acquisition and integrity evidence.

## Source Data Rule
- Source CSV files must be treated as immutable.
- Do not edit, rename, overwrite, or transform source files in place.
- Downstream processing must write to separate output boundaries.

## Git Boundary
- Raw dataset files must not be committed to Git.
- Generated processing outputs must not be committed unless explicitly classified as small, reproducible evidence.
- Dataset credentials and authentication tokens must remain outside the repository.

## Reproducibility
- The archive SHA-256 and extracted-file SHA-256 values are recorded in the acquisition manifest.
- The dataset source and license are documented separately.
- The acquisition process uses the Kaggle CLI.

## CDC Boundary
- Static Olist source data is the baseline historical dataset.
- CDC events derived from the dataset are simulation/replay artifacts.
- Genuine PostgreSQL CDC evidence from Area 02 remains separate from simulated Olist change events.
