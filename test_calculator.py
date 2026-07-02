"""Tests unitarios para calculator.py (framework: unittest)."""

import unittest
from calculator import suma, resta, multiplicar, dividir


class TestOperaciones(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(5, 3), 8)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(0, 0), 0)

    def test_resta(self):
        self.assertEqual(resta(10, 4), 6)
        self.assertEqual(resta(0, 5), -5)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(-2, 5), -10)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(7, 2), 3.5)
        with self.assertRaises(ValueError):
            dividir(5, 0)


if __name__ == "__main__":
    unittest.main()
