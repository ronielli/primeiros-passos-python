from .conta import ContaBancaria


class ContaPoupanca(ContaBancaria):
    def __init__(self, dono: str, saldo: float, juros: float):
        super().__init__(dono, saldo)
        self.taxa_juros = juros

    def render_juros(self):
        self.saldo += self.saldo * self.taxa_juros


class ContaCorrente(ContaBancaria):
    def __init__(self, dono: str, saldo: float, limite: float = 0.0):
        super().__init__(dono, saldo)
        self.limite = limite

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError(
                f"💸 Valor inválido para saque: R$ {valor:.2f} (deve ser positivo)"
            )
        saldo_total = self.saldo + self.limite
        if valor > saldo_total:
            raise ValueError(f"🚫 Limite excedido — disponível: R$ {saldo_total:.2f}")
        self.saldo -= valor
        self.operacoes.append(f"🔴 Saque:     R$ {valor:.2f}")
