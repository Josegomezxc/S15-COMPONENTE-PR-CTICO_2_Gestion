"""Tests para el módulo de exportación CSV."""

import os
import unittest
from calculator_app.historial import (
    guardar_historial,
    limpiar_historial,
    HISTORIAL_FILE,
)
from calculator_app.exportar import generar_csv


class TestExportarCSV(unittest.TestCase):

    def setUp(self):
        if os.path.exists(HISTORIAL_FILE):
            os.remove(HISTORIAL_FILE)

    def tearDown(self):
        if os.path.exists(HISTORIAL_FILE):
            os.remove(HISTORIAL_FILE)

    def test_generar_csv_vacio(self):
        contenido = generar_csv()
        lineas = contenido.strip().split("\n")
        self.assertEqual(len(lineas), 1)
        self.assertIn("Fecha", lineas[0])

    def test_generar_csv_con_datos(self):
        guardar_historial([
            {"fecha": "2026-01-01T12:00:00", "a": 5, "b": 3, "operacion": "suma", "resultado": 8},
            {"fecha": "2026-01-01T12:01:00", "a": 10, "b": 2, "operacion": "dividir", "resultado": 5},
        ])
        contenido = generar_csv()
        lineas = contenido.strip().split("\n")
        self.assertEqual(len(lineas), 3)
        self.assertIn("5", lineas[1])
        self.assertIn("dividir", lineas[2])

    def test_exportar_sin_historial(self):
        limpiar_historial()
        contenido = generar_csv()
        self.assertIn("Fecha", contenido)


if __name__ == "__main__":
    unittest.main()
