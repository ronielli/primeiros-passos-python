# Exercício 11 — Completar o CRUD + organizar com APIRouter

**Tema:** `PUT` e `DELETE`, status `204`, `response_model` (DTO de saída) e
`APIRouter` (separar rotas em módulo próprio — reusando pacotes da Aula 6).

> Continuação da API do exercício 10. Vamos fechar o CRUD e **organizar** o código,
> saindo do `main.py` único.

## Parte A — Completar o CRUD (no `fundamentos/api/main.py` mesmo, por enquanto)

### 1. `PUT /tarefas/{tarefa_id}` — atualizar
- Recebe **os dois**: `tarefa_id: int` (path) **e** `dados: TarefaNova` (body).
- Ache a tarefa pelo id; se não existir → `HTTPException(404)`.
- Atualize `titulo` e `feita` e **retorne a tarefa atualizada**.

### 2. `DELETE /tarefas/{tarefa_id}` — remover
- `status_code=204` (sucesso sem corpo).
- Ache pelo id; se não existir → `HTTPException(404)`.
- Remova da lista e **não retorne nada**.

> Teste no `/docs`: crie, atualize e delete uma tarefa. Confira o status 204 no delete.

## Parte B — `response_model` (moldar a saída)

### 3. Crie um modelo de **saída** e aplique nas rotas de leitura
```python
class TarefaOut(BaseModel):
    id: int
    titulo: str
    feita: bool
```
- `@app.get("/tarefas", response_model=list[TarefaOut])`
- `@app.get("/tarefas/{tarefa_id}", response_model=TarefaOut)`

Isso garante o **contrato** da resposta (e filtraria qualquer campo extra que você
não quisesse expor).

## Parte C — Organizar com `APIRouter` (o pulo do gato)

Reorganize a API nesta estrutura (reusando pacotes da Aula 6):

```
fundamentos/api/
├── main.py                  ← só cria o app e inclui o router
└── routers/
    ├── __init__.py          ← marca como pacote
    └── tarefas.py           ← TODAS as rotas de /tarefas + os modelos
```

### 4. Em `routers/tarefas.py`
```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/tarefas", tags=["tarefas"])

# ... modelos (TarefaNova, TarefaOut) e a lista "tarefas" ...

@router.get("", response_model=list[TarefaOut])   # vira GET /tarefas
def listar(): ...
# ... e as outras rotas, agora com @router e SEM o "/tarefas" no caminho
#     (o prefix já cuida disso). Ex: @router.get("/{tarefa_id}")
```

### 5. Em `main.py`
```python
from fastapi import FastAPI
from routers import tarefas

app = FastAPI()

@app.get("/")
def raiz():
    return {"status": "ok"}

app.include_router(tarefas.router)
```

## Rodar

```bash
uv run fastapi dev fundamentos/api/main.py
```
Abra `/docs` — repare que as rotas de tarefas agora aparecem agrupadas pela **tag**
"tarefas".

## Conceitos praticados

- CRUD completo: `GET` / `POST` / **`PUT`** / **`DELETE`**.
- Path param + request body **na mesma rota** (PUT).
- `status_code=204` (sucesso sem corpo) no DELETE.
- `response_model` = validar/moldar a **saída** (contrato da API).
- `APIRouter` + `include_router` = organizar rotas em módulos (o "express.Router").
- Reuso de **pacote/`__init__.py`** (Aula 6) na pasta `routers/`.

## Dica (vindo do Express)

| Express | FastAPI |
|---------|---------|
| `const router = express.Router()` | `router = APIRouter(prefix="/tarefas")` |
| `router.put("/:id", ...)` | `@router.put("/{tarefa_id}")` |
| `app.use("/tarefas", router)` | `app.include_router(router)` (prefix vai no router) |
| `res.status(204).end()` | `status_code=204` + `return None` |
