# Exercício 12 — Persistência com SQLite + SQLModel

## Contexto

A API de tarefas agora usa SQLite para persistir dados. Neste exercício você vai
adicionar um segundo recurso — **categorias** — para praticar o mesmo fluxo do zero.

## O que fazer

1. Em `api/database.py`, adicione o modelo `Categoria` com os campos:
   - `id: int | None` — chave primária, autoincrement
   - `nome: str`

2. Crie `api/routers/categorias.py` com CRUD completo:
   - `GET /categorias` — lista todas as categorias
   - `GET /categorias/{id}` — busca por id (404 se não encontrar)
   - `POST /categorias` — cria nova categoria (status 201)
   - `DELETE /categorias/{id}` — deleta (status 204, 404 se não encontrar)

3. Registre o novo router em `api/main.py`.

## Restrições

- Não copie o `tarefas.py` inteiro — escreva do zero usando ele como referência.
- Use o alias `SessionDep` como no router de tarefas.

## Como testar

```bash
uv run fastapi dev fundamentos/api/main.py
```

Abra `/docs` e teste os 4 endpoints de `/categorias`.
