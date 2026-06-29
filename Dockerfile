FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app

# deps primeiro (cache de camada)
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

# resto do código
COPY . .
RUN uv sync --frozen --no-dev

EXPOSE 8000

# migrations + sobe a API (host 0.0.0.0 pra ser acessível de fora do container)
CMD ["sh", "-c", "uv run alembic upgrade head && uv run fastapi run fundamentos/api/main.py --host 0.0.0.0 --port 8000"]
