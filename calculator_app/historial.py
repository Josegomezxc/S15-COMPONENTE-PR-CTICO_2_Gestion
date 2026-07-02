import json
import os
from datetime import datetime

HISTORIAL_FILE = os.path.join(os.path.dirname(__file__), "historial.json")


def cargar_historial():
    try:
        with open(HISTORIAL_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_historial(historial):
    with open(HISTORIAL_FILE, "w", encoding="utf-8") as f:
        json.dump(historial, f, ensure_ascii=False, indent=2)


def agregar_operacion(a, b, operacion, resultado):
    historial = cargar_historial()
    historial.append({
        "fecha": datetime.now().isoformat(),
        "a": a,
        "b": b,
        "operacion": operacion,
        "resultado": resultado,
    })
    guardar_historial(historial)


def limpiar_historial():
    guardar_historial([])
