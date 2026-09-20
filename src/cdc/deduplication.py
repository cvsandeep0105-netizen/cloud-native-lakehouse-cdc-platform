from hashlib import sha256

def build_event_identity(source_system: str, source_schema: str, source_table: str,
                         transaction_id: str, source_position: str,
                         event_sequence: str) -> str:
    parts = [source_system, source_schema, source_table, transaction_id, source_position, event_sequence]
    if any(value is None or value == '' for value in parts):
        raise ValueError('All CDC identity components are required')
    canonical = '|'.join(str(value) for value in parts)
    return sha256(canonical.encode('utf-8')).hexdigest()


def deduplicate_event_ids(event_ids: list[str]) -> list[str]:
    seen = set()
    unique = []
    for event_id in event_ids:
        if event_id not in seen:
            seen.add(event_id)
            unique.append(event_id)
    return unique


def apply_idempotently(processed_event_ids: set[str], event_id: str) -> bool:
    if event_id in processed_event_ids:
        return False
    processed_event_ids.add(event_id)
    return True
