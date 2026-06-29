# Exercício 24 — Validação de entrada (EmailStr, Field, field_validator)

## Contexto

Hoje `UsuarioCriar` tem `email: str` e `senha: str` — aceita `"banana"` como email e
`"1"` como senha. Vamos validar de verdade na **fronteira** (o FastAPI rejeita com 422
antes da rota rodar), usando as 3 camadas do Pydantic.

## Parte A — `EmailStr` no email

Em `api/database.py`:

```python
from pydantic import EmailStr   # novo import

class UsuarioCriar(SQLModel):
    email: EmailStr              # era: str
    senha: str
```

> `EmailStr` valida o formato (tem `@`, domínio…). Já está instalado (veio com o
> FastAPI). Não precisa de migration: no banco continua sendo texto — `EmailStr` é
> validação de **entrada**, não muda a coluna.

(Opcional: bota `EmailStr` também no `UsuarioBase.email`, pra o `PUT` validar igual.)

## Parte B — `Field` na senha (mínimo 8)

```python
from sqlmodel import Field   # já está importado no arquivo

class UsuarioCriar(SQLModel):
    email: EmailStr
    senha: str = Field(min_length=8)
```

> Use o `Field` do **sqlmodel** (já importado) — ele aceita as restrições do Pydantic
> (`min_length`, `max_length`, `gt`, `le`, `pattern`…).

## Parte C — ATENÇÃO: isso quebra testes antigos (de propósito)

Vários testes usam `"senha": "1234"` (4 chars). Com `min_length=8`, eles passam a
receber **422** em vez de 201. Isso **não é bug** — é a validação funcionando. Atualize
esses testes pra usar uma senha válida, ex.: `"senha-1234"` (em `test_auth.py` e onde
mais aparecer `"1234"` como senha).

> Lição: apertar uma regra quebra suposições antigas. Em projeto real, mudar validação
> = revisar quem dependia do comportamento frouxo.

## Parte D — Teste novo: email inválido → 422

Em `tests/test_auth.py`:

```python
def test_registro_email_invalido(client):
    r = client.post("/usuarios", json={"email": "banana", "senha": "senha-1234"})
    assert r.status_code == 422

def test_registro_senha_curta(client):
    r = client.post("/usuarios", json={"email": "ok@x.com", "senha": "123"})
    assert r.status_code == 422
```

## Parte E (bônus) — regra customizada com `@field_validator`

Se quiser ir além: exigir que a senha tenha pelo menos um número.

```python
from pydantic import field_validator

class UsuarioCriar(SQLModel):
    email: EmailStr
    senha: str = Field(min_length=8)

    @field_validator("senha")
    @classmethod
    def senha_tem_numero(cls, v: str) -> str:
        if not any(c.isdigit() for c in v):
            raise ValueError("a senha precisa ter pelo menos um número")
        return v
```

## Como testar

```bash
uv run poe test     # todos verdes (depois de ajustar as senhas curtas)
uv run poe dev      # POST /usuarios com email "banana" no /docs → 422
```

## Conceitos que este exercício fixa

- Tipos especializados (`EmailStr`) validam formato, não só "é texto".
- `Field(min_length=...)` e amigos = restrições declarativas (≈ `z.string().min()`).
- `@field_validator` = regra customizada (≈ `z.refine()`).
- Validação acontece na fronteira → 422 automático, antes da rota.
- Apertar validação pode quebrar testes que usavam dado frouxo (e tudo bem).
