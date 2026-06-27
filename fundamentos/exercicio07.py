from exercicio06 import ContaBancaria


class ContaPoupanca(ContaBancaria):
    def __init__(self, dono: str, saldo: float, juros: float):
        super().__init__(dono, saldo)
        self.taxa_juros = juros

    def render_juros(self):
        self.saldo += self.saldo * self.taxa_juros

    @staticmethod
    def validar_valor(v):  # função "solta" dentro da classe (sem self)
        return v > 0


print(ContaPoupanca.validar_valor(10))
print(ContaPoupanca.validar_valor(-1))
conta = ContaPoupanca("ana", 1000, 0.05)
print(conta)
conta.render_juros()
print(conta)

try:
    conta.sacar(108)
except ValueError as e:
    print(f"Erro sacar: {e}")


class ContaCorrente(ContaBancaria):
    def __init__(self, dono: str, saldo: float, limite: float = 0.0):
        super().__init__(dono, saldo)
        self.limite = limite

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError(f"valor deve ser positivo: {valor:.2f}")
        saldo_total = self.saldo + self.limite
        if valor > saldo_total:
            raise ValueError(f"limite excedido: {saldo_total:.2f}")

        self.saldo -= valor
        self.operacoes.append(f"saque: {valor:.2f}")


conta_corrente = ContaCorrente("Bruno", 100, 50)

print(f"conta_corrente: {conta_corrente}")
try:
    conta_corrente.sacar(151)
except ValueError as e:
    print(f"Erro sacar: {e}")

print(f"saldo: {conta_corrente.saldo_formatado}")
