# Containerize the project so it runs the same anywhere.
# Part 2 of the series covers this in depth. This is a working starting point.
FROM python:3.12-slim

# Install uv, the same tool you use locally.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app
COPY . .

# Install dependencies from the lockfile into the container's environment.
RUN uv sync --frozen --no-dev

# Default command trains the model. In Part 2 you swap this for your service.
CMD ["uv", "run", "scripts/train.py"]
