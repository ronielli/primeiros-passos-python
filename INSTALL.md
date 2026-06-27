# Configuração do ambiente (Linux)

## 1. Instalar o `uv`

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Feche e reabra o terminal para o `uv` entrar no PATH.

## 2. Clonar o repositório (se ainda não tiver)

```bash
git clone <url-do-repo>
cd primeiros-passos-python
```

## 3. Criar o ambiente virtual e instalar dependências

```bash
uv sync
```

Isso cria a pasta `.venv/` e instala tudo do `pyproject.toml` (ruff, mypy, pytest, pre-commit).

## 4. Ativar o ambiente virtual

```bash
source .venv/bin/activate
```

## 5. Instalar os hooks do pre-commit

```bash
pre-commit install
```

## 6. Extensão do Ruff no Cursor

Instale a extensão **Ruff** (`charliermarsh.ruff`) pelo painel de extensões do Cursor (`Ctrl+Shift+X`).

---

Após esses passos o projeto está pronto: autocomplete, formatação ao salvar e checagem de tipos funcionando.
