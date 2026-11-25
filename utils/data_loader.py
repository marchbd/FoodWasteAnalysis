from pathlib import Path
from typing import Optional

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "Datasetfood.csv"


def load_dataset(path: Path = RAW_DATA_PATH) -> Optional[pd.DataFrame]:
    """Load the source dataset if it exists; otherwise return None."""
    if not path.exists():
        return None
    try:
        return pd.read_csv(path)
    except (OSError, pd.errors.ParserError, UnicodeDecodeError) as exc:
        raise RuntimeError(f"Could not read dataset at {path}: {exc}") from exc
