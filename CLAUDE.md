# Memoria del proyecto · Portal de Datos ESAP

> Contexto para retomar el trabajo en cualquier sesión. Leer completo antes de actuar.

## 1. Qué es
- **Proyecto:** base de datos de la **SuperApp ESAP** (Escuela Superior de Administración Pública). **No es UAPA ni SIPAE:** de ese proyecto solo se reutiliza el método (portal autónomo + scripts versionados + reglas de trabajo).
- **Usuario:** Aldair, responsable de la base de datos en la entrega del proyecto. Escribe en español.
- **Dos públicos, dos juegos de documentos:**
  - **Entregable al cliente:** descriptivo, en lenguaje directo y neutro. **No lleva hallazgos, indicadores con meta, oportunidades de mejora ni recomendaciones.**
    1. **Portal de Datos** (`portal/Portal_de_Datos_ESAP_<versión>.html`): HTML autónomo (sin conexión ni CDN) con dominios, catálogo, fichas de tabla, relaciones con multiplicidad UML, modelo ER por dominio, programables y datos personales.
    2. **Resumen ejecutivo** (`informe/Resumen_Ejecutivo_BD_ESAP_<versión>.docx`): alcance, dominios, contenido del modelo y datos personales; cita el portal (con enlace a cada sección) y el repositorio.
    3. **Detalle técnico:** `docs/csv/`, `docs/catalogo/*.md`, `docs/informe_extraccion_<versión>.md` y las consultas de `sql/`.
  - **Uso interno (personal del proyecto):** `interno/` (fuera de Git).
    1. **Informe interno de hallazgos y oportunidades de mejora** (`interno/Informe_Interno_Hallazgos_BD_ESAP_<versión>.docx`): indicadores K01–K10 con meta y estado, hallazgos H01–H12 con evidencia, oportunidades OM01–OM09 priorizadas, condiciones de intervención y anexos.
    2. **Portal interno** (`interno/Portal_de_Datos_ESAP_<versión>_interno.html`): el mismo portal con las vistas Calidad e Identidad y el diagnóstico de FK.
    3. **CSV de diagnóstico** (`interno/csv/`).

## 2. Base de datos
- **Motor:** PostgreSQL 16 (`esap_db`). Hay dos entornos, **DEV y QA**, accesibles por **Tailscale**; el usuario los usa desde pgAdmin.
- **Se trabaja con QA.** DEV y QA pueden tener la misma base `esap_db`: verificar siempre el servidor que imprime la extracción.
- **Conexión:** servicio `esap_qa` de `pg_service.conf` (plantilla en `config/pg_service.conf.example`) y contraseña en `pgpass.conf`. Nunca guardar credenciales en el repositorio.
- **Solo lectura:** la extracción corre en `BEGIN TRANSACTION READ ONLY` y el servicio fija `default_transaction_read_only=on`. Lo ideal es un rol lector dedicado (`sql/00_rol_lector.sql`, lo ejecuta el DBA).
- **Esquemas conocidos (QA, 2026):** `auth`, `academic_registration`, `academic_work_plan`, `audit`, `certification`, `control_interno`, `internal_disciplinary_control`, `legal_management`, `notifications`, `public`, `requerimientos_oc` (por confirmar). Diagnóstico previo (mayo 2026): 162 tablas en 11 esquemas, 61 sin filas, correo replicado en 6 esquemas.
- **Fuente maestra de identidad:** `auth.personas` (`dir_email`, `num_identificacion`, `id_person`). `auth."user"` enlaza con `id_person`.
- **Convenciones de nombres:** mezcla de español e inglés; claves con prefijo (`id_sede`, `id_person`) y con sufijo (`programa_id`, `sede_id`).

