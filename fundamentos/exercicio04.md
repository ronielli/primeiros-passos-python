# Exercício 04 — Controle de fluxo

**Tema:** loops (`for`/`while`), `enumerate`, `zip`, `match`.

## Dados

```python
pedidos = [
    {"cliente": "ana",   "valor": 150.0, "pago": True},
    {"cliente": "bruno", "valor": 80.0,  "pago": False},
    {"cliente": "carla", "valor": 200.0, "pago": True},
    {"cliente": "diego", "valor": 50.0,  "pago": False},
]
```

## Enunciado

Resolva **usando loops** (foco em controle de fluxo, evite comprehension aqui):

1. **`enumerate`:** imprima uma lista numerada começando do **1**:
   ```
   1. ana - R$ 150.00 (pago)
   2. bruno - R$ 80.00 (pendente)
   ...
   ```
   Dica: `enumerate(pedidos, start=1)` começa em 1; use `if pedido["pago"]`
   para decidir entre "pago"/"pendente".

2. **Acumulador com `for`:** calcule e imprima o **total já recebido**
   (soma dos `valor` só dos pedidos com `pago == True`).

3. **`match` com guardas:** escreva `faixa(valor)` que retorna a categoria:
   ```python
   match valor:
       case v if v >= 150:
           return "alto"
       case v if v >= 70:
           return "médio"
       case _:
           return "baixo"
   ```
   Depois imprima a faixa de cada pedido.

4. **`zip` (desafio):** dadas duas listas paralelas —
   ```python
   produtos = ["caneta", "caderno", "mochila"]
   precos   = [5.0, 25.0, 120.0]
   ```
   use `zip` para imprimir `"caneta custa R$ 5.00"` para cada par.

## Conceitos praticados

- `for item in iteravel` (estilo for-of)
- `range(inicio, fim, passo)`
- `enumerate(xs, start=1)` → índice + valor
- `zip(a, b)` → iterar listas em paralelo
- `while`, `break`, `continue`
- `match`/`case` com guardas (`case v if ...`) e coringa (`case _`)
- Desempacotamento: `x, y = par`, `primeiro, *resto = lista`
