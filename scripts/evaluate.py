"""Thin entry point: evaluate the saved model.

    uv run scripts/evaluate.py

Like scripts/train.py, this just wires things together. The metric logic would
live in src/my_ml_project/ so it stays testable.
"""

from __future__ import annotations

from pathlib import Path

import joblib

from my_ml_project.data import load_data
from my_ml_project.features import build_features
from my_ml_project.predict import predict

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "model.pkl"


def main() -> None:
    if not MODEL_PATH.exists():
        raise SystemExit("No model found. Run `uv run scripts/train.py` first.")

    model = joblib.load(MODEL_PATH)
    df = load_data()
    X, y = build_features(df)
    preds = predict(model, X)

    # TODO: compare preds to y and print the metrics you care about.
    print(f"Scored {len(preds)} rows against {len(y)} labels.")


if __name__ == "__main__":
    main()
