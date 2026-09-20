from .config import OPERATIONS

def expected_operations() -> list[str]:
    return OPERATIONS.copy()

def validate_operation(operation: str) -> None:
    if operation not in OPERATIONS:
        raise ValueError(f'Unsupported CDC operation: {operation}')
