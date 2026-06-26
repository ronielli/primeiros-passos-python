# aula01.py - meu primeiro Python


def saudar(nome):
    return f"Olá, {nome}! Bem-vindo ao Python."


# Em Python não há "main" obrigatório, o código roda de cima pra baixo
mensagem = saudar("Ronielli")
print(mensagem)

# Tipos básicos
idade = 30  # int
altura = 1.75  # float
ativo = True  # bool (maiúsculo!)
nada = None  # equivale a null

print(idade, altura, ativo, nada)


print(type(idade))  # vê o tipo de uma variável
