"""Feature engineering.

Keep feature logic here as plain, testable functions, so your notebook and your
training script share one source of truth. Add features one small function at a
time, and test each one in tests/.
"""

from __future__ import annotations

import pandas as pd


def build_features(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Turn a raw DataFrame into a feature matrix X and a target y."""
    # TODO: build your features and split off the target column.
    raise NotImplementedError("Implement build_features() for your project.")
