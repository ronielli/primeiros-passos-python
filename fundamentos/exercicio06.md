# Exercício 06 — Classes / POO

**Tema:** `class`, `__init__`, `self`, métodos, `__repr__`, `raise` dentro de método.

## Enunciado

Crie uma classe `ContaBancaria`:

1. **`__init__`:** recebe `dono: str` e `saldo: float = 0.0`. Guarda os dois em
   `self.dono` e `self.saldo`.

2. **`depositar(self, valor: float)`:**
   - se `valor <= 0`, lança `ValueError("valor inválido")`;
   - senão, soma ao saldo.

3. **`sacar(self, valor: float)`:**
   - se `valor <= 0`, lança `ValueError("valor inválido")`;
   - se `valor > self.saldo`, lança `ValueError("saldo insuficiente")`;
   - senão, subtrai do saldo.

4. **`__repr__(self)`:** retorna algo como
   `ContaBancaria(dono='ana', saldo=150.0)`.

5. **Teste no final:**
   - crie uma conta `ContaBancaria("ana", 100)`;
   - deposite 50, saque 30;
   - imprima a conta (deve usar o `__repr__`);
   - tente sacar um valor maior que o saldo dentro de um `try/except` e imprima
     o erro.

## Conceitos praticados

- `class Nome:` e instanciação **sem `new`** (`ContaBancaria("ana", 100)`)
- `__init__(self, ...)` como construtor
- `self` como referência ao objeto (o `this`)
- Métodos que recebem `self` e mexem em `self.atributo`
- `raise ValueError(...)` dentro de método (regras de negócio)
- `__repr__` para uma representação legível no `print`

## Bônus (se sobrar energia)

- Adicione um método `historico` guardando cada operação numa lista
  `self.operacoes` (criada no `__init__`).
