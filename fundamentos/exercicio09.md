# Exercício 09 — Decorators (`@`)

**Tema:** funções como objetos, higher-order functions, escrever o próprio
decorator, `*args/**kwargs` no wrapper, `functools.wraps`.

> Você já *usou* `@property` e `@staticmethod`. Agora vai *escrever* os seus —
> é o mesmo conceito de wrapper/middleware que você já conhece do JS/Express.

## Crie um arquivo `exercicio09.py` com:

### 1. Decorator `cronometro`
Mede quanto tempo uma função leva pra rodar.

- Use `time.perf_counter()` antes e depois de chamar a função.
- Imprima algo como `⏱️  soma_lenta levou 0.0123s`.
- **Importante:** o wrapper deve aceitar `*args, **kwargs` e repassar pra função
  original, e **retornar** o resultado dela.
- Use `@functools.wraps(func)` no wrapper (pra preservar nome/docstring).

```python
@cronometro
def soma_lenta(n):
    total = 0
    for i in range(n):
        total += i
    return total
```

### 2. Decorator `repetir(vezes)` — decorator COM argumento
Esse é o nível "boss": um decorator que **recebe um parâmetro**. Ele executa a
função decorada `vezes` vezes seguidas.

> Dica: decorator com argumento tem **3 camadas** de função:
> ```python
> def repetir(vezes):          # 1) recebe o argumento
>     def decorator(func):     # 2) recebe a função
>         def wrapper(*args, **kwargs):   # 3) o embrulho de sempre
>             ...
>         return wrapper
>     return decorator
> ```

Uso esperado:
```python
@repetir(3)
def cumprimentar(nome):
    print(f"Olá, {nome}!")

cumprimentar("Ana")   # imprime 3 vezes
```

### 3. Teste no final (protegido por `if __name__ == "__main__":`)
- Chame `soma_lenta(1_000_000)` e veja o tempo aparecer.
- Chame `cumprimentar("Ana")` e veja repetir 3x.
- **Prova do `@wraps`:** imprima `print(soma_lenta.__name__)` — deve mostrar
  `soma_lenta` (e NÃO `wrapper`). Se mostrar `wrapper`, faltou o `@wraps`.

## Conceitos praticados

- Função é objeto (passar/retornar função).
- `@decorator` = açúcar para `func = decorator(func)`.
- `*args, **kwargs` no wrapper para aceitar qualquer assinatura.
- `functools.wraps` para preservar a identidade da função original.
- Decorator **com argumento** (as 3 camadas).

## Por que isso importa pro próximo passo 🎯

Na primeira API com **FastAPI**, as rotas são decorators:
```python
@app.get("/usuarios")
def listar_usuarios():
    ...
```
Entender o `@` agora faz a API fazer sentido depois.
