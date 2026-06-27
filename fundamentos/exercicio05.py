print("------1 raise com validação-----")


def sacar(saldo: float, valor: float):
    if valor <= 0:
        raise ValueError(f"valor deve ser positivo: {valor:.2f}")

    if valor > saldo:
        raise ValueError(f"saldo insuficiente: {saldo:.2f}")

    return saldo - valor


try:
    print(sacar(2, 3))
except ValueError as e:
    print(f"Erro: {e}")

try:
    print(sacar(2, 0))
except ValueError as e:
    print(f"Erro: {e}")

try:
    print(sacar(2, 1))
except ValueError as e:
    print(f"Erro: {e}")

print("------2 try/except-----")


def parse_idade(texto: str):
    try:
        idade = int(texto)
        return idade
    except ValueError:
        print("não é um numero valido")
        return -1
    except Exception as e:
        print(f"erro inesperado: {e}")
        return -1


print(parse_idade("1"))
print(parse_idade("2.1"))

print("------3 Vários except-----")


def dividir(texto: str):
    try:
        idade = int(texto)
        return 10 / idade
    except ValueError:
        print("não é um numero valido")
        return -0.0
    except ZeroDivisionError:
        print("não pode ser zero")
        return 0.0
    except Exception as e:
        print(f"erro inesperado: {e}")
        return 0.0


print(dividir("0"))
print(dividir("2"))

print("------4 EAFP com dict-----")

usuarios = [
    {"nome": "ana", "email": "ana@x.io"},
    {"nome": "carla", "email": "carla@x.io"},
    {"nome": "bruno"},
    {},
]

for item in usuarios:
    try:
        nome = item["nome"]
        email = item["email"]
        print(f"nome: {nome} - email:{email}")
    except KeyError:
        print(f"{item.get('nome', 'desconhecido')} não tem email")

    except Exception as e:
        print(f"erro inesperado: {e}")

print("------5 - finally (demonstração)")

try:
    sacar(2, 10)
except ValueError as e:
    print(f"Erro: {e}")
finally:
    print("--- operação finalizada ---")
