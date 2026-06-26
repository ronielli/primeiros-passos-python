# Exercício 02 — Comprehensions

**Tema:** list comprehension e dict comprehension (o `map`/`filter` do Python).

## Dados

```python
usuarios = [
    {"nome": "ana",   "idade": 28, "ativo": True},
    {"nome": "bruno", "idade": 17, "ativo": True},
    {"nome": "carla", "idade": 35, "ativo": False},
    {"nome": "diego", "idade": 22, "ativo": True},
]
```

## Enunciado

Resolva **cada item com UMA list/dict comprehension** (sem `for` solto):

1. `nomes` → lista só com os nomes.
2. `maiores` → lista dos usuários com `idade >= 18`.
3. `nomes_maiusculos` → lista dos nomes em MAIÚSCULO (`.upper()`).
4. `ativos_maiores` → nomes dos que são **ativos E maiores de idade** (`and`).
5. **Desafio (dict comprehension):** `idade_por_nome` →
   `{"ana": 28, "bruno": 17, ...}`.

## Conceitos praticados

- Sintaxe: `[EXPRESSÃO for ITEM in ITERÁVEL if CONDIÇÃO]`
- `map` → `[f(x) for x in xs]`
- `filter` → `[x for x in xs if cond]`
- Dict comprehension → `{chave: valor for ...}`
- Diferença entre **lista de registros** (`[{...}, {...}]`) e
  **dict indexado** (`{chave: valor}`)
