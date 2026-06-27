import time
from functools import wraps


def cronometro(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()
        print(f"Levou {fim - inicio:.4f}s")
        return resultado

    return wrapper


def repetir(vezes):  # 1) recebe o argumento
    def decorator(func):  # 2) recebe a função
        @wraps(func)
        def wrapper(*args, **kwargs):  # 3) o embrulho de sempre
            for _ in range(vezes):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repetir(3)
def cumprimentar(nome):
    print(f"Olá, {nome}!")


@cronometro
def soma_lenta(n):
    total = 0
    for i in range(n):
        total += i
    return total


if __name__ == "__main__":
    soma_lenta(19_855_000)
    cumprimentar("Ana")
    print(soma_lenta.__name__)
    print(cumprimentar.__name__)
