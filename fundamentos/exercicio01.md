# Exercício 01 — Listas e dicionários

**Tema:** tipos básicos, listas de dicionários, funções, loops.

## Enunciado

1. Crie uma lista de dicionários representando **3 produtos**, cada um com
   `nome`, `preco` e `estoque`.
2. Escreva uma função `total_em_estoque(produtos)` que retorna a **soma de
   `preco * estoque`** de todos os produtos.
3. Escreva uma função `produtos_disponiveis(produtos)` que retorna só os
   produtos com `estoque > 0`.
4. Imprima os dois resultados com `print()`.

## Conceitos praticados

- Lista de dicionários (`list` + `dict`)
- Função com `for` e acumulador
- Filtro com `if` dentro do loop
- `append()` em lista

## Versão "modo Python" (depois de fazer com `for`)

```python
def total_em_estoque(items):
    return sum(item["preco"] * item["estoque"] for item in items)

def produtos_disponiveis(items):
    return [item for item in items if item["estoque"] > 0]
```
