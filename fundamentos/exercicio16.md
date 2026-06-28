# Exercício 16 — Configuração com pydantic-settings

## Contexto

Hoje a `SECRET_KEY` está hardcoded e **commitada** no git (`usuarios.py`), e a URL do
banco está fixa no código (`database.py`). Vamos centralizar tudo numa configuração
tipada que lê de variáveis de ambiente e de um arquivo `.env` (que fica fora do git).

## Dependência

```bash
uv add pydantic-settings
```

## O que fazer

### 1. `api/config.py` (arquivo novo)

Crie uma classe `Settings(BaseSettings)` com os campos:

- `secret_key: str` — **sem default** (obrigatório).
- `algorithm: str = "HS256"`
- `database_url: str = "sqlite:///tarefas.db"`
- `access_token_expire_minutes: int = 30`

Configure `model_config = SettingsConfigDict(env_file=".env")` e exporte uma
instância pronta: `settings = Settings()`.

### 2. `.env` (na raiz do projeto — NÃO commitar)

```
SECRET_KEY=troque-por-um-segredo-grande-e-aleatorio
DATABASE_URL=sqlite:///tarefas.db
```

> O `.gitignore` já ignora `.env`. Confirme com `git status` que ele NÃO aparece.

### 3. `.env.example` (este SIM vai pro git)

Mesmo conteúdo do `.env`, mas **sem segredos reais** — serve de modelo pra quem
clonar o projeto saber quais variáveis existem:

```
SECRET_KEY=
DATABASE_URL=sqlite:///tarefas.db
```

### 4. Trocar os valores hardcoded

- `usuarios.py`: remova `SECRET_KEY` e `ALGORITHM`; use `settings.secret_key` e
  `settings.algorithm`. Troque o `timedelta(minutes=30)` por
  `settings.access_token_expire_minutes`.
- `database.py`: troque `create_engine("sqlite:///tarefas.db")` por
  `create_engine(settings.database_url)`.

### 5. Não quebrar os testes

Os testes não devem depender do seu `.env` real. Pense: o `conftest.py` já cria o
próprio engine em memória, então o banco de teste já está isolado. Só garanta que
a `secret_key` exista quando os testes rodam (o `.env` na raiz resolve, pois o
pytest roda da raiz). Rode `uv run poe test` e confirme que continua tudo verde.

## Como testar

```bash
uv run poe dev        # a API deve subir lendo o .env
uv run poe test       # 18 testes devem continuar passando
```

Teste manual: apague a linha `SECRET_KEY` do `.env` e tente subir a API — ela deve
**falhar na inicialização** com erro de validação do Pydantic (campo obrigatório
faltando). Isso é o comportamento desejado: melhor falhar cedo e claro.

## Restrições

- O `.env` **nunca** vai pro git (segredos ficam fora do versionamento).
- A `secret_key` é obrigatória — a app não sobe sem ela.
- Nada de `os.environ[...]` na mão; use o objeto `settings`.

## Conceitos que este exercício fixa

- 12-factor config: configuração vem do ambiente, não do código.
- `BaseSettings` lê env vars + `.env` e **valida/converte os tipos**.
- Campo obrigatório (sem default) = falha cedo se faltar.
- `.env` (segredo, fora do git) vs `.env.example` (modelo, no git).
