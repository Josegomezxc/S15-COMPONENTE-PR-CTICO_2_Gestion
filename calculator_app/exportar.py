import csv
import io
from .historial import cargar_historial


def generar_csv():
    historial = cargar_historial()
    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow(["Fecha", "Operando A", "Operacion", "Operando B", "Resultado"])

    op_nombres = {"suma": "+", "resta": "-", "multiplicar": "*", "dividir": "/"}

    for item in historial:
        writer.writerow([
            item.get("fecha", ""),
            item.get("a", ""),
            op_nombres.get(item.get("operacion", ""), item.get("operacion", "")),
            item.get("b", ""),
            item.get("resultado", ""),
        ])

    return output.getvalue()
