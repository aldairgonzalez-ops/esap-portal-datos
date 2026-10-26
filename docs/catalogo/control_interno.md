# Control interno (`control_interno`)

Schema unificado para el Sistema de Control Interno Institucional

85 tablas · 6 vistas · 1310 columnas · 34.506 filas · 24 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`accion_correctiva`](#accion_correctiva) | Tabla | 29 | Acciones correctivas, de mejora o preventivas de los planes de mejoramiento. Un registro por acción, asociada a un plan (y opcionalmente a un hallazgo), con su responsable, fechas, indicador y meta, estado, avance, verificación de la Oficina de Control Interno y la calificación de cumplimiento y efectividad (EM-FO-002); de ella dependen las evidencias, alertas y registros de seguimiento. |
| [`accion_mejora`](#accion_mejora) | Tabla | 0 | Acciones de mejora dentro de un plan |
| [`actividad_etapa_auditoria`](#actividad_etapa_auditoria) | Tabla | 0 | Actividades dentro de cada etapa de auditoría |
| [`actividad_plan_anual_5`](#actividad_plan_anual_5) | Tabla | 1604 | Actividades por rol del plan anual |
| [`actividad_proceso_auditoria`](#actividad_proceso_auditoria) | Tabla | 0 | Actividades del proceso de auditoría. Cada fase tiene hasta 3 actividades requeridas para avanzar. |
| [`actividad_rol`](#actividad_rol) | Tabla | 0 | Actividades por rol configurable (RF020) |
| [`adjunto_actividad_plan_anual_5`](#adjunto_actividad_plan_anual_5) | Tabla | 21 | Archivos adjuntos (evidencias) para actividades del Plan Anual de Auditoría según Decreto 648/2017 |
| [`alerta_plan`](#alerta_plan) | Tabla | 21 | Alertas generadas automáticamente durante el seguimiento de los planes de mejoramiento (RF-SG-08). Un registro por alerta, asociada a un plan y, si aplica, a una acción correctiva, con su tipo, descripción, fecha de generación y si fue atendida, cuándo y por quién. |
| [`ampliacion_plazo`](#ampliacion_plazo) | Tabla | 0 | Solicitudes de ampliación de plazo de auditorías |
| [`aprobacion`](#aprobacion) | Tabla | 10 | Sistema de aprobaciones centralizado |
| [`auditor_perfil`](#auditor_perfil) | Tabla | 0 | Perfil profesional de auditores. Almacena información específica como especialidades y disponibilidad. |
| [`auditoria`](#auditoria) | Tabla | 70 | Auditorías del sistema con gestión Kanban, Lista y Calendario |
| [`auditoria_especial_info`](#auditoria_especial_info) | Tabla | 0 | Información específica de auditorías especiales (motivo, solicitante, justificación). |
| [`auditoria_gestion`](#auditoria_gestion) | Tabla | 0 | Gestión de auditorías con fases y seguimiento |
| [`auditoria_programada`](#auditoria_programada) | Tabla | 0 | Auditorías programadas en el plan anual |
| [`auditoria_territorial_info`](#auditoria_territorial_info) | Tabla | 0 | Información específica de auditorías territoriales (ciudad, departamento, contacto). |
| [`cache_esap`](#cache_esap) | Tabla | 0 | Cache del sistema ESAP |
| [`cierre_plan`](#cierre_plan) | Tabla | 2 | Cierre de los planes de mejoramiento (EM-PT-002 act. 8-10, RF-SG-11, RF-SG-12). Un registro por cierre de plan, con la fecha y el responsable del cierre, observaciones, verificación de efectividad y archivo del expediente mediante índice electrónico. |
| [`condicion_disparo_notificacion`](#condicion_disparo_notificacion) | Tabla | 12 | Catálogo de condiciones que disparan notificaciones en el módulo de control interno. Un registro por condición, con su nombre, descripción y estado activo. |
| [`configuracion_esap`](#configuracion_esap) | Tabla | 7 | Configuraciones específicas del sistema ESAP |
| [`configuracion_profesionales_ocig`](#configuracion_profesionales_ocig) | Tabla | 31 | Configuración de profesionales asignados al equipo OCIG (Oficina de Control Interno de Gestión) |
| [`criterio_auditoria`](#criterio_auditoria) | Tabla | 27 | Criterios de auditoría (normas, políticas, estándares aplicables) |
| [`cronograma_auditoria`](#cronograma_auditoria) | Tabla | 0 | Cronograma de auditorías del plan anual |
| [`cronograma_fase_auditoria`](#cronograma_fase_auditoria) | Tabla | 0 | Cronograma estimado por fase de la auditoría (duración de cada fase) |
| [`datos_automaticos_informe`](#datos_automaticos_informe) | Tabla | 0 | Datos automáticos poblados desde el sistema (US-022) |
| [`documento`](#documento) | Tabla | 77 | Gestión documental centralizada (RF013) |
| [`documento_aprobacion`](#documento_aprobacion) | Tabla | 0 | Archivos adjuntos a las solicitudes de aprobación de control interno. Un registro por archivo, asociado a una aprobación (control_interno.aprobacion) y a un documento (control_interno.documento), con nombre, ruta, tipo MIME y tamaño. |
| [`documento_plan_mejoramiento`](#documento_plan_mejoramiento) | Tabla | 0 | Documentos adjuntos a los planes de mejoramiento y a sus acciones correctivas. Un registro por documento, con nombre, tipo, datos del archivo, quién y cuándo lo cargó, y su validación por el auditor (pendiente de revisión, aceptada, con observaciones o rechazada). |
| [`entrega_informe_ley`](#entrega_informe_ley) | Tabla | 0 | Entregas de informes de ley por periodo |
| [`equipo_auditor`](#equipo_auditor) | Tabla | 160 | Equipo de auditores asignados a una auditoría. Relación N-N entre auditorías y personas. |
| [`especialidades_ocig`](#especialidades_ocig) | Tabla | 13 | Catálogo de especialidades de la Oficina de Control Interno de Gestión (OCIG). Un registro por especialidad, con su nombre, descripción, orden y estado activo. |
| [`etapa_auditoria`](#etapa_auditoria) | Tabla | 0 | Etapas de ejecución de auditorías |
| [`etapa_kanban`](#etapa_kanban) | Tabla | 12 | Etapas configuradas para cada tablero Kanban |
| [`evaluacion_proceso`](#evaluacion_proceso) | Tabla | 54 | Evaluaciones DAFP de procesos auditables. Cada proceso puede tener múltiples evaluaciones con diferentes vigencias/fechas de corte. |
| [`eventos_timeline`](#eventos_timeline) | Tabla | 265 | Registro histórico de todos los eventos importantes relacionados con planes de mejoramiento |
| [`evidencia_accion`](#evidencia_accion) | Tabla | 0 | Evidencias de cumplimiento que carga el área auditada para las acciones de mejora (RF-SG-02). Un registro por evidencia, asociada a una acción correctiva, con los datos del archivo, quién y cuándo la cargó, y la calificación del auditor de la Oficina de Control Interno con sus comentarios y la eventual solicitud de nueva evidencia (RF-SG-03, RF-SG-13). |
| [`evidencia_documento`](#evidencia_documento) | Tabla | 48 | Sistema independiente de gestión de evidencias y documentos vinculados a Hallazgos, Acciones, Planes y Auditorías |
| [`hallazgo`](#hallazgo) | Tabla | 34 | Hallazgos identificados en las auditorías |
| [`historial_auditoria`](#historial_auditoria) | Tabla | 480 | Historial completo de cambios y eventos de una auditoría. Trazabilidad completa de todas las acciones. El campo cambios almacena un array JSONB con formato: [{"campo": "Progreso", "valorAnterior": "10%", "valorNuevo": "15%"}] |
| [`historial_generacion_informe`](#historial_generacion_informe) | Tabla | 0 | Auditoría completa de generación y aprobación de informes |
| [`historial_plan_anual`](#historial_plan_anual) | Tabla | 29731 | Historial de cambios y auditoría del Plan Anual 5 Roles. Registra todas las operaciones CRUD para trazabilidad y compliance. |
| [`informe_ley`](#informe_ley) | Tabla | 16 | Informes normativos requeridos por ley (RF012) |
| [`integraciones_esap`](#integraciones_esap) | Tabla | 0 | Configuración de integraciones externas |
| [`item_lista_chequeo`](#item_lista_chequeo) | Tabla | 109 | Items individuales de una lista de chequeo |
| [`lista_aplicada`](#lista_aplicada) | Tabla | 0 | Aplicaciones de listas de chequeo en auditorías |
| [`lista_chequeo`](#lista_chequeo) | Tabla | 71 | Listas de chequeo configurables para auditorías |
| [`logs_auditoria_esap`](#logs_auditoria_esap) | Tabla | 0 | Logs de auditoría de acciones del sistema |
| [`normatividad_aplicable`](#normatividad_aplicable) | Tabla | 0 | Normatividad aplicable a la auditoría (decretos, leyes, manuales, políticas) |
| [`nota_auditoria`](#nota_auditoria) | Tabla | 0 | Notas y observaciones de las auditorías. Similar a un sistema de comentarios con categorización. Las notas marcadas como importantes (importante=true) aparecen destacadas en amarillo. |
| [`notificacion`](#notificacion) | Tabla | 945 | Sistema de notificaciones (RF014) |
| [`objetivo_auditoria`](#objetivo_auditoria) | Tabla | 39 | Objetivos específicos de cada auditoría. Cada auditoría puede tener múltiples objetivos. |
| [`parametro_sistema`](#parametro_sistema) | Tabla | 1 | Parámetros de configuración del sistema (RF020) |
| [`paso_workflow_informe`](#paso_workflow_informe) | Tabla | 0 | Pasos individuales del workflow de aprobación |
| [`plan_anual`](#plan_anual) | Tabla | 0 | Planes anuales de auditoría |
| [`plan_anual_5_roles`](#plan_anual_5_roles) | Tabla | 63 | Planes anuales de auditoría organizados según los cinco roles de la oficina de control interno del Decreto 648. Un registro por plan y vigencia, con su responsable, periodo de ejecución, estado (borrador, en revisión, aprobado, en ejecución, completado), avance de actividades, comité y orden de aprobación y firma de activación; se relaciona con las auditorías y el historial del plan. |
| [`plan_anual_wizard_borrador`](#plan_anual_wizard_borrador) | Tabla | 2 | Borradores del asistente de creación del plan anual de auditoría. Un registro por usuario, con el estado del asistente guardado en formato JSON. |
| [`plan_individual`](#plan_individual) | Tabla | 0 | Planes individuales de auditoría |
| [`plan_mejoramiento`](#plan_mejoramiento) | Tabla | 14 | Planes de mejoramiento derivados de hallazgos |
| [`plantilla_email`](#plantilla_email) | Tabla | 0 | Plantillas de correo electrónico (RF020) |
| [`plantilla_informe_ley`](#plantilla_informe_ley) | Tabla | 16 | Plantillas para generación automática de informes de ley |
| [`plantilla_reporte`](#plantilla_reporte) | Tabla | 0 | Plantillas para generación de reportes |
| [`plantillas_documentos_esap`](#plantillas_documentos_esap) | Tabla | 0 | Plantillas de documentos personalizadas |
| [`preferencia_notificacion`](#preferencia_notificacion) | Tabla | 1 | Preferencias de notificación por usuario (RF014) |
| [`proceso_auditable`](#proceso_auditable) | Tabla | 36 | Procesos auditables del universo de auditorías |
| [`programa_anual_ajuste`](#programa_anual_ajuste) | Tabla | 3 | Ajustes del Programa Anual (EFDS-1919): borrador de la siguiente versión; la versión que se genera lo cierra. |
| [`registro_seguimiento`](#registro_seguimiento) | Tabla | 0 | Registros de seguimiento de las acciones de mejora en cada seguimiento trimestral. Un registro por acción evaluada en un seguimiento (control_interno.seguimiento_trimestral), con las acciones programadas e implementadas, los controles, si el hallazgo se repite y los puntajes de cumplimiento y efectividad. |
| [`reunion_apertura`](#reunion_apertura) | Tabla | 15 | Información de la reunión de apertura de la auditoría |
| [`reunion_cierre`](#reunion_cierre) | Tabla | 11 | Información de la reunión de cierre de la auditoría |
| [`rol_decreto_648`](#rol_decreto_648) | Tabla | 0 | Roles del Decreto 648 configurable (RF020) |
| [`rol_decreto_648_template`](#rol_decreto_648_template) | Tabla | 5 | Plantillas de los cinco roles de la oficina de control interno según el Decreto 648. Un registro por rol, con su número, nombre, descripción, color y estado activo. |
| [`rol_plan_anual`](#rol_plan_anual) | Tabla | 0 | Roles y disponibilidad de auditores en el plan anual |
| [`rol_plan_anual_5`](#rol_plan_anual_5) | Tabla | 405 | Roles del plan anual (5 roles) |
| [`seccion_lista_chequeo`](#seccion_lista_chequeo) | Tabla | 0 | Secciones organizadas de listas de chequeo |
| [`seguimiento_plan`](#seguimiento_plan) | Tabla | 7 | Cortes de seguimiento periódico de los planes de mejoramiento (EM-PT-002 act. 5 y 7). Un registro por corte, trimestral (control interno) o semestral (ente externo), con su responsable, resumen, informe, conteo de acciones según su cumplimiento, alertas generadas y si lo generó el proceso automático. |
| [`seguimiento_plan_mejoramiento`](#seguimiento_plan_mejoramiento) | Tabla | 0 | Seguimientos trimestrales de planes de mejoramiento |
| [`seguimiento_trimestral`](#seguimiento_trimestral) | Tabla | 0 | Seguimientos trimestrales de los planes de mejoramiento. Un registro por plan, trimestre y año, con las fechas del periodo y del seguimiento, los porcentajes de avance, cumplimiento y efectividad, las acciones revisadas y las observaciones; el detalle por acción se registra en control_interno.registro_seguimiento. |
| [`sesiones_esap`](#sesiones_esap) | Tabla | 0 | Sesiones activas de usuarios |
| [`tablero_kanban`](#tablero_kanban) | Tabla | 2 | Configuración de tableros Kanban para auditorías y planes de mejoramiento |
| [`tareas_auditoria`](#tareas_auditoria) | Tabla | 0 | Tareas personalizadas asignadas a auditorías |
| [`tipo_auditoria`](#tipo_auditoria) | Tabla | 5 | Tipos de auditoría configurables del sistema (Regular, Territorial, Especial) |
| [`tipo_proceso`](#tipo_proceso) | Tabla | 7 | Catálogo parametrizable de tipos de procesos auditables |
| [`usuarios_esap`](#usuarios_esap) | Tabla | 0 | Usuarios del sistema ESAP |
| [`v_auditor_disponibilidad`](#v_auditor_disponibilidad) | Vista |  | Vista que muestra auditores con sus especialidades, disponibilidad y conteo de auditorías en curso |
| [`v_auditorias_finalizadas`](#v_auditorias_finalizadas) | Vista |  | Vista de auditorías finalizadas con información del documento de cierre |
| [`v_auditorias_kanban_completo`](#v_auditorias_kanban_completo) | Vista |  | Vista completa de auditorías con toda la información necesaria para el módulo Kanban |
| [`v_auditorias_por_estado`](#v_auditorias_por_estado) | Vista |  | Vista de contadores de auditorías por estado para el dashboard del Kanban |
| [`v_estado_vinculacion_auditorias`](#v_estado_vinculacion_auditorias) | Vista |  | Vista para verificar el estado de la vinculación de auditorías al Rol 4.  Muestra qué planes tienen actividad configurada y cuántas auditorías están vinculadas. |
| [`v_resumen_auditorias_por_año`](#v_resumen_auditorias_por_año) | Vista |  | _Por documentar_ |
| [`version_lista_chequeo`](#version_lista_chequeo) | Tabla | 0 | Historial de versiones de listas de chequeo |
| [`version_programa_anual`](#version_programa_anual) | Tabla | 25 | Versiones del Programa Anual de Auditoría por vigencia (EFDS-1919). Se generan al exportar si cambió lo que el documento imprime. |
| [`workflow_aprobacion_informe`](#workflow_aprobacion_informe) | Tabla | 0 | Workflow de aprobación para informes de ley (US-033) |

## accion_correctiva

Acciones correctivas, de mejora o preventivas de los planes de mejoramiento. Un registro por acción, asociada a un plan (y opcionalmente a un hallazgo), con su responsable, fechas, indicador y meta, estado, avance, verificación de la Oficina de Control Interno y la calificación de cumplimiento y efectividad (EM-FO-002); de ella dependen las evidencias, alertas y registros de seguimiento.

- Clave primaria: `id`
- Filas: 29
- Referencia a: `plan_id` → `control_interno.plan_mejoramiento` (0..* → 1)
- Relaciones implícitas: `hallazgo_id` ↝ `control_interno.hallazgo` (100.0 % con padre)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla accion_correctiva. Se genera automáticamente. | PK |
| 2 | `plan_id` | `uuid` | no | Referencia al registro de control_interno.plan_mejoramiento (id). | FK→control_interno.plan_mejoramiento.id |
| 3 | `descripcion` | `text` | no | Descripción de la acción correctiva. |  |
| 4 | `tipo` | `character varying(50)` | no | Tipo de acción (correctiva, mejora o preventiva). |  |
| 5 | `responsable` | `character varying(255)` | no | Nombre del responsable de ejecutar la acción correctiva (texto libre de 1 a 255 caracteres). |  |
| 6 | `fecha_inicio` | `date` | no | Fecha de inicio de la acción correctiva. |  |
| 7 | `fecha_fin` | `date` | no | Fecha de finalización de la acción correctiva. |  |
| 8 | `recursos` | `text` | sí | Recursos requeridos para ejecutar la acción correctiva, en texto libre. |  |
| 9 | `indicador` | `character varying(500)` | sí | Indicador con el que se mide el cumplimiento de la acción correctiva. |  |
| 10 | `meta_indicador` | `character varying(500)` | sí | Meta esperada del indicador de la acción correctiva. |  |
| 11 | `estado` | `character varying(50)` | no | Estado de la acción correctiva (completada, en-progreso, implementada, programada o vencida). |  |
| 12 | `porcentaje_avance` | `integer` | sí | Porcentaje de avance de la acción correctiva, de 0 a 100; los cambios quedan registrados como evento de progreso. |  |
| 13 | `observaciones` | `text` | sí | Observaciones sobre la acción correctiva. |  |
| 14 | `evidencias` | `jsonb` | sí | Evidencias de la acción correctiva, en formato JSON: lista de objetos con identificador, nombre, tipo, URL, fecha, indicador de validación, validador y fecha de validación. Por defecto, una lista vacía. |  |
| 15 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 16 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 17 | `hallazgo_id` | `uuid` | sí | ID del hallazgo al que está vinculada esta acción correctiva (opcional) | ↝control_interno.hallazgo.id |
| 18 | `estado_verificacion_oci` | `character varying(20)` | sí | Verificación OCI: sin_verificar, cumplida, parcial, incumplida |  |
| 19 | `evidencia_verificada` | `text` | sí | Descripción de la evidencia revisada por el OCI |  |
| 20 | `observacion_oci` | `text` | sí | Observación opcional del OCI |  |
| 21 | `fecha_verificacion_oci` | `timestamp without time zone` | sí | Fecha en que se registró la verificación OCI |  |
| 22 | `verificada_por_id` | `bigint` | sí | ID del usuario que registró la verificación |  |
| 23 | `cantidad_acciones_programadas` | `integer` | sí | Cantidad de acciones programadas como meta de la acción correctiva (EM-FO-002). |  |
| 24 | `cantidad_acciones_implementadas` | `integer` | sí | Cantidad de acciones implementadas de la acción correctiva (EM-FO-002). |  |
| 25 | `cumplimiento_emfo` | `integer` | sí | Cumplimiento calculado de la acción. Valores: 2 = Cumple, 1 = Parcial, 0 = No cumple (EM-FO-002). |  |
| 26 | `estado_accion_seguimiento` | `character varying(20)` | sí | Estado de la acción en el seguimiento: abierta o cerrada; por defecto abierta (EM-FO-002). |  |
| 27 | `responsable_seguimiento` | `character varying(500)` | sí | Responsable del seguimiento de la acción (jefe de la Oficina de Control Interno o quien tenga sus funciones). |  |
| 28 | `observacion_cumplimiento` | `text` | sí | Observaciones sobre el cumplimiento de la acción. |  |
| 29 | `evaluar_aplicacion_controles` | `boolean` | sí | Criterio 1 de efectividad: indica si se evaluó la aplicación de los controles (sí/no). |  |
| 30 | `validar_situacion_no_repitio` | `boolean` | sí | Criterio 2 de efectividad: indica si se validó que la situación no se volvió a presentar (sí/no). |  |
| 31 | `efectividad_emfo` | `integer` | sí | Efectividad calculada de la acción. Valores: 2 = Efectiva, 1 = Parcial, 0 = Inefectiva (EM-FO-002). |  |
| 32 | `efectividad_verificada` | `boolean` | sí | Indica si la efectividad de la acción se verificó en la siguiente auditoría; por defecto falso (EM-PT-002, actividad 9). |  |
| 33 | `observacion_efectividad` | `text` | sí | Observaciones sobre la efectividad de la acción. |  |

## accion_mejora

Acciones de mejora dentro de un plan

- Clave primaria: `id`
- Filas: 0
- Referencia a: `plan_mejoramiento_id` → `control_interno.plan_mejoramiento` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla accion_mejora. Se genera automáticamente. | PK |
| 2 | `numero` | `integer` | no | Número de la acción de mejora dentro del plan. |  |
| 3 | `descripcion` | `text` | no | Descripción de la acción de mejora. |  |
| 4 | `tipo` | `character varying(50)` | no | Tipo de acción de mejora (correctiva, mejora o preventiva). |  |
| 5 | `responsable` | `character varying(255)` | no | Nombre del responsable de ejecutar la acción de mejora. |  |
| 6 | `fecha_inicio` | `date` | no | Fecha de inicio de la acción de mejora. |  |
| 7 | `fecha_fin` | `date` | no | Fecha de finalización de la acción de mejora. |  |
| 8 | `estado` | `character varying(50)` | no | Estado de la acción de mejora (completada, en_progreso, pendiente o vencida). |  |
| 9 | `avance` | `integer` | no | Avance de la acción de mejora. |  |
| 10 | `evidencias` | `jsonb` | no | Evidencias de la acción de mejora, en formato JSON. |  |
| 11 | `observaciones` | `text` | sí | Observaciones sobre la acción de mejora. |  |
| 12 | `plan_mejoramiento_id` | `uuid` | no | Referencia al registro de control_interno.plan_mejoramiento (id). | FK→control_interno.plan_mejoramiento.id |
| 13 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## actividad_etapa_auditoria

Actividades dentro de cada etapa de auditoría

- Clave primaria: `id`
- Filas: 0
- Referencia a: `etapa_id` → `control_interno.etapa_auditoria` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla actividad_etapa_auditoria. Se genera automáticamente. | PK |
| 2 | `etapa_id` | `uuid` | no | Referencia al registro de control_interno.etapa_auditoria (id). | FK→control_interno.etapa_auditoria.id |
| 3 | `nombre` | `character varying(500)` | no | Nombre de la actividad de la etapa de auditoría. |  |
| 4 | `descripcion` | `text` | sí | Descripción de la actividad de la etapa de auditoría. |  |
| 5 | `tipo` | `character varying(100)` | no | Tipo de actividad de la etapa de auditoría. |  |
| 6 | `estado` | `character varying(50)` | no | Estado de la actividad de la etapa de auditoría (completada, en-progreso o pendiente). |  |
| 7 | `responsable` | `character varying(255)` | sí | Responsable de la actividad dentro de la etapa de auditoría. |  |
| 8 | `fecha_limite` | `date` | sí | Fecha límite de la actividad de la etapa de auditoría. |  |
| 9 | `completada` | `boolean` | sí | Indica si la actividad de la etapa de auditoría está completada. |  |
| 10 | `fecha_completacion` | `timestamp without time zone` | sí | Fecha y hora en que se completó la actividad de la etapa de auditoría. |  |
| 11 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## actividad_plan_anual_5

Actividades por rol del plan anual

- Clave primaria: `id`
- Filas: 1604
- Referencia a: `rol_id` → `control_interno.rol_plan_anual_5` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla actividad_plan_anual_5. Se genera automáticamente. | PK |
| 2 | `rol_id` | `uuid` | no | Referencia al registro de control_interno.rol_plan_anual_5 (id). | FK→control_interno.rol_plan_anual_5.id |
| 3 | `plan_id` | `uuid` | no | Identificador del rol del plan anual al que pertenece la actividad (control_interno.plan_anual_5_roles). |  |
| 4 | `nombre` | `character varying(500)` | no | Nombre de la actividad del plan anual. |  |
| 5 | `descripcion` | `text` | sí | Descripción de la actividad del plan anual. |  |
| 6 | `responsable` | `character varying(255)` | no | Nombre del responsable de la actividad del plan anual (texto de 1 a 255 caracteres). |  |
| 7 | `fecha_inicio` | `date` | no | Fecha de inicio de la actividad del plan anual. |  |
| 8 | `fecha_fin` | `date` | no | Fecha de finalización de la actividad del plan anual. |  |
| 9 | `estado` | `character varying(50)` | no | Estado de la actividad del plan anual (completada, en-progreso, pendiente o retrasada). |  |
| 10 | `porcentaje_avance` | `integer` | sí | Porcentaje de avance de la actividad, de 0 a 100; en actividades de auditoría lo actualiza el cálculo de cumplimiento de la vigencia. |  |
| 11 | `observaciones` | `text` | sí | Observaciones sobre la actividad del plan anual. |  |
| 12 | `prioridad` | `character varying(20)` | no | Prioridad de la actividad. Valores permitidos: Alta, Media, Baja; por defecto Media. |  |
| 13 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 15 | `control` | `text` | sí | Descripción del control aplicado a la actividad |  |
| 16 | `evaluacion` | `text` | sí | Evaluación del cumplimiento de la actividad |  |
| 17 | `seguimiento` | `text` | sí | Registro de seguimiento de la actividad |  |
| 18 | `requiere_verificacion_director` | `boolean` | sí | Indica si la actividad requiere verificación del Director OCIG antes de marcarse como completada |  |
| 19 | `verificada_por_director` | `boolean` | sí | Indica si la actividad fue verificada y aprobada por el Director OCIG |  |
| 20 | `fecha_verificacion` | `timestamp without time zone` | sí | Fecha y hora en que el Director OCIG verificó la actividad |  |
| 21 | `observaciones_director` | `text` | sí | Observaciones o comentarios del Director OCIG al verificar la actividad |  |
| 22 | `configuracion_evidencias` | `jsonb` | sí | Configuración JSON de requisitos de evidencias: adjuntosRequeridos, observacionRequerida, minimoAdjuntos, tiposPermitidos, longitudMinima |  |
| 23 | `activo` | `boolean` | sí | Indica si la actividad del plan anual está activa. Por defecto verdadero. |  |
| 24 | `tipo_calculo` | `character varying(50)` | sí | Tipo de cálculo de cumplimiento: manual (usuario), auditorias (automático), planes_mejoramiento (automático) |  |
| 25 | `total_auditorias_programadas` | `integer` | sí | Total de auditorías programadas asociadas a la actividad del plan anual; lo actualiza la función fn_actualizar_cumplimiento_auditorias_vigencia. Por defecto 0. |  |
| 26 | `total_auditorias_finalizadas` | `integer` | sí | Total de auditorías finalizadas asociadas a la actividad del plan anual; lo actualiza la función fn_actualizar_cumplimiento_auditorias_vigencia. Por defecto 0. |  |
| 27 | `auditorias_por_tipo` | `jsonb` | sí | Desglose de auditorías por tipo: {"regular": {"programadas": 5, "finalizadas": 3}, "territorial": {...}, "especial": {...}} |  |
| 28 | `puntos_control` | `jsonb` | sí | Array de puntos de control de la actividad con sus estados y evidencias |  |
| 29 | `frecuencia_puntos_control` | `character varying(20)` | sí | Frecuencia de evaluación de los puntos de control (diaria, semanal, quincenal, mensual, etc.) |  |
| 30 | `responsables` | `jsonb` | sí | Array de responsables de la actividad con id, nombre, cargo y email |  |
| 31 | `fecha_corte` | `date` | sí | Fecha de corte para el seguimiento periódico de la actividad |  |
| 32 | `entradas_seguimiento` | `jsonb` | sí | Array de entradas de seguimiento vinculadas a puntos de control |  |
| 33 | `tareas_seguimiento` | `jsonb` | sí | Sub-tareas de la actividad. Cada tarea tiene: id, descripcion, completada, responsables[], fechaLimite, fechaCompletada, completadaPor |  |

## actividad_proceso_auditoria

Actividades del proceso de auditoría. Cada fase tiene hasta 3 actividades requeridas para avanzar.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..1 → 1); `completada_por_id` → `auth.personas` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla actividad_proceso_auditoria. Se genera automáticamente. | PK |
| 2 | `auditoria_id` | `uuid` | no | Referencia al registro de control_interno.auditoria (id). | FK→control_interno.auditoria.id |
| 3 | `fase` | `character varying(50)` | no | Fase del proceso de auditoría a la que pertenece la actividad. Valores permitidos: Planeación, Comunicación, Ejecución, Seguimiento. |  |
| 4 | `nombre` | `character varying(255)` | no | Nombre de la actividad del proceso de auditoría. |  |
| 5 | `descripcion` | `text` | sí | Descripción de la actividad del proceso de auditoría. |  |
| 6 | `orden` | `integer` | no | Posición de la actividad dentro de la fase del proceso de auditoría; máximo tres actividades por fase. |  |
| 7 | `estado` | `character varying(50)` | no | Estado de la actividad del proceso de auditoría (completada, en-progreso o pendiente). |  |
| 8 | `fecha_limite` | `date` | sí | Fecha límite de la actividad del proceso de auditoría. |  |
| 9 | `fecha_completacion` | `timestamp without time zone` | sí | Fecha y hora en que se completó la actividad del proceso de auditoría. |  |
| 10 | `completada_por_id` | `uuid` | sí | Referencia al registro de auth.personas (id_person). | FK→auth.personas.id_person |
| 11 | `observaciones` | `text` | sí | Observaciones sobre la actividad del proceso de auditoría. |  |
| 12 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 13 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## actividad_rol

Actividades por rol configurable (RF020)

- Clave primaria: `id`
- Filas: 0
- Referencia a: `rol_id` → `control_interno.rol_decreto_648` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla actividad_rol. Se genera automáticamente. | PK |
| 2 | `rol_id` | `uuid` | no | Referencia al registro de control_interno.rol_decreto_648 (id). | FK→control_interno.rol_decreto_648.id |
| 3 | `nombre` | `character varying(255)` | no | Nombre de la actividad del rol. |  |
| 4 | `descripcion` | `text` | sí | Descripción de la actividad del rol. |  |
| 5 | `orden` | `integer` | sí | Posición de la actividad en el ordenamiento dentro del rol. |  |
| 6 | `activa` | `boolean` | sí | Indica si la actividad del rol está activa. |  |
| 7 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 8 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## adjunto_actividad_plan_anual_5

Archivos adjuntos (evidencias) para actividades del Plan Anual de Auditoría según Decreto 648/2017

- Clave primaria: `id`
- Filas: 21
- Referencia a: `actividad_id` → `control_interno.actividad_plan_anual_5` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla adjunto_actividad_plan_anual_5. Se genera automáticamente. | PK |
| 2 | `actividad_id` | `uuid` | no | FK a la actividad del plan anual a la que pertenece este adjunto | FK→control_interno.actividad_plan_anual_5.id |
| 3 | `nombre` | `character varying(255)` | no | Nombre del archivo adjunto (evidencia) de la actividad del Plan Anual de Auditoría. |  |
| 4 | `tipo` | `character varying(100)` | sí | MIME type del archivo (ej: application/pdf, image/jpeg, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet) |  |
| 5 | `tamanio` | `bigint` | sí | Tamaño del archivo en bytes |  |
| 6 | `fecha_carga` | `timestamp without time zone` | sí | Fecha y hora en que se cargó el archivo; por defecto el momento de registro. |  |
| 7 | `cargado_por` | `character varying(255)` | sí | Nombre del usuario que cargó el archivo. |  |
| 8 | `cargado_por_id` | `bigint` | sí | Identificador del usuario que cargó el archivo; referencia opcional a la persona en auth.personas. |  |
| 9 | `ruta_archivo` | `character varying(500)` | sí | Ruta física del archivo en el servidor o storage |  |
| 10 | `url` | `character varying(500)` | sí | URL pública o firmada para acceder/descargar el archivo |  |
| 11 | `hash_archivo` | `character varying(255)` | sí | Hash SHA-256 del archivo para verificar su integridad (opcional). |  |
| 12 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 13 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## alerta_plan

Alertas generadas automáticamente durante el seguimiento de los planes de mejoramiento (RF-SG-08). Un registro por alerta, asociada a un plan y, si aplica, a una acción correctiva, con su tipo, descripción, fecha de generación y si fue atendida, cuándo y por quién.

- Clave primaria: `id`
- Filas: 21
- Referencia a: `accion_id` → `control_interno.accion_correctiva` (0..1 → 0..1); `plan_id` → `control_interno.plan_mejoramiento` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla alerta_plan. Se genera automáticamente. | PK |
| 2 | `plan_id` | `uuid` | no | Referencia al registro de control_interno.plan_mejoramiento (id). | FK→control_interno.plan_mejoramiento.id |
| 3 | `accion_id` | `uuid` | sí | Referencia al registro de control_interno.accion_correctiva (id). | FK→control_interno.accion_correctiva.id |
| 4 | `tipo` | `character varying(50)` | no | Tipo de alerta generada automáticamente en el seguimiento del plan, según EM-PT-002 actividad 6: vencida_sin_evidencia (acción vencida sin evidencia), inefectiva (acción identificada como inefectiva), cumplimiento_mes_actual o cumplimiento_mes_siguiente (cumplimiento programado para el mes en curso o el siguiente). |  |
| 5 | `descripcion` | `text` | sí | Descripción legible de la alerta. |  |
| 6 | `generada_at` | `timestamp with time zone` | sí | Fecha y hora de la generación. |  |
| 7 | `atendida` | `boolean` | sí | Indica si la alerta fue atendida o resuelta; por defecto falso. |  |
| 8 | `atendida_at` | `timestamp with time zone` | sí | Fecha y hora en que se atendió la alerta. |  |
| 9 | `atendida_por_id` | `character varying(255)` | sí | Identificador del usuario que atendió la alerta. |  |

## ampliacion_plazo

Solicitudes de ampliación de plazo de auditorías

- Clave primaria: `id`
- Filas: 0
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla ampliacion_plazo. Se genera automáticamente. | PK |
| 2 | `auditoria_id` | `uuid` | no | Referencia al registro de control_interno.auditoria (id). | FK→control_interno.auditoria.id |
| 3 | `fecha_fin_original` | `date` | no | Fecha de finalización original de la auditoría, antes de la ampliación. |  |
| 4 | `fecha_fin_solicitada` | `date` | no | Nueva fecha de finalización solicitada para la auditoría. |  |
| 5 | `fecha_solicitud` | `timestamp without time zone` | no | Fecha y hora de la solicitud de ampliación de plazo. |  |
| 6 | `fecha_respuesta` | `timestamp without time zone` | sí | Fecha y hora de respuesta a la solicitud de ampliación de plazo. |  |
| 7 | `estado` | `character varying(20)` | no | Estados: pendiente, aprobada, rechazada |  |
| 8 | `justificacion` | `text` | no | Justificación de la solicitud de ampliación de plazo de la auditoría. |  |
| 9 | `motivo_rechazo` | `text` | sí | Motivo del rechazo. |  |
| 10 | `comentarios` | `text` | sí | Comentarios adicionales sobre la solicitud de ampliación de plazo. |  |
| 11 | `solicitado_por` | `character varying(100)` | no | Usuario que realizó la solicitud. |  |
| 12 | `aprobado_rechazado_por` | `character varying(100)` | sí | Usuario que aprobó o rechazó la solicitud de ampliación de plazo. |  |
| 13 | `dias_ampliacion` | `integer` | sí | Días de ampliación solicitados (calculado automáticamente) |  |
| 14 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 15 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## aprobacion

Sistema de aprobaciones centralizado

- Clave primaria: `id`
- Filas: 10

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla aprobacion. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(255)` | sí | Código de la aprobación, único en la tabla. | única |
| 3 | `tipo` | `character varying(100)` | sí | Tipo de aprobación (documento, informe, plan-auditoria o plan-mejora). |  |
| 4 | `titulo` | `character varying(500)` | sí | Título de la solicitud de aprobación. |  |
| 5 | `descripcion` | `text` | sí | Descripción de la solicitud de aprobación. |  |
| 6 | `solicitante` | `character varying(255)` | sí | Solicitante de la aprobación, registrado como texto; en las aprobaciones de plan de mejoramiento se copia el responsable de implementación del plan o Sistema. |  |
| 7 | `fecha_solicitud` | `date` | sí | Fecha de la solicitud de aprobación. |  |
| 8 | `prioridad` | `character varying(20)` | no | Prioridad de la solicitud de aprobación. Valores permitidos: Alta, Media, Baja; por defecto Media. |  |
| 9 | `estado` | `character varying(50)` | no | Estado de la aprobación (aprobado, en-revision, pendiente o rechazado). |  |
| 10 | `territorial` | `character varying(255)` | sí | Dirección territorial asociada a la solicitud de aprobación; en las de plan de mejoramiento se copia de la auditoría del hallazgo o del plan. |  |
| 11 | `sede` | `character varying(255)` | sí | Sede asociada a la solicitud de aprobación; en las de plan de mejoramiento se copia de la auditoría del hallazgo o del plan. |  |
| 12 | `relacionado` | `character varying(255)` | sí | Referencia al elemento relacionado con la solicitud de aprobación; en las de tipo plan-mejora guarda el identificador del plan de mejoramiento, que se aprueba o rechaza junto con la solicitud. |  |
| 13 | `documentos_count` | `integer` | sí | Cantidad de documentos asociados a la aprobación; la relación se guarda en documento_aprobacion. Por defecto 0. |  |
| 14 | `aprobado_por` | `character varying(255)` | sí | Usuario que realizó la aprobación. |  |
| 15 | `fecha_aprobacion` | `timestamp without time zone` | sí | Fecha y hora de aprobación de la solicitud. |  |
| 16 | `rechazado_por` | `character varying(255)` | sí | Usuario que realizó el rechazo. |  |
| 17 | `fecha_rechazo` | `timestamp without time zone` | sí | Fecha y hora de rechazo de la solicitud. |  |
| 18 | `motivo_rechazo` | `text` | sí | Motivo del rechazo de la solicitud de aprobación. |  |
| 19 | `observaciones` | `text` | sí | Observaciones registradas al aprobar la solicitud. El rechazo se documenta en motivo_rechazo. |  |
| 20 | `area` | `character varying(255)` | sí | Área asociada a la solicitud de aprobación; en las de plan de mejoramiento es el área responsable del plan, no el área que aprueba. |  |
| 21 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 22 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## auditor_perfil

Perfil profesional de auditores. Almacena información específica como especialidades y disponibilidad.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `persona_id` → `auth.personas` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla auditor_perfil. Se genera automáticamente. | PK |
| 2 | `persona_id` | `uuid` | no | Referencia al registro de auth.personas (id_person). | única FK→auth.personas.id_person |
| 3 | `especialidad` | `character varying(255)` | sí | Especialidad del auditor (ej: Auditoría Financiera, Control Interno, Gestión Administrativa) |  |
| 4 | `cargo` | `character varying(100)` | sí | Cargo del auditor (por ejemplo, Auditor Líder, Auditor Senior, Auditor Junior). |  |
| 5 | `nivel_experiencia` | `character varying(50)` | sí | Nivel de experiencia del auditor. Valores permitidos: Junior, Intermedio, Senior, Líder, Jefe. |  |
| 6 | `estado_disponibilidad` | `character varying(50)` | sí | Estado de disponibilidad: Disponible, Parcial, No disponible, En licencia |  |
| 7 | `fecha_ultima_actividad` | `date` | sí | Fecha de la última actividad registrada del auditor. |  |
| 8 | `observaciones` | `text` | sí | Observaciones sobre el perfil profesional del auditor. |  |
| 9 | `activo` | `boolean` | sí | Indica si el perfil del auditor está activo. |  |
| 10 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 11 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## auditoria

Auditorías del sistema con gestión Kanban, Lista y Calendario

- Clave primaria: `id`
- Filas: 70
- Referencia a: `actividad_plan_anual_id` → `control_interno.actividad_plan_anual_5` (0..1 → 0..1); `auditor_asignado_id` → `auth.personas` (0..1 → 0..1); `auditor_lider_id` → `auth.personas` (0..* → 0..1); `supervisor_asignado_id` → `auth.personas` (0..* → 0..1); `auditor_asignado_id` → `auth.personas` (0..1 → 0..1); `auditor_lider_id` → `auth.personas` (0..* → 0..1); `plan_anual_id` → `control_interno.plan_anual_5_roles` (0..* → 0..1); `supervisor_asignado_id` → `auth.personas` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla auditoria. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(255)` | no | Código único de la auditoría, con formato AUD-YYYY-### (año y consecutivo). | única |
| 3 | `nombre` | `character varying(500)` | no | Nombre de la auditoría. |  |
| 4 | `tipo` | `character varying(50)` | no | Tipo de auditoría. Los tipos predefinidos son Regular, Territorial y Especial; admite tipos personalizados, que se administran en control_interno.tipo_auditoria con el permiso de gestión de configuración. |  |
| 5 | `fase` | `character varying(50)` | no | Fase actual de la auditoría (planeacion, en-curso, revision, completada) |  |
| 6 | `territorial` | `character varying(255)` | no | Dirección territorial donde se realiza la auditoría; obligatoria y guardada como texto. |  |
| 7 | `sede` | `character varying(255)` | no | Sede donde se realiza la auditoría |  |
| 8 | `responsable` | `character varying(255)` | no | Responsable de la auditoría |  |
| 9 | `fecha_inicio` | `date` | no | Inicio de Etapa 1: Planeación (= fechaInicioPlaneacion) |  |
| 10 | `fecha_fin` | `date` | no | Fin de Etapa 3: Comunicación (= fechaFinComunicacion, fin de la auditoría) |  |
| 11 | `progreso` | `integer` | sí | Porcentaje de avance de la auditoría, de 0 a 100. Por defecto 0. |  |
| 12 | `prioridad` | `character varying(20)` | no | Prioridad de la auditoría. Valores permitidos: Alta, Media, Baja; por defecto Media. |  |
| 13 | `hallazgos` | `integer` | sí | Número de hallazgos registrados en la auditoría; aumenta o disminuye con las operaciones de incremento y decremento (sin bajar de 0) o toma el valor enviado al editar la auditoría. Por defecto, 0. |  |
| 14 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 15 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 16 | `estado_kanban` | `character varying(50)` | sí | Estado de la auditoría en el Kanban |  |
| 17 | `semaforo` | `character varying(20)` | sí | Color del semáforo de seguimiento de la auditoría en el tablero Kanban. Valores permitidos: verde, amarillo, rojo; por defecto verde. Se asigna con el valor enviado al editar la auditoría. |  |
| 18 | `tipo_kanban` | `character varying(50)` | sí | Tipo operativo de la auditoría en el tablero Kanban. Valores permitidos: regular, especial, territorial; por defecto regular. Al crear la auditoría se deriva de tipo_kanban o de tipo; el Programa Anual combina ambos campos para clasificar la auditoría. |  |
| 19 | `prioridad_kanban` | `character varying(20)` | sí | Prioridad de la auditoría en el tablero Kanban. Valores permitidos: baja, media, alta, crítica; por defecto media. Las tarjetas del tablero usan prioridad_kanban; los filtros y estadísticas usan prioridad. |  |
| 20 | `area_objetivo` | `character varying(255)` | sí | Área objetivo de la auditoría, en texto libre. |  |
| 21 | `permite_cambiar_objetivos` | `boolean` | sí | Indica si se permite cambiar los objetivos de la auditoría. Por defecto verdadero; se modifica con el valor enviado al editar la auditoría. |  |
| 22 | `descripcion` | `text` | sí | Descripción detallada de la auditoría |  |
| 23 | `alcance` | `text` | sí | Alcance de la auditoría: áreas a evaluar y procesos incluidos. |  |
| 24 | `proceso_auditado` | `character varying(500)` | sí | Proceso auditado: identificador (UUID) de control_interno.proceso_auditable o, si no está vinculado, el nombre del proceso en texto. |  |
| 25 | `responsable_area_nombre` | `character varying(255)` | sí | Nombre del responsable del área auditada. |  |
| 26 | `responsable_area_cargo` | `character varying(255)` | sí | Cargo del responsable del área auditada. |  |
| 27 | `responsable_area_email` | `character varying(255)` | sí | Correo electrónico del responsable del área auditada. | Contacto |
| 28 | `supervisor_asignado_id` | `uuid` | sí | ID del supervisor asignado (FK a auth.personas) | FK→auth.personas.id_person |
| 29 | `fecha_reunion_apertura` | `timestamp without time zone` | sí | Fecha y hora de la reunión de apertura de la auditoría. |  |
| 30 | `metodologia` | `text` | sí | Metodología aplicada en la auditoría. |  |
| 31 | `periodicidad` | `character varying(20)` | sí | Periodicidad de la auditoría. Valores permitidos: unica, trimestral, semestral, anual; por defecto unica. |  |
| 32 | `presupuesto_estimado` | `numeric(15,2)` | sí | Presupuesto estimado de la auditoría. |  |
| 33 | `vinculada_plan_anual` | `boolean` | sí | Indica si la auditoría pertenece al programa/plan anual OCI |  |
| 34 | `plan_anual_id` | `uuid` | sí | FK al plan anual 5 roles (control_interno.plan_anual_5_roles) | FK→control_interno.plan_anual_5_roles.id |
| 35 | `plan_anual_vigencia` | `integer` | sí | Año de vigencia del plan anual (ej. 2026) |  |
| 36 | `rol_decreto_asociado` | `character varying(255)` | sí | Rol Decreto 648/2017 asociado en la programación |  |
| 37 | `observaciones_adicionales` | `text` | sí | Observaciones adicionales sobre la auditoría. |  |
| 38 | `checklist_completados` | `jsonb` | sí | Estado de los checkboxes de actividades de auditoría. Formato: {"ep1": true, "ep2": false, ...} |  |
| 39 | `archivada` | `boolean` | sí | Indica si la auditoría está archivada. Por defecto falso; las funciones de cumplimiento y de vinculación al plan anual excluyen las auditorías archivadas. |  |
| 40 | `fecha_archivo` | `timestamp without time zone` | sí | Fecha y hora en que se archivó la auditoría. |  |
| 41 | `activa` | `boolean` | sí | Indica si la auditoría está activa |  |
| 42 | `fecha_eliminacion` | `timestamp without time zone` | sí | Fecha y hora de eliminación de la auditoría. |  |
| 43 | `riesgo_kanban` | `character varying(20)` | sí | Nivel de riesgo de la auditoría en el tablero Kanban. Valores permitidos: Alto, Medio, Bajo; se asigna con el valor enviado al editar la auditoría y el tablero muestra Medio si está vacío. |  |
| 44 | `calificacion_riesgo` | `character varying(255)` | sí | Calificación del riesgo de la auditoría (ampliado a 255 caracteres) |  |
| 45 | `ultima_actuacion` | `text` | sí | Descripción de la última actuación de la auditoría, diligenciada con el valor enviado al editarla; no se calcula desde el historial. |  |
| 46 | `dias_restantes` | `integer` | sí | Número de días que faltan para la fecha de fin de la auditoría (fecha_fin menos la fecha actual, mínimo 0). Lo calcula un trigger al crear la auditoría o al cambiar fecha_inicio o fecha_fin; no se recalcula a diario. Por defecto 0. |  |
| 47 | `porcentaje_tiempo` | `integer` | sí | Porcentaje del tiempo programado de la auditoría transcurrido entre fecha_inicio y fecha_fin, de 0 a 100. Lo calcula un trigger al crear la auditoría o al cambiar fecha_inicio o fecha_fin. Por defecto 0. |  |
| 48 | `total_documentos` | `integer` | sí | Número de documentos asociados a la auditoría; lo actualiza la función actualizar_contadores_documentos_informes. Por defecto 0. |  |
| 49 | `total_informes` | `integer` | sí | Número de documentos de tipo informe asociados a la auditoría; lo actualiza la función actualizar_contadores_documentos_informes. Por defecto 0. |  |
| 50 | `total_tareas` | `integer` | sí | Número de tareas de la auditoría, diligenciado al editarla. Por defecto, 0. |  |
| 51 | `actividades_completas` | `boolean` | sí | Indica si todas las actividades de la auditoría están completas, es decir, si no hay actividades pendientes; lo actualiza la función actualizar_actividades_auditoria. |  |
| 52 | `actividades_pendientes` | `integer` | sí | Número de actividades pendientes de la auditoría; lo actualiza la función actualizar_actividades_auditoria. Por defecto 0. |  |
| 53 | `auditor_lider_id` | `uuid` | sí | ID del auditor líder (FK a auth.personas) | FK→auth.personas.id_person |
| 54 | `auditor_asignado_id` | `uuid` | sí | ID del auditor asignado (FK a auth.personas) | FK→auth.personas.id_person |
| 55 | `programa_anual_metadata` | `jsonb` | sí | Metadata del programa anual: { "mesInicio": 0-11, "semanaInicio": 1-4, "duraciones": { "planeacion": number, "ejecucion": number, "comunicacion": number } } |  |
| 56 | `aprobada` | `boolean` | no | Indica si la auditoría fue aprobada por el Jefe de Control Interno |  |
| 57 | `fecha_aprobacion` | `timestamp without time zone` | sí | Fecha y hora en que la auditoría fue aprobada |  |
| 58 | `aprobada_por` | `character varying(255)` | sí | Nombre completo del usuario que aprobó la auditoría |  |
| 59 | `aprobada_por_id` | `bigint` | sí | ID del usuario que aprobó la auditoría (referencia a auth.personas) |  |
| 60 | `actividad_plan_anual_id` | `uuid` | sí | Referencia al registro de control_interno.actividad_plan_anual_5 (id). | FK→control_interno.actividad_plan_anual_5.id |
| 61 | `documento_cierre` | `jsonb` | sí | Documento de cierre obligatorio (matriz/formato): {nombre, url, tipo, tamano, fechaCarga, cargadoPor} |  |
| 62 | `observaciones_cierre` | `text` | sí | Observaciones o comentarios adicionales sobre el cierre de la auditoría |  |
| 63 | `fecha_finalizacion` | `timestamp without time zone` | sí | Fecha y hora en que se finalizó la auditoría |  |
| 64 | `finalizada_por` | `character varying(255)` | sí | Nombre del usuario que finalizó la auditoría |  |
| 65 | `finalizada_por_id` | `bigint` | sí | ID del usuario que finalizó la auditoría (referencia a auth.personas) |  |
| 66 | `fecha_fin_planeacion` | `date` | sí | Fin de Etapa 1: Planeación |  |
| 67 | `fecha_fin_ejecucion` | `date` | sí | Fin de Etapa 2: Ejecución |  |
| 68 | `fecha_inicio_ejecucion` | `date` | sí | Inicio de Etapa 2: Ejecución |  |
| 69 | `fecha_inicio_comunicacion` | `date` | sí | Inicio de Etapa 3: Comunicación |  |
| 70 | `lecciones_aprendidas` | `text` | sí | Lecciones aprendidas (Informe de Cierre - Sección 2) |  |
| 71 | `recomendaciones_futuras_auditorias` | `text` | sí | Recomendaciones para futuras auditorías (Informe de Cierre) |  |
| 72 | `informe_cierre_aprobado` | `boolean` | sí | Si el Jefe OCI aprobó el informe de cierre |  |
| 73 | `informe_cierre_aprobado_por` | `character varying(255)` | sí | Nombre de quien aprobó el informe de cierre |  |
| 74 | `informe_cierre_aprobado_por_id` | `bigint` | sí | ID del usuario que aprobó el informe de cierre |  |
| 75 | `informe_cierre_aprobado_at` | `timestamp without time zone` | sí | Fecha de aprobación del informe de cierre |  |
| 76 | `periodo_inicio` | `date` | sí | Fecha de inicio del periodo auditado. |  |
| 77 | `periodo_fin` | `date` | sí | Fecha de fin del periodo auditado. |  |
| 78 | `fortalezas` | `jsonb` | no | Fortalezas identificadas en la ejecución (lista de textos) |  |
| 79 | `recomendaciones_generales` | `jsonb` | no | Recomendaciones generales de la auditoría, adicionales a las de cada hallazgo (lista de textos) |  |
| 80 | `conclusiones` | `text` | sí | Conclusiones de la auditoría registradas en la ejecución |  |
| 81 | `semanas_excluidas` | `jsonb` | no | Lunes (YYYY-MM-DD) de las semanas que el usuario sacó del cronograma (EFDS-2132) |  |
| 82 | `unidades_auditables` | `jsonb` | no | Nombres de las unidades auditables del proceso que cubre la auditoría (EFDS-2316) |  |

## auditoria_especial_info

Información específica de auditorías especiales (motivo, solicitante, justificación).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `aprobado_por_id` → `auth.personas` (0..1 → 0..1); `auditoria_id` → `control_interno.auditoria` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla auditoria_especial_info. Se genera automáticamente. | PK |
| 2 | `auditoria_id` | `uuid` | no | Referencia al registro de control_interno.auditoria (id). | única FK→control_interno.auditoria.id |
| 3 | `tipo_motivo` | `character varying(100)` | no | Tipo de motivo de la auditoría especial. Valores permitidos: denuncia, emergencia, ente_control, solicitud_ente_control, revision_especifica, seguimiento_urgente, otro. |  |
| 4 | `solicitante` | `character varying(255)` | no | Entidad o persona que solicita la auditoría especial (por ejemplo, Contraloría General de la República). |  |
| 5 | `justificacion` | `text` | no | Justificación de la auditoría especial; mínimo 20 caracteres. |  |
| 6 | `fecha_solicitud` | `date` | sí | Fecha en que se solicitó la auditoría especial. |  |
| 7 | `fecha_aprobacion` | `date` | sí | Fecha en que se aprobó la auditoría especial. |  |
| 8 | `aprobado_por_id` | `uuid` | sí | Referencia al registro de auth.personas (id_person). | FK→auth.personas.id_person |
| 9 | `observaciones` | `text` | sí | Observaciones sobre la auditoría especial. |  |
| 10 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 11 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## auditoria_gestion

Gestión de auditorías con fases y seguimiento

- Clave primaria: `id`
- Filas: 0
- Referencia a: `auditoria_programada_id` → `control_interno.auditoria_programada` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla auditoria_gestion. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(255)` | no | Código de la auditoría en gestión. Único en la tabla. | única |
| 3 | `nombre` | `character varying(500)` | no | Nombre de la auditoría en gestión. |  |
| 4 | `tipo` | `character varying(100)` | no | Tipo de auditoría en gestión. |  |
| 5 | `fase` | `character varying(50)` | no | Fase de gestión de la auditoría. Valores permitidos: planeacion, en-curso, revision, completada; por defecto planeacion. |  |
| 6 | `territorial` | `character varying(255)` | sí | Dirección territorial donde se realiza la auditoría. |  |
| 7 | `sede` | `character varying(255)` | sí | Sede donde se realiza la auditoría. |  |
| 8 | `responsable` | `character varying(255)` | no | Responsable de la auditoría. |  |
| 9 | `fecha_inicio` | `date` | no | Fecha de inicio de la auditoría. |  |
| 10 | `fecha_fin` | `date` | no | Fecha de finalización de la auditoría. |  |
| 11 | `progreso` | `integer` | sí | Porcentaje de progreso de la auditoría, de 0 a 100. Por defecto 0. |  |
| 12 | `prioridad` | `character varying(20)` | no | Prioridad de la auditoría. Valores permitidos: Alta, Media, Baja; por defecto Media. |  |
| 13 | `hallazgos_count` | `integer` | sí | Número de hallazgos registrados en la auditoría. Por defecto 0. |  |
| 14 | `auditoria_programada_id` | `uuid` | sí | Referencia al registro de control_interno.auditoria_programada (id). | FK→control_interno.auditoria_programada.id |
| 15 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 16 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## auditoria_programada

Auditorías programadas en el plan anual

- Clave primaria: `id`
- Filas: 0
- Referencia a: `proceso_id` → `control_interno.proceso_auditable` (0..1 → 1); `programa_anual_id` → `control_interno.plan_anual` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla auditoria_programada. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(255)` | no | Código de la auditoría programada. Único en la tabla. | única |
| 3 | `nombre` | `character varying(255)` | no | Nombre de la auditoría programada. |  |
| 4 | `proceso_id` | `uuid` | no | Referencia al registro de control_interno.proceso_auditable (id). | FK→control_interno.proceso_auditable.id |
| 5 | `proceso_codigo` | `character varying(255)` | no | Código del proceso que se audita, copiado del proceso auditable referido por proceso_id al importar la auditoría al programa anual. |  |
| 6 | `proceso_nombre` | `character varying(255)` | no | Nombre del proceso que se audita, copiado del proceso auditable referido por proceso_id al importar la auditoría al programa anual. |  |
| 7 | `tipo` | `character varying(50)` | no | Tipo de auditoría programada (cumplimiento, desempeño, financiera, gestión o TIC). |  |
| 8 | `alcance` | `text` | no | Alcance de la auditoría programada. |  |
| 9 | `proceso_auditar` | `character varying(255)` | no | Proceso o tema que se va a auditar; al importar la auditoría desde el universo se llena con el nombre del proceso. |  |
| 10 | `auditor_lider` | `character varying(255)` | no | Auditor líder asignado a la auditoría programada, registrado como texto; queda vacío al importar la auditoría. |  |
| 11 | `equipo_auditor` | `jsonb` | no | Integrantes del equipo auditor, en formato JSON: objeto con las listas auditores, profesionalesEspecializados, profesionalesUniversitarios y tecnicos. Al importar la auditoría las listas quedan vacías. |  |
| 12 | `fecha_inicio_planeada` | `date` | no | Fecha planeada de inicio de la auditoría. |  |
| 13 | `fecha_fin_planeada` | `date` | no | Fecha planeada de finalización de la auditoría. |  |
| 14 | `duracion_dias` | `integer` | no | Duración planeada de la auditoría en días calendario (mínimo 1): suma de las duraciones de planeación, ejecución y comunicación; se actualiza al ampliar el plazo. |  |
| 15 | `prioridad` | `character varying(20)` | no | Prioridad de la auditoría programada. Valores permitidos: alta, media, baja. |  |
| 16 | `riesgo_inherente` | `character varying(20)` | no | Nivel de riesgo inherente del proceso auditado. Valores permitidos: alto, medio, bajo. |  |
| 17 | `estado` | `character varying(50)` | no | Estado de la auditoría programada (planeada, en curso, completada o cancelada). |  |
| 18 | `es_territorial` | `boolean` | sí | Indica si la auditoría programada es territorial. |  |
| 19 | `territorial` | `character varying(255)` | sí | Dirección territorial donde se realiza la auditoría, cuando es territorial; al importarla se copia del proceso auditable. |  |
| 20 | `es_especial` | `boolean` | sí | Indica si la auditoría programada es especial. |  |
| 21 | `solicitada_por` | `character varying(255)` | sí | Usuario que realizó la solicitud. |  |
| 22 | `motivo_especial` | `text` | sí | Motivo del especial. |  |
| 23 | `etapas` | `jsonb` | no | Etapas planeadas de la auditoría, en formato JSON: objetos planeacion, ejecucion y comunicacion, cada uno con fecha de inicio, fecha de fin, duración en días y estado (pendiente al crearse). |  |
| 24 | `ampliaciones` | `jsonb` | sí | Historial de ampliaciones de plazo de la auditoría programada, en formato JSON: lista con fecha de solicitud y de autorización, justificación, quien autoriza, fechas límite anterior y nueva y duraciones anterior y nueva. Lo escribe el programa anual; no se relaciona con control_interno.ampliacion_plazo. |  |
| 25 | `fecha_limite_original` | `date` | no | Fecha límite inicial de la auditoría programada, antes de ampliaciones. |  |
| 26 | `fecha_limite_actual` | `date` | no | Fecha límite vigente de la auditoría programada. |  |
| 27 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 28 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 29 | `programa_anual_id` | `uuid` | sí | Referencia al plan anual al que pertenece esta auditoría | FK→control_interno.plan_anual.id |

## auditoria_territorial_info

Información específica de auditorías territoriales (ciudad, departamento, contacto).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla auditoria_territorial_info. Se genera automáticamente. | PK |
| 2 | `auditoria_id` | `uuid` | no | Referencia al registro de control_interno.auditoria (id). | única FK→control_interno.auditoria.id |
| 3 | `nombre` | `character varying(255)` | no | Nombre de la territorial auditada (por ejemplo, «Antioquia - Medellín»). |  |
| 4 | `ciudad` | `character varying(255)` | no | Ciudad donde se realiza la auditoría territorial. |  |
| 5 | `departamento` | `character varying(255)` | no | Departamento donde se realiza la auditoría territorial. |  |
| 6 | `direccion` | `text` | sí | Dirección física del lugar de la auditoría territorial. | Contacto |
| 7 | `contacto_nombre` | `character varying(255)` | sí | Nombre de la persona de contacto en la sede territorial. |  |
| 8 | `contacto_email` | `character varying(255)` | sí | Correo electrónico de la persona de contacto en la sede territorial. | Contacto |
| 9 | `contacto_telefono` | `character varying(20)` | sí | Teléfono de la persona de contacto en la sede territorial. | Contacto |
| 10 | `observaciones` | `text` | sí | Observaciones sobre la auditoría territorial. |  |
| 11 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## cache_esap

Cache del sistema ESAP

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla cache_esap. Se genera automáticamente. | PK |
| 2 | `clave` | `character varying(500)` | no | Clave única de la entrada de caché. | única |
| 3 | `valor` | `jsonb` | no | Valor almacenado en caché para la clave, en formato JSON. |  |
| 4 | `fecha_expiracion` | `timestamp without time zone` | sí | Fecha y hora en que expira la entrada de caché. |  |
| 5 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 6 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## cierre_plan

Cierre de los planes de mejoramiento (EM-PT-002 act. 8-10, RF-SG-11, RF-SG-12). Un registro por cierre de plan, con la fecha y el responsable del cierre, observaciones, verificación de efectividad y archivo del expediente mediante índice electrónico.

- Clave primaria: `id`
- Filas: 2
- Referencia a: `plan_id` → `control_interno.plan_mejoramiento` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla cierre_plan. Se genera automáticamente. | PK |
| 2 | `plan_id` | `uuid` | no | Referencia al registro de control_interno.plan_mejoramiento (id). | única FK→control_interno.plan_mejoramiento.id |
| 3 | `cerrado` | `boolean` | sí | Indica si el plan de mejoramiento está cerrado; por defecto falso. |  |
| 4 | `fecha_cierre` | `timestamp with time zone` | sí | Fecha y hora de cierre del plan de mejoramiento. |  |
| 5 | `cerrado_por_id` | `character varying(255)` | sí | Identificador del responsable que cerró el plan (jefe de la Oficina de Control Interno o delegado). |  |
| 6 | `cerrado_por_nombre` | `character varying(500)` | sí | Nombre del responsable que cerró el plan, copiado para trazabilidad. |  |
| 7 | `observaciones_cierre` | `text` | sí | Observaciones del cierre del plan. |  |
| 8 | `efectividad_verificada` | `boolean` | sí | Indica si la efectividad se verificó en la siguiente auditoría; por defecto falso (EM-PT-002, actividad 9). |  |
| 9 | `archivado` | `boolean` | sí | Indica si el expediente del plan se archivó con índice electrónico; por defecto falso (EM-PT-002, actividad 10). |  |
| 10 | `indice_electronico_ref` | `character varying(1000)` | sí | Referencia al índice electrónico del expediente del plan. |  |
| 11 | `fecha_archivo` | `timestamp with time zone` | sí | Fecha y hora de archivo del expediente. |  |
| 12 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## condicion_disparo_notificacion

Catálogo de condiciones que disparan notificaciones en el módulo de control interno. Un registro por condición, con su nombre, descripción y estado activo.

- Clave primaria: `id`
- Filas: 12

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla condicion_disparo_notificacion. Se genera automáticamente. | PK |
| 2 | `nombre` | `character varying(255)` | no | Nombre de la condición que dispara la notificación. | única |
| 3 | `descripcion` | `character varying(255)` | sí | Descripción de la condición que dispara la notificación. |  |
| 4 | `activo` | `boolean` | sí | Indica si la condición de disparo de notificación está activa. |  |
| 5 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 6 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## configuracion_esap

Configuraciones específicas del sistema ESAP

- Clave primaria: `id`
- Filas: 7

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla configuracion_esap. Se genera automáticamente. | PK |
| 2 | `clave` | `character varying(255)` | no | Clave única del parámetro de configuración. | única |
| 3 | `valor` | `text` | no | Valor del parámetro de configuración. |  |
| 4 | `descripcion` | `text` | sí | Descripción del parámetro de configuración. |  |
| 5 | `tipo` | `character varying(50)` | sí | Tipo de dato del valor de configuración (boolean, json, number o string). |  |
| 6 | `categoria` | `character varying(255)` | sí | Categoría con la que se agrupa el parámetro de configuración. |  |
| 7 | `activo` | `boolean` | sí | Indica si el parámetro de configuración está activo. |  |
| 8 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## configuracion_profesionales_ocig

Configuración de profesionales asignados al equipo OCIG (Oficina de Control Interno de Gestión)

- Clave primaria: `id`
- Filas: 31

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla configuracion_profesionales_ocig. Se genera automáticamente. | PK |
| 2 | `id_tercero` | `character varying(36)` | no | ID del tercero (persona) en auth.personas | única |
| 3 | `rol_ocig` | `character varying(100)` | no | Rol del profesional dentro del equipo OCIG |  |
| 4 | `especialidades` | `text[]` | sí | Array de especialidades del profesional (ej: Auditoría Financiera, Auditoría TI) |  |
| 5 | `capacidad_maxima_auditorias` | `integer` | no | Número máximo de auditorías simultáneas que puede manejar |  |
| 6 | `horas_mensuales_disponibles` | `integer` | no | Horas mensuales disponibles para auditorías |  |
| 7 | `puede_ser_lider` | `boolean` | no | Indica si el profesional puede ser asignado como auditor líder |  |
| 8 | `activo` | `boolean` | no | Indica si el profesional está activo en el equipo de la Oficina de Control Interno de Gestión. |  |
| 9 | `fecha_asignacion` | `date` | no | Fecha en que el profesional se asignó al equipo OCIG; por defecto la fecha actual. |  |
| 10 | `observaciones` | `text` | sí | Observaciones sobre la asignación del profesional al equipo de la Oficina de Control Interno de Gestión. |  |
| 11 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 12 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 13 | `created_by` | `uuid` | sí | Usuario que creó el registro. |  |
| 14 | `updated_by` | `uuid` | sí | Usuario que realizó la última actualización del registro. |  |

## criterio_auditoria

Criterios de auditoría (normas, políticas, estándares aplicables)

- Clave primaria: `id`
- Filas: 27
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla criterio_auditoria. Se genera automáticamente. | PK |
| 2 | `auditoria_id` | `uuid` | no | Referencia al registro de control_interno.auditoria (id). | FK→control_interno.auditoria.id |
| 3 | `criterio` | `text` | no | Texto del criterio de auditoría (norma, política o estándar aplicable). |  |
| 4 | `orden` | `integer` | sí | Posición del criterio en la lista de criterios de la auditoría. |  |
| 5 | `activo` | `boolean` | sí | Indica si el criterio de auditoría está activo. |  |
| 6 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 7 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## cronograma_auditoria

Cronograma de auditorías del plan anual

- Clave primaria: `id`
- Filas: 0
- Referencia a: `plan_id` → `control_interno.plan_anual` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla cronograma_auditoria. Se genera automáticamente. | PK |
| 2 | `plan_id` | `uuid` | no | Referencia al registro de control_interno.plan_anual (id). | FK→control_interno.plan_anual.id |
| 3 | `codigo` | `character varying(255)` | no | Código de la auditoría en el cronograma. |  |
| 4 | `nombre` | `character varying(255)` | no | Nombre de la auditoría en el cronograma. |  |
| 5 | `proceso` | `character varying(255)` | no | Proceso que se audita en la auditoría del cronograma. |  |
| 6 | `nivel_riesgo` | `character varying(20)` | sí | Nivel de riesgo del proceso. Valores permitidos: Alto, Medio, Bajo. |  |
| 7 | `trimestre` | `character varying(10)` | no | Trimestre del año en que se programa la auditoría. |  |
| 8 | `fecha_inicio` | `date` | no | Fecha de inicio de la auditoría en el cronograma. |  |
| 9 | `fecha_fin` | `date` | no | Fecha de finalización de la auditoría en el cronograma. |  |
| 10 | `auditor_responsable` | `character varying(255)` | sí | Auditor responsable de la auditoría programada. |  |
| 11 | `horas_estimadas` | `integer` | no | Horas estimadas para ejecutar la auditoría. |  |
| 12 | `estado` | `character varying(50)` | sí | Estado de la auditoría en el cronograma (planificado, en ejecución, en revisión, completada o cancelada). |  |
| 13 | `es_territorial` | `boolean` | sí | Indica si la auditoría del cronograma es territorial. |  |
| 14 | `territorial` | `character varying(255)` | sí | Dirección territorial de la auditoría, cuando es territorial. |  |
| 15 | `es_especial` | `boolean` | sí | Indica si la auditoría del cronograma es especial. |  |
| 16 | `equipo` | `jsonb` | sí | Integrantes del equipo auditor, en formato JSON. |  |
| 17 | `etapas_cronograma` | `jsonb` | sí | Etapas del cronograma de la auditoría, en formato JSON. |  |
| 18 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 19 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## cronograma_fase_auditoria

Cronograma estimado por fase de la auditoría (duración de cada fase)

- Clave primaria: `id`
- Filas: 0
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla cronograma_fase_auditoria. Se genera automáticamente. | PK |
| 2 | `auditoria_id` | `uuid` | no | Referencia al registro de control_interno.auditoria (id). | FK→control_interno.auditoria.id |
| 3 | `fase` | `character varying(50)` | no | Fase de la auditoría a la que corresponde el cronograma. Valores permitidos: Planeación, Comunicación, Ejecución, Seguimiento. |  |
| 4 | `fecha_inicio` | `date` | no | Fecha estimada de inicio de la fase de la auditoría. |  |
| 5 | `fecha_fin` | `date` | no | Fecha estimada de finalización de la fase de la auditoría. |  |
| 6 | `dias_estimados` | `integer` | no | Duración estimada de la fase de la auditoría, en días. |  |
| 7 | `observaciones` | `text` | sí | Observaciones sobre el cronograma de la fase. |  |
| 8 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## datos_automaticos_informe

Datos automáticos poblados desde el sistema (US-022)

- Clave primaria: `id`
- Filas: 0
- Referencia a: `entrega_id` → `control_interno.entrega_informe_ley` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla datos_automaticos_informe. Se genera automáticamente. | PK |
| 2 | `entrega_id` | `uuid` | no | Referencia al registro de control_interno.entrega_informe_ley (id). | FK→control_interno.entrega_informe_ley.id |
| 3 | `tipo_dato` | `character varying(100)` | no | Tipo de dato poblado automáticamente desde el sistema para el informe, por ejemplo auditorias, planes_mejoramiento, indicadores o hallazgos (US-022). |  |
| 4 | `datos` | `jsonb` | no | JSON con los datos estructurados según el tipo de dato |  |
| 5 | `fecha_generacion` | `timestamp without time zone` | sí | Fecha y hora en que se generaron los datos automáticos del informe. |  |
| 6 | `fuente_datos` | `character varying(255)` | sí | Fuente de los datos automáticos del informe, por ejemplo sistema, api_externa o manual. |  |
| 7 | `version_datos` | `character varying(50)` | sí | Versión del conjunto de datos automáticos del informe. Por defecto 1.0. |  |
| 8 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## documento

Gestión documental centralizada (RF013)

- Clave primaria: `id`
- Filas: 77
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..* → 0..1); `documento_biblioteca_id` → `control_interno.documento` (0..* → 0..1); `version_anterior_id` → `control_interno.documento` (0..* → 0..1)
- Relaciones implícitas: `etapa_kanban_id` ↝ `control_interno.etapa_kanban` (100.0 % con padre); `hallazgo_id` ↝ `control_interno.hallazgo` (100.0 % con padre)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla documento. Se genera automáticamente. | PK |
| 2 | `nombre` | `character varying(255)` | no | Nombre del documento. |  |
| 3 | `descripcion` | `text` | sí | Descripción del documento. |  |
| 4 | `tipo_documento` | `character varying(100)` | no | Tipo de documento: oficio_anuncio, carta_representacion, carta_compromiso, programa_individual, acta_reunion_apertura, acta_reunion_cierre, lista_chequeo, evidencia_hallazgo, evidencia_controversia, informe_preliminar, informe_final, informe_ejecutivo, evidencia_plan_mejoramiento y, para la biblioteca de plantillas, plantilla, oficio, acta, informe, evidencia, formato, guia u otro. Los tipos informe_preliminar, informe_final e informe_ejecutivo se cuentan como informes de la auditoría. |  |
| 5 | `etapa` | `character varying(50)` | sí | Etapa de la auditoría a la que pertenece el documento. Valores permitidos: planeacion, planificacion, comunicacion, ejecucion, hallazgos, comunicacion_resultados, seguimiento, cierre. |  |
| 6 | `auditoria_id` | `uuid` | sí | Referencia al registro de control_interno.auditoria (id). | FK→control_interno.auditoria.id |
| 7 | `hallazgo_id` | `uuid` | sí | Hallazgo al que se vincula el documento; relación sin llave foránea declarada. | ↝control_interno.hallazgo.id |
| 8 | `plan_mejoramiento_id` | `uuid` | sí | Identificador del plan de mejoramiento (control_interno.plan_mejoramiento) al que se vincula el documento; se deja en nulo si se borra el plan. |  |
| 9 | `ruta_archivo` | `character varying(500)` | no | Ruta de almacenamiento del archivo del documento. |  |
| 10 | `nombre_archivo` | `character varying(255)` | no | Nombre del archivo del documento. |  |
| 11 | `tipo_mime` | `character varying(100)` | no | Tipo MIME del archivo (por ejemplo, application/pdf). |  |
| 12 | `tamanio_bytes` | `bigint` | no | Tamaño del archivo, en bytes. |  |
| 13 | `version` | `integer` | sí | Número de versión del documento. |  |
| 14 | `version_anterior_id` | `uuid` | sí | Referencia al registro de control_interno.documento (id). | FK→control_interno.documento.id |
| 15 | `subido_por` | `character varying(255)` | no | Usuario que realizó la carga. |  |
| 16 | `hash_archivo` | `character varying(255)` | sí | Hash SHA-256 (hexadecimal) del contenido del archivo; se calcula al subirlo y se usa para detectar duplicados y crear una nueva versión. |  |
| 17 | `comprimido` | `boolean` | sí | Indica si el archivo del documento está comprimido. |  |
| 18 | `ruta_servidor_g` | `character varying(500)` | sí | Ruta del archivo en el servidor G, registrada al marcar el documento como sincronizado junto con sincronizado_servidor_g y fecha_sincronizacion. |  |
| 19 | `sincronizado_servidor_g` | `boolean` | sí | Indica si el documento está sincronizado con el servidor G. |  |
| 20 | `fecha_sincronizacion` | `timestamp without time zone` | sí | Fecha y hora de la sincronización del documento con el servidor G. |  |
| 21 | `tipo_reporte` | `character varying(100)` | sí | Tipo de reporte cuando el documento es un reporte generado. Valores permitidos: acta-apertura, acta-cierre, informe-auditoria, matriz-hallazgos, plan-anual, plan-mejora, reporte-cumplimiento, reporte-ejecutivo, reporte-gravedad, reporte-territorial, otro. |  |
| 22 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 23 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 24 | `documento_biblioteca_id` | `uuid` | sí | Referencia al registro de control_interno.documento (id). | FK→control_interno.documento.id |
| 25 | `visible_auditoria_id` | `uuid` | sí | Identificador de la auditoría para la que es visible el documento plantilla; nulo indica que es visible para todas. |  |
| 26 | `etapa_kanban_id` | `uuid` | sí | ID de la etapa en tabla etapa_kanban (FK lógica - estable aunque cambie el nombre) | ↝control_interno.etapa_kanban.id |
| 27 | `etapa_kanban_nombre` | `character varying(255)` | sí | Nombre de la etapa al momento de guardar (snapshot para mostrar aunque cambie la configuración) |  |
| 28 | `plan_anual_vigencia` | `integer` | sí | Año de vigencia del plan anual (plantillas de biblioteca) |  |
| 29 | `plan_anual_id` | `uuid` | sí | UUID del plan anual 5 roles asociado |  |

## documento_aprobacion

Archivos adjuntos a las solicitudes de aprobación de control interno. Un registro por archivo, asociado a una aprobación (control_interno.aprobacion) y a un documento (control_interno.documento), con nombre, ruta, tipo MIME y tamaño.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `aprobacion_id` → `control_interno.aprobacion` (0..1 → 1); `documento_id` → `control_interno.documento` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla documento_aprobacion. Se genera automáticamente. | PK |
| 2 | `aprobacion_id` | `uuid` | no | Referencia al registro de control_interno.aprobacion (id). | FK→control_interno.aprobacion.id |
| 3 | `documento_id` | `uuid` | sí | Referencia al registro de control_interno.documento (id). | FK→control_interno.documento.id |
| 4 | `nombre_archivo` | `character varying(255)` | no | Nombre del archivo adjunto a la solicitud de aprobación. |  |
| 5 | `ruta_archivo` | `character varying(500)` | sí | Ruta de almacenamiento del archivo adjunto. |  |
| 6 | `tipo_mime` | `character varying(100)` | sí | Tipo MIME del archivo adjunto. |  |
| 7 | `tamanio_bytes` | `bigint` | sí | Tamaño del archivo adjunto, en bytes. |  |
| 8 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |

## documento_plan_mejoramiento

Documentos adjuntos a los planes de mejoramiento y a sus acciones correctivas. Un registro por documento, con nombre, tipo, datos del archivo, quién y cuándo lo cargó, y su validación por el auditor (pendiente de revisión, aceptada, con observaciones o rechazada).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `accion_id` → `control_interno.accion_correctiva` (0..1 → 0..1); `plan_mejoramiento_id` → `control_interno.plan_mejoramiento` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla documento_plan_mejoramiento. Se genera automáticamente. | PK |
| 2 | `plan_mejoramiento_id` | `uuid` | no | Referencia al registro de control_interno.plan_mejoramiento (id). | FK→control_interno.plan_mejoramiento.id |
| 3 | `accion_id` | `uuid` | sí | Referencia al registro de control_interno.accion_correctiva (id). | FK→control_interno.accion_correctiva.id |
| 4 | `nombre` | `character varying(255)` | no | Nombre del documento del plan de mejoramiento. |  |
| 5 | `descripcion` | `text` | sí | Descripción del documento del plan de mejoramiento. |  |
| 6 | `tipo_documento` | `character varying(100)` | no | Tipo de documento del plan de mejoramiento, en texto recibido del cliente; por defecto documento_plan para los documentos del plan y evidencia_accion para las evidencias de una acción. |  |
| 7 | `ruta_archivo` | `character varying(500)` | no | Ruta de almacenamiento del archivo. |  |
| 8 | `nombre_archivo_original` | `character varying(255)` | no | Nombre original del archivo al momento de subirlo. |  |
| 9 | `tipo_mime` | `character varying(100)` | no | Tipo MIME del archivo. |  |
| 10 | `tamanio_bytes` | `bigint` | no | Tamaño del archivo, en bytes. |  |
| 11 | `subido_por` | `character varying(255)` | no | Usuario que realizó la carga. |  |
| 12 | `subido_por_id` | `bigint` | sí | Identificador numérico del usuario que subió el documento, enviado por el cliente. |  |
| 13 | `fecha_subida` | `timestamp with time zone` | sí | Fecha y hora en que se cargó el documento. |  |
| 14 | `estado_validacion` | `character varying(50)` | sí | Estado de la validación de la evidencia por el auditor: PENDIENTE_REVISION, ACEPTADA, CON_OBSERVACIONES o RECHAZADA; por defecto PENDIENTE_REVISION. |  |
| 15 | `comentarios_auditor` | `text` | sí | Comentarios del auditor al validar el documento. |  |
| 16 | `fecha_validacion` | `timestamp with time zone` | sí | Fecha y hora en que se validó el documento. |  |
| 17 | `validado_por` | `character varying(255)` | sí | Usuario que realizó la validación. |  |
| 18 | `solicita_nueva_evidencia` | `boolean` | sí | Indica si se solicitó una nueva evidencia para el documento. |  |
| 19 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 20 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## entrega_informe_ley

Entregas de informes de ley por periodo

- Clave primaria: `id`
- Filas: 0
- Referencia a: `informe_id` → `control_interno.informe_ley` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla entrega_informe_ley. Se genera automáticamente. | PK |
| 2 | `informe_id` | `uuid` | no | Referencia al registro de control_interno.informe_ley (id). | FK→control_interno.informe_ley.id |
| 3 | `periodo` | `character varying(50)` | no | Periodo que reporta la entrega del informe de ley, en formato mes (2025-01), trimestre (2025-Q1), semestre (2025-S1) o año (2025). |  |
| 4 | `fecha_vencimiento` | `date` | no | Fecha de vencimiento de la entrega del informe de ley. |  |
| 5 | `fecha_entrega` | `timestamp without time zone` | sí | Fecha y hora en que se entregó el informe de ley. |  |
| 6 | `estado` | `character varying(50)` | no | Estado de la entrega del informe de ley (pendiente, en proceso, entregado, rechazado o vencido). |  |
| 7 | `archivo_nombre` | `character varying(255)` | sí | Nombre del archivo del informe entregado. |  |
| 8 | `archivo_url` | `character varying(500)` | sí | URL del archivo entregado del informe de ley. |  |
| 9 | `archivo_tamano` | `bigint` | sí | Tamaño en bytes del archivo del informe entregado, cargado por el usuario o generado desde la plantilla. |  |
| 10 | `elaborado_por` | `character varying(255)` | sí | Nombre del usuario que elaboró la entrega del informe; «Sistema» cuando no se conoce el nombre. |  |
| 11 | `fecha_elaboracion` | `timestamp without time zone` | sí | Fecha y hora en que se elaboró el informe de ley. |  |
| 12 | `aprobado_por` | `character varying(255)` | sí | Usuario que realizó la aprobación. |  |
| 13 | `fecha_aprobacion` | `timestamp without time zone` | sí | Fecha y hora en que se aprobó el informe de ley. |  |
| 14 | `enviado_por` | `character varying(255)` | sí | Usuario que realizó el envío. |  |
| 15 | `observaciones` | `text` | sí | Observaciones sobre la entrega del informe. |  |
| 16 | `motivo_rechazo` | `text` | sí | Motivo del rechazo. |  |
| 17 | `numero_radicado` | `character varying(255)` | sí | Número de radicado de la entrega del informe. |  |
| 18 | `fecha_radicacion` | `timestamp without time zone` | sí | Fecha y hora en que se radicó el informe de ley. |  |
| 19 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 20 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 21 | `estado_workflow` | `character varying(50)` | sí | Estado en el workflow de aprobación |  |
| 22 | `datos_automaticos_poblados` | `boolean` | sí | Indica si los datos automáticos fueron poblados |  |
| 23 | `fecha_generacion` | `timestamp without time zone` | sí | Fecha y hora en que se generó el archivo del informe de ley. |  |
| 24 | `generado_por` | `character varying(255)` | sí | Usuario que realizó la generación. |  |
| 25 | `formato_archivo` | `character varying(50)` | sí | Formato del archivo generado. Valores permitidos: PDF, Word, Excel. |  |
| 26 | `plantilla_usada` | `character varying(255)` | sí | Plantilla con la que se generó el archivo de la entrega; copia el valor de url_plantilla del informe de ley (ruta o código de la plantilla) al generar el archivo. |  |
| 27 | `version_plantilla` | `character varying(50)` | sí | Versión de la plantilla usada para generar el informe. |  |
| 28 | `metadata_generacion` | `jsonb` | sí | Metadatos de la generación: tiempo, tamaño, variables usadas, etc. |  |

## equipo_auditor

Equipo de auditores asignados a una auditoría. Relación N-N entre auditorías y personas.

- Clave primaria: `id`
- Filas: 160
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..* → 1); `persona_id` → `auth.personas` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla equipo_auditor. Se genera automáticamente. | PK |
| 2 | `auditoria_id` | `uuid` | no | Referencia al registro de control_interno.auditoria (id). | FK→control_interno.auditoria.id |
| 3 | `persona_id` | `uuid` | no | Referencia al registro de auth.personas (id_person). | FK→auth.personas.id_person |
| 4 | `rol` | `character varying(100)` | sí | Rol del auditor en esta auditoría específica: Auditor, Auditor Senior, Auditor Junior, Inspector, Profesional Especializado, etc. |  |
| 5 | `activo` | `boolean` | sí | Indica si la asignación del auditor a la auditoría está activa. |  |
| 6 | `fecha_asignacion` | `timestamp without time zone` | sí | Fecha y hora en que se asignó el auditor a la auditoría. |  |
| 7 | `fecha_retiro` | `timestamp without time zone` | sí | Fecha y hora en que se retiró el auditor de la auditoría. |  |
| 8 | `observaciones` | `text` | sí | Observaciones sobre la asignación del auditor a la auditoría. |  |
| 9 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 10 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## especialidades_ocig

Catálogo de especialidades de la Oficina de Control Interno de Gestión (OCIG). Un registro por especialidad, con su nombre, descripción, orden y estado activo.

- Clave primaria: `id`
- Filas: 13

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla especialidades_ocig. Se genera automáticamente. | PK |
| 2 | `nombre` | `character varying(100)` | no | Nombre de la especialidad de la Oficina de Control Interno de Gestión. | única |
| 3 | `descripcion` | `text` | sí | Descripción de la especialidad. |  |
| 4 | `activo` | `boolean` | sí | Indica si la especialidad está activa. |  |
| 5 | `orden` | `integer` | sí | Posición de la especialidad en el listado. |  |
| 6 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 7 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## etapa_auditoria

Etapas de ejecución de auditorías

- Clave primaria: `id`
- Filas: 0
- Referencia a: `auditoria_id` → `control_interno.auditoria_programada` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla etapa_auditoria. Se genera automáticamente. | PK |
| 2 | `auditoria_id` | `uuid` | no | Referencia al registro de control_interno.auditoria_programada (id). | FK→control_interno.auditoria_programada.id |
| 3 | `etapa` | `character varying(50)` | no | Etapa de ejecución de la auditoría. Valores permitidos: planeacion, comunicacion, ejecucion. |  |
| 4 | `estado` | `character varying(50)` | no | Estado de la etapa de la auditoría (pendiente, en progreso o completada). |  |
| 5 | `fecha_inicio` | `date` | no | Fecha de inicio de la etapa de la auditoría. |  |
| 6 | `fecha_fin` | `date` | sí | Fecha de finalización de la etapa de la auditoría. |  |
| 7 | `fecha_limite` | `date` | no | Fecha límite de la etapa de la auditoría. |  |
| 8 | `datos` | `jsonb` | no | Datos registrados para la etapa de la auditoría, en formato JSON. |  |
| 9 | `porcentaje_avance` | `integer` | sí | Porcentaje de avance de la etapa de la auditoría, de 0 a 100; 0 por defecto. |  |
| 10 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 11 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## etapa_kanban

Etapas configuradas para cada tablero Kanban

- Clave primaria: `id`
- Filas: 12
- Referencia a: `tablero_kanban_id` → `control_interno.tablero_kanban` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla etapa_kanban. Se genera automáticamente. | PK |
| 2 | `tablero_kanban_id` | `uuid` | no | Referencia al registro de control_interno.tablero_kanban (id). | FK→control_interno.tablero_kanban.id |
| 3 | `nombre` | `character varying(255)` | no | Nombre de la etapa del tablero Kanban. |  |
| 4 | `descripcion` | `text` | sí | Descripción de la etapa del tablero Kanban. |  |
| 5 | `orden` | `integer` | no | Posición de la etapa en el tablero Kanban. |  |
| 6 | `color` | `character varying(7)` | no | Color de la etapa en el tablero Kanban, en formato hexadecimal. |  |
| 7 | `tiempo_sla` | `integer` | no | Tiempo SLA en días hábiles para esta etapa |  |
| 8 | `limite_wip` | `integer` | sí | Límite de elementos en progreso (null = sin límite) |  |
| 9 | `visible` | `boolean` | no | Indica si la etapa se muestra en el tablero Kanban. |  |
| 10 | `notificar_vencimiento` | `boolean` | no | Indica si se notifica el vencimiento en la etapa. |  |
| 11 | `dias_anticipacion_alerta` | `integer` | no | Días de anticipación con que se alerta el vencimiento de la etapa; mínimo 0 y 0 por defecto. |  |
| 12 | `estado` | `character varying(20)` | no | Estado de la etapa: inicial, intermedia o final |  |
| 13 | `permitir_retroceso` | `boolean` | no | Indica si se permite devolver elementos a una etapa anterior desde esta etapa. |  |
| 14 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 15 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 16 | `deleted_at` | `timestamp with time zone` | sí | Fecha y hora de la eliminación. |  |

## evaluacion_proceso

Evaluaciones DAFP de procesos auditables. Cada proceso puede tener múltiples evaluaciones con diferentes vigencias/fechas de corte.

- Clave primaria: `id`
- Filas: 54
- Referencia a: `proceso_id` → `control_interno.proceso_auditable` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla evaluacion_proceso. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | FK al proceso maestro del catálogo | FK→control_interno.proceso_auditable.id |
| 3 | `vigencia` | `integer` | no | Año de la evaluación (ej: 2025, 2026) |  |
| 4 | `fecha_corte` | `date` | no | Fecha de corte para la evaluación |  |
| 5 | `dependencia_responsable` | `text` | no | Dependencia responsable del proceso evaluado. |  |
| 6 | `riesgos_extremos` | `integer` | sí | Número de riesgos inherentes de nivel extremo del proceso (sección 1 de la evaluación). Por defecto 0. |  |
| 7 | `riesgos_altos` | `integer` | sí | Número de riesgos inherentes de nivel alto del proceso. Por defecto 0. |  |
| 8 | `riesgos_moderados` | `integer` | sí | Número de riesgos inherentes de nivel moderado del proceso. Por defecto 0. |  |
| 9 | `riesgos_bajos` | `integer` | sí | Número de riesgos inherentes de nivel bajo del proceso. Por defecto 0. |  |
| 10 | `total_riesgos` | `integer` | sí | Número total de riesgos inherentes del proceso: suma de riesgos extremos, altos, moderados y bajos. Por defecto 0. |  |
| 11 | `requerimiento_comite` | `boolean` | sí | Indica si existe un requerimiento del Comité de Auditoría o de la Dirección para auditar el proceso; si es verdadero, el proceso se incluye en el Plan Anual de Auditoría. Por defecto falso. |  |
| 12 | `requerimiento_entes_reg` | `boolean` | sí | Indica si existe un requerimiento de entes reguladores (por ejemplo, Contraloría, Procuraduría o ministerios) para auditar el proceso; no registra cuál ente lo hizo. Por defecto falso. |  |
| 13 | `fecha_ultima_auditoria` | `date` | sí | Fecha de la última auditoría realizada al proceso (sección 3 de la evaluación). |  |
| 14 | `resultado_ultima_auditoria` | `character varying(100)` | sí | Resultado de la última auditoría realizada al proceso: SIN_AUDITORIA, ADECUADO o INADECUADO, en texto de hasta 100 caracteres. |  |
| 15 | `criticidad` | `integer` | sí | Calificación de criticidad del proceso, de 0 a 5; componente C del puntaje de riesgo C+E-M. Por defecto 0. |  |
| 16 | `exposicion` | `integer` | sí | Calificación de exposición del proceso, de 0 a 5; es el componente E del puntaje de riesgo C+E-M. Por defecto 0. |  |
| 17 | `mitigantes` | `integer` | sí | Calificación de los mitigantes del proceso, de 0 a 5; es el componente M que se resta en el puntaje de riesgo C+E-M. Por defecto 0. |  |
| 18 | `score_riesgo` | `integer` | sí | Puntaje de riesgo del proceso, de 0 a 15, calculado como criticidad + exposición − mitigantes y acotado a ese rango. Por defecto 0. |  |
| 19 | `ponderacion_riesgo` | `character varying(20)` | sí | Resultado del cálculo DAFP: EXTREMO, ALTO, MODERADO, BAJO, MUY BAJO |  |
| 20 | `dias_transcurridos` | `integer` | sí | Número de días transcurridos desde la última auditoría del proceso. |  |
| 21 | `plan_rotacion` | `character varying(20)` | sí | Ciclo de rotación de auditoría asignado al proceso según la ponderación DAFP; el formulario actual guarda el mismo valor de ciclo_rotacion_dafp (Cada año, Cada 2 años, Cada 3 años, Cada 4 años, No auditar o Todos los años). |  |
| 22 | `dias_rotacion` | `integer` | sí | Número de días del ciclo de rotación de auditoría del proceso, derivado del ciclo DAFP (365, 730, 1095 o 1460; 0 para No auditar). Si no se informa un valor, el sistema usa 360. |  |
| 23 | `decision_rotacion` | `character varying(20)` | sí | Decisión de programación según la rotación: «Incluir en año 1» o «Programar según rotación». Complementa decision_final, que registra INCLUIR_PLAN_ANUAL o INCLUIR_AUDITORIA_POSTERIOR. |  |
| 24 | `decision_final` | `character varying(50)` | sí | Decisión: INCLUIR PLAN ANUAL o AUDITORÍA POSTERIOR |  |
| 25 | `motivo_decision` | `text` | sí | Motivo de la decisión final sobre la auditoría del proceso; el formulario lo genera con la ponderación DAFP, el nivel, el ciclo y si el proceso queda en el año 1 o en años posteriores. |  |
| 26 | `prioridad_regla` | `integer` | sí | Número de la regla DAFP aplicada en la evaluación del proceso, de 1 a 5. |  |
| 27 | `creado_por` | `character varying(255)` | sí | Usuario que creó el registro. |  |
| 28 | `activo` | `boolean` | sí | Indica si la evaluación del proceso está activa. Por defecto verdadero. |  |
| 29 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 30 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 31 | `tiempo_ultima_auditoria` | `integer` | sí | Criterio DAFP: tiempo transcurrido desde la última auditoría. 1=<=1año … 5=>4años/Nunca |  |
| 32 | `temas_alta_direccion` | `integer` | sí | Criterio DAFP: temas de interés de la Alta Dirección. 2=Bajo … 5=Muy relevante |  |
| 33 | `objetivos_estrategicos` | `integer` | sí | Criterio DAFP: cantidad de objetivos estratégicos asociados. 2=1 obj … 5=4+ obj |  |
| 34 | `hallazgos_anteriores` | `integer` | sí | Criterio DAFP: resultados de auditorías anteriores (hallazgos). 1=Sin hallazgos … 5=7+ |  |
| 35 | `ponderacion_final_dafp` | `numeric(4,2)` | sí | Ponderación DAFP calculada: RI×0.4 + Tiempo×0.1 + AD×0.1 + Obj×0.1 + Hallazgos×0.3 |  |
| 36 | `nivel_criticidad_dafp` | `character varying(20)` | sí | Nivel de criticidad resultante: Extremo \| Alto \| Moderado \| Bajo |  |
| 37 | `ciclo_rotacion_dafp` | `character varying(20)` | sí | Ciclo de rotación de auditorías: Cada año \| Cada 2 años \| Cada 3 años |  |
| 38 | `auditable_calculado` | `boolean` | no | Calculado al guardar evaluación DAFP: false si ciclo es No auditar, true si hay rotación. |  |
| 39 | `auditable_manual` | `boolean` | sí | Override manual desde tabla Universo. NULL = usar auditable_calculado. |  |

## eventos_timeline

Registro histórico de todos los eventos importantes relacionados con planes de mejoramiento

- Clave primaria: `id`
- Filas: 265
- Referencia a: `plan_mejoramiento_id` → `control_interno.plan_mejoramiento` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla eventos_timeline. Se genera automáticamente. | PK |
| 2 | `plan_mejoramiento_id` | `uuid` | no | ID del plan de mejoramiento al que pertenece el evento | FK→control_interno.plan_mejoramiento.id |
| 3 | `tipo` | `control_interno.tipo_evento_timeline` | no | Tipo de evento registrado (creación, actualización, evidencia, etc.) |  |
| 4 | `descripcion` | `text` | no | Descripción legible del evento para mostrar en el timeline |  |
| 5 | `usuario_id` | `uuid` | sí | ID del usuario que generó el evento |  |
| 6 | `usuario_nombre` | `character varying(255)` | sí | Nombre del usuario que generó el evento (desnormalizado para histórico) |  |
| 7 | `fecha` | `timestamp with time zone` | no | Fecha y hora en que ocurrió el evento |  |
| 8 | `metadata` | `jsonb` | sí | Información adicional del evento en formato JSON (IDs relacionados, valores anteriores/nuevos, etc.) |  |
| 9 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |

## evidencia_accion

Evidencias de cumplimiento que carga el área auditada para las acciones de mejora (RF-SG-02). Un registro por evidencia, asociada a una acción correctiva, con los datos del archivo, quién y cuándo la cargó, y la calificación del auditor de la Oficina de Control Interno con sus comentarios y la eventual solicitud de nueva evidencia (RF-SG-03, RF-SG-13).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `accion_id` → `control_interno.accion_correctiva` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla evidencia_accion. Se genera automáticamente. | PK |
| 2 | `accion_id` | `uuid` | no | Referencia al registro de control_interno.accion_correctiva (id). | FK→control_interno.accion_correctiva.id |
| 3 | `archivo_ref` | `character varying(1000)` | no | Referencia al archivo de la evidencia en el repositorio documental (URL o ruta relativa). |  |
| 4 | `archivo_nombre` | `character varying(500)` | no | Nombre original del archivo cargado. |  |
| 5 | `archivo_tipo` | `character varying(100)` | sí | Tipo MIME del archivo. |  |
| 6 | `archivo_tamanio` | `bigint` | sí | Tamaño del archivo en bytes. |  |
| 7 | `descripcion` | `text` | sí | Descripción libre de la evidencia. |  |
| 8 | `cargada_por_id` | `character varying(255)` | no | Identificador del usuario del área auditada que cargó la evidencia. |  |
| 9 | `cargada_por_nombre` | `character varying(500)` | sí | Nombre del usuario que cargó la evidencia, copiado para trazabilidad. |  |
| 10 | `cargada_at` | `timestamp with time zone` | sí | Fecha y hora de la carga. |  |
| 11 | `estado_validacion` | `character varying(30)` | sí | Estado de la validación de la evidencia por el auditor de la Oficina de Control Interno; por defecto pendiente (RF-SG-02). |  |
| 12 | `comentarios` | `text` | sí | Comentarios del auditor al calificar la evidencia; mínimo 10 caracteres. |  |
| 13 | `solicita_nueva_evidencia` | `boolean` | sí | Indica si el auditor solicita nueva evidencia o aclaraciones; por defecto falso (RF-SG-03). |  |
| 14 | `calificada_por_id` | `character varying(255)` | sí | Identificador del auditor que calificó la evidencia. |  |
| 15 | `calificada_por_nombre` | `character varying(500)` | sí | Nombre del auditor que calificó la evidencia, copiado para trazabilidad. |  |
| 16 | `calificada_at` | `timestamp with time zone` | sí | Fecha y hora de la calificación de la evidencia. |  |

## evidencia_documento

Sistema independiente de gestión de evidencias y documentos vinculados a Hallazgos, Acciones, Planes y Auditorías

- Clave primaria: `id`
- Filas: 48
- Referencia a: `accion_correctiva_id` → `control_interno.accion_correctiva` (0..1 → 0..1); `auditoria_id` → `control_interno.auditoria` (0..* → 0..1); `hallazgo_id` → `control_interno.hallazgo` (0..* → 0..1); `plan_mejoramiento_id` → `control_interno.plan_mejoramiento` (0..1 → 0..1); `version_anterior_id` → `control_interno.evidencia_documento` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla evidencia_documento. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(50)` | no | Código único generado automáticamente: EVD-YYYY-NNNN | única |
| 3 | `nombre` | `character varying(255)` | no | Nombre del documento de evidencia. |  |
| 4 | `descripcion` | `text` | sí | Descripción de la evidencia o documento. |  |
| 5 | `tipo_documento` | `control_interno.tipo_documento_evidencia` | no | Tipo de documento de evidencia. Valores permitidos: evidencia_hallazgo, evidencia_accion, evidencia_plan, documento_plan, certificado, acta, informe, otro. |  |
| 6 | `hallazgo_id` | `uuid` | sí | Referencia al registro de control_interno.hallazgo (id). | FK→control_interno.hallazgo.id |
| 7 | `accion_correctiva_id` | `uuid` | sí | Referencia al registro de control_interno.accion_correctiva (id). | FK→control_interno.accion_correctiva.id |
| 8 | `plan_mejoramiento_id` | `uuid` | sí | Referencia al registro de control_interno.plan_mejoramiento (id). | FK→control_interno.plan_mejoramiento.id |
| 9 | `auditoria_id` | `uuid` | sí | Referencia al registro de control_interno.auditoria (id). | FK→control_interno.auditoria.id |
| 10 | `ruta_archivo` | `character varying(500)` | no | Ruta del archivo físico de la evidencia. |  |
| 11 | `nombre_archivo_original` | `character varying(255)` | no | Nombre original del archivo al momento de subirlo. |  |
| 12 | `tipo_mime` | `character varying(100)` | no | Tipo MIME del archivo. |  |
| 13 | `tamanio_bytes` | `bigint` | no | Tamaño del archivo, en bytes. |  |
| 14 | `hash_archivo` | `character varying(255)` | sí | Hash SHA256 del archivo para verificar integridad |  |
| 15 | `version` | `integer` | sí | Número de versión del documento; por defecto 1. |  |
| 16 | `version_anterior_id` | `uuid` | sí | Referencia a la versión anterior para mantener historial | FK→control_interno.evidencia_documento.id |
| 17 | `es_version_actual` | `boolean` | sí | Indica si el registro corresponde a la versión vigente del documento. |  |
| 18 | `estado_validacion` | `control_interno.estado_validacion_evidencia` | sí | Estado de validación por auditor (US-032): pendiente, aceptado, rechazado, con_observaciones |  |
| 19 | `validado_por` | `character varying(255)` | sí | Usuario que realizó la validación. |  |
| 20 | `fecha_validacion` | `timestamp without time zone` | sí | Fecha y hora en que se validó la evidencia. |  |
| 21 | `observaciones_validacion` | `text` | sí | Observaciones registradas al validar la evidencia. |  |
| 22 | `subido_por` | `character varying(255)` | no | Nombre del usuario que cargó el documento. |  |
| 23 | `subido_por_id` | `bigint` | sí | Identificador de la persona que cargó el documento; referencia opcional a auth.personas. |  |
| 24 | `fecha_subida` | `timestamp without time zone` | sí | Fecha y hora en que se cargó la evidencia. |  |
| 25 | `ruta_servidor_g` | `character varying(500)` | sí | Ruta del documento en el servidor G: con el que se sincroniza. |  |
| 26 | `sincronizado_servidor_g` | `boolean` | sí | Indica si la evidencia está sincronizada con el servidor G. |  |
| 27 | `fecha_sincronizacion` | `timestamp without time zone` | sí | Fecha y hora de la sincronización de la evidencia con el servidor G. |  |
| 28 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 29 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## hallazgo

Hallazgos identificados en las auditorías

- Clave primaria: `id`
- Filas: 34
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla hallazgo. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(255)` | no | Código del hallazgo. Único en la tabla. | única |
| 3 | `categoria` | `character varying(50)` | no | Categoría del hallazgo: leve, moderado, grave, critico, borrador (por clasificar) o controversia (conservado para registros antiguos); borrador por defecto. |  |
| 4 | `estado` | `character varying(255)` | no | Estado del hallazgo. |  |
| 5 | `area` | `character varying(255)` | no | Área o dependencia en la que se identificó el hallazgo. |  |
| 6 | `auditoria` | `character varying(255)` | no | Código de la auditoría en la que se identificó el hallazgo; se resuelve contra la auditoría y se sincroniza con auditoria_id. |  |
| 7 | `auditoria_id` | `uuid` | sí | Referencia al registro de control_interno.auditoria (id). | FK→control_interno.auditoria.id |
| 8 | `descripcion` | `text` | no | Descripción del hallazgo. |  |
| 9 | `criterio_incumplido` | `text` | no | Criterio (norma, política o estándar) que se incumple en el hallazgo. |  |
| 10 | `normativa_relacionada` | `jsonb` | no | Normas relacionadas con el hallazgo, en formato JSON (arreglo). |  |
| 11 | `evidencias` | `jsonb` | no | Evidencias del hallazgo, como arreglo JSON de objetos con nombre, tipo, fecha y URL opcional. Por defecto arreglo vacío. |  |
| 12 | `recomendaciones` | `jsonb` | no | Recomendaciones del auditor sobre el hallazgo, en formato JSON (arreglo). |  |
| 13 | `fecha_deteccion` | `date` | no | Fecha en que se detectó el hallazgo. |  |
| 14 | `fecha_notificacion` | `date` | sí | Fecha en que se notificó el hallazgo. |  |
| 15 | `responsable` | `character varying(255)` | sí | Responsable de atender el hallazgo. |  |
| 16 | `fecha_limite_correccion` | `date` | sí | Fecha límite para corregir el hallazgo. |  |
| 17 | `observaciones_controversia` | `text` | sí | Observaciones sobre la controversia presentada frente al hallazgo. |  |
| 18 | `titulo` | `character varying(500)` | sí | Título del hallazgo. |  |
| 19 | `gravedad` | `character varying(20)` | sí | Gravedad del hallazgo. Valores permitidos: Baja, Media, Alta, Crítica. |  |
| 20 | `fecha_compromiso` | `date` | sí | Fecha de compromiso para la atención del hallazgo. |  |
| 21 | `progreso_cumplimiento` | `integer` | sí | Porcentaje de cumplimiento de las acciones asociadas al hallazgo, de 0 a 100; 0 por defecto. |  |
| 22 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 23 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 24 | `argumentos_controversia` | `text` | sí | Argumentos técnicos y normativa del área auditada al presentar controversia |  |
| 25 | `documento_controversia_url` | `character varying(500)` | sí | URL o ID del documento adjunto de controversia (PDF, DOCX, JPG) |  |
| 26 | `documento_controversia_nombre` | `character varying(255)` | sí | Nombre original del archivo adjunto de controversia |  |
| 27 | `decision_auditor` | `character varying(50)` | sí | Decisión del auditor: ratificado, modificado, retirado |  |
| 28 | `fundamentacion_tecnica` | `text` | sí | Fundamentación técnica de la decisión del auditor (trazabilidad permanente) |  |
| 29 | `fecha_decision` | `timestamp without time zone` | sí | Fecha en que el auditor tomó la decisión sobre la controversia |  |
| 30 | `auditor_decision_id` | `bigint` | sí | ID del auditor que tomó la decisión sobre la controversia |  |
| 31 | `causa_raiz` | `text` | sí | Causa raíz del hallazgo identificada |  |
| 32 | `efecto` | `text` | sí | Consecuencia o efecto del hallazgo |  |
| 33 | `causa` | `text` | sí | Razón o causa del hallazgo identificado |  |
| 34 | `controversia_turno` | `character varying(50)` | sí | Turno de respuesta en la controversia del hallazgo. Valores previstos: auditor, auditado. |  |

## historial_auditoria

Historial completo de cambios y eventos de una auditoría. Trazabilidad completa de todas las acciones. El campo cambios almacena un array JSONB con formato: [{"campo": "Progreso", "valorAnterior": "10%", "valorNuevo": "15%"}]

- Clave primaria: `id`
- Filas: 480
- Referencia a: `auditoria_id` → `control_interno.auditoria` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla historial_auditoria. Se genera automáticamente. | PK |
| 2 | `auditoria_id` | `uuid` | no | Referencia al registro de control_interno.auditoria (id). | FK→control_interno.auditoria.id |
| 3 | `tipo_evento` | `character varying(50)` | no | Tipo de evento registrado en el historial de la auditoría. Valores permitidos: creacion, actualizacion, cambio_estado, asignacion, aprobacion, ampliacion_plazo, documento, hallazgo, nota, archivo, finalizacion, eliminacion. |  |
| 4 | `fecha` | `date` | no | Fecha del evento. |  |
| 5 | `hora` | `time without time zone` | no | Hora del evento. |  |
| 6 | `accion` | `character varying(255)` | no | Texto corto que describe la acción registrada en el historial de la auditoría (por ejemplo, «Auditoría creada», «Cambio de estado», «Evidencia cargada»); lo fija el sistema o la función fn_registrar_cambio_estado_auditoria («Cambio de estado automático»). La clasificación cerrada está en tipo_evento. |  |
| 7 | `descripcion` | `text` | sí | Descripción del cambio o evento registrado en la auditoría. |  |
| 8 | `observaciones` | `text` | sí | Observaciones sobre el cambio o evento. |  |
| 9 | `documento_adjunto` | `character varying(500)` | sí | Documento adjunto al evento del historial de la auditoría. |  |
| 10 | `ip_address` | `character varying(45)` | sí | Dirección IP desde la que se originó el evento. | Identificador en línea (IP) |
| 11 | `user_agent` | `text` | sí | Agente de usuario (navegador) desde el que se realizó la acción. |  |
| 12 | `cambios` | `jsonb` | sí | Array JSONB de cambios realizados. Formato: [{"campo": string, "valorAnterior": string, "valorNuevo": string}]. Ejemplo: [{"campo": "Progreso", "valorAnterior": "10%", "valorNuevo": "15%"}] |  |
| 13 | `estado_anterior` | `character varying(50)` | sí | Estado de la auditoría antes del cambio; si es nulo se muestra Planeación, el estado inicial. |  |
| 14 | `estado_nuevo` | `character varying(50)` | sí | Estado de la auditoría después del cambio. |  |
| 15 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 16 | `usuario_id` | `uuid` | sí | Identificador de la persona (auth.personas.id_person) que realizó la acción; se obtiene a partir del auth."user".id_user del usuario autenticado. Puede ser nulo. |  |
| 17 | `nombre_usuario` | `character varying(255)` | sí | Nombre completo del usuario que realizó la acción (desnormalizado para auditoría) |  |
| 18 | `user_email` | `character varying(255)` | sí | Email del usuario que realizó la acción (desnormalizado para auditoría) | Contacto |

## historial_generacion_informe

Auditoría completa de generación y aprobación de informes

- Clave primaria: `id`
- Filas: 0
- Referencia a: `entrega_id` → `control_interno.entrega_informe_ley` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla historial_generacion_informe. Se genera automáticamente. | PK |
| 2 | `entrega_id` | `uuid` | no | Referencia al registro de control_interno.entrega_informe_ley (id). | FK→control_interno.entrega_informe_ley.id |
| 3 | `accion` | `character varying(100)` | no | Acción registrada en el historial de generación y aprobación del informe. Valores esperados: generado, actualizado, enviado_aprobacion, aprobado, rechazado. |  |
| 4 | `usuario_id` | `character varying(255)` | sí | Identificador del usuario que realizó la acción sobre la entrega del informe. |  |
| 5 | `usuario_nombre` | `character varying(255)` | sí | Nombre del usuario que realizó la acción sobre el informe. |  |
| 6 | `observaciones` | `text` | sí | Observaciones sobre la generación o aprobación del informe. |  |
| 7 | `datos_anteriores` | `jsonb` | sí | Datos del informe antes de la acción, en formato JSON. |  |
| 8 | `datos_nuevos` | `jsonb` | sí | Datos del informe después de la acción, en formato JSON. |  |
| 9 | `ip_origen` | `character varying(50)` | sí | Dirección IP desde la que se realizó la acción. | Identificador en línea (IP) |
| 10 | `user_agent` | `text` | sí | Agente de usuario (navegador) desde el que se realizó la acción. |  |
| 11 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |

## historial_plan_anual

Historial de cambios y auditoría del Plan Anual 5 Roles. Registra todas las operaciones CRUD para trazabilidad y compliance.

- Clave primaria: `id`
- Filas: 29731
- Referencia a: `plan_id` → `control_interno.plan_anual_5_roles` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla historial_plan_anual. Se genera automáticamente. | PK |
| 2 | `plan_id` | `uuid` | no | Referencia al registro de control_interno.plan_anual_5_roles (id). | FK→control_interno.plan_anual_5_roles.id |
| 3 | `tipo_evento` | `character varying(50)` | no | Tipo de evento: creacion, actualizacion, aprobacion, actividad_creada, actividad_actualizada, actividad_eliminada, cambio_estado |  |
| 4 | `fecha` | `date` | no | Fecha del evento registrado en el historial del plan anual. |  |
| 5 | `hora` | `time without time zone` | no | Hora del evento registrado en el historial del plan anual. |  |
| 6 | `usuario_id` | `uuid` | sí | FK a auth.personas(id_tercero) - Usuario que realizó la acción |  |
| 7 | `accion` | `character varying(255)` | no | Texto corto que describe la acción registrada en el historial del Plan Anual 5 Roles (por ejemplo, «Creación de Plan Anual», «Actividad creada», «Actualización responsable de rol»); lo fija el sistema o la función fn_registrar_cambio_estado_plan_anual («Cambio de estado automático»). La clasificación cerrada está en tipo_evento. |  |
| 8 | `descripcion` | `text` | sí | Descripción del cambio registrado en el plan anual. |  |
| 9 | `observaciones` | `text` | sí | Observaciones sobre el cambio en el plan anual. |  |
| 10 | `ip_address` | `character varying(45)` | sí | Dirección IP del usuario que realizó la acción | Identificador en línea (IP) |
| 11 | `user_agent` | `text` | sí | User agent del navegador del usuario |  |
| 12 | `cambios` | `jsonb` | sí | Array JSONB con formato [{campo: string, valorAnterior: string, valorNuevo: string}] |  |
| 13 | `estado_anterior` | `character varying(50)` | sí | Estado del plan anual antes del cambio. |  |
| 14 | `estado_nuevo` | `character varying(50)` | sí | Estado del plan anual después del cambio. |  |
| 15 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |

## informe_ley

Informes normativos requeridos por ley (RF012)

- Clave primaria: `id`
- Filas: 16

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla informe_ley. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(255)` | no | Código único del informe de ley, por ejemplo INF-CHIP o INF-SECOP. | única |
| 3 | `nombre` | `character varying(255)` | no | Nombre del informe de ley. |  |
| 4 | `descripcion` | `text` | no | Descripción del informe de ley. |  |
| 5 | `tipo` | `character varying(50)` | sí | Tipo de informe (interno, ley o normativo). |  |
| 6 | `periodicidad` | `character varying(50)` | no | Periodicidad de presentación del informe de ley. Valores permitidos en la base: mensual, trimestral, semestral, anual. |  |
| 7 | `fecha_vencimiento` | `date` | sí | Fecha de vencimiento del informe de ley. |  |
| 8 | `estado` | `character varying(50)` | sí | Estado del informe de ley (pendiente, en proceso, en revisión, aprobado, presentado o vencido). |  |
| 9 | `dias_restantes` | `integer` | sí | Días que faltan para el vencimiento del informe. |  |
| 10 | `alerta` | `character varying(50)` | sí | Color de alerta según la cercanía del vencimiento. Valores permitidos: verde, amarillo, naranja, rojo. |  |
| 11 | `area` | `character varying(255)` | no | Área a la que corresponde el informe de ley. Obligatoria. |  |
| 12 | `responsable` | `character varying(255)` | no | Nombre del responsable de elaborar el informe de ley; texto libre, obligatorio. |  |
| 13 | `normativa` | `text` | sí | Norma que establece la obligación de presentar el informe. |  |
| 14 | `acciones_sugeridas` | `jsonb` | sí | Acciones sugeridas para preparar el informe, en formato JSON. |  |
| 15 | `historial` | `jsonb` | sí | Historial del informe, en formato JSON. |  |
| 16 | `proximo_recordatorio` | `timestamp without time zone` | sí | Fecha y hora del próximo recordatorio programado del informe. |  |
| 17 | `recordatorios_enviados` | `integer` | sí | Número de recordatorios enviados del informe. |  |
| 18 | `formato_template` | `character varying(255)` | sí | Código de la plantilla del informe que se usa cuando url_plantilla está vacía. |  |
| 19 | `datos_integrados` | `jsonb` | sí | Datos integrados de otros módulos para generar el informe, en formato JSON. |  |
| 20 | `codigo_corto` | `character varying(50)` | sí | Código corto del informe de ley. Único en la tabla. | única |
| 21 | `categoria` | `character varying(100)` | sí | Categoría del informe de ley. Valores permitidos: financiero, administrativo, contractual, talento-humano, transparencia, control. |  |
| 22 | `dia_presentacion` | `integer` | sí | Día del mes o del periodo en que se presenta el informe, de 1 a 31. |  |
| 23 | `entidad_destino` | `character varying(500)` | sí | Entidad a la que se presenta el informe de ley. |  |
| 24 | `area_responsable` | `character varying(255)` | sí | Área responsable de elaborar y presentar el informe; si no se envía, toma el valor de area. |  |
| 25 | `tiene_plantilla` | `boolean` | sí | Indica si el informe tiene plantilla; por defecto falso. |  |
| 26 | `url_plantilla` | `character varying(500)` | sí | URL de la plantilla del informe. |  |
| 27 | `requiere_aprobacion` | `boolean` | sí | Indica si el informe requiere aprobación; por defecto verdadero. |  |
| 28 | `dias_anticipacion_alerta` | `integer` | sí | Días de anticipación con que se alerta el vencimiento del informe, de 1 a 90; 7 por defecto. |  |
| 29 | `activo` | `boolean` | sí | Indica si el informe de ley está activo. |  |
| 30 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 31 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## integraciones_esap

Configuración de integraciones externas

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla integraciones_esap. Se genera automáticamente. | PK |
| 2 | `nombre` | `character varying(255)` | no | Nombre de la integración externa. |  |
| 3 | `tipo` | `character varying(100)` | no | Tipo de integración (api, email, sftp, webhook u otro). |  |
| 4 | `configuracion` | `jsonb` | no | Parámetros de configuración de la integración externa, en formato JSON. |  |
| 5 | `activa` | `boolean` | sí | Indica si la integración está activa. |  |
| 6 | `ultima_sincronizacion` | `timestamp without time zone` | sí | Fecha y hora de la última sincronización ejecutada con la integración externa. |  |
| 7 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 8 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## item_lista_chequeo

Items individuales de una lista de chequeo

- Clave primaria: `id`
- Filas: 109
- Referencia a: `lista_chequeo_id` → `control_interno.lista_chequeo` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla item_lista_chequeo. Se genera automáticamente. | PK |
| 2 | `lista_chequeo_id` | `uuid` | no | Referencia al registro de control_interno.lista_chequeo (id). | FK→control_interno.lista_chequeo.id |
| 3 | `texto` | `text` | no | Texto del item de verificación |  |
| 4 | `categoria` | `character varying(100)` | no | Categoría del item (opcional) |  |
| 5 | `obligatorio` | `boolean` | no | Indica si el item es obligatorio |  |
| 6 | `orden` | `integer` | no | Orden de visualización del item |  |
| 7 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 9 | `completado` | `boolean` | sí | Indica si el item ha sido marcado como completado en el tablero Kanban |  |
| 10 | `fecha_completado` | `timestamp without time zone` | sí | Fecha y hora en que se marcó el item como completado |  |
| 11 | `completado_por` | `character varying(255)` | sí | Usuario que marcó el item como completado |  |
| 12 | `observaciones` | `text` | sí | Observaciones o notas adicionales del auditor sobre este item |  |
| 13 | `documento_biblioteca_id` | `character varying(255)` | sí | ID del documento en la biblioteca de plantillas asociado a este ítem |  |
| 14 | `documento_nombre` | `character varying(500)` | sí | Nombre del documento de la biblioteca asociado (snapshot) |  |

## lista_aplicada

Aplicaciones de listas de chequeo en auditorías

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla lista_aplicada. Se genera automáticamente. | PK |
| 2 | `lista_chequeo_id` | `uuid` | no | Identificador de la lista de chequeo aplicada (control_interno.lista_chequeo). |  |
| 3 | `lista_chequeo_codigo` | `character varying(255)` | no | Código de la lista de chequeo aplicada. |  |
| 4 | `lista_chequeo_nombre` | `character varying(255)` | no | Nombre de la lista de chequeo aplicada. |  |
| 5 | `auditoria_id` | `character varying(255)` | no | Identificador de la auditoría en la que se aplicó la lista de chequeo. |  |
| 6 | `fecha_aplicacion` | `date` | no | Fecha en que se aplicó la lista de chequeo. |  |
| 7 | `aplicado_por` | `character varying(255)` | no | Usuario que aplicó la lista de chequeo. |  |
| 8 | `respuestas` | `jsonb` | no | Respuestas registradas a los ítems de la lista de chequeo, en formato JSON. |  |
| 9 | `resultado` | `jsonb` | no | Resultado consolidado de la aplicación de la lista de chequeo, en formato JSON. |  |
| 10 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 11 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## lista_chequeo

Listas de chequeo configurables para auditorías

- Clave primaria: `id`
- Filas: 71
- Referencia a: `tipo_auditoria_id` → `control_interno.tipo_auditoria` (0..* → 0..1)
- Relaciones implícitas: `etapa_kanban_id` ↝ `control_interno.etapa_kanban` (100.0 % con padre)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla lista_chequeo. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(255)` | no | Código único de la lista (ej: LC-ADM-001) | única |
| 3 | `nombre` | `character varying(255)` | no | Nombre descriptivo de la lista de chequeo |  |
| 4 | `descripcion` | `text` | sí | Descripción de la lista de chequeo |  |
| 5 | `categoria` | `character varying(100)` | sí | Categoría de la lista de chequeo (obligatoria) |  |
| 6 | `tipo` | `character varying(100)` | no | Tipo de lista de chequeo: planeacion, ejecucion o comunicacion |  |
| 7 | `tipo_auditoria_id` | `uuid` | sí | Tipo de auditoría asociado (opcional) | FK→control_interno.tipo_auditoria.id |
| 8 | `activa` | `boolean` | no | Indica si la lista está activa y disponible |  |
| 9 | `usos_programados` | `integer` | no | Contador de usos programados con esta lista |  |
| 10 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 11 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 12 | `deleted_at` | `timestamp without time zone` | sí | Fecha de eliminación (soft delete) |  |
| 13 | `auditoria_id` | `uuid` | sí | Identificador (UUID) de la auditoría (control_interno.auditoria.id) a la que se vincula la lista de chequeo. |  |
| 14 | `nombre_auditoria` | `character varying(500)` | sí | Nombre de la auditoría a la que se vincula la lista de chequeo; se registra al crear o vincular la lista. |  |
| 15 | `auditor_responsable` | `character varying(255)` | sí | Auditor responsable de aplicar la lista de chequeo. |  |
| 16 | `fecha_aplicacion` | `date` | sí | Fecha en que la lista de chequeo se vinculó a una auditoría; se asigna con la fecha del momento. |  |
| 17 | `fecha_diligenciamiento` | `date` | sí | Fecha en que se diligenció la lista de chequeo. |  |
| 18 | `items_completados` | `integer` | sí | Número de ítems diligenciados de la lista de chequeo. Por defecto 0. |  |
| 19 | `cumplimiento` | `integer` | sí | Porcentaje de cumplimiento de la lista de chequeo, de 0 a 100: ítems completados sobre el total de ítems, redondeado. Por defecto 0. |  |
| 20 | `no_cumplimientos` | `integer` | sí | Número de ítems evaluados como no cumplidos. Por defecto 0. |  |
| 21 | `no_aplica` | `integer` | sí | Número de ítems marcados como no aplica. Por defecto 0. |  |
| 22 | `hallazgos_generados` | `integer` | sí | Número de hallazgos generados a partir de la lista de chequeo. Por defecto 0. |  |
| 23 | `version` | `character varying(50)` | sí | Versión de la lista de chequeo, fijada por el usuario; 1.0 por defecto. |  |
| 24 | `estado` | `character varying(50)` | sí | Estado de la lista de chequeo: activa, inactiva u obsoleta; activa por defecto. |  |
| 25 | `aplicable_para` | `jsonb` | sí | Tipos de auditoría para los que aplica la lista de chequeo, como arreglo JSON de textos sin lista cerrada. Por defecto ["gestion", "cumplimiento"]. |  |
| 26 | `created_by` | `character varying(255)` | sí | Usuario que creó el registro. |  |
| 27 | `items_json` | `jsonb` | sí | Ítems de la lista de chequeo en formato JSON. |  |
| 28 | `proceso` | `character varying(255)` | sí | Proceso institucional al que corresponde la lista de chequeo. |  |
| 29 | `subproceso` | `character varying(255)` | sí | Subproceso institucional al que corresponde la lista de chequeo. |  |
| 30 | `categoria_esap` | `character varying(100)` | sí | Categoría de la lista de chequeo según la clasificación de la ESAP. |  |
| 31 | `normativa_aplicable` | `text` | sí | Normativa aplicable a la lista de chequeo. |  |
| 32 | `objetivo` | `text` | sí | Objetivo de la lista de chequeo. |  |
| 33 | `version_base` | `character varying(50)` | sí | Versión de la plantilla base de la que se generó la lista de chequeo. |  |
| 34 | `permite_no_aplica` | `boolean` | sí | Indica si la lista de chequeo admite la respuesta no aplica en sus ítems. Por defecto verdadero. |  |
| 35 | `requiere_evidencias` | `boolean` | sí | Indica si la lista de chequeo exige adjuntar evidencias. Por defecto verdadero. |  |
| 36 | `genera_hallazgos_automaticos` | `boolean` | sí | Indica si la lista de chequeo genera hallazgos de forma automática. Por defecto verdadero. |  |
| 37 | `fase_planeacion` | `boolean` | sí | Indica si la lista de chequeo se aplica en la fase de planeación de la auditoría. Por defecto falso. |  |
| 38 | `fase_ejecucion` | `boolean` | sí | Indica si la lista de chequeo se aplica en la fase de ejecución de la auditoría. Por defecto falso. |  |
| 39 | `fase_comunicacion` | `boolean` | sí | Indica si la lista de chequeo se aplica en la fase de comunicación de la auditoría. Por defecto falso. |  |
| 40 | `fase_seguimiento` | `boolean` | sí | Indica si la lista de chequeo se aplica en la fase de seguimiento de la auditoría. Por defecto falso. |  |
| 41 | `etapa_kanban_id` | `uuid` | sí | ID de la etapa en tabla etapa_kanban (FK lógica - estable aunque cambie el nombre) | ↝control_interno.etapa_kanban.id |
| 42 | `etapa_kanban_nombre` | `character varying(255)` | sí | Nombre de la etapa al momento de guardar (snapshot para mostrar aunque cambie la configuración) |  |
| 43 | `plan_anual_vigencia` | `integer` | sí | Año de vigencia del plan anual |  |
| 44 | `plan_anual_id` | `uuid` | sí | UUID del plan anual 5 roles asociado |  |

## logs_auditoria_esap

Logs de auditoría de acciones del sistema

- Clave primaria: `id`
- Filas: 0
- Referencia a: `usuario_id` → `control_interno.usuarios_esap` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla logs_auditoria_esap. Se genera automáticamente. | PK |
| 2 | `usuario_id` | `uuid` | sí | Referencia al registro de control_interno.usuarios_esap (id). | FK→control_interno.usuarios_esap.id |
| 3 | `accion` | `character varying(255)` | no | Acción realizada por el usuario que se registra en el log. |  |
| 4 | `entidad` | `character varying(255)` | sí | Nombre de la entidad o tabla afectada por la acción. |  |
| 5 | `entidad_id` | `uuid` | sí | Identificador del registro afectado por la acción. |  |
| 6 | `detalles` | `jsonb` | sí | Detalles adicionales de la acción, en formato JSON. |  |
| 7 | `ip_address` | `character varying(45)` | sí | Dirección IP desde la que se realizó la acción (IPv4 o IPv6). | Identificador en línea (IP) |
| 8 | `user_agent` | `text` | sí | Agente de usuario (navegador) desde el que se realizó la acción. |  |
| 9 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |

## normatividad_aplicable

Normatividad aplicable a la auditoría (decretos, leyes, manuales, políticas)

- Clave primaria: `id`
- Filas: 0
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla normatividad_aplicable. Se genera automáticamente. | PK |
| 2 | `auditoria_id` | `uuid` | no | Referencia al registro de control_interno.auditoria (id). | FK→control_interno.auditoria.id |
| 3 | `normatividad` | `text` | no | Nombre de la norma o documento aplicable a la auditoría (por ejemplo, «Decreto 648 de 2017», «Manual de Contratación»). |  |
| 4 | `tipo` | `character varying(100)` | sí | Tipo de norma. Valores esperados: decreto, ley, manual, politica, otro. |  |
| 5 | `activo` | `boolean` | sí | Indica si la norma aplicable está activa. |  |
| 6 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 7 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## nota_auditoria

Notas y observaciones de las auditorías. Similar a un sistema de comentarios con categorización. Las notas marcadas como importantes (importante=true) aparecen destacadas en amarillo.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..1 → 1); `autor_id` → `auth.personas` (0..1 → 1); `editor_id` → `auth.personas` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla nota_auditoria. Se genera automáticamente. | PK |
| 2 | `auditoria_id` | `uuid` | no | Referencia al registro de control_interno.auditoria (id). | FK→control_interno.auditoria.id |
| 3 | `contenido` | `text` | no | Texto de la nota u observación de la auditoría. |  |
| 4 | `categoria` | `character varying(50)` | no | Categoría de la nota: General, Hallazgo, Seguimiento, Evidencia, Recomendación, Observación |  |
| 5 | `autor_id` | `uuid` | no | Referencia al registro de auth.personas (id_person). | FK→auth.personas.id_person |
| 6 | `fecha` | `date` | no | Fecha de registro de la nota de auditoría. |  |
| 7 | `hora` | `time without time zone` | no | Hora en que se registró la nota. |  |
| 8 | `importante` | `boolean` | sí | Si es true, la nota se marca como importante y aparece destacada con fondo amarillo en el frontend |  |
| 9 | `editada` | `boolean` | sí | Indica si la nota fue editada. |  |
| 10 | `fecha_edicion` | `timestamp without time zone` | sí | Fecha y hora de la última edición de la nota. |  |
| 11 | `editor_id` | `uuid` | sí | Referencia al registro de auth.personas (id_person). | FK→auth.personas.id_person |
| 12 | `activo` | `boolean` | sí | Indica si la nota está activa. |  |
| 13 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## notificacion

Sistema de notificaciones (RF014)

- Clave primaria: `id`
- Filas: 945

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla notificacion. Se genera automáticamente. | PK |
| 2 | `usuario_id` | `character varying(255)` | no | Identificador del usuario destinatario de la notificación, guardado como texto. |  |
| 3 | `tipo_notificacion` | `character varying(100)` | no | Tipo de la notificación. Los códigos de evento EVT-* se convierten en tipos como anuncio_auditoria, recordatorio_plazo, alerta_vencimiento, aprobacion_plan, rechazo_plan u otro, y el código original se guarda en metadata.eventoCode. |  |
| 4 | `titulo` | `character varying(255)` | no | Título de la notificación. |  |
| 5 | `mensaje` | `text` | no | Texto del mensaje de la notificación. |  |
| 6 | `estado` | `character varying(50)` | sí | Estado de la notificación (pendiente, enviada, leída o archivada). |  |
| 7 | `canal` | `character varying(50)` | sí | Canal por el que se envía la notificación. Valores permitidos: sistema, email, ambos. |  |
| 8 | `leida` | `boolean` | sí | Indica si el usuario leyó la notificación. |  |
| 9 | `fecha_lectura` | `timestamp without time zone` | sí | Fecha y hora en que se leyó la notificación. |  |
| 10 | `enviada_email` | `boolean` | sí | Indica si la notificación se envió por correo electrónico. |  |
| 11 | `fecha_envio_email` | `timestamp without time zone` | sí | Fecha y hora del envío de la notificación por correo electrónico. |  |
| 12 | `metadata` | `jsonb` | sí | Metadatos adicionales de la notificación en formato JSON. |  |
| 13 | `accion_url` | `character varying(500)` | sí | URL a la que dirige la notificación para realizar la acción asociada. |  |
| 14 | `prioridad` | `character varying(20)` | sí | Prioridad de la notificación. Valores permitidos: baja, normal, alta, critica. |  |
| 15 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 16 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## objetivo_auditoria

Objetivos específicos de cada auditoría. Cada auditoría puede tener múltiples objetivos.

- Clave primaria: `id`
- Filas: 39
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla objetivo_auditoria. Se genera automáticamente. | PK |
| 2 | `auditoria_id` | `uuid` | no | Referencia al registro de control_interno.auditoria (id). | FK→control_interno.auditoria.id |
| 3 | `descripcion` | `text` | no | Descripción del objetivo de la auditoría. |  |
| 4 | `orden` | `integer` | sí | Posición del objetivo en la lista de objetivos de la auditoría. |  |
| 5 | `activo` | `boolean` | sí | Indica si el objetivo de la auditoría está activo. |  |
| 6 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 7 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## parametro_sistema

Parámetros de configuración del sistema (RF020)

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla parametro_sistema. Se genera automáticamente. | PK |
| 2 | `clave` | `character varying(255)` | no | Clave única que identifica el parámetro de configuración. | única |
| 3 | `valor` | `text` | no | Valor del parámetro de configuración, almacenado como texto. |  |
| 4 | `descripcion` | `text` | sí | Descripción del parámetro del sistema. |  |
| 5 | `tipo` | `character varying(50)` | sí | Tipo de dato del valor del parámetro (boolean, json, number o string). |  |
| 6 | `categoria` | `character varying(255)` | sí | Categoría que agrupa los parámetros de configuración. |  |
| 7 | `editable` | `boolean` | sí | Indica si el parámetro puede modificarse desde la configuración. |  |
| 8 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## paso_workflow_informe

Pasos individuales del workflow de aprobación

- Clave primaria: `id`
- Filas: 0
- Referencia a: `workflow_id` → `control_interno.workflow_aprobacion_informe` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla paso_workflow_informe. Se genera automáticamente. | PK |
| 2 | `workflow_id` | `uuid` | no | Referencia al registro de control_interno.workflow_aprobacion_informe (id). | FK→control_interno.workflow_aprobacion_informe.id |
| 3 | `numero_paso` | `integer` | no | Número del paso dentro del workflow de aprobación del informe. |  |
| 4 | `nombre` | `character varying(100)` | no | Nombre interno del paso del workflow de aprobación del informe, por ejemplo elaboracion, revision, aprobacion o publicacion. |  |
| 5 | `nombre_display` | `character varying(255)` | no | Nombre del paso para mostrar en pantalla, por ejemplo Elaboración o Revisión Técnica. |  |
| 6 | `descripcion` | `text` | sí | Descripción del paso del flujo de aprobación. |  |
| 7 | `responsable` | `character varying(255)` | sí | Responsable de ejecutar el paso del workflow. |  |
| 8 | `rol_responsable` | `character varying(255)` | sí | Rol que debe ejecutar el paso del workflow del informe de ley: «Auditor» para la elaboración y «Jefe OCI» para la revisión y la aprobación. |  |
| 9 | `estado` | `character varying(50)` | sí | Estado del paso del flujo de aprobación (pendiente, en proceso, completado o rechazado). |  |
| 10 | `fecha_inicio` | `timestamp without time zone` | sí | Fecha y hora de inicio del paso. |  |
| 11 | `fecha_fin` | `timestamp without time zone` | sí | Fecha y hora de finalización del paso. |  |
| 12 | `observaciones` | `text` | sí | Observaciones sobre el paso del flujo de aprobación. |  |
| 13 | `accion` | `character varying(50)` | sí | Acción que corresponde al paso del workflow. Valores permitidos: elaborar, revisar, aprobar, publicar. |  |
| 14 | `es_obligatorio` | `boolean` | sí | Indica si el paso es obligatorio en el flujo de aprobación. |  |
| 15 | `orden` | `integer` | no | Posición del paso en el flujo de aprobación. |  |
| 16 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 17 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## plan_anual

Planes anuales de auditoría

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla plan_anual. Se genera automáticamente. | PK |
| 2 | `año` | `integer` | no | Año (vigencia) del plan anual de auditoría, entre 2020 y 2100. |  |
| 3 | `nombre` | `character varying(255)` | no | Nombre del plan anual de auditoría. |  |
| 4 | `estado` | `character varying(50)` | sí | Estado del plan anual (borrador, aprobado, en ejecución o cerrado). |  |
| 5 | `fecha_creacion` | `date` | no | Fecha y hora de creación del registro. |  |
| 6 | `fecha_aprobacion` | `date` | sí | Fecha en que se aprobó el plan anual. |  |
| 7 | `creado_por` | `character varying(255)` | no | Usuario que creó el registro. |  |
| 8 | `version` | `character varying(50)` | sí | Versión del plan anual. |  |
| 9 | `total_actividades` | `integer` | sí | Cantidad total de actividades del plan anual. |  |
| 10 | `actividades_completadas` | `integer` | sí | Cantidad de actividades del plan anual completadas. |  |
| 11 | `porcentaje_cumplimiento` | `integer` | sí | Porcentaje de cumplimiento del plan anual, entre 0 y 100. |  |
| 12 | `enfoques` | `jsonb` | sí | Enfoques de auditoría definidos para el plan anual, en formato JSON. |  |
| 13 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## plan_anual_5_roles

Planes anuales de auditoría organizados según los cinco roles de la oficina de control interno del Decreto 648. Un registro por plan y vigencia, con su responsable, periodo de ejecución, estado (borrador, en revisión, aprobado, en ejecución, completado), avance de actividades, comité y orden de aprobación y firma de activación; se relaciona con las auditorías y el historial del plan.

- Clave primaria: `id`
- Filas: 63

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla plan_anual_5_roles. Se genera automáticamente. | PK |
| 2 | `ano` | `integer` | no | Año (vigencia) del plan anual de auditoría; es único por plan, entre 2020 y 2100. | única |
| 3 | `fecha_creacion` | `date` | no | Fecha y hora de creación del registro. |  |
| 4 | `responsable` | `character varying(255)` | no | Nombre del responsable del plan anual; obligatorio. Se registra aparte de responsable_id (auth.personas.id_person). |  |
| 5 | `estado` | `character varying(50)` | no | Estado del plan anual: borrador, en-revision, aprobado, en-ejecucion, completado |  |
| 6 | `porcentaje_cumplimiento_general` | `integer` | sí | Porcentaje de cumplimiento general del plan anual: promedio redondeado del porcentaje de cumplimiento de sus roles (rol_plan_anual_5), calculado por el sistema. Por defecto, 0. |  |
| 7 | `total_actividades` | `integer` | sí | Cantidad total de actividades del plan anual. |  |
| 8 | `actividades_completadas` | `integer` | sí | Cantidad de actividades del plan anual completadas. |  |
| 9 | `actividades_en_progreso` | `integer` | sí | Cantidad de actividades del plan anual en progreso. |  |
| 10 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 11 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 12 | `fecha_inicio` | `date` | sí | Fecha de inicio del periodo de ejecución del plan anual |  |
| 13 | `fecha_fin` | `date` | sí | Fecha de finalización del periodo de ejecución del plan anual |  |
| 14 | `responsable_id` | `uuid` | sí | UUID del profesional OCIG responsable/líder del plan (FK a configuracion_profesionales_ocig) |  |
| 15 | `equipo_aprobacion` | `jsonb` | sí | Integrantes del comité que aprueba el plan anual, como arreglo JSON de objetos con identificador (id o auditorId), nombre (nombre o auditorNombre), correo, estado de la votación (PENDIENTE por defecto, OBSERVADA, entre otros) y observación. Por defecto arreglo vacío. |  |
| 16 | `orden_aprobacion` | `character varying(20)` | sí | Orden en que el comité aprueba el plan anual: secuencial (vota el primer integrante pendiente) o paralelo (votan todos los pendientes). Valor por defecto: secuencial. |  |
| 17 | `firma_activacion` | `jsonb` | sí | Datos de la firma con la que se activa el plan anual, en formato JSON: firmante, fecha de firma, IP, hash y agente de usuario. Nula por defecto. |  |

## plan_anual_wizard_borrador

Borradores del asistente de creación del plan anual de auditoría. Un registro por usuario, con el estado del asistente guardado en formato JSON.

- Clave primaria: `id`
- Filas: 2

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla plan_anual_wizard_borrador. Se genera automáticamente. | PK |
| 2 | `usuario_id` | `character varying(255)` | no | Identificador del usuario dueño del borrador; cada usuario tiene un solo borrador. | única |
| 3 | `payload` | `jsonb` | no | Estado del asistente de creación del plan anual guardado como borrador, en formato JSON, con las marcas savedAt y timestamp. Hay un borrador por usuario. |  |
| 4 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 5 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## plan_individual

Planes individuales de auditoría

- Clave primaria: `id`
- Filas: 0
- Referencia a: `auditoria_id` → `control_interno.auditoria_programada` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla plan_individual. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(255)` | no | Código del plan individual de auditoría. Único en la tabla. | única |
| 3 | `auditoria_id` | `uuid` | no | Referencia al registro de control_interno.auditoria_programada (id). | FK→control_interno.auditoria_programada.id |
| 4 | `auditoria_codigo` | `character varying(255)` | no | Código de la auditoría a la que corresponde el plan individual; se copia de auditoria_programada.codigo al crear el plan y no se actualiza después. |  |
| 5 | `nombre` | `character varying(255)` | no | Nombre del plan individual de auditoría. |  |
| 6 | `alcance` | `text` | no | Alcance de la auditoría descrito en el plan individual. |  |
| 7 | `objetivo` | `text` | no | Objetivo de la auditoría descrito en el plan individual. |  |
| 8 | `proceso_auditar` | `character varying(255)` | no | Proceso de la entidad que se audita; obligatorio. |  |
| 9 | `riesgos` | `jsonb` | no | Riesgos identificados para la auditoría, como arreglo JSON de objetos con descripción, probabilidad, impacto, nivel (alto, medio o bajo) y controles. |  |
| 10 | `criterios_auditoria` | `jsonb` | no | Criterios de auditoría aplicables, como arreglo JSON de textos. |  |
| 11 | `normativa_aplicable` | `jsonb` | no | Normas aplicables a la auditoría, como arreglo JSON de objetos con tipo, número, nombre y artículo opcional. |  |
| 12 | `equipo_auditor` | `jsonb` | no | Equipo auditor asignado a la auditoría, como objeto JSON con el auditor líder, los auditores (nombre, cargo, correo y teléfono opcional) y, de forma opcional, los profesionales especializados (nombre, especialidad y correo). |  |
| 13 | `documentos` | `jsonb` | no | Documentos asociados al plan individual, como arreglo JSON de objetos con tipo, nombre, descripción opcional, fecha de generación opcional y estado (pendiente, generado o enviado). |  |
| 14 | `estado` | `character varying(50)` | no | Estado del plan individual (borrador, enviado o aceptado). |  |
| 15 | `fecha_creacion` | `date` | no | Fecha y hora de creación del registro. |  |
| 16 | `fecha_envio` | `date` | sí | Fecha en que se envió el plan individual. |  |
| 17 | `enviado_por` | `character varying(255)` | sí | Usuario que realizó el envío. |  |
| 18 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 19 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## plan_mejoramiento

Planes de mejoramiento derivados de hallazgos

- Clave primaria: `id`
- Filas: 14
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..1 → 0..1); `hallazgo_id` → `control_interno.hallazgo` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla plan_mejoramiento. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(255)` | no | Código del plan de mejoramiento. Único en la tabla. | única |
| 3 | `hallazgo_id` | `uuid` | sí | Referencia al registro de control_interno.hallazgo (id). | FK→control_interno.hallazgo.id |
| 4 | `hallazgo_codigo` | `character varying(255)` | sí | Código del hallazgo que origina el plan de mejoramiento. |  |
| 5 | `auditoria_id` | `uuid` | sí | Referencia al registro de control_interno.auditoria (id). | FK→control_interno.auditoria.id |
| 6 | `titulo` | `character varying(255)` | no | Título del plan de mejoramiento. |  |
| 7 | `descripcion` | `text` | sí | Descripción del plan de mejoramiento. |  |
| 8 | `objetivos` | `jsonb` | no | Objetivos del plan de mejoramiento, como arreglo JSON de textos. |  |
| 9 | `area_responsable` | `character varying(255)` | no | Área responsable de implementar el plan de mejoramiento. |  |
| 10 | `responsable_implementacion` | `character varying(255)` | no | Responsable de implementar el plan de mejoramiento, como texto (nombre, correo o usuario). Si no se informa, se usa el correo del responsable del área de la auditoría. |  |
| 11 | `estado` | `character varying(50)` | no | Estado del plan de mejoramiento (borrador, revisión, aprobado, rechazado, en ejecución, completado o vencido). |  |
| 12 | `fecha_creacion` | `date` | sí | Fecha y hora de creación del registro. |  |
| 13 | `fecha_aprobacion` | `date` | sí | Fecha en que se aprobó el plan de mejoramiento. |  |
| 14 | `fecha_inicio_ejecucion` | `date` | sí | Fecha en que inició la ejecución del plan de mejoramiento. |  |
| 15 | `fecha_limite` | `date` | no | Fecha límite del plan de mejoramiento. |  |
| 16 | `fecha_cierre` | `date` | sí | Fecha de cierre del plan de mejoramiento. |  |
| 17 | `recursos` | `jsonb` | sí | Recursos requeridos para ejecutar el plan de mejoramiento, en formato JSON. |  |
| 18 | `indicadores` | `jsonb` | sí | Indicadores para medir el avance o la efectividad del plan de mejoramiento, en formato JSON. |  |
| 19 | `avance_global` | `integer` | sí | Avance global del plan de mejoramiento; 0 por defecto. |  |
| 20 | `aprobado_por` | `character varying(255)` | sí | Usuario que realizó la aprobación. |  |
| 21 | `observaciones` | `text` | sí | Observaciones sobre el plan de mejoramiento. |  |
| 22 | `observaciones_aprobacion` | `text` | sí | Observaciones registradas al aprobar el plan de mejoramiento. |  |
| 23 | `motivo_rechazo` | `text` | sí | Motivo del rechazo. |  |
| 24 | `seguimientos` | `jsonb` | sí | Seguimientos realizados al plan de mejoramiento, en formato JSON. |  |
| 25 | `codigo_auditoria` | `character varying(255)` | sí | Código de la auditoría de la que proviene el plan de mejoramiento. |  |
| 26 | `porcentaje_efectividad` | `integer` | sí | Porcentaje de efectividad del plan de mejoramiento, de 0 a 100; 0 por defecto. |  |
| 27 | `seguimientos_realizados` | `integer` | sí | Cantidad de seguimientos realizados al plan de mejoramiento. |  |
| 28 | `seguimientos_totales` | `integer` | sí | Cantidad total de seguimientos programados para el plan de mejoramiento. Valor por defecto: 4. |  |
| 29 | `proximo_seguimiento` | `date` | sí | Fecha programada para el próximo seguimiento del plan de mejoramiento. |  |
| 30 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 31 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## plantilla_email

Plantillas de correo electrónico (RF020)

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla plantilla_email. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(255)` | no | Código de la plantilla de correo electrónico. Único en la tabla. | única |
| 3 | `nombre` | `character varying(255)` | no | Nombre de la plantilla de correo electrónico. |  |
| 4 | `asunto` | `character varying(500)` | no | Asunto del correo electrónico de la plantilla. |  |
| 5 | `cuerpo` | `text` | no | Cuerpo del correo electrónico de la plantilla. |  |
| 6 | `variables_disponibles` | `jsonb` | sí | Variables que se pueden usar en el asunto y el cuerpo de la plantilla de correo, en formato JSON. |  |
| 7 | `activa` | `boolean` | sí | Indica si la plantilla de correo electrónico está activa. |  |
| 8 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## plantilla_informe_ley

Plantillas para generación automática de informes de ley

- Clave primaria: `id`
- Filas: 16

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla plantilla_informe_ley. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(255)` | no | Código de la plantilla de informe de ley. Único en la tabla. | única |
| 3 | `nombre` | `character varying(255)` | no | Nombre de la plantilla de informe de ley. |  |
| 4 | `descripcion` | `text` | sí | Descripción de la plantilla de informe de ley. |  |
| 5 | `tipo_formato` | `character varying(50)` | no | Formato del archivo de la plantilla del informe de ley. Valores permitidos: Word, Excel, PDF, HTML. |  |
| 6 | `ruta_plantilla` | `character varying(500)` | no | Ruta relativa del archivo de la plantilla del informe de ley (Handlebars, .hbs) dentro de la carpeta templates del módulo de informes de ley. |  |
| 7 | `variables_disponibles` | `jsonb` | sí | Variables disponibles en la plantilla. Las marcadas como requeridas deben estar presentes. |  |
| 8 | `estructura_datos` | `jsonb` | sí | Estructura esperada de datos. Campos con "requerido": false son opcionales. |  |
| 9 | `activa` | `boolean` | sí | Indica si la plantilla de informe de ley está activa. |  |
| 10 | `version` | `character varying(50)` | sí | Versión de la plantilla de informe de ley. |  |
| 11 | `creado_por` | `character varying(255)` | sí | Usuario que creó el registro. |  |
| 12 | `actualizado_por` | `character varying(255)` | sí | Usuario que realizó la última actualización del registro. |  |
| 13 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## plantilla_reporte

Plantillas para generación de reportes

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla plantilla_reporte. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(255)` | no | Código de la plantilla de reporte. Único en la tabla. | única |
| 3 | `nombre` | `character varying(255)` | no | Nombre de la plantilla de reporte. |  |
| 4 | `tipo` | `character varying(100)` | no | Tipo de plantilla de reporte. |  |
| 5 | `descripcion` | `text` | sí | Descripción de la plantilla de reporte. |  |
| 6 | `formato` | `character varying(50)` | no | Formato del reporte generado. Valores permitidos: PDF, Excel, Word, PowerPoint. |  |
| 7 | `ruta_template` | `character varying(500)` | sí | Ruta del archivo de la plantilla del reporte. |  |
| 8 | `variables_disponibles` | `jsonb` | sí | Variables que se pueden usar en la plantilla del reporte, en formato JSON. |  |
| 9 | `activa` | `boolean` | sí | Indica si la plantilla de reporte está activa. |  |
| 10 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 11 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## plantillas_documentos_esap

Plantillas de documentos personalizadas

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla plantillas_documentos_esap. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(255)` | no | Código de la plantilla de documento. Único en la tabla. | única |
| 3 | `nombre` | `character varying(255)` | no | Nombre de la plantilla de documento. |  |
| 4 | `descripcion` | `text` | sí | Descripción de la plantilla de documento. |  |
| 5 | `tipo_documento` | `character varying(100)` | no | Tipo de documento que genera la plantilla. |  |
| 6 | `contenido` | `text` | no | Contenido de la plantilla del documento. |  |
| 7 | `variables_disponibles` | `jsonb` | sí | Variables que se pueden usar en la plantilla del documento, en formato JSON. |  |
| 8 | `activa` | `boolean` | sí | Indica si la plantilla de documento está activa. |  |
| 9 | `version` | `integer` | sí | Número de versión de la plantilla de documento. |  |
| 10 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 11 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## preferencia_notificacion

Preferencias de notificación por usuario (RF014)

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla preferencia_notificacion. Se genera automáticamente. | PK |
| 2 | `usuario_id` | `character varying(255)` | no | Identificador del usuario al que pertenecen las preferencias; cada usuario tiene un solo registro. | única |
| 3 | `notificaciones_email` | `boolean` | sí | Indica si el usuario recibe notificaciones por correo electrónico. |  |
| 4 | `notificaciones_sistema` | `boolean` | sí | Indica si el usuario recibe notificaciones en el sistema. |  |
| 5 | `tipos_notificacion` | `jsonb` | sí | Configuración por tipo de notificación, como objeto JSON cuya clave es el código del evento y cuyo valor indica los canales email y sistema y si está activo. En el registro de configuración global (usuario_id GLOBAL_CONFIG) cada evento lleva además la condición de disparo y los roles destinatarios. |  |
| 6 | `frecuencia_recordatorios` | `character varying(50)` | sí | Número de días de anticipación de los recordatorios al usuario, guardado como texto. Valor por defecto: 7. |  |
| 7 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 8 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 9 | `horario_preferido` | `character varying(50)` | sí | Horario preferido del usuario para recibir notificaciones |  |

## proceso_auditable

Procesos auditables del universo de auditorías

- Clave primaria: `id`
- Filas: 36
- Referencia a: `tipo_proceso_id` → `control_interno.tipo_proceso` (1..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla proceso_auditable. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(255)` | no | Código del proceso auditable. Único en la tabla. | única |
| 3 | `nombre` | `character varying(255)` | no | Nombre del proceso auditable. |  |
| 4 | `descripcion` | `text` | no | Descripción del proceso auditable. |  |
| 5 | `tipo` | `character varying(50)` | no | Tipo de proceso auditable. |  |
| 6 | `macroproceso` | `character varying(255)` | sí | Macroproceso al que pertenece el proceso auditable. |  |
| 7 | `responsable` | `character varying(255)` | no | Responsable del proceso auditable, en texto libre; si no se informa se guarda «Sin asignar». |  |
| 8 | `dependencia` | `character varying(255)` | no | Dependencia de la ESAP a cargo del proceso auditable. |  |
| 9 | `territorial` | `character varying(255)` | sí | Dirección territorial a la que corresponde el proceso auditable, en texto libre y opcional; se usa como filtro del universo de auditorías. |  |
| 10 | `evaluacion_riesgo` | `jsonb` | no | Evaluación de riesgo del proceso auditable, como objeto JSON con probabilidad, impacto y nivel de control (1 a 3), riesgo inherente (probabilidad × impacto), riesgo residual (inherente ÷ nivel de control), nivel de riesgo (bajo, medio, alto) y campos opcionales de controles, factores de riesgo, distribución de riesgos DAFP, decisión de rotación e inclusión en el plan anual y puntaje C+E-M. Los valores derivados se calculan al crear o actualizar el proceso. |  |
| 11 | `frecuencia_auditoria` | `character varying(255)` | no | Frecuencia con que debe auditarse el proceso, en texto: anual (valor por defecto), bienal, trienal, cuatrienal o «Cada N años». Se usa para calcular la fecha de la próxima auditoría a partir de la última. |  |
| 12 | `ultima_auditoria` | `date` | sí | Fecha de la última auditoría realizada al proceso. |  |
| 13 | `proxima_auditoria` | `date` | sí | Fecha programada para la próxima auditoría del proceso. |  |
| 14 | `prioridad` | `integer` | no | Prioridad del proceso auditable, número entero de 1 a 4 calculado como 5 menos los años de priorización: nivel de riesgo alto = 4, medio = 3, bajo = 2, otro = 1. Puede fijarse directamente al actualizar, y entonces se recalculan los años de priorización. |  |
| 15 | `priorizacion_anos` | `integer` | no | Periodicidad de auditoría del proceso, en años (1 a 4), según su nivel de riesgo. |  |
| 16 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 17 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 18 | `resultado_ultima_auditoria` | `character varying(255)` | sí | Resultado de la última auditoría realizada (Adecuado, Con observaciones, etc.) |  |
| 19 | `activo` | `boolean` | sí | Indica si el proceso auditable está activo. |  |
| 20 | `unidades_auditables` | `jsonb` | sí | Unidades auditables que componen el proceso, como arreglo JSON de textos. |  |
| 21 | `tipo_proceso_id` | `uuid` | sí | Relación al catálogo control_interno.tipo_proceso | FK→control_interno.tipo_proceso.id |
| 22 | `es_especial` | `boolean` | no | Proceso Especial (EFDS-1923): va directo a Programación sin pasar por Universo Auditable. El subtipo lo determina tipo_proceso_id. |  |

## programa_anual_ajuste

Ajustes del Programa Anual (EFDS-1919): borrador de la siguiente versión; la versión que se genera lo cierra.

- Clave primaria: `id`
- Filas: 3

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla programa_anual_ajuste. Se genera automáticamente. | PK |
| 2 | `vigencia` | `integer` | no | Vigencia (año) del programa anual que se ajusta. |  |
| 3 | `iniciado_por` | `character varying(255)` | no | Usuario que realizó el inicio. |  |
| 4 | `iniciado_por_id` | `character varying(64)` | sí | Identificador del usuario que inició el ajuste del Programa Anual (EFDS-1919): el id_user de auth."user" tomado del token de sesión; queda vacío si lo inicia el sistema. |  |
| 5 | `iniciado_at` | `timestamp with time zone` | no | Fecha y hora del inicio. |  |
| 6 | `cerrado_at` | `timestamp with time zone` | sí | Fecha y hora del cierre. |  |
| 7 | `version_resultante` | `integer` | sí | Número de la versión del Programa Anual con la que se cerró el ajuste; vacío si el ajuste se cerró sin cambios (EFDS-1919). |  |

## registro_seguimiento

Registros de seguimiento de las acciones de mejora en cada seguimiento trimestral. Un registro por acción evaluada en un seguimiento (control_interno.seguimiento_trimestral), con las acciones programadas e implementadas, los controles, si el hallazgo se repite y los puntajes de cumplimiento y efectividad.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `accion_id` → `control_interno.accion_correctiva` (0..1 → 1); `seguimiento_id` → `control_interno.seguimiento_trimestral` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla registro_seguimiento. Se genera automáticamente. | PK |
| 2 | `accion_id` | `uuid` | no | Referencia al registro de control_interno.accion_correctiva (id). | FK→control_interno.accion_correctiva.id |
| 3 | `seguimiento_id` | `uuid` | no | Referencia al registro de control_interno.seguimiento_trimestral (id). | FK→control_interno.seguimiento_trimestral.id |
| 4 | `accion_descripcion` | `text` | no | Descripción de la acción de mejora objeto del seguimiento. |  |
| 5 | `acciones_programadas` | `integer` | sí | Cantidad de acciones programadas, mínimo 1. |  |
| 6 | `acciones_implementadas` | `integer` | sí | Cantidad de acciones implementadas. |  |
| 7 | `puntaje_cumplimiento` | `integer` | sí | Puntaje de cumplimiento de la acción en el seguimiento, en escala de 0 a 2, calculado por el sistema: 2 si las acciones implementadas igualan o superan las programadas, 1 si hay al menos una implementada y 0 si no hay ninguna. Valor por defecto: 0. |  |
| 8 | `controles_implementados` | `character varying(20)` | no | Indica si se implementaron los controles. Valores permitidos: SI, NO, PARCIAL. |  |
| 9 | `hallazgo_se_repite` | `character varying(20)` | no | Indica si el hallazgo se repite. Valores permitidos: SI, NO. |  |
| 10 | `puntaje_efectividad` | `integer` | sí | Puntaje de efectividad de la acción en el seguimiento, en escala de 0 a 2, calculado por el sistema: 0 si el hallazgo se repite, 2 si los controles están implementados y el hallazgo no se repite, 1 en los demás casos. Valor por defecto: 0. |  |
| 11 | `observaciones` | `text` | sí | Observaciones sobre el seguimiento de la acción. |  |
| 12 | `evidencias` | `jsonb` | sí | Evidencias del registro de seguimiento, como arreglo JSON de textos. Por defecto, arreglo vacío. |  |
| 13 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## reunion_apertura

Información de la reunión de apertura de la auditoría

- Clave primaria: `id`
- Filas: 15
- Referencia a: `documento_biblioteca_id` → `control_interno.documento` (0..1 → 0..1); `auditoria_id` → `control_interno.auditoria` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla reunion_apertura. Se genera automáticamente. | PK |
| 2 | `auditoria_id` | `uuid` | no | Referencia al registro de control_interno.auditoria (id). | única FK→control_interno.auditoria.id |
| 3 | `fecha` | `timestamp without time zone` | no | Fecha y hora de la reunión de apertura de la auditoría. |  |
| 4 | `modalidad` | `character varying(50)` | no | Modalidad de la reunión de apertura. Valores permitidos: presencial, virtual, hibrida. |  |
| 5 | `lugar` | `character varying(255)` | sí | Lugar de la reunión de apertura cuando la modalidad es presencial. |  |
| 6 | `enlace_virtual` | `character varying(500)` | sí | Enlace de conexión a la reunión de apertura cuando la modalidad es virtual o híbrida. |  |
| 7 | `agenda` | `jsonb` | sí | Temas a tratar en la reunión de apertura, como arreglo JSON. |  |
| 8 | `participantes` | `jsonb` | sí | Participantes de la reunión de apertura con sus roles, como arreglo JSON. |  |
| 9 | `estado_acta` | `character varying(50)` | sí | Estado del acta de la reunión de apertura. Valores permitidos: pendiente, en_elaboracion, aprobada, firmada. |  |
| 10 | `acta_ruta` | `character varying(500)` | sí | Ruta del archivo del acta de la reunión de apertura. |  |
| 11 | `observaciones` | `text` | sí | Observaciones sobre la reunión de apertura. |  |
| 12 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 13 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 14 | `documento_biblioteca_id` | `uuid` | sí | Referencia al registro de control_interno.documento (id). | FK→control_interno.documento.id |
| 15 | `elaborado_por` | `character varying(255)` | sí | Persona que elaboró el acta de la reunión de apertura, en texto libre digitado en el formulario. |  |
| 16 | `revisado_por` | `character varying(255)` | sí | Usuario que realizó la revisión. |  |

## reunion_cierre

Información de la reunión de cierre de la auditoría

- Clave primaria: `id`
- Filas: 11
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..1 → 1); `documento_biblioteca_id` → `control_interno.documento` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla reunion_cierre. Se genera automáticamente. | PK |
| 2 | `auditoria_id` | `uuid` | no | Referencia al registro de control_interno.auditoria (id). | única FK→control_interno.auditoria.id |
| 3 | `fecha` | `timestamp without time zone` | no | Fecha y hora de la reunión de cierre de la auditoría. |  |
| 4 | `modalidad` | `character varying(50)` | no | Modalidad de la reunión de cierre. Valores permitidos: presencial, virtual, hibrida. |  |
| 5 | `lugar` | `character varying(255)` | sí | Lugar donde se realiza la reunión de cierre. |  |
| 6 | `enlace_virtual` | `character varying(500)` | sí | Enlace de conexión a la reunión de cierre virtual o híbrida. |  |
| 7 | `agenda` | `jsonb` | sí | Agenda de la reunión de cierre, como objeto JSON con la clave temasTratados, que guarda el texto de los temas tratados; vacía si no se informan temas. |  |
| 8 | `participantes` | `jsonb` | sí | Participantes de la reunión de cierre, como arreglo JSON de textos; cada participante de la lista separada por comas se guarda como un elemento. |  |
| 9 | `estado_acta` | `character varying(50)` | sí | Estado del acta de la reunión de cierre. Valores permitidos: pendiente, en_elaboracion, aprobada, firmada. |  |
| 10 | `acta_ruta` | `character varying(500)` | sí | Ruta del archivo del acta de la reunión de cierre. |  |
| 11 | `observaciones` | `text` | sí | Observaciones sobre la reunión de cierre. |  |
| 12 | `elaborado_por` | `character varying(255)` | sí | Persona que elaboró el acta de la reunión de cierre, en texto libre digitado en el formulario. |  |
| 13 | `revisado_por` | `character varying(255)` | sí | Usuario que realizó la revisión. |  |
| 14 | `documento_biblioteca_id` | `uuid` | sí | Referencia al registro de control_interno.documento (id). | FK→control_interno.documento.id |
| 15 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 16 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## rol_decreto_648

Roles del Decreto 648 configurable (RF020)

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla rol_decreto_648. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(255)` | no | Código del rol del Decreto 648. Único en la tabla. | única |
| 3 | `nombre` | `character varying(255)` | no | Nombre del rol del Decreto 648. |  |
| 4 | `descripcion` | `text` | sí | Descripción del rol del Decreto 648. |  |
| 5 | `orden` | `integer` | sí | Posición del rol en el listado. |  |
| 6 | `activo` | `boolean` | sí | Indica si el rol está activo. |  |
| 7 | `editable` | `boolean` | sí | Indica si el rol puede modificarse desde la configuración. |  |
| 8 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## rol_decreto_648_template

Plantillas de los cinco roles de la oficina de control interno según el Decreto 648. Un registro por rol, con su número, nombre, descripción, color y estado activo.

- Clave primaria: `id`
- Filas: 5

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla rol_decreto_648_template. Se genera automáticamente. | PK |
| 2 | `rol_numero` | `integer` | no | Número del rol de la oficina de control interno según el Decreto 648, de 1 a 5: 1 Liderazgo estratégico, 2 Enfoque hacia la prevención, 3 Evaluación de la gestión del riesgo, 4 Evaluación y seguimiento, 5 Relación con entes externos de control. | única |
| 3 | `nombre` | `character varying(255)` | no | Nombre de la plantilla de rol del Decreto 648. |  |
| 4 | `descripcion` | `text` | no | Descripción de la plantilla de rol del Decreto 648. |  |
| 5 | `color` | `character varying(7)` | no | Color hexadecimal con que se muestra el rol en la interfaz. Valor por defecto: #3B82F6. |  |
| 6 | `activo` | `boolean` | sí | Indica si la plantilla de rol está activa. |  |
| 7 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 8 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## rol_plan_anual

Roles y disponibilidad de auditores en el plan anual

- Clave primaria: `id`
- Filas: 0
- Referencia a: `plan_id` → `control_interno.plan_anual` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla rol_plan_anual. Se genera automáticamente. | PK |
| 2 | `plan_id` | `uuid` | no | Referencia al registro de control_interno.plan_anual (id). | FK→control_interno.plan_anual.id |
| 3 | `tipo` | `character varying(100)` | no | Tipo de rol en el plan anual (Auditor, Auditor Líder, Prof. Especializado, Prof. Universitario o Técnico). |  |
| 4 | `nombre` | `character varying(255)` | sí | Nombre de la persona asignada al rol. |  |
| 5 | `email` | `character varying(255)` | sí | Correo electrónico de la persona asignada al rol. | Contacto |
| 6 | `disponibilidad` | `character varying(50)` | sí | Disponibilidad del auditor en el plan anual. Valores permitidos: disponible, parcial, no-disponible. |  |
| 7 | `horas_totales` | `integer` | sí | Horas totales disponibles del auditor en el año. Valor por defecto: 1800. |  |
| 8 | `horas_asignadas` | `integer` | sí | Horas del auditor ya asignadas a auditorías. |  |
| 9 | `auditorias_asignadas` | `integer` | sí | Cantidad de auditorías asignadas al auditor. |  |
| 10 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 11 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## rol_plan_anual_5

Roles del plan anual (5 roles)

- Clave primaria: `id`
- Filas: 405

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla rol_plan_anual_5. Se genera automáticamente. | PK |
| 2 | `plan_id` | `uuid` | no | Identificador del plan anual al que pertenece el rol (control_interno.plan_anual_5_roles). |  |
| 3 | `rol_numero` | `integer` | no | Número del rol dentro del plan anual, de 1 a 5; único por plan. Las funciones de cumplimiento de auditorías usan el rol 4. |  |
| 4 | `nombre` | `character varying(255)` | no | Nombre del rol del plan anual. |  |
| 5 | `descripcion` | `text` | no | Descripción del rol del plan anual. |  |
| 6 | `color` | `character varying(7)` | no | Color hexadecimal con que se muestra el rol en la interfaz. Valor por defecto: #3B82F6. |  |
| 7 | `porcentaje_cumplimiento` | `integer` | sí | Porcentaje de cumplimiento del rol en el plan anual, entre 0 y 100. |  |
| 8 | `total_actividades` | `integer` | sí | Cantidad total de actividades del rol en el plan anual. |  |
| 9 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 10 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 11 | `responsable` | `character varying(255)` | sí | Nombre del responsable principal del rol en el plan anual |  |
| 12 | `responsable_id` | `uuid` | sí | UUID del profesional OCI (id_person) responsable del rol |  |
| 13 | `responsables` | `jsonb` | no | Detalle del responsable del rol [{id,nombre,cargo,email}] |  |
| 14 | `activo` | `boolean` | no | Indica si el rol del plan anual está activo. Usado para soft delete/reactivación. |  |

## seccion_lista_chequeo

Secciones organizadas de listas de chequeo

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla seccion_lista_chequeo. Se genera automáticamente. | PK |
| 2 | `lista_id` | `uuid` | no | Identificador de la lista de chequeo a la que pertenece la sección (control_interno.lista_chequeo). El DDL de referencia del repositorio declara la FK con borrado en cascada. |  |
| 3 | `orden` | `integer` | no | Posición de la sección en la lista de chequeo. |  |
| 4 | `nombre` | `character varying(255)` | no | Nombre de la sección de la lista de chequeo. |  |
| 5 | `descripcion` | `text` | sí | Descripción de la sección de la lista de chequeo. |  |
| 6 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 7 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## seguimiento_plan

Cortes de seguimiento periódico de los planes de mejoramiento (EM-PT-002 act. 5 y 7). Un registro por corte, trimestral (control interno) o semestral (ente externo), con su responsable, resumen, informe, conteo de acciones según su cumplimiento, alertas generadas y si lo generó el proceso automático.

- Clave primaria: `id`
- Filas: 7
- Referencia a: `plan_id` → `control_interno.plan_mejoramiento` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla seguimiento_plan. Se genera automáticamente. | PK |
| 2 | `plan_id` | `uuid` | no | Referencia al registro de control_interno.plan_mejoramiento (id). | FK→control_interno.plan_mejoramiento.id |
| 3 | `periodicidad` | `character varying(20)` | no | Periodicidad del corte de seguimiento del plan de mejoramiento: TRIMESTRAL (control interno) o SEMESTRAL (ente externo). Valor por defecto: TRIMESTRAL. |  |
| 4 | `tipo_control` | `character varying(20)` | no | Tipo de control del seguimiento. Valores: INTERNO, ENTE_EXTERNO; valor por defecto INTERNO. |  |
| 5 | `fecha_corte` | `timestamp without time zone` | no | Fecha de corte del seguimiento. |  |
| 6 | `responsable_id` | `character varying(255)` | no | Identificador (UUID) del responsable del seguimiento: jefe de la Oficina de Control Interno o equipo auditor. |  |
| 7 | `responsable_nombre` | `character varying(255)` | sí | Nombre del responsable del seguimiento. |  |
| 8 | `resumen` | `text` | sí | Resumen ejecutivo del seguimiento. |  |
| 9 | `informe_ref` | `character varying(500)` | sí | Referencia al informe de ley y seguimiento generado en el corte. |  |
| 10 | `total_acciones_evaluadas` | `integer` | sí | Número total de acciones del plan evaluadas en el corte. |  |
| 11 | `acciones_cumplen` | `integer` | sí | Número de acciones que cumplen en el corte (cumplimiento = 2). |  |
| 12 | `acciones_parcial` | `integer` | sí | Número de acciones con cumplimiento parcial en el corte (cumplimiento = 1). |  |
| 13 | `acciones_no_cumplen` | `integer` | sí | Número de acciones que no cumplen en el corte (cumplimiento = 0). |  |
| 14 | `alertas_generadas` | `integer` | sí | Número de alertas generadas en el corte. |  |
| 15 | `automatico` | `boolean` | sí | Indica si el seguimiento lo generó automáticamente el proceso programado (job): true = generado por el job. |  |
| 16 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |

## seguimiento_plan_mejoramiento

Seguimientos trimestrales de planes de mejoramiento

- Clave primaria: `id`
- Filas: 0
- Referencia a: `plan_id` → `control_interno.plan_mejoramiento` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla seguimiento_plan_mejoramiento. Se genera automáticamente. | PK |
| 2 | `plan_id` | `uuid` | no | Referencia al registro de control_interno.plan_mejoramiento (id). | FK→control_interno.plan_mejoramiento.id |
| 3 | `numero_seguimiento` | `integer` | no | Número consecutivo del seguimiento dentro del plan de mejoramiento; único por plan. |  |
| 4 | `fecha_seguimiento` | `date` | no | Fecha del seguimiento al plan de mejoramiento. |  |
| 5 | `realizado_por` | `character varying(255)` | no | Persona que realizó el seguimiento. |  |
| 6 | `observaciones` | `text` | sí | Observaciones sobre el seguimiento al plan de mejoramiento. |  |
| 7 | `cumplimiento` | `integer` | sí | Porcentaje de cumplimiento registrado en el seguimiento, de 0 a 100. Valor por defecto: 0. |  |
| 8 | `efectividad` | `integer` | sí | Porcentaje de efectividad registrado en el seguimiento, de 0 a 100. Valor por defecto: 0. |  |
| 9 | `acciones_implementadas` | `integer` | sí | Cantidad de acciones implementadas a la fecha del seguimiento. |  |
| 10 | `acciones_totales` | `integer` | sí | Cantidad total de acciones del plan de mejoramiento evaluadas en el seguimiento. |  |
| 11 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## seguimiento_trimestral

Seguimientos trimestrales de los planes de mejoramiento. Un registro por plan, trimestre y año, con las fechas del periodo y del seguimiento, los porcentajes de avance, cumplimiento y efectividad, las acciones revisadas y las observaciones; el detalle por acción se registra en control_interno.registro_seguimiento.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `plan_id` → `control_interno.plan_mejoramiento` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla seguimiento_trimestral. Se genera automáticamente. | PK |
| 2 | `plan_id` | `uuid` | no | Referencia al registro de control_interno.plan_mejoramiento (id). | FK→control_interno.plan_mejoramiento.id |
| 3 | `trimestre` | `integer` | no | Trimestre del seguimiento, de 1 a 4. |  |
| 4 | `año` | `integer` | no | Año del seguimiento, entre 2020 y 2100. |  |
| 5 | `fecha_inicio` | `date` | no | Fecha de inicio del trimestre de seguimiento. |  |
| 6 | `fecha_fin` | `date` | no | Fecha de finalización del trimestre de seguimiento. |  |
| 7 | `fecha_seguimiento` | `date` | sí | Fecha en que se realizó el seguimiento trimestral. |  |
| 8 | `avance_global` | `integer` | sí | Porcentaje de avance global en el trimestre, entre 0 y 100. |  |
| 9 | `porcentaje_cumplimiento` | `integer` | sí | Porcentaje de cumplimiento en el trimestre, entre 0 y 100. |  |
| 10 | `porcentaje_efectividad` | `integer` | sí | Porcentaje de efectividad en el trimestre, entre 0 y 100. |  |
| 11 | `acciones_revisadas` | `integer` | sí | Cantidad de acciones revisadas en el seguimiento trimestral. |  |
| 12 | `acciones_totales` | `integer` | sí | Cantidad total de acciones del plan en el seguimiento trimestral. |  |
| 13 | `observaciones_generales` | `text` | sí | Observaciones generales del seguimiento trimestral. |  |
| 14 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 15 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## sesiones_esap

Sesiones activas de usuarios

- Clave primaria: `id`
- Filas: 0
- Referencia a: `usuario_id` → `control_interno.usuarios_esap` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla sesiones_esap. Se genera automáticamente. | PK |
| 2 | `usuario_id` | `uuid` | no | Referencia al registro de control_interno.usuarios_esap (id). | FK→control_interno.usuarios_esap.id |
| 3 | `token` | `character varying(500)` | no | Token único de la sesión del usuario. | única Credencial de acceso |
| 4 | `ip_address` | `character varying(45)` | sí | Dirección IP desde la que se inició la sesión (IPv4 o IPv6). | Identificador en línea (IP) |
| 5 | `user_agent` | `text` | sí | Agente de usuario (navegador) de la sesión. |  |
| 6 | `fecha_inicio` | `timestamp without time zone` | sí | Fecha y hora de inicio de la sesión. |  |
| 7 | `fecha_expiracion` | `timestamp without time zone` | no | Fecha y hora en que expira la sesión. |  |
| 8 | `activa` | `boolean` | sí | Indica si la sesión está activa. |  |
| 9 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |

## tablero_kanban

Configuración de tableros Kanban para auditorías y planes de mejoramiento

- Clave primaria: `id`
- Filas: 2

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla tablero_kanban. Se genera automáticamente. | PK |
| 2 | `nombre` | `character varying(255)` | no | Nombre del tablero Kanban. |  |
| 3 | `descripcion` | `text` | sí | Descripción del tablero Kanban. |  |
| 4 | `tipo` | `character varying(50)` | no | Tipo de tablero: auditorias o planes_mejoramiento |  |
| 5 | `activo` | `boolean` | no | Indica si el tablero Kanban está activo. |  |
| 6 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 7 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 8 | `deleted_at` | `timestamp with time zone` | sí | Fecha y hora de la eliminación. |  |
| 9 | `configuracion_visual` | `jsonb` | sí | Configuración visual del tablero Kanban, como objeto JSON de banderas booleanas: mostrarContadores, mostrarTiempos, alertasSLA, alertasWIP, transicionesAutomaticas, compactarVista, mostrarAvatar y permitirDragDrop. |  |

## tareas_auditoria

Tareas personalizadas asignadas a auditorías

- Clave primaria: `id`
- Filas: 0
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla tareas_auditoria. Se genera automáticamente. | PK |
| 2 | `auditoria_id` | `uuid` | no | Referencia al registro de control_interno.auditoria (id). | FK→control_interno.auditoria.id |
| 3 | `titulo` | `character varying(255)` | no | Título de la tarea. |  |
| 4 | `descripcion` | `text` | sí | Descripción de la tarea de la auditoría. |  |
| 5 | `estado` | `control_interno.estado_tarea` | no | Estado de la tarea (Pendiente, En Progreso, Completada o Cancelada). |  |
| 6 | `prioridad` | `control_interno.prioridad_tarea` | no | Prioridad de la tarea. Valores permitidos: Baja, Media, Alta, Urgente. |  |
| 7 | `fase` | `control_interno.fase_tarea` | sí | Fase de la auditoría a la que corresponde la tarea. Valores permitidos: Planeación, Ejecución, Comunicación, Seguimiento. |  |
| 8 | `responsable_id` | `uuid` | no | Identificador (UUID) del usuario responsable de la tarea de auditoría. |  |
| 9 | `responsable_nombre` | `character varying(255)` | no | Nombre del usuario responsable de la tarea. |  |
| 10 | `fecha_vencimiento` | `timestamp without time zone` | sí | Fecha y hora de vencimiento de la tarea. |  |
| 11 | `fecha_completado` | `timestamp without time zone` | sí | Fecha y hora en que se completó la tarea. |  |
| 12 | `progreso` | `integer` | sí | Porcentaje de avance de la tarea de auditoría, de 0 a 100. Por defecto 0. |  |
| 13 | `notas` | `text` | sí | Notas registradas sobre la tarea de auditoría. |  |
| 14 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 15 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## tipo_auditoria

Tipos de auditoría configurables del sistema (Regular, Territorial, Especial)

- Clave primaria: `id`
- Filas: 5

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla tipo_auditoria. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(255)` | no | Código único del tipo (ej: AUD-REG, AUD-TERR) | única |
| 3 | `nombre` | `character varying(255)` | no | Nombre descriptivo del tipo de auditoría |  |
| 4 | `descripcion` | `text` | sí | Descripción detallada del tipo de auditoría |  |
| 5 | `alcance` | `text` | sí | Alcance general del tipo de auditoría |  |
| 6 | `duracion_promedio` | `integer` | no | Duración promedio en días |  |
| 7 | `equipo_promedio` | `integer` | no | Número promedio de personas en el equipo |  |
| 8 | `color` | `character varying(7)` | no | Color hexadecimal para representación visual |  |
| 9 | `activa` | `boolean` | no | Indica si el tipo está activo y disponible |  |
| 10 | `auditorias_programadas` | `integer` | no | Contador de auditorías programadas con este tipo |  |
| 11 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 13 | `deleted_at` | `timestamp without time zone` | sí | Fecha de eliminación (soft delete) |  |

## tipo_proceso

Catálogo parametrizable de tipos de procesos auditables

- Clave primaria: `id`
- Filas: 7

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla tipo_proceso. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(80)` | no | Código estable usado por frontend y procesos existentes | única |
| 3 | `nombre` | `character varying(120)` | no | Nombre visible del tipo de proceso |  |
| 4 | `color` | `character varying(120)` | no | Clases CSS del distintivo visual en frontend |  |
| 5 | `orden` | `integer` | no | Posición del tipo de proceso en el catálogo. |  |
| 6 | `activo` | `boolean` | no | Indica si el tipo de proceso está activo. |  |
| 7 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## usuarios_esap

Usuarios del sistema ESAP

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla usuarios_esap. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(255)` | no | Código del usuario. Único en la tabla. | única |
| 3 | `nombre_completo` | `character varying(255)` | no | Nombre completo del usuario. | Nombre de persona |
| 4 | `email` | `character varying(255)` | no | Correo electrónico del usuario. | única Contacto |
| 5 | `cargo` | `character varying(255)` | sí | Cargo del usuario en la ESAP. |  |
| 6 | `area` | `character varying(255)` | sí | Área o dependencia a la que pertenece el usuario. |  |
| 7 | `rol` | `character varying(100)` | sí | Rol del usuario en el sistema. |  |
| 8 | `activo` | `boolean` | sí | Indica si el usuario está activo. |  |
| 9 | `ultimo_acceso` | `timestamp without time zone` | sí | Fecha y hora del último acceso del usuario al sistema. |  |
| 10 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 11 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## v_auditor_disponibilidad

Vista que muestra auditores con sus especialidades, disponibilidad y conteo de auditorías en curso

- Clave primaria: no declarada
- Filas: —
- Vista que usa: `auth.personas`, `control_interno.auditor_perfil`, `control_interno.auditoria`, `control_interno.equipo_auditor`

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `persona_id` | `uuid` | sí | _Por documentar_ |  |
| 2 | `nombre` | `character varying(1000)` | sí | _Por documentar_ |  |
| 3 | `num_identificacion` | `character varying(30)` | sí | _Por documentar_ | Identificación |
| 4 | `tip_identificacion` | `character varying(6)` | sí | _Por documentar_ |  |
| 5 | `email` | `character varying(100)` | sí | _Por documentar_ | Contacto |
| 6 | `especialidad` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `cargo` | `character varying(100)` | sí | _Por documentar_ |  |
| 8 | `nivel_experiencia` | `character varying(50)` | sí | _Por documentar_ |  |
| 9 | `estado_disponibilidad` | `character varying(50)` | sí | _Por documentar_ |  |
| 10 | `auditorias_en_curso` | `bigint` | sí | _Por documentar_ |  |
| 11 | `auditorias_como_lider` | `bigint` | sí | _Por documentar_ |  |
| 12 | `auditorias_como_asignado` | `bigint` | sí | _Por documentar_ |  |
| 13 | `fecha_ultima_actividad` | `date` | sí | _Por documentar_ |  |
| 14 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 15 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 16 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 17 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## v_auditorias_finalizadas

Vista de auditorías finalizadas con información del documento de cierre

- Clave primaria: no declarada
- Filas: —
- Vista que usa: `control_interno.auditoria`

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | sí | _Por documentar_ |  |
| 2 | `codigo` | `character varying(255)` | sí | _Por documentar_ |  |
| 3 | `nombre` | `character varying(500)` | sí | _Por documentar_ |  |
| 4 | `tipo` | `character varying(50)` | sí | _Por documentar_ |  |
| 5 | `fecha_inicio` | `date` | sí | _Por documentar_ |  |
| 6 | `fecha_fin` | `date` | sí | _Por documentar_ |  |
| 7 | `fecha_finalizacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 8 | `finalizada_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 9 | `finalizada_por_id` | `bigint` | sí | _Por documentar_ |  |
| 10 | `documento_cierre_nombre` | `text` | sí | _Por documentar_ |  |
| 11 | `documento_cierre_url` | `text` | sí | _Por documentar_ |  |
| 12 | `documento_cierre_tipo` | `text` | sí | _Por documentar_ |  |
| 13 | `documento_cierre_tamano` | `integer` | sí | _Por documentar_ |  |
| 14 | `observaciones_cierre` | `text` | sí | _Por documentar_ |  |
| 15 | `progreso` | `integer` | sí | _Por documentar_ |  |
| 16 | `hallazgos` | `integer` | sí | _Por documentar_ |  |

## v_auditorias_kanban_completo

Vista completa de auditorías con toda la información necesaria para el módulo Kanban

- Clave primaria: no declarada
- Filas: —
- Vista que usa: `auth.personas`, `control_interno.auditor_perfil`, `control_interno.auditoria`, `control_interno.auditoria_especial_info`, `control_interno.auditoria_territorial_info`, `control_interno.reunion_apertura`

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | sí | _Por documentar_ |  |
| 2 | `codigo` | `character varying(255)` | sí | _Por documentar_ |  |
| 3 | `titulo` | `character varying(500)` | sí | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `estado` | `character varying(50)` | sí | _Por documentar_ |  |
| 6 | `tipo` | `character varying(50)` | sí | _Por documentar_ |  |
| 7 | `riesgo` | `character varying(20)` | sí | _Por documentar_ |  |
| 8 | `semaforo` | `character varying(20)` | sí | _Por documentar_ |  |
| 9 | `territorial` | `character varying(255)` | sí | _Por documentar_ |  |
| 10 | `prioridad` | `character varying(20)` | sí | _Por documentar_ |  |
| 11 | `area_objetivo` | `character varying(255)` | sí | _Por documentar_ |  |
| 12 | `proceso_auditado` | `character varying(500)` | sí | _Por documentar_ |  |
| 13 | `alcance` | `text` | sí | _Por documentar_ |  |
| 14 | `progreso` | `integer` | sí | _Por documentar_ |  |
| 15 | `total_hallazgos` | `integer` | sí | _Por documentar_ |  |
| 16 | `dias_restantes` | `integer` | sí | _Por documentar_ |  |
| 17 | `porcentaje_tiempo` | `integer` | sí | _Por documentar_ |  |
| 18 | `ultima_actuacion` | `text` | sí | _Por documentar_ |  |
| 19 | `calificacion_riesgo` | `character varying(255)` | sí | _Por documentar_ |  |
| 20 | `total_documentos` | `integer` | sí | _Por documentar_ |  |
| 21 | `total_informes` | `integer` | sí | _Por documentar_ |  |
| 22 | `total_tareas` | `integer` | sí | _Por documentar_ |  |
| 23 | `actividades_completas` | `boolean` | sí | _Por documentar_ |  |
| 24 | `actividades_pendientes` | `integer` | sí | _Por documentar_ |  |
| 25 | `responsable_area_nombre` | `character varying(255)` | sí | _Por documentar_ |  |
| 26 | `responsable_area_cargo` | `character varying(255)` | sí | _Por documentar_ |  |
| 27 | `responsable_area_email` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 28 | `supervisor_asignado_id` | `uuid` | sí | _Por documentar_ |  |
| 29 | `supervisor_asignado_nombre` | `character varying(1000)` | sí | _Por documentar_ |  |
| 30 | `supervisor_asignado_email` | `character varying(100)` | sí | _Por documentar_ | Contacto |
| 31 | `fecha_reunion_apertura` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 32 | `reunion_modalidad` | `character varying(50)` | sí | _Por documentar_ |  |
| 33 | `reunion_estado_acta` | `character varying(50)` | sí | _Por documentar_ |  |
| 34 | `auditor_lider_id` | `uuid` | sí | _Por documentar_ |  |
| 35 | `auditor_lider_nombre` | `character varying(1000)` | sí | _Por documentar_ |  |
| 36 | `auditor_lider_email` | `character varying(100)` | sí | _Por documentar_ | Contacto |
| 37 | `auditor_lider_especialidad` | `character varying(255)` | sí | _Por documentar_ |  |
| 38 | `auditor_lider_cargo` | `character varying(100)` | sí | _Por documentar_ |  |
| 39 | `auditor_asignado_id` | `uuid` | sí | _Por documentar_ |  |
| 40 | `auditor_asignado_nombre` | `character varying(1000)` | sí | _Por documentar_ |  |
| 41 | `auditor_asignado_email` | `character varying(100)` | sí | _Por documentar_ | Contacto |
| 42 | `auditor_asignado_especialidad` | `character varying(255)` | sí | _Por documentar_ |  |
| 43 | `auditor_asignado_cargo` | `character varying(100)` | sí | _Por documentar_ |  |
| 44 | `territorial_nombre` | `character varying(255)` | sí | _Por documentar_ |  |
| 45 | `territorial_ciudad` | `character varying(255)` | sí | _Por documentar_ |  |
| 46 | `territorial_departamento` | `character varying(255)` | sí | _Por documentar_ |  |
| 47 | `especial_tipo_motivo` | `character varying(100)` | sí | _Por documentar_ |  |
| 48 | `especial_solicitante` | `character varying(255)` | sí | _Por documentar_ |  |
| 49 | `especial_justificacion` | `text` | sí | _Por documentar_ |  |
| 50 | `fecha_inicio` | `date` | sí | _Por documentar_ |  |
| 51 | `fecha_fin` | `date` | sí | _Por documentar_ |  |
| 52 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 53 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## v_auditorias_por_estado

Vista de contadores de auditorías por estado para el dashboard del Kanban

- Clave primaria: no declarada
- Filas: —
- Vista que usa: `control_interno.auditoria`

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `estado` | `character varying(50)` | sí | _Por documentar_ |  |
| 2 | `total` | `bigint` | sí | _Por documentar_ |  |
| 3 | `verdes` | `bigint` | sí | _Por documentar_ |  |
| 4 | `amarillas` | `bigint` | sí | _Por documentar_ |  |
| 5 | `rojas` | `bigint` | sí | _Por documentar_ |  |
| 6 | `progreso_promedio` | `numeric` | sí | _Por documentar_ |  |
| 7 | `total_hallazgos` | `bigint` | sí | _Por documentar_ |  |

## v_estado_vinculacion_auditorias

Vista para verificar el estado de la vinculación de auditorías al Rol 4.  Muestra qué planes tienen actividad configurada y cuántas auditorías están vinculadas.

- Clave primaria: no declarada
- Filas: —
- Vista que usa: `control_interno.actividad_plan_anual_5`, `control_interno.auditoria`, `control_interno.plan_anual_5_roles`, `control_interno.rol_plan_anual_5`

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `plan_id` | `uuid` | sí | _Por documentar_ |  |
| 2 | `año` | `integer` | sí | _Por documentar_ |  |
| 3 | `actividad_id` | `uuid` | sí | _Por documentar_ |  |
| 4 | `actividad_nombre` | `character varying(500)` | sí | _Por documentar_ |  |
| 5 | `tipo_calculo` | `character varying(50)` | sí | _Por documentar_ |  |
| 6 | `total_auditorias_programadas` | `integer` | sí | _Por documentar_ |  |
| 7 | `total_auditorias_finalizadas` | `integer` | sí | _Por documentar_ |  |
| 8 | `porcentaje_avance` | `integer` | sí | _Por documentar_ |  |
| 9 | `auditorias_vinculadas_real` | `bigint` | sí | _Por documentar_ |  |
| 10 | `total_auditorias_año` | `bigint` | sí | _Por documentar_ |  |

## v_resumen_auditorias_por_año

_Por documentar._

- Clave primaria: no declarada
- Filas: —
- Vista que usa: `control_interno.auditoria`

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `año` | `integer` | sí | _Por documentar_ |  |
| 2 | `tipo` | `character varying(50)` | sí | _Por documentar_ |  |
| 3 | `estado_kanban` | `character varying(50)` | sí | _Por documentar_ |  |
| 4 | `total` | `bigint` | sí | _Por documentar_ |  |
| 5 | `finalizadas` | `bigint` | sí | _Por documentar_ |  |
| 6 | `en_proceso` | `bigint` | sí | _Por documentar_ |  |
| 7 | `pendientes` | `bigint` | sí | _Por documentar_ |  |

## version_lista_chequeo

Historial de versiones de listas de chequeo

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla version_lista_chequeo. Se genera automáticamente. | PK |
| 2 | `lista_id` | `uuid` | no | Identificador de la lista de chequeo versionada (control_interno.lista_chequeo). El DDL de referencia del repositorio declara la FK con borrado en cascada. |  |
| 3 | `version` | `character varying(50)` | no | Número de versión de la lista de chequeo. |  |
| 4 | `fecha` | `date` | no | Fecha de la versión de la lista de chequeo. |  |
| 5 | `usuario` | `character varying(255)` | no | Usuario que generó la versión de la lista de chequeo. |  |
| 6 | `cambios` | `text` | no | Descripción de los cambios incluidos en la versión. |  |
| 7 | `motivo_cambio` | `text` | no | Motivo del cambio. |  |
| 8 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |

## version_programa_anual

Versiones del Programa Anual de Auditoría por vigencia (EFDS-1919). Se generan al exportar si cambió lo que el documento imprime.

- Clave primaria: `id`
- Filas: 25

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla version_programa_anual. Se genera automáticamente. | PK |
| 2 | `vigencia` | `integer` | no | Vigencia (año) del programa anual. |  |
| 3 | `version` | `integer` | no | Número de versión del programa anual dentro de la vigencia. |  |
| 4 | `huella` | `character varying(64)` | no | Huella (hash) de los campos que imprime el documento del Programa Anual; si no cambia, no se genera una versión nueva (EFDS-1919). |  |
| 5 | `filas` | `jsonb` | no | Filas del Programa Anual tal como quedaron en esta versión, en formato JSON. |  |
| 6 | `cambios` | `jsonb` | no | Diferencias frente a la versión anterior, en formato JSON; vacío en la versión 1. |  |
| 7 | `generada_por` | `character varying(255)` | no | Usuario que realizó la generación. |  |
| 8 | `generada_por_id` | `character varying(64)` | sí | Identificador del usuario que generó la versión del Programa Anual (EFDS-1919): el id_user de auth."user" tomado del token de sesión; queda vacío si la genera el sistema. |  |
| 9 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 10 | `motivo` | `text` | sí | Motivo de la nueva versión del Programa Anual; hasta 1000 caracteres (EFDS-1919). |  |

## workflow_aprobacion_informe

Workflow de aprobación para informes de ley (US-033)

- Clave primaria: `id`
- Filas: 0
- Referencia a: `entrega_id` → `control_interno.entrega_informe_ley` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla workflow_aprobacion_informe. Se genera automáticamente. | PK |
| 2 | `entrega_id` | `uuid` | no | Referencia al registro de control_interno.entrega_informe_ley (id). | FK→control_interno.entrega_informe_ley.id |
| 3 | `paso_actual` | `integer` | sí | Número del paso en que se encuentra el workflow de aprobación. Valor por defecto: 1. |  |
| 4 | `estado_workflow` | `character varying(50)` | sí | Estado del workflow de aprobación del informe. Valores permitidos: en-elaboracion, en-revision, en-aprobacion, aprobado, rechazado, completado. |  |
| 5 | `completado` | `boolean` | sí | Indica si se completó el flujo de aprobación del informe. |  |
| 6 | `fecha_completado` | `timestamp without time zone` | sí | Fecha y hora en que se completó el flujo de aprobación. |  |
| 7 | `creado_por` | `character varying(255)` | sí | Usuario que creó el registro. |  |
| 8 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
