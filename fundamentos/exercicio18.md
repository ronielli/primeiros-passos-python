# Exercício 18 — Migrations com Alembic

## Contexto

Hoje o schema do banco nasce de `SQLModel.metadata.create_all()` no `lifespan`. Isso
só cria tabelas que faltam — **nunca altera** uma tabela existente. Vamos trocar por
**migrations versionadas** com Alembic, que registram cada mudança de schema em um
arquivo (git para o banco).

## Dependência

```bash
uv add alembic
```

## Parte A — Inicializar e conectar o Alembic aos seus modelos

### 1. Inicializar

Na raiz do projeto:

```bash
uv run alembic init alembic
```

Isso cria a pasta `alembic/` (com `env.py` e `versions/`) e o arquivo `alembic.ini`.

### 2. `alembic/env.py` — apresentar os modelos e a URL

O Alembic precisa de duas coisas suas: o **metadata** dos modelos (pra comparar) e a
**URL do banco**. No topo do `env.py`, adicione o path da API e os imports:

```python
import sys
from pathlib import Path

# deixa o Python achar os modulos da API (mesma ideia do pythonpath dos testes)
sys.path.append(str(Path(__file__).resolve().parents[1] / "fundamentos" / "api"))

from sqlmodel import SQLModel
import database  # noqa: F401  (importa p/ registrar TODAS as tabelas no metadata)
from config import settings
```

Depois, no corpo do `env.py`:

- Troque `target_metadata = None` por `target_metadata = SQLModel.metadata`.
- Faça o Alembic usar a sua URL: logo após `config = context.config`, adicione
  `config.set_main_option("sqlalchemy.url", settings.database_url)`.

> Por que `import database` com `# noqa`? Importar o módulo executa as definições de
> classe (`Categoria`, `Tarefa`, `Usuario`), e é isso que as registra no
> `SQLModel.metadata`. Sem esse import, o autogenerate acharia o metadata vazio.

## Parte B — Primeira migration (o schema atual)

```bash
uv run alembic revision --autogenerate -m "schema inicial"
```

Abra o arquivo gerado em `alembic/versions/`. **Leia-o** — deve ter `op.create_table`
para `categoria`, `tarefa` e `usuario`. (Se vier vazio, o `import database` não pegou.)

Aplique:

```bash
uv run alembic upgrade head
```

Confira que a tabela `alembic_version` foi criada e as suas tabelas existem.

## Parte C — Uma mudança de schema de verdade

Agora o motivo de tudo isto. No `database.py`, adicione um campo na `Tarefa`:

```python
class TarefaBase(SQLModel):
    titulo: str
    feita: bool = False
    prioridade: int = 0          # <-- campo novo
    categoria_id: int | None = Field(default=None, foreign_key="categoria.id")
```

Gere a migration da mudança e aplique:

```bash
uv run alembic revision --autogenerate -m "add prioridade na tarefa"
uv run alembic upgrade head
```

Leia o novo arquivo: deve ter um `op.add_column(...)` com `prioridade`. Repare que
ele **não** recriou nada — só adicionou a coluna. Isso é o que o `create_all` jamais
faria.

Teste o `downgrade` (reverter o último passo) e depois reaplicar:

```bash
uv run alembic downgrade -1     # volta 1 passo (remove a coluna)
uv run alembic upgrade head     # aplica de novo
```

## Parte D — Tirar o create_all do lifespan

Como o schema agora é responsabilidade do Alembic:

- Em `main.py`, remova a chamada `create_db_and_tables()` do `lifespan` (pode deixar
  o `lifespan` vazio com só `yield`, ou remover se não usar mais).
- **NÃO** apague `create_db_and_tables()` do `database.py` — os testes (`conftest.py`)
  ainda usam `SQLModel.metadata.create_all` no banco em memória, e isso está certo:
  em teste a gente cria o schema na hora, não roda migration.

## Como testar

```bash
uv run poe test                    # 18 testes continuam verdes
uv run alembic current             # mostra em qual revision o banco está
uv run alembic history             # mostra a corrente de migrations
uv run poe dev                     # API sobe sem recriar o schema sozinha
```

## Restrições

- A pasta `alembic/versions/` **vai** para o git (as migrations são código).
- `tarefas.db` continua fora do git.
- Sempre **ler** o arquivo gerado pelo autogenerate antes de aplicar.

## Conceitos que este exercício fixa

- `create_all` cria, mas nunca altera — por isso precisamos de migrations.
- Ciclo: muda modelo → `revision --autogenerate` → revisa → `upgrade head`.
- `revision`/`down_revision` formam a corrente; `alembic_version` marca onde o banco está.
- `upgrade`/`downgrade` — aplicar e reverter.
- Migration é código versionado; schema deixa de ser "automágico" no boot.
