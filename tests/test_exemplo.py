# tests/test_exemplo.py — exemplo de teste com pytest (nosso "jest")
# Rode com:  uv run pytest

import pytest


def soma(a: int, b: int) -> int:
    return a + b


# No pytest, um teste é só uma função que começa com "test_"
# e usa o "assert" do próprio Python (não precisa de expect().toBe()).
def test_soma_simples():
    assert soma(2, 3) == 5


def test_soma_negativos():
    assert soma(-1, -1) == -2


# Dá pra rodar o mesmo teste com vários dados (parametrize = test.each do Jest)
@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (1, 1, 2),
        (0, 0, 0),
        (10, 5, 15),
    ],
)
def test_soma_varios_casos(a: int, b: int, esperado: int):
    assert soma(a, b) == esperado
