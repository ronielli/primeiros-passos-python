class ContaBancaria:
    def __init__(self, dono: str, saldo: float = 0.0):
        self.dono = dono
        self.saldo = saldo
        self.operacoes = []

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError(
                f"💸 Valor inválido para depósito: R$ {valor:.2f} (deve ser positivo)"
            )
        self.saldo += valor
        self.operacoes.append(f"✅ Depósito:  R$ {valor:.2f}")

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError(
                f"💸 Valor inválido para saque: R$ {valor:.2f} (deve ser positivo)"
            )

        if valor > self.saldo:
            raise ValueError(f"🚫 Saldo insuficiente — disponível: R$ {self.saldo:.2f}")

        self.saldo -= valor
        self.operacoes.append(f"🔴 Saque:     R$ {valor:.2f}")

    def __repr__(self):
        linha = "─" * 36
        op = "\n".join(f"  {item}" for item in self.operacoes) or "  (sem operações)"
        return (
            f"\n🏦 Conta de {self.dono}\n"
            f"{linha}\n"
            f"{op}\n"
            f"{linha}\n"
            f"  💰 Saldo atual: {self.saldo_formatado}\n"
        )

    @property
    def saldo_formatado(self):
        return f"R$ {self.saldo:.2f}"