## 3. Cómo se trabaja (flujo)
```
python herramientas/extraer.py                         # 1. extracción de solo lectura -> extracciones/<fecha>/
python herramientas/generar_portal.py --extraccion extracciones/<fecha> --version vX.Y [--anterior extracciones/<fecha previa>] --repo <url>
python herramientas/generar_resumen.py --extraccion extracciones/<fecha> --version vX.Y --url-portal <url> --repo <url>
python herramientas/generar_informe_interno.py --extraccion extracciones/<fecha> --version vX.Y      # uso interno
```
- Si Claude corre **en el equipo del usuario** (Claude Code en VS Code o en la terminal, con Tailscale activo), puede lanzar el paso 1 directamente.
- Si Claude corre **en la nube**, no llega a la red de Tailscale: el usuario ejecuta el paso 1 y sube la carpeta de la extracción (por Git o por Drive) para los pasos 2 y 3.
- Probar el portal en el navegador antes de entregar: todas las vistas y fichas, tema claro y oscuro, sin errores de consola. Servidor local: `.claude/launch.json` (`python -m http.server 8765`).

## 4. Reglas de trabajo
1. **Nada escribe en la base sin aprobación explícita.** Todo script que escribe se genera en simulación (termina en `ROLLBACK` salvo `-v aplicar=1`), se revisa la salida, se aplica con aprobación y queda su lote con reversa (`herramientas/generar_comentarios.py`).
2. **No se cambian datos ni restricciones** (FK, índices, borrados, renombres) mientras desarrollo y QA trabajen en la base. Solo se intervienen metadatos (`COMMENT ON`), con lote y reversa. Las FK, índices y la depuración de tablas son **recomendaciones** para el equipo de desarrollo.
3. **No se extraen ni publican valores de datos.** Solo estructura, estadísticas (fracción de nulos, n_distinct) y conteos. Nada de valores frecuentes, histogramas ni muestras.
4. **No inventar descripciones.** Distinguir: descripción de la base (`COMMENT`) · propuesta (`config/descripciones.csv`, marcada «propuesta») · por documentar. Los nombres de dominio de `config/dominios.csv` son propuestas a validar con el cliente.
5. **Lenguaje directo y neutro** en todo documento. En el entregable se describe, no se califica: «por documentar», «tabla de apoyo», «sin filas en QA». Los hallazgos, el diagnóstico, las metas y las recomendaciones van **solo** en el informe interno y el portal interno, también en tono neutro: qué se observó, por qué importa y dónde verlo, sin adjetivos alarmistas. Antes de entregar, revisar que nada de `interno/` llegue al cliente.
6. **Versionado:** cada cambio del portal es una versión nueva (`--version`), con su informe de extracción. No sobrescribir versiones ya entregadas.
7. **Datos personales:** la clasificación por nombre de columna (Ley 1581 de 2012) es inicial y se valida con el responsable del tratamiento.

## 5. Estructura del repositorio
| Ruta | Contenido |
|---|---|
| `sql/extraccion/` | 14 consultas de solo lectura (00–13) y `extraer_todo.sql`, que las encadena |
| `sql/00_rol_lector.sql` | Rol lector para el DBA (opcional) |
| `sql/metadatos/` | Lotes `COMMENT ON` generados, con su reversa |
| `herramientas/` | `extraer.py`, `modelo.py`, `generar_portal.py`, `plantilla_portal.html`, `generar_resumen.py`, `generar_informe_interno.py`, `generar_comentarios.py`, `docx_util.py` |
| `config/` | `dominios.csv` (nombre funcional de cada esquema), `descripciones.csv` (propuestas de descripción), plantilla de conexión |
| `extracciones/<fecha>/` | JSONL de cada corte (solo metadatos y conteos) |
| `portal/`, `docs/`, `informe/` | Entregables generados (cliente) |
| `interno/` | Informe interno, portal interno y CSV de diagnóstico (no se versiona ni se entrega) |
| `pruebas/` | Esquema sintético para probar el flujo sin tocar QA |

## 6. Referencias
ISO/IEC 25012 (calidad de datos) · ISO/IEC 11179 (metadatos) · DAMA-DMBOK2 · Ley 1581 de 2012 y Decreto 1377 de 2013 · Ley 1712 de 2014 · MRAE de MinTIC.
Antecedentes en Drive: `Mi unidad/SuperApp ESAP/` (informes de diagnóstico V1–V5, modelo MDM original, presentaciones y volcados de esquemas de julio de 2026).
