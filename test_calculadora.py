"""Tests unitarios para calculadora.py (framework: pytest)."""

import pytest
from calculadora import suma, resta, multiplicar, dividir


def test_suma():
    assert suma(5, 3) == 8
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0


def test_resta():
    assert resta(10, 4) == 6
    assert resta(0, 5) == -5


def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(-2, 5) == -10
    assert multiplicar(0, 100) == 0


def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(7, 2) == 3.5


def test_dividir_por_cero():
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        dividir(5, 0)
