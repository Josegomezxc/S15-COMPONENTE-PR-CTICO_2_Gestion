"""Tests para el módulo de historial."""

import json
import os
import unittest
from datetime import datetime
from calculator_app.historial import (
    cargar_historial,
    guardar_historial,
    agregar_operacion,
    limpiar_historial,
    HISTORIAL_FILE,
)


class TestHistorial(unittest.TestCase):

    def setUp(self):
        if os.path.exists(HISTORIAL_FILE):
            os.remove(HISTORIAL_FILE)

    def tearDown(self):
        if os.path.exists(HISTORIAL_FILE):
            os.remove(HISTORIAL_FILE)

    def test_cargar_historial_vacio(self):
        data = cargar_historial()
        self.assertEqual(data, [])

    def test_guardar_y_cargar(self):
        entrada = [{"a": 1, "b": 2, "operacion": "suma", "resultado": 3}]
        guardar_historial(entrada)
        data = cargar_historial()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["resultado"], 3)

    def test_agregar_operacion(self):
        agregar_operacion(5, 3, "suma", 8)
        data = cargar_historial()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["a"], 5)
        self.assertEqual(data[0]["b"], 3)
        self.assertIn("fecha", data[0])

    def test_limpiar_historial(self):
        agregar_operacion(1, 2, "suma", 3)
        limpiar_historial()
        data = cargar_historial()
        self.assertEqual(data, [])


if __name__ == "__main__":
    unittest.main()
