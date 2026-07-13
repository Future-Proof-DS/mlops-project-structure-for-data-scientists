"""Inference logic.

Turns a fitted model and some rows into predictions.
"""

from __future__ import annotations

import pandas as pd


def predict(model, X: pd.DataFrame) -> pd.Series:
    """Return predictions for the rows in X."""
    # TODO: call your model on X and return the predictions as a Series.
    raise NotImplementedError("Implement predict() for your project.")
