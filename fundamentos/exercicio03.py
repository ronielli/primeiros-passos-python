from typing import TypedDict


class Product(TypedDict):
    nome: str
    preco: float
    estoque: int


product_list: list[Product] = []


def criar_produto(nome: str, preco: float, estoque: int = 0):
    item: Product = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque,
    }
    product_list.append(item)
    return item


def aplicar_desconto(produto: Product, percentual: float) -> Product:
    novo_preco = produto["preco"] - produto["preco"] * percentual / 100

    novo_produto: Product = {**produto, "preco": novo_preco}

    return novo_produto


def resumo(*produtos: Product):
    return "\n".join(f"{p['nome']}: R$ {p['preco']:.2f}" for p in produtos)


criar_produto("Sabonete", 10)
criar_produto("Limão", 20)
criar_produto("Laranja", 30)
print("---------------print test------------")

print(resumo(product_list[0], product_list[1], product_list[2]))

print("---------------desconto------------")

descont = aplicar_desconto(product_list[0], 10)
product_list[0] = descont
print(resumo(product_list[0], product_list[1], product_list[2]))
