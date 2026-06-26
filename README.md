# Estudos de Python

Projeto de aprendizado de Python para backend, partindo de uma base em JavaScript.

## Requisitos

- [uv](https://docs.astral.sh/uv/) (gerenciador de dependências e ambiente)

## Setup

```bash
# Instala todas as dependências (cria o .venv automaticamente)
uv sync

# Ativa os hooks de pré-commit (lint/format automático antes de cada commit)
uv run pre-commit install
```

## Comandos do dia a dia

| Tarefa | Comando |
|---|---|
| Rodar um arquivo | `uv run python arquivo.py` |
| Lint (achar/consertar problemas) | `uv run ruff check --fix .` |
| Format (formatar o código) | `uv run ruff format .` |
| Type check (validar os tipos) | `uv run mypy .` |
| Rodar os testes | `uv run pytest` |
| Adicionar uma dependência | `uv add nome-do-pacote` |
| Adicionar uma dep de dev | `uv add --dev nome-do-pacote` |

## Estrutura

```
.
├── pyproject.toml         # metadados, dependências e config das ferramentas
├── uv.lock                # versões travadas (não editar à mão)
├── .pre-commit-config.yaml
├── aula*.py / exercicio*.py  # material de estudo
└── tests/                 # testes (pytest)
```
