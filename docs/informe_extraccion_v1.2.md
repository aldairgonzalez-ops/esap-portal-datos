# Informe de la extracción · Portal de Datos ESAP v1.2

| | |
|---|---|
| Base | `esap_db` |
| Servidor | `100.127.140.5:5432` (IP interna del servidor: `172.18.0.25`) |
| Motor | PostgreSQL 16.14 (Debian 16.14-1.pgdg13+1) on x86_64-pc-linux-gnu |
| Usuario de extracción | `postgres` |
| Fecha de extracción | 2026-10-22 09:22:00 |
| Portal generado | `portal/Portal_de_Datos_ESAP_v1.2.html` · 2026-10-26 20:54 |

## Cifras

- Esquemas: 16 · tablas: 418 (1 de apoyo) · vistas: 8
- Columnas: 5700 · FK: 424 · relaciones implícitas: 9
- Funciones y procedimientos: 66 · triggers: 69 · tipos enumerados: 18
- Filas totales: 228.231
- Descripciones registradas en la base (COMMENT): 224 de 418 tablas · 604 de 5700 columnas
- Descripciones validadas en `config/descripciones.csv`, pendientes de registrar en la base: 194 tablas · 5096 columnas

## Cambios frente a la extracción del 2026-10-21

- **Tablas nuevas (0):** ninguna
- **Tablas que ya no están (0):** ninguna
- **Columnas nuevas en tablas que ya existían (0):** ninguna
- **Columnas retiradas de tablas que siguen (0):** ninguna
- **Columnas con otro tipo:** ninguna
- **FK nuevas (0):** ninguna
- **FK retiradas (0):** ninguna
- **Programables nuevos (0):** ninguna
- **Programables retirados (0):** ninguna
- **Tablas con otro número de filas:** 4

| Tabla | Antes | Ahora |
|---|--:|--:|
| `notifications.notificacion` | 6324 | 6345 |
| `legal_management.correos_juridicos` | 14036 | 14042 |
| `legal_management.correo_juridico_historial` | 14552 | 14558 |
| `legal_management.adjuntos_correo` | 2552 | 2554 |
