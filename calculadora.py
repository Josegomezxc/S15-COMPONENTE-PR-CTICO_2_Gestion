"""Módulo de re-exportación de operaciones matemáticas.

Expone las funciones suma, resta, multiplicar y dividir
como parte de la interfaz pública de la calculadora.
"""

from calculator import suma, resta, multiplicar, dividir

__all__ = ["suma", "resta", "multiplicar", "dividir"]
