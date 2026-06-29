# Exercício 22 — CI com GitHub Actions

## Contexto

O repo tem testes, lint e checagem de tipos, mas nada disso roda **automaticamente**.
Vamos adicionar CI: a cada push (e em todo PR), uma máquina limpa na nuvem roda as
mesmas checagens. É o `pre-commit`, mas no servidor e pra todo mundo.

## O que fazer

### `.github/workflows/ci.yml` (arquivo novo)

Crie a pasta `.github/workflows/` e o arquivo `ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  checks:
    runs-on: ubuntu-latest
    steps:
      - name: Baixar o código
        uses: actions/checkout@v4

      - name: Instalar o uv
        uses: astral-sh/setup-uv@v5

      - name: Instalar dependências
        run: uv sync --frozen

      - name: Lint (ruff)
        run: uv run poe lint

      - name: Formatação (ruff)
        run: uv run ruff format --check .

      - name: Tipos (mypy)
        run: uv run poe types

      - name: Testes + cobertura
        run: uv run poe cov
        env:
          SECRET_KEY: ci-secret-de-teste
```

## Pontos de atenção

- **Indentação YAML é por espaços** (nunca tab) — 2 espaços por nível. YAML é
  sensível a isso, igual Python.
- O `env: SECRET_KEY` fica **só** no passo dos testes (é o único que executa o
  `config.py`; lint e mypy são estáticos e não precisam).
- `uv sync --frozen` = instala exatamente o `uv.lock` (não atualiza nada), pro CI
  ser reprodutível.

## Como testar

```bash
# 1. valida que o YAML é válido localmente
uv run python -c "import yaml; yaml.safe_load(open('.github/workflows/ci.yml')); print('YAML ok')"

# 2. commita e dá push
git add .github/workflows/ci.yml
git commit -m "ci: roda lint, tipos e testes no GitHub Actions"
git push

# 3. abre o GitHub → aba "Actions" → vê o workflow rodando (verde = passou)
```

## Restrições

- Não suba segredo real no YAML — `ci-secret-de-teste` é fake de propósito (os
  testes usam banco em memória). Segredo real iria nos GitHub Secrets.
- O workflow só roda os comandos que você já tem (`poe lint/types/cov`).

## Conceitos que este exercício fixa

- CI = checagens automáticas numa máquina limpa a cada push/PR.
- `on` (gatilhos), `jobs`, `runs-on`, `steps` (`uses` = ação pronta, `run` = comando).
- Máquina do CI não tem `.env` → segredo vem do ambiente (≈ Aula 14, do lado do CI).
- CI ≈ pre-commit, mas no servidor e impossível de pular.
