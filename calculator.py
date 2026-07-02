"""Módulo con operaciones matemáticas básicas.

Proporciona funciones para suma, resta, multiplicación y división
de números reales.
"""


def suma(a, b):
    """Retorna la suma de a y b."""
    return a + b


def resta(a, b):
    """Retorna la resta de a menos b."""
    return a - b


def multiplicar(a, b):
    """Retorna el producto de a por b."""
    return a * b


def dividir(a, b):
    """Retorna la división de a entre b.

    Lanza ValueError si b es cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


if __name__ == "__main__":
    print(suma(5, 3))
