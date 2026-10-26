# Gestión jurídica (`legal_management`)

Gestión jurídica de la ESAP: expedientes judiciales con sus actores, actuaciones, documentos y términos procesales; consultas jurídicas, correos de los buzones jurídicos, procesos de cobro coactivo y alertas de vencimiento.

54 tablas · 0 vistas · 791 columnas · 33.031 filas · 7 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`actas`](#actas) | Tabla | 0 | Actas de reuniones o sesiones de los expedientes de gestión jurídica. Un registro por acta, asociada a un expediente, con número, fecha, horario, duración, lugar, presidente, participantes, resumen, decisiones, tipo, estado (firmada o programada) y archivo del acta. |
| [`actors`](#actors) | Tabla | 168 | Actores de los expedientes de gestión jurídica: demandantes, demandados y otros. Un registro por actor de un expediente, con nombre, tipo de persona (natural o jurídica), identificación, rol, cargo, dependencia, apoderado y datos de contacto. |
| [`actuaciones`](#actuaciones) | Tabla | 427 | Historial unificado de actuaciones de los expedientes y procesos de la gestión jurídica. Un registro por actuación, con su tipo, fecha, documento soporte, responsable y origen (manual, audiencia, auto, acta, evidencia u oficio), y la referencia al registro que la generó. El expediente se identifica por texto, sin relación declarada con legal_management.expedientes. |
| [`adjuntos_correo`](#adjuntos_correo) | Tabla | 2554 | Adjuntos de correos electrónicos sincronizados desde Microsoft Graph |
| [`audiencias`](#audiencias) | Tabla | 18 | Audiencias programadas en los expedientes de la gestión jurídica. Un registro por audiencia, asociada a un expediente (legal_management.expedientes), con su fecha y hora, duración, modalidad (virtual o presencial), abogado responsable e historial de reprogramaciones. Su estado pasa por programada, realizada, cancelada o aplazada. |
| [`autos`](#autos) | Tabla | 4 | Autos emitidos dentro de los expedientes de la gestión jurídica. Un registro por auto, asociado a un expediente (legal_management.expedientes), con su número, tipo, fecha, juzgado, resumen y archivo. Su estado pasa por pendiente, notificado o archivado. |
| [`borradores_correos`](#borradores_correos) | Tabla | 2 | Borradores privados de correos nuevos del Centro de Comunicaciones (Redactar Correo). Se autoguardan y se eliminan al enviarse. |
| [`cat_tipos_requerimiento`](#cat_tipos_requerimiento) | Tabla | 9 | Catálogo de tipos de requerimiento de los organismos de control. Un registro por tipo, con nombre, descripción, orden de presentación e indicador de activo; legal_management.requerimientos_oc toma de aquí su tipo de requerimiento. |
| [`coactivos_historial`](#coactivos_historial) | Tabla | 48 | Historial de eventos de los procesos de cobro coactivo. Un registro por evento (creación, pago, cambio de etapa o actualización) de un proceso de legal_management.procesos_coactivos, con el campo modificado, sus valores anterior y nuevo, el usuario y la fecha. |
| [`comentarios`](#comentarios) | Tabla | 9 | Comentarios registrados sobre los expedientes de la gestión jurídica. Un registro por comentario, asociado a un expediente (legal_management.expedientes), con su texto y el usuario autor. |
| [`comentarios_consulta`](#comentarios_consulta) | Tabla | 2 | Comentarios registrados sobre las consultas jurídicas. Un registro por comentario, asociado a una consulta de legal_management.consultas_juridicas, con el mensaje, el usuario autor, su cargo y la fecha. |
| [`comentarios_correo`](#comentarios_correo) | Tabla | 2 | Comentarios del tab "Comentarios" en el Detalle de Comunicación (Centro de Comunicaciones). |
| [`comentarios_oc`](#comentarios_oc) | Tabla | 28 | Comentarios registrados sobre los requerimientos de los organismos de control. Un registro por comentario, asociado a un requerimiento de legal_management.requerimientos_oc, con su tipo, contenido y autor. |
| [`conceptos_juridicos`](#conceptos_juridicos) | Tabla | 0 | Conceptos jurídicos emitidos en respuesta a las consultas de asesoría jurídica. Un registro por concepto (concepto, memorando, revisión o viabilidad), asociado a una consulta de legal_management.consultas_juridicas, con su análisis, normatividad, conclusión, redactor, revisión, aprobación y emisión. Su estado pasa por borrador, en revisión, devuelto, aprobado o emitido, y puede publicarse en el banco de conceptos. |
| [`consulta_juridica_historial`](#consulta_juridica_historial) | Tabla | 132 | Historial de eventos de las consultas jurídicas. Un registro por evento (creación, asignación, reasignación, cambio de etapa, respuesta, envío o devolución por el jefe, entre otros) de una consulta de legal_management.consultas_juridicas, con su descripción, detalle, usuario y fecha. |
| [`consultas_juridicas`](#consultas_juridicas) | Tabla | 31 | Registro de consultas y asesorías jurídicas internas de ESAP |
| [`correo_juridico_historial`](#correo_juridico_historial) | Tabla | 14558 | Historial de eventos de los correos jurídicos. Un registro por evento (recepción, clasificación automática o manual, asociación a un proceso, lectura, archivo, respuesta, entre otros) de un correo de legal_management.correos_juridicos, con su descripción, usuario y fecha. |
| [`correo_tracking_tokens`](#correo_tracking_tokens) | Tabla | 100 | Tokens de seguimiento de apertura de los correos jurídicos y de descarga de sus adjuntos. Un registro por token (píxel de apertura o enlace de descarga), asociado a un correo de legal_management.correos_juridicos y, si aplica, a un adjunto de legal_management.adjuntos_correo, con la fecha, la dirección IP y el navegador de apertura. |
| [`correos_juridicos`](#correos_juridicos) | Tabla | 14042 | Correos de los buzones jurídicos sincronizados desde Microsoft Graph y correos enviados desde la plataforma. Un registro por mensaje, con remitente, destinatarios, asunto, cuerpo, dirección (entrante o enviado), buzón, hilo de conversación y clasificación automática (tipo, categoría, módulo y proceso sugeridos). Se relaciona con sus adjuntos, comentarios, historial y tokens de seguimiento, y puede derivarse a un expediente o a una consulta jurídica. |
| [`decisiones_disciplinarias`](#decisiones_disciplinarias) | Tabla | 6 | Tabla para almacenar decisiones de procesos disciplinarios en el módulo de juzgamiento |
| [`documentos`](#documentos) | Tabla | 157 | Documentos asociados a expedientes judiciales |
| [`documentos_consulta`](#documentos_consulta) | Tabla | 25 | Documentos adjuntos a consultas jurídicas |
| [`documentos_oc`](#documentos_oc) | Tabla | 21 | Documentos asociados a los requerimientos de los organismos de control. Un registro por documento (oficio, respuesta, acuse, anexo, evidencia, informe u otro), asociado a un requerimiento de legal_management.requerimientos_oc, con su archivo, tamaño, tipo MIME, fecha y usuario que lo cargó. |
| [`evidencias`](#evidencias) | Tabla | 16 | Evidencias aportadas a los expedientes de la gestión jurídica. Un registro por evidencia, asociada a un expediente (legal_management.expedientes), con su descripción, quien la aportó, fecha de presentación, archivo, tipo y prioridad. Su estado pasa por pendiente, en revisión, admitida, válida o rechazada. |
| [`excepciones_procesales`](#excepciones_procesales) | Tabla | 2 | Excepciones procesales del módulo de Juzgamiento Disciplinario |
| [`expedientes`](#expedientes) | Tabla | 91 | Expedientes de los procesos de la gestión jurídica (defensa judicial, juzgamiento disciplinario y otros tipos de proceso configurados). Un registro por expediente, con su radicado, jurisdicción, tipo de proceso, partes, abogado sustanciador, etapa, términos procesales, provisión contable y estado de archivo. Es la tabla central del módulo: de ella dependen actas, actores, audiencias, autos, comentarios, decisiones, documentos, evidencias, excepciones, notas y tareas, y puede vincularse a un proceso principal. |
| [`hallazgos`](#hallazgos) | Tabla | 0 | Hallazgos de auditoría de los organismos de control y su plan de mejoramiento. Un registro por hallazgo, asociado a un requerimiento de legal_management.requerimientos_oc, con su tipo (administrativo, disciplinario, fiscal o penal), causa, efecto, acción correctiva, responsables, indicador, avance y periodicidad de reporte. Su estado pasa por abierto, en curso, en revisión, cerrado o rechazado. |
| [`historial_consultas`](#historial_consultas) | Tabla | 0 | Bitácora de cambios de las consultas jurídicas. Un registro por acción sobre una consulta de legal_management.consultas_juridicas, con su descripción, los estados anterior y nuevo, el usuario y la fecha. |
| [`notas_expediente`](#notas_expediente) | Tabla | 3 | Notas internas de los abogados sobre el expediente |
| [`oficios_enviados`](#oficios_enviados) | Tabla | 4 | Oficios judiciales enviados desde el sistema, con soporte para plantillas institucionales ESAP |
| [`organismos_control`](#organismos_control) | Tabla | 9 | Catálogo de organismos de control externos que emiten requerimientos a la entidad. Un registro por organismo, con su sigla, nombre, descripción, correos de contacto e indicador de activo. |
| [`pagos_coactivos`](#pagos_coactivos) | Tabla | 10 | Pagos registrados en los procesos de cobro coactivo. Un registro por pago de un proceso de legal_management.procesos_coactivos, con su valor, fecha, soporte, origen (banco o manual) y su distribución entre capital, intereses y costas. |
| [`pei_indicadores`](#pei_indicadores) | Tabla | 24 | Indicadores del plan estratégico institucional (PEI) de la gestión jurídica. Un registro por indicador, con su eje estratégico, meta, unidad de medida, plazo, frecuencia de medición, prioridad y responsable; sus avances se registran en legal_management.pei_registros_avance. Su estado es activo, inactivo o archivado. |
| [`pei_registros_avance`](#pei_registros_avance) | Tabla | 24 | Historial de avances de los indicadores del plan estratégico institucional (PEI). Un registro por reporte de avance de un indicador de legal_management.pei_indicadores, con el valor reportado, el porcentaje de avance frente a la meta, la justificación, la evidencia y el usuario que lo registró. |
| [`planes_comentarios`](#planes_comentarios) | Tabla | 0 | Comentarios registrados sobre los planes de mejoramiento. Un registro por comentario, asociado a un plan de legal_management.planes_mejoramiento, con el mensaje y el usuario autor. |
| [`planes_evidencias`](#planes_evidencias) | Tabla | 14 | Evidencias cargadas a los planes de mejoramiento. Un registro por archivo de evidencia, asociado a un plan de legal_management.planes_mejoramiento, con su título, URL, tipo de archivo y usuario que lo cargó. |
| [`planes_hallazgos`](#planes_hallazgos) | Tabla | 4 | Hallazgos o acciones de mejora asociados a los planes de mejoramiento. Un registro por hallazgo de un plan de legal_management.planes_mejoramiento, con su nombre, descripción, archivo de soporte y porcentaje de avance; el avance global del plan es el promedio de los avances de sus hallazgos. |
| [`planes_mejoramiento`](#planes_mejoramiento) | Tabla | 22 | Planes de mejoramiento de la entidad, originados en auditorías, organismos de control, autoevaluaciones o riesgos. Un registro por plan, con su código, origen, documento base, área y responsable, fechas, presupuesto, severidad y avance global; se relaciona con sus hallazgos, seguimientos, evidencias y comentarios. Su estado pasa por abierto, en ejecución, vencido o cerrado, y puede archivarse. |
| [`planes_seguimientos`](#planes_seguimientos) | Tabla | 22 | Bitácora de seguimiento de los planes de mejoramiento. Un registro por reporte de avance de un plan de legal_management.planes_mejoramiento, con la descripción, el porcentaje reportado, la fecha y el usuario que lo registró. |
| [`plantillas_documentos`](#plantillas_documentos) | Tabla | 5 | Plantillas de documentos Word de la gestión jurídica. Un registro por plantilla, con su nombre, categoría (actas, evidencias, oficios, pruebas, comunicaciones, notificaciones o documentos generales), archivo original, tipo MIME, tamaño, contenido en Base64 y usuario que la cargó. |
| [`procesos_coactivos`](#procesos_coactivos) | Tabla | 7 | Tabla de procesos de cobro coactivo - Módulo Gestión Legal |
| [`procesos_coactivos_adjuntos`](#procesos_coactivos_adjuntos) | Tabla | 13 | Archivos adjuntos de los procesos de cobro coactivo. Un registro por archivo, asociado a un proceso de legal_management.procesos_coactivos, con su nombre original y almacenado, tipo, tamaño, URL e indicador de si corresponde al título ejecutivo. |
| [`requerimientos_oc`](#requerimientos_oc) | Tabla | 14 | Requerimientos recibidos de los organismos de control. Un registro por requerimiento, con sus radicados externo e interno, organismo emisor, tipo, asunto, plazo y fecha de vencimiento, responsable, abogado asignado, prioridad y soportes de respuesta; se relaciona con sus comentarios, documentos, hallazgos, borradores de respuesta y solicitudes de insumos. Su estado pasa por recibido, en análisis, en respuesta, enviado, cerrado o vencido, y puede archivarse. |
| [`respuesta_borrador_oc`](#respuesta_borrador_oc) | Tabla | 2 | Almacena borradores de respuestas a requerimientos de órganos de control |
| [`riesgo_historial`](#riesgo_historial) | Tabla | 8 | Historial de cambios y eventos de riesgos para trazabilidad |
| [`riesgos`](#riesgos) | Tabla | 6 | Riesgos institucionales de la gestión jurídica. Un registro por riesgo, con su código, proceso, tipo (corrupción, fiscal, gestión o seguridad digital), valoración inherente y residual (probabilidad, impacto y zona), causas, consecuencias, controles, plan de tratamiento, responsable y provisión contable, y el proceso jurídico de origen cuando aplica; su historial se registra en legal_management.riesgo_historial. Avanza por etapas desde identificado hasta cerrado. |
| [`sequences`](#sequences) | Tabla | 1 | Consecutivos genéricos de la gestión jurídica para generar radicados legibles por año (por ejemplo, TERM-2026-0001). Un registro por nombre de secuencia (prefijo y año), con el último número asignado. |
| [`solicitudes_insumos`](#solicitudes_insumos) | Tabla | 0 | Solicitudes de insumos que se delegan a otras áreas para responder los requerimientos de los organismos de control. Un registro por solicitud, asociada a un requerimiento de legal_management.requerimientos_oc, con el área y el funcionario destinatarios, los documentos solicitados, los plazos, la respuesta y los documentos entregados. Su estado pasa por pendiente, en proceso, entregado, rechazado o vencido. |
| [`system_configurations`](#system_configurations) | Tabla | 8 | Parámetros de configuración de los módulos de la gestión jurídica (por ejemplo, columnas del tablero Kanban y tipos de proceso). Un registro por clave de configuración, con el módulo al que pertenece, su valor en formato JSON y su descripción. |
| [`tareas_expediente`](#tareas_expediente) | Tabla | 35 | Tareas asociadas a expedientes judiciales para control de actividades |
| [`tasas_referencia`](#tasas_referencia) | Tabla | 0 | Tasas de referencia mensuales para la liquidación de intereses en los procesos de cobro coactivo (Resolución 492). Un registro por año, mes y tipo de tasa (DIAN o usura), con su valor en porcentaje anual. |
| [`terminos_alertas_enviadas`](#terminos_alertas_enviadas) | Tabla | 109 | Registro de las alertas de vencimiento ya enviadas para cada término procesal, para no reenviar la misma alerta. Un registro por envío, asociado a un término de legal_management.terminos_procesales y a la regla de legal_management.terminos_reglas_alerta que lo disparó; sin regla, corresponde a la anticipación personalizada del propio término. |
| [`terminos_procesales`](#terminos_procesales) | Tabla | 233 | Torre de control transversal para vencimientos de términos procesales de todos los módulos |
| [`terminos_reglas_alerta`](#terminos_reglas_alerta) | Tabla | 2 | Reglas globales de alerta automática de vencimiento de los términos procesales. Un registro por regla, con las horas de anticipación al vencimiento, los canales de envío (correo electrónico o notificación en la aplicación) e indicador de activa; los envíos se registran en legal_management.terminos_alertas_enviadas. |

## actas

Actas de reuniones o sesiones de los expedientes de gestión jurídica. Un registro por acta, asociada a un expediente, con número, fecha, horario, duración, lugar, presidente, participantes, resumen, decisiones, tipo, estado (firmada o programada) y archivo del acta.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla actas. Se genera automáticamente. | PK |
| 2 | `expediente_id` | `uuid` | no | Referencia al registro de legal_management.expedientes (id). | FK→legal_management.expedientes.id |
| 3 | `numero_acta` | `character varying(100)` | sí | Número del acta. |  |
| 4 | `fecha` | `date` | sí | Fecha de la reunión o sesión que consta en el acta. |  |
| 5 | `horario` | `character varying(50)` | sí | Horario de la reunión registrada en el acta, en texto libre. |  |
| 6 | `duracion` | `character varying(50)` | sí | Duración de la reunión registrada en el acta, en texto libre. |  |
| 7 | `lugar` | `character varying(255)` | sí | Lugar donde se realizó la reunión. |  |
| 8 | `presidente` | `character varying(255)` | sí | Nombre de quien presidió la reunión. |  |
| 9 | `participantes` | `text` | sí | Participantes del acta, guardados como JSON o como lista separada por comas. |  |
| 10 | `resumen` | `text` | sí | Resumen del contenido del acta. |  |
| 11 | `decisiones_tomadas` | `text` | sí | Decisiones tomadas en la reunión. |  |
| 12 | `estado` | `character varying(50)` | sí | Estado del acta (Firmada o Programada). |  |
| 13 | `archivo_nombre` | `character varying(255)` | sí | Nombre del archivo del acta. |  |
| 14 | `archivo_url` | `text` | sí | URL del archivo del acta. |  |
| 15 | `archivo_tamano` | `integer` | sí | Tamaño del archivo del acta, en bytes. |  |
| 16 | `tipo` | `character varying(100)` | sí | Tipo de acta. |  |
| 17 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 18 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## actors

Actores de los expedientes de gestión jurídica: demandantes, demandados y otros. Un registro por actor de un expediente, con nombre, tipo de persona (natural o jurídica), identificación, rol, cargo, dependencia, apoderado y datos de contacto.

- Clave primaria: `id`
- Filas: 168
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla actors. Se genera automáticamente. | PK |
| 2 | `expediente_id` | `uuid` | no | Referencia al registro de legal_management.expedientes (id). | FK→legal_management.expedientes.id |
| 3 | `nombre` | `character varying(255)` | no | Nombre del actor del expediente. |  |
| 4 | `tipo_persona` | `character varying(50)` | no | Tipo de persona del actor. Valores: NATURAL, JURIDICA. |  |
| 5 | `identificacion` | `character varying(50)` | sí | Número de identificación del actor del expediente. |  |
| 6 | `rol` | `character varying(50)` | no | Rol del actor en el expediente. Valores: DEMANDANTE, DEMANDADO, OTRO. |  |
| 7 | `cargo` | `character varying(100)` | sí | Cargo del actor; opcional, para demandados y otros. |  |
| 8 | `email` | `character varying(255)` | sí | Correo electrónico del actor del expediente. | Contacto |
| 9 | `telefono` | `character varying(50)` | sí | Número de teléfono del actor del expediente. | Contacto |
| 10 | `direccion` | `character varying(255)` | sí | Dirección del actor del expediente. | Contacto |
| 11 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 13 | `apoderado` | `character varying(255)` | sí | Nombre del apoderado del actor. |  |
| 14 | `dependencia` | `character varying(150)` | sí | Dependencia del actor (parte del expediente: demandante, demandado u otro). |  |

## actuaciones

Historial unificado de actuaciones de los expedientes y procesos de la gestión jurídica. Un registro por actuación, con su tipo, fecha, documento soporte, responsable y origen (manual, audiencia, auto, acta, evidencia u oficio), y la referencia al registro que la generó. El expediente se identifica por texto, sin relación declarada con legal_management.expedientes.

- Clave primaria: `id`
- Filas: 427

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla actuaciones. Se genera automáticamente. | PK |
| 2 | `expediente_id` | `character varying(255)` | no | Identificador del expediente o proceso al que pertenece la actuación: GUID en procesos judiciales o radicado en procesos disciplinarios. No tiene clave foránea. |  |
| 3 | `tipo_actuacion` | `character varying(100)` | no | Tipo de actuación, en texto abierto sin catálogo cerrado. Por defecto, ACTUACION. Incluye, entre otros, AUTO_ADMISORIO, FALLO, NOTA_INTERNA, OFICIO, CAMBIO_ETAPA, PRUEBAS, EVIDENCIA, OTROS y el título de eventos automáticos. |  |
| 4 | `descripcion` | `text` | sí | Descripción de la actuación del expediente. |  |
| 5 | `fecha_actuacion` | `timestamp without time zone` | no | Fecha y hora de la actuación del expediente. |  |
| 6 | `documento_url` | `character varying(255)` | sí | URL del documento soporte de la actuación. |  |
| 7 | `documento_nombre` | `character varying(255)` | sí | Nombre del documento soporte de la actuación. |  |
| 8 | `usuario_responsable` | `character varying(100)` | sí | Nombre para mostrar del usuario responsable de la actuación. Valor por defecto: Sistema. El identificador del usuario (auth."user") que se notifica va en responsable_id. |  |
| 9 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 10 | `origen` | `character varying(50)` | sí | Origen de la actuación en el historial unificado. Valores: MANUAL, AUDIENCIA, AUTO, ACTA, EVIDENCIA, OFICIO. Por defecto, MANUAL. |  |
| 11 | `referencia_id` | `uuid` | sí | Identificador del registro original que generó la actuación (auto, audiencia, etc.). |  |
| 12 | `metadata` | `jsonb` | sí | Datos adicionales de la actuación, en formato JSON. |  |
| 13 | `responsable_id` | `character varying(255)` | sí | Identificador del usuario (auth."user") asignado como responsable de la actuación; se usa para notificarle la nueva actividad pendiente. |  |

## adjuntos_correo

Adjuntos de correos electrónicos sincronizados desde Microsoft Graph

- Clave primaria: `id`
- Filas: 2554
- Referencia a: `correo_id` → `legal_management.correos_juridicos` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla adjuntos_correo. Se genera automáticamente. | PK |
| 2 | `correo_id` | `uuid` | no | Referencia al registro de legal_management.correos_juridicos (id). | FK→legal_management.correos_juridicos.id |
| 3 | `graph_message_id` | `character varying(500)` | no | Identificador del mensaje en Microsoft Graph al que pertenece el adjunto. |  |
| 4 | `graph_attachment_id` | `character varying(500)` | no | ID del adjunto en Graph API, usado para descarga bajo demanda |  |
| 5 | `nombre` | `character varying(500)` | no | Nombre del archivo adjunto del correo electrónico. |  |
| 6 | `content_type` | `character varying(255)` | sí | Tipo de contenido (MIME) del adjunto. |  |
| 7 | `tamanio` | `integer` | sí | Tamaño del adjunto, en bytes. Valor por defecto: 0. |  |
| 8 | `archivo_local_url` | `text` | sí | Ruta local si el archivo fue descargado al servidor |  |
| 9 | `descargado` | `boolean` | sí | Indica si el adjunto del correo electrónico se descargó. |  |
| 10 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |

## audiencias

Audiencias programadas en los expedientes de la gestión jurídica. Un registro por audiencia, asociada a un expediente (legal_management.expedientes), con su fecha y hora, duración, modalidad (virtual o presencial), abogado responsable e historial de reprogramaciones. Su estado pasa por programada, realizada, cancelada o aplazada.

- Clave primaria: `id`
- Filas: 18
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla audiencias. Se genera automáticamente. | PK |
| 2 | `expediente_id` | `uuid` | no | Referencia al registro de legal_management.expedientes (id). | FK→legal_management.expedientes.id |
| 3 | `abogado_id` | `uuid` | no | Identificador del abogado responsable de la audiencia. Tenía FK a la tabla abogados, que fue eliminada al pasar a la autenticación federada. |  |
| 4 | `titulo` | `character varying(255)` | no | Título de la audiencia. |  |
| 5 | `fecha_hora_inicio` | `timestamp without time zone` | no | Fecha y hora de inicio de la audiencia. |  |
| 6 | `duracion_minutos` | `integer` | no | Duración de la audiencia, en minutos. |  |
| 7 | `modalidad` | `character varying(50)` | no | Modalidad de la audiencia. Valores: VIRTUAL, PRESENCIAL. |  |
| 8 | `ubicacion` | `character varying(255)` | sí | Lugar de realización de la audiencia. |  |
| 9 | `link_reunion` | `text` | sí | Enlace de la reunión virtual de la audiencia. |  |
| 10 | `estado` | `character varying(50)` | sí | Estado de la audiencia. Valores: PROGRAMADA, REALIZADA, CANCELADA, APLAZADA. Por defecto, PROGRAMADA. |  |
| 11 | `notas_preparacion` | `text` | sí | Notas de preparación de la audiencia, registradas al crearla o editarla. |  |
| 12 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 13 | `historial` | `jsonb` | sí | Historial de reprogramaciones de la audiencia, en formato JSON. Cada elemento tiene fechaOriginal, fechaNueva, motivo, detalle, registradoPor y fechaRegistro; se agrega cuando se informa un motivo de reasignación. Valor por defecto: arreglo vacío. |  |
| 14 | `abogado_nombre` | `character varying(255)` | sí | Nombre del abogado responsable de la audiencia. |  |
| 15 | `abogado_email` | `character varying(255)` | sí | Correo electrónico del abogado responsable de la audiencia. | Contacto |

## autos

Autos emitidos dentro de los expedientes de la gestión jurídica. Un registro por auto, asociado a un expediente (legal_management.expedientes), con su número, tipo, fecha, juzgado, resumen y archivo. Su estado pasa por pendiente, notificado o archivado.

- Clave primaria: `id`
- Filas: 4
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla autos. Se genera automáticamente. | PK |
| 2 | `expediente_id` | `uuid` | no | Referencia al registro de legal_management.expedientes (id). | FK→legal_management.expedientes.id |
| 3 | `numero` | `character varying` | no | Número del auto (por ejemplo, AUTO-001-2024). |  |
| 4 | `tipo` | `character varying` | no | Tipo de auto (por ejemplo, Auto Admisorio), enviado como texto desde el formulario. |  |
| 5 | `fecha_auto` | `timestamp without time zone` | no | Fecha y hora del auto. |  |
| 6 | `juzgado` | `character varying` | no | Juzgado que emite el auto. Valor por defecto: Juzgado Interno Disciplinario. |  |
| 7 | `resumen` | `text` | sí | Resumen del contenido del auto. |  |
| 8 | `estado` | `character varying` | no | Estado del auto. Valores: Pendiente, Notificado, Archivado. Por defecto, Pendiente. |  |
| 9 | `fecha_notificacion` | `timestamp without time zone` | sí | Fecha y hora de notificación del auto. |  |
| 10 | `archivo_url` | `character varying` | no | URL del archivo del auto. Obligatoria. |  |
| 11 | `archivo_nombre` | `character varying` | no | Nombre del archivo del auto. |  |
| 12 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 13 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## borradores_correos

Borradores privados de correos nuevos del Centro de Comunicaciones (Redactar Correo). Se autoguardan y se eliminan al enviarse.

- Clave primaria: `id`
- Filas: 2

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla borradores_correos. Se genera automáticamente. | PK |
| 2 | `usuario_id` | `character varying(100)` | no | Identificador del usuario propietario del borrador; cada usuario solo ve sus propios borradores. |  |
| 3 | `usuario_nombre` | `character varying(255)` | sí | Nombre del usuario dueño del borrador. |  |
| 4 | `buzon` | `character varying(20)` | no | Cuenta remitente/bandeja de origen (JUDICIAL \| CORREOS) para restaurar el remitente correcto al reabrir. |  |
| 5 | `destinatarios_to` | `text` | sí | Destinatarios principales («Para») del borrador, como arreglo JSON de correos en texto. |  |
| 6 | `destinatarios_cc` | `text` | sí | Destinatarios en copia (CC) del borrador. |  |
| 7 | `destinatarios_cco` | `text` | sí | Destinatarios en copia oculta (CCO) del borrador. |  |
| 8 | `asunto` | `character varying(500)` | sí | Asunto del correo en borrador. |  |
| 9 | `cuerpo` | `text` | sí | Cuerpo del correo nuevo en redacción, autoguardado en el borrador privado del usuario. |  |
| 10 | `adjuntos` | `jsonb` | no | Adjuntos embebidos como arreglo JSON base64: [{ name, contentType, contentBytes, size }]. Límite ~25MB aplicado en el frontend. |  |
| 11 | `solicitar_acuse` | `boolean` | no | Indica si el usuario dejó marcada la opción «solicitar acuse de recibido» en el borrador. |  |
| 12 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 13 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## cat_tipos_requerimiento

Catálogo de tipos de requerimiento de los organismos de control. Un registro por tipo, con nombre, descripción, orden de presentación e indicador de activo; legal_management.requerimientos_oc toma de aquí su tipo de requerimiento.

- Clave primaria: `id`
- Filas: 9

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `character varying(50)` | no | Identificador único del registro en la tabla cat_tipos_requerimiento. | PK |
| 2 | `nombre` | `character varying(200)` | no | Nombre del tipo de requerimiento. |  |
| 3 | `descripcion` | `text` | sí | Descripción del tipo de requerimiento. |  |
| 4 | `activo` | `boolean` | sí | Indica si el tipo de requerimiento está activo. |  |
| 5 | `orden` | `integer` | sí | Posición del tipo de requerimiento en el ordenamiento. |  |
| 6 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 7 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## coactivos_historial

Historial de eventos de los procesos de cobro coactivo. Un registro por evento (creación, pago, cambio de etapa o actualización) de un proceso de legal_management.procesos_coactivos, con el campo modificado, sus valores anterior y nuevo, el usuario y la fecha.

- Clave primaria: `id`
- Filas: 48
- Referencia a: `proceso_id` → `legal_management.procesos_coactivos` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla coactivos_historial. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de legal_management.procesos_coactivos (id). | FK→legal_management.procesos_coactivos.id |
| 3 | `tipo_evento` | `character varying(50)` | no | Tipo de evento del historial del proceso coactivo. Valores: CREACION, PAGO, CAMBIO_ETAPA, ACTUALIZACION. |  |
| 4 | `campo_modificado` | `character varying(100)` | sí | Nombre del campo modificado en el evento: deudor, obligacion.valor o responsable (ACTUALIZACION), estado (CAMBIO_ETAPA), estadoArchivo (ARCHIVADO, RESTAURADO, ELIMINADO) o valorPagado (PAGO, ELIMINACION_PAGO). Queda vacío en CREACION. |  |
| 5 | `valor_anterior` | `text` | sí | Valor del campo antes de la modificación. |  |
| 6 | `valor_nuevo` | `text` | sí | Valor del campo después de la modificación. |  |
| 7 | `usuario` | `character varying(100)` | sí | Identificador o nombre del usuario responsable del evento. |  |
| 8 | `detalles` | `text` | sí | Descripción en texto del evento del historial (por ejemplo, cambio de responsable o motivo del archivo). |  |
| 9 | `fecha_evento` | `timestamp without time zone` | sí | Fecha y hora del evento en el historial del proceso coactivo. |  |

## comentarios

Comentarios registrados sobre los expedientes de la gestión jurídica. Un registro por comentario, asociado a un expediente (legal_management.expedientes), con su texto y el usuario autor.

- Clave primaria: `id`
- Filas: 9
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla comentarios. Se genera automáticamente. | PK |
| 2 | `expediente_id` | `uuid` | no | Referencia al registro de legal_management.expedientes (id). | FK→legal_management.expedientes.id |
| 3 | `contenido` | `text` | no | Texto del comentario. |  |
| 4 | `usuario_id` | `character varying(255)` | sí | Identificador del usuario autor del comentario, enviado por el cliente; el nombre va en usuario_nombre. |  |
| 5 | `usuario_nombre` | `character varying(255)` | no | Nombre del usuario autor del comentario. |  |
| 6 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 7 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## comentarios_consulta

Comentarios registrados sobre las consultas jurídicas. Un registro por comentario, asociado a una consulta de legal_management.consultas_juridicas, con el mensaje, el usuario autor, su cargo y la fecha.

- Clave primaria: `id`
- Filas: 2
- Referencia a: `consulta_id` → `legal_management.consultas_juridicas` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla comentarios_consulta. Se genera automáticamente. | PK |
| 2 | `consulta_id` | `uuid` | no | Referencia al registro de legal_management.consultas_juridicas (id). | FK→legal_management.consultas_juridicas.id |
| 3 | `mensaje` | `text` | no | Texto del comentario sobre la consulta jurídica. |  |
| 4 | `usuario` | `character varying(255)` | no | Usuario autor del comentario, enviado por el cliente; Sistema cuando no se informa. |  |
| 5 | `cargo` | `character varying(255)` | sí | Cargo del usuario autor del comentario. |  |
| 6 | `fecha` | `timestamp without time zone` | sí | Fecha y hora del comentario. Valor por defecto: momento del registro. |  |

## comentarios_correo

Comentarios del tab "Comentarios" en el Detalle de Comunicación (Centro de Comunicaciones).

- Clave primaria: `id`
- Filas: 2
- Referencia a: `correo_id` → `legal_management.correos_juridicos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla comentarios_correo. Se genera automáticamente. | PK |
| 2 | `correo_id` | `uuid` | no | Referencia al registro de legal_management.correos_juridicos (id). | FK→legal_management.correos_juridicos.id |
| 3 | `mensaje` | `character varying` | no | Texto del comentario sobre la comunicación. |  |
| 4 | `usuario` | `character varying` | no | Usuario autor del comentario, enviado por el cliente; Sistema cuando no se informa. |  |
| 5 | `cargo` | `character varying` | sí | Cargo del usuario autor del comentario. |  |
| 6 | `fecha` | `timestamp without time zone` | sí | Fecha y hora del comentario. Valor por defecto: momento del registro. |  |

## comentarios_oc

Comentarios registrados sobre los requerimientos de los organismos de control. Un registro por comentario, asociado a un requerimiento de legal_management.requerimientos_oc, con su tipo, contenido y autor.

- Clave primaria: `id`
- Filas: 28
- Referencia a: `requerimiento_id` → `legal_management.requerimientos_oc` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla comentarios_oc. Se genera automáticamente. | PK |
| 2 | `requerimiento_id` | `uuid` | no | Referencia al registro de legal_management.requerimientos_oc (id). | FK→legal_management.requerimientos_oc.id |
| 3 | `contenido` | `text` | no | Texto del comentario sobre el requerimiento. |  |
| 4 | `tipo` | `character varying(30)` | sí | Tipo de comentario del requerimiento (ACTUACION, ALERTA, COMENTARIO, actuacion, alerta, general, importante, interno, respuesta o seguimiento). |  |
| 5 | `autor_id` | `uuid` | sí | Identificador del usuario autor del comentario. |  |
| 6 | `autor_nombre` | `character varying(200)` | sí | Nombre del autor del comentario. |  |
| 7 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 8 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## conceptos_juridicos

Conceptos jurídicos emitidos en respuesta a las consultas de asesoría jurídica. Un registro por concepto (concepto, memorando, revisión o viabilidad), asociado a una consulta de legal_management.consultas_juridicas, con su análisis, normatividad, conclusión, redactor, revisión, aprobación y emisión. Su estado pasa por borrador, en revisión, devuelto, aprobado o emitido, y puede publicarse en el banco de conceptos.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `consulta_id` → `legal_management.consultas_juridicas` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla conceptos_juridicos. Se genera automáticamente. | PK |
| 2 | `consulta_id` | `uuid` | no | Referencia al registro de legal_management.consultas_juridicas (id). | FK→legal_management.consultas_juridicas.id |
| 3 | `numero_concepto` | `character varying(50)` | no | Número del concepto jurídico. Es único en la tabla. | única |
| 4 | `tipo_documento` | `character varying(30)` | sí | Tipo de documento jurídico. Valores permitidos: CONCEPTO, MEMORANDO, REVISION, VIABILIDAD. Valor por defecto: CONCEPTO. |  |
| 5 | `titulo` | `character varying(300)` | no | Título del concepto jurídico. |  |
| 6 | `resumen` | `text` | sí | Resumen del concepto jurídico. |  |
| 7 | `analisis_juridico` | `text` | no | Análisis jurídico que sustenta el concepto. |  |
| 8 | `normatividad_aplicable` | `text` | sí | Normas aplicables al caso analizado en el concepto. |  |
| 9 | `conclusion` | `text` | no | Conclusión del concepto jurídico. |  |
| 10 | `recomendaciones` | `text` | sí | Recomendaciones del concepto jurídico. |  |
| 11 | `documento_pdf_url` | `character varying(500)` | sí | URL del documento PDF del concepto. |  |
| 12 | `estado` | `character varying(20)` | sí | Estado del concepto jurídico (APROBADO, BORRADOR, DEVUELTO, EMITIDO o EN_REVISION). |  |
| 13 | `abogado_redactor_id` | `uuid` | sí | Identificador del abogado que redactó el concepto. Tenía FK a la tabla abogados, eliminada al pasar a la autenticación federada. |  |
| 14 | `abogado_redactor_nombre` | `character varying(150)` | sí | Nombre del abogado que redactó el concepto. |  |
| 15 | `revisor_id` | `uuid` | sí | Identificador del usuario que revisó el concepto. |  |
| 16 | `revisor_nombre` | `character varying(150)` | sí | Nombre del usuario que revisó el concepto. |  |
| 17 | `fecha_revision` | `timestamp without time zone` | sí | Fecha y hora de revisión del concepto jurídico. |  |
| 18 | `comentarios_revision` | `text` | sí | Comentarios de la revisión del concepto. |  |
| 19 | `aprobado_por` | `character varying(150)` | sí | Usuario que realizó la aprobación. |  |
| 20 | `fecha_aprobacion` | `timestamp without time zone` | sí | Fecha y hora de aprobación del concepto jurídico. |  |
| 21 | `fecha_emision` | `timestamp without time zone` | sí | Fecha y hora de emisión del concepto jurídico. |  |
| 22 | `notificado_a` | `character varying(300)` | sí | Personas o dependencias a las que se notificó el concepto. |  |
| 23 | `visible_banco` | `boolean` | sí | Indica si el concepto jurídico es visible en el banco de conceptos. |  |
| 24 | `etiquetas` | `text[]` | sí | Etiquetas para clasificar y buscar el concepto. |  |
| 25 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 26 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## consulta_juridica_historial

Historial de eventos de las consultas jurídicas. Un registro por evento (creación, asignación, reasignación, cambio de etapa, respuesta, envío o devolución por el jefe, entre otros) de una consulta de legal_management.consultas_juridicas, con su descripción, detalle, usuario y fecha.

- Clave primaria: `id`
- Filas: 132
- Referencia a: `consulta_id` → `legal_management.consultas_juridicas` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla consulta_juridica_historial. Se genera automáticamente. | PK |
| 2 | `consulta_id` | `uuid` | no | Referencia al registro de legal_management.consultas_juridicas (id). | FK→legal_management.consultas_juridicas.id |
| 3 | `tipo_evento` | `character varying` | no | Tipo de evento del historial de la consulta jurídica: CREACIÓN, ASIGNACIÓN, REASIGNACIÓN, CAMBIO_ETAPA, RESPUESTA, ENVIADO_A_JEFE, DEVUELTA_POR_JEFE, ARCHIVADO, ELIMINADO_SOFT, RESTAURADO, VENCIMIENTO o ALERTA_VENCIMIENTO. |  |
| 4 | `descripcion` | `text` | no | Descripción del evento en el historial de la consulta jurídica. |  |
| 5 | `detalle` | `text` | sí | Detalle adicional del evento, en texto plano (por ejemplo, radicado, nueva etapa, número de oficio y tipo de respuesta, o motivo de la devolución). |  |
| 6 | `usuario` | `character varying` | sí | Usuario que generó el evento: el nombre del solicitante en la creación, Sistema o Sistema (Cron) en eventos automáticos, o el valor que envía el cliente en las demás acciones. |  |
| 7 | `fecha` | `timestamp without time zone` | no | Fecha y hora del evento. Valor por defecto: momento del registro. |  |

## consultas_juridicas

Registro de consultas y asesorías jurídicas internas de ESAP

- Clave primaria: `id`
- Filas: 31

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla consultas_juridicas. Se genera automáticamente. | PK |
| 2 | `numero_radicado` | `character varying(50)` | no | Número de radicado de la consulta jurídica. Es único en la tabla. | única |
| 3 | `tipo_solicitud` | `character varying(30)` | sí | Tipo de solicitud. Valores: consulta, concepto_juridico, control_legalidad. |  |
| 4 | `area_solicitante` | `character varying(100)` | sí | Área que solicita la consulta. |  |
| 5 | `funcionario_solicitante` | `character varying(150)` | sí | Nombre del funcionario que solicita la consulta. |  |
| 6 | `cargo_solicitante` | `character varying(100)` | sí | Cargo del funcionario solicitante. |  |
| 7 | `email_solicitante` | `character varying(150)` | sí | Correo electrónico del solicitante. | Contacto |
| 8 | `telefono_solicitante` | `character varying(20)` | sí | Teléfono del solicitante. | Contacto |
| 9 | `asunto` | `character varying(300)` | sí | Asunto de la consulta jurídica. |  |
| 10 | `descripcion` | `text` | sí | Descripción de la consulta jurídica. |  |
| 11 | `antecedentes` | `text` | sí | Antecedentes de la consulta jurídica. |  |
| 12 | `documentos_soporte_urls` | `text[]` | sí | URL de los documentos soporte de la consulta. |  |
| 13 | `tema_principal` | `character varying(100)` | sí | Tema principal de la consulta. |  |
| 14 | `palabras_clave` | `text[]` | sí | Palabras clave de la consulta. |  |
| 15 | `abogado_asignado_id` | `uuid` | sí | Identificador (UUID) del usuario (auth."user", id_user) asignado a la consulta. Tenía FK a la tabla abogados, eliminada al pasar a la autenticación federada. |  |
| 16 | `abogado_asignado_nombre` | `character varying(150)` | sí | Nombre del abogado asignado a la consulta. |  |
| 17 | `fecha_asignacion` | `timestamp without time zone` | sí | Fecha y hora de asignación de la consulta jurídica. |  |
| 18 | `estado` | `character varying(30)` | sí | Estado de la consulta jurídica. Valores posibles: en_radicacion, asignado, en_analisis, en_revision, pendiente_revision_jefe, devuelta_por_jefe, respondido, cerrado, vencido. La aplicación siempre fija el estado al crear (en_radicacion o asignado); el defecto RADICADA de la base viene de la versión inicial de la tabla. |  |
| 19 | `fecha_radicacion` | `timestamp without time zone` | sí | Fecha y hora de radicación de la consulta jurídica. |  |
| 20 | `fecha_vencimiento` | `timestamp without time zone` | sí | Fecha y hora de vencimiento de la consulta jurídica. |  |
| 21 | `dias_termino` | `integer` | sí | Días de término para responder la consulta. Valor por defecto: 30. Columna de la versión inicial; la aplicación usa termino_legal_dias. |  |
| 22 | `dias_transcurridos` | `integer` | sí | Días transcurridos desde la radicación de la consulta. Valor por defecto: 0. |  |
| 23 | `suspendida` | `boolean` | sí | Indica si la consulta jurídica está suspendida. |  |
| 24 | `fecha_suspension` | `timestamp without time zone` | sí | Fecha y hora de suspensión de la consulta jurídica. |  |
| 25 | `motivo_suspension` | `text` | sí | Motivo de la suspensión. |  |
| 26 | `confidencial` | `boolean` | sí | Indica si la consulta jurídica es confidencial. |  |
| 27 | `areas_con_acceso` | `text[]` | sí | Áreas con acceso a la consulta cuando es confidencial. |  |
| 28 | `prioridad` | `character varying(20)` | sí | Prioridad de la consulta: alta, media o baja. La aplicación asigna media al crear si no se informa y la cambia a alta cuando faltan 3 días o menos para el vencimiento; el defecto NORMAL de la base viene de la versión inicial de la tabla. |  |
| 29 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 30 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 31 | `created_by` | `character varying(150)` | sí | Usuario que creó el registro. |  |
| 32 | `updated_by` | `character varying(150)` | sí | Usuario que realizó la última actualización del registro. |  |
| 33 | `fecha_recepcion` | `timestamp without time zone` | sí | Fecha y hora de recepción de la consulta jurídica. |  |
| 34 | `termino_legal_dias` | `integer` | sí | Término legal de 30 días hábiles según CPACA Art. 50 |  |
| 35 | `fecha_maxima_respuesta` | `timestamp without time zone` | sí | Fecha y hora máxima para responder la consulta jurídica. |  |
| 36 | `fecha_respuesta` | `timestamp without time zone` | sí | Fecha y hora de respuesta de la consulta jurídica. |  |
| 37 | `observaciones` | `text` | sí | Observaciones sobre la consulta jurídica. |  |
| 38 | `canal_entrada` | `character varying(30)` | sí | Canal por el que ingresó la consulta. Valores: correo_electronico, active_document, ventanilla_unica. |  |
| 39 | `dependencia_solicitante` | `character varying(200)` | sí | Dependencia que solicita la consulta. Es la columna que usa la aplicación; area_solicitante viene de la versión inicial de la tabla y no está mapeada en la entidad. |  |
| 40 | `nombre_solicitante` | `character varying(200)` | sí | Nombre del solicitante de la consulta. Es la columna que usa la aplicación (también como autor del evento de creación); funcionario_solicitante viene de la versión inicial de la tabla y no está mapeada en la entidad. |  |
| 41 | `tipo_usuario` | `character varying(20)` | sí | Tipo de usuario solicitante. Valores: interno, externo. Por defecto, interno. |  |
| 42 | `materia_juridica` | `character varying(30)` | sí | Materia jurídica de la consulta. Valores: laboral, contractual, administrativo, disciplinario, presupuestal, academico, otra. |  |
| 43 | `complejidad` | `character varying(10)` | sí | Complejidad de la consulta. Valores: alta, media, baja. |  |
| 44 | `numero_oficio_respuesta` | `character varying(50)` | sí | Número del oficio con que se respondió la consulta, digitado al registrar la respuesta. |  |
| 45 | `tipo_respuesta` | `character varying(30)` | sí | Tipo de respuesta. Valores: favorable, con_observaciones, desfavorable, informativa. |  |
| 46 | `documento_respuesta_url` | `text` | sí | URL del documento de respuesta a la consulta. |  |
| 47 | `respuesta` | `text` | sí | Texto de la respuesta a la consulta. |  |
| 48 | `estado_archivo` | `character varying` | sí | Estado de archivo de la consulta. Valores: ACTIVO, ARCHIVADO, ELIMINADO. Por defecto, ACTIVO. |  |
| 49 | `fecha_archivo` | `timestamp without time zone` | sí | Fecha y hora de archivo de la consulta jurídica. |  |
| 50 | `usuario_archivo` | `character varying` | sí | Usuario que archivó la consulta. |  |
| 51 | `motivo_archivo` | `text` | sí | Motivo del archivo. |  |
| 52 | `destinatarios_adicionales` | `text` | sí | JSON array con los emails adicionales a los que se envió la respuesta, ej: ["a@b.com","c@d.com"] |  |
| 53 | `comentario_devolucion_jefe` | `text` | sí | Comentario del jefe al devolver la respuesta al abogado para ajustes. Se borra cuando el abogado reenvía al jefe o cuando el jefe aprueba. |  |
| 54 | `origen_comunicacion_id` | `uuid` | sí | Identificador de la comunicación (correo jurídico) que dio origen a la consulta cuando se crea desde el Centro de Comunicaciones (Clasificación IA). |  |

## correo_juridico_historial

Historial de eventos de los correos jurídicos. Un registro por evento (recepción, clasificación automática o manual, asociación a un proceso, lectura, archivo, respuesta, entre otros) de un correo de legal_management.correos_juridicos, con su descripción, usuario y fecha.

- Clave primaria: `id`
- Filas: 14558
- Referencia a: `correo_juridico_id` → `legal_management.correos_juridicos` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla correo_juridico_historial. Se genera automáticamente. | PK |
| 2 | `correo_juridico_id` | `uuid` | no | Referencia al registro de legal_management.correos_juridicos (id). | FK→legal_management.correos_juridicos.id |
| 3 | `tipo_evento` | `character varying(50)` | no | Tipo de evento del historial del correo jurídico. Valores: RECIBIDO, CLASIFICADO_IA, CLASIFICACION_MANUAL, ASOCIADO_PROCESO, LEIDO, ARCHIVADO, RESPONDIDO, REENVIADO. |  |
| 4 | `descripcion` | `text` | no | Descripción del evento en el historial del correo jurídico. |  |
| 5 | `detalle_json` | `jsonb` | sí | Detalle del evento del correo, en formato JSON. |  |
| 6 | `usuario` | `character varying(255)` | sí | Usuario que generó el evento. Valor por defecto: Sistema. |  |
| 7 | `fecha_creacion` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |

## correo_tracking_tokens

Tokens de seguimiento de apertura de los correos jurídicos y de descarga de sus adjuntos. Un registro por token (píxel de apertura o enlace de descarga), asociado a un correo de legal_management.correos_juridicos y, si aplica, a un adjunto de legal_management.adjuntos_correo, con la fecha, la dirección IP y el navegador de apertura.

- Clave primaria: `id`
- Filas: 100
- Referencia a: `adjunto_id` → `legal_management.adjuntos_correo` (0..1 → 0..1); `correo_id` → `legal_management.correos_juridicos` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla correo_tracking_tokens. Se genera automáticamente. | PK |
| 2 | `correo_id` | `uuid` | no | Referencia al registro de legal_management.correos_juridicos (id). | FK→legal_management.correos_juridicos.id |
| 3 | `adjunto_id` | `uuid` | sí | Referencia al registro de legal_management.adjuntos_correo (id). | FK→legal_management.adjuntos_correo.id |
| 4 | `token` | `character varying(100)` | no | Token único de seguimiento de apertura del correo o adjunto. | única Credencial de acceso |
| 5 | `tipo` | `character varying(20)` | no | Tipo de token de seguimiento del correo. Valores permitidos: OPEN_PIXEL (píxel de apertura), DOWNLOAD_LINK (enlace de descarga). |  |
| 6 | `abierto` | `boolean` | no | Indica si se abrió el correo o el adjunto rastreado. |  |
| 7 | `fecha_apertura` | `timestamp without time zone` | sí | Fecha y hora de apertura del correo o el adjunto rastreado. |  |
| 8 | `ip_apertura` | `character varying(50)` | sí | Dirección IP desde la que se abrió el correo o adjunto. | Identificador en línea (IP) |
| 9 | `user_agent` | `text` | sí | Agente de usuario (navegador) registrado al abrir el correo o el adjunto rastreado. |  |
| 10 | `destinatario_email` | `character varying(255)` | sí | Correo electrónico del destinatario original del mensaje, guardado como contexto. | Contacto |
| 11 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |

## correos_juridicos

Correos de los buzones jurídicos sincronizados desde Microsoft Graph y correos enviados desde la plataforma. Un registro por mensaje, con remitente, destinatarios, asunto, cuerpo, dirección (entrante o enviado), buzón, hilo de conversación y clasificación automática (tipo, categoría, módulo y proceso sugeridos). Se relaciona con sus adjuntos, comentarios, historial y tokens de seguimiento, y puede derivarse a un expediente o a una consulta jurídica.

- Clave primaria: `id`
- Filas: 14042
- Referencia a: `parent_email_id` → `legal_management.correos_juridicos` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla correos_juridicos. Se genera automáticamente. | PK |
| 2 | `graph_message_id` | `character varying(500)` | no | Identificador del mensaje en Microsoft Graph. Es único en la tabla. | única |
| 3 | `asunto` | `character varying(500)` | no | Asunto del correo. |  |
| 4 | `remitente_email` | `character varying(255)` | no | Correo electrónico del remitente. |  |
| 5 | `remitente_nombre` | `character varying(255)` | sí | Nombre del remitente. |  |
| 6 | `destinatarios` | `text` | sí | Destinatarios en copia (CC) del correo, como arreglo JSON de correos. |  |
| 7 | `fecha_recepcion` | `timestamp without time zone` | no | Fecha y hora de recepción del correo jurídico. |  |
| 8 | `cuerpo_html` | `text` | sí | Cuerpo del correo en formato HTML. |  |
| 9 | `cuerpo_texto` | `text` | sí | Cuerpo del correo en texto plano. |  |
| 10 | `tiene_adjuntos` | `boolean` | sí | Indica si el correo jurídico tiene adjuntos. |  |
| 11 | `leido` | `boolean` | sí | Indica si el correo jurídico fue leído. |  |
| 12 | `archivado` | `boolean` | sí | Indica si el correo jurídico está archivado. |  |
| 13 | `urgente` | `boolean` | sí | Indica si el correo jurídico está marcado como urgente. |  |
| 14 | `tipo` | `character varying(20)` | sí | Clasificación del correo. Valores: JUDICIAL, CORREO, OFICIO. Por defecto, CORREO. |  |
| 15 | `categoria` | `character varying(100)` | sí | Categoría del correo: la que asigna la clasificación automática (JUDICIAL, OFICIO, CONSULTA o CORREO), la que corrige un usuario, la heredada del hilo, o ENVIADO, RESPUESTA o REENVIO en correos salientes. tipo se deriva de ella (JUDICIAL, OFICIO o CORREO) y ai_suggested_category conserva la categoría automática. |  |
| 16 | `modulo_sugerido` | `character varying(100)` | sí | Módulo de gestión jurídica sugerido para el correo (MOD-01: Defensa Judicial, MOD-02: Juzgamiento Disciplinario, MOD-03: Asesoría Jurídica o Buzón General). Lo calcula la clasificación automática con reglas heurísticas y un clasificador bayesiano, y se recalcula si un usuario corrige la categoría. |  |
| 17 | `confianza_clasificacion` | `double precision` | sí | Nivel de confianza de la clasificación automática del correo, en escala de 0 a 1. |  |
| 18 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 19 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 20 | `ai_suggested_category` | `character varying(100)` | sí | Categoría del correo sugerida por inteligencia artificial. |  |
| 21 | `is_trained` | `boolean` | sí | Indica si el correo jurídico está marcado como entrenado. |  |
| 22 | `expediente_id` | `character varying(255)` | sí | Identificador (expedientes.id, guardado como texto) del expediente de Defensa Judicial o Juzgamiento Disciplinario al que se asoció el correo; las consultas de Asesoría Jurídica van en consulta_id. |  |
| 23 | `direccion` | `character varying(20)` | sí | Dirección del correo. Valores: ENTRANTE, ENVIADO. Por defecto, ENTRANTE. |  |
| 24 | `destinatarios_to` | `text` | sí | Destinatarios principales («Para») de los correos enviados, respuestas y reenvíos, como lista de correos separada por coma y espacio (no JSON). |  |
| 25 | `is_forwarded` | `boolean` | sí | Indica si el correo jurídico fue reenviado. |  |
| 26 | `is_replied` | `boolean` | sí | Indica si el correo fue respondido. |  |
| 27 | `parent_email_id` | `uuid` | sí | Referencia al registro de legal_management.correos_juridicos (id). | FK→legal_management.correos_juridicos.id |
| 28 | `thread_id` | `character varying(500)` | sí | Identificador del hilo de conversación del correo. |  |
| 29 | `internet_message_id` | `character varying(500)` | sí | Identificador del mensaje en Internet (cabecera Message-ID). |  |
| 30 | `proceso_id_sugerido` | `character varying(100)` | sí | Radicado del proceso detectado en el asunto o cuerpo del correo por la extracción automática de entidades (patrones PD-AAAA-N, DJ-AAAA-N, RAD., EXP. o radicado judicial), o radicado informado al registrar un traslado. No es el identificador interno del expediente. |  |
| 31 | `implicado_sugerido` | `character varying(255)` | sí | Nombre del implicado detectado en el texto del correo por la extracción automática de entidades (después de palabras como contra, investigado o demandado). |  |
| 32 | `submodulo_sugerido` | `character varying(100)` | sí | Submódulo sugerido por la extracción automática de entidades del correo: DEFENSA_JUDICIAL o JUZGAMIENTO_DISCIPLINARIO. |  |
| 33 | `buzon` | `character varying(20)` | no | Buzón de origen: cuenta de correo desde la que se sincronizó el mensaje; separa la bandeja JUDICIAL (Judiciales/Oficios) de la bandeja CORREOS. Valores: JUDICIAL, CORREOS. Por defecto, JUDICIAL. |  |
| 34 | `destinatarios_cco` | `text` | sí | Destinatarios en Copia Oculta (CCO/BCC), como arreglo JSON de correos. No visibles para los demás destinatarios; se conservan para trazabilidad. |  |
| 35 | `consulta_id` | `uuid` | sí | Identificador de la consulta de Asesoría Jurídica (consultas_juridicas) a la que se derivó la comunicación. |  |
| 36 | `modulo_destino` | `character varying(50)` | sí | Módulo al que se derivó la comunicación. Valores: DEFENSA_JUDICIAL, JUZGAMIENTO_DISCIPLINARIO, ASESORIA_JURIDICA. |  |

## decisiones_disciplinarias

Tabla para almacenar decisiones de procesos disciplinarios en el módulo de juzgamiento

- Clave primaria: `id`
- Filas: 6
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla decisiones_disciplinarias. Se genera automáticamente. | PK |
| 2 | `tipo_decision` | `character varying(100)` | no | Tipo de decisión: AUTO_DE_FALLO, ARCHIVO, SUSPENSION, etc. |  |
| 3 | `tipo_fallo` | `character varying(100)` | no | Tipo de fallo: ABSOLUTORIO, CONDENATORIO, INHIBITORIO |  |
| 4 | `sancion` | `character varying(255)` | sí | Tipo de sanción aplicada en la decisión, si aplica. |  |
| 5 | `consideraciones` | `text` | no | Consideraciones del fallo. |  |
| 6 | `fundamentos_juridicos` | `text` | sí | Fundamentos legales de la decisión. |  |
| 7 | `responsable` | `character varying(255)` | no | Nombre del funcionario que toma la decisión. |  |
| 8 | `cargo_responsable` | `character varying(255)` | sí | Cargo del funcionario que toma la decisión. |  |
| 9 | `fecha` | `date` | no | Fecha de la decisión. Valor por defecto: fecha actual. |  |
| 10 | `expediente_id` | `uuid` | no | Referencia al registro de legal_management.expedientes (id). | FK→legal_management.expedientes.id |
| 11 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |

## documentos

Documentos asociados a expedientes judiciales

- Clave primaria: `id`
- Filas: 157
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla documentos. Se genera automáticamente. | PK |
| 2 | `expediente_id` | `uuid` | no | Referencia al registro de legal_management.expedientes (id). | FK→legal_management.expedientes.id |
| 3 | `nombre` | `character varying(500)` | no | Nombre del documento asociado al expediente. |  |
| 4 | `tipo` | `character varying(100)` | no | Tipo de documento: DEMANDA, AUTO, MEMORIAL, PRUEBA, SENTENCIA, NOTIFICACION, OTRO |  |
| 5 | `descripcion` | `text` | sí | Descripción del documento del expediente judicial. |  |
| 6 | `archivo_url` | `text` | sí | URL o ruta al archivo físico o en storage |  |
| 7 | `archivo_nombre_original` | `character varying(500)` | sí | Nombre original del archivo cargado. |  |
| 8 | `archivo_tamano` | `integer` | sí | Tamaño del archivo en bytes. |  |
| 9 | `archivo_mime_type` | `character varying(100)` | sí | Tipo MIME del archivo. |  |
| 10 | `fecha_documento` | `date` | sí | Fecha del documento, distinta de la fecha de carga. |  |
| 11 | `numero_folios` | `integer` | sí | Número de folios del documento. |  |
| 12 | `confidencial` | `boolean` | sí | Indica si el documento del expediente judicial es confidencial. |  |
| 13 | `subido_por` | `character varying(255)` | sí | Usuario que cargó el documento, enviado por el cliente; en cargas automáticas toma etiquetas como Sistema (Campo Dinámico) o Sistema (Derivación de Comunicación). |  |
| 14 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 15 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 16 | `categoria` | `character varying(50)` | sí | Categoría del documento. Valor por defecto: documentos. |  |
| 17 | `etapa` | `character varying(100)` | sí | Etapa procesal en la que fue incorporado el documento |  |

## documentos_consulta

Documentos adjuntos a consultas jurídicas

- Clave primaria: `id`
- Filas: 25
- Referencia a: `consulta_id` → `legal_management.consultas_juridicas` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla documentos_consulta. Se genera automáticamente. | PK |
| 2 | `consulta_id` | `uuid` | no | Referencia a la consulta jurídica | FK→legal_management.consultas_juridicas.id |
| 3 | `nombre` | `character varying(255)` | no | Nombre del documento adjunto a la consulta jurídica. |  |
| 4 | `tipo_documento` | `character varying(50)` | sí | Tipo: solicitud, normativa, concepto, respuesta, otro |  |
| 5 | `descripcion` | `text` | sí | Descripción del documento adjunto a la consulta jurídica. |  |
| 6 | `archivo_url` | `text` | sí | URL del archivo del documento. |  |
| 7 | `archivo_nombre_original` | `character varying(255)` | sí | Nombre original del archivo cargado. |  |
| 8 | `tamano_bytes` | `bigint` | sí | Tamaño en bytes del documento adjunto a la consulta jurídica. |  |
| 9 | `mime_type` | `character varying(100)` | sí | Tipo MIME del documento adjunto a la consulta jurídica. |  |
| 10 | `subido_por` | `character varying(200)` | sí | Usuario que realizó la carga. |  |
| 11 | `fecha_documento` | `date` | sí | Fecha del documento adjunto a la consulta jurídica. |  |
| 12 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 13 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 14 | `firmado` | `boolean` | sí | Indica si el documento ha sido firmado (true=firmado, false=sin firmar) |  |

## documentos_oc

Documentos asociados a los requerimientos de los organismos de control. Un registro por documento (oficio, respuesta, acuse, anexo, evidencia, informe u otro), asociado a un requerimiento de legal_management.requerimientos_oc, con su archivo, tamaño, tipo MIME, fecha y usuario que lo cargó.

- Clave primaria: `id`
- Filas: 21
- Referencia a: `requerimiento_id` → `legal_management.requerimientos_oc` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla documentos_oc. Se genera automáticamente. | PK |
| 2 | `requerimiento_id` | `uuid` | no | Referencia al registro de legal_management.requerimientos_oc (id). | FK→legal_management.requerimientos_oc.id |
| 3 | `nombre` | `character varying(255)` | no | Nombre del documento del requerimiento. |  |
| 4 | `tipo_documento` | `character varying(50)` | sí | Tipo de documento. Valores permitidos: acuse, anexo, evidencia, informe, oficio, otro, respuesta. Valor por defecto: otro. |  |
| 5 | `descripcion` | `text` | sí | Descripción del documento del requerimiento. |  |
| 6 | `archivo_url` | `text` | sí | URL del archivo del documento. |  |
| 7 | `tamano_bytes` | `bigint` | sí | Tamaño en bytes del documento del requerimiento. |  |
| 8 | `mime_type` | `character varying(100)` | sí | Tipo MIME del documento del requerimiento. |  |
| 9 | `subido_por` | `character varying(200)` | sí | Usuario que realizó la carga. |  |
| 10 | `fecha_documento` | `date` | sí | Fecha del documento del requerimiento. |  |
| 11 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## evidencias

Evidencias aportadas a los expedientes de la gestión jurídica. Un registro por evidencia, asociada a un expediente (legal_management.expedientes), con su descripción, quien la aportó, fecha de presentación, archivo, tipo y prioridad. Su estado pasa por pendiente, en revisión, admitida, válida o rechazada.

- Clave primaria: `id`
- Filas: 16
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla evidencias. Se genera automáticamente. | PK |
| 2 | `expediente_id` | `uuid` | no | Referencia al registro de legal_management.expedientes (id). | FK→legal_management.expedientes.id |
| 3 | `descripcion` | `text` | sí | Descripción de la evidencia del expediente. |  |
| 4 | `aportado_por` | `character varying(255)` | sí | Persona que aportó la evidencia. |  |
| 5 | `fecha_presentacion` | `timestamp with time zone` | sí | Fecha y hora de presentación de la evidencia. |  |
| 6 | `archivo_nombre` | `character varying(255)` | sí | Nombre del archivo de la evidencia. |  |
| 7 | `archivo_url` | `text` | sí | URL del archivo de la evidencia. |  |
| 8 | `archivo_tamano` | `integer` | sí | Tamaño del archivo de la evidencia, en bytes. |  |
| 9 | `tipo` | `character varying(100)` | sí | Tipo de evidencia. |  |
| 10 | `prioridad` | `character varying(20)` | sí | Prioridad de la evidencia. Valores permitidos: Alta, Media, Baja. |  |
| 11 | `estado` | `character varying(50)` | sí | Estado de la evidencia (Admitida, En Revisión, Pendiente, Rechazada o Valida). |  |
| 12 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 13 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 14 | `tipo_archivo` | `character varying(50)` | sí | File extension (e.g., jpg, pdf, png) for correct icon display |  |

## excepciones_procesales

Excepciones procesales del módulo de Juzgamiento Disciplinario

- Clave primaria: `id`
- Filas: 2
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla excepciones_procesales. Se genera automáticamente. | PK |
| 2 | `tipo` | `character varying(100)` | no | Exception type - now configurable via ConfiguracionesSIGL, not restricted to fixed ENUM values |  |
| 3 | `descripcion` | `text` | no | Descripción de la excepción procesal. |  |
| 4 | `fundamento` | `text` | sí | Fundamento de la excepción procesal. |  |
| 5 | `estado` | `character varying(20)` | no | Estado de la excepción: PENDIENTE, RESUELTA, RECHAZADA |  |
| 6 | `resolucion` | `text` | sí | Decisión adoptada sobre la excepción procesal. |  |
| 7 | `fecha_presentacion` | `date` | no | Fecha de presentación de la excepción procesal. |  |
| 8 | `fecha_resolucion` | `date` | sí | Fecha de resolución de la excepción procesal. |  |
| 9 | `presentado_por` | `character varying(255)` | sí | Persona que presentó la excepción. |  |
| 10 | `expediente_id` | `uuid` | no | Referencia al registro de legal_management.expedientes (id). | FK→legal_management.expedientes.id |
| 11 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 12 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## expedientes

Expedientes de los procesos de la gestión jurídica (defensa judicial, juzgamiento disciplinario y otros tipos de proceso configurados). Un registro por expediente, con su radicado, jurisdicción, tipo de proceso, partes, abogado sustanciador, etapa, términos procesales, provisión contable y estado de archivo. Es la tabla central del módulo: de ella dependen actas, actores, audiencias, autos, comentarios, decisiones, documentos, evidencias, excepciones, notas y tareas, y puede vincularse a un proceso principal.

- Clave primaria: `id`
- Filas: 91
- Referencia a: `proceso_principal_id` → `legal_management.expedientes` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla expedientes. Se genera automáticamente. | PK |
| 2 | `radicado` | `character varying(50)` | no | Número de radicado del expediente, de 23 dígitos. Es único en la tabla. | única |
| 3 | `jurisdiccion` | `character varying(50)` | no | Jurisdicción del expediente. Valores: CIVIL, PENAL, ADMINISTRATIVO. |  |
| 4 | `tipo_proceso` | `character varying(100)` | no | Tipo de proceso del expediente. Toma el nombre de un tipo de proceso de la configuración del módulo (system_configurations, llaves defensa-judicial y juzgamiento), que define sus etapas. Por defecto, Ordinario; los procesos disciplinarios usan Disciplinario. |  |
| 5 | `demandante` | `character varying(255)` | no | Nombre del demandante. |  |
| 6 | `demandado` | `character varying(255)` | no | Nombre del demandado. Valor por defecto: ESAP. |  |
| 7 | `estado` | `character varying(50)` | no | Estado del expediente. La aplicación asigna ACTIVO al crearlo; el valor por defecto de la columna es RADICADO. |  |
| 8 | `fecha_radicacion` | `timestamp without time zone` | no | Fecha y hora de radicación del expediente. |  |
| 9 | `cuantia` | `numeric(15,2)` | sí | Cuantía del proceso, en valor numérico. |  |
| 10 | `abogado_sustanciador` | `character varying(255)` | sí | Identificador del usuario (id_user de auth."user") del abogado sustanciador: el usuario autenticado si resuelve solo, o el abogadoId enviado. La búsqueda por abogado también compara con public_id y con el nombre de la persona. |  |
| 11 | `fecha_prescripcion` | `timestamp without time zone` | sí | Fecha y hora de prescripción del expediente. |  |
| 12 | `riesgo_prescripcion` | `boolean` | sí | Indica si el expediente tiene riesgo de prescripción. |  |
| 13 | `termino_procesal_dias` | `integer` | sí | Duración del término procesal, contada desde fecha_notificacion según tipo_conteo_termino: días hábiles (por defecto), días calendario u horas. Con ella se calcula fecha_vencimiento_termino. |  |
| 14 | `ultima_actuacion` | `character varying(255)` | sí | Descripción de la última actuación registrada en el expediente. |  |
| 15 | `ubicacion_fisica` | `character varying(255)` | sí | Ubicación física del expediente. |  |
| 16 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 17 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 18 | `sancion_proyectada` | `character varying` | sí | Sanción proyectada en el proceso. |  |
| 19 | `etapa` | `character varying(50)` | sí | Stage of the process: AVOCAMIENTO, PRUEBAS, ALEGATOS, etc. |  |
| 20 | `cargo_investigado` | `character varying(255)` | sí | Job title of the investigated person |  |
| 21 | `ley_aplicable` | `character varying(100)` | sí | Applicable law, e.g., Ley 1952/2019 |  |
| 22 | `hechos` | `text` | sí | Descripción de los hechos del proceso en texto plano. Cuando hay lista de hechos (hechos_list), se deriva uniendo sus elementos con una línea en blanco, para compatibilidad con vistas previas. |  |
| 23 | `fecha_limite_etapa` | `timestamp without time zone` | sí | Fecha y hora límite de la etapa del expediente. |  |
| 24 | `tipo_solicitud` | `character varying(100)` | sí | Type of report/request, e.g. Informe Pormenorizado |  |
| 25 | `radicado_externo` | `character varying(50)` | sí | External ID from the requesting entity |  |
| 26 | `asunto` | `character varying(255)` | sí | Short title or subject of the request |  |
| 27 | `datos_requeridos` | `text` | sí | JSON or text listing required data points |  |
| 28 | `medio_control` | `character varying(255)` | sí | Medio de control judicial del proceso. |  |
| 29 | `juzgado_conocimiento` | `character varying(255)` | sí | Juzgado que conoce del proceso. |  |
| 30 | `pretension_demandante` | `text` | sí | Pretensiones del demandante. |  |
| 31 | `acto_administrativo_demandado` | `text` | sí | Acto administrativo demandado en el proceso. |  |
| 32 | `fecha_notificacion` | `timestamp without time zone` | sí | Fecha y hora de notificación del expediente. |  |
| 33 | `fecha_vencimiento_termino` | `timestamp without time zone` | sí | Fecha y hora de vencimiento del término del expediente. |  |
| 34 | `tipo_id_demandante` | `character varying(10)` | sí | Tipo de documento de identificación del demandante. |  |
| 35 | `numero_id_demandante` | `character varying(20)` | sí | Número de documento de identificación del demandante. |  |
| 36 | `tipo_id_demandado` | `character varying(10)` | sí | Tipo de documento de identificación del demandado. |  |
| 37 | `numero_id_demandado` | `character varying(20)` | sí | Número de documento de identificación del demandado. |  |
| 38 | `etapa_procesal` | `character varying(100)` | sí | Etapa del tablero (Kanban) en que está el expediente; sus valores son los estados configurados para el tipo de proceso. Valor por defecto: RADICACION. etapa, en cambio, guarda la etapa de Juzgamiento Disciplinario (por ejemplo, E1_AVOCAMIENTO). |  |
| 39 | `documentos_iniciales_urls` | `text[]` | sí | URL de los documentos iniciales del expediente, como arreglo. |  |
| 40 | `tipo_falta` | `character varying(50)` | sí | Severity: Leve, Grave, Gravísima |  |
| 41 | `dependencia_investigado` | `character varying(150)` | sí | Department of the investigated person |  |
| 42 | `demandante_direccion` | `character varying(500)` | sí | Dirección de notificaciones del demandante | Contacto |
| 43 | `demandante_telefono` | `character varying(50)` | sí | Teléfono de contacto del demandante | Contacto |
| 44 | `demandante_email` | `character varying(255)` | sí | Correo electrónico del demandante | Contacto |
| 45 | `demandante_apoderado` | `character varying(255)` | sí | Nombre del apoderado del demandante |  |
| 46 | `demandado_direccion` | `character varying(500)` | sí | Dirección de contacto del demandado; opcional. | Contacto |
| 47 | `demandado_telefono` | `character varying(50)` | sí | Teléfono del demandado. | Contacto |
| 48 | `demandado_email` | `character varying(255)` | sí | Correo electrónico del demandado. | Contacto |
| 49 | `tipo_conteo_termino` | `character varying(20)` | sí | Tipo de conteo de los términos del expediente. Valores: HABILES (días hábiles), CALENDARIO (días calendario). Por defecto, HABILES. |  |
| 50 | `estado_archivo` | `character varying(20)` | no | Estado de archivo: ACTIVO (en Kanban), ARCHIVADO (guardado), ELIMINADO (soft delete) |  |
| 51 | `fecha_archivo` | `timestamp without time zone` | sí | Fecha en que se archivó o eliminó el expediente |  |
| 52 | `usuario_archivo` | `character varying(255)` | sí | Usuario que realizó la acción de archivar/eliminar |  |
| 53 | `motivo_archivo` | `text` | sí | Razón o motivo del archivo/eliminación |  |
| 54 | `nivel_riesgo` | `character varying(255)` | sí | Nivel de riesgo del expediente, usado en el tablero y en conciliación. |  |
| 55 | `provision_contable` | `numeric(15,2)` | sí | Valor de la provisión contable del proceso. |  |
| 56 | `fecha_estimacion_provision` | `timestamp without time zone` | sí | Fecha y hora de estimación de la provisión del expediente. |  |
| 57 | `observacion_provision` | `text` | sí | Observación sobre la provisión contable. |  |
| 58 | `proceso_principal_id` | `uuid` | sí | Referencia al registro de legal_management.expedientes (id). | FK→legal_management.expedientes.id |
| 59 | `abogados_anteriores` | `text[]` | sí | Array of previously assigned lawyer names, populated when abogado_sustanciador is changed via reassignment |  |
| 60 | `fecha_hechos` | `timestamp without time zone` | sí | Fecha en que ocurrieron los hechos disciplinarios. Determina la ley aplicable: anterior al 30/06/2021 = Ley 734/2002, igual o posterior = Ley 1952/2019. |  |
| 61 | `es_delito_admin_publica` | `boolean` | sí | Indica si el proceso penal corresponde a delitos contra la administración pública |  |
| 62 | `es_conducta_patrimonio_publico` | `boolean` | sí | Indica si el proceso penal involucra conductas que afecten el patrimonio público |  |
| 63 | `es_otro_delito_penal` | `boolean` | no | Indica si el proceso penal corresponde a una categoría distinta a las definidas (otros delitos penales) |  |
| 64 | `otro_delito_penal_descripcion` | `character varying(200)` | sí | Descripción libre del tipo de delito penal cuando es_otro_delito_penal = true |  |
| 65 | `campos_adicionales` | `jsonb` | sí | Campos adicionales del expediente, en formato JSON: objeto con una entrada por campo dinámico del formulario. Los archivos cargados en base64 se guardan como documentos del expediente y en el JSON queda solo su metadata (nombre, tamaño). La territorial, antes guardada aquí, tiene columna propia. |  |
| 66 | `origen` | `character varying(50)` | sí | Origen del proceso (por ejemplo, queja, denuncia, de oficio). |  |
| 67 | `territorial` | `character varying(150)` | sí | Territorial asociada al expediente; antes se guardaba en campos_adicionales (migración 369). |  |
| 68 | `presunta_conducta` | `text` | sí | Descripción de la presunta conducta investigada. |  |
| 69 | `hechos_list` | `jsonb` | no | Hechos del proceso, como arreglo JSON; la columna hechos conserva su versión concatenada en texto. |  |
| 70 | `origen_comunicacion_id` | `uuid` | sí | Identificador de la comunicación (correo jurídico) que dio origen al proceso cuando se crea desde el Centro de Comunicaciones (Clasificación IA). |  |

## hallazgos

Hallazgos de auditoría de los organismos de control y su plan de mejoramiento. Un registro por hallazgo, asociado a un requerimiento de legal_management.requerimientos_oc, con su tipo (administrativo, disciplinario, fiscal o penal), causa, efecto, acción correctiva, responsables, indicador, avance y periodicidad de reporte. Su estado pasa por abierto, en curso, en revisión, cerrado o rechazado.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `requerimiento_id` → `legal_management.requerimientos_oc` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla hallazgos. Se genera automáticamente. | PK |
| 2 | `requerimiento_id` | `uuid` | sí | Referencia al registro de legal_management.requerimientos_oc (id). | FK→legal_management.requerimientos_oc.id |
| 3 | `codigo_hallazgo` | `character varying(50)` | no | Código único del hallazgo. | única |
| 4 | `numero_interno` | `character varying(50)` | sí | Número interno asignado al hallazgo por la entidad. |  |
| 5 | `tipo_hallazgo` | `character varying(30)` | sí | Tipo de hallazgo según su incidencia. Valores permitidos: ADMINISTRATIVO, DISCIPLINARIO, FISCAL, PENAL. Por defecto, ADMINISTRATIVO. |  |
| 6 | `titulo` | `character varying(300)` | no | Título del hallazgo. |  |
| 7 | `descripcion` | `text` | no | Descripción del hallazgo. |  |
| 8 | `causa_raiz` | `text` | sí | Causa raíz identificada para el hallazgo. |  |
| 9 | `efecto` | `text` | sí | Efecto o consecuencia del hallazgo. |  |
| 10 | `area_responsable` | `character varying(150)` | sí | Nombre del área responsable de atender el hallazgo. |  |
| 11 | `funcionario_responsable` | `character varying(200)` | sí | Nombre del funcionario responsable de atender el hallazgo. |  |
| 12 | `accion_correctiva` | `text` | no | Acción correctiva definida para subsanar el hallazgo. |  |
| 13 | `fecha_compromiso` | `date` | no | Fecha de compromiso para atender el hallazgo. |  |
| 14 | `indicador_cumplimiento` | `text` | sí | Indicador con el que se mide el cumplimiento de la acción correctiva. |  |
| 15 | `meta_indicador` | `character varying(100)` | sí | Meta del indicador de cumplimiento. |  |
| 16 | `estado` | `character varying(30)` | sí | Estado del hallazgo (ABIERTO, CERRADO, EN_CURSO, EN_REVISION o RECHAZADO). |  |
| 17 | `porcentaje_avance` | `integer` | sí | Porcentaje de avance de la acción correctiva (0 a 100). Por defecto, 0. |  |
| 18 | `fecha_ultimo_reporte` | `timestamp without time zone` | sí | Fecha y hora del último reporte del hallazgo. |  |
| 19 | `fecha_proximo_reporte` | `date` | sí | Fecha del próximo reporte del hallazgo. |  |
| 20 | `periodicidad_reporte` | `character varying(20)` | sí | Periodicidad con que se reporta el avance del hallazgo. Valores permitidos: ANUAL, MENSUAL, SEMESTRAL, TRIMESTRAL. Por defecto, TRIMESTRAL. |  |
| 21 | `documento_plan_url` | `text` | sí | URL del documento del plan de mejoramiento asociado al hallazgo. |  |
| 22 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 23 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 24 | `created_by` | `character varying(150)` | sí | Usuario que creó el registro. |  |

## historial_consultas

Bitácora de cambios de las consultas jurídicas. Un registro por acción sobre una consulta de legal_management.consultas_juridicas, con su descripción, los estados anterior y nuevo, el usuario y la fecha.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `consulta_id` → `legal_management.consultas_juridicas` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla historial_consultas. Se genera automáticamente. | PK |
| 2 | `consulta_id` | `uuid` | no | Referencia al registro de legal_management.consultas_juridicas (id). | FK→legal_management.consultas_juridicas.id |
| 3 | `accion` | `character varying(100)` | no | Acción registrada sobre la consulta. |  |
| 4 | `descripcion` | `text` | sí | Descripción de la acción registrada en el historial de la consulta. |  |
| 5 | `estado_anterior` | `character varying(30)` | sí | Estado de la consulta antes de la acción. |  |
| 6 | `estado_nuevo` | `character varying(30)` | sí | Estado de la consulta después de la acción. |  |
| 7 | `usuario_nombre` | `character varying(150)` | sí | Nombre del usuario que realizó la acción. |  |
| 8 | `fecha` | `timestamp without time zone` | sí | Fecha y hora en que se registró la acción. Por defecto, la fecha y hora de inserción. |  |

## notas_expediente

Notas internas de los abogados sobre el expediente

- Clave primaria: `id`
- Filas: 3
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla notas_expediente. Se genera automáticamente. | PK |
| 2 | `expediente_id` | `uuid` | no | Referencia al registro de legal_management.expedientes (id). | FK→legal_management.expedientes.id |
| 3 | `contenido` | `text` | no | Contenido de la nota del expediente. |  |
| 4 | `tipo` | `character varying(30)` | sí | Tipo de nota: importante, seguimiento, informacion, general, alerta |  |
| 5 | `autor_id` | `uuid` | sí | Identificador del autor de la nota. |  |
| 6 | `autor_nombre` | `character varying(255)` | sí | Nombre del autor de la nota, para mostrar o como respaldo. |  |
| 7 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 8 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## oficios_enviados

Oficios judiciales enviados desde el sistema, con soporte para plantillas institucionales ESAP

- Clave primaria: `id`
- Filas: 4

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla oficios_enviados. Se genera automáticamente. | PK |
| 2 | `numero` | `character varying(50)` | no | Número del oficio enviado. |  |
| 3 | `expediente_id` | `character varying(100)` | no | Identificador del expediente al que corresponde el oficio, guardado como texto y filtrado junto con modulo. |  |
| 4 | `modulo` | `character varying(50)` | sí | Módulo desde el que se envía el oficio (por ejemplo, juzgamiento-disciplinario, defensa-judicial, procesos-coactivos). |  |
| 5 | `asunto` | `character varying(500)` | no | Asunto del oficio. |  |
| 6 | `destinatario` | `character varying(300)` | no | Nombre del destinatario del oficio. |  |
| 7 | `destinatario_email` | `character varying(200)` | sí | Correo electrónico del destinatario del oficio. | Contacto |
| 8 | `contenido` | `text` | no | Contenido del oficio en texto. Obligatorio. |  |
| 9 | `contenido_html` | `text` | sí | Contenido HTML del oficio tal como se envió por correo, con la plantilla aplicada. |  |
| 10 | `firma` | `character varying(200)` | sí | Firma del oficio, enviada como texto desde el formulario. |  |
| 11 | `plantilla` | `character varying(50)` | sí | Plantilla usada en el oficio. Valores: prorroga, remision, contestacion, solicitudPruebas, oficioBlanco. |  |
| 12 | `estado` | `character varying(30)` | sí | Estado del oficio enviado. |  |
| 13 | `fecha_envio` | `timestamp without time zone` | sí | Fecha y hora de envío del oficio. |  |
| 14 | `archivos_adjuntos` | `jsonb` | sí | Archivos adjuntos del oficio, como arreglo JSON de objetos {nombre, url, tipo, size}. |  |
| 15 | `graph_message_id` | `character varying(200)` | sí | Identificador del mensaje en Microsoft Graph cuando el oficio se envió por correo. |  |
| 16 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 17 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## organismos_control

Catálogo de organismos de control externos que emiten requerimientos a la entidad. Un registro por organismo, con su sigla, nombre, descripción, correos de contacto e indicador de activo.

- Clave primaria: `id`
- Filas: 9

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla organismos_control. Se genera automáticamente. | PK |
| 2 | `sigla` | `character varying(20)` | no | Sigla única del organismo de control. | única |
| 3 | `nombre` | `character varying(200)` | no | Nombre del organismo de control. |  |
| 4 | `descripcion` | `text` | sí | Descripción del organismo de control. |  |
| 5 | `activo` | `boolean` | sí | Indica si el organismo de control está activo. |  |
| 6 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 7 | `correos` | `jsonb` | no | Lista de correos electrónicos del organismo de control, en formato JSON. Por defecto, lista vacía. |  |
| 8 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## pagos_coactivos

Pagos registrados en los procesos de cobro coactivo. Un registro por pago de un proceso de legal_management.procesos_coactivos, con su valor, fecha, soporte, origen (banco o manual) y su distribución entre capital, intereses y costas.

- Clave primaria: `id`
- Filas: 10
- Referencia a: `proceso_id` → `legal_management.procesos_coactivos` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla pagos_coactivos. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de legal_management.procesos_coactivos (id). | FK→legal_management.procesos_coactivos.id |
| 3 | `valor` | `numeric(15,2)` | no | Valor total del pago registrado en el proceso coactivo. |  |
| 4 | `fecha_pago` | `timestamp without time zone` | no | Fecha y hora del pago del proceso coactivo. |  |
| 5 | `soporte_url` | `text` | sí | URL del soporte del pago. |  |
| 6 | `origen` | `character varying(50)` | sí | Origen del registro del pago. Valores: BANCO, MANUAL. Por defecto, MANUAL. |  |
| 7 | `observaciones` | `text` | sí | Observaciones sobre el pago del proceso coactivo. |  |
| 8 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 10 | `abono_capital` | `numeric(15,2)` | sí | Parte del pago abonada al capital de la obligación. Por defecto, 0. |  |
| 11 | `abono_intereses` | `numeric(15,2)` | sí | Parte del pago abonada a los intereses de la obligación. Por defecto, 0. |  |
| 12 | `abono_costas` | `numeric(15,2)` | sí | Parte del pago abonada a las costas del proceso. Por defecto, 0. |  |

## pei_indicadores

Indicadores del plan estratégico institucional (PEI) de la gestión jurídica. Un registro por indicador, con su eje estratégico, meta, unidad de medida, plazo, frecuencia de medición, prioridad y responsable; sus avances se registran en legal_management.pei_registros_avance. Su estado es activo, inactivo o archivado.

- Clave primaria: `id`
- Filas: 24

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla pei_indicadores. Se genera automáticamente. | PK |
| 2 | `nombre` | `character varying(255)` | no | Nombre del indicador del PEI (por ejemplo, «Eficiencia en Defensa Judicial»). |  |
| 3 | `descripcion` | `text` | sí | Descripción del indicador del plan estratégico institucional (PEI). |  |
| 4 | `eje_estrategico` | `character varying(50)` | no | Eje estratégico del indicador. Valores: GESTION, TALENTO, TRANSPARENCIA, TECNOLOGIA. |  |
| 5 | `meta_objetivo` | `numeric(10,2)` | no | Meta numérica del indicador, expresada en la unidad de unidad_medida; el avance se calcula como valor reportado entre meta por 100. |  |
| 6 | `unidad_medida` | `character varying(20)` | sí | Unidad de medida de la meta. Valores: PORCENTAJE, NUMERO, MONEDA; valor por defecto PORCENTAJE. |  |
| 7 | `fecha_inicio` | `date` | no | Fecha de inicio del plazo del indicador. |  |
| 8 | `fecha_fin` | `date` | no | Fecha de finalización del indicador del plan estratégico institucional (PEI). |  |
| 9 | `frecuencia_medicion` | `character varying(20)` | sí | Frecuencia de medición del indicador. Por defecto, MENSUAL. |  |
| 10 | `responsable_id` | `uuid` | sí | Identificador (UUID) del usuario responsable del indicador: id_user de auth."user", el mismo que trae el token del usuario autenticado. El nombre se guarda en responsable_nombre. |  |
| 11 | `responsable_nombre` | `character varying(200)` | sí | Nombre del responsable del indicador, copiado para mostrar. |  |
| 12 | `estado` | `character varying(20)` | sí | Estado del indicador. Valores: ACTIVO, INACTIVO, ARCHIVADO; valor por defecto ACTIVO. |  |
| 13 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 15 | `prioridad` | `character varying(20)` | sí | Prioridad del indicador. Por defecto, MEDIA. |  |
| 16 | `tipo_indicador` | `character varying(50)` | sí | Tipo de indicador del plan estratégico institucional. Por defecto, GESTION. |  |
| 17 | `archived_at` | `timestamp with time zone` | sí | Fecha y hora en que se archivó el indicador; vacío si está activo. |  |
| 18 | `archived_by` | `character varying(255)` | sí | Usuario que archivó el indicador; queda vacío al restaurarlo. |  |
| 19 | `archive_reason` | `text` | sí | Motivo por el que se archivó el indicador. |  |

## pei_registros_avance

Historial de avances de los indicadores del plan estratégico institucional (PEI). Un registro por reporte de avance de un indicador de legal_management.pei_indicadores, con el valor reportado, el porcentaje de avance frente a la meta, la justificación, la evidencia y el usuario que lo registró.

- Clave primaria: `id`
- Filas: 24
- Referencia a: `indicador_id` → `legal_management.pei_indicadores` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla pei_registros_avance. Se genera automáticamente. | PK |
| 2 | `indicador_id` | `integer` | sí | Referencia al registro de legal_management.pei_indicadores (id). | FK→legal_management.pei_indicadores.id |
| 3 | `valor_reportado` | `numeric(10,2)` | no | Valor real del indicador reportado en el registro de avance. |  |
| 4 | `porcentaje_avance` | `numeric(5,2)` | sí | Porcentaje de avance, calculado como (valor_reportado / meta) × 100. |  |
| 5 | `observaciones` | `text` | sí | Justificación del avance reportado. |  |
| 6 | `evidencia_url` | `text` | sí | Enlace al documento soporte del avance; opcional. |  |
| 7 | `fecha_registro` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 8 | `usuario_registra_id` | `uuid` | sí | Identificador del usuario que registró el avance. |  |

## planes_comentarios

Comentarios registrados sobre los planes de mejoramiento. Un registro por comentario, asociado a un plan de legal_management.planes_mejoramiento, con el mensaje y el usuario autor.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `plan_id` → `legal_management.planes_mejoramiento` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla planes_comentarios. Se genera automáticamente. | PK |
| 2 | `plan_id` | `uuid` | sí | Referencia al registro de legal_management.planes_mejoramiento (id). | FK→legal_management.planes_mejoramiento.id |
| 3 | `mensaje` | `text` | no | Texto del comentario sobre el plan de mejoramiento. |  |
| 4 | `usuario_id` | `uuid` | sí | Identificador del usuario que escribió el comentario, enviado por el cliente. |  |
| 5 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |

## planes_evidencias

Evidencias cargadas a los planes de mejoramiento. Un registro por archivo de evidencia, asociado a un plan de legal_management.planes_mejoramiento, con su título, URL, tipo de archivo y usuario que lo cargó.

- Clave primaria: `id`
- Filas: 14
- Referencia a: `plan_id` → `legal_management.planes_mejoramiento` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla planes_evidencias. Se genera automáticamente. | PK |
| 2 | `plan_id` | `uuid` | sí | Referencia al registro de legal_management.planes_mejoramiento (id). | FK→legal_management.planes_mejoramiento.id |
| 3 | `titulo` | `character varying(150)` | no | Título de la evidencia cargada al plan de mejoramiento. |  |
| 4 | `url_archivo` | `text` | no | URL del archivo de la evidencia. |  |
| 5 | `tipo_archivo` | `character varying(255)` | sí | Tipo MIME del archivo de la evidencia, tomado del archivo cargado. |  |
| 6 | `uploaded_by` | `character varying(255)` | sí | Usuario que cargó la evidencia. Si no se informa, se registra «Sistema». |  |
| 7 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |

## planes_hallazgos

Hallazgos o acciones de mejora asociados a los planes de mejoramiento. Un registro por hallazgo de un plan de legal_management.planes_mejoramiento, con su nombre, descripción, archivo de soporte y porcentaje de avance; el avance global del plan es el promedio de los avances de sus hallazgos.

- Clave primaria: `id`
- Filas: 4
- Referencia a: `plan_id` → `legal_management.planes_mejoramiento` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla planes_hallazgos. Se genera automáticamente. | PK |
| 2 | `plan_id` | `uuid` | no | Referencia al registro de legal_management.planes_mejoramiento (id). | FK→legal_management.planes_mejoramiento.id |
| 3 | `nombre` | `character varying(255)` | no | Nombre del hallazgo asociado al plan. |  |
| 4 | `descripcion` | `text` | sí | Descripción del hallazgo asociado al plan. |  |
| 5 | `porcentaje_avance` | `integer` | no | Porcentaje de avance del hallazgo o acción de mejora (0 a 100). El avance global del plan es el promedio de los avances de sus hallazgos. Por defecto, 0. |  |
| 6 | `archivo_url` | `text` | sí | URL del archivo de soporte del hallazgo. |  |
| 7 | `archivo_nombre` | `character varying(255)` | sí | Nombre del archivo de soporte del hallazgo. |  |
| 8 | `archivo_mime` | `character varying(100)` | sí | Tipo MIME del archivo de soporte del hallazgo. |  |
| 9 | `created_by` | `character varying(150)` | sí | Usuario que creó el registro. |  |
| 10 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 11 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## planes_mejoramiento

Planes de mejoramiento de la entidad, originados en auditorías, organismos de control, autoevaluaciones o riesgos. Un registro por plan, con su código, origen, documento base, área y responsable, fechas, presupuesto, severidad y avance global; se relaciona con sus hallazgos, seguimientos, evidencias y comentarios. Su estado pasa por abierto, en ejecución, vencido o cerrado, y puede archivarse.

- Clave primaria: `id`
- Filas: 22

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla planes_mejoramiento. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(50)` | no | Código del plan de mejoramiento, único en la tabla. | única |
| 3 | `titulo` | `character varying(255)` | no | Título del plan de mejoramiento. |  |
| 4 | `descripcion` | `text` | sí | Descripción del plan de mejoramiento. |  |
| 5 | `origen` | `character varying(50)` | no | Origen del plan de mejoramiento. Valores permitidos: AUDITORIA_EXTERNA, AUTOEVALUACION, CONTRALORIA, HALLAZGO_AUDITORIA, OCI, OTRO, PROCURADURIA, RIESGO. |  |
| 6 | `origen_id` | `uuid` | sí | Identificador del registro que dio origen al plan. Cuando origen es RIESGO, corresponde a legal_management.riesgos.id; no tiene clave foránea. |  |
| 7 | `responsable_id` | `uuid` | sí | Identificador del usuario responsable del plan (auth."user"). |  |
| 8 | `fecha_inicio` | `date` | no | Fecha de inicio del plan de mejoramiento. |  |
| 9 | `fecha_fin_estimada` | `date` | no | Fecha estimada de finalización del plan de mejoramiento. |  |
| 10 | `fecha_cierre_real` | `date` | sí | Fecha real de cierre del plan de mejoramiento. |  |
| 11 | `avance_porcentaje` | `numeric(5,2)` | sí | Porcentaje de avance global del plan de mejoramiento. Se actualiza con el porcentaje reportado en cada seguimiento y, si el plan tiene hallazgos, se recalcula como el promedio redondeado del avance de sus hallazgos. Por defecto, 0. |  |
| 12 | `presupuesto` | `numeric(15,2)` | sí | Presupuesto asignado al plan de mejoramiento. Por defecto, 0. |  |
| 13 | `estado` | `character varying(20)` | sí | Estado del plan de mejoramiento. Valores permitidos: ABIERTO, EN_EJECUCION, VENCIDO, CERRADO. Por defecto, ABIERTO. |  |
| 14 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 15 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 16 | `documento_origen` | `character varying(255)` | sí | Identificador o nombre del documento base (ej: Informe de Auditoría) |  |
| 17 | `area_responsable` | `character varying(255)` | sí | Nombre del área encargada dentro de la entidad |  |
| 18 | `fecha_recepcion` | `date` | sí | Fecha de recepción del plan de mejoramiento. |  |
| 19 | `fecha_respuesta` | `date` | sí | Fecha de respuesta del plan de mejoramiento. |  |
| 20 | `severidad` | `character varying(50)` | sí | Nivel de criticidad: CRITICO, ALTO, MEDIO, BAJO |  |
| 21 | `responsable_nombre` | `character varying(255)` | sí | Text name of responsible person when no abogado is linked |  |
| 22 | `archived_at` | `timestamp with time zone` | sí | Fecha y hora en que se archivó el plan. |  |
| 23 | `archived_by` | `character varying(255)` | sí | Usuario que archivó el plan de mejoramiento; queda vacío al restaurarlo. |  |
| 24 | `archive_reason` | `text` | sí | Motivo por el que se archivó el plan de mejoramiento. |  |

## planes_seguimientos

Bitácora de seguimiento de los planes de mejoramiento. Un registro por reporte de avance de un plan de legal_management.planes_mejoramiento, con la descripción, el porcentaje reportado, la fecha y el usuario que lo registró.

- Clave primaria: `id`
- Filas: 22
- Referencia a: `plan_id` → `legal_management.planes_mejoramiento` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla planes_seguimientos. Se genera automáticamente. | PK |
| 2 | `plan_id` | `uuid` | sí | Referencia al registro de legal_management.planes_mejoramiento (id). | FK→legal_management.planes_mejoramiento.id |
| 3 | `descripcion_avance` | `text` | no | Descripción del avance reportado en el seguimiento del plan. |  |
| 4 | `porcentaje_reportado` | `numeric(5,2)` | sí | Porcentaje de avance total reportado en el seguimiento. Al registrarlo, reemplaza el avance_porcentaje del plan. |  |
| 5 | `fecha_reporte` | `timestamp without time zone` | sí | Fecha y hora del reporte de avance del plan. |  |
| 6 | `usuario_id` | `uuid` | sí | Identificador del usuario que registró el seguimiento. |  |

## plantillas_documentos

Plantillas de documentos Word de la gestión jurídica. Un registro por plantilla, con su nombre, categoría (actas, evidencias, oficios, pruebas, comunicaciones, notificaciones o documentos generales), archivo original, tipo MIME, tamaño, contenido en Base64 y usuario que la cargó.

- Clave primaria: `id`
- Filas: 5

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla plantillas_documentos. Se genera automáticamente. | PK |
| 2 | `nombre` | `character varying(500)` | no | Nombre de la plantilla de documento. |  |
| 3 | `categoria` | `character varying(100)` | no | Categoría de la plantilla. Valores: actas, evidencias, oficios, pruebas, comunicaciones, notificaciones, documentos-generales. |  |
| 4 | `nombre_original` | `character varying(500)` | no | Nombre original del archivo de la plantilla cargada. |  |
| 5 | `mime_type` | `character varying(100)` | no | Tipo MIME del archivo de la plantilla de documento. |  |
| 6 | `tamano` | `integer` | no | Tamaño del archivo de la plantilla, en bytes. |  |
| 7 | `contenido_base64` | `text` | no | Contenido del archivo de la plantilla codificado en Base64. |  |
| 8 | `subido_por` | `character varying(255)` | sí | Usuario que realizó la carga. |  |
| 9 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 10 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## procesos_coactivos

Tabla de procesos de cobro coactivo - Módulo Gestión Legal

- Clave primaria: `id`
- Filas: 7

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla procesos_coactivos. Se genera automáticamente. | PK |
| 2 | `radicado` | `character varying(50)` | no | Número de radicado único del proceso de cobro coactivo, de 23 dígitos. | única |
| 3 | `deudor` | `jsonb` | no | Información del deudor en formato JSON (nombre, identificacion, telefono, email, direccion) |  |
| 4 | `obligacion` | `jsonb` | no | Información de la obligación en formato JSON (concepto, valor, fechaVencimiento) |  |
| 5 | `estado` | `legal_management.estado_proceso_coactivo` | sí | Estado del proceso de cobro coactivo (PERSUASIVA, COACTIVA, MEDIDAS_CAUTELARES, EXCEPCIONES o LIQUIDACION). |  |
| 6 | `responsable` | `character varying(255)` | sí | Responsable del proceso coactivo, registrado como texto. Por defecto, «Sin asignar». |  |
| 7 | `documentos_adjuntos` | `integer` | sí | Cantidad de archivos adjuntos del proceso. Se recalcula contando procesos_coactivos_adjuntos al agregar o eliminar un adjunto o un pago. Por defecto, 0. |  |
| 8 | `notificaciones_enviadas` | `integer` | sí | Cantidad de notificaciones enviadas en el proceso. Por defecto, 0. |  |
| 9 | `observaciones` | `text` | sí | Observaciones sobre el proceso de cobro coactivo. |  |
| 10 | `ultima_actuacion` | `timestamp without time zone` | sí | Fecha y hora de la última actuación del proceso. Se actualiza al crear o actualizar el proceso y al registrar o eliminar un pago. |  |
| 11 | `fecha_creacion` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 13 | `valor_pagado` | `numeric(15,2)` | sí | Valor total pagado en el proceso: suma acumulada de los pagos registrados en pagos_coactivos. Por defecto, 0. |  |
| 14 | `saldo_pendiente` | `numeric(15,2)` | sí | Saldo pendiente de la obligación. Al crear el proceso es el valor de la obligación; al registrar un pago se recalcula con la liquidación, que suma capital, intereses moratorios y costas pendientes. Por defecto, 0. |  |
| 15 | `estado_archivo` | `character varying(20)` | sí | Estado de archivo del proceso: ACTIVO, ARCHIVADO o ELIMINADO (papelera). Por defecto, ACTIVO. |  |
| 16 | `fecha_archivo` | `timestamp without time zone` | sí | Fecha y hora de archivo del proceso de cobro coactivo. |  |
| 17 | `usuario_archivo` | `character varying(150)` | sí | Usuario que archivó o eliminó el proceso. |  |
| 18 | `motivo_archivo` | `text` | sí | Motivo del archivo. |  |
| 19 | `fecha_ejecutoria` | `timestamp without time zone` | sí | Fecha de ejecutoria en el proceso de cobro coactivo, agregada para la Resolución 492 / Manual de Cartera. Es la fecha desde la que se liquidan los intereses moratorios y se cuenta la prescripción de cinco años. |  |
| 20 | `tipo_interes_aplicable` | `character varying(20)` | sí | Tipo de tasa de interés con que se liquidan los intereses moratorios: DIAN o USURA. Por defecto, DIAN. |  |
| 21 | `valor_costas` | `numeric(15,2)` | sí | Valor de las costas del proceso. Por defecto, 0. |  |

## procesos_coactivos_adjuntos

Archivos adjuntos de los procesos de cobro coactivo. Un registro por archivo, asociado a un proceso de legal_management.procesos_coactivos, con su nombre original y almacenado, tipo, tamaño, URL e indicador de si corresponde al título ejecutivo.

- Clave primaria: `id`
- Filas: 13
- Referencia a: `proceso_id` → `legal_management.procesos_coactivos` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla procesos_coactivos_adjuntos. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de legal_management.procesos_coactivos (id). | FK→legal_management.procesos_coactivos.id |
| 3 | `nombre_original` | `character varying` | no | Nombre original del archivo adjunto, tal como se cargó. |  |
| 4 | `nombre_archivo` | `character varying` | no | Nombre con el que el sistema almacenó el archivo adjunto: 32 caracteres hexadecimales aleatorios más la extensión original. |  |
| 5 | `mime_type` | `character varying` | no | Tipo MIME del archivo adjunto al proceso coactivo. |  |
| 6 | `tamano` | `integer` | no | Tamaño del archivo adjunto, en bytes. |  |
| 7 | `fecha_creacion` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `tipo` | `character varying(100)` | sí | Tipo de adjunto del proceso coactivo. |  |
| 9 | `archivo_url` | `character varying(500)` | sí | URL del archivo adjunto. |  |
| 10 | `es_titulo_ejecutivo` | `boolean` | sí | Indica si el adjunto corresponde al título ejecutivo del proceso coactivo. |  |

## requerimientos_oc

Requerimientos recibidos de los organismos de control. Un registro por requerimiento, con sus radicados externo e interno, organismo emisor, tipo, asunto, plazo y fecha de vencimiento, responsable, abogado asignado, prioridad y soportes de respuesta; se relaciona con sus comentarios, documentos, hallazgos, borradores de respuesta y solicitudes de insumos. Su estado pasa por recibido, en análisis, en respuesta, enviado, cerrado o vencido, y puede archivarse.

- Clave primaria: `id`
- Filas: 14

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla requerimientos_oc. Se genera automáticamente. | PK |
| 2 | `radicado_externo` | `character varying(100)` | no | Número de radicado asignado por el organismo de control al requerimiento. |  |
| 3 | `radicado_interno` | `character varying(30)` | no | Número de radicado interno único que genera el sistema al crear el requerimiento, con formato REQ-OC-<año>-<consecutivo de 4 dígitos>. | única |
| 4 | `organismo_id` | `character varying(255)` | sí | Identificador del organismo de control que emite el requerimiento, guardado como texto. Puede ser el id de legal_management.organismos_control o un identificador local (UUID) que no existe en esa tabla; por eso no tiene clave foránea. |  |
| 5 | `tipo_requerimiento` | `character varying(50)` | no | Tipo de requerimiento del organismo de control, tomado del catálogo legal_management.cat_tipos_requerimiento (id). |  |
| 6 | `asunto` | `text` | no | Asunto del requerimiento del organismo de control. |  |
| 7 | `descripcion` | `text` | sí | Descripción del requerimiento. |  |
| 8 | `fecha_recepcion` | `timestamp without time zone` | no | Fecha y hora de recepción del requerimiento. Por defecto, la fecha y hora del registro. |  |
| 9 | `unidad_tiempo` | `character varying(20)` | sí | Unidad en que se expresa el plazo otorgado. Valores permitidos: DIAS_CALENDARIO, DIAS_HABILES, HORAS. Por defecto, DIAS_HABILES. |  |
| 10 | `plazo_otorgado` | `integer` | no | Plazo otorgado por el organismo de control para responder, en la unidad de unidad_tiempo. Por defecto, 15. |  |
| 11 | `fecha_vencimiento` | `timestamp without time zone` | no | Fecha de vencimiento del plazo de respuesta. Si no se informa, el sistema la calcula a partir de fecha_recepcion, plazo_otorgado y unidad_tiempo (por defecto, días hábiles). |  |
| 12 | `funcionario_responsable` | `character varying(200)` | sí | Nombre del funcionario responsable de atender el requerimiento. Al reasignar, se guarda el nombre del usuario asignado o, si falta, su identificador. |  |
| 13 | `area_responsable` | `character varying(150)` | sí | Área responsable de atender el requerimiento, registrada como texto; no está enlazada a un catálogo. |  |
| 14 | `abogado_asignado_id` | `uuid` | sí | Identificador del usuario de autenticación (auth."user") asignado como abogado del requerimiento; no referencia legal_management.abogados. |  |
| 15 | `estado` | `character varying(30)` | sí | Estado del requerimiento. Valores permitidos: RECIBIDO, EN_ANALISIS, EN_RESPUESTA, ENVIADO, CERRADO, VENCIDO. Por defecto, RECIBIDO. |  |
| 16 | `prioridad` | `character varying(15)` | sí | Prioridad del requerimiento. Valores permitidos: BAJA, NORMAL, ALTA, CRITICA. Por defecto, NORMAL. |  |
| 17 | `archivo_adjunto_url` | `text` | sí | URL del archivo adjunto del requerimiento recibido. |  |
| 18 | `oficio_respuesta_url` | `text` | sí | URL del oficio de respuesta al requerimiento. |  |
| 19 | `acuse_recibo_url` | `text` | sí | URL del acuse de recibo del requerimiento. El requerimiento no se puede cerrar sin acuse de recibo o sin oficio de respuesta. |  |
| 20 | `fecha_respuesta` | `timestamp without time zone` | sí | Fecha y hora de respuesta al requerimiento. |  |
| 21 | `observaciones` | `text` | sí | Observaciones sobre el requerimiento. |  |
| 22 | `created_by` | `character varying(150)` | sí | Usuario que creó el registro. |  |
| 23 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 24 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 25 | `estado_archivo` | `character varying` | sí | Estado del requerimiento en el sistema de archivo: ACTIVO, ARCHIVADO, ELIMINADO |  |
| 26 | `fecha_archivo` | `timestamp without time zone` | sí | Fecha y hora en que se archivó el requerimiento. |  |
| 27 | `usuario_archivo` | `character varying` | sí | Usuario que archivó o eliminó el requerimiento. |  |
| 28 | `motivo_archivo` | `text` | sí | Motivo por el que se archivó el requerimiento. |  |

## respuesta_borrador_oc

Almacena borradores de respuestas a requerimientos de órganos de control

- Clave primaria: `id`
- Filas: 2
- Referencia a: `requerimiento_id` → `legal_management.requerimientos_oc` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla respuesta_borrador_oc. Se genera automáticamente. | PK |
| 2 | `requerimiento_id` | `uuid` | no | Referencia al registro de legal_management.requerimientos_oc (id). | única FK→legal_management.requerimientos_oc.id |
| 3 | `destinatario_nombre` | `character varying(200)` | sí | Nombre del destinatario de la respuesta. |  |
| 4 | `destinatario_email` | `character varying(200)` | sí | Correo electrónico del destinatario de la respuesta. | Contacto |
| 5 | `destinatario_cargo` | `character varying(150)` | sí | Cargo del destinatario de la respuesta. |  |
| 6 | `tipo_respuesta` | `character varying(50)` | sí | Tipo de respuesta al requerimiento. |  |
| 7 | `contenido` | `text` | sí | Contenido del borrador de respuesta. |  |
| 8 | `documentos_adjuntos` | `jsonb` | sí | Lista de documentos adjuntos a la respuesta, en formato JSON (lista de textos). Por defecto, lista vacía. |  |
| 9 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 10 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## riesgo_historial

Historial de cambios y eventos de riesgos para trazabilidad

- Clave primaria: `id`
- Filas: 8
- Referencia a: `riesgo_id` → `legal_management.riesgos` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla riesgo_historial. Se genera automáticamente. | PK |
| 2 | `riesgo_id` | `uuid` | no | Referencia al registro de legal_management.riesgos (id). | FK→legal_management.riesgos.id |
| 3 | `tipo_evento` | `character varying(50)` | no | Tipo: CREACION, ACTUALIZACION, CAMBIO_ETAPA, CAMBIO_ZONA, ARCHIVADO, CONTROL_AGREGADO, etc. |  |
| 4 | `descripcion` | `text` | no | Descripción del evento o cambio en el historial del riesgo. |  |
| 5 | `campo_modificado` | `character varying(100)` | sí | Campo que fue modificado (e.g. etapa, probabilidad, impacto) |  |
| 6 | `valor_anterior` | `text` | sí | Valor antes del cambio |  |
| 7 | `valor_nuevo` | `text` | sí | Valor después del cambio |  |
| 8 | `usuario` | `character varying(200)` | sí | Usuario que generó el evento del riesgo. En la creación se toma el valor createdBy enviado por el cliente; los demás eventos se registran como «Sistema». |  |
| 9 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |

## riesgos

Riesgos institucionales de la gestión jurídica. Un registro por riesgo, con su código, proceso, tipo (corrupción, fiscal, gestión o seguridad digital), valoración inherente y residual (probabilidad, impacto y zona), causas, consecuencias, controles, plan de tratamiento, responsable y provisión contable, y el proceso jurídico de origen cuando aplica; su historial se registra en legal_management.riesgo_historial. Avanza por etapas desde identificado hasta cerrado.

- Clave primaria: `id`
- Filas: 6

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla riesgos. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(30)` | no | Código del riesgo, único en la tabla. | única |
| 3 | `nombre` | `character varying(255)` | no | Nombre del riesgo. |  |
| 4 | `descripcion` | `text` | no | Descripción del riesgo. |  |
| 5 | `proceso` | `character varying(100)` | no | Proceso institucional al que pertenece el riesgo, registrado como texto. Es distinto de proceso_id, que identifica el proceso de un submódulo jurídico (modulo_origen y proceso_radicado). |  |
| 6 | `tipo_riesgo` | `character varying(30)` | no | Tipo de riesgo. Valores permitidos: CORRUPCION, FISCAL, GESTION, SEGURIDAD_DIGITAL. |  |
| 7 | `etapa` | `character varying(30)` | sí | Etapa del ciclo de gestión del riesgo. Valores permitidos: ANALIZADO, CERRADO, IDENTIFICADO, MATERIALIZADO, MONITOREO, TRATAMIENTO, VALORADO. Por defecto, IDENTIFICADO. |  |
| 8 | `probabilidad_inherente` | `integer` | sí | Probabilidad inherente del riesgo (valoración antes de controles), en escala de 1 a 5. Con impacto_inherente calcula zona_inherente. Por defecto, 3. |  |
| 9 | `impacto_inherente` | `integer` | sí | Nivel de impacto del riesgo inherente, en escala de 1 a 5. Con probabilidad_inherente calcula zona_inherente. Por defecto, 3. |  |
| 10 | `zona_inherente` | `character varying(20)` | sí | Zona de riesgo inherente. Valores permitidos: ALTO, BAJO, EXTREMO, MODERADO. Por defecto, MODERADO. |  |
| 11 | `probabilidad_residual` | `integer` | sí | Probabilidad residual del riesgo (valoración después de controles), en escala de 1 a 5. Con impacto_residual calcula zona_residual. Por defecto, 3. |  |
| 12 | `impacto_residual` | `integer` | sí | Nivel de impacto del riesgo residual, después de aplicar los controles, en escala de 1 a 5. Con probabilidad_residual calcula zona_residual. Por defecto, 3. |  |
| 13 | `zona_residual` | `character varying(20)` | sí | Zona de riesgo residual, después de aplicar los controles. Valores permitidos: ALTO, BAJO, EXTREMO, MODERADO. Por defecto, MODERADO. |  |
| 14 | `causas` | `jsonb` | sí | Causas del riesgo, como arreglo JSON. |  |
| 15 | `consecuencias` | `jsonb` | sí | Lista de consecuencias del riesgo, en formato JSON. Por defecto, lista vacía. |  |
| 16 | `controles_existentes` | `jsonb` | sí | Controles existentes del riesgo, como arreglo JSON. |  |
| 17 | `plan_tratamiento` | `jsonb` | sí | Acciones del plan de tratamiento del riesgo, en formato JSON: cada acción tiene accion, responsable, fechaLimite, estado (PENDIENTE, EN_CURSO o COMPLETADA) y avance. Por defecto, lista vacía. |  |
| 18 | `responsable` | `character varying(200)` | no | Nombre del responsable del riesgo. |  |
| 19 | `responsable_id` | `uuid` | sí | Identificador del usuario responsable del riesgo (auth."user"). |  |
| 20 | `estado` | `character varying(20)` | sí | Estado del riesgo. Valores permitidos: ACTIVO, ARCHIVADO, CERRADO, ELIMINADO; valor por defecto ACTIVO. |  |
| 21 | `created_by` | `character varying(200)` | sí | Usuario que creó el registro. |  |
| 22 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 23 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 24 | `cuantia_estimada` | `numeric(15,2)` | sí | Valor monetario estimado del riesgo |  |
| 25 | `provision_contable` | `numeric(15,2)` | sí | Provisión contable calculada = cuantía × porcentaje |  |
| 26 | `porcentaje_provision` | `integer` | sí | Porcentaje aplicado según zona: EXTREMO=100, ALTO=75, MODERADO=50, BAJO=25 |  |
| 27 | `fecha_calculo_provision` | `timestamp without time zone` | sí | Fecha del último cálculo de provisión |  |
| 28 | `modulo_origen` | `character varying(50)` | sí | Módulo fuente: DEFENSA_JUDICIAL, JUZGAMIENTO, ASESORIA_JURIDICA, COACTIVOS, ORGANOS_CONTROL |  |
| 29 | `proceso_id` | `uuid` | sí | UUID del proceso asociado en el módulo correspondiente |  |
| 30 | `proceso_radicado` | `character varying(100)` | sí | Radicado o número del proceso para referencia rápida |  |
| 31 | `motivo_archivo` | `text` | sí | Motivo del archivado del riesgo. |  |

## sequences

Consecutivos genéricos de la gestión jurídica para generar radicados legibles por año (por ejemplo, TERM-2026-0001). Un registro por nombre de secuencia (prefijo y año), con el último número asignado.

- Clave primaria: `name`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `name` | `character varying(100)` | no | Clave primaria de la tabla sequences: name. | PK |
| 2 | `current_value` | `integer` | no | Último número asignado de la secuencia. Cada fila es un consecutivo anual por prefijo (nombre <PREFIJO>_<año>); hoy se usa para el radicado de términos procesales (prefijo TERM). Por defecto, 0. |  |
| 3 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## solicitudes_insumos

Solicitudes de insumos que se delegan a otras áreas para responder los requerimientos de los organismos de control. Un registro por solicitud, asociada a un requerimiento de legal_management.requerimientos_oc, con el área y el funcionario destinatarios, los documentos solicitados, los plazos, la respuesta y los documentos entregados. Su estado pasa por pendiente, en proceso, entregado, rechazado o vencido.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `requerimiento_id` → `legal_management.requerimientos_oc` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla solicitudes_insumos. Se genera automáticamente. | PK |
| 2 | `requerimiento_id` | `uuid` | no | Referencia al registro de legal_management.requerimientos_oc (id). | FK→legal_management.requerimientos_oc.id |
| 3 | `area_destino` | `character varying(150)` | no | Área a la que se solicitan los insumos para responder el requerimiento. |  |
| 4 | `funcionario_destino` | `character varying(200)` | sí | Nombre del funcionario al que se dirige la solicitud de insumos. |  |
| 5 | `email_destino` | `character varying(150)` | sí | Correo electrónico del funcionario al que se dirige la solicitud. | Contacto |
| 6 | `descripcion_solicitud` | `text` | no | Descripción de los insumos solicitados. |  |
| 7 | `documentos_solicitados` | `text` | sí | Relación de documentos solicitados al área, en texto. |  |
| 8 | `fecha_solicitud` | `timestamp without time zone` | sí | Fecha y hora de la solicitud de insumos. |  |
| 9 | `fecha_vencimiento_interna` | `timestamp without time zone` | no | Fecha y hora de vencimiento interno de la solicitud de insumos. |  |
| 10 | `fecha_respuesta` | `timestamp without time zone` | sí | Fecha y hora de respuesta a la solicitud de insumos. |  |
| 11 | `estado` | `character varying(25)` | sí | Estado de la solicitud de insumos (ENTREGADO, EN_PROCESO, PENDIENTE, RECHAZADO o VENCIDO). |  |
| 12 | `documentos_entregados_url` | `text` | sí | URL de los documentos entregados por el área al responder la solicitud. |  |
| 13 | `comentario_respuesta` | `text` | sí | Comentario del área al responder la solicitud. |  |
| 14 | `solicitado_por` | `character varying(150)` | sí | Usuario que realizó la solicitud. |  |
| 15 | `respondido_por` | `character varying(150)` | sí | Funcionario que respondió la solicitud. |  |
| 16 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 17 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## system_configurations

Parámetros de configuración de los módulos de la gestión jurídica (por ejemplo, columnas del tablero Kanban y tipos de proceso). Un registro por clave de configuración, con el módulo al que pertenece, su valor en formato JSON y su descripción.

- Clave primaria: `key`
- Filas: 8

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `key` | `character varying` | no | Clave primaria de la tabla system_configurations: key. | PK |
| 2 | `module` | `character varying` | no | Módulo al que pertenece el parámetro de configuración; por ejemplo, defensa-judicial, juzgamiento o asesoria-juridica. Si no se indica, general. |  |
| 3 | `value` | `jsonb` | no | Valor del parámetro de configuración, en formato JSON. |  |
| 4 | `description` | `text` | sí | Descripción del parámetro de configuración del sistema. |  |
| 5 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 6 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |

## tareas_expediente

Tareas asociadas a expedientes judiciales para control de actividades

- Clave primaria: `id`
- Filas: 35
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla tareas_expediente. Se genera automáticamente. | PK |
| 2 | `expediente_id` | `uuid` | no | Referencia al registro de legal_management.expedientes (id). | FK→legal_management.expedientes.id |
| 3 | `titulo` | `character varying(255)` | no | Título de la tarea. |  |
| 4 | `descripcion` | `text` | sí | Descripción de la tarea del expediente. |  |
| 5 | `fecha_vencimiento` | `timestamp without time zone` | sí | Fecha y hora de vencimiento de la tarea del expediente. |  |
| 6 | `prioridad` | `character varying(20)` | sí | Nivel de prioridad: alta, media, baja |  |
| 7 | `estado` | `character varying(30)` | sí | Estado de la tarea: pendiente, en_proceso, completada, cancelada |  |
| 8 | `responsable_id` | `uuid` | sí | Identificador del responsable asignado a la tarea. |  |
| 9 | `responsable_nombre` | `character varying(255)` | sí | Nombre del responsable de la tarea; se usa cuando el responsable no es un abogado registrado. |  |
| 10 | `fecha_creacion` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 11 | `fecha_completada` | `timestamp without time zone` | sí | Fecha y hora en que se completó la tarea del expediente. |  |
| 12 | `creado_por` | `character varying(255)` | sí | Usuario que creó el registro. |  |
| 13 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## tasas_referencia

Tasas de referencia mensuales para la liquidación de intereses en los procesos de cobro coactivo (Resolución 492). Un registro por año, mes y tipo de tasa (DIAN o usura), con su valor en porcentaje anual.

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla tasas_referencia. Se genera automáticamente. | PK |
| 2 | `anio` | `integer` | no | Año al que corresponde la tasa de referencia. |  |
| 3 | `mes` | `integer` | no | Mes de la tasa de referencia, de 1 a 12. |  |
| 4 | `valor_tasa` | `numeric(5,2)` | no | Valor de la tasa de referencia para el año y el mes, en porcentaje anual; la liquidación lo divide entre 12 para el interés mensual. |  |
| 5 | `tipo_tasa` | `character varying(20)` | no | Tipo de tasa de referencia: DIAN o USURA. Por defecto, DIAN. |  |
| 6 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 7 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## terminos_alertas_enviadas

Registro de las alertas de vencimiento ya enviadas para cada término procesal, para no reenviar la misma alerta. Un registro por envío, asociado a un término de legal_management.terminos_procesales y a la regla de legal_management.terminos_reglas_alerta que lo disparó; sin regla, corresponde a la anticipación personalizada del propio término.

- Clave primaria: `id`
- Filas: 109
- Referencia a: `regla_id` → `legal_management.terminos_reglas_alerta` (1..* → 0..1); `termino_id` → `legal_management.terminos_procesales` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla terminos_alertas_enviadas. Se genera automáticamente. | PK |
| 2 | `termino_id` | `uuid` | no | Referencia al registro de legal_management.terminos_procesales (id). | FK→legal_management.terminos_procesales.id |
| 3 | `regla_id` | `uuid` | sí | Referencia al registro de legal_management.terminos_reglas_alerta (id). | FK→legal_management.terminos_reglas_alerta.id |
| 4 | `fecha_envio` | `timestamp with time zone` | no | Fecha y hora de envío de la alerta de término. |  |

## terminos_procesales

Torre de control transversal para vencimientos de términos procesales de todos los módulos

- Clave primaria: `id`
- Filas: 233

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla terminos_procesales. Se genera automáticamente. | PK |
| 2 | `origen_modulo` | `character varying(50)` | no | Módulo de origen del término procesal. Valores permitidos: ASESORIA, DEFENSA, JUZGAMIENTO, MANUAL, ORGANOS_CONTROL, PROCESOS_COACTIVOS. |  |
| 3 | `referencia_id` | `uuid` | sí | Identificador del proceso o expediente en la tabla del módulo de origen. |  |
| 4 | `numero_radicado` | `character varying(100)` | sí | Número de radicado del proceso, para búsqueda rápida. |  |
| 5 | `nombre_actuacion` | `character varying(255)` | no | Nombre de la actuación a la que corresponde el término (por ejemplo, «Contestación Demanda», «Fallo Disciplinario»). |  |
| 6 | `fecha_base` | `timestamp with time zone` | no | Fecha de notificación o de inicio del conteo del término. |  |
| 7 | `dias_termino` | `integer` | no | Cantidad de días otorgados para el término, en la unidad que indica tipo_dias. |  |
| 8 | `tipo_dias` | `character varying(20)` | sí | Unidad del conteo del término. Valores permitidos: HABILES, CALENDARIO, HORAS; valor por defecto HABILES. |  |
| 9 | `fecha_vencimiento` | `timestamp with time zone` | no | Fecha de vencimiento del término, calculada por el sistema al registrar el término. |  |
| 10 | `fecha_alerta_preventiva` | `timestamp with time zone` | sí | Fecha de la alerta preventiva: vencimiento menos 5 días. |  |
| 11 | `fecha_alerta_critica` | `timestamp with time zone` | sí | Fecha de la alerta crítica: vencimiento menos 2 días. |  |
| 12 | `estado` | `character varying(20)` | sí | Estado del término. Valores permitidos: CUMPLIDO, ELIMINADO, PENDIENTE, SUSPENDIDO, VENCIDO; valor por defecto PENDIENTE. |  |
| 13 | `prioridad` | `character varying(10)` | sí | Prioridad del término procesal. Valores permitidos: ALTA, BAJA, MEDIA. Por defecto, MEDIA. |  |
| 14 | `responsable_id` | `uuid` | sí | Identificador del usuario asignado como responsable del término. |  |
| 15 | `observaciones` | `text` | sí | Observaciones sobre el término. |  |
| 16 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 17 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 18 | `closed_at` | `timestamp with time zone` | sí | Fecha y hora del cierre. |  |
| 19 | `responsable_nombre` | `character varying(255)` | sí | Nombre del responsable del término procesal. |  |
| 20 | `destinatario` | `character varying(255)` | sí | Entidad o dependencia receptora del informe o actuación sujeta al término. |  |
| 21 | `fundamento_normativo` | `jsonb` | sí | Normas que sustentan el término procesal, en formato JSON: cada elemento tiene tipo, cita, actualizacionPeriodica y, opcionalmente, mesRecordatorio. |  |
| 22 | `ente_solicitante` | `character varying(255)` | sí | Entidad u organismo que solicita el informe o actuación sujeta al término, registrado como texto; no está enlazado al catálogo de organismos de control. |  |
| 23 | `horas_anticipacion_alerta_personalizada` | `integer` | sí | Horas de anticipación al vencimiento para la alerta de este término; si tiene valor, el programador de alertas ignora las reglas globales de terminos_reglas_alerta y usa solo este umbral. |  |
| 24 | `recordatorio_manual_horas_anticipacion` | `integer` | sí | Horas de anticipación de un recordatorio programado manualmente por el usuario (envío único); el programador lo deja vacío después de enviarlo. |  |
| 25 | `ultimo_recordatorio_recurrente_en` | `timestamp with time zone` | sí | Fecha y hora del último recordatorio periódico enviado; el programador la usa para espaciar los recordatorios y se limpia al mover el vencimiento. |  |
| 26 | `alerta_vencimiento_enviada_en` | `timestamp with time zone` | sí | Fecha y hora del aviso único de término vencido, distinto de los recordatorios periódicos. |  |

## terminos_reglas_alerta

Reglas globales de alerta automática de vencimiento de los términos procesales. Un registro por regla, con las horas de anticipación al vencimiento, los canales de envío (correo electrónico o notificación en la aplicación) e indicador de activa; los envíos se registran en legal_management.terminos_alertas_enviadas.

- Clave primaria: `id`
- Filas: 2

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla terminos_reglas_alerta. Se genera automáticamente. | PK |
| 2 | `horas_anticipacion` | `integer` | no | Horas de anticipación al vencimiento con que se dispara la alerta. Valor único por regla. | única |
| 3 | `activa` | `boolean` | no | Indica si la regla de alerta de términos está activa. |  |
| 4 | `enviar_email` | `boolean` | no | Indica si la regla de alerta de términos envía la alerta por correo electrónico. |  |
| 5 | `notificar_in_app` | `boolean` | no | Indica si la regla de alerta de términos genera una notificación dentro de la aplicación. |  |
| 6 | `descripcion` | `character varying(255)` | sí | Descripción de la regla de alerta de términos. |  |
| 7 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
