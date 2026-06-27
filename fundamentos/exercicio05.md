# Exercício 05 — Tratamento de erros

**Tema:** `try`/`except`/`else`/`finally`, `raise`, exceções específicas, EAFP.

## Enunciado

1. **`raise` com validação:** escreva
   `def sacar(saldo: float, valor: float) -> float:` que:
   - lança `ValueError("valor deve ser positivo")` se `valor <= 0`;
   - lança `ValueError("saldo insuficiente")` se `valor > saldo`;
   - senão, retorna o novo saldo (`saldo - valor`).

2. **`try`/`except` específico:** escreva
   `def parse_idade(texto: str) -> int:` que tenta converter `texto` para `int`.
   - Se conseguir, retorna o número.
   - Se der `ValueError` (ex: `"abc"`), retorna `-1` e imprime uma mensagem amigável.

3. **Vários `except`:** escreva
   `def dividir(a: float, b: float) -> float:` que retorna `a / b`, mas trata:
   - `ZeroDivisionError` → imprime "não dá pra dividir por zero" e retorna `0.0`.

4. **EAFP com dict:** dada a lista abaixo, percorra e imprima o email de cada
   usuário. Alguns **não têm** a chave `"email"` — trate isso com `try/except
   KeyError` (estilo EAFP), imprimindo `"<nome> não tem email"`.
   ```python
   usuarios = [
       {"nome": "ana", "email": "ana@x.io"},
       {"nome": "bruno"},
       {"nome": "carla", "email": "carla@x.io"},
   ]
   ```

5. **`finally` (demonstração):** chame `sacar()` dentro de um `try/except` que:
   - captura o `ValueError` e imprime a mensagem do erro;
   - tem um `finally` que sempre imprime `"--- operação finalizada ---"`.
   Teste tanto um saque válido quanto um inválido.

## Conceitos praticados

- `raise TipoDeErro("mensagem")`
- `except TipoEspecifico as e`
- Múltiplos `except` (do específico ao genérico)
- `else` e `finally` no try
- Filosofia EAFP (tentar e tratar, em vez de checar antes)
- Capturar a mensagem do erro com `as e` e usar `str(e)`
