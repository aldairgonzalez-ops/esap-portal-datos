# Requerimientos de organismos de control (`requerimientos_oc`)

Requerimientos de los organismos de control a la ESAP: radicación y cálculo de vencimientos, solicitudes de insumos a otras áreas, bitácora de acciones, hallazgos con sus avances y catálogo de organismos.

6 tablas · 0 vistas · 94 columnas · 32 filas · 2 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`avances_hallazgo`](#avances_hallazgo) | Tabla | 0 | Reportes de avance de los hallazgos de los organismos de control. Un registro por reporte de un hallazgo de requerimientos_oc.hallazgos, con la fecha, el porcentaje de avance, la descripción, los documentos de soporte, el reporte a SIRECI y el funcionario que lo reportó. |
| [`cat_organismos_control`](#cat_organismos_control) | Tabla | 25 | Catálogo maestro de organismos de control que pueden generar requerimientos a la ESAP |
| [`hallazgos`](#hallazgos) | Tabla | 2 | Hallazgos de auditoría de los organismos de control y su plan de mejoramiento. Un registro por hallazgo, asociado a un requerimiento de requerimientos_oc.requerimientos, con su código, número interno, tipo (administrativo, disciplinario, fiscal o penal), causa, efecto, acción correctiva, responsables, indicador, avance y periodicidad de reporte; sus avances se registran en requerimientos_oc.avances_hallazgo. Su estado pasa por abierto, en curso, en revisión, cerrado o rechazado. |
| [`historial_requerimientos`](#historial_requerimientos) | Tabla | 0 | Bitácora de acciones sobre los requerimientos de los organismos de control. Un registro por acción (creación, asignación, delegación, cambio de estado, respuesta o cierre) sobre un requerimiento de requerimientos_oc.requerimientos, con su descripción, los estados anterior y nuevo, el usuario, su área y la fecha; los cambios de estado se registran automáticamente. |
| [`requerimientos`](#requerimientos) | Tabla | 5 | Gestión de requerimientos de órganos de control con radicado automático y cálculo de vencimiento |
| [`solicitudes_insumos`](#solicitudes_insumos) | Tabla | 0 | Solicitudes de insumos que se delegan a otras áreas para responder los requerimientos de los organismos de control. Un registro por solicitud, asociada a un requerimiento de requerimientos_oc.requerimientos, con el área y el funcionario destinatarios, los documentos solicitados, los plazos, la respuesta y los documentos entregados. Su estado pasa por pendiente, en proceso, entregado, rechazado o vencido. |

## avances_hallazgo

Reportes de avance de los hallazgos de los organismos de control. Un registro por reporte de un hallazgo de requerimientos_oc.hallazgos, con la fecha, el porcentaje de avance, la descripción, los documentos de soporte, el reporte a SIRECI y el funcionario que lo reportó.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `hallazgo_id` → `requerimientos_oc.hallazgos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla avances_hallazgo. Se genera automáticamente. | PK |
| 2 | `hallazgo_id` | `uuid` | no | Referencia al registro de requerimientos_oc.hallazgos (id). | FK→requerimientos_oc.hallazgos.id |
| 3 | `fecha_reporte` | `timestamp without time zone` | sí | Fecha y hora del reporte de avance del hallazgo. |  |
| 4 | `porcentaje_avance` | `integer` | sí | Porcentaje de avance reportado para el hallazgo (0 a 100). |  |
| 5 | `descripcion_avance` | `text` | no | Descripción del avance reportado. |  |
| 6 | `documentos_adjuntos_urls` | `text[]` | sí | Lista de URL de los documentos que soportan el avance. |  |
| 7 | `reportado_a_sireci` | `boolean` | sí | Indica si el avance se reportó a SIRECI. |  |
| 8 | `fecha_reporte_sireci` | `timestamp without time zone` | sí | Fecha y hora del reporte del avance a SIRECI. |  |
| 9 | `reportado_por` | `character varying(150)` | sí | Funcionario que reportó el avance. |  |
| 10 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |

## cat_organismos_control

Catálogo maestro de organismos de control que pueden generar requerimientos a la ESAP

- Clave primaria: `id`
- Filas: 25

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla cat_organismos_control. Se genera automáticamente. | PK |
| 2 | `nombre` | `character varying(255)` | no | Nombre del organismo de control. | única |
| 3 | `sigla` | `character varying(50)` | no | Sigla del organismo de control. |  |
| 4 | `tipo` | `character varying(50)` | no | Tipo de organismo de control. Valores: CONTRALORIA, PROCURADURIA, MINISTERIO, SUPERINTENDENCIA, OTROS. |  |
| 5 | `nivel` | `character varying(50)` | no | Nivel territorial del organismo de control. Valores: NACIONAL, DEPARTAMENTAL, MUNICIPAL. |  |
| 6 | `activo` | `boolean` | sí | Indica si el organismo de control está activo. |  |
| 7 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 8 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## hallazgos

Hallazgos de auditoría de los organismos de control y su plan de mejoramiento. Un registro por hallazgo, asociado a un requerimiento de requerimientos_oc.requerimientos, con su código, número interno, tipo (administrativo, disciplinario, fiscal o penal), causa, efecto, acción correctiva, responsables, indicador, avance y periodicidad de reporte; sus avances se registran en requerimientos_oc.avances_hallazgo. Su estado pasa por abierto, en curso, en revisión, cerrado o rechazado.

- Clave primaria: `id`
- Filas: 2
- Referencia a: `requerimiento_id` → `requerimientos_oc.requerimientos` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla hallazgos. Se genera automáticamente. | PK |
| 2 | `requerimiento_id` | `uuid` | sí | Referencia al registro de requerimientos_oc.requerimientos (id). | FK→requerimientos_oc.requerimientos.id |
| 3 | `codigo_hallazgo` | `character varying(50)` | no | Código único del hallazgo asignado por el organismo de control. | única |
| 4 | `numero_interno` | `character varying(50)` | sí | Número interno del hallazgo en la ESAP. Si no se informa, lo genera un trigger con el formato HAL-ESAP-<año>-<consecutivo de 4 dígitos>; codigo_hallazgo es el código del organismo de control. |  |
| 5 | `tipo_hallazgo` | `character varying(30)` | sí | Tipo de hallazgo según su incidencia. Valores permitidos: ADMINISTRATIVO, DISCIPLINARIO, FISCAL, PENAL. Por defecto, ADMINISTRATIVO. |  |
| 6 | `titulo` | `character varying(300)` | no | Título del hallazgo. |  |
| 7 | `descripcion` | `text` | no | Descripción del hallazgo. |  |
| 8 | `causa_raiz` | `text` | sí | Causa raíz identificada para el hallazgo. |  |
| 9 | `efecto` | `text` | sí | Efecto o consecuencia del hallazgo. |  |
| 10 | `area_responsable` | `character varying(100)` | sí | Nombre del área responsable de atender el hallazgo, registrado como texto; no está enlazado a un catálogo. |  |
| 11 | `funcionario_responsable` | `character varying(150)` | sí | Funcionario responsable de atender el hallazgo. |  |
| 12 | `accion_correctiva` | `text` | no | Acción correctiva definida para subsanar el hallazgo. |  |
| 13 | `fecha_compromiso` | `date` | no | Fecha de compromiso para la atención del hallazgo. |  |
| 14 | `indicador_cumplimiento` | `text` | sí | Indicador con el que se mide el cumplimiento de la acción correctiva. |  |
| 15 | `meta_indicador` | `character varying(100)` | sí | Meta del indicador de cumplimiento. |  |
| 16 | `estado` | `character varying(30)` | sí | Estado del hallazgo (ABIERTO, EN_CURSO, EN_REVISION, CERRADO o RECHAZADO). |  |
| 17 | `porcentaje_avance` | `integer` | sí | Porcentaje de avance de la acción correctiva (0 a 100). Por defecto, 0. |  |
| 18 | `fecha_ultimo_reporte` | `timestamp without time zone` | sí | Fecha y hora del último reporte de avance del hallazgo. |  |
| 19 | `fecha_proximo_reporte` | `date` | sí | Fecha del próximo reporte de avance del hallazgo. |  |
| 20 | `periodicidad_reporte` | `character varying(20)` | sí | Periodicidad con que se reporta el avance del hallazgo. Valores permitidos: ANUAL, MENSUAL, SEMESTRAL, TRIMESTRAL. Por defecto, SEMESTRAL. |  |
| 21 | `documento_plan_url` | `character varying(500)` | sí | URL del documento del plan de mejoramiento asociado al hallazgo. |  |
| 22 | `documentos_evidencia_urls` | `text[]` | sí | Lista de URL de los documentos de evidencia del hallazgo. |  |
| 23 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 24 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 25 | `created_by` | `character varying(150)` | sí | Usuario que creó el registro. |  |

## historial_requerimientos

Bitácora de acciones sobre los requerimientos de los organismos de control. Un registro por acción (creación, asignación, delegación, cambio de estado, respuesta o cierre) sobre un requerimiento de requerimientos_oc.requerimientos, con su descripción, los estados anterior y nuevo, el usuario, su área y la fecha; los cambios de estado se registran automáticamente.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `requerimiento_id` → `requerimientos_oc.requerimientos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla historial_requerimientos. Se genera automáticamente. | PK |
| 2 | `requerimiento_id` | `uuid` | no | Referencia al registro de requerimientos_oc.requerimientos (id). | FK→requerimientos_oc.requerimientos.id |
| 3 | `accion` | `character varying(50)` | no | Acción registrada sobre el requerimiento: CREACION, ASIGNACION, DELEGACION, CAMBIO_ESTADO, RESPUESTA o CIERRE. El trigger registra CAMBIO_ESTADO cuando cambia el estado. |  |
| 4 | `descripcion` | `text` | sí | Descripción de la acción registrada en el historial del requerimiento. |  |
| 5 | `estado_anterior` | `character varying(30)` | sí | Estado del requerimiento antes de la acción. |  |
| 6 | `estado_nuevo` | `character varying(30)` | sí | Estado del requerimiento después de la acción. |  |
| 7 | `usuario_nombre` | `character varying(150)` | sí | Nombre del usuario que realizó la acción. Queda vacío cuando la acción la registra el trigger de cambio de estado. |  |
| 8 | `area_usuario` | `character varying(100)` | sí | Área a la que pertenece el usuario que realizó la acción. |  |
| 9 | `fecha` | `timestamp without time zone` | sí | Fecha y hora en que se registró la acción. Por defecto, la fecha y hora de inserción. |  |

## requerimientos

Gestión de requerimientos de órganos de control con radicado automático y cálculo de vencimiento

- Clave primaria: `id`
- Filas: 5
- Referencia a: `entidad_id` → `requerimientos_oc.cat_organismos_control` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla requerimientos. Se genera automáticamente. | PK |
| 2 | `radicado_externo` | `character varying(50)` | no | Número de radicado asignado por el organismo de control al requerimiento. |  |
| 3 | `radicado_interno` | `character varying(20)` | no | Formato: OC-YYYY-NNNNN (generado automáticamente) | única |
| 4 | `entidad_id` | `integer` | no | Referencia al registro de requerimientos_oc.cat_organismos_control (id). | FK→requerimientos_oc.cat_organismos_control.id |
| 5 | `asunto` | `text` | no | Asunto del requerimiento. |  |
| 6 | `tipo_requerimiento` | `character varying(50)` | no | Tipo de requerimiento del órgano de control. Valores permitidos: INFORMACION, AUDITORIA, HALLAZGO, AJUSTE. |  |
| 7 | `fecha_recepcion` | `date` | no | Fecha de recepción del requerimiento del órgano de control. |  |
| 8 | `fecha_vencimiento` | `date` | no | Calculada automáticamente sumando días hábiles (sin sábados/domingos) a fecha_recepcion |  |
| 9 | `estado` | `character varying(50)` | no | Estado del requerimiento. Valores permitidos: EN_PREPARACION, EN_REVISION, APROBADO, ENVIADO, CERRADO; valor por defecto EN_PREPARACION. |  |
| 10 | `prioridad_calculada` | `character varying(20)` | sí | Calculada dinámicamente basada en días restantes y tipo de requerimiento |  |
| 11 | `archivo_adjunto_url` | `character varying(500)` | sí | URL del archivo del requerimiento recibido. |  |
| 12 | `usuario_asignado_id` | `integer` | sí | Identificador del usuario asignado al requerimiento; referencia a auth.personas. |  |
| 13 | `auditoria_created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. Por defecto, la fecha y hora de inserción. |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 15 | `unidad_tiempo` | `character varying(20)` | sí | Unidad de tiempo del plazo otorgado. Valores permitidos: DIAS_CALENDARIO, DIAS_HABILES, HORAS. Por defecto, DIAS_HABILES. |  |
| 16 | `dias_plazo_otorgado` | `integer` | sí | Plazo otorgado para responder el requerimiento. Por defecto, 15. |  |
| 17 | `referencia_externa` | `character varying(100)` | sí | Referencia externa del requerimiento. |  |
| 18 | `descripcion` | `text` | sí | Descripción del requerimiento. |  |
| 19 | `funcionario_responsable` | `character varying(150)` | sí | Funcionario responsable de atender el requerimiento. |  |
| 20 | `area_responsable` | `character varying(100)` | sí | Nombre del área responsable de atender el requerimiento, registrado como texto; no está enlazado a un catálogo. |  |
| 21 | `fecha_respuesta` | `timestamp without time zone` | sí | Fecha y hora de la respuesta al requerimiento. |  |
| 22 | `oficio_respuesta_url` | `character varying(500)` | sí | URL del oficio de respuesta al requerimiento. |  |
| 23 | `acuse_recibo_url` | `character varying(500)` | sí | URL del acuse de recibo de la respuesta por parte del organismo de control. |  |
| 24 | `observaciones` | `text` | sí | Observaciones sobre el requerimiento. |  |
| 25 | `created_by` | `character varying(150)` | sí | Usuario que creó el registro. |  |

## solicitudes_insumos

Solicitudes de insumos que se delegan a otras áreas para responder los requerimientos de los organismos de control. Un registro por solicitud, asociada a un requerimiento de requerimientos_oc.requerimientos, con el área y el funcionario destinatarios, los documentos solicitados, los plazos, la respuesta y los documentos entregados. Su estado pasa por pendiente, en proceso, entregado, rechazado o vencido.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `requerimiento_id` → `requerimientos_oc.requerimientos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla solicitudes_insumos. Se genera automáticamente. | PK |
| 2 | `requerimiento_id` | `uuid` | no | Referencia al registro de requerimientos_oc.requerimientos (id). | FK→requerimientos_oc.requerimientos.id |
| 3 | `area_destino` | `character varying(100)` | no | Área a la que se solicitan los insumos para responder el requerimiento. |  |
| 4 | `funcionario_destino` | `character varying(150)` | sí | Nombre del funcionario al que se dirige la solicitud de insumos. |  |
| 5 | `email_destino` | `character varying(150)` | sí | Correo electrónico del funcionario al que se dirige la solicitud. | Contacto |
| 6 | `descripcion_solicitud` | `text` | no | Descripción de los insumos solicitados. |  |
| 7 | `documentos_solicitados` | `text` | sí | Relación de documentos solicitados al área, en texto. |  |
| 8 | `fecha_solicitud` | `timestamp without time zone` | sí | Fecha y hora de la solicitud de insumos. |  |
| 9 | `fecha_vencimiento` | `timestamp without time zone` | no | Fecha y hora de vencimiento de la solicitud de insumos. |  |
| 10 | `fecha_respuesta` | `timestamp without time zone` | sí | Fecha y hora de la respuesta a la solicitud de insumos. |  |
| 11 | `estado` | `character varying(20)` | sí | Estado de la solicitud de insumos (PENDIENTE, EN_PROCESO, ENTREGADO, RECHAZADO o VENCIDO). |  |
| 12 | `documentos_entregados_urls` | `text[]` | sí | Lista de URL de los documentos entregados por el área. |  |
| 13 | `comentario_respuesta` | `text` | sí | Comentario del área al responder la solicitud. |  |
| 14 | `solicitado_por` | `character varying(150)` | sí | Usuario que realizó la solicitud. |  |
| 15 | `respondido_por` | `character varying(150)` | sí | Funcionario que respondió la solicitud. |  |
| 16 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 17 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
