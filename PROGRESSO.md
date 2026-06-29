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
| 13 | 🧪 Testes com pytest: `TestClient` (≈ supertest), `fixture` com `yield` (setup/teardown), fixture que depende de fixture, `app.dependency_overrides` (≈ jest.mock) p/ injetar banco de teste, banco em RAM (`sqlite://` + `StaticPool`), `conftest.py` (setup global) vs fixture local, testar erros (401/404/422), asserts no conteúdo (não só status), **mock** com `patch` ("patch where it's used") | ✅ |
| 14 | ⚙️ Configuração com `pydantic-settings`: 12-factor config (config vem do ambiente), `BaseSettings` lê env vars + `.env` e **valida/converte tipos**, campo sem default = obrigatório (falha cedo com `ValidationError`), `.env` (segredo, fora do git) vs `.env.example` (modelo, no git), env var MAIÚSCULA ↔ atributo `snake_case` (case-insensitive no nome), plugin `pydantic.mypy` p/ o checker entender (ensinar > ignorar) | ✅ |
| 15 | 🔒 DTO de saída: modelo de tabela ≠ modelo de resposta, `response_model` **filtra** a saída (corta campos fora do DTO), `UsuarioPublico` p/ não vazar `senha_hash`, testar a **ausência** de campos (teste de segurança), bug achado **rodando o app** (`/run`) que os testes não pegavam | ✅ |
| 16 | 🗃️ Migrations com Alembic: `create_all` cria mas nunca **altera** → migrations versionadas, `alembic init` + `env.py` (apresentar `SQLModel.metadata` e a URL do `settings`), ciclo muda modelo → `revision --autogenerate` → **revisa** → `upgrade head`, corrente `revision`/`down_revision` + `alembic_version` (1 linha = head), `downgrade`/`upgrade` (arquivo=receita, banco=prato), default Python (`= 0`) ≠ `server_default` (banco), `nullable` é o add seguro, migrations vão pro git (não o `.db`) | ✅ |
| 17 | 🧹 Limpeza de tipos (mypy zerado): container vazio (`[]`) precisa de anotação (mypy não infere), dict heterogêneo vira `dict[str, object]` → `TypedDict` (≈ `interface` do TS) p/ descrever a forma, `# type: ignore[código]` estreito+comentado p/ falso-positivo de lib (vale p/ mypy E pyright). Regra: info que falta é SUA → anota; info errada vem da LIB → suprime | ✅ |
| 18 | 🔬 Testes avançados: **cobertura** (`pytest-cov`, `--cov-report=term-missing` = mapa de pontos cegos; alta ≠ correto), `parametrize` (1 teste, N entradas ≈ `test.each`), `monkeypatch` (troca atributo só no teste, desfaz sozinho ≈ `jest.spyOn`) p/ token JWT expirado (`access_token_expire_minutes = -1`), `engine.dispose()` no teardown (mata ResourceWarning), `--cov-fail-under` (guard rail de CI). 26 testes, 83% | ✅ |
| 19 | 🐳 Docker: Dockerfile (receita) → image (artefato) → container (rodando), base `ghcr.io/astral-sh/uv`, cache de camadas (copiar deps antes do código ≈ `COPY package.json`), `--host 0.0.0.0` (senão inacessível de fora), `.dockerignore` (não copiar `.env`/`.db`/`.venv`), segredo via `-e` no run (não na imagem), `CMD` roda `alembic upgrade` + `fastapi run`, `docker run -p host:container -e VAR --rm`. API completa rodando em container | ✅ |
| 20 | 🤖 CI com GitHub Actions: `.github/workflows/ci.yml`, roda numa máquina limpa a cada push/PR (`on: push/pull_request`), `jobs`/`runs-on`/`steps` (`uses` = ação pronta tipo `actions/checkout`/`astral-sh/setup-uv`, `run` = comando), reusa as tasks `poe` (lint/types/cov), `SECRET_KEY` via `env:` no passo de teste (CI não tem `.env`), segredo real → GitHub Secrets. CI (push, nuvem, não pula) vs pre-commit (commit, local, pula) | ✅ |

