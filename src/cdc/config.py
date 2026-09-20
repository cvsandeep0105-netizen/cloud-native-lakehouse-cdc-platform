from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CDC_EVIDENCE_DIR = PROJECT_ROOT / 'evidence' / 'area-12' / 'cdc'
CDC_DOCS_DIR = PROJECT_ROOT / 'docs' / 'cdc'

DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'postgres'
DB_SCHEMA = 'project02'
DB_USER = 'postgres'

CDC_PUBLICATION = 'project02_area12_publication'
CDC_SLOT = 'project02_area12_slot'
CDC_TEST_TABLE = 'project02_area12_cdc_test'

OPERATIONS = ['INSERT', 'UPDATE', 'DELETE']
