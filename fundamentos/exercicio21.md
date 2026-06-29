# Exercício 21 — Containerizar a API com Docker

## Contexto

A API está completa (testada, migrada, configurável). Falta empacotá-la num
**container** pra rodar isolada, do jeito que iria pra produção. Meta: `docker run`
sobe a API, aplica as migrations e responde no `localhost:8000`.

## Parte A — `Dockerfile` (na raiz do projeto)

Crie o arquivo `Dockerfile` com estas etapas (cada linha comentada na aula):

```dockerfile
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
```

## Parte B — `.dockerignore` (na raiz)

Pra não copiar lixo/segredo pra dentro da imagem:

```
.venv
.git
__pycache__
*.pyc
*.db
.env
.pytest_cache
.ruff_cache
.mypy_cache
.coverage
htmlcov
```

## Parte C — Build

```bash
docker build -t tarefas-api .
```

A primeira vez baixa a imagem base (demora um pouco). No fim deve dizer algo como
`naming to docker.io/library/tarefas-api`.

## Parte D — Run

```bash
docker run --rm -p 8000:8000 \
  -e SECRET_KEY=um-segredo-qualquer \
  -e DATABASE_URL=sqlite:///estudos.db \
  tarefas-api
```

Deve aparecer o log do Alembic (`Running upgrade ...`) e depois o uvicorn subindo.

## Parte E — Dirigir (provar que funciona)

Em **outro terminal**:

```bash
curl localhost:8000/                                   # {"status":"ok"}
curl -X POST localhost:8000/usuarios \
  -H 'Content-Type: application/json' \
  -d '{"email":"docker@x.com","senha":"1234"}'         # 201, sem senha_hash
```

Pra parar: `Ctrl+C` no terminal do `docker run`.

## Restrições

- O `.env` **não** entra na imagem — segredo vai via `-e` no `docker run`.
- `--host 0.0.0.0` no `fastapi run`, senão a API fica inacessível de fora.
- Use `uv sync --frozen` (respeita o `uv.lock`, não atualiza nada).

## Conceitos que este exercício fixa

- Dockerfile (receita) → image (artefato) → container (rodando).
- Cache de camadas: copiar deps antes do código (= `COPY package.json` antes).
- `-p host:container` (portas), `-e` (env/config), `--rm` (limpeza).
- Migrations rodam na subida do container; segredos entram em runtime.
- `0.0.0.0` vs `127.0.0.1` dentro do container.
