# Informe de Feedback y Mejora Continua

## ¿Qué error se produjo?
Se modificó la función `suma` en `calculator.py` cambiando el operador de `+` a `-`, haciendo que `suma(5, 3)` retornara `2` en lugar de `8`.

## ¿Cómo fue detectado?
Ejecutando las suites de tests localmente con `python -m unittest discover` y `pytest -v`, replicando los mismos pasos que ejecuta el pipeline de CI/CD definido en `.github/workflows/build.yml`.

## ¿Qué información proporcionó el pipeline?

**unittest** (`AssertionError: 2 != 8`):
```
FAIL: test_suma (test_calculator.TestCalculadora.test_suma)
  File "test_calculator.py", line 7, in test_suma
    self.assertEqual(suma(5, 3), 8)
AssertionError: 2 != 8
```

**pytest** (`assert 2 == 8`):
```
FAILED test_calculadora.py::test_suma - assert 2 == 8
  test_calculadora.py:12: AssertionError
```

Ambos frameworks indicaron:
- Archivo y línea exacta del fallo.
- Valor esperado (`8`) vs. valor obtenido (`2`).
- Traza completa de la llamada.

## ¿Cómo se solucionó?
Revirtiendo la línea 10 de `calculator.py` de `return a - b` a `return a + b`, restaurando la lógica correcta de la función `suma`. Se verificó la corrección ejecutando nuevamente ambos conjuntos de tests, obteniendo **9/9 pruebas pasadas** (4 unittest + 5 pytest).
