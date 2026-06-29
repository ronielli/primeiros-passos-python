# Exercício 20 — Testes avançados (cobertura, parametrize, monkeypatch)

## Contexto

A API tem 18 testes, mas a cobertura é **76%** — há código sem teste, principalmente
o CRUD de categorias (54%) e caminhos de erro do usuário. Vamos usar a cobertura como
mapa pra fechar os buracos, e aprender `parametrize` e `monkeypatch` no caminho.

## Setup (já pronto)

- `pytest-cov` instalado; task `uv run poe cov` mostra o relatório `term-missing`.

## Parte A — Ler o mapa

```bash
uv run poe cov
```

Olhe a coluna `Missing`. Os alvos principais:
- `categorias.py` (54%) — GET lista, GET/{id} (404), PUT, DELETE.
- `usuarios.py` (74%) — token expirado, GET lista, GET/{id} (404), PUT, DELETE.
- `tarefas.py` (77%) — PUT.

## Parte B — `tests/test_categorias.py` (arquivo novo)

Cubra o CRUD de categoria. Sugestão de testes:
- `test_criar_categoria` — POST 201 + id.
- `test_listar_categorias` — cria 2, GET `/categorias` retorna 2.
- `test_categoria_inexistente` — GET `/categorias/999` → 404.
- `test_atualizar_categoria` — POST, PUT muda o nome, confere.
- `test_deletar_categoria` — POST, DELETE → 204, GET → 404.

## Parte C — `parametrize` para rotas protegidas

No `test_auth.py` (ou onde fizer sentido), troque/some um teste parametrizado que
prova que **várias rotas exigem token**:

```python
@pytest.mark.parametrize("metodo, url", [
    ("get", "/tarefas"),
    ("get", "/usuarios/me"),
])
def test_rotas_protegidas_sem_token(client, metodo, url):
    r = getattr(client, metodo)(url)
    assert r.status_code == 401
```

## Parte D — `monkeypatch`: token expirado (o destaque)

No `test_auth.py`, adicione um teste que prova que um JWT vencido dá 401, usando
`monkeypatch` pra fazer o token nascer expirado:

```python
def test_me_token_expirado(client, monkeypatch):
    from config import settings
    client.post("/usuarios", json={"email": "r@g.com", "senha": "1234"})
    monkeypatch.setattr(settings, "access_token_expire_minutes", -1)  # nasce vencido
    token = client.post(
        "/usuarios/login", json={"email": "r@g.com", "senha": "1234"}
    ).json()["access_token"]
    r = client.get("/usuarios/me", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 401
```

## Meta

```bash
uv run poe cov     # cobertura sobe (mira em 90%+ na API)
uv run poe test    # tudo verde
```

Não precisa chegar a 100% — `database.py` tem `get_session`/`create_db_and_tables` que
só rodam em produção. Foque nos routers.

## Conceitos que este exercício fixa

- Cobertura = mapa de pontos cegos (não troféu; alta ≠ correto).
- `parametrize` = um teste, N entradas (≈ `test.each`).
- `monkeypatch` = troca atributo/env só no teste, desfaz sozinho (≈ `jest.spyOn`).
- Testar caminhos de erro (404, 401 expirado) além do feliz.
