usuarios = [
    {"nome": "Ana", "idade": 28, "ativo": True},
    {"nome": "Bruno", "idade": 17, "ativo": True},
    {"nome": "Carla", "idade": 35, "ativo": False},
    {"nome": "Diego", "idade": 22, "ativo": True},
]


def nomes(items):
    return [item["nome"] for item in items]


def maiores(items):
    return [item["nome"] for item in items if item["idade"] >= 18]


def nomes_maiusculos(items):
    return [item["nome"].upper() for item in items]


def ativos_maiores(items):
    return [item["nome"] for item in items if item["idade"] > 18 and item["ativo"]]


def comprehension(items):
    return [{"name": item["nome"], "idade": item["idade"]} for item in items]


def comprehension2(items):
    return {
        item["nome"]: item["idade"]
        for item in items
        if item["idade"] > 18 and item["ativo"]
    }


print(nomes(usuarios))
print(maiores(usuarios))
print(nomes_maiusculos(usuarios))
print(ativos_maiores(usuarios))
print(comprehension(usuarios))
print(comprehension2(usuarios))
