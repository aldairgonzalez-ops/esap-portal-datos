# Control disciplinario interno (`internal_disciplinary_control`)

Control disciplinario interno: noticias disciplinarias, procesos con sus actuaciones, autos y versiones, términos procesales y días festivos, tareas, evidencias, alertas, reasignaciones y catálogo de conductas.

26 tablas · 0 vistas · 358 columnas · 1.181 filas · 4 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`actas_configuration`](#actas_configuration) | Tabla | 8 | Tabla de configuración paramétrica de actas para el módulo disciplinario |
| [`alertas_enviadas`](#alertas_enviadas) | Tabla | 117 | Alertas enviadas en el control disciplinario sobre términos procesales y autos. Un registro por alerta, asociada a un término, a una regla de alerta o a un auto, con su tipo (correo, visual o sistema), destinatario, asunto, mensaje, estado del envío (pendiente, enviada o error) y fechas de envío y lectura. |
| [`auto_versions`](#auto_versions) | Tabla | 244 | Historial de versiones de los autos legales del proceso disciplinario. Un registro por versión de un auto (internal_disciplinary_control.legal_autos), con el contenido del auto, número de versión, motivo del cambio, archivo adjunto, autor y fecha. |
| [`autos_configuration`](#autos_configuration) | Tabla | 38 | Configuración de los tipos de auto del proceso disciplinario. Un registro por tipo de auto, con su nombre, estado, orden, etapa del proceso a la que corresponde y los datos de su plantilla (archivo, nombre, descripción, versión y estado). |
| [`dias_festivos`](#dias_festivos) | Tabla | 19 | Días festivos que se tienen en cuenta en el control disciplinario. Un registro por fecha festiva, con su descripción, tipo (nacional, regional o institucional), territorio cuando es regional y estado activo. |
| [`disciplinary_behaviors`](#disciplinary_behaviors) | Tabla | 17 | Catálogo parametrizable de conductas indisciplinarias |
| [`disciplinary_news`](#disciplinary_news) | Tabla | 35 | Noticias disciplinarias recibidas |
| [`disciplinary_news_processes`](#disciplinary_news_processes) | Tabla | 9 | Tabla puente para asociar noticias disciplinarias con procesos disciplinarios |
| [`disciplinary_process_actuaciones`](#disciplinary_process_actuaciones) | Tabla | 148 | Actuaciones registradas en los procesos disciplinarios. Un registro por actuación, asociada a un proceso y, si aplica, a una noticia disciplinaria, con su tipo, etapa, descripción, responsable, fecha y observaciones. |
| [`disciplinary_process_notes`](#disciplinary_process_notes) | Tabla | 14 | Notas de los procesos disciplinarios. Un registro por nota, asociada a un proceso, con su texto y la etapa del proceso a la que corresponde. |
| [`disciplinary_process_reassignment_requests`](#disciplinary_process_reassignment_requests) | Tabla | 24 | Tabla para solicitudes de reasignación de procesos disciplinarios |
| [`disciplinary_process_tasks`](#disciplinary_process_tasks) | Tabla | 15 | Tareas de los procesos disciplinarios. Un registro por tarea, asociada a un proceso, con título, descripción, prioridad (alta, media o baja), etapa, responsable, fecha de vencimiento y si está completada. |
| [`disciplinary_processes`](#disciplinary_processes) | Tabla | 26 | Procesos disciplinarios activos |
| [`disciplinary_professional`](#disciplinary_professional) | Tabla | 9 | Profesionales (abogados) asignados a procesos disciplinarios |
| [`entidades_remision`](#entidades_remision) | Tabla | 9 | Tabla para gestionar las entidades de remisión en procesos disciplinarios |
| [`evidence`](#evidence) | Tabla | 70 | Evidencias y documentos adjuntos a los procesos |
| [`expediente_compartido`](#expediente_compartido) | Tabla | 95 | Tabla para gestionar los enlaces compartidos de expedientes disciplinarios |
| [`legal_autos`](#legal_autos) | Tabla | 218 | Autos legales generados en los procesos |
| [`oficios_configuration`](#oficios_configuration) | Tabla | 14 | Configuración de los tipos de oficio del proceso disciplinario. Un registro por oficio, con su tipo, nombre, código, descripción, estado, etapa del proceso, orden y los datos de su plantilla (archivo, nombre, descripción, versión y estado). |
| [`plantilla_auto`](#plantilla_auto) | Tabla | 1 | Plantillas en HTML para la elaboración de autos del proceso disciplinario. Un registro por plantilla, con su nombre, descripción, contenido y estado (activo o inactivo). |
| [`reglas_alerta`](#reglas_alerta) | Tabla | 7 | Reglas de alerta de vencimiento de términos procesales. Un registro por regla, con su nombre, días hábiles de anticipación, canales (correo y panel), descripción y estado activo; las alertas generadas se registran en internal_disciplinary_control.alertas_enviadas. |
| [`sequences`](#sequences) | Tabla | 7 | Tabla para gestionar secuencias de radicados |
| [`stage_configuration`](#stage_configuration) | Tabla | 7 | Configuración de días hábiles por etapa procesal |
| [`system_configuration`](#system_configuration) | Tabla | 1 | Configuración global del sistema disciplinario |
| [`terminos_procesales`](#terminos_procesales) | Tabla | 23 | Términos procesales con su control de vencimiento. Un registro por término de una actuación de un proceso, con el responsable, fecha de inicio, días hábiles, fecha de vencimiento, días restantes, estado (pendiente, próximo a vencer, vencido o cumplido), envío de alerta y fecha de cumplimiento. |
| [`tipos_remision`](#tipos_remision) | Tabla | 6 | Tabla para gestionar los tipos de remisión en procesos disciplinarios |

## actas_configuration

Tabla de configuración paramétrica de actas para el módulo disciplinario

- Clave primaria: `id`
- Filas: 8

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla actas_configuration. Se genera automáticamente. | PK |
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
| 14 | `createdat` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 15 | `updatedat` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## alertas_enviadas

Alertas enviadas en el control disciplinario sobre términos procesales y autos. Un registro por alerta, asociada a un término, a una regla de alerta o a un auto, con su tipo (correo, visual o sistema), destinatario, asunto, mensaje, estado del envío (pendiente, enviada o error) y fechas de envío y lectura.

- Clave primaria: `id`
- Filas: 117
- Referencia a: `auto_id` → `internal_disciplinary_control.legal_autos` (0..1 → 0..1); `regla_alerta_id` → `internal_disciplinary_control.reglas_alerta` (0..1 → 0..1); `termino_id` → `internal_disciplinary_control.terminos_procesales` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla alertas_enviadas. Se genera automáticamente. | PK |
| 2 | `termino_id` | `uuid` | sí | Referencia al registro de internal_disciplinary_control.terminos_procesales (id). | FK→internal_disciplinary_control.terminos_procesales.id |
| 3 | `regla_alerta_id` | `uuid` | sí | Referencia al registro de internal_disciplinary_control.reglas_alerta (id). | FK→internal_disciplinary_control.reglas_alerta.id |
| 4 | `tipo` | `internal_disciplinary_control.tipo_alerta_enum` | no | Tipo de alerta enviada (email, visual o sistema). |  |
| 5 | `destinatario` | `character varying(200)` | no | Destinatario de la alerta, en texto; el contenido depende del origen: correo del responsable del término en las alertas automáticas de términos, nombre del abogado asignado en la alerta de asignación de proceso e identificador del abogado asignado en las alertas de autos y prórrogas. |  |
| 6 | `asunto` | `character varying(500)` | sí | Asunto de la alerta enviada. |  |
| 7 | `mensaje` | `text` | sí | Texto del mensaje de la alerta enviada. |  |
| 8 | `estado` | `internal_disciplinary_control.estado_alerta_enum` | no | Estado del envío de la alerta (pendiente, enviada o error). |  |
| 9 | `fecha_envio` | `timestamp without time zone` | no | Fecha y hora en que se envió la alerta. |  |
| 10 | `fecha_lectura` | `timestamp without time zone` | sí | Fecha y hora en que el destinatario leyó la alerta; aplica a las alertas visuales. |  |
| 11 | `error_mensaje` | `text` | sí | Mensaje de error del envío de la alerta; se diligencia cuando el estado es error. |  |
| 12 | `creado_por_id` | `uuid` | sí | Identificador de quien creó la alerta: vacío en las alertas automáticas de términos; en las alertas de autos, el identificador del usuario que aprueba o del abogado asignado. |  |
| 13 | `fecha_creacion` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 14 | `auto_id` | `uuid` | sí | Referencia al registro de internal_disciplinary_control.legal_autos (id). | FK→internal_disciplinary_control.legal_autos.id |

## auto_versions

Historial de versiones de los autos legales del proceso disciplinario. Un registro por versión de un auto (internal_disciplinary_control.legal_autos), con el contenido del auto, número de versión, motivo del cambio, archivo adjunto, autor y fecha.

- Clave primaria: `id`
- Filas: 244

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla auto_versions. Se genera automáticamente. | PK |
| 2 | `autoId` | `uuid` | sí | Identificador del auto al que pertenece la versión (internal_disciplinary_control.legal_autos). La relación está mapeada en la entidad y el DDL de referencia del repositorio declara la FK con borrado en cascada. |  |
| 3 | `contenido` | `text` | no | Contenido del auto en esta versión, en HTML (texto enriquecido): copia del contenido del auto al momento de la versión. |  |
| 4 | `versionNumber` | `integer` | no | Número de la versión del auto. |  |
| 5 | `createdBy` | `uuid` | sí | Usuario que creó el registro. |  |
| 6 | `changeReason` | `text` | sí | Motivo del cambio que generó la versión del auto. |  |
| 7 | `createdAt` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `documentUrl` | `text` | sí | URL del archivo adjunto en esta versión (si existe) |  |
| 9 | `documentName` | `text` | sí | Nombre del archivo adjunto en esta versión |  |

## autos_configuration

Configuración de los tipos de auto del proceso disciplinario. Un registro por tipo de auto, con su nombre, estado, orden, etapa del proceso a la que corresponde y los datos de su plantilla (archivo, nombre, descripción, versión y estado).

- Clave primaria: no declarada
- Filas: 38

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único de la configuración de auto (UUID generado automáticamente). |  |
| 2 | `tipo` | `character varying(100)` | no | Tipo de auto configurado. |  |
| 3 | `nombre` | `character varying(200)` | no | Nombre del auto configurado. |  |
| 4 | `estado` | `character varying(50)` | no | Estado de la configuración del auto. |  |
| 5 | `plantilla` | `text` | sí | Ruta del archivo de la plantilla del auto (Word.docx,.doc,.dotx,.rtf o PDF) cargado al servicio, con la forma /uploads/plantillas-autos/<archivo>. |  |
| 6 | `orden` | `integer` | sí | Posición del auto en el listado. |  |
| 7 | `createdAt` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 8 | `updatedAt` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 9 | `stage` | `character varying(50)` | sí | Etapa del proceso disciplinario asociada al tipo de auto: RECEPCION, EVALUACION, VALORACION, INDAGACION_PREVIA, INVESTIGACION, JUZGAMIENTO o SEGUNDA_INSTANCIA; vacía si el auto está disponible para todas las etapas. En los autos de pliego de cargos se usa como etapa destino del proceso al aprobarse. |  |
| 10 | `nombre_plantilla` | `character varying(255)` | sí | Nombre de la plantilla asociada al tipo de auto |  |
| 11 | `descripcion_plantilla` | `text` | sí | Descripción de la plantilla |  |
| 12 | `version_plantilla` | `character varying(50)` | sí | Versión de la plantilla (ej: 1.0, 2.0) |  |
| 13 | `estado_plantilla` | `character varying(50)` | sí | Estado de la plantilla (activo/inactivo) |  |

## dias_festivos

Días festivos que se tienen en cuenta en el control disciplinario. Un registro por fecha festiva, con su descripción, tipo (nacional, regional o institucional), territorio cuando es regional y estado activo.

- Clave primaria: `id`
- Filas: 19

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla dias_festivos. Se genera automáticamente. | PK |
| 2 | `fecha` | `date` | no | Fecha del día festivo; única por tipo y territorio. |  |
| 3 | `descripcion` | `character varying(200)` | no | Descripción del día festivo. |  |
| 4 | `tipo` | `internal_disciplinary_control.tipo_festivo_enum` | no | Tipo de día festivo (nacional, regional o institucional). |  |
| 5 | `territorio` | `character varying(100)` | sí | Territorio al que aplica el día festivo; se diligencia solo si el tipo es regional. |  |
| 6 | `activo` | `boolean` | no | Indica si el día festivo está activo. |  |
| 7 | `creado_por_id` | `uuid` | no | Identificador de la persona que registró el día festivo. |  |
| 8 | `fecha_creacion` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `fecha_actualizacion` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

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
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla disciplinary_news. Se genera automáticamente. | PK |
| 2 | `radicado` | `character varying(255)` | no | Número de radicado único de la noticia disciplinaria, por ejemplo ND-2025-001. | única |
| 3 | `fechaRecepcion` | `timestamp without time zone` | no | Fecha y hora de recepción de la noticia disciplinaria. Por defecto, la fecha y hora de creación del registro. |  |
| 4 | `origen` | `internal_disciplinary_control.disciplinary_news_origen_enum` | sí | Origen de la noticia disciplinaria. Valores permitidos: ANONIMO, QUEJOSO, OFICIO, REMISION, POR_DETERMINAR. |  |
| 5 | `territorial` | `character varying(100)` | sí | Dirección territorial de la noticia disciplinaria, en texto obligatorio digitado en el formulario. |  |
| 6 | `dependenciaDenunciado` | `character varying(255)` | sí | Dependencia a la que pertenece el denunciado. |  |
| 7 | `denunciante` | `jsonb` | sí | Datos del denunciante en formato JSON |  |
| 8 | `disciplinable` | `jsonb` | sí | Datos del disciplinable en formato JSON |  |
| 9 | `hechos` | `text` | no | Descripción de los hechos objeto de la noticia disciplinaria. |  |
| 10 | `adjuntos` | `text[]` | sí | Archivos adjuntos de la noticia disciplinaria, como arreglo de textos con el nombre del archivo guardado en la carpeta de cargas del radicado; al remitir por competencia se agregan las rutas de los autos y evidencias del proceso. |  |
| 11 | `estado` | `internal_disciplinary_control.disciplinary_news_estado_enum` | no | Estados: RADICADA, ASIGNADA, DEVUELTA, ARCHIVADA |  |
| 12 | `observaciones` | `text` | sí | Observaciones sobre la noticia disciplinaria. |  |
| 13 | `updatedAt` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 14 | `historialAuditoria` | `jsonb` | sí | Historial de cambios de la noticia disciplinaria, como arreglo JSON; cada elemento registra id, tipo de evento (radicacion, asociacion, remision_competencia, entre otros), usuario, fecha y observaciones, y según el evento userId, userEmail, resultado o descripcion. Por defecto, arreglo vacío. |  |
| 15 | `fechaQueja` | `timestamp without time zone` | sí | Fecha reportada de la queja/hechos |  |
| 16 | `conductas` | `text[]` | sí | Conductas presuntamente indisciplinarias |  |
| 17 | `kanbanStage` | `uuid` | sí | Identificador de la etapa del tablero Kanban en que se encuentra la noticia disciplinaria (internal_disciplinary_control.stage_configuration). La noticia inicia en la etapa de orden 1 y la columna queda vacía al remitirse. |  |
| 18 | `fechaHechos` | `timestamp without time zone` | sí | Fecha en que ocurrieron los hechos. |  |
| 19 | `fechaCaducidad` | `timestamp without time zone` | sí | Fecha de caducidad de la acción disciplinaria, calculada por el sistema como fechaHechos más 5 años (Ley 734 de 2002, art. 30); se recalcula si cambia fechaHechos y queda vacía si esta no se conoce. |  |
| 20 | `proceso_asociado_id` | `uuid` | sí | Identificador del proceso disciplinario al que se asoció la noticia (internal_disciplinary_control.disciplinary_processes). La asociación también queda en disciplinary_news_processes; la columna se vacía si la noticia pierde todas sus asociaciones. |  |
| 21 | `proceso_asociado_numero` | `character varying(50)` | sí | Radicado del proceso disciplinario asociado a la noticia: copia de radicadoProceso del proceso referenciado por proceso_asociado_id. |  |
| 22 | `proceso_asociado_fecha` | `timestamp with time zone` | sí | Fecha y hora en que se asoció la noticia al proceso disciplinario. |  |
| 23 | `proceso_asociado_justificacion` | `text` | sí | Justificación de la asociación de la noticia con el proceso disciplinario. |  |
| 24 | `numero_rc` | `character varying(50)` | sí | Número RC de la remisión por competencia de la noticia, generado por el sistema con el formato RC-<año>-<número de cuatro dígitos>. |  |
| 25 | `entidad_remision` | `character varying(255)` | sí | Nombre de la entidad a la que se remite la noticia disciplinaria por competencia, digitado en la remisión. |  |
| 26 | `correo_entidad_remision` | `character varying(255)` | sí | Correo electrónico de la entidad a la que se remite la noticia. |  |
| 27 | `fecha_remision` | `timestamp with time zone` | sí | Fecha y hora de remisión de la noticia a la entidad destino. |  |
| 28 | `tipo_remision` | `character varying(100)` | sí | Código del tipo de remisión por competencia, del catálogo tipos_remision: sin-competencia (valor por defecto), factor-territorial, factor-funcional, naturaleza-falta o prelacion-competencia. |  |
| 29 | `justificacion_remision` | `text` | sí | Justificación de la remisión de la noticia disciplinaria. |  |
| 30 | `descripcion_remision` | `jsonb` | sí | Descripción de la remisión por competencia, como objeto JSON con los datos de la noticia remitida (numeroRadicado, origen, fechaRecepcion, territorial, dependenciaDenunciado, denunciante, disciplinable, hechos, conductas, fechaHechos, fechaCaducidad), más el total y los nombres de los archivos remitidos y la lista de autos y de actas y evidencias del proceso. |  |
| 31 | `radicador_id` | `uuid` | sí | Identificador del usuario que radicó la noticia disciplinaria: id_user de auth."user", tomado del formulario o del token de sesión. |  |
| 32 | `conducta_disciplinaria` | `character varying(255)` | sí | Conducta disciplinaria seleccionada para la noticia. |  |
| 33 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |

## disciplinary_news_processes

Tabla puente para asociar noticias disciplinarias con procesos disciplinarios

- Clave primaria: `id`
- Filas: 9
- Referencia a: `process_id` → `internal_disciplinary_control.disciplinary_processes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla disciplinary_news_processes. Se genera automáticamente. | PK |
| 2 | `news_id` | `uuid` | no | ID de la noticia disciplinaria |  |
| 3 | `process_id` | `uuid` | no | ID del proceso disciplinario | FK→internal_disciplinary_control.disciplinary_processes.id |
| 4 | `fecha_asociacion` | `timestamp with time zone` | no | Fecha en que se realizó la asociación |  |
| 5 | `justificacion` | `text` | sí | Justificación de la asociación |  |
| 6 | `created_at` | `timestamp with time zone` | no | Fecha de creación del registro |  |
| 7 | `updated_at` | `timestamp with time zone` | no | Fecha de última actualización del registro |  |

## disciplinary_process_actuaciones

Actuaciones registradas en los procesos disciplinarios. Un registro por actuación, asociada a un proceso y, si aplica, a una noticia disciplinaria, con su tipo, etapa, descripción, responsable, fecha y observaciones.

- Clave primaria: `id`
- Filas: 148
- Referencia a: `newsId` → `internal_disciplinary_control.disciplinary_news` (0..* → 0..1); `processId` → `internal_disciplinary_control.disciplinary_processes` (1..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla disciplinary_process_actuaciones. Se genera automáticamente. | PK |
| 2 | `processId` | `uuid` | sí | Referencia al registro de internal_disciplinary_control.disciplinary_processes (id). | FK→internal_disciplinary_control.disciplinary_processes.id |
| 3 | `tipo` | `character varying(50)` | no | Tipo de actuación del proceso disciplinario. |  |
| 4 | `etapa` | `character varying(80)` | sí | Etapa del proceso disciplinario en que se registra la actuación: la recibida en el formulario o, si no llega, la etapa actual del proceso (nombre de etapa de stage_configuration); para actuaciones de la noticia, RADICACION por defecto. |  |
| 5 | `descripcion` | `text` | no | Descripción de la actuación del proceso disciplinario. |  |
| 6 | `responsableNombre` | `character varying(255)` | no | Nombre del responsable de la actuación. |  |
| 7 | `fechaActuacion` | `timestamp with time zone` | no | Fecha y hora de la actuación; por defecto, la del registro. |  |
| 8 | `observaciones` | `text` | sí | Observaciones sobre la actuación. |  |
| 9 | `createdAt` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 10 | `updatedAt` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 11 | `newsId` | `uuid` | sí | Referencia al registro de internal_disciplinary_control.disciplinary_news (id). | FK→internal_disciplinary_control.disciplinary_news.id |

## disciplinary_process_notes

Notas de los procesos disciplinarios. Un registro por nota, asociada a un proceso, con su texto y la etapa del proceso a la que corresponde.

- Clave primaria: `id`
- Filas: 14
- Referencia a: `processId` → `internal_disciplinary_control.disciplinary_processes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla disciplinary_process_notes. Se genera automáticamente. | PK |
| 2 | `processId` | `uuid` | no | Referencia al registro de internal_disciplinary_control.disciplinary_processes (id). | FK→internal_disciplinary_control.disciplinary_processes.id |
| 3 | `texto` | `text` | no | Texto de la nota del proceso disciplinario. |  |
| 4 | `etapa` | `character varying(80)` | sí | Etapa del proceso disciplinario a la que corresponde la nota: la recibida en el formulario o, si no llega, la etapa actual del proceso (nombre de etapa de stage_configuration). |  |
| 5 | `createdAt` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 6 | `updatedAt` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## disciplinary_process_reassignment_requests

Tabla para solicitudes de reasignación de procesos disciplinarios

- Clave primaria: `id`
- Filas: 24
- Referencia a: `current_professional_id` → `internal_disciplinary_control.disciplinary_professional` (0..* → 0..1); `new_professional_id` → `internal_disciplinary_control.disciplinary_professional` (0..* → 1); `process_id` → `internal_disciplinary_control.disciplinary_processes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla disciplinary_process_reassignment_requests. Se genera automáticamente. | PK |
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
| 15 | `was_initially_unassigned` | `boolean` | sí | Indica si el proceso no tenía profesional asignado al momento de la solicitud de reasignación. |  |

## disciplinary_process_tasks

Tareas de los procesos disciplinarios. Un registro por tarea, asociada a un proceso, con título, descripción, prioridad (alta, media o baja), etapa, responsable, fecha de vencimiento y si está completada.

- Clave primaria: `id`
- Filas: 15
- Referencia a: `processId` → `internal_disciplinary_control.disciplinary_processes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla disciplinary_process_tasks. Se genera automáticamente. | PK |
| 2 | `processId` | `uuid` | no | Referencia al registro de internal_disciplinary_control.disciplinary_processes (id). | FK→internal_disciplinary_control.disciplinary_processes.id |
| 3 | `titulo` | `character varying(255)` | no | Título de la tarea del proceso disciplinario. |  |
| 4 | `descripcion` | `text` | sí | Descripción de la tarea del proceso disciplinario. |  |
| 5 | `prioridad` | `character varying(20)` | no | Prioridad de la tarea. Valores permitidos: alta, media, baja. |  |
| 6 | `etapa` | `character varying(80)` | sí | Etapa del proceso disciplinario a la que corresponde la tarea: la recibida en el formulario o, si no llega, la etapa actual del proceso (nombre de etapa de stage_configuration). |  |
| 7 | `responsableNombre` | `character varying(255)` | sí | Nombre del responsable de la tarea. |  |
| 8 | `fechaVencimiento` | `date` | no | Fecha de vencimiento de la tarea. |  |
| 9 | `completada` | `boolean` | no | Indica si la tarea está completada. |  |
| 10 | `fechaCompletada` | `timestamp with time zone` | sí | Fecha y hora en que se completó la tarea. |  |
| 11 | `observaciones` | `text` | sí | Observaciones sobre la tarea. |  |
| 12 | `createdAt` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 13 | `updatedAt` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## disciplinary_processes

Procesos disciplinarios activos

- Clave primaria: `id`
- Filas: 26
- Referencia a: `abogado_asignado_id` → `internal_disciplinary_control.disciplinary_professional` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla disciplinary_processes. Se genera automáticamente. | PK |
| 2 | `radicadoProceso` | `character varying(255)` | no | Número de radicado del proceso disciplinario, único, con formato P-###-YYYY. | única |
| 3 | `newsId` | `uuid` | no | Identificador (UUID) de la noticia disciplinaria que dio origen al proceso (internal_disciplinary_control.disciplinary_news). La relación está mapeada en la entidad y el DDL de referencia del repositorio declara la FK con ON DELETE RESTRICT. |  |
| 4 | `abogado_asignado_id` | `uuid` | sí | Referencia al registro de internal_disciplinary_control.disciplinary_professional (id). | FK→internal_disciplinary_control.disciplinary_professional.id |
| 5 | `etapaActual` | `character varying(100)` | no | Etapa actual del proceso disciplinario (VARCHAR - flexible para nuevas etapas) |  |
| 6 | `estado` | `internal_disciplinary_control.disciplinary_processes_estado_enum` | no | Estados: ACTIVO, SUSPENDIDO, ARCHIVADO, TERMINADO |  |
| 7 | `fechaPrescripcion` | `timestamp with time zone` | sí | Fecha en que prescribe la acción disciplinaria del proceso, calculada por el sistema al crear el proceso como la fecha de recepción de la noticia más 15 años. |  |
| 8 | `fechaVencimientoEtapa` | `timestamp with time zone` | sí | Fecha en que vence el término de la etapa actual del proceso, calculada por el sistema al iniciar o cambiar de etapa sumando a la fecha del cambio los días hábiles de la etapa en stage_configuration (sin festivos nacionales ni institucionales); queda vacía al remitir el proceso. |  |
| 9 | `observaciones` | `text` | sí | Observaciones sobre el proceso disciplinario. |  |
| 10 | `pruebas` | `text[]` | sí | Lista de pruebas del proceso disciplinario, como arreglo de rutas relativas de los archivos cargados como evidencia (o URL externa); campo heredado que se mantiene junto con la tabla evidence. |  |
| 11 | `createdAt` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 12 | `updatedAt` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 13 | `kanbanStage` | `uuid` | sí | Identificador de la columna del tablero Kanban en que se ubica el proceso (internal_disciplinary_control.stage_configuration). El proceso inicia en la etapa de orden 2 (Valoración) y la columna se actualiza en cada cambio de etapa. |  |
| 14 | `kanbanNotice` | `text` | sí | Aviso que se muestra en la tarjeta del proceso en el tablero Kanban: texto que el usuario registra al cambiar de etapa o aviso que genera el sistema al aprobarse el auto de remisión o al remitir el proceso por competencia. |  |
| 15 | `drafts_count` | `integer` | sí | Cantidad de borradores asociados al proceso. Se actualiza mediante la función public.update_process_statistics. |  |
| 16 | `documents_count` | `integer` | sí | Cantidad de documentos asociados al proceso. Se actualiza mediante la función public.update_process_documents_count. |  |
| 17 | `time_percentage` | `numeric(5,2)` | sí | Porcentaje del término de la etapa actual que ya transcurrió (0 a 100), medido entre el inicio de la etapa y fechaVencimientoEtapa. Valor por defecto: 0. |  |
| 18 | `proceso_asociado_id` | `uuid` | sí | Identificador del otro proceso disciplinario (disciplinary_processes.id) al que se asoció este proceso como conexo, similar o consolidado; en la consolidación ambos procesos quedan apuntando uno al otro. |  |
| 19 | `proceso_asociado_numero` | `character varying(50)` | sí | Radicado del proceso asociado: copia de radicadoProceso del proceso referenciado por proceso_asociado_id. |  |
| 20 | `proceso_asociado_tipo` | `character varying(20)` | sí | Tipo de vínculo con el proceso asociado: conexo, similar o consolidado. |  |
| 21 | `proceso_asociado_fecha` | `timestamp with time zone` | sí | Fecha y hora en que se registró la asociación con el otro proceso. |  |
| 22 | `proceso_asociado_justificacion` | `text` | sí | Justificación de la asociación del proceso con otro proceso, digitada por el usuario que registra la asociación. |  |
| 23 | `procesos_consolidados` | `text[]` | sí | Radicados de los procesos consolidados (el principal y el secundario), como arreglo de textos. |  |
| 24 | `proceso_consolidado_principal` | `uuid` | sí | Identificador del proceso principal de la consolidación (disciplinary_processes.id): el proceso más antiguo por fecha de creación. |  |
| 25 | `informacion_consolidada` | `jsonb` | sí | Información del proceso principal de la consolidación, como objeto JSON con radicado, fechaInicio, hechos y disciplinable; la llena el sistema al consolidar. |  |
| 26 | `fechaInicioEtapa` | `timestamp with time zone` | sí | Fecha de inicio de la etapa actual del proceso. |  |
| 27 | `fecha_cierre` | `timestamp with time zone` | sí | Fecha y hora de cierre del proceso disciplinario: se llena al cerrar el proceso por el envío del pliego de cargos a jurídica y se borra si el proceso se restaura. |  |
| 28 | `etapa_al_cierre` | `character varying(100)` | sí | Etapa en que se encontraba el proceso al momento del cierre: copia de etapaActual; se borra si el proceso se restaura. |  |
| 29 | `cerrado_por_id` | `uuid` | sí | Identificador del usuario que cerró el proceso al enviar el pliego de cargos a jurídica; se borra si el proceso se restaura. |  |
| 30 | `correo_juridica_enviado` | `boolean` | sí | Indica si se envió el correo a la Oficina Jurídica con el expediente al cerrar el proceso por el auto de pliego de cargos aprobado. El buzón se toma de la variable de entorno JURIDICA_EMAIL. Por defecto, falso. |  |
| 31 | `correo_juridica_fecha_envio` | `timestamp with time zone` | sí | Fecha y hora de envío del correo a la Oficina Jurídica; se llena junto con correo_juridica_enviado = verdadero. |  |
| 32 | `restaurado` | `boolean` | no | Indica si el proceso disciplinario fue restaurado desde estado archivado |  |
| 33 | `en_proceso_remision` | `boolean` | sí | Indica si el proceso está en trámite de remisión por competencia a otra entidad; se marca al crear el proceso cuando la noticia proviene de una remisión o trae entidad o tipo de remisión. Por defecto, falso. |  |
| 34 | `remision_aprobada` | `boolean` | sí | Indica si la remisión por competencia del proceso fue aprobada: se marca cuando el jefe aprueba el auto de remisión por competencia y al ejecutarse la remisión. Por defecto, falso. |  |
| 35 | `numero_rc` | `character varying(50)` | sí | Número RC de la remisión por competencia del proceso, generado por el sistema con el formato RC-<año>-<número de cuatro dígitos>. |  |
| 36 | `entidad_remision` | `character varying(255)` | sí | Nombre de la entidad a la que se remite el proceso, guardado como texto: se toma de la noticia, del auto de remisión aprobado o de la entidad digitada al remitir. Existe el catálogo entidades_remision, pero la columna no lo referencia. |  |
| 37 | `correo_entidad_remision` | `character varying(255)` | sí | Correo electrónico de la entidad a la que se remite el proceso; es la dirección a la que se envía la remisión. |  |
| 38 | `fecha_remision` | `timestamp with time zone` | sí | Fecha y hora en que se ejecutó la remisión del proceso a la entidad destino (envío), no la de aprobación del auto. |  |
| 39 | `tipo_remision` | `character varying(100)` | sí | Código del tipo de remisión por competencia, del catálogo tipos_remision: sin-competencia (valor por defecto), factor-territorial, factor-funcional, naturaleza-falta o prelacion-competencia. |  |
| 40 | `justificacion_remision` | `text` | sí | Justificación de la remisión del proceso a otra entidad, obligatoria y digitada por el usuario que ejecuta la remisión. |  |
| 41 | `descripcion_remision` | `jsonb` | sí | Descripción de la remisión por competencia, como objeto JSON con los datos de la noticia remitida (numeroRadicado, origen, fechaRecepcion, territorial, dependenciaDenunciado, denunciante, disciplinable, hechos, conductas, fechaHechos, fechaCaducidad); se registra en el formulario o se arma con los datos de la noticia. |  |

## disciplinary_professional

Profesionales (abogados) asignados a procesos disciplinarios

- Clave primaria: `id`
- Filas: 9
- Relaciones implícitas: `id_user` ↝ `auth.user` (100.0 % con padre)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla disciplinary_professional. Se genera automáticamente. | PK |
| 2 | `nombre_completo` | `character varying(255)` | no | Nombre completo del profesional. | Nombre de persona |
| 3 | `email` | `character varying(255)` | no | Correo electrónico del profesional. | única Contacto |
| 4 | `telefono` | `character varying(50)` | sí | Número de teléfono del profesional. | Contacto |
| 5 | `cargo` | `character varying(100)` | no | Cargo del profesional, por ejemplo Jefe de Oficina o Profesional Universitario. |  |
| 6 | `especialidad` | `character varying(100)` | sí | Especialidad del profesional, en texto. |  |
| 7 | `tipo_contrato` | `character varying(50)` | sí | Tipo de vinculación o contrato del profesional, en texto. |  |
| 8 | `territorial` | `character varying(100)` | sí | Dirección territorial a la que pertenece el profesional, en texto. |  |
| 9 | `capacidad_maxima` | `integer` | sí | Número máximo de procesos activos simultáneos que se pueden asignar al profesional; se compara con los procesos en estado ACTIVO cuya noticia no está devuelta y se limita al máximo configurado por cargo en system_configuration. Valor por defecto: 10. |  |
| 10 | `estado` | `character varying(50)` | sí | Estado del profesional. |  |
| 11 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 13 | `firma_url` | `text` | sí | URL del archivo de firma mecánica/digital del profesional |  |
| 14 | `id_user` | `uuid` | sí | Usuario del sistema asociado al profesional (auth.user); relación sin llave foránea declarada. | ↝auth.user.id_user |

## entidades_remision

Tabla para gestionar las entidades de remisión en procesos disciplinarios

- Clave primaria: `id`
- Filas: 9

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla entidades_remision. Se genera automáticamente. | PK |
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
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla evidence. Se genera automáticamente. | PK |
| 2 | `url` | `text` | no | Dirección web (URL) del archivo de la evidencia; admite URL externas largas. |  |
| 3 | `filename` | `character varying(255)` | sí | Nombre del archivo de la evidencia. |  |
| 4 | `description` | `text` | sí | Descripción de la evidencia. |  |
| 5 | `fileType` | `character varying(100)` | sí | Tipo de archivo: pdf, docx, jpg, etc. |  |
| 6 | `fileSize` | `integer` | sí | Tamaño del archivo de la evidencia en bytes; 0 cuando la evidencia es una URL externa. |  |
| 7 | `createdAt` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 8 | `processId` | `uuid` | no | Referencia al registro de internal_disciplinary_control.disciplinary_processes (id). | FK→internal_disciplinary_control.disciplinary_processes.id |
| 9 | `nombreDocumento` | `character varying(255)` | sí | Nombre del documento cargado como evidencia: el nombre digitado en el formulario o, si no llega, el nombre original del archivo. Tiene el mismo valor que nombreArchivo; filename guarda siempre el nombre original del archivo. |  |
| 10 | `tipoDocumento` | `character varying(50)` | sí | Tipo de documento de la evidencia, en texto: EVIDENCIA, PRUEBA DOCUMENTAL, AUTO, OFICIO, NOTIFICACION, ACTA o DECLARACION, que determinan el formato de archivo admitido; si no se informa, DOCUMENTO. |  |
| 11 | `etapa` | `character varying(100)` | sí | Etapa del proceso disciplinario en la que se cargó la evidencia (máximo 80 caracteres). |  |
| 12 | `usuarioCarga` | `character varying(255)` | sí | Usuario que cargó la evidencia, en texto recibido del formulario; «Sistema» si no llega. |  |
| 13 | `categoria` | `character varying(50)` | sí | Categoría de la evidencia, en texto recibido del formulario. |  |
| 14 | `destinatario` | `character varying(255)` | sí | Destinatario de la comunicación registrada como evidencia, en texto recibido del formulario. |  |
| 15 | `asunto` | `character varying(255)` | sí | Asunto de la comunicación registrada como evidencia, en texto recibido del formulario. |  |
| 16 | `participantes` | `integer` | sí | Número de participantes registrados en la evidencia, recibido del formulario. |  |
| 17 | `archivoUrl` | `character varying` | sí | Ruta relativa del archivo de la evidencia en la carpeta del proceso (o URL externa). Se llena con el mismo valor que url y es la que se lee primero al adjuntar evidencias. |  |
| 18 | `nombreArchivo` | `character varying` | sí | Nombre del archivo de la evidencia: el nombre digitado en el formulario o el nombre original del archivo; tiene el mismo valor que nombreDocumento. |  |
| 19 | `tipo` | `character varying` | sí | Tipo de evidencia: copia de tipoDocumento (EVIDENCIA, PRUEBA DOCUMENTAL, AUTO, OFICIO, NOTIFICACION, ACTA, DECLARACION u otro texto). Valor por defecto: DOCUMENTO. |  |

## expediente_compartido

Tabla para gestionar los enlaces compartidos de expedientes disciplinarios

- Clave primaria: `id`
- Filas: 95

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla expediente_compartido. Se genera automáticamente. | PK |
| 2 | `token_acceso` | `character varying(255)` | no | Token único de acceso al enlace compartido | única Credencial de acceso |
| 3 | `proceso_id` | `uuid` | no | ID del proceso disciplinario que se comparte |  |
| 4 | `tipo_compartido` | `internal_disciplinary_control.tipo_compartido` | no | Tipo de compartido: LINK, QR o EMAIL |  |
| 5 | `estado` | `internal_disciplinary_control.estado_compartido` | no | Estado del enlace compartido del expediente (ACTIVO, INACTIVO o EXPIRADO). |  |
| 6 | `requiere_clave` | `boolean` | sí | Indica si el enlace requiere clave de acceso |  |
| 7 | `clave_hash` | `character varying(255)` | sí | Hash de la clave de acceso (bcrypt) |  |
| 8 | `tiempo_expiracion_horas` | `integer` | sí | Tiempo de expiración en horas |  |
| 9 | `fecha_expiracion` | `timestamp without time zone` | sí | Fecha en que expira el enlace |  |
| 10 | `email_destinatario` | `character varying(255)` | sí | Email del destinatario (para tipo EMAIL) | Contacto |
| 11 | `mensaje_adicional` | `text` | sí | Mensaje adicional incluido en el correo |  |
| 12 | `creado_por` | `character varying(255)` | sí | Usuario que creó el registro. |  |
| 13 | `contador_accesos` | `integer` | sí | Número de veces que se ha accedido al enlace compartido. Valor por defecto: 0. |  |
| 14 | `ultimo_acceso` | `timestamp without time zone` | sí | Fecha y hora del último acceso al enlace compartido. |  |
| 15 | `ip_ultimo_acceso` | `character varying(45)` | sí | Dirección IP desde la que se hizo el último acceso al enlace compartido (IPv4 o IPv6). | Identificador en línea (IP) |
| 16 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 17 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 18 | `es_publico` | `boolean` | sí | Indica si el enlace es público (sin autenticación) |  |
| 19 | `permite_descarga` | `boolean` | sí | Indica si el enlace compartido permite descargar el expediente. |  |

## legal_autos

Autos legales generados en los procesos

- Clave primaria: `id`
- Filas: 218
- Referencia a: `processId` → `internal_disciplinary_control.disciplinary_processes` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla legal_autos. Se genera automáticamente. | PK |
| 2 | `processId` | `uuid` | no | Referencia al registro de internal_disciplinary_control.disciplinary_processes (id). | FK→internal_disciplinary_control.disciplinary_processes.id |
| 3 | `tipo` | `character varying(50)` | no | Tipos: AUTO_APERTURA, AUTO_PRUEBAS, AUTO_CIERRE, etc. |  |
| 4 | `contenido` | `text` | no | Contenido del auto en HTML (texto enriquecido). |  |
| 5 | `estado` | `character varying(50)` | sí | Estados: BORRADOR, EN_REVISION, APROBADO, RECHAZADO, NOTIFICADO |  |
| 6 | `firmaUrl` | `text` | sí | URL del PDF firmado del auto. |  |
| 7 | `comentarios` | `text` | sí | Comentarios del auto: observaciones del jefe al revisarlo (aprobar o devolver), comentarios que se anexan con fecha y hora al cargar una nueva versión del documento durante la revisión, o texto enviado al actualizar el auto. |  |
| 8 | `aprobadoPorId` | `uuid` | sí | Identificador del jefe que aprobó el auto. |  |
| 9 | `createdAt` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 10 | `updatedAt` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 11 | `notificationDate` | `timestamp with time zone` | sí | Fecha de notificación del auto. |  |
| 12 | `notificationEvidence` | `text` | sí | URL del archivo de prueba de notificación del auto. |  |
| 13 | `rejection_comments` | `text` | sí | Comentarios del rechazo del auto. |  |
| 14 | `currentVersion` | `integer` | sí | Número de la versión vigente del auto. Valor por defecto: 1. |  |
| 15 | `numero` | `character varying(150)` | sí | Número del auto legal. |  |
| 16 | `documentUrl` | `text` | sí | Ruta del documento vigente del auto (archivo cargado o PDF convertido, con forma /files/<archivo>). Al firmar el auto, esta ruta se copia a firmaUrl, que conserva el PDF firmado. |  |
| 17 | `documentName` | `text` | sí | Nombre del documento del auto. |  |
| 18 | `documentType` | `text` | sí | Tipo MIME del documento del auto (por ejemplo, application/pdf). |  |
| 19 | `documentSize` | `integer` | sí | Tamaño del documento del auto, en bytes. |  |
| 20 | `etapaDestino` | `character varying(50)` | sí | Etapa procesal a la que pasa el proceso al aprobarse el auto. Toma un código de etapa (RECEPCION, VALORACION, INDAGACION_PREVIA, INVESTIGACION, EVALUACION, CARGOS, JUZGAMIENTO, INDAGACION, FALLO, SEGUNDA_INSTANCIA, INHIBITORIO): el informado, el sufijo de un auto AUTO_APERTURA_*, la etapa de la configuración del auto o CARGOS para el pliego de cargos. |  |
| 21 | `prorrogaMeses` | `integer` | sí | Meses de prórroga; solo aplica para AUTO_PRORROGA. Valores permitidos: 3, 6. |  |
| 22 | `fechaVencimientoAnterior` | `timestamp with time zone` | sí | Fecha de vencimiento anterior a la prórroga, registrada para el historial de prórrogas. |  |
| 23 | `fechaVencimientoNueva` | `timestamp with time zone` | sí | Nueva fecha de vencimiento de la etapa activa tras la prórroga concedida por el auto. Se llena solo al aprobar autos de tipo AUTO_PRORROGA (fecha anterior más prorrogaMeses). |  |
| 24 | `autoConfigurationId` | `uuid` | sí | Identificador de la plantilla exacta (autos_configuration.id) usada al crear el auto. |  |
| 25 | `etapaPreviaAprobacion` | `character varying(100)` | sí | Etapa en la que estaba el proceso justo antes de aprobar el auto; solo se guarda si la aprobación cambió la etapa, y permite que «Reversar aprobación» devuelva el proceso a esa etapa (EFDS-1564). |  |
| 26 | `rejectionDocumentUrl` | `text` | sí | URL del documento de soporte que adjunta el jefe al devolver el auto. |  |
| 27 | `rejectionDocumentName` | `text` | sí | Nombre original del archivo de soporte que el jefe adjunta al devolver el auto. |  |
| 28 | `radicador_asignado_id` | `uuid` | sí | ID del usuario radicador asignado a este auto |  |
| 29 | `entidad_destino` | `character varying(255)` | sí | Entidad a la que se remite el expediente por competencia. Se llena en autos AUTO_REMISION_COMPETENCIA o AUTO_REMISION, al crearlos o al aprobarlos. |  |
| 30 | `entidad_destino_email` | `character varying(255)` | sí | Correo electrónico de la entidad destino del auto. |  |

## oficios_configuration

Configuración de los tipos de oficio del proceso disciplinario. Un registro por oficio, con su tipo, nombre, código, descripción, estado, etapa del proceso, orden y los datos de su plantilla (archivo, nombre, descripción, versión y estado).

- Clave primaria: `id`
- Filas: 14

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla oficios_configuration. Se genera automáticamente. | PK |
| 2 | `tipo` | `character varying(100)` | no | Tipo de oficio configurado. | única |
| 3 | `nombre` | `character varying(200)` | no | Nombre del oficio configurado. |  |
| 4 | `codigo` | `character varying(50)` | sí | Código del oficio configurado. |  |
| 5 | `descripcion` | `text` | sí | Descripción del oficio configurado. |  |
| 6 | `estado` | `character varying(50)` | no | Estado de la configuración del oficio. |  |
| 7 | `plantilla` | `text` | sí | Plantilla del oficio: ruta del archivo Word cargado (/uploads/plantillas-oficios/...); la API también admite base64 o enlace. No se guarda como HTML. |  |
| 8 | `nombre_plantilla` | `character varying(255)` | sí | Nombre de la plantilla asociada a la configuración del oficio. |  |
| 9 | `descripcion_plantilla` | `text` | sí | Descripción de la plantilla del oficio. |  |
| 10 | `version_plantilla` | `character varying(50)` | sí | Versión de la plantilla del oficio. Valor por defecto: 1.0. |  |
| 11 | `estado_plantilla` | `character varying(50)` | sí | Estado de la plantilla del oficio. Valores permitidos: activo, inactivo. Valor por defecto: activo. |  |
| 12 | `stage` | `character varying(50)` | sí | Etapa del proceso disciplinario asociada al oficio. |  |
| 13 | `orden` | `integer` | sí | Posición del oficio en el listado. |  |
| 14 | `createdAt` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 15 | `updatedAt` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## plantilla_auto

Plantillas en HTML para la elaboración de autos del proceso disciplinario. Un registro por plantilla, con su nombre, descripción, contenido y estado (activo o inactivo).

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla plantilla_auto. Se genera automáticamente. | PK |
| 2 | `htmlContent` | `text` | no | Contenido HTML de la plantilla de auto. |  |
| 3 | `estado` | `character varying(50)` | no | Estado de la plantilla de auto. Valores permitidos: activo, inactivo. Por defecto, activo. |  |
| 4 | `nombre` | `character varying(100)` | sí | Nombre de la plantilla de auto. |  |
| 5 | `descripcion` | `text` | sí | Descripción de la plantilla de auto. |  |
| 6 | `createdAt` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 7 | `updatedAt` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## reglas_alerta

Reglas de alerta de vencimiento de términos procesales. Un registro por regla, con su nombre, días hábiles de anticipación, canales (correo y panel), descripción y estado activo; las alertas generadas se registran en internal_disciplinary_control.alertas_enviadas.

- Clave primaria: `id`
- Filas: 7

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla reglas_alerta. Se genera automáticamente. | PK |
| 2 | `nombre` | `character varying(200)` | no | Nombre de la regla de alerta. | única |
| 3 | `dias_anticipacion` | `integer` | no | Días hábiles de anticipación al vencimiento con que se genera la alerta, de 0 a 30. El valor 0 lo usa la regla de proceso vencido que crea el sistema; las reglas creadas o editadas por la API exigen de 1 a 30. |  |
| 4 | `activa` | `boolean` | no | Indica si la regla de alerta está activa. |  |
| 5 | `enviar_email` | `boolean` | no | Indica si la regla envía la alerta por correo electrónico. |  |
| 6 | `mostrar_panel` | `boolean` | no | Indica si la regla muestra la alerta en el panel. |  |
| 7 | `descripcion` | `text` | sí | Descripción de la regla de alerta. |  |
| 8 | `creado_por_id` | `uuid` | sí | Identificador de la persona que creó la regla (auth.personas); nulo en las reglas generadas por el sistema. |  |
| 9 | `fecha_creacion` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 10 | `fecha_actualizacion` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## sequences

Tabla para gestionar secuencias de radicados

- Clave primaria: `name`
- Filas: 7

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `name` | `character varying(255)` | no | Clave primaria de la tabla sequences: name. | PK |
| 2 | `currentValue` | `integer` | sí | Último número asignado de la secuencia de consecutivos (se incrementa y luego se usa). Por defecto, 0. |  |
| 3 | `updatedAt` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## stage_configuration

Configuración de días hábiles por etapa procesal

- Clave primaria: `id`
- Filas: 7

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla stage_configuration. Se genera automáticamente. | PK |
| 2 | `etapa` | `character varying(255)` | no | Nombre de la etapa procesal (máximo 80 caracteres). |  |
| 3 | `diasHabiles` | `integer` | no | Días hábiles de duración de la etapa (entre 1 y 180). Valor por defecto: 30. |  |
| 4 | `descripcion` | `text` | sí | Descripción de la etapa procesal. |  |
| 5 | `activo` | `boolean` | sí | Indica si la configuración de la etapa está activa. |  |
| 6 | `createdAt` | `timestamp without time zone` | no | Fecha de creación del registro |  |
| 7 | `updatedAt` | `timestamp without time zone` | no | Fecha de última actualización del registro |  |
| 8 | `color` | `character varying(50)` | sí | Color con que se muestra la etapa en la interfaz, en formato hexadecimal. Por defecto, #6B7280. |  |
| 9 | `orden` | `integer` | sí | Posición de la etapa procesal en el listado. |  |

## system_configuration

Configuración global del sistema disciplinario

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla system_configuration. Se genera automáticamente. | PK |
| 2 | `roleCapacities` | `jsonb` | sí | Capacidad máxima por cargo, en formato JSON (llave: texto del cargo; valor: número). Fija el tope de capacidad_maxima del profesional, que se compara con sus procesos activos asignados. |  |
| 3 | `notificationSettings` | `jsonb` | sí | Configuración de notificaciones, en formato JSON (por ejemplo, vencimiento7dias, emailMasterSwitch). |  |
| 4 | `alertSettings` | `jsonb` | sí | Configuración de alertas, en formato JSON (por ejemplo, porcentajeAmarillo: 85, porcentajeRojo: 95). |  |
| 5 | `securitySettings` | `jsonb` | sí | Configuración de seguridad y auditoría, en formato JSON (por ejemplo, auditEnabled, digitalSignature). |  |
| 6 | `documentTemplates` | `jsonb` | sí | Plantillas de documentos (oficios, autos, actas), en formato JSON. |  |

## terminos_procesales

Términos procesales con su control de vencimiento. Un registro por término de una actuación de un proceso, con el responsable, fecha de inicio, días hábiles, fecha de vencimiento, días restantes, estado (pendiente, próximo a vencer, vencido o cumplido), envío de alerta y fecha de cumplimiento.

- Clave primaria: `id`
- Filas: 23

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla terminos_procesales. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Identificador (UUID) del proceso disciplinario al que pertenece el término; corresponde a disciplinary_processes.id según la relación de la entidad. |  |
| 3 | `numero_proceso` | `character varying(20)` | sí | Número de radicado del proceso; puede estar vacío si aún no hay radicado visible. |  |
| 4 | `actuacion` | `character varying(200)` | no | Tipo de actuación procesal a la que corresponde el término. |  |
| 5 | `responsable_id` | `uuid` | no | Identificador de la persona responsable del término (auth.personas). |  |
| 6 | `responsable_nombre` | `character varying(200)` | no | Nombre del responsable del término, copiado de la persona responsable. |  |
| 7 | `email_responsable` | `character varying(100)` | no | Correo electrónico del responsable del término. | Contacto |
| 8 | `fecha_inicio` | `date` | no | Fecha de inicio del término procesal. |  |
| 9 | `dias_habiles` | `integer` | no | Número de días hábiles del término, mayor que 0 y hasta 180. |  |
| 10 | `fecha_vencimiento` | `date` | no | Fecha de vencimiento del término procesal. |  |
| 11 | `dias_restantes` | `integer` | no | Días que faltan para el vencimiento del término; negativo si está vencido, con mínimo de -365. |  |
| 12 | `estado` | `internal_disciplinary_control.termino_estado_enum` | no | Estado del término procesal (pendiente, próximo a vencer, vencido o cumplido). |  |
| 13 | `alerta_enviada` | `boolean` | no | Indica si se envió la alerta del término procesal. |  |
| 14 | `fecha_cumplimiento` | `date` | sí | Fecha en que se cumplió el término procesal. |  |
| 15 | `observaciones` | `text` | sí | Observaciones sobre el término procesal. |  |
| 16 | `creado_por_id` | `uuid` | no | Identificador de la persona que registró el término (auth.personas). |  |
| 17 | `fecha_creacion` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 18 | `fecha_actualizacion` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## tipos_remision

Tabla para gestionar los tipos de remisión en procesos disciplinarios

- Clave primaria: `id`
- Filas: 6

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla tipos_remision. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(100)` | no | Código único del tipo de remisión | única |
| 3 | `nombre` | `character varying(255)` | no | Nombre del tipo de remisión |  |
| 4 | `descripcion` | `text` | sí | Descripción del tipo de remisión |  |
| 5 | `activo` | `boolean` | sí | Indica si el tipo está activo |  |
| 6 | `orden` | `integer` | sí | Orden de visualización del tipo |  |
| 7 | `created_at` | `timestamp without time zone` | no | Fecha de creación del registro |  |
| 8 | `updated_at` | `timestamp without time zone` | no | Fecha de última actualización del registro |  |
