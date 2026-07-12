"""Training logic (the real work, kept out of the thin script).

`train_model` takes data in and returns a fitted model. Keeping it as a
function, not a script, means scripts, notebooks, tests, and pipelines can all
call it without copying code.
"""

from __future__ import annotations

import pandas as pd


def train_model(df: pd.DataFrame):
    """Fit and return a model."""
    # TODO: build your features (see ml_project.features.build_features), fit an
    # estimator on them, and return the fitted model.
    raise NotImplementedError("Implement train_model() for your project.")
