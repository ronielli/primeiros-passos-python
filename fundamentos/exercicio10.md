# Exercício 10 — 🎯 Primeira API com FastAPI

**Tema:** criar uma API REST de verdade. Rotas como decorators, path/query params,
request body com validação automática (Pydantic), e a doc interativa (Swagger).

> Aqui tudo se junta: decorators viram rotas, type hints viram validação, dict/list
> viram JSON. É o "Express + Zod" do Python — mas com validação e docs de brinde.

## 0. Instalar o FastAPI

```bash
uv add "fastapi[standard]"
```

Isso adiciona o FastAPI + o servidor (uvicorn) ao `pyproject.toml` e ao `uv.lock`.

## 1. Estrutura

Crie uma pasta **`api/`** na raiz do projeto (saindo de `fundamentos/`):

```
api/
└── main.py
```

## 2. A API — em `api/main.py`

Monte uma mini-API de uma "lista de tarefas" (to-do), com estes endpoints:

### a) `GET /` — health check
Retorna `{"status": "ok"}`.

### b) `GET /tarefas` — listar todas
Retorne uma lista de tarefas. Comece com uma lista "em memória" no topo do arquivo:
```python
tarefas = [
    {"id": 1, "titulo": "Aprender FastAPI", "feita": False},
    {"id": 2, "titulo": "Tomar café", "feita": True},
]
```

### c) `GET /tarefas/{tarefa_id}` — buscar uma (path param)
- O `{tarefa_id}` na rota vira **argumento da função** com type hint:
  ```python
  @app.get("/tarefas/{tarefa_id}")
  def buscar(tarefa_id: int):   # FastAPI converte e valida "int" sozinho
      ...
  ```
- Se não existir, lance `HTTPException(status_code=404, detail="Tarefa não encontrada")`
  (`from fastapi import HTTPException`).

### d) `POST /tarefas` — criar (request body com validação)
- Defina um **modelo Pydantic** pro corpo do request:
  ```python
  from pydantic import BaseModel

  class TarefaNova(BaseModel):
      titulo: str
      feita: bool = False
  ```
- A função recebe esse modelo como parâmetro; o FastAPI valida o JSON sozinho:
  ```python
  @app.post("/tarefas")
  def criar(tarefa: TarefaNova):
      ...
  ```
- Gere um novo `id`, guarde na lista `tarefas` e **retorne a tarefa criada**.

## 3. Rodar

```bash
uv run fastapi dev api/main.py
```

Abra **http://127.0.0.1:8000/docs** — a doc interativa (Swagger). Teste cada
endpoint por ali, inclusive o POST (botão "Try it out").

## Conceitos praticados

- `@app.get(...)` / `@app.post(...)` — rotas são **decorators**.
- **Path param** (`/{id}`) com type hint = conversão + validação automática.
- **Request body** com modelo **Pydantic** = validação do JSON sem você escrever `if`.
- `HTTPException` para respostas de erro (404, etc.).
- dict/list de Python → JSON automático.
- Doc interativa gerada sozinha a partir dos type hints.

## Dica (vindo do JS)

| Express | FastAPI |
|---------|---------|
| `app.get("/x", (req, res) => ...)` | `@app.get("/x")` + `def ...` |
| `req.params.id` | argumento `id: int` da função |
| `req.body` + validação manual (Zod) | parâmetro `tarefa: TarefaNova` (Pydantic) |
| `res.json({...})` | só `return {...}` |
| `res.status(404)` | `raise HTTPException(404, ...)` |
