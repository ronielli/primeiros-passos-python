# Exercício 08 — Módulos e Pacotes (organização de projeto)

**Tema:** módulo vs pacote, `__init__.py`, import absoluto vs relativo,
`if __name__ == "__main__":`.

> Finalmente paramos de copiar a `ContaBancaria`! 🎉 Aqui você vai **organizar o
> código em pastas** e importar de um lugar pro outro, como num projeto de verdade.

## Objetivo

Transformar o código de contas (dos exercícios 06/07) num **pacote** organizado e
usá-lo a partir de um arquivo principal.

## Estrutura a criar

Dentro de `fundamentos/`, crie esta árvore:

```
banco/                  ← o pacote
├── __init__.py         ← "index" do pacote
├── conta.py            ← módulo com ContaBancaria
└── tipos.py            ← módulo com ContaPoupanca e ContaCorrente
exercicio08.py          ← arquivo principal que usa o pacote
```

## Passos

### 1. `banco/conta.py`
- Coloque aqui a classe **`ContaBancaria`** (pode reaproveitar a do exercício 07,
  com `depositar`, `sacar`, `__repr__` e a property `saldo_formatado`).

### 2. `banco/tipos.py`
- Coloque aqui **`ContaPoupanca`** e **`ContaCorrente`**.
- Elas herdam de `ContaBancaria` — então importe a base **com import relativo**:
  ```python
  from .conta import ContaBancaria
  ```

### 3. `banco/__init__.py`
- Centralize os exports do pacote, pra quem usa importar tudo de `banco`:
  ```python
  from .conta import ContaBancaria
  from .tipos import ContaPoupanca, ContaCorrente
  ```

### 4. `exercicio08.py` (o principal)
- Importe **direto do pacote** (graças ao `__init__.py`):
  ```python
  from banco import ContaBancaria, ContaPoupanca, ContaCorrente
  ```
- Dentro de um `main()`:
  - crie uma `ContaPoupanca`, renda juros, imprima o `saldo_formatado`;
  - crie uma `ContaCorrente`, faça um saque usando o limite.
- Proteja a execução com:
  ```python
  if __name__ == "__main__":
      main()
  ```

## Como rodar

Rode a partir da **raiz do projeto** (pra o Python achar o pacote `banco`):

```bash
uv run python fundamentos/exercicio08.py
```

## Conceitos praticados

- Pasta vira **pacote** com `__init__.py`.
- **Import relativo** (`from .conta import ...`) dentro do pacote.
- **Import absoluto/agregado** (`from banco import ...`) a partir de fora.
- `__init__.py` como ponto central de exports (o "index" do pacote).
- `if __name__ == "__main__":` separando "código que roda" de "código importável".

## Desafio opcional

No `exercicio08.py`, troque o import agregado por um **import de submódulo**:
```python
from banco.tipos import ContaPoupanca
import banco.conta
```
e veja a diferença de como você acessa as coisas (`banco.conta.ContaBancaria`).
