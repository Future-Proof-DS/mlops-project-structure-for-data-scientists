"""Inference logic.

Turns a fitted model and some rows into predictions. In Part 2 of the series, a
FastAPI service calls into here.
"""

from __future__ import annotations

import pandas as pd


def predict(model, X: pd.DataFrame) -> pd.Series:
    """Return predictions for the rows in X."""
    # TODO: call your model on X and return the predictions as a Series.
    raise NotImplementedError("Implement predict() for your project.")
