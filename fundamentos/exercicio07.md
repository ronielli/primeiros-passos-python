# Exercício 07 — Herança e o resto de POO

**Tema:** herança (`class B(A)`), `super()`, override de método, `@property`.

> Continuação do exercício 06. Pode copiar a `ContaBancaria` para este arquivo
> (no próximo exercício a gente aprende `import` e para de copiar 😉).

## Enunciado

### 1. Classe base `ContaBancaria`
Reaproveite a do exercício 06 (`__init__` com `dono`/`saldo`, `depositar`,
`sacar` com validações, `__repr__`).

### 2. Subclasse `ContaPoupanca(ContaBancaria)`
- **`__init__`:** recebe `dono`, `saldo` e `taxa_juros: float` (ex: `0.05` = 5%).
  Use `super().__init__(dono, saldo)` para reaproveitar o construtor do pai e
  depois guarde `self.taxa_juros`.
- **`render_juros(self)`:** aumenta o saldo aplicando a taxa
  (`self.saldo += self.saldo * self.taxa_juros`).

### 3. Subclasse `ContaCorrente(ContaBancaria)`
- **`__init__`:** recebe `dono`, `saldo` e `limite: float = 0.0` (cheque especial).
- **Override de `sacar`:** a corrente pode sacar até `saldo + limite`.
  Reescreva o `sacar` para permitir isso (lance `ValueError("limite excedido")`
  se passar de `saldo + limite`).

### 4. `@property`
Adicione na `ContaBancaria` uma property `saldo_formatado` que retorna
`"R$ 1.234,56"` (ou ao menos `"R$ 1234.56"`). Acesse **sem parênteses**:
`print(conta.saldo_formatado)`.

### 5. Teste no final
- Crie uma `ContaPoupanca("ana", 1000, 0.05)`, renda juros e imprima.
- Crie uma `ContaCorrente("bruno", 100, limite=50)`, saque 130 (deve funcionar,
  usando o limite) e tente sacar mais que `saldo + limite` (deve dar erro).
- Mostre o `saldo_formatado` de alguma conta.

## Conceitos praticados

- `class Subclasse(ClassePai):`
- `super().__init__(...)` e `super().metodo(...)`
- Override (redefinir um método herdado)
- `@property` (método acessado como atributo)
- Reuso: a subclasse herda tudo do pai e só muda/adiciona o necessário

## Dica

Override que **reaproveita** o pai costuma chamar `super()`:
```python
def sacar(self, valor):
    # ... regra própria ...
    # ou reusa: super().sacar(valor)
```
