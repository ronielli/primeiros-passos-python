produtos = [
    {"nome": "batata", "preco": 10.00, "quantidade": 10},
    {"nome": "arroz", "preco": 20.00, "quantidade": 20},
    {"nome": "feijão", "preco": 30.00, "quantidade": 0},
]


def total_em_estoque2(items):
    return sum(item["preco"] * item["quantidade"] for item in items)


def total_em_estoque(items):
    total = 0
    for item in items:
        total += item["quantidade"] * item["preco"]
    return total


def produtos_disponiveis(items):
    items_disponiveis = []

    for item in items:
        if item["quantidade"] > 0:
            items_disponiveis.append(item)

    return items_disponiveis


def produtos_disponiveis2(items):
    return [item for item in items if item["quantidade"] > 0]


em_estoque = total_em_estoque(produtos)
print(em_estoque)

em_estoque2 = total_em_estoque2(produtos)
print(em_estoque2)

disponiveis = produtos_disponiveis(produtos)
print(disponiveis)

disponiveis2 = produtos_disponiveis2(produtos)
print(disponiveis2)
