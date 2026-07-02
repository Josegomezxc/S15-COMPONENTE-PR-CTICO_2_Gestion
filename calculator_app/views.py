import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from calculator import suma, resta, multiplicar, dividir
from .historial import agregar_operacion, cargar_historial, limpiar_historial
from .exportar import generar_csv


OPERACIONES = {
    "suma": suma,
    "resta": resta,
    "multiplicar": multiplicar,
    "dividir": dividir,
}


def index(request):
    return render(request, "calculator_app/index.html")


@csrf_exempt
def calculate(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)

    try:
        data = json.loads(request.body)
        a = float(data["a"])
        b = float(data["b"])
        op = data["op"]
    except (KeyError, ValueError, TypeError):
        return JsonResponse({"error": "Datos inválidos"}, status=400)

    func = OPERACIONES.get(op)
    if not func:
        return JsonResponse({"error": f"Operación '{op}' no válida"}, status=400)

    try:
        resultado = func(a, b)
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)

    agregar_operacion(a, b, op, resultado)
    return JsonResponse({"resultado": resultado})


def historial(request):
    if request.method == "POST":
        limpiar_historial()
        return JsonResponse({"mensaje": "Historial limpiado"})
    data = cargar_historial()
    return JsonResponse(data, safe=False)


def exportar_csv(request):
    csv_content = generar_csv()
    response = HttpResponse(csv_content, content_type="text/csv; charset=utf-8")
    response["Content-Disposition"] = 'attachment; filename="historial_calculadora.csv"'
    return response
