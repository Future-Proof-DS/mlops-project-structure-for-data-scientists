# ML Project Template for Data Scientists

A clean, production-minded starting point for any machine learning project. Fork
it, rename one package, and you have the structure most MLOps-mature teams have
converged on, already wired up with `uv`, tests, and CI.

This is the companion template to **Part 1** of the
[MLOps for Data Scientists](https://futureproofds.com/blog/mlops-for-data-scientists)
course. The article explains *why* the structure looks like this; this repo is
the structure itself, ready to build on.

---

## Why this exists

Most models never reach production. Not because the modeling was bad, but
because the code around the model was never built to leave a laptop. This
template fixes that on day one: your logic lives in an installable package, your
notebooks stay for exploration, and your scripts are thin entry points that
production can actually call.

The ML code is intentionally left as **stubs**. This is a template, not a demo,
so you drop in your own project.

## How to use it

1. Click **Use this template** (or fork it) to start your own project.
2. Rename the `src/my_ml_project/` package to your project's name, and update the
   matching line in `pyproject.toml` (`[tool.hatch.build.targets.wheel]`).
3. Implement the stubs in `src/my_ml_project/` (`data.py`, `features.py`,
   `train.py`, `predict.py`). Each has a `TODO` marking what goes there.
4. Build from there.

**Prefer the command line?**

```bash
# With the GitHub CLI (creates a fresh repo from the template):
gh repo create my-project --template Future-Proof-DS/mlops-project-structure-for-data-scientists --clone

# Or plain git (copy the files, start your own history):
git clone https://github.com/Future-Proof-DS/mlops-project-structure-for-data-scientists.git my-project
cd my-project && rm -rf .git && git init
```

### The tooling (works before you write any code)

This project uses [uv](https://docs.astral.sh/uv/). With `uv run`, you don't
create or activate a virtual environment yourself: uv reads `pyproject.toml`,
builds an isolated environment, installs dependencies, and caches it.

```bash
uv sync --all-extras   # set up the environment
uv run pytest          # runs the example test (green out of the box)
uv run ruff check .    # lints the project
```

Once you've implemented the stubs, the scripts run end to end:

```bash
uv run scripts/train.py       # trains your model, saves models/model.pkl
uv run scripts/evaluate.py    # scores it
```

To explore in the notebook, install the notebook extra and launch Jupyter:

```bash
uv sync --all-extras
uv run jupyter lab            # opens notebooks/01_exploration.ipynb
```

> **No uv?** Install it in one line:
> `curl -LsSf https://astral.sh/uv/install.sh | sh`
> ([other platforms](https://docs.astral.sh/uv/getting-started/installation/)).

## What goes where

```
.
├── src/my_ml_project/      # YOUR CODE. Installable package, imported everywhere.
│   ├── data.py          #   loading + cleaning
│   ├── features.py      #   feature engineering (plain, testable functions)
│   ├── train.py         #   training logic
│   └── predict.py       #   inference logic
├── scripts/             # Thin entry points. Production runs these, not notebooks.
│   ├── train.py         #   parses args, calls src/, saves the model
│   └── evaluate.py
├── notebooks/           # Your workshop. Notebooks import FROM src/, never the reverse.
│   └── 01_exploration.ipynb
├── tests/               # Because your logic is functions, it's testable.
├── config/              # Config and hyperparameters, out of the code.
├── data/                # Raw data is immutable; everything downstream transforms it.
│   ├── 01_raw/          #   untouched source data
│   ├── 02_interim/      #   partially cleaned
│   ├── 03_processed/    #   model-ready
│   └── 04_predictions/  #   model outputs
├── models/              # Saved model artifacts.
├── Dockerfile           # Containerize the project.
├── docker-compose.yml   # Local orchestration.
├── .github/workflows/   # CI/CD pipeline.
├── pyproject.toml       # Dependencies + project metadata.
└── uv.lock              # Exact, reproducible dependency versions.
```

## The conventions that matter

- **`src/` layout.** Your package must be *installed* to import it, which
  surfaces the import bugs that would otherwise only appear in deployment.
- **Notebooks import from `src/`, not the other way around.** When you write
  production logic inside a notebook, that's the signal to extract it.
- **Scripts stay thin.** They parse arguments and call into `src/`. The real,
  testable logic never lives in the script.
- **`data/01_raw/` is immutable.** You never edit it. Every other data folder is
  a reproducible transformation of it.
- **Dependencies are locked** (`uv.lock`), so the project builds the same on your
  machine, in CI, and in a container.
