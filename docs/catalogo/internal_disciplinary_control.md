# Control disciplinario interno (`internal_disciplinary_control`)

Procesos de control disciplinario interno.

26 tablas · 0 vistas · 358 columnas · 1.181 filas · 4 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`actas_configuration`](#actas_configuration) | Tabla | 8 | Tabla de configuración paramétrica de actas para el módulo disciplinario |
| [`alertas_enviadas`](#alertas_enviadas) | Tabla | 117 | _Por documentar_ |
| [`auto_versions`](#auto_versions) | Tabla | 244 | _Por documentar_ |
| [`autos_configuration`](#autos_configuration) | Tabla | 38 | _Por documentar_ |
| [`dias_festivos`](#dias_festivos) | Tabla | 19 | _Por documentar_ |
| [`disciplinary_behaviors`](#disciplinary_behaviors) | Tabla | 17 | Catálogo parametrizable de conductas indisciplinarias |
| [`disciplinary_news`](#disciplinary_news) | Tabla | 35 | Noticias disciplinarias recibidas |
| [`disciplinary_news_processes`](#disciplinary_news_processes) | Tabla | 9 | Tabla puente para asociar noticias disciplinarias con procesos disciplinarios |
| [`disciplinary_process_actuaciones`](#disciplinary_process_actuaciones) | Tabla | 148 | _Por documentar_ |
| [`disciplinary_process_notes`](#disciplinary_process_notes) | Tabla | 14 | _Por documentar_ |
| [`disciplinary_process_reassignment_requests`](#disciplinary_process_reassignment_requests) | Tabla | 24 | Tabla para solicitudes de reasignación de procesos disciplinarios |
| [`disciplinary_process_tasks`](#disciplinary_process_tasks) | Tabla | 15 | _Por documentar_ |
| [`disciplinary_processes`](#disciplinary_processes) | Tabla | 26 | Procesos disciplinarios activos |
| [`disciplinary_professional`](#disciplinary_professional) | Tabla | 9 | Profesionales (abogados) asignados a procesos disciplinarios |
| [`entidades_remision`](#entidades_remision) | Tabla | 9 | Tabla para gestionar las entidades de remisión en procesos disciplinarios |
| [`evidence`](#evidence) | Tabla | 70 | Evidencias y documentos adjuntos a los procesos |
| [`expediente_compartido`](#expediente_compartido) | Tabla | 95 | Tabla para gestionar los enlaces compartidos de expedientes disciplinarios |
| [`legal_autos`](#legal_autos) | Tabla | 218 | Autos legales generados en los procesos |
| [`oficios_configuration`](#oficios_configuration) | Tabla | 14 | _Por documentar_ |
| [`plantilla_auto`](#plantilla_auto) | Tabla | 1 | _Por documentar_ |
| [`reglas_alerta`](#reglas_alerta) | Tabla | 7 | _Por documentar_ |
| [`sequences`](#sequences) | Tabla | 7 | Tabla para gestionar secuencias de radicados |
| [`stage_configuration`](#stage_configuration) | Tabla | 7 | Configuración de días hábiles por etapa procesal |
| [`system_configuration`](#system_configuration) | Tabla | 1 | Configuración global del sistema disciplinario |
| [`terminos_procesales`](#terminos_procesales) | Tabla | 23 | _Por documentar_ |
| [`tipos_remision`](#tipos_remision) | Tabla | 6 | Tabla para gestionar los tipos de remisión en procesos disciplinarios |

## actas_configuration

Tabla de configuración paramétrica de actas para el módulo disciplinario

- Clave primaria: `id`
- Filas: 8

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `tipo` | `character varying(100)` | no | Tipo de acta (ej: ACTA_AUDIENCIA, ACTA_VERIFICACION, ACTA_CONSTITUCION) | única |
| 3 | `nombre` | `character varying(200)` | no | Nombre descriptivo del tipo de acta |  |
| 4 | `estado` | `character varying(50)` | sí | Estado de la configuración (activo/inactivo) |  |
| 5 | `codigo` | `character varying(50)` | sí | Código único del tipo de acta (ej: ACTA-001) |  |
| 6 | `descripcion` | `text` | sí | Descripción del tipo de acta |  |
| 7 | `plantilla` | `text` | sí | URL o contenido de la plantilla asociada |  |
| 8 | `nombre_plantilla` | `character varying(255)` | sí | Nombre del archivo de plantilla |  |
| 9 | `descripcion_plantilla` | `text` | sí | Descripción de la plantilla |  |
| 10 | `version_plantilla` | `character varying(50)` | sí | Versión de la plantilla |  |
| 11 | `estado_plantilla` | `character varying(50)` | sí | Estado de la plantilla (activo/inactivo) |  |
| 12 | `stage` | `character varying(50)` | sí | Etapa del proceso asociada (RECEPCION, EVALUACION, etc.) |  |
| 13 | `orden` | `integer` | sí | Orden de visualización en listados |  |
| 14 | `createdat` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 15 | `updatedat` | `timestamp without time zone` | sí | _Por documentar_ |  |

## alertas_enviadas

_Por documentar._

- Clave primaria: `id`
- Filas: 117
- Referencia a: `auto_id` → `internal_disciplinary_control.legal_autos` (0..1 → 0..1); `regla_alerta_id` → `internal_disciplinary_control.reglas_alerta` (0..1 → 0..1); `termino_id` → `internal_disciplinary_control.terminos_procesales` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `termino_id` | `uuid` | sí | _Por documentar_ | FK→internal_disciplinary_control.terminos_procesales.id |
| 3 | `regla_alerta_id` | `uuid` | sí | _Por documentar_ | FK→internal_disciplinary_control.reglas_alerta.id |
| 4 | `tipo` | `internal_disciplinary_control.tipo_alerta_enum` | no | _Por documentar_ |  |
| 5 | `destinatario` | `character varying(200)` | no | _Por documentar_ |  |
| 6 | `asunto` | `character varying(500)` | sí | _Por documentar_ |  |
| 7 | `mensaje` | `text` | sí | _Por documentar_ |  |
| 8 | `estado` | `internal_disciplinary_control.estado_alerta_enum` | no | _Por documentar_ |  |
| 9 | `fecha_envio` | `timestamp without time zone` | no | _Por documentar_ |  |
| 10 | `fecha_lectura` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `error_mensaje` | `text` | sí | _Por documentar_ |  |
| 12 | `creado_por_id` | `uuid` | sí | _Por documentar_ |  |
| 13 | `fecha_creacion` | `timestamp without time zone` | no | _Por documentar_ |  |
| 14 | `auto_id` | `uuid` | sí | _Por documentar_ | FK→internal_disciplinary_control.legal_autos.id |

## auto_versions

_Por documentar._

- Clave primaria: `id`
- Filas: 244

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `autoId` | `uuid` | sí | _Por documentar_ |  |
| 3 | `contenido` | `text` | no | _Por documentar_ |  |
| 4 | `versionNumber` | `integer` | no | _Por documentar_ |  |
| 5 | `createdBy` | `uuid` | sí | _Por documentar_ |  |
| 6 | `changeReason` | `text` | sí | _Por documentar_ |  |
| 7 | `createdAt` | `timestamp with time zone` | no | _Por documentar_ |  |
| 8 | `documentUrl` | `text` | sí | URL del archivo adjunto en esta versión (si existe) |  |
| 9 | `documentName` | `text` | sí | Nombre del archivo adjunto en esta versión |  |

## autos_configuration

_Por documentar._

- Clave primaria: no declarada
- Filas: 38

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ |  |
| 2 | `tipo` | `character varying(100)` | no | _Por documentar_ |  |
| 3 | `nombre` | `character varying(200)` | no | _Por documentar_ |  |
| 4 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 5 | `plantilla` | `text` | sí | _Por documentar_ |  |
| 6 | `orden` | `integer` | sí | _Por documentar_ |  |
| 7 | `createdAt` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 8 | `updatedAt` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 9 | `stage` | `character varying(50)` | sí | _Por documentar_ |  |
| 10 | `nombre_plantilla` | `character varying(255)` | sí | Nombre de la plantilla asociada al tipo de auto |  |
| 11 | `descripcion_plantilla` | `text` | sí | Descripción de la plantilla |  |
| 12 | `version_plantilla` | `character varying(50)` | sí | Versión de la plantilla (ej: 1.0, 2.0) |  |
| 13 | `estado_plantilla` | `character varying(50)` | sí | Estado de la plantilla (activo/inactivo) |  |

## dias_festivos

_Por documentar._

- Clave primaria: `id`
- Filas: 19

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `fecha` | `date` | no | _Por documentar_ |  |
| 3 | `descripcion` | `character varying(200)` | no | _Por documentar_ |  |
| 4 | `tipo` | `internal_disciplinary_control.tipo_festivo_enum` | no | _Por documentar_ |  |
| 5 | `territorio` | `character varying(100)` | sí | _Por documentar_ |  |
| 6 | `activo` | `boolean` | no | _Por documentar_ |  |
| 7 | `creado_por_id` | `uuid` | no | _Por documentar_ |  |
| 8 | `fecha_creacion` | `timestamp without time zone` | no | _Por documentar_ |  |
| 9 | `fecha_actualizacion` | `timestamp without time zone` | no | _Por documentar_ |  |

## disciplinary_behaviors

Catálogo parametrizable de conductas indisciplinarias

- Clave primaria: `id`
- Filas: 17

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único de la conducta | PK |
| 2 | `codigo` | `character varying(50)` | no | Código único de la conducta (ej: ABANDONO_CARGO) | única |
| 3 | `nombre` | `character varying(255)` | no | Nombre descriptivo de la conducta | única |
| 4 | `descripcion` | `text` | sí | Descripción detallada de la conducta |  |
| 5 | `estado` | `boolean` | no | Estado activo/inactivo de la conducta |  |
| 6 | `orden` | `integer` | no | Orden de visualización en listas |  |
| 7 | `created_at` | `timestamp without time zone` | no | Fecha de creación del registro |  |
| 8 | `updated_at` | `timestamp without time zone` | no | Fecha de última actualización |  |

## disciplinary_news

Noticias disciplinarias recibidas

- Clave primaria: `id`
- Filas: 35

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `radicado` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `fechaRecepcion` | `timestamp without time zone` | no | _Por documentar_ |  |
| 4 | `origen` | `internal_disciplinary_control.disciplinary_news_origen_enum` | sí | _Por documentar_ |  |
| 5 | `territorial` | `character varying(100)` | sí | _Por documentar_ |  |
| 6 | `dependenciaDenunciado` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `denunciante` | `jsonb` | sí | Datos del denunciante en formato JSON |  |
| 8 | `disciplinable` | `jsonb` | sí | Datos del disciplinable en formato JSON |  |
| 9 | `hechos` | `text` | no | _Por documentar_ |  |
| 10 | `adjuntos` | `text[]` | sí | _Por documentar_ |  |
| 11 | `estado` | `internal_disciplinary_control.disciplinary_news_estado_enum` | no | Estados: RADICADA, ASIGNADA, DEVUELTA, ARCHIVADA |  |
| 12 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 13 | `updatedAt` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 14 | `historialAuditoria` | `jsonb` | sí | _Por documentar_ |  |
| 15 | `fechaQueja` | `timestamp without time zone` | sí | Fecha reportada de la queja/hechos |  |
| 16 | `conductas` | `text[]` | sí | Conductas presuntamente indisciplinarias |  |
| 17 | `kanbanStage` | `uuid` | sí | _Por documentar_ |  |
| 18 | `fechaHechos` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 19 | `fechaCaducidad` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 20 | `proceso_asociado_id` | `uuid` | sí | _Por documentar_ |  |
| 21 | `proceso_asociado_numero` | `character varying(50)` | sí | _Por documentar_ |  |
| 22 | `proceso_asociado_fecha` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 23 | `proceso_asociado_justificacion` | `text` | sí | _Por documentar_ |  |
| 24 | `numero_rc` | `character varying(50)` | sí | _Por documentar_ |  |
| 25 | `entidad_remision` | `character varying(255)` | sí | _Por documentar_ |  |
| 26 | `correo_entidad_remision` | `character varying(255)` | sí | _Por documentar_ |  |
| 27 | `fecha_remision` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 28 | `tipo_remision` | `character varying(100)` | sí | _Por documentar_ |  |
| 29 | `justificacion_remision` | `text` | sí | _Por documentar_ |  |
| 30 | `descripcion_remision` | `jsonb` | sí | _Por documentar_ |  |
| 31 | `radicador_id` | `uuid` | sí | _Por documentar_ |  |
| 32 | `conducta_disciplinaria` | `character varying(255)` | sí | _Por documentar_ |  |
| 33 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |

## disciplinary_news_processes

Tabla puente para asociar noticias disciplinarias con procesos disciplinarios

- Clave primaria: `id`
- Filas: 9
- Referencia a: `process_id` → `internal_disciplinary_control.disciplinary_processes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `news_id` | `uuid` | no | ID de la noticia disciplinaria |  |
| 3 | `process_id` | `uuid` | no | ID del proceso disciplinario | FK→internal_disciplinary_control.disciplinary_processes.id |
| 4 | `fecha_asociacion` | `timestamp with time zone` | no | Fecha en que se realizó la asociación |  |
| 5 | `justificacion` | `text` | sí | Justificación de la asociación |  |
| 6 | `created_at` | `timestamp with time zone` | no | Fecha de creación del registro |  |
| 7 | `updated_at` | `timestamp with time zone` | no | Fecha de última actualización del registro |  |

## disciplinary_process_actuaciones

_Por documentar._

- Clave primaria: `id`
- Filas: 148
- Referencia a: `newsId` → `internal_disciplinary_control.disciplinary_news` (0..* → 0..1); `processId` → `internal_disciplinary_control.disciplinary_processes` (1..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `processId` | `uuid` | sí | _Por documentar_ | FK→internal_disciplinary_control.disciplinary_processes.id |
| 3 | `tipo` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `etapa` | `character varying(80)` | sí | _Por documentar_ |  |
| 5 | `descripcion` | `text` | no | _Por documentar_ |  |
| 6 | `responsableNombre` | `character varying(255)` | no | _Por documentar_ |  |
| 7 | `fechaActuacion` | `timestamp with time zone` | no | _Por documentar_ |  |
| 8 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 9 | `createdAt` | `timestamp with time zone` | no | _Por documentar_ |  |
| 10 | `updatedAt` | `timestamp with time zone` | no | _Por documentar_ |  |
| 11 | `newsId` | `uuid` | sí | _Por documentar_ | FK→internal_disciplinary_control.disciplinary_news.id |

## disciplinary_process_notes

_Por documentar._

- Clave primaria: `id`
- Filas: 14
- Referencia a: `processId` → `internal_disciplinary_control.disciplinary_processes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `processId` | `uuid` | no | _Por documentar_ | FK→internal_disciplinary_control.disciplinary_processes.id |
| 3 | `texto` | `text` | no | _Por documentar_ |  |
| 4 | `etapa` | `character varying(80)` | sí | _Por documentar_ |  |
| 5 | `createdAt` | `timestamp with time zone` | no | _Por documentar_ |  |
| 6 | `updatedAt` | `timestamp with time zone` | no | _Por documentar_ |  |

## disciplinary_process_reassignment_requests

Tabla para solicitudes de reasignación de procesos disciplinarios

- Clave primaria: `id`
- Filas: 24
- Referencia a: `current_professional_id` → `internal_disciplinary_control.disciplinary_professional` (0..* → 0..1); `new_professional_id` → `internal_disciplinary_control.disciplinary_professional` (0..* → 1); `process_id` → `internal_disciplinary_control.disciplinary_processes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `process_id` | `uuid` | no | ID del proceso disciplinario a reasignar | FK→internal_disciplinary_control.disciplinary_processes.id |
| 3 | `current_professional_id` | `uuid` | sí | ID del profesional actualmente asignado | FK→internal_disciplinary_control.disciplinary_professional.id |
| 4 | `new_professional_id` | `uuid` | no | ID del profesional solicitado para asignación | FK→internal_disciplinary_control.disciplinary_professional.id |
| 5 | `justification` | `text` | no | Justificación de la solicitud de reasignación |  |
| 6 | `priority` | `character varying(10)` | sí | Prioridad de la solicitud (NORMAL o URGENTE) |  |
| 7 | `status` | `character varying(15)` | sí | Estado de la solicitud (PENDIENTE, APROBADA, RECHAZADA) |  |
| 8 | `jefe_observations` | `text` | sí | Observaciones del jefe al procesar la solicitud |  |
| 9 | `rejection_reason` | `text` | sí | Motivo de rechazo si aplica |  |
| 10 | `resolved_at` | `timestamp without time zone` | sí | Fecha en que se resolvió la solicitud |  |
| 11 | `requested_by` | `character varying(100)` | no | Nombre del usuario que solicitó la reasignación |  |
| 12 | `requested_by_id` | `character varying(50)` | sí | ID del usuario que solicitó la reasignación |  |
| 13 | `created_at` | `timestamp without time zone` | no | Fecha de creación de la solicitud |  |
| 14 | `updated_at` | `timestamp without time zone` | no | Fecha de última actualización de la solicitud |  |
| 15 | `was_initially_unassigned` | `boolean` | sí | _Por documentar_ |  |

## disciplinary_process_tasks

_Por documentar._

- Clave primaria: `id`
- Filas: 15
- Referencia a: `processId` → `internal_disciplinary_control.disciplinary_processes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `processId` | `uuid` | no | _Por documentar_ | FK→internal_disciplinary_control.disciplinary_processes.id |
| 3 | `titulo` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `prioridad` | `character varying(20)` | no | _Por documentar_ |  |
| 6 | `etapa` | `character varying(80)` | sí | _Por documentar_ |  |
| 7 | `responsableNombre` | `character varying(255)` | sí | _Por documentar_ |  |
| 8 | `fechaVencimiento` | `date` | no | _Por documentar_ |  |
| 9 | `completada` | `boolean` | no | _Por documentar_ |  |
| 10 | `fechaCompletada` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 11 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 12 | `createdAt` | `timestamp with time zone` | no | _Por documentar_ |  |
| 13 | `updatedAt` | `timestamp with time zone` | no | _Por documentar_ |  |

## disciplinary_processes

Procesos disciplinarios activos

- Clave primaria: `id`
- Filas: 26
- Referencia a: `abogado_asignado_id` → `internal_disciplinary_control.disciplinary_professional` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `radicadoProceso` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `newsId` | `uuid` | no | _Por documentar_ |  |
| 4 | `abogado_asignado_id` | `uuid` | sí | _Por documentar_ | FK→internal_disciplinary_control.disciplinary_professional.id |
| 5 | `etapaActual` | `character varying(100)` | no | Etapa actual del proceso disciplinario (VARCHAR - flexible para nuevas etapas) |  |
| 6 | `estado` | `internal_disciplinary_control.disciplinary_processes_estado_enum` | no | Estados: ACTIVO, SUSPENDIDO, ARCHIVADO, TERMINADO |  |
| 7 | `fechaPrescripcion` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 8 | `fechaVencimientoEtapa` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 9 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 10 | `pruebas` | `text[]` | sí | _Por documentar_ |  |
| 11 | `createdAt` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 12 | `updatedAt` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 13 | `kanbanStage` | `uuid` | sí | _Por documentar_ |  |
| 14 | `kanbanNotice` | `text` | sí | _Por documentar_ |  |
| 15 | `drafts_count` | `integer` | sí | _Por documentar_ |  |
| 16 | `documents_count` | `integer` | sí | _Por documentar_ |  |
| 17 | `time_percentage` | `numeric(5,2)` | sí | _Por documentar_ |  |
| 18 | `proceso_asociado_id` | `uuid` | sí | _Por documentar_ |  |
| 19 | `proceso_asociado_numero` | `character varying(50)` | sí | _Por documentar_ |  |
| 20 | `proceso_asociado_tipo` | `character varying(20)` | sí | _Por documentar_ |  |
| 21 | `proceso_asociado_fecha` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 22 | `proceso_asociado_justificacion` | `text` | sí | _Por documentar_ |  |
| 23 | `procesos_consolidados` | `text[]` | sí | _Por documentar_ |  |
| 24 | `proceso_consolidado_principal` | `uuid` | sí | _Por documentar_ |  |
| 25 | `informacion_consolidada` | `jsonb` | sí | _Por documentar_ |  |
| 26 | `fechaInicioEtapa` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 27 | `fecha_cierre` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 28 | `etapa_al_cierre` | `character varying(100)` | sí | _Por documentar_ |  |
| 29 | `cerrado_por_id` | `uuid` | sí | _Por documentar_ |  |
| 30 | `correo_juridica_enviado` | `boolean` | sí | _Por documentar_ |  |
| 31 | `correo_juridica_fecha_envio` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 32 | `restaurado` | `boolean` | no | Indica si el proceso disciplinario fue restaurado desde estado archivado |  |
| 33 | `en_proceso_remision` | `boolean` | sí | _Por documentar_ |  |
| 34 | `remision_aprobada` | `boolean` | sí | _Por documentar_ |  |
| 35 | `numero_rc` | `character varying(50)` | sí | _Por documentar_ |  |
| 36 | `entidad_remision` | `character varying(255)` | sí | _Por documentar_ |  |
| 37 | `correo_entidad_remision` | `character varying(255)` | sí | _Por documentar_ |  |
| 38 | `fecha_remision` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 39 | `tipo_remision` | `character varying(100)` | sí | _Por documentar_ |  |
| 40 | `justificacion_remision` | `text` | sí | _Por documentar_ |  |
| 41 | `descripcion_remision` | `jsonb` | sí | _Por documentar_ |  |

## disciplinary_professional

Profesionales (abogados) asignados a procesos disciplinarios

- Clave primaria: `id`
- Filas: 9
- Relaciones implícitas: `id_user` ↝ `auth.user` (100.0 % con padre)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `nombre_completo` | `character varying(255)` | no | _Por documentar_ | Nombre de persona |
| 3 | `email` | `character varying(255)` | no | _Por documentar_ | única Contacto |
| 4 | `telefono` | `character varying(50)` | sí | _Por documentar_ | Contacto |
| 5 | `cargo` | `character varying(100)` | no | _Por documentar_ |  |
| 6 | `especialidad` | `character varying(100)` | sí | _Por documentar_ |  |
| 7 | `tipo_contrato` | `character varying(50)` | sí | _Por documentar_ |  |
| 8 | `territorial` | `character varying(100)` | sí | _Por documentar_ |  |
| 9 | `capacidad_maxima` | `integer` | sí | _Por documentar_ |  |
| 10 | `estado` | `character varying(50)` | sí | _Por documentar_ |  |
| 11 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 13 | `firma_url` | `text` | sí | URL del archivo de firma mecánica/digital del profesional |  |
| 14 | `id_user` | `uuid` | sí | _Por documentar_ | ↝auth.user.id_user |

## entidades_remision

Tabla para gestionar las entidades de remisión en procesos disciplinarios

- Clave primaria: `id`
- Filas: 9

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `nombre` | `character varying(255)` | no | Nombre de la entidad de remisión |  |
| 3 | `correo` | `character varying(255)` | no | Correo electrónico de la entidad de remisión |  |
| 4 | `activo` | `boolean` | sí | Indica si la entidad está activa |  |
| 5 | `created_at` | `timestamp without time zone` | no | Fecha de creación del registro |  |
| 6 | `updated_at` | `timestamp without time zone` | no | Fecha de última actualización del registro |  |

## evidence

Evidencias y documentos adjuntos a los procesos

- Clave primaria: `id`
- Filas: 70
- Referencia a: `processId` → `internal_disciplinary_control.disciplinary_processes` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `url` | `text` | no | _Por documentar_ |  |
| 3 | `filename` | `character varying(255)` | sí | _Por documentar_ |  |
| 4 | `description` | `text` | sí | _Por documentar_ |  |
| 5 | `fileType` | `character varying(100)` | sí | Tipo de archivo: pdf, docx, jpg, etc. |  |
| 6 | `fileSize` | `integer` | sí | _Por documentar_ |  |
| 7 | `createdAt` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 8 | `processId` | `uuid` | no | _Por documentar_ | FK→internal_disciplinary_control.disciplinary_processes.id |
| 9 | `nombreDocumento` | `character varying(255)` | sí | _Por documentar_ |  |
| 10 | `tipoDocumento` | `character varying(50)` | sí | _Por documentar_ |  |
| 11 | `etapa` | `character varying(100)` | sí | _Por documentar_ |  |
| 12 | `usuarioCarga` | `character varying(255)` | sí | _Por documentar_ |  |
| 13 | `categoria` | `character varying(50)` | sí | _Por documentar_ |  |
| 14 | `destinatario` | `character varying(255)` | sí | _Por documentar_ |  |
| 15 | `asunto` | `character varying(255)` | sí | _Por documentar_ |  |
| 16 | `participantes` | `integer` | sí | _Por documentar_ |  |
| 17 | `archivoUrl` | `character varying` | sí | _Por documentar_ |  |
| 18 | `nombreArchivo` | `character varying` | sí | _Por documentar_ |  |
| 19 | `tipo` | `character varying` | sí | _Por documentar_ |  |

## expediente_compartido

Tabla para gestionar los enlaces compartidos de expedientes disciplinarios

- Clave primaria: `id`
- Filas: 95

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `token_acceso` | `character varying(255)` | no | Token único de acceso al enlace compartido | única Credencial de acceso |
| 3 | `proceso_id` | `uuid` | no | ID del proceso disciplinario que se comparte |  |
| 4 | `tipo_compartido` | `internal_disciplinary_control.tipo_compartido` | no | Tipo de compartido: LINK, QR o EMAIL |  |
| 5 | `estado` | `internal_disciplinary_control.estado_compartido` | no | _Por documentar_ |  |
| 6 | `requiere_clave` | `boolean` | sí | Indica si el enlace requiere clave de acceso |  |
| 7 | `clave_hash` | `character varying(255)` | sí | Hash de la clave de acceso (bcrypt) |  |
| 8 | `tiempo_expiracion_horas` | `integer` | sí | Tiempo de expiración en horas |  |
| 9 | `fecha_expiracion` | `timestamp without time zone` | sí | Fecha en que expira el enlace |  |
| 10 | `email_destinatario` | `character varying(255)` | sí | Email del destinatario (para tipo EMAIL) | Contacto |
| 11 | `mensaje_adicional` | `text` | sí | Mensaje adicional incluido en el correo |  |
| 12 | `creado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 13 | `contador_accesos` | `integer` | sí | _Por documentar_ |  |
| 14 | `ultimo_acceso` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 15 | `ip_ultimo_acceso` | `character varying(45)` | sí | _Por documentar_ | Identificador en línea (IP) |
| 16 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 17 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 18 | `es_publico` | `boolean` | sí | Indica si el enlace es público (sin autenticación) |  |
| 19 | `permite_descarga` | `boolean` | sí | _Por documentar_ |  |

## legal_autos

Autos legales generados en los procesos

- Clave primaria: `id`
- Filas: 218
- Referencia a: `processId` → `internal_disciplinary_control.disciplinary_processes` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `processId` | `uuid` | no | _Por documentar_ | FK→internal_disciplinary_control.disciplinary_processes.id |
| 3 | `tipo` | `character varying(50)` | no | Tipos: AUTO_APERTURA, AUTO_PRUEBAS, AUTO_CIERRE, etc. |  |
| 4 | `contenido` | `text` | no | _Por documentar_ |  |
| 5 | `estado` | `character varying(50)` | sí | Estados: BORRADOR, EN_REVISION, APROBADO, RECHAZADO, NOTIFICADO |  |
| 6 | `firmaUrl` | `text` | sí | _Por documentar_ |  |
| 7 | `comentarios` | `text` | sí | _Por documentar_ |  |
| 8 | `aprobadoPorId` | `uuid` | sí | _Por documentar_ |  |
| 9 | `createdAt` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 10 | `updatedAt` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 11 | `notificationDate` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 12 | `notificationEvidence` | `text` | sí | _Por documentar_ |  |
| 13 | `rejection_comments` | `text` | sí | _Por documentar_ |  |
| 14 | `currentVersion` | `integer` | sí | _Por documentar_ |  |
| 15 | `numero` | `character varying(150)` | sí | _Por documentar_ |  |
| 16 | `documentUrl` | `text` | sí | _Por documentar_ |  |
| 17 | `documentName` | `text` | sí | _Por documentar_ |  |
| 18 | `documentType` | `text` | sí | _Por documentar_ |  |
| 19 | `documentSize` | `integer` | sí | _Por documentar_ |  |
| 20 | `etapaDestino` | `character varying(50)` | sí | _Por documentar_ |  |
| 21 | `prorrogaMeses` | `integer` | sí | _Por documentar_ |  |
| 22 | `fechaVencimientoAnterior` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 23 | `fechaVencimientoNueva` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 24 | `autoConfigurationId` | `uuid` | sí | _Por documentar_ |  |
| 25 | `etapaPreviaAprobacion` | `character varying(100)` | sí | _Por documentar_ |  |
| 26 | `rejectionDocumentUrl` | `text` | sí | _Por documentar_ |  |
| 27 | `rejectionDocumentName` | `text` | sí | _Por documentar_ |  |
| 28 | `radicador_asignado_id` | `uuid` | sí | ID del usuario radicador asignado a este auto |  |
| 29 | `entidad_destino` | `character varying(255)` | sí | _Por documentar_ |  |
| 30 | `entidad_destino_email` | `character varying(255)` | sí | _Por documentar_ |  |

## oficios_configuration

_Por documentar._

- Clave primaria: `id`
- Filas: 14

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `tipo` | `character varying(100)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(200)` | no | _Por documentar_ |  |
| 4 | `codigo` | `character varying(50)` | sí | _Por documentar_ |  |
| 5 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 6 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 7 | `plantilla` | `text` | sí | _Por documentar_ |  |
| 8 | `nombre_plantilla` | `character varying(255)` | sí | _Por documentar_ |  |
| 9 | `descripcion_plantilla` | `text` | sí | _Por documentar_ |  |
| 10 | `version_plantilla` | `character varying(50)` | sí | _Por documentar_ |  |
| 11 | `estado_plantilla` | `character varying(50)` | sí | _Por documentar_ |  |
| 12 | `stage` | `character varying(50)` | sí | _Por documentar_ |  |
| 13 | `orden` | `integer` | sí | _Por documentar_ |  |
| 14 | `createdAt` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 15 | `updatedAt` | `timestamp with time zone` | sí | _Por documentar_ |  |

## plantilla_auto

_Por documentar._

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `htmlContent` | `text` | no | _Por documentar_ |  |
| 3 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `nombre` | `character varying(100)` | sí | _Por documentar_ |  |
| 5 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 6 | `createdAt` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 7 | `updatedAt` | `timestamp with time zone` | sí | _Por documentar_ |  |

## reglas_alerta

_Por documentar._

- Clave primaria: `id`
- Filas: 7

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `nombre` | `character varying(200)` | no | _Por documentar_ | única |
| 3 | `dias_anticipacion` | `integer` | no | _Por documentar_ |  |
| 4 | `activa` | `boolean` | no | _Por documentar_ |  |
| 5 | `enviar_email` | `boolean` | no | _Por documentar_ |  |
| 6 | `mostrar_panel` | `boolean` | no | _Por documentar_ |  |
| 7 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 8 | `creado_por_id` | `uuid` | sí | _Por documentar_ |  |
| 9 | `fecha_creacion` | `timestamp without time zone` | no | _Por documentar_ |  |
| 10 | `fecha_actualizacion` | `timestamp without time zone` | no | _Por documentar_ |  |

## sequences

Tabla para gestionar secuencias de radicados

- Clave primaria: `name`
- Filas: 7

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `name` | `character varying(255)` | no | _Por documentar_ | PK |
| 2 | `currentValue` | `integer` | sí | _Por documentar_ |  |
| 3 | `updatedAt` | `timestamp without time zone` | sí | _Por documentar_ |  |

## stage_configuration

Configuración de días hábiles por etapa procesal

- Clave primaria: `id`
- Filas: 7

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `etapa` | `character varying(255)` | no | _Por documentar_ |  |
| 3 | `diasHabiles` | `integer` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 6 | `createdAt` | `timestamp without time zone` | no | Fecha de creación del registro |  |
| 7 | `updatedAt` | `timestamp without time zone` | no | Fecha de última actualización del registro |  |
| 8 | `color` | `character varying(50)` | sí | _Por documentar_ |  |
| 9 | `orden` | `integer` | sí | _Por documentar_ |  |

## system_configuration

Configuración global del sistema disciplinario

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `roleCapacities` | `jsonb` | sí | _Por documentar_ |  |
| 3 | `notificationSettings` | `jsonb` | sí | _Por documentar_ |  |
| 4 | `alertSettings` | `jsonb` | sí | _Por documentar_ |  |
| 5 | `securitySettings` | `jsonb` | sí | _Por documentar_ |  |
| 6 | `documentTemplates` | `jsonb` | sí | _Por documentar_ |  |

## terminos_procesales

_Por documentar._

- Clave primaria: `id`
- Filas: 23

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `proceso_id` | `uuid` | no | _Por documentar_ |  |
| 3 | `numero_proceso` | `character varying(20)` | sí | _Por documentar_ |  |
| 4 | `actuacion` | `character varying(200)` | no | _Por documentar_ |  |
| 5 | `responsable_id` | `uuid` | no | _Por documentar_ |  |
| 6 | `responsable_nombre` | `character varying(200)` | no | _Por documentar_ |  |
| 7 | `email_responsable` | `character varying(100)` | no | _Por documentar_ | Contacto |
| 8 | `fecha_inicio` | `date` | no | _Por documentar_ |  |
| 9 | `dias_habiles` | `integer` | no | _Por documentar_ |  |
| 10 | `fecha_vencimiento` | `date` | no | _Por documentar_ |  |
| 11 | `dias_restantes` | `integer` | no | _Por documentar_ |  |
| 12 | `estado` | `internal_disciplinary_control.termino_estado_enum` | no | _Por documentar_ |  |
| 13 | `alerta_enviada` | `boolean` | no | _Por documentar_ |  |
| 14 | `fecha_cumplimiento` | `date` | sí | _Por documentar_ |  |
| 15 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 16 | `creado_por_id` | `uuid` | no | _Por documentar_ |  |
| 17 | `fecha_creacion` | `timestamp without time zone` | no | _Por documentar_ |  |
| 18 | `fecha_actualizacion` | `timestamp without time zone` | no | _Por documentar_ |  |

## tipos_remision

Tabla para gestionar los tipos de remisión en procesos disciplinarios

- Clave primaria: `id`
- Filas: 6

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(100)` | no | Código único del tipo de remisión | única |
| 3 | `nombre` | `character varying(255)` | no | Nombre del tipo de remisión |  |
| 4 | `descripcion` | `text` | sí | Descripción del tipo de remisión |  |
| 5 | `activo` | `boolean` | sí | Indica si el tipo está activo |  |
| 6 | `orden` | `integer` | sí | Orden de visualización del tipo |  |
| 7 | `created_at` | `timestamp without time zone` | no | Fecha de creación del registro |  |
| 8 | `updated_at` | `timestamp without time zone` | no | Fecha de última actualización del registro |  |
