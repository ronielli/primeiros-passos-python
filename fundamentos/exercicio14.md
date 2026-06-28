# Exercício 14 — Autenticação com JWT

## Contexto

A API está aberta — qualquer um pode criar e deletar dados. Vamos adicionar
autenticação com JWT para proteger as rotas.

## Dependências

```bash
uv add "passlib[bcrypt]" "python-jose[cryptography]"
```

## O que fazer

### 1. `api/database.py`

Adicione o modelo `Usuario`:
- `id: int | None` — chave primária
- `email: str` — único
- `senha_hash: str`

### 2. `api/auth.py` (arquivo novo)

Crie um módulo com:
- `SECRET_KEY` e `ALGORITHM = "HS256"` como constantes
- `pwd_context = CryptContext(schemes=["bcrypt"])`
- `oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")`
- Função `hash_senha(senha: str) -> str`
- Função `verificar_senha(senha: str, hash: str) -> bool`
- Função `criar_token(dados: dict) -> str` — adiciona expiração de 30 min e assina
- Função `get_current_user(token, session) -> Usuario` — decodifica o token,
  busca o usuário no banco, lança 401 se inválido

### 3. `api/routers/auth.py` (arquivo novo)

CRUD mínimo de autenticação:
- `POST /auth/registro` — recebe `email` + `senha`, salva com senha hasheada (201)
- `POST /auth/login` — valida credenciais, devolve `{"access_token": ..., "token_type": "bearer"}`
- `GET /auth/me` — rota protegida, retorna o usuário logado

### 4. `api/main.py`

Registre o novo router.

### 5. Proteja uma rota

No `POST /tarefas`, adicione `current_user: Usuario = Depends(get_current_user)`
para exigir autenticação.

## Como testar

```bash
uv run fastapi dev fundamentos/api/main.py
```

1. `POST /auth/registro` com email e senha
2. `POST /auth/login` — copie o `access_token`
3. No Swagger, clique em "Authorize" e cole o token
4. `GET /auth/me` — deve retornar seus dados
5. `POST /tarefas` sem token → 401; com token → 201

## Restrições

- Nunca salve a senha em texto puro — sempre use `hash_senha()`
- A `SECRET_KEY` em produção viria de variável de ambiente, não hardcoded
