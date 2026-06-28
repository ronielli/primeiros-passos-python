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
| 5 | Herança: `class B(A)`, `super()`, override, `@property`, `@staticmethod`, design "é um(a)" | ✅ |
| 6 | Módulos e pacotes: módulo vs pacote, `__init__.py` (re-export/fachada), import absoluto vs relativo (`from .x import`), `if __name__` | ✅ |
| 7 | Decorators: função como objeto, `@` = açúcar p/ `f = deco(f)`, wrapper com `*args/**kwargs`, decorator COM argumento (3 camadas), `functools.wraps` | ✅ |
| 8 | 🎯 Primeira API com FastAPI: `@app.get/post`, path param tipado, request body com Pydantic (`BaseModel`), `HTTPException(404)`, `status_code=201`, validação 422 automática, doc `/docs` | ✅ |
| 9 | CRUD completo + organização: `PUT`/`DELETE`, `204 No Content`, `response_model` (DTO de saída, filtra campos), `APIRouter` + `include_router` (rotas em módulo próprio) | ✅ |
| 10 | Banco de dados: SQLite + SQLModel, `table=True`, `engine`, `Session`, `Depends` para injeção, `session.add/commit/refresh/delete`, modelo base vs modelo de tabela (`CategoriaBase` + `Categoria`), `lifespan` para inicializar o banco | ✅ |
| 11 | Relacionamentos: `foreign_key`, `Relationship(back_populates=)`, ordem das classes importa (sem forward ref), `selectinload` para eager loading, `TarefaComCategoria` como DTO de leitura aninhado, `IntegrityError` para FK violada | ✅ |
| 12 | Autenticação JWT: `bcrypt` para hash de senha, `jose` para gerar/verificar token, `HTTPBearer` + `Depends` para proteger rotas, cookie `httponly` + header Bearer (suporte mobile e web), `OAuth2PasswordRequestForm` | ✅ |

Exercícios resolvidos em `fundamentos/` (cada um tem `.md` com o enunciado + `.py`
com a solução): **exercicio01 a exercicio09**, + exercicio10/11 (`.md`) = a **API** em
`fundamentos/api/` (CRUD completo de tarefas em memória, organizado com `APIRouter`).
Exercício 12: CRUD de categorias com SQLModel. Exercício 13: relacionamentos FK + Relationship, DTO aninhado, eager loading.

Já praticado na prática: `import` entre arquivos, organização em **pacote** (`banco/`
com `conta.py` + `tipos.py` + `__init__.py` re-exportando), os dois estilos de import
(`import banco.conta` vs `from banco import ...`), e o `if __name__ == "__main__":`
para separar "código que roda" de "código importável".

## Pontos-chave já dominados

- Comprehensions (substituem map/filter; dict comprehension para indexar).
- `*args`/`**kwargs` e spread `*`/`**` (na definição e na chamada).
- Type hints (`nome: str`, `-> dict`).
- `snake_case` (não camelCase), aspas simples dentro de f-string, sem `( )` no if/for.
- EAFP vs LBYL; `.get()` para dict.
- `self`/`__init__` sem dificuldade (vindo de classes do JS).
- `__repr__` deve ser curto/representativo (não embutir logs/listas grandes).

## Próximo passo

➡️ 🧪 **Aula 13 — Testes automatizados com pytest**. A API está funcional mas sem
cobertura de testes. Próximos temas:
1. **pytest** básico — estrutura de teste, `assert`, fixtures.
2. **TestClient** do FastAPI — testar endpoints sem subir o servidor.
3. **Banco em memória** para testes — SQLite `:memory:` para isolar cada teste.
4. Testar fluxo de autenticação: registro → login → rota protegida.
5. Testar casos de erro: 404, 401, 422.

> A API atual roda com: `uv run fastapi dev fundamentos/api/main.py` → abrir `/docs`.

## Como retomar

Abrir o projeto e dizer algo como "vamos pra aula 5" ou "continua de onde paramos".
