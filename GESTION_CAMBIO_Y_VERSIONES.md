# Gestión del Cambio y Gestión de Versiones

---

## Punto 1 — Gestión del Cambio

### Solicitud de Cambio SC-001

#### Datos Generales

| Campo | Valor |
|---|---|
| **Solicitud N°** | SC-001 |
| **Proyecto** | Calculadora Profesional — Entorno DevOps |
| **Solicitante** | Cliente (Usuario final) |
| **Fecha de solicitud** | 2026-06-15 |
| **Fecha de aprobación** | 2026-06-18 |
| **Responsable** | Adrián (Líder del grupo) |

#### Cambio Solicitado

Agregar un **módulo de historial de operaciones** que permita:

1. Almacenar automáticamente cada operación realizada (fecha, operandos, operación, resultado).
2. Visualizar el historial en la interfaz.
3. Exportar el historial a un archivo CSV descargable.

#### Motivo del Cambio

El cliente necesita llevar un registro trazable de las operaciones realizadas para su posterior revisión y análisis. Anteriormente la calculadora solo mostraba el resultado en pantalla sin persistencia de datos.

#### Impacto del Cambio

| Área | Impacto |
|---|---|
| **Código nuevo** | `calculator_app/historial.py`, `calculator_app/exportar.py` |
| **Código modificado** | `calculator_app/views.py`, `calculator_app/urls.py`, `templates/index.html` |
| **Tests nuevos** | `test_historial.py`, `test_exportar.py` |
| **Documentación** | Esta solicitud, README actualizado |
| **Ramas** | `feature/historial`, `feature/exportar` |

#### Prioridad

Alta — funcionalidad solicitada por el cliente para la entrega final.

#### Aprobación

| Rol | Nombre | Fecha |
|---|---|---|
| **Líder de proyecto** | Adrián | 2026-06-18 |
| **Desarrollador** | Adan | 2026-06-18 |
| **Desarrollador** | Natanael | 2026-06-18 |
| **Desarrollador** | Cucho | 2026-06-18 |
| **Desarrollador** | Quevedo | 2026-06-18 |

#### Implementación

El cambio fue implementado en las siguientes ramas:

- `feature/historial` — Módulo de historial
- `feature/exportar` — Exportación CSV
- `feature/boton-signo` — Botón de cambio de signo (±)
- `feature/footer-version` — Información de versión en footer
- `feature/color-eq` — Mejora visual del botón igual
- `feature/borde-brillante` — Efecto decorativo en la calculadora

Todas fueron integradas a `develop` y posteriormente a `master` mediante merges.

#### Seguimiento

- **Commit inicial (v1)**: `66da046` — Calculadora básica funcional
- **Commit final (v2)**: `ea32488` — Calculadora con historial + exportación CSV + CI/CD + deploy
- **URL en producción**: https://s15-componente-pr-ctico-2-gestion.onrender.com

---

## Punto 2 — Gestión de Versiones (GitHub)

### Repositorio

**URL:** https://github.com/Josegomezxc/S15-COMPONENTE-PR-CTICO_2_Gestion

### Ramas Utilizadas

| Rama | Propósito |
|---|---|
| `master` | Rama principal — código en producción |
| `develop` | Rama de integración — aquí se fusionan las features |
| `feature/historial` | Módulo de historial de operaciones |
| `feature/exportar` | Exportación CSV del historial |
| `feature/boton-signo` | Botón de cambio de signo (±) |
| `feature/footer-version` | Información de versión en footer |
| `feature/color-eq` | Mejora visual del botón igual |
| `feature/borde-brillante` | Efecto decorativo animado |

### Historial de Commits (Graph)

```
* ea32488 (master, tag: v2) docs: actualizar seguimiento en solicitud de cambio
*   3513250 fix: merge test fix to master
|\
| *   81d7635 (develop) fix: merge test fix from exportar
| |\
| | * 5358acc (feature/exportar) fix: corregir test
* | | d1980da release: v2 - Historial y Exportación CSV
|\| |
| * | 888138c merge: integrar feature/exportar a develop
| |\|
| | * 93259eb feat: agregar módulo de exportación CSV
| * | ae0b14e merge: integrar feature/historial a develop
| |\|
| | * baf99be (feature/historial) test: tests para historial
| | * 1aad40e feat: módulo de historial de operaciones
| * | 55ee063 deploy: configurar Render
| * | d48e6fe ci: pipeline CI/CD con GitHub Actions
| |/
| * 992d33e test: tests unitarios (unittest + pytest)
| * e513585 docs: solicitud de cambio SC-001
|/
* 66da046 (tag: v1) Version 1 — Calculadora básica
```

### Commits por Miembro del Equipo

| Persona | Commits | Aportación |
|---|---|---|
| **Adrián (Líder)** | `e513585`, `992d33e`, `d48e6fe`, `55ee063`, `ae0b14e`, `888138c`, `d1980da`, `3513250`, `ea32488` | Estructura base, tests, CI/CD, deploy, merges |
| **Adan** | (feature/boton-signo) | Botón de cambio de signo (±) |
| **Natanael** | (feature/footer-version) | Información de versión en footer |
| **Cucho** | (feature/color-eq) | Mejora visual del botón igual |
| **Quevedo** | (feature/borde-brillante) | Efecto decorativo animado |

### Comparación entre Versiones: v1 vs v2

#### v1 — Calculadora Básica (tag: v1, commit `66da046`)

```
- Operaciones: suma, resta, multiplicación, división
- Interfaz web básica con Tailwind CSS
- Backend Django con API REST
- Sin persistencia de datos
- Sin tests automatizados
- Sin CI/CD
- Sin despliegue
```

#### v2 — Calculadora Completa (tag: v2, commit `ea32488`)

```
- Todo lo de v1 más:
- Módulo de historial con persistencia en JSON
- Panel lateral para visualizar operaciones anteriores
- Exportación de historial a CSV descargable
- Botón de cambio de signo (±)
- Información de versión en footer
- Mejoras visuales (colores, animaciones)
- Pipeline CI/CD con GitHub Actions (16 tests)
- Despliegue automático en Render
- 5 ramas de desarrollo paralelo
- 5 desarrolladores colaborando
```

#### Resumen del cambio entre v1 y v2 (`git diff v1..v2 --stat`)

```
15 archivos modificados
523 líneas añadidas
46 líneas eliminadas

Archivos nuevos:
  .github/workflows/build.yml  → Pipeline CI/CD
  SOLICITUD_CAMBIO.md          → Documentación del cambio
  calculator_app/historial.py   → Módulo de historial
  calculator_app/exportar.py    → Exportación CSV
  render.yaml                   → Configuración de despliegue
  test_calculadora.py           → Tests (pytest)
  test_calculator.py            → Tests (unittest)
  test_historial.py             → Tests de historial
  test_exportar.py              → Tests de exportación
```

### Comandos para la Demostración en Vivo

```bash
# Ver historial completo con ramas
git log --oneline --graph --all --decorate

# Comparar versiones (cambios entre v1 y v2)
git diff v1..v2 --stat

# Ver contenido completo de un cambio
git diff v1..v2

# Ver commits de un miembro específico
git log --author="Adan"
git log --author="Natanael"

# Ver qué archivos cambiaron en cada versión
git show v1 --name-only
git show v2 --name-only
```
