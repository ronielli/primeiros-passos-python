class ContaBancaria:
    def __init__(self, dono: str, saldo: float = 0.0):
        self.dono = dono
        self.saldo = saldo
        self.operacoes = []

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError(f"valor deve ser positivo: {valor:.2f}")
        self.saldo += valor
        self.operacoes.append(f"deposito: {valor:.2f}")

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError(f"valor deve ser positivo: {valor:.2f}")

        if valor > self.saldo:
            raise ValueError(f"saldo insuficiente: {self.saldo:.2f}")

        self.saldo -= valor
        self.operacoes.append(f"saque: {valor:.2f}")

    def __repr__(self):
        op = "\n".join(item for item in self.operacoes)
        return f"ContaBancaria(dono={self.dono!r}, saldo:{self.saldo:.2f})\n{op}"

    @property
    def saldo_formatado(self):
        return f"R$ {self.saldo:.2f}"


# Este bloco só roda quando você executa "python exercicio06.py" diretamente.
# Quando outro arquivo faz "from exercicio06 import ContaBancaria", ele NÃO roda.
if __name__ == "__main__":
    conta = ContaBancaria("Ana", 100)
    print(conta)

    try:
        conta.depositar(-10)
    except ValueError as e:
        print(f"Erro depositar: {e}")

    try:
        conta.sacar(-10)
    except ValueError as e:
        print(f"Erro sacar: {e}")

    try:
        conta.sacar(150)
    except ValueError as e:
        print(f"Erro sacar: {e}")

    conta.depositar(50)
    print(conta)

    conta.sacar(30)
    print(conta)
