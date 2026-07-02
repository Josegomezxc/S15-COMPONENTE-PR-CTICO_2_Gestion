# Solicitud de Cambio

## Datos Generales

| Campo | Valor |
|---|---|
| **Solicitud N°** | SC-001 |
| **Proyecto** | Calculadora Profesional — Entorno DevOps |
| **Solicitante** | Cliente (Usuario final) |
| **Fecha de solicitud** | 2026-06-15 |
| **Fecha de aprobación** | 2026-06-18 |
| **Responsable** | Adrián (Líder del grupo) |

## Cambio Solicitado

Agregar un **módulo de historial de operaciones** que permita:

1. Almacenar automáticamente cada operación realizada (fecha, operandos, operación, resultado).
2. Visualizar el historial en la interfaz.
3. Exportar el historial a un archivo CSV descargable.

## Motivo del Cambio

El cliente necesita llevar un registro trazable de las operaciones realizadas para su posterior revisión y análisis. Anteriormente la calculadora solo mostraba el resultado en pantalla sin persistencia de datos.

## Impacto del Cambio

| Área | Impacto |
|---|---|
| **Código nuevo** | `calculator_app/historial.py`, `calculator_app/exportar.py` |
| **Código modificado** | `calculator_app/views.py`, `calculator_app/urls.py`, `templates/index.html` |
| **Tests nuevos** | `test_historial.py`, `test_exportar.py` |
| **Documentación** | Esta solicitud, README actualizado |
| **Ramas** | `feature/historial`, `feature/exportar` |

## Prioridad

Alta — funcionalidad solicitada por el cliente para la entrega final.

## Aprobación

| Rol | Nombre | Fecha |
|---|---|---|
| **Líder de proyecto** | Adrián | 2026-06-18 |
| **Desarrollador** | [Compañero 1] | 2026-06-18 |
| **Desarrollador** | [Compañero 2] | 2026-06-18 |

## Implementación

El cambio fue implementado en las siguientes ramas:

- `feature/historial` — Módulo de historial (commits de Compañero 1)
- `feature/exportar` — Exportación CSV (commits de Compañero 2)

Ambas fueron integradas a `develop` y posteriormente a `master` mediante pull requests.

## Seguimiento

- **Commit inicial (v1)**: `66da046` — Calculadora básica funcional
- **Commit final (v2)**: [completar después del merge]
- **URL en producción**: [completar después del deploy]
