# Exercício 13 — Relacionamentos entre tabelas

## Contexto

Tarefa e Categoria existem no banco mas são ilhas separadas. Neste exercício você vai
conectar as duas tabelas com ForeignKey e Relationship, e retornar o JSON aninhado.

## O que fazer

### 1. `api/database.py`

Em `Tarefa`, adicione:
- `categoria_id: int | None` com `Field(default=None, foreign_key="categoria.id")`
- `categoria: 'Categoria | None'` com `Relationship(back_populates="tarefas")`

Em `Categoria`, adicione:
- `tarefas: list['Tarefa']` com `Relationship(back_populates="categoria")`

Crie o modelo de leitura aninhado (sem `table=True`):
```python
class TarefaComCategoria(SQLModel):
    id: int | None
    titulo: str
    feita: bool
    categoria: Categoria | None
```

### 2. `api/routers/tarefas.py`

- Importe `TarefaComCategoria` de `database`
- Troque o `response_model` do `GET /tarefas/{id}` para `TarefaComCategoria`

### 3. Antes de testar

Apague o arquivo `tarefas.db` — o schema mudou e o SQLite não altera colunas
automaticamente:

```bash
rm fundamentos/api/tarefas.db
```

## Como testar

```bash
uv run fastapi dev fundamentos/api/main.py
```

1. Crie uma categoria via `POST /categorias`
2. Crie uma tarefa via `POST /tarefas` passando `categoria_id` com o id da categoria
3. Busque a tarefa via `GET /tarefas/{id}` — o JSON deve trazer a categoria embutida

## Restrições

- Não copie código pronto — escreva a partir do que aprendeu
- O `back_populates` dos dois lados deve bater: `"tarefas"` em `Tarefa` aponta para
  o atributo `tarefas` de `Categoria`, e vice-versa
