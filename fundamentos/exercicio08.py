import banco.conta
from banco import ContaCorrente, ContaPoupanca

conta_bancaria = banco.conta.ContaBancaria("Ana", 10)
conta_bancaria.depositar(5)

conta_poupanca = ContaPoupanca("João", 15, 0.5)
conta_poupanca.depositar(5)
conta_poupanca.render_juros()

conta_corrente = ContaCorrente("Maria", 20, 10)
conta_corrente.depositar(5)
conta_corrente.sacar(25)

print(conta_bancaria)
print(conta_poupanca)
print(conta_corrente)
