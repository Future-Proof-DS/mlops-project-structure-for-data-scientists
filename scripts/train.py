"""Thin entry point: train the model and save it.

    uv run scripts/train.py

Production runs a script, never a notebook. All the real logic lives in
src/ml_project/, so this stays a few lines. Implement the package's stubs, then
this runs end to end.
"""

from __future__ import annotations

from pathlib import Path

import joblib

from ml_project.data import load_data
from ml_project.train import train_model

MODELS_DIR = Path(__file__).resolve().parent.parent / "models"


def main() -> None:
    df = load_data()
    model = train_model(df)

    MODELS_DIR.mkdir(exist_ok=True)
    out_path = MODELS_DIR / "model.pkl"
    joblib.dump(model, out_path)
    print(f"✅ Model trained and saved to {out_path}")


if __name__ == "__main__":
    main()
