# Exercício 17 — DTO de saída: parar de vazar o senha_hash

## Contexto

Rodando a API (`/run`), descobrimos que **toda resposta de usuário devolve o
`senha_hash`**:

```json
POST /usuarios  →  {"id":2, "senha_hash":"$2b$12$...", "email":"x@y.com"}
```

Isso é uma falha de segurança: o hash nunca deve sair da API. A causa é que as rotas
usam `response_model=Usuario`, e o `Usuario` carrega o `senha_hash`. Vamos criar um
DTO de saída que expõe só o que pode ser público.

## O que fazer

### 1. `api/database.py`

Crie um modelo de leitura pública, **sem** `senha_hash`:

```python
class UsuarioPublico(SQLModel):
    id: int
    email: str
```

(Não mexa no `Usuario` de tabela — o banco continua guardando o hash.)

### 2. `api/routers/usuarios.py`

Troque o `response_model` de **todas** as rotas que devolvem usuário, de `Usuario`
para `UsuarioPublico`:

- `GET /usuarios` → `response_model=list[UsuarioPublico]`
- `GET /usuarios/me` → `response_model=UsuarioPublico`
- `GET /usuarios/{usuario_id}` → `response_model=UsuarioPublico`
- `POST /usuarios` → `response_model=UsuarioPublico`
- `PUT /usuarios/{usuario_id}` → `response_model=UsuarioPublico`

> O `get_current_user` continua usando o `Usuario` completo internamente — ele
> precisa do objeto inteiro. O que muda é só o que a rota **devolve**.

### 3. Teste que prova a correção (o ponto da aula)

No `tests/test_auth.py`, adicione um teste que **afirma a ausência** do campo —
é isso que faltava antes:

```python
def test_registro_nao_vaza_senha_hash(client):
    r = client.post("/usuarios", json={"email": "r@g.com", "senha": "1234"})
    assert r.status_code == 201
    assert "senha_hash" not in r.json()      # o campo NÃO pode estar na resposta
    assert "senha" not in r.json()
```

Faça o mesmo raciocínio para `GET /usuarios/me` (registra, loga, chama `/me` com o
token, e afirma que `senha_hash` não está no corpo).

## Como testar

```bash
uv run poe test       # 18 + 2 testes novos, todos verdes
uv run poe dev        # POST /usuarios no /docs não deve mais mostrar senha_hash
```

## Restrições

- Não remova `senha_hash` do modelo de tabela `Usuario` (o banco precisa dele).
- O `senha_hash` (e a `senha`) **nunca** podem aparecer numa resposta HTTP.

## Conceitos que este exercício fixa

- Modelo de tabela ≠ modelo de resposta (DTO de saída).
- `response_model` **filtra** a saída (corta campos fora do DTO).
- Testar a **ausência** de algo, não só a presença — testes de segurança.
- Bugs que só aparecem quando você **roda o app**, não nos testes existentes.
