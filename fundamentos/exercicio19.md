# Exercício 19 — Zerar o mypy (limpeza de tipos)

## Contexto

`uv run poe types` (mypy) acusa 5 erros em exercícios antigos + 1 falso-positivo na
API. Vamos zerar — não por perfeccionismo, mas porque cada erro ensina um conceito de
type hint. Meta: `Success: no issues found`.

## Os 5 erros (rode `uv run poe types` pra ver)

### Categoria 1 — Container vazio precisa de anotação (`var-annotated`)

`mypy` não adivinha o tipo de um `[]` vazio. Anote o tipo do elemento:

- `fundamentos/exercicio03.py:1` → `product_list` guarda dicts:
  `product_list: list[dict] = []`
- `fundamentos/exercicio06.py:5` → `self.operacoes` guarda strings:
  `self.operacoes: list[str] = []`
- `fundamentos/banco/conta.py:5` → idem: `self.operacoes: list[str] = []`

### Categoria 2 — Dict heterogêneo → `TypedDict` (`operator`)

`fundamentos/exercicio04.py:16`. Como `pedidos` mistura tipos de valor, o mypy infere
`dict[str, object]`, e `object` não soma. Crie um `TypedDict` (≈ interface do TS):

```python
from typing import TypedDict

class Pedido(TypedDict):
    cliente: str
    valor: float
    pago: bool

pedidos: list[Pedido] = [ ... ]   # mantém os mesmos dados
recebido = 0.0                     # float (era int)
```

### Categoria 3 — Falso-positivo do SQLModel (`arg-type`)

`fundamentos/api/routers/tarefas.py:28`. Troque o `# pyright: ignore[reportArgumentType]`
por `# type: ignore[arg-type]` (esse os dois checkers respeitam). Mantenha o comentário
explicativo acima.

## Como testar

```bash
uv run poe types     # deve dar: Success: no issues found
uv run poe test      # 18 testes continuam verdes
uv run poe lint      # ruff continua limpo
```

## Restrições

- Não mude o comportamento dos exercícios — só adicione/ajuste os tipos.
- O `# type: ignore` deve ser **estreito** (com o código `[arg-type]`), não um
  `# type: ignore` "pelado" que esconde tudo.

## Conceitos que este exercício fixa

- Container vazio (`[]`, `{}`) precisa de anotação; cheio o mypy infere.
- `dict[str, object]` quando os valores são heterogêneos → `object` trava operações.
- `TypedDict` = descrever o formato de um dict (≈ `interface` do TS).
- `# type: ignore[código]` vale pra mypy E pyright; use estreito e comentado.
