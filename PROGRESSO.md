# Progresso dos estudos de Python

> Arquivo de continuidade — registra onde paramos para retomar em qualquer máquina.
> **Para o Claude:** se estiver lendo isto, este é o estado do aprendizado. Continue
> do ponto "Próximo passo". O aluno é dev JavaScript/Node experiente aprendendo
> Python do zero, com foco em **backend/APIs**, estilo **hands-on** (faz exercício,
> recebe correção). Ensinar traduzindo de JS para Python. Commits sempre no nome do
> usuário (Ronielli), **sem** atribuição ao Claude.

## Setup do ambiente (já configurado)

- **uv** gerencia deps + venv + lockfile. Rode tudo com `uv run <cmd>`.
- Ferramentas de dev: **ruff** (lint+format), **mypy** (types), **pytest** (testes),
  **pre-commit** (hooks instalados).
- Config central em `pyproject.toml`. Lockfile: `uv.lock`.
- Cache de bytecode centralizado via `PYTHONPYCACHEPREFIX` no `~/.zshrc`.
- VS Code: extensão Ruff (format on save) + cSpell `en,pt,pt_BR`.

### Ao clonar em outra máquina

```bash
# 1. Instalar o uv (https://docs.astral.sh/uv/)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Na pasta do projeto:
uv sync                      # recria o ambiente e instala tudo do uv.lock
uv run pre-commit install    # reativa os hooks de pré-commit
```

## Conteúdo já aprendido

| Aula | Tema | Status |
|------|------|--------|
| 1 | Tipos, listas, dicts, comprehensions (list + dict) | ✅ |
| 2 | Controle de fluxo: for/while, enumerate, zip, match, ternário, continue/break | ✅ |
| 3 | Erros: try/except/else/finally, raise, EAFP, `.get()` | ✅ |
| 4 | Classes/POO: class, `__init__`, self, métodos, raise em método, `__repr__`, dunder | ✅ |

Exercícios resolvidos em `fundamentos/` (cada um tem `.md` com o enunciado + `.py`
com a solução): **exercicio01 a exercicio06**.

## Pontos-chave já dominados

- Comprehensions (substituem map/filter; dict comprehension para indexar).
- `*args`/`**kwargs` e spread `*`/`**` (na definição e na chamada).
- Type hints (`nome: str`, `-> dict`).
- `snake_case` (não camelCase), aspas simples dentro de f-string, sem `( )` no if/for.
- EAFP vs LBYL; `.get()` para dict.
- `self`/`__init__` sem dificuldade (vindo de classes do JS).
- `__repr__` deve ser curto/representativo (não embutir logs/listas grandes).

## Próximo passo

➡️ **Aula 5 — Herança e o resto de POO** (subclasses, `super().__init__()`,
sobrescrever métodos, talvez `@property` e métodos de classe/estáticos).

Depois, na ordem: **módulos (`import`)** → **decorators (`@`)** → 🎯 **primeira API
com FastAPI** (`uv add fastapi`).

## Como retomar

Abrir o projeto e dizer algo como "vamos pra aula 5" ou "continua de onde paramos".
