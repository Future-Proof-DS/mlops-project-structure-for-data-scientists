# Containerize the project so it runs the same anywhere.
FROM python:3.12-slim

# Install uv, the same tool you use locally.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app
COPY . .

# Install dependencies from the lockfile into the container's environment.
RUN uv sync --frozen --no-dev

# Default command trains the model. Swap this for your own entry point or service.
CMD ["uv", "run", "scripts/train.py"]
