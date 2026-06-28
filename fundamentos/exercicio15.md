# Exercício 15 — Testes automatizados com pytest

## Contexto

A API funciona, mas não tem **nenhum teste**. Vamos cobrir os endpoints com testes
que rodam num banco em memória descartável — cada teste começa do zero, sem depender
do `tarefas.db` real.

## Setup já pronto (não precisa mexer)

- `pyproject.toml` já tem `pythonpath = ["fundamentos/api"]`, então nos testes você
  importa direto: `from main import app`, `from database import ...`.
- `httpx` (necessário pro `TestClient`) já está instalado.

## O que fazer

### 1. `tests/conftest.py` (arquivo novo)

Crie as fixtures compartilhadas:

- **`session`** — engine SQLite em memória (`"sqlite://"` + `StaticPool` +
  `check_same_thread=False`), cria as tabelas com `SQLModel.metadata.create_all`,
  e entrega uma `Session` via `yield`.
- **`client`** — recebe a fixture `session`, sobrescreve `get_session` com
  `app.dependency_overrides`, entrega um `TestClient(app)` via `yield`, e no
  teardown faz `app.dependency_overrides.clear()`.

### 2. `tests/test_tarefas.py` (arquivo novo)

Use a fixture `client`. Escreva testes para:

- `test_raiz` — `GET /` retorna 200 e `{"status": "ok"}`.
- `test_criar_tarefa` — `POST /tarefas` com `{"titulo": "estudar"}` retorna 201,
  e o JSON de volta tem `titulo == "estudar"`, `feita == False` e um `id`.
- `test_buscar_tarefa_inexistente` — `GET /tarefas/999` retorna 404.
- `test_criar_e_buscar` — cria uma tarefa, pega o `id` da resposta, faz
  `GET /tarefas/{id}` e confere que veio a tarefa certa.
- `test_deletar_tarefa` — cria, deleta (`DELETE` → 204), e confirma que buscar
  de novo dá 404.
- `test_criar_tarefa_categoria_inexistente` — `POST /tarefas` com
  `categoria_id` que não existe retorna 422.

### 3. `tests/test_auth.py` (arquivo novo)

Teste o fluxo de autenticação:

- `test_registro` — `POST /usuarios` com email e senha retorna 201.
- `test_login_sucesso` — registra, faz `POST /usuarios/login` e confere que veio
  um `access_token` no JSON.
- `test_login_senha_errada` — registra, tenta login com senha errada → 401.
- `test_me_sem_token` — `GET /usuarios/me` sem token → 401.
- `test_me_com_token` — registra, faz login, pega o token e chama `GET /usuarios/me`
  com o header `Authorization: Bearer <token>`; confere que o email bate.
- `test_listar_tarefas_protegida` — `GET /tarefas` sem token → 401.

> Dica do header: `client.get("/usuarios/me", headers={"Authorization": f"Bearer {token}"})`.

## Como rodar

```bash
uv run pytest                 # roda tudo
uv run pytest -v              # mostra cada teste pelo nome
uv run pytest tests/test_auth.py   # só um arquivo
```

## Restrições

- **Nada de tocar no `tarefas.db` real** — todo teste roda no banco em memória.
- Cada teste deve passar sozinho e em qualquer ordem (sem depender de outro).
- Não mude o código da API pra fazer o teste passar; se um teste pegar um bug real,
  me avise antes de "consertar".

## Conceitos que este exercício fixa

- `TestClient` (≈ supertest), `fixture` com `yield` (≈ beforeEach/afterEach).
- `app.dependency_overrides` (≈ jest.mock) pra injetar o banco de teste.
- `conftest.py` como setup global auto-descoberto.
- Banco isolado por teste com `StaticPool`.
