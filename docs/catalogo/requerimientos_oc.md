# Requerimientos (`requerimientos_oc`)

Requerimientos y solicitudes registrados en la plataforma.

6 tablas · 0 vistas · 94 columnas · 32 filas · 2 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`avances_hallazgo`](#avances_hallazgo) | Tabla | 0 | _Por documentar_ |
| [`cat_organismos_control`](#cat_organismos_control) | Tabla | 25 | Catálogo maestro de organismos de control que pueden generar requerimientos a la ESAP |
| [`hallazgos`](#hallazgos) | Tabla | 2 | _Por documentar_ |
| [`historial_requerimientos`](#historial_requerimientos) | Tabla | 0 | _Por documentar_ |
| [`requerimientos`](#requerimientos) | Tabla | 5 | Gestión de requerimientos de órganos de control con radicado automático y cálculo de vencimiento |
| [`solicitudes_insumos`](#solicitudes_insumos) | Tabla | 0 | _Por documentar_ |

## avances_hallazgo

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `hallazgo_id` → `requerimientos_oc.hallazgos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `hallazgo_id` | `uuid` | no | _Por documentar_ | FK→requerimientos_oc.hallazgos.id |
| 3 | `fecha_reporte` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 4 | `porcentaje_avance` | `integer` | sí | _Por documentar_ |  |
| 5 | `descripcion_avance` | `text` | no | _Por documentar_ |  |
| 6 | `documentos_adjuntos_urls` | `text[]` | sí | _Por documentar_ |  |
| 7 | `reportado_a_sireci` | `boolean` | sí | _Por documentar_ |  |
| 8 | `fecha_reporte_sireci` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 9 | `reportado_por` | `character varying(150)` | sí | _Por documentar_ |  |
| 10 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## cat_organismos_control

Catálogo maestro de organismos de control que pueden generar requerimientos a la ESAP

- Clave primaria: `id`
- Filas: 25

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | _Por documentar_ | PK |
| 2 | `nombre` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `sigla` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `tipo` | `character varying(50)` | no | _Por documentar_ |  |
| 5 | `nivel` | `character varying(50)` | no | _Por documentar_ |  |
| 6 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 7 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 8 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## hallazgos

_Por documentar._

- Clave primaria: `id`
- Filas: 2
- Referencia a: `requerimiento_id` → `requerimientos_oc.requerimientos` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `requerimiento_id` | `uuid` | sí | _Por documentar_ | FK→requerimientos_oc.requerimientos.id |
| 3 | `codigo_hallazgo` | `character varying(50)` | no | _Por documentar_ | única |
| 4 | `numero_interno` | `character varying(50)` | sí | _Por documentar_ |  |
| 5 | `tipo_hallazgo` | `character varying(30)` | sí | _Por documentar_ |  |
| 6 | `titulo` | `character varying(300)` | no | _Por documentar_ |  |
| 7 | `descripcion` | `text` | no | _Por documentar_ |  |
| 8 | `causa_raiz` | `text` | sí | _Por documentar_ |  |
| 9 | `efecto` | `text` | sí | _Por documentar_ |  |
| 10 | `area_responsable` | `character varying(100)` | sí | _Por documentar_ |  |
| 11 | `funcionario_responsable` | `character varying(150)` | sí | _Por documentar_ |  |
| 12 | `accion_correctiva` | `text` | no | _Por documentar_ |  |
| 13 | `fecha_compromiso` | `date` | no | _Por documentar_ |  |
| 14 | `indicador_cumplimiento` | `text` | sí | _Por documentar_ |  |
| 15 | `meta_indicador` | `character varying(100)` | sí | _Por documentar_ |  |
| 16 | `estado` | `character varying(30)` | sí | _Por documentar_ |  |
| 17 | `porcentaje_avance` | `integer` | sí | _Por documentar_ |  |
| 18 | `fecha_ultimo_reporte` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 19 | `fecha_proximo_reporte` | `date` | sí | _Por documentar_ |  |
| 20 | `periodicidad_reporte` | `character varying(20)` | sí | _Por documentar_ |  |
| 21 | `documento_plan_url` | `character varying(500)` | sí | _Por documentar_ |  |
| 22 | `documentos_evidencia_urls` | `text[]` | sí | _Por documentar_ |  |
| 23 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 24 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 25 | `created_by` | `character varying(150)` | sí | _Por documentar_ |  |

## historial_requerimientos

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `requerimiento_id` → `requerimientos_oc.requerimientos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `requerimiento_id` | `uuid` | no | _Por documentar_ | FK→requerimientos_oc.requerimientos.id |
| 3 | `accion` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `estado_anterior` | `character varying(30)` | sí | _Por documentar_ |  |
| 6 | `estado_nuevo` | `character varying(30)` | sí | _Por documentar_ |  |
| 7 | `usuario_nombre` | `character varying(150)` | sí | _Por documentar_ |  |
| 8 | `area_usuario` | `character varying(100)` | sí | _Por documentar_ |  |
| 9 | `fecha` | `timestamp without time zone` | sí | _Por documentar_ |  |

## requerimientos

Gestión de requerimientos de órganos de control con radicado automático y cálculo de vencimiento

- Clave primaria: `id`
- Filas: 5
- Referencia a: `entidad_id` → `requerimientos_oc.cat_organismos_control` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `radicado_externo` | `character varying(50)` | no | _Por documentar_ |  |
| 3 | `radicado_interno` | `character varying(20)` | no | Formato: OC-YYYY-NNNNN (generado automáticamente) | única |
| 4 | `entidad_id` | `integer` | no | _Por documentar_ | FK→requerimientos_oc.cat_organismos_control.id |
| 5 | `asunto` | `text` | no | _Por documentar_ |  |
| 6 | `tipo_requerimiento` | `character varying(50)` | no | _Por documentar_ |  |
| 7 | `fecha_recepcion` | `date` | no | _Por documentar_ |  |
| 8 | `fecha_vencimiento` | `date` | no | Calculada automáticamente sumando días hábiles (sin sábados/domingos) a fecha_recepcion |  |
| 9 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 10 | `prioridad_calculada` | `character varying(20)` | sí | Calculada dinámicamente basada en días restantes y tipo de requerimiento |  |
| 11 | `archivo_adjunto_url` | `character varying(500)` | sí | _Por documentar_ |  |
| 12 | `usuario_asignado_id` | `integer` | sí | _Por documentar_ |  |
| 13 | `auditoria_created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 15 | `unidad_tiempo` | `character varying(20)` | sí | _Por documentar_ |  |
| 16 | `dias_plazo_otorgado` | `integer` | sí | _Por documentar_ |  |
| 17 | `referencia_externa` | `character varying(100)` | sí | _Por documentar_ |  |
| 18 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 19 | `funcionario_responsable` | `character varying(150)` | sí | _Por documentar_ |  |
| 20 | `area_responsable` | `character varying(100)` | sí | _Por documentar_ |  |
| 21 | `fecha_respuesta` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 22 | `oficio_respuesta_url` | `character varying(500)` | sí | _Por documentar_ |  |
| 23 | `acuse_recibo_url` | `character varying(500)` | sí | _Por documentar_ |  |
| 24 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 25 | `created_by` | `character varying(150)` | sí | _Por documentar_ |  |

## solicitudes_insumos

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `requerimiento_id` → `requerimientos_oc.requerimientos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `requerimiento_id` | `uuid` | no | _Por documentar_ | FK→requerimientos_oc.requerimientos.id |
| 3 | `area_destino` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `funcionario_destino` | `character varying(150)` | sí | _Por documentar_ |  |
| 5 | `email_destino` | `character varying(150)` | sí | _Por documentar_ | Contacto |
| 6 | `descripcion_solicitud` | `text` | no | _Por documentar_ |  |
| 7 | `documentos_solicitados` | `text` | sí | _Por documentar_ |  |
| 8 | `fecha_solicitud` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 9 | `fecha_vencimiento` | `timestamp without time zone` | no | _Por documentar_ |  |
| 10 | `fecha_respuesta` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `estado` | `character varying(20)` | sí | _Por documentar_ |  |
| 12 | `documentos_entregados_urls` | `text[]` | sí | _Por documentar_ |  |
| 13 | `comentario_respuesta` | `text` | sí | _Por documentar_ |  |
| 14 | `solicitado_por` | `character varying(150)` | sí | _Por documentar_ |  |
| 15 | `respondido_por` | `character varying(150)` | sí | _Por documentar_ |  |
| 16 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 17 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
