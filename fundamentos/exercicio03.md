# Exercício 03 — Funções, type hints e spread

**Tema:** funções com type hints, valores padrão, `*args` e spread (`*`/`**`).

## Enunciado

Crie uma "mini-biblioteca" de produtos com type hints em tudo:

1. `def criar_produto(nome: str, preco: float, estoque: int = 0) -> dict:`
   retorna o dict do produto. (`estoque` tem default 0.)

2. `def aplicar_desconto(produto: dict, percentual: float) -> dict:`
   retorna um **novo** dict com o `preco` reduzido em `percentual`%.
   Ex: preço 100 com 10% → 90. **Não modifique o original** — crie um novo
   com spread: `{**produto, "preco": novo_preco}`.

3. `def resumo(*produtos: dict) -> str:` recebe **vários produtos** via `*args`
   e retorna uma string de resumo.
   Dica de formatação: `f"R$ {valor:.2f}"` (2 casas decimais).

4. No final, crie 2-3 produtos, aplique um desconto em um deles e imprima o
   `resumo(...)`.

## Conceitos praticados

- Type hints: `nome: str`, `-> dict`
- Argumento com valor padrão: `estoque: int = 0`
- `*args`: `def resumo(*produtos)`
- Spread na definição (`*args`) e na chamada (`resumo(*lista)`)
- Spread de dict: `{**produto, "preco": novo}` (cópia imutável)
- f-string formatada: `f"{x:.2f}"`
- `"\n".join(...)` para juntar strings

## Boas práticas reforçadas

- `snake_case` em vez de `camelCase`
- Aspas simples dentro de f-string: `f"{p['nome']}"`
- Evitar efeito colateral escondido (função que cria **e** guarda numa global)
