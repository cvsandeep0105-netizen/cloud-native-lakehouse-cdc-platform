from pathlib import Path

def capture_file(path: Path, payload: bytes) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    return path.stat().st_size

def validate_capture(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(path)
    if path.stat().st_size == 0:
        raise ValueError(f'CDC capture is empty: {path}')