Exercícios resolvidos em `fundamentos/` (cada um tem `.md` com o enunciado + `.py`
com a solução): **exercicio01 a exercicio09**, + exercicio10/11 (`.md`) = a **API** em
`fundamentos/api/` (CRUD completo de tarefas em memória, organizado com `APIRouter`).
Exercício 12: CRUD de categorias com SQLModel. Exercício 13: relacionamentos FK + Relationship, DTO aninhado, eager loading. Exercício 14: autenticação JWT. Exercício 15: testes com pytest (`tests/conftest.py` com fixtures `session`/`client` + `dependency_overrides`, `tests/test_tarefas.py` e `tests/test_auth.py` cobrindo CRUD, auth e casos de erro — 12 testes passando). Exercício 16: configuração com `pydantic-settings` (`api/config.py` com `Settings(BaseSettings)`, `.env` + `.env.example`, `SECRET_KEY`/`DATABASE_URL`/expiração saíram do código). Exercício 17: DTO de saída `UsuarioPublico` (para de vazar `senha_hash` nas respostas) + testes de não-vazamento. Exercício 18: migrations com Alembic (`alembic/` com `env.py` ligado ao `SQLModel.metadata` + `settings.database_url`, 3 migrations: schema inicial, `descricao` na categoria, `prioridade` na tarefa com `server_default`); `create_all` saiu do `lifespan` (só os testes usam). Exercício 19: limpeza de tipos — mypy zerado (`TypedDict` em ex03/04, `list[str]` nas contas, `# type: ignore[arg-type]` no selectinload). Exercício 20: testes avançados — `tests/test_categorias.py` (CRUD), `parametrize` (rotas protegidas) e `monkeypatch` (token expirado) no test_auth, cobertura 76%→83% com `poe cov` (`--cov-fail-under=80`). Exercício 21: Docker — `Dockerfile` (base uv, migrations+`fastapi run` no CMD) + `.dockerignore`; `docker build`/`run` com a API completa rodando em container (testado com curl). Exercício 22: CI — `.github/workflows/ci.yml` roda lint/format/types/cov a cada push/PR (GitHub Actions, `SECRET_KEY` via env).

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

➡️ **Aula 20 — a definir.** A API está funcional, **com testes** (26 testes, 83%
cobertura), config externalizada, sem vazar senha_hash, **com migrations (Alembic)**,
mypy zerado e **containerizada (Docker)**. Candidatos a próximo tema:
1. **Deploy real na nuvem** — Fly.io / Railway / Render (subir a imagem Docker que já
   temos). É o passo que faltou: do container local pro ar de verdade.
2. **CI com GitHub Actions** — rodar `poe test`/`lint`/`types` a cada push (o repo já
   tem tudo pronto pra isso).
3. Fechar buracos de cobertura (`PUT /tarefas`, CRUD de usuário) ou melhorias da API
   em `project-api-next-steps` (EmailStr, email único, paginação, filtrar por usuário).
4. Opcional: slim na imagem Docker (multi-stage build; hoje são ~378MB).

### Ferramentas de produtividade já instaladas (Aula 13)

- **`uv run poe <task>`** — atalhos (ver `[tool.poe.tasks]`): `dev`, `test`, `test:v`,
  `watch`, `lint`, `fix`, `fmt`, `types`.
- **`uv run ptw .`** (ou `poe watch`) — re-roda os testes ao salvar (≈ `jest --watch`).
- Config: `pythonpath`/`filterwarnings` no pytest, `extraPaths` no basedpyright
  (`[tool.pyright]`), tudo no `pyproject.toml`.

> A API atual roda com: `uv run poe dev` → abrir `/docs`. Testes: `uv run poe test`.

## Como retomar

Abrir o projeto e dizer algo como "vamos pra aula 5" ou "continua de onde paramos".
