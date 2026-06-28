from typing import TypedDict


class Pedido(TypedDict):
    cliente: str
    valor: float
    pago: bool


pedidos: list[Pedido] = [
    {"cliente": "ana", "valor": 150.0, "pago": True},
    {"cliente": "bruno", "valor": 80.0, "pago": False},
    {"cliente": "carla", "valor": 200.0, "pago": True},
    {"cliente": "diego", "valor": 50.0, "pago": False},
]

for i, pedido in enumerate(pedidos):
    status = "pago" if pedido["pago"] else "pendente"
    print(f"{i + 1}.", f"{pedido['cliente']} - R$ {pedido['valor']:.2f} ({status})")

recebido: float = 0
for pedido in pedidos:
    if not pedido["pago"]:
        continue
    recebido += pedido["valor"]

print("recebido1:", recebido)


def recebido_def():
    return sum(item["valor"] for item in pedidos if item["pago"])


print("recebido2:", recebido_def())


def faixa(valor):
    match valor:
        case v if v >= 150:
            return "alto"
        case v if v >= 70:
            return "médio"
        case _:
            return "baixo"


print(faixa(70))

produtos = ["caneta", "caderno", "mochila"]
precos = [5.0, 25.0, 120.0]
for produto, preco in zip(produtos, precos, strict=True):
    print(f"{produto} custa R$ {preco:.2f}")
