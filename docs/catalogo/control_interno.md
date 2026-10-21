# Control interno (`control_interno`)

Schema unificado para el Sistema de Control Interno Institucional

85 tablas · 6 vistas · 1310 columnas · 34.506 filas · 24 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`accion_correctiva`](#accion_correctiva) | Tabla | 29 | _Por documentar_ |
| [`accion_mejora`](#accion_mejora) | Tabla | 0 | Acciones de mejora dentro de un plan |
| [`actividad_etapa_auditoria`](#actividad_etapa_auditoria) | Tabla | 0 | Actividades dentro de cada etapa de auditoría |
| [`actividad_plan_anual_5`](#actividad_plan_anual_5) | Tabla | 1604 | Actividades por rol del plan anual |
| [`actividad_proceso_auditoria`](#actividad_proceso_auditoria) | Tabla | 0 | Actividades del proceso de auditoría. Cada fase tiene hasta 3 actividades requeridas para avanzar. |
| [`actividad_rol`](#actividad_rol) | Tabla | 0 | Actividades por rol configurable (RF020) |
| [`adjunto_actividad_plan_anual_5`](#adjunto_actividad_plan_anual_5) | Tabla | 21 | Archivos adjuntos (evidencias) para actividades del Plan Anual de Auditoría según Decreto 648/2017 |
| [`alerta_plan`](#alerta_plan) | Tabla | 21 | _Por documentar_ |
| [`ampliacion_plazo`](#ampliacion_plazo) | Tabla | 0 | Solicitudes de ampliación de plazo de auditorías |
| [`aprobacion`](#aprobacion) | Tabla | 10 | Sistema de aprobaciones centralizado |
| [`auditor_perfil`](#auditor_perfil) | Tabla | 0 | Perfil profesional de auditores. Almacena información específica como especialidades y disponibilidad. |
| [`auditoria`](#auditoria) | Tabla | 70 | Auditorías del sistema con gestión Kanban, Lista y Calendario |
| [`auditoria_especial_info`](#auditoria_especial_info) | Tabla | 0 | Información específica de auditorías especiales (motivo, solicitante, justificación). |
| [`auditoria_gestion`](#auditoria_gestion) | Tabla | 0 | Gestión de auditorías con fases y seguimiento |
| [`auditoria_programada`](#auditoria_programada) | Tabla | 0 | Auditorías programadas en el plan anual |
| [`auditoria_territorial_info`](#auditoria_territorial_info) | Tabla | 0 | Información específica de auditorías territoriales (ciudad, departamento, contacto). |
| [`cache_esap`](#cache_esap) | Tabla | 0 | Cache del sistema ESAP |
| [`cierre_plan`](#cierre_plan) | Tabla | 2 | _Por documentar_ |
| [`condicion_disparo_notificacion`](#condicion_disparo_notificacion) | Tabla | 12 | _Por documentar_ |
| [`configuracion_esap`](#configuracion_esap) | Tabla | 7 | Configuraciones específicas del sistema ESAP |
| [`configuracion_profesionales_ocig`](#configuracion_profesionales_ocig) | Tabla | 31 | Configuración de profesionales asignados al equipo OCIG (Oficina de Control Interno de Gestión) |
| [`criterio_auditoria`](#criterio_auditoria) | Tabla | 27 | Criterios de auditoría (normas, políticas, estándares aplicables) |
| [`cronograma_auditoria`](#cronograma_auditoria) | Tabla | 0 | Cronograma de auditorías del plan anual |
| [`cronograma_fase_auditoria`](#cronograma_fase_auditoria) | Tabla | 0 | Cronograma estimado por fase de la auditoría (duración de cada fase) |
| [`datos_automaticos_informe`](#datos_automaticos_informe) | Tabla | 0 | Datos automáticos poblados desde el sistema (US-022) |
| [`documento`](#documento) | Tabla | 77 | Gestión documental centralizada (RF013) |
| [`documento_aprobacion`](#documento_aprobacion) | Tabla | 0 | _Por documentar_ |
| [`documento_plan_mejoramiento`](#documento_plan_mejoramiento) | Tabla | 0 | _Por documentar_ |
| [`entrega_informe_ley`](#entrega_informe_ley) | Tabla | 0 | Entregas de informes de ley por periodo |
| [`equipo_auditor`](#equipo_auditor) | Tabla | 160 | Equipo de auditores asignados a una auditoría. Relación N-N entre auditorías y personas. |
| [`especialidades_ocig`](#especialidades_ocig) | Tabla | 13 | _Por documentar_ |
| [`etapa_auditoria`](#etapa_auditoria) | Tabla | 0 | Etapas de ejecución de auditorías |
| [`etapa_kanban`](#etapa_kanban) | Tabla | 12 | Etapas configuradas para cada tablero Kanban |
| [`evaluacion_proceso`](#evaluacion_proceso) | Tabla | 54 | Evaluaciones DAFP de procesos auditables. Cada proceso puede tener múltiples evaluaciones con diferentes vigencias/fechas de corte. |
| [`eventos_timeline`](#eventos_timeline) | Tabla | 265 | Registro histórico de todos los eventos importantes relacionados con planes de mejoramiento |
| [`evidencia_accion`](#evidencia_accion) | Tabla | 0 | _Por documentar_ |
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
| [`plan_anual_5_roles`](#plan_anual_5_roles) | Tabla | 63 | _Por documentar_ |
| [`plan_anual_wizard_borrador`](#plan_anual_wizard_borrador) | Tabla | 2 | _Por documentar_ |
| [`plan_individual`](#plan_individual) | Tabla | 0 | Planes individuales de auditoría |
| [`plan_mejoramiento`](#plan_mejoramiento) | Tabla | 14 | Planes de mejoramiento derivados de hallazgos |
| [`plantilla_email`](#plantilla_email) | Tabla | 0 | Plantillas de correo electrónico (RF020) |
| [`plantilla_informe_ley`](#plantilla_informe_ley) | Tabla | 16 | Plantillas para generación automática de informes de ley |
| [`plantilla_reporte`](#plantilla_reporte) | Tabla | 0 | Plantillas para generación de reportes |
| [`plantillas_documentos_esap`](#plantillas_documentos_esap) | Tabla | 0 | Plantillas de documentos personalizadas |
| [`preferencia_notificacion`](#preferencia_notificacion) | Tabla | 1 | Preferencias de notificación por usuario (RF014) |
| [`proceso_auditable`](#proceso_auditable) | Tabla | 36 | Procesos auditables del universo de auditorías |
| [`programa_anual_ajuste`](#programa_anual_ajuste) | Tabla | 3 | Ajustes del Programa Anual (EFDS-1919): borrador de la siguiente versión; la versión que se genera lo cierra. |
| [`registro_seguimiento`](#registro_seguimiento) | Tabla | 0 | _Por documentar_ |
| [`reunion_apertura`](#reunion_apertura) | Tabla | 15 | Información de la reunión de apertura de la auditoría |
| [`reunion_cierre`](#reunion_cierre) | Tabla | 11 | Información de la reunión de cierre de la auditoría |
| [`rol_decreto_648`](#rol_decreto_648) | Tabla | 0 | Roles del Decreto 648 configurable (RF020) |
| [`rol_decreto_648_template`](#rol_decreto_648_template) | Tabla | 5 | _Por documentar_ |
| [`rol_plan_anual`](#rol_plan_anual) | Tabla | 0 | Roles y disponibilidad de auditores en el plan anual |
| [`rol_plan_anual_5`](#rol_plan_anual_5) | Tabla | 405 | Roles del plan anual (5 roles) |
| [`seccion_lista_chequeo`](#seccion_lista_chequeo) | Tabla | 0 | Secciones organizadas de listas de chequeo |
| [`seguimiento_plan`](#seguimiento_plan) | Tabla | 7 | _Por documentar_ |
| [`seguimiento_plan_mejoramiento`](#seguimiento_plan_mejoramiento) | Tabla | 0 | Seguimientos trimestrales de planes de mejoramiento |
| [`seguimiento_trimestral`](#seguimiento_trimestral) | Tabla | 0 | _Por documentar_ |
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

_Por documentar._

- Clave primaria: `id`
- Filas: 29
- Referencia a: `plan_id` → `control_interno.plan_mejoramiento` (0..* → 1)
- Relaciones implícitas: `hallazgo_id` ↝ `control_interno.hallazgo` (100.0 % con padre)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `plan_id` | `uuid` | no | _Por documentar_ | FK→control_interno.plan_mejoramiento.id |
| 3 | `descripcion` | `text` | no | _Por documentar_ |  |
| 4 | `tipo` | `character varying(50)` | no | _Por documentar_ |  |
| 5 | `responsable` | `character varying(255)` | no | _Por documentar_ |  |
| 6 | `fecha_inicio` | `date` | no | _Por documentar_ |  |
| 7 | `fecha_fin` | `date` | no | _Por documentar_ |  |
| 8 | `recursos` | `text` | sí | _Por documentar_ |  |
| 9 | `indicador` | `character varying(500)` | sí | _Por documentar_ |  |
| 10 | `meta_indicador` | `character varying(500)` | sí | _Por documentar_ |  |
| 11 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 12 | `porcentaje_avance` | `integer` | sí | _Por documentar_ |  |
| 13 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 14 | `evidencias` | `jsonb` | sí | _Por documentar_ |  |
| 15 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 16 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 17 | `hallazgo_id` | `uuid` | sí | ID del hallazgo al que está vinculada esta acción correctiva (opcional) | ↝control_interno.hallazgo.id |
| 18 | `estado_verificacion_oci` | `character varying(20)` | sí | Verificación OCI: sin_verificar, cumplida, parcial, incumplida |  |
| 19 | `evidencia_verificada` | `text` | sí | Descripción de la evidencia revisada por el OCI |  |
| 20 | `observacion_oci` | `text` | sí | Observación opcional del OCI |  |
| 21 | `fecha_verificacion_oci` | `timestamp without time zone` | sí | Fecha en que se registró la verificación OCI |  |
| 22 | `verificada_por_id` | `bigint` | sí | ID del usuario que registró la verificación |  |
| 23 | `cantidad_acciones_programadas` | `integer` | sí | _Por documentar_ |  |
| 24 | `cantidad_acciones_implementadas` | `integer` | sí | _Por documentar_ |  |
| 25 | `cumplimiento_emfo` | `integer` | sí | _Por documentar_ |  |
| 26 | `estado_accion_seguimiento` | `character varying(20)` | sí | _Por documentar_ |  |
| 27 | `responsable_seguimiento` | `character varying(500)` | sí | _Por documentar_ |  |
| 28 | `observacion_cumplimiento` | `text` | sí | _Por documentar_ |  |
| 29 | `evaluar_aplicacion_controles` | `boolean` | sí | _Por documentar_ |  |
| 30 | `validar_situacion_no_repitio` | `boolean` | sí | _Por documentar_ |  |
| 31 | `efectividad_emfo` | `integer` | sí | _Por documentar_ |  |
| 32 | `efectividad_verificada` | `boolean` | sí | _Por documentar_ |  |
| 33 | `observacion_efectividad` | `text` | sí | _Por documentar_ |  |

## accion_mejora

Acciones de mejora dentro de un plan

- Clave primaria: `id`
- Filas: 0
- Referencia a: `plan_mejoramiento_id` → `control_interno.plan_mejoramiento` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `numero` | `integer` | no | _Por documentar_ |  |
| 3 | `descripcion` | `text` | no | _Por documentar_ |  |
| 4 | `tipo` | `character varying(50)` | no | _Por documentar_ |  |
| 5 | `responsable` | `character varying(255)` | no | _Por documentar_ |  |
| 6 | `fecha_inicio` | `date` | no | _Por documentar_ |  |
| 7 | `fecha_fin` | `date` | no | _Por documentar_ |  |
| 8 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 9 | `avance` | `integer` | no | _Por documentar_ |  |
| 10 | `evidencias` | `jsonb` | no | _Por documentar_ |  |
| 11 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 12 | `plan_mejoramiento_id` | `uuid` | no | _Por documentar_ | FK→control_interno.plan_mejoramiento.id |
| 13 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## actividad_etapa_auditoria

Actividades dentro de cada etapa de auditoría

- Clave primaria: `id`
- Filas: 0
- Referencia a: `etapa_id` → `control_interno.etapa_auditoria` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `etapa_id` | `uuid` | no | _Por documentar_ | FK→control_interno.etapa_auditoria.id |
| 3 | `nombre` | `character varying(500)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `tipo` | `character varying(100)` | no | _Por documentar_ |  |
| 6 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 7 | `responsable` | `character varying(255)` | sí | _Por documentar_ |  |
| 8 | `fecha_limite` | `date` | sí | _Por documentar_ |  |
| 9 | `completada` | `boolean` | sí | _Por documentar_ |  |
| 10 | `fecha_completacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## actividad_plan_anual_5

Actividades por rol del plan anual

- Clave primaria: `id`
- Filas: 1604
- Referencia a: `rol_id` → `control_interno.rol_plan_anual_5` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `rol_id` | `uuid` | no | _Por documentar_ | FK→control_interno.rol_plan_anual_5.id |
| 3 | `plan_id` | `uuid` | no | _Por documentar_ |  |
| 4 | `nombre` | `character varying(500)` | no | _Por documentar_ |  |
| 5 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 6 | `responsable` | `character varying(255)` | no | _Por documentar_ |  |
| 7 | `fecha_inicio` | `date` | no | _Por documentar_ |  |
| 8 | `fecha_fin` | `date` | no | _Por documentar_ |  |
| 9 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 10 | `porcentaje_avance` | `integer` | sí | _Por documentar_ |  |
| 11 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 12 | `prioridad` | `character varying(20)` | no | _Por documentar_ |  |
| 13 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 15 | `control` | `text` | sí | Descripción del control aplicado a la actividad |  |
| 16 | `evaluacion` | `text` | sí | Evaluación del cumplimiento de la actividad |  |
| 17 | `seguimiento` | `text` | sí | Registro de seguimiento de la actividad |  |
| 18 | `requiere_verificacion_director` | `boolean` | sí | Indica si la actividad requiere verificación del Director OCIG antes de marcarse como completada |  |
| 19 | `verificada_por_director` | `boolean` | sí | Indica si la actividad fue verificada y aprobada por el Director OCIG |  |
| 20 | `fecha_verificacion` | `timestamp without time zone` | sí | Fecha y hora en que el Director OCIG verificó la actividad |  |
| 21 | `observaciones_director` | `text` | sí | Observaciones o comentarios del Director OCIG al verificar la actividad |  |
| 22 | `configuracion_evidencias` | `jsonb` | sí | Configuración JSON de requisitos de evidencias: adjuntosRequeridos, observacionRequerida, minimoAdjuntos, tiposPermitidos, longitudMinima |  |
| 23 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 24 | `tipo_calculo` | `character varying(50)` | sí | Tipo de cálculo de cumplimiento: manual (usuario), auditorias (automático), planes_mejoramiento (automático) |  |
| 25 | `total_auditorias_programadas` | `integer` | sí | _Por documentar_ |  |
| 26 | `total_auditorias_finalizadas` | `integer` | sí | _Por documentar_ |  |
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
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `auditoria_id` | `uuid` | no | _Por documentar_ | FK→control_interno.auditoria.id |
| 3 | `fase` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 6 | `orden` | `integer` | no | _Por documentar_ |  |
| 7 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 8 | `fecha_limite` | `date` | sí | _Por documentar_ |  |
| 9 | `fecha_completacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 10 | `completada_por_id` | `uuid` | sí | _Por documentar_ | FK→auth.personas.id_person |
| 11 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 12 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 13 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## actividad_rol

Actividades por rol configurable (RF020)

- Clave primaria: `id`
- Filas: 0
- Referencia a: `rol_id` → `control_interno.rol_decreto_648` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `rol_id` | `uuid` | no | _Por documentar_ | FK→control_interno.rol_decreto_648.id |
| 3 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `orden` | `integer` | sí | _Por documentar_ |  |
| 6 | `activa` | `boolean` | sí | _Por documentar_ |  |
| 7 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 8 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## adjunto_actividad_plan_anual_5

Archivos adjuntos (evidencias) para actividades del Plan Anual de Auditoría según Decreto 648/2017

- Clave primaria: `id`
- Filas: 21
- Referencia a: `actividad_id` → `control_interno.actividad_plan_anual_5` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `actividad_id` | `uuid` | no | FK a la actividad del plan anual a la que pertenece este adjunto | FK→control_interno.actividad_plan_anual_5.id |
| 3 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `tipo` | `character varying(100)` | sí | MIME type del archivo (ej: application/pdf, image/jpeg, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet) |  |
| 5 | `tamanio` | `bigint` | sí | Tamaño del archivo en bytes |  |
| 6 | `fecha_carga` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 7 | `cargado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 8 | `cargado_por_id` | `bigint` | sí | _Por documentar_ |  |
| 9 | `ruta_archivo` | `character varying(500)` | sí | Ruta física del archivo en el servidor o storage |  |
| 10 | `url` | `character varying(500)` | sí | URL pública o firmada para acceder/descargar el archivo |  |
| 11 | `hash_archivo` | `character varying(255)` | sí | _Por documentar_ |  |
| 12 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 13 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## alerta_plan

_Por documentar._

- Clave primaria: `id`
- Filas: 21
- Referencia a: `accion_id` → `control_interno.accion_correctiva` (0..1 → 0..1); `plan_id` → `control_interno.plan_mejoramiento` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `plan_id` | `uuid` | no | _Por documentar_ | FK→control_interno.plan_mejoramiento.id |
| 3 | `accion_id` | `uuid` | sí | _Por documentar_ | FK→control_interno.accion_correctiva.id |
| 4 | `tipo` | `character varying(50)` | no | _Por documentar_ |  |
| 5 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 6 | `generada_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 7 | `atendida` | `boolean` | sí | _Por documentar_ |  |
| 8 | `atendida_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 9 | `atendida_por_id` | `character varying(255)` | sí | _Por documentar_ |  |

## ampliacion_plazo

Solicitudes de ampliación de plazo de auditorías

- Clave primaria: `id`
- Filas: 0
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `auditoria_id` | `uuid` | no | _Por documentar_ | FK→control_interno.auditoria.id |
| 3 | `fecha_fin_original` | `date` | no | _Por documentar_ |  |
| 4 | `fecha_fin_solicitada` | `date` | no | _Por documentar_ |  |
| 5 | `fecha_solicitud` | `timestamp without time zone` | no | _Por documentar_ |  |
| 6 | `fecha_respuesta` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 7 | `estado` | `character varying(20)` | no | Estados: pendiente, aprobada, rechazada |  |
| 8 | `justificacion` | `text` | no | _Por documentar_ |  |
| 9 | `motivo_rechazo` | `text` | sí | _Por documentar_ |  |
| 10 | `comentarios` | `text` | sí | _Por documentar_ |  |
| 11 | `solicitado_por` | `character varying(100)` | no | _Por documentar_ |  |
| 12 | `aprobado_rechazado_por` | `character varying(100)` | sí | _Por documentar_ |  |
| 13 | `dias_ampliacion` | `integer` | sí | Días de ampliación solicitados (calculado automáticamente) |  |
| 14 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 15 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |

## aprobacion

Sistema de aprobaciones centralizado

- Clave primaria: `id`
- Filas: 10

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(255)` | sí | _Por documentar_ | única |
| 3 | `tipo` | `character varying(100)` | sí | _Por documentar_ |  |
| 4 | `titulo` | `character varying(500)` | sí | _Por documentar_ |  |
| 5 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 6 | `solicitante` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `fecha_solicitud` | `date` | sí | _Por documentar_ |  |
| 8 | `prioridad` | `character varying(20)` | no | _Por documentar_ |  |
| 9 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 10 | `territorial` | `character varying(255)` | sí | _Por documentar_ |  |
| 11 | `sede` | `character varying(255)` | sí | _Por documentar_ |  |
| 12 | `relacionado` | `character varying(255)` | sí | _Por documentar_ |  |
| 13 | `documentos_count` | `integer` | sí | _Por documentar_ |  |
| 14 | `aprobado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 15 | `fecha_aprobacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 16 | `rechazado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 17 | `fecha_rechazo` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 18 | `motivo_rechazo` | `text` | sí | _Por documentar_ |  |
| 19 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 20 | `area` | `character varying(255)` | sí | _Por documentar_ |  |
| 21 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 22 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## auditor_perfil

Perfil profesional de auditores. Almacena información específica como especialidades y disponibilidad.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `persona_id` → `auth.personas` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `persona_id` | `uuid` | no | _Por documentar_ | única FK→auth.personas.id_person |
| 3 | `especialidad` | `character varying(255)` | sí | Especialidad del auditor (ej: Auditoría Financiera, Control Interno, Gestión Administrativa) |  |
| 4 | `cargo` | `character varying(100)` | sí | _Por documentar_ |  |
| 5 | `nivel_experiencia` | `character varying(50)` | sí | _Por documentar_ |  |
| 6 | `estado_disponibilidad` | `character varying(50)` | sí | Estado de disponibilidad: Disponible, Parcial, No disponible, En licencia |  |
| 7 | `fecha_ultima_actividad` | `date` | sí | _Por documentar_ |  |
| 8 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 9 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 10 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## auditoria

Auditorías del sistema con gestión Kanban, Lista y Calendario

- Clave primaria: `id`
- Filas: 70
- Referencia a: `actividad_plan_anual_id` → `control_interno.actividad_plan_anual_5` (0..1 → 0..1); `auditor_asignado_id` → `auth.personas` (0..1 → 0..1); `auditor_lider_id` → `auth.personas` (0..* → 0..1); `supervisor_asignado_id` → `auth.personas` (0..* → 0..1); `auditor_asignado_id` → `auth.personas` (0..1 → 0..1); `auditor_lider_id` → `auth.personas` (0..* → 0..1); `plan_anual_id` → `control_interno.plan_anual_5_roles` (0..* → 0..1); `supervisor_asignado_id` → `auth.personas` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(500)` | no | _Por documentar_ |  |
| 4 | `tipo` | `character varying(50)` | no | _Por documentar_ |  |
| 5 | `fase` | `character varying(50)` | no | Fase actual de la auditoría (planeacion, en-curso, revision, completada) |  |
| 6 | `territorial` | `character varying(255)` | no | _Por documentar_ |  |
| 7 | `sede` | `character varying(255)` | no | Sede donde se realiza la auditoría |  |
| 8 | `responsable` | `character varying(255)` | no | Responsable de la auditoría |  |
| 9 | `fecha_inicio` | `date` | no | Inicio de Etapa 1: Planeación (= fechaInicioPlaneacion) |  |
| 10 | `fecha_fin` | `date` | no | Fin de Etapa 3: Comunicación (= fechaFinComunicacion, fin de la auditoría) |  |
| 11 | `progreso` | `integer` | sí | _Por documentar_ |  |
| 12 | `prioridad` | `character varying(20)` | no | _Por documentar_ |  |
| 13 | `hallazgos` | `integer` | sí | _Por documentar_ |  |
| 14 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 15 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 16 | `estado_kanban` | `character varying(50)` | sí | Estado de la auditoría en el Kanban |  |
| 17 | `semaforo` | `character varying(20)` | sí | _Por documentar_ |  |
| 18 | `tipo_kanban` | `character varying(50)` | sí | _Por documentar_ |  |
| 19 | `prioridad_kanban` | `character varying(20)` | sí | _Por documentar_ |  |
| 20 | `area_objetivo` | `character varying(255)` | sí | _Por documentar_ |  |
| 21 | `permite_cambiar_objetivos` | `boolean` | sí | _Por documentar_ |  |
| 22 | `descripcion` | `text` | sí | Descripción detallada de la auditoría |  |
| 23 | `alcance` | `text` | sí | _Por documentar_ |  |
| 24 | `proceso_auditado` | `character varying(500)` | sí | _Por documentar_ |  |
| 25 | `responsable_area_nombre` | `character varying(255)` | sí | _Por documentar_ |  |
| 26 | `responsable_area_cargo` | `character varying(255)` | sí | _Por documentar_ |  |
| 27 | `responsable_area_email` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 28 | `supervisor_asignado_id` | `uuid` | sí | ID del supervisor asignado (FK a auth.personas) | FK→auth.personas.id_person |
| 29 | `fecha_reunion_apertura` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 30 | `metodologia` | `text` | sí | _Por documentar_ |  |
| 31 | `periodicidad` | `character varying(20)` | sí | _Por documentar_ |  |
| 32 | `presupuesto_estimado` | `numeric(15,2)` | sí | _Por documentar_ |  |
| 33 | `vinculada_plan_anual` | `boolean` | sí | Indica si la auditoría pertenece al programa/plan anual OCI |  |
| 34 | `plan_anual_id` | `uuid` | sí | FK al plan anual 5 roles (control_interno.plan_anual_5_roles) | FK→control_interno.plan_anual_5_roles.id |
| 35 | `plan_anual_vigencia` | `integer` | sí | Año de vigencia del plan anual (ej. 2026) |  |
| 36 | `rol_decreto_asociado` | `character varying(255)` | sí | Rol Decreto 648/2017 asociado en la programación |  |
| 37 | `observaciones_adicionales` | `text` | sí | _Por documentar_ |  |
| 38 | `checklist_completados` | `jsonb` | sí | Estado de los checkboxes de actividades de auditoría. Formato: {"ep1": true, "ep2": false, ...} |  |
| 39 | `archivada` | `boolean` | sí | _Por documentar_ |  |
| 40 | `fecha_archivo` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 41 | `activa` | `boolean` | sí | Indica si la auditoría está activa |  |
| 42 | `fecha_eliminacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 43 | `riesgo_kanban` | `character varying(20)` | sí | _Por documentar_ |  |
| 44 | `calificacion_riesgo` | `character varying(255)` | sí | Calificación del riesgo de la auditoría (ampliado a 255 caracteres) |  |
| 45 | `ultima_actuacion` | `text` | sí | _Por documentar_ |  |
| 46 | `dias_restantes` | `integer` | sí | _Por documentar_ |  |
| 47 | `porcentaje_tiempo` | `integer` | sí | _Por documentar_ |  |
| 48 | `total_documentos` | `integer` | sí | _Por documentar_ |  |
| 49 | `total_informes` | `integer` | sí | _Por documentar_ |  |
| 50 | `total_tareas` | `integer` | sí | _Por documentar_ |  |
| 51 | `actividades_completas` | `boolean` | sí | _Por documentar_ |  |
| 52 | `actividades_pendientes` | `integer` | sí | _Por documentar_ |  |
| 53 | `auditor_lider_id` | `uuid` | sí | ID del auditor líder (FK a auth.personas) | FK→auth.personas.id_person |
| 54 | `auditor_asignado_id` | `uuid` | sí | ID del auditor asignado (FK a auth.personas) | FK→auth.personas.id_person |
| 55 | `programa_anual_metadata` | `jsonb` | sí | Metadata del programa anual: { "mesInicio": 0-11, "semanaInicio": 1-4, "duraciones": { "planeacion": number, "ejecucion": number, "comunicacion": number } } |  |
| 56 | `aprobada` | `boolean` | no | Indica si la auditoría fue aprobada por el Jefe de Control Interno |  |
| 57 | `fecha_aprobacion` | `timestamp without time zone` | sí | Fecha y hora en que la auditoría fue aprobada |  |
| 58 | `aprobada_por` | `character varying(255)` | sí | Nombre completo del usuario que aprobó la auditoría |  |
| 59 | `aprobada_por_id` | `bigint` | sí | ID del usuario que aprobó la auditoría (referencia a auth.personas) |  |
| 60 | `actividad_plan_anual_id` | `uuid` | sí | _Por documentar_ | FK→control_interno.actividad_plan_anual_5.id |
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
| 76 | `periodo_inicio` | `date` | sí | _Por documentar_ |  |
| 77 | `periodo_fin` | `date` | sí | _Por documentar_ |  |
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
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `auditoria_id` | `uuid` | no | _Por documentar_ | única FK→control_interno.auditoria.id |
| 3 | `tipo_motivo` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `solicitante` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `justificacion` | `text` | no | _Por documentar_ |  |
| 6 | `fecha_solicitud` | `date` | sí | _Por documentar_ |  |
| 7 | `fecha_aprobacion` | `date` | sí | _Por documentar_ |  |
| 8 | `aprobado_por_id` | `uuid` | sí | _Por documentar_ | FK→auth.personas.id_person |
| 9 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 10 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## auditoria_gestion

Gestión de auditorías con fases y seguimiento

- Clave primaria: `id`
- Filas: 0
- Referencia a: `auditoria_programada_id` → `control_interno.auditoria_programada` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(500)` | no | _Por documentar_ |  |
| 4 | `tipo` | `character varying(100)` | no | _Por documentar_ |  |
| 5 | `fase` | `character varying(50)` | no | _Por documentar_ |  |
| 6 | `territorial` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `sede` | `character varying(255)` | sí | _Por documentar_ |  |
| 8 | `responsable` | `character varying(255)` | no | _Por documentar_ |  |
| 9 | `fecha_inicio` | `date` | no | _Por documentar_ |  |
| 10 | `fecha_fin` | `date` | no | _Por documentar_ |  |
| 11 | `progreso` | `integer` | sí | _Por documentar_ |  |
| 12 | `prioridad` | `character varying(20)` | no | _Por documentar_ |  |
| 13 | `hallazgos_count` | `integer` | sí | _Por documentar_ |  |
| 14 | `auditoria_programada_id` | `uuid` | sí | _Por documentar_ | FK→control_interno.auditoria_programada.id |
| 15 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 16 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## auditoria_programada

Auditorías programadas en el plan anual

- Clave primaria: `id`
- Filas: 0
- Referencia a: `proceso_id` → `control_interno.proceso_auditable` (0..1 → 1); `programa_anual_id` → `control_interno.plan_anual` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `proceso_id` | `uuid` | no | _Por documentar_ | FK→control_interno.proceso_auditable.id |
| 5 | `proceso_codigo` | `character varying(255)` | no | _Por documentar_ |  |
| 6 | `proceso_nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 7 | `tipo` | `character varying(50)` | no | _Por documentar_ |  |
| 8 | `alcance` | `text` | no | _Por documentar_ |  |
| 9 | `proceso_auditar` | `character varying(255)` | no | _Por documentar_ |  |
| 10 | `auditor_lider` | `character varying(255)` | no | _Por documentar_ |  |
| 11 | `equipo_auditor` | `jsonb` | no | _Por documentar_ |  |
| 12 | `fecha_inicio_planeada` | `date` | no | _Por documentar_ |  |
| 13 | `fecha_fin_planeada` | `date` | no | _Por documentar_ |  |
| 14 | `duracion_dias` | `integer` | no | _Por documentar_ |  |
| 15 | `prioridad` | `character varying(20)` | no | _Por documentar_ |  |
| 16 | `riesgo_inherente` | `character varying(20)` | no | _Por documentar_ |  |
| 17 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 18 | `es_territorial` | `boolean` | sí | _Por documentar_ |  |
| 19 | `territorial` | `character varying(255)` | sí | _Por documentar_ |  |
| 20 | `es_especial` | `boolean` | sí | _Por documentar_ |  |
| 21 | `solicitada_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 22 | `motivo_especial` | `text` | sí | _Por documentar_ |  |
| 23 | `etapas` | `jsonb` | no | _Por documentar_ |  |
| 24 | `ampliaciones` | `jsonb` | sí | _Por documentar_ |  |
| 25 | `fecha_limite_original` | `date` | no | _Por documentar_ |  |
| 26 | `fecha_limite_actual` | `date` | no | _Por documentar_ |  |
| 27 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 28 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 29 | `programa_anual_id` | `uuid` | sí | Referencia al plan anual al que pertenece esta auditoría | FK→control_interno.plan_anual.id |

## auditoria_territorial_info

Información específica de auditorías territoriales (ciudad, departamento, contacto).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `auditoria_id` | `uuid` | no | _Por documentar_ | única FK→control_interno.auditoria.id |
| 3 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `ciudad` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `departamento` | `character varying(255)` | no | _Por documentar_ |  |
| 6 | `direccion` | `text` | sí | _Por documentar_ | Contacto |
| 7 | `contacto_nombre` | `character varying(255)` | sí | _Por documentar_ |  |
| 8 | `contacto_email` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 9 | `contacto_telefono` | `character varying(20)` | sí | _Por documentar_ | Contacto |
| 10 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 11 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## cache_esap

Cache del sistema ESAP

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `clave` | `character varying(500)` | no | _Por documentar_ | única |
| 3 | `valor` | `jsonb` | no | _Por documentar_ |  |
| 4 | `fecha_expiracion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 5 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 6 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## cierre_plan

_Por documentar._

- Clave primaria: `id`
- Filas: 2
- Referencia a: `plan_id` → `control_interno.plan_mejoramiento` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `plan_id` | `uuid` | no | _Por documentar_ | única FK→control_interno.plan_mejoramiento.id |
| 3 | `cerrado` | `boolean` | sí | _Por documentar_ |  |
| 4 | `fecha_cierre` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 5 | `cerrado_por_id` | `character varying(255)` | sí | _Por documentar_ |  |
| 6 | `cerrado_por_nombre` | `character varying(500)` | sí | _Por documentar_ |  |
| 7 | `observaciones_cierre` | `text` | sí | _Por documentar_ |  |
| 8 | `efectividad_verificada` | `boolean` | sí | _Por documentar_ |  |
| 9 | `archivado` | `boolean` | sí | _Por documentar_ |  |
| 10 | `indice_electronico_ref` | `character varying(1000)` | sí | _Por documentar_ |  |
| 11 | `fecha_archivo` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 12 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |

## condicion_disparo_notificacion

_Por documentar._

- Clave primaria: `id`
- Filas: 12

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `nombre` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `descripcion` | `character varying(255)` | sí | _Por documentar_ |  |
| 4 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 5 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 6 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## configuracion_esap

Configuraciones específicas del sistema ESAP

- Clave primaria: `id`
- Filas: 7

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `clave` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `valor` | `text` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `tipo` | `character varying(50)` | sí | _Por documentar_ |  |
| 6 | `categoria` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 8 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## configuracion_profesionales_ocig

Configuración de profesionales asignados al equipo OCIG (Oficina de Control Interno de Gestión)

- Clave primaria: `id`
- Filas: 31

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `id_tercero` | `character varying(36)` | no | ID del tercero (persona) en auth.personas | única |
| 3 | `rol_ocig` | `character varying(100)` | no | Rol del profesional dentro del equipo OCIG |  |
| 4 | `especialidades` | `text[]` | sí | Array de especialidades del profesional (ej: Auditoría Financiera, Auditoría TI) |  |
| 5 | `capacidad_maxima_auditorias` | `integer` | no | Número máximo de auditorías simultáneas que puede manejar |  |
| 6 | `horas_mensuales_disponibles` | `integer` | no | Horas mensuales disponibles para auditorías |  |
| 7 | `puede_ser_lider` | `boolean` | no | Indica si el profesional puede ser asignado como auditor líder |  |
| 8 | `activo` | `boolean` | no | _Por documentar_ |  |
| 9 | `fecha_asignacion` | `date` | no | _Por documentar_ |  |
| 10 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 11 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 12 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 13 | `created_by` | `uuid` | sí | _Por documentar_ |  |
| 14 | `updated_by` | `uuid` | sí | _Por documentar_ |  |

## criterio_auditoria

Criterios de auditoría (normas, políticas, estándares aplicables)

- Clave primaria: `id`
- Filas: 27
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `auditoria_id` | `uuid` | no | _Por documentar_ | FK→control_interno.auditoria.id |
| 3 | `criterio` | `text` | no | _Por documentar_ |  |
| 4 | `orden` | `integer` | sí | _Por documentar_ |  |
| 5 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 6 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 7 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## cronograma_auditoria

Cronograma de auditorías del plan anual

- Clave primaria: `id`
- Filas: 0
- Referencia a: `plan_id` → `control_interno.plan_anual` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `plan_id` | `uuid` | no | _Por documentar_ | FK→control_interno.plan_anual.id |
| 3 | `codigo` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `proceso` | `character varying(255)` | no | _Por documentar_ |  |
| 6 | `nivel_riesgo` | `character varying(20)` | sí | _Por documentar_ |  |
| 7 | `trimestre` | `character varying(10)` | no | _Por documentar_ |  |
| 8 | `fecha_inicio` | `date` | no | _Por documentar_ |  |
| 9 | `fecha_fin` | `date` | no | _Por documentar_ |  |
| 10 | `auditor_responsable` | `character varying(255)` | sí | _Por documentar_ |  |
| 11 | `horas_estimadas` | `integer` | no | _Por documentar_ |  |
| 12 | `estado` | `character varying(50)` | sí | _Por documentar_ |  |
| 13 | `es_territorial` | `boolean` | sí | _Por documentar_ |  |
| 14 | `territorial` | `character varying(255)` | sí | _Por documentar_ |  |
| 15 | `es_especial` | `boolean` | sí | _Por documentar_ |  |
| 16 | `equipo` | `jsonb` | sí | _Por documentar_ |  |
| 17 | `etapas_cronograma` | `jsonb` | sí | _Por documentar_ |  |
| 18 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 19 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## cronograma_fase_auditoria

Cronograma estimado por fase de la auditoría (duración de cada fase)

- Clave primaria: `id`
- Filas: 0
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `auditoria_id` | `uuid` | no | _Por documentar_ | FK→control_interno.auditoria.id |
| 3 | `fase` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `fecha_inicio` | `date` | no | _Por documentar_ |  |
| 5 | `fecha_fin` | `date` | no | _Por documentar_ |  |
| 6 | `dias_estimados` | `integer` | no | _Por documentar_ |  |
| 7 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 8 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## datos_automaticos_informe

Datos automáticos poblados desde el sistema (US-022)

- Clave primaria: `id`
- Filas: 0
- Referencia a: `entrega_id` → `control_interno.entrega_informe_ley` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `entrega_id` | `uuid` | no | _Por documentar_ | FK→control_interno.entrega_informe_ley.id |
| 3 | `tipo_dato` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `datos` | `jsonb` | no | JSON con los datos estructurados según el tipo de dato |  |
| 5 | `fecha_generacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 6 | `fuente_datos` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `version_datos` | `character varying(50)` | sí | _Por documentar_ |  |
| 8 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## documento

Gestión documental centralizada (RF013)

- Clave primaria: `id`
- Filas: 77
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..* → 0..1); `documento_biblioteca_id` → `control_interno.documento` (0..* → 0..1); `version_anterior_id` → `control_interno.documento` (0..* → 0..1)
- Relaciones implícitas: `etapa_kanban_id` ↝ `control_interno.etapa_kanban` (100.0 % con padre); `hallazgo_id` ↝ `control_interno.hallazgo` (100.0 % con padre)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 3 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 4 | `tipo_documento` | `character varying(100)` | no | _Por documentar_ |  |
| 5 | `etapa` | `character varying(50)` | sí | _Por documentar_ |  |
| 6 | `auditoria_id` | `uuid` | sí | _Por documentar_ | FK→control_interno.auditoria.id |
| 7 | `hallazgo_id` | `uuid` | sí | _Por documentar_ | ↝control_interno.hallazgo.id |
| 8 | `plan_mejoramiento_id` | `uuid` | sí | _Por documentar_ |  |
| 9 | `ruta_archivo` | `character varying(500)` | no | _Por documentar_ |  |
| 10 | `nombre_archivo` | `character varying(255)` | no | _Por documentar_ |  |
| 11 | `tipo_mime` | `character varying(100)` | no | _Por documentar_ |  |
| 12 | `tamanio_bytes` | `bigint` | no | _Por documentar_ |  |
| 13 | `version` | `integer` | sí | _Por documentar_ |  |
| 14 | `version_anterior_id` | `uuid` | sí | _Por documentar_ | FK→control_interno.documento.id |
| 15 | `subido_por` | `character varying(255)` | no | _Por documentar_ |  |
| 16 | `hash_archivo` | `character varying(255)` | sí | _Por documentar_ |  |
| 17 | `comprimido` | `boolean` | sí | _Por documentar_ |  |
| 18 | `ruta_servidor_g` | `character varying(500)` | sí | _Por documentar_ |  |
| 19 | `sincronizado_servidor_g` | `boolean` | sí | _Por documentar_ |  |
| 20 | `fecha_sincronizacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 21 | `tipo_reporte` | `character varying(100)` | sí | _Por documentar_ |  |
| 22 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 23 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 24 | `documento_biblioteca_id` | `uuid` | sí | _Por documentar_ | FK→control_interno.documento.id |
| 25 | `visible_auditoria_id` | `uuid` | sí | _Por documentar_ |  |
| 26 | `etapa_kanban_id` | `uuid` | sí | ID de la etapa en tabla etapa_kanban (FK lógica - estable aunque cambie el nombre) | ↝control_interno.etapa_kanban.id |
| 27 | `etapa_kanban_nombre` | `character varying(255)` | sí | Nombre de la etapa al momento de guardar (snapshot para mostrar aunque cambie la configuración) |  |
| 28 | `plan_anual_vigencia` | `integer` | sí | Año de vigencia del plan anual (plantillas de biblioteca) |  |
| 29 | `plan_anual_id` | `uuid` | sí | UUID del plan anual 5 roles asociado |  |

## documento_aprobacion

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `aprobacion_id` → `control_interno.aprobacion` (0..1 → 1); `documento_id` → `control_interno.documento` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `aprobacion_id` | `uuid` | no | _Por documentar_ | FK→control_interno.aprobacion.id |
| 3 | `documento_id` | `uuid` | sí | _Por documentar_ | FK→control_interno.documento.id |
| 4 | `nombre_archivo` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `ruta_archivo` | `character varying(500)` | sí | _Por documentar_ |  |
| 6 | `tipo_mime` | `character varying(100)` | sí | _Por documentar_ |  |
| 7 | `tamanio_bytes` | `bigint` | sí | _Por documentar_ |  |
| 8 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## documento_plan_mejoramiento

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `accion_id` → `control_interno.accion_correctiva` (0..1 → 0..1); `plan_mejoramiento_id` → `control_interno.plan_mejoramiento` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `plan_mejoramiento_id` | `uuid` | no | _Por documentar_ | FK→control_interno.plan_mejoramiento.id |
| 3 | `accion_id` | `uuid` | sí | _Por documentar_ | FK→control_interno.accion_correctiva.id |
| 4 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 6 | `tipo_documento` | `character varying(100)` | no | _Por documentar_ |  |
| 7 | `ruta_archivo` | `character varying(500)` | no | _Por documentar_ |  |
| 8 | `nombre_archivo_original` | `character varying(255)` | no | _Por documentar_ |  |
| 9 | `tipo_mime` | `character varying(100)` | no | _Por documentar_ |  |
| 10 | `tamanio_bytes` | `bigint` | no | _Por documentar_ |  |
| 11 | `subido_por` | `character varying(255)` | no | _Por documentar_ |  |
| 12 | `subido_por_id` | `bigint` | sí | _Por documentar_ |  |
| 13 | `fecha_subida` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 14 | `estado_validacion` | `character varying(50)` | sí | _Por documentar_ |  |
| 15 | `comentarios_auditor` | `text` | sí | _Por documentar_ |  |
| 16 | `fecha_validacion` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 17 | `validado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 18 | `solicita_nueva_evidencia` | `boolean` | sí | _Por documentar_ |  |
| 19 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 20 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |

## entrega_informe_ley

Entregas de informes de ley por periodo

- Clave primaria: `id`
- Filas: 0
- Referencia a: `informe_id` → `control_interno.informe_ley` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `informe_id` | `uuid` | no | _Por documentar_ | FK→control_interno.informe_ley.id |
| 3 | `periodo` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `fecha_vencimiento` | `date` | no | _Por documentar_ |  |
| 5 | `fecha_entrega` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 6 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 7 | `archivo_nombre` | `character varying(255)` | sí | _Por documentar_ |  |
| 8 | `archivo_url` | `character varying(500)` | sí | _Por documentar_ |  |
| 9 | `archivo_tamano` | `bigint` | sí | _Por documentar_ |  |
| 10 | `elaborado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 11 | `fecha_elaboracion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `aprobado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 13 | `fecha_aprobacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 14 | `enviado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 15 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 16 | `motivo_rechazo` | `text` | sí | _Por documentar_ |  |
| 17 | `numero_radicado` | `character varying(255)` | sí | _Por documentar_ |  |
| 18 | `fecha_radicacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 19 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 20 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 21 | `estado_workflow` | `character varying(50)` | sí | Estado en el workflow de aprobación |  |
| 22 | `datos_automaticos_poblados` | `boolean` | sí | Indica si los datos automáticos fueron poblados |  |
| 23 | `fecha_generacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 24 | `generado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 25 | `formato_archivo` | `character varying(50)` | sí | _Por documentar_ |  |
| 26 | `plantilla_usada` | `character varying(255)` | sí | _Por documentar_ |  |
| 27 | `version_plantilla` | `character varying(50)` | sí | _Por documentar_ |  |
| 28 | `metadata_generacion` | `jsonb` | sí | Metadatos de la generación: tiempo, tamaño, variables usadas, etc. |  |

## equipo_auditor

Equipo de auditores asignados a una auditoría. Relación N-N entre auditorías y personas.

- Clave primaria: `id`
- Filas: 160
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..* → 1); `persona_id` → `auth.personas` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `auditoria_id` | `uuid` | no | _Por documentar_ | FK→control_interno.auditoria.id |
| 3 | `persona_id` | `uuid` | no | _Por documentar_ | FK→auth.personas.id_person |
| 4 | `rol` | `character varying(100)` | sí | Rol del auditor en esta auditoría específica: Auditor, Auditor Senior, Auditor Junior, Inspector, Profesional Especializado, etc. |  |
| 5 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 6 | `fecha_asignacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 7 | `fecha_retiro` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 8 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 9 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 10 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## especialidades_ocig

_Por documentar._

- Clave primaria: `id`
- Filas: 13

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | _Por documentar_ | PK |
| 2 | `nombre` | `character varying(100)` | no | _Por documentar_ | única |
| 3 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 4 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 5 | `orden` | `integer` | sí | _Por documentar_ |  |
| 6 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 7 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## etapa_auditoria

Etapas de ejecución de auditorías

- Clave primaria: `id`
- Filas: 0
- Referencia a: `auditoria_id` → `control_interno.auditoria_programada` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `auditoria_id` | `uuid` | no | _Por documentar_ | FK→control_interno.auditoria_programada.id |
| 3 | `etapa` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 5 | `fecha_inicio` | `date` | no | _Por documentar_ |  |
| 6 | `fecha_fin` | `date` | sí | _Por documentar_ |  |
| 7 | `fecha_limite` | `date` | no | _Por documentar_ |  |
| 8 | `datos` | `jsonb` | no | _Por documentar_ |  |
| 9 | `porcentaje_avance` | `integer` | sí | _Por documentar_ |  |
| 10 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## etapa_kanban

Etapas configuradas para cada tablero Kanban

- Clave primaria: `id`
- Filas: 12
- Referencia a: `tablero_kanban_id` → `control_interno.tablero_kanban` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `tablero_kanban_id` | `uuid` | no | _Por documentar_ | FK→control_interno.tablero_kanban.id |
| 3 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `orden` | `integer` | no | _Por documentar_ |  |
| 6 | `color` | `character varying(7)` | no | _Por documentar_ |  |
| 7 | `tiempo_sla` | `integer` | no | Tiempo SLA en días hábiles para esta etapa |  |
| 8 | `limite_wip` | `integer` | sí | Límite de elementos en progreso (null = sin límite) |  |
| 9 | `visible` | `boolean` | no | _Por documentar_ |  |
| 10 | `notificar_vencimiento` | `boolean` | no | _Por documentar_ |  |
| 11 | `dias_anticipacion_alerta` | `integer` | no | _Por documentar_ |  |
| 12 | `estado` | `character varying(20)` | no | Estado de la etapa: inicial, intermedia o final |  |
| 13 | `permitir_retroceso` | `boolean` | no | _Por documentar_ |  |
| 14 | `created_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 15 | `updated_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 16 | `deleted_at` | `timestamp with time zone` | sí | _Por documentar_ |  |

## evaluacion_proceso

Evaluaciones DAFP de procesos auditables. Cada proceso puede tener múltiples evaluaciones con diferentes vigencias/fechas de corte.

- Clave primaria: `id`
- Filas: 54
- Referencia a: `proceso_id` → `control_interno.proceso_auditable` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `proceso_id` | `uuid` | no | FK al proceso maestro del catálogo | FK→control_interno.proceso_auditable.id |
| 3 | `vigencia` | `integer` | no | Año de la evaluación (ej: 2025, 2026) |  |
| 4 | `fecha_corte` | `date` | no | Fecha de corte para la evaluación |  |
| 5 | `dependencia_responsable` | `text` | no | _Por documentar_ |  |
| 6 | `riesgos_extremos` | `integer` | sí | _Por documentar_ |  |
| 7 | `riesgos_altos` | `integer` | sí | _Por documentar_ |  |
| 8 | `riesgos_moderados` | `integer` | sí | _Por documentar_ |  |
| 9 | `riesgos_bajos` | `integer` | sí | _Por documentar_ |  |
| 10 | `total_riesgos` | `integer` | sí | _Por documentar_ |  |
| 11 | `requerimiento_comite` | `boolean` | sí | _Por documentar_ |  |
| 12 | `requerimiento_entes_reg` | `boolean` | sí | _Por documentar_ |  |
| 13 | `fecha_ultima_auditoria` | `date` | sí | _Por documentar_ |  |
| 14 | `resultado_ultima_auditoria` | `character varying(100)` | sí | _Por documentar_ |  |
| 15 | `criticidad` | `integer` | sí | _Por documentar_ |  |
| 16 | `exposicion` | `integer` | sí | _Por documentar_ |  |
| 17 | `mitigantes` | `integer` | sí | _Por documentar_ |  |
| 18 | `score_riesgo` | `integer` | sí | _Por documentar_ |  |
| 19 | `ponderacion_riesgo` | `character varying(20)` | sí | Resultado del cálculo DAFP: EXTREMO, ALTO, MODERADO, BAJO, MUY BAJO |  |
| 20 | `dias_transcurridos` | `integer` | sí | _Por documentar_ |  |
| 21 | `plan_rotacion` | `character varying(20)` | sí | _Por documentar_ |  |
| 22 | `dias_rotacion` | `integer` | sí | _Por documentar_ |  |
| 23 | `decision_rotacion` | `character varying(20)` | sí | _Por documentar_ |  |
| 24 | `decision_final` | `character varying(50)` | sí | Decisión: INCLUIR PLAN ANUAL o AUDITORÍA POSTERIOR |  |
| 25 | `motivo_decision` | `text` | sí | _Por documentar_ |  |
| 26 | `prioridad_regla` | `integer` | sí | _Por documentar_ |  |
| 27 | `creado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 28 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 29 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 30 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
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
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `plan_mejoramiento_id` | `uuid` | no | ID del plan de mejoramiento al que pertenece el evento | FK→control_interno.plan_mejoramiento.id |
| 3 | `tipo` | `control_interno.tipo_evento_timeline` | no | Tipo de evento registrado (creación, actualización, evidencia, etc.) |  |
| 4 | `descripcion` | `text` | no | Descripción legible del evento para mostrar en el timeline |  |
| 5 | `usuario_id` | `uuid` | sí | ID del usuario que generó el evento |  |
| 6 | `usuario_nombre` | `character varying(255)` | sí | Nombre del usuario que generó el evento (desnormalizado para histórico) |  |
| 7 | `fecha` | `timestamp with time zone` | no | Fecha y hora en que ocurrió el evento |  |
| 8 | `metadata` | `jsonb` | sí | Información adicional del evento en formato JSON (IDs relacionados, valores anteriores/nuevos, etc.) |  |
| 9 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |

## evidencia_accion

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `accion_id` → `control_interno.accion_correctiva` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `accion_id` | `uuid` | no | _Por documentar_ | FK→control_interno.accion_correctiva.id |
| 3 | `archivo_ref` | `character varying(1000)` | no | _Por documentar_ |  |
| 4 | `archivo_nombre` | `character varying(500)` | no | _Por documentar_ |  |
| 5 | `archivo_tipo` | `character varying(100)` | sí | _Por documentar_ |  |
| 6 | `archivo_tamanio` | `bigint` | sí | _Por documentar_ |  |
| 7 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 8 | `cargada_por_id` | `character varying(255)` | no | _Por documentar_ |  |
| 9 | `cargada_por_nombre` | `character varying(500)` | sí | _Por documentar_ |  |
| 10 | `cargada_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 11 | `estado_validacion` | `character varying(30)` | sí | _Por documentar_ |  |
| 12 | `comentarios` | `text` | sí | _Por documentar_ |  |
| 13 | `solicita_nueva_evidencia` | `boolean` | sí | _Por documentar_ |  |
| 14 | `calificada_por_id` | `character varying(255)` | sí | _Por documentar_ |  |
| 15 | `calificada_por_nombre` | `character varying(500)` | sí | _Por documentar_ |  |
| 16 | `calificada_at` | `timestamp with time zone` | sí | _Por documentar_ |  |

## evidencia_documento

Sistema independiente de gestión de evidencias y documentos vinculados a Hallazgos, Acciones, Planes y Auditorías

- Clave primaria: `id`
- Filas: 48
- Referencia a: `accion_correctiva_id` → `control_interno.accion_correctiva` (0..1 → 0..1); `auditoria_id` → `control_interno.auditoria` (0..* → 0..1); `hallazgo_id` → `control_interno.hallazgo` (0..* → 0..1); `plan_mejoramiento_id` → `control_interno.plan_mejoramiento` (0..1 → 0..1); `version_anterior_id` → `control_interno.evidencia_documento` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(50)` | no | Código único generado automáticamente: EVD-YYYY-NNNN | única |
| 3 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `tipo_documento` | `control_interno.tipo_documento_evidencia` | no | _Por documentar_ |  |
| 6 | `hallazgo_id` | `uuid` | sí | _Por documentar_ | FK→control_interno.hallazgo.id |
| 7 | `accion_correctiva_id` | `uuid` | sí | _Por documentar_ | FK→control_interno.accion_correctiva.id |
| 8 | `plan_mejoramiento_id` | `uuid` | sí | _Por documentar_ | FK→control_interno.plan_mejoramiento.id |
| 9 | `auditoria_id` | `uuid` | sí | _Por documentar_ | FK→control_interno.auditoria.id |
| 10 | `ruta_archivo` | `character varying(500)` | no | _Por documentar_ |  |
| 11 | `nombre_archivo_original` | `character varying(255)` | no | _Por documentar_ |  |
| 12 | `tipo_mime` | `character varying(100)` | no | _Por documentar_ |  |
| 13 | `tamanio_bytes` | `bigint` | no | _Por documentar_ |  |
| 14 | `hash_archivo` | `character varying(255)` | sí | Hash SHA256 del archivo para verificar integridad |  |
| 15 | `version` | `integer` | sí | _Por documentar_ |  |
| 16 | `version_anterior_id` | `uuid` | sí | Referencia a la versión anterior para mantener historial | FK→control_interno.evidencia_documento.id |
| 17 | `es_version_actual` | `boolean` | sí | _Por documentar_ |  |
| 18 | `estado_validacion` | `control_interno.estado_validacion_evidencia` | sí | Estado de validación por auditor (US-032): pendiente, aceptado, rechazado, con_observaciones |  |
| 19 | `validado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 20 | `fecha_validacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 21 | `observaciones_validacion` | `text` | sí | _Por documentar_ |  |
| 22 | `subido_por` | `character varying(255)` | no | _Por documentar_ |  |
| 23 | `subido_por_id` | `bigint` | sí | _Por documentar_ |  |
| 24 | `fecha_subida` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 25 | `ruta_servidor_g` | `character varying(500)` | sí | _Por documentar_ |  |
| 26 | `sincronizado_servidor_g` | `boolean` | sí | _Por documentar_ |  |
| 27 | `fecha_sincronizacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 28 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 29 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## hallazgo

Hallazgos identificados en las auditorías

- Clave primaria: `id`
- Filas: 34
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `categoria` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `estado` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `area` | `character varying(255)` | no | _Por documentar_ |  |
| 6 | `auditoria` | `character varying(255)` | no | _Por documentar_ |  |
| 7 | `auditoria_id` | `uuid` | sí | _Por documentar_ | FK→control_interno.auditoria.id |
| 8 | `descripcion` | `text` | no | _Por documentar_ |  |
| 9 | `criterio_incumplido` | `text` | no | _Por documentar_ |  |
| 10 | `normativa_relacionada` | `jsonb` | no | _Por documentar_ |  |
| 11 | `evidencias` | `jsonb` | no | _Por documentar_ |  |
| 12 | `recomendaciones` | `jsonb` | no | _Por documentar_ |  |
| 13 | `fecha_deteccion` | `date` | no | _Por documentar_ |  |
| 14 | `fecha_notificacion` | `date` | sí | _Por documentar_ |  |
| 15 | `responsable` | `character varying(255)` | sí | _Por documentar_ |  |
| 16 | `fecha_limite_correccion` | `date` | sí | _Por documentar_ |  |
| 17 | `observaciones_controversia` | `text` | sí | _Por documentar_ |  |
| 18 | `titulo` | `character varying(500)` | sí | _Por documentar_ |  |
| 19 | `gravedad` | `character varying(20)` | sí | _Por documentar_ |  |
| 20 | `fecha_compromiso` | `date` | sí | _Por documentar_ |  |
| 21 | `progreso_cumplimiento` | `integer` | sí | _Por documentar_ |  |
| 22 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 23 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
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
| 34 | `controversia_turno` | `character varying(50)` | sí | _Por documentar_ |  |

## historial_auditoria

Historial completo de cambios y eventos de una auditoría. Trazabilidad completa de todas las acciones. El campo cambios almacena un array JSONB con formato: [{"campo": "Progreso", "valorAnterior": "10%", "valorNuevo": "15%"}]

- Clave primaria: `id`
- Filas: 480
- Referencia a: `auditoria_id` → `control_interno.auditoria` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `auditoria_id` | `uuid` | no | _Por documentar_ | FK→control_interno.auditoria.id |
| 3 | `tipo_evento` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `fecha` | `date` | no | _Por documentar_ |  |
| 5 | `hora` | `time without time zone` | no | _Por documentar_ |  |
| 6 | `accion` | `character varying(255)` | no | _Por documentar_ |  |
| 7 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 8 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 9 | `documento_adjunto` | `character varying(500)` | sí | _Por documentar_ |  |
| 10 | `ip_address` | `character varying(45)` | sí | _Por documentar_ | Identificador en línea (IP) |
| 11 | `user_agent` | `text` | sí | _Por documentar_ |  |
| 12 | `cambios` | `jsonb` | sí | Array JSONB de cambios realizados. Formato: [{"campo": string, "valorAnterior": string, "valorNuevo": string}]. Ejemplo: [{"campo": "Progreso", "valorAnterior": "10%", "valorNuevo": "15%"}] |  |
| 13 | `estado_anterior` | `character varying(50)` | sí | _Por documentar_ |  |
| 14 | `estado_nuevo` | `character varying(50)` | sí | _Por documentar_ |  |
| 15 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 16 | `usuario_id` | `uuid` | sí | _Por documentar_ |  |
| 17 | `nombre_usuario` | `character varying(255)` | sí | Nombre completo del usuario que realizó la acción (desnormalizado para auditoría) |  |
| 18 | `user_email` | `character varying(255)` | sí | Email del usuario que realizó la acción (desnormalizado para auditoría) | Contacto |

## historial_generacion_informe

Auditoría completa de generación y aprobación de informes

- Clave primaria: `id`
- Filas: 0
- Referencia a: `entrega_id` → `control_interno.entrega_informe_ley` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `entrega_id` | `uuid` | no | _Por documentar_ | FK→control_interno.entrega_informe_ley.id |
| 3 | `accion` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `usuario_id` | `character varying(255)` | sí | _Por documentar_ |  |
| 5 | `usuario_nombre` | `character varying(255)` | sí | _Por documentar_ |  |
| 6 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 7 | `datos_anteriores` | `jsonb` | sí | _Por documentar_ |  |
| 8 | `datos_nuevos` | `jsonb` | sí | _Por documentar_ |  |
| 9 | `ip_origen` | `character varying(50)` | sí | _Por documentar_ | Identificador en línea (IP) |
| 10 | `user_agent` | `text` | sí | _Por documentar_ |  |
| 11 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## historial_plan_anual

Historial de cambios y auditoría del Plan Anual 5 Roles. Registra todas las operaciones CRUD para trazabilidad y compliance.

- Clave primaria: `id`
- Filas: 29731
- Referencia a: `plan_id` → `control_interno.plan_anual_5_roles` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `plan_id` | `uuid` | no | _Por documentar_ | FK→control_interno.plan_anual_5_roles.id |
| 3 | `tipo_evento` | `character varying(50)` | no | Tipo de evento: creacion, actualizacion, aprobacion, actividad_creada, actividad_actualizada, actividad_eliminada, cambio_estado |  |
| 4 | `fecha` | `date` | no | _Por documentar_ |  |
| 5 | `hora` | `time without time zone` | no | _Por documentar_ |  |
| 6 | `usuario_id` | `uuid` | sí | FK a auth.personas(id_tercero) - Usuario que realizó la acción |  |
| 7 | `accion` | `character varying(255)` | no | _Por documentar_ |  |
| 8 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 9 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 10 | `ip_address` | `character varying(45)` | sí | Dirección IP del usuario que realizó la acción | Identificador en línea (IP) |
| 11 | `user_agent` | `text` | sí | User agent del navegador del usuario |  |
| 12 | `cambios` | `jsonb` | sí | Array JSONB con formato [{campo: string, valorAnterior: string, valorNuevo: string}] |  |
| 13 | `estado_anterior` | `character varying(50)` | sí | _Por documentar_ |  |
| 14 | `estado_nuevo` | `character varying(50)` | sí | _Por documentar_ |  |
| 15 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## informe_ley

Informes normativos requeridos por ley (RF012)

- Clave primaria: `id`
- Filas: 16

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | no | _Por documentar_ |  |
| 5 | `tipo` | `character varying(50)` | sí | _Por documentar_ |  |
| 6 | `periodicidad` | `character varying(50)` | no | _Por documentar_ |  |
| 7 | `fecha_vencimiento` | `date` | sí | _Por documentar_ |  |
| 8 | `estado` | `character varying(50)` | sí | _Por documentar_ |  |
| 9 | `dias_restantes` | `integer` | sí | _Por documentar_ |  |
| 10 | `alerta` | `character varying(50)` | sí | _Por documentar_ |  |
| 11 | `area` | `character varying(255)` | no | _Por documentar_ |  |
| 12 | `responsable` | `character varying(255)` | no | _Por documentar_ |  |
| 13 | `normativa` | `text` | sí | _Por documentar_ |  |
| 14 | `acciones_sugeridas` | `jsonb` | sí | _Por documentar_ |  |
| 15 | `historial` | `jsonb` | sí | _Por documentar_ |  |
| 16 | `proximo_recordatorio` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 17 | `recordatorios_enviados` | `integer` | sí | _Por documentar_ |  |
| 18 | `formato_template` | `character varying(255)` | sí | _Por documentar_ |  |
| 19 | `datos_integrados` | `jsonb` | sí | _Por documentar_ |  |
| 20 | `codigo_corto` | `character varying(50)` | sí | _Por documentar_ | única |
| 21 | `categoria` | `character varying(100)` | sí | _Por documentar_ |  |
| 22 | `dia_presentacion` | `integer` | sí | _Por documentar_ |  |
| 23 | `entidad_destino` | `character varying(500)` | sí | _Por documentar_ |  |
| 24 | `area_responsable` | `character varying(255)` | sí | _Por documentar_ |  |
| 25 | `tiene_plantilla` | `boolean` | sí | _Por documentar_ |  |
| 26 | `url_plantilla` | `character varying(500)` | sí | _Por documentar_ |  |
| 27 | `requiere_aprobacion` | `boolean` | sí | _Por documentar_ |  |
| 28 | `dias_anticipacion_alerta` | `integer` | sí | _Por documentar_ |  |
| 29 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 30 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 31 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## integraciones_esap

Configuración de integraciones externas

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 3 | `tipo` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `configuracion` | `jsonb` | no | _Por documentar_ |  |
| 5 | `activa` | `boolean` | sí | _Por documentar_ |  |
| 6 | `ultima_sincronizacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 7 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 8 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## item_lista_chequeo

Items individuales de una lista de chequeo

- Clave primaria: `id`
- Filas: 109
- Referencia a: `lista_chequeo_id` → `control_interno.lista_chequeo` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `lista_chequeo_id` | `uuid` | no | _Por documentar_ | FK→control_interno.lista_chequeo.id |
| 3 | `texto` | `text` | no | Texto del item de verificación |  |
| 4 | `categoria` | `character varying(100)` | no | Categoría del item (opcional) |  |
| 5 | `obligatorio` | `boolean` | no | Indica si el item es obligatorio |  |
| 6 | `orden` | `integer` | no | Orden de visualización del item |  |
| 7 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 8 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |
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
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `lista_chequeo_id` | `uuid` | no | _Por documentar_ |  |
| 3 | `lista_chequeo_codigo` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `lista_chequeo_nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `auditoria_id` | `character varying(255)` | no | _Por documentar_ |  |
| 6 | `fecha_aplicacion` | `date` | no | _Por documentar_ |  |
| 7 | `aplicado_por` | `character varying(255)` | no | _Por documentar_ |  |
| 8 | `respuestas` | `jsonb` | no | _Por documentar_ |  |
| 9 | `resultado` | `jsonb` | no | _Por documentar_ |  |
| 10 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## lista_chequeo

Listas de chequeo configurables para auditorías

- Clave primaria: `id`
- Filas: 71
- Referencia a: `tipo_auditoria_id` → `control_interno.tipo_auditoria` (0..* → 0..1)
- Relaciones implícitas: `etapa_kanban_id` ↝ `control_interno.etapa_kanban` (100.0 % con padre)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(255)` | no | Código único de la lista (ej: LC-ADM-001) | única |
| 3 | `nombre` | `character varying(255)` | no | Nombre descriptivo de la lista de chequeo |  |
| 4 | `descripcion` | `text` | sí | Descripción de la lista de chequeo |  |
| 5 | `categoria` | `character varying(100)` | sí | Categoría de la lista de chequeo (obligatoria) |  |
| 6 | `tipo` | `character varying(100)` | no | Tipo de lista de chequeo: planeacion, ejecucion o comunicacion |  |
| 7 | `tipo_auditoria_id` | `uuid` | sí | Tipo de auditoría asociado (opcional) | FK→control_interno.tipo_auditoria.id |
| 8 | `activa` | `boolean` | no | Indica si la lista está activa y disponible |  |
| 9 | `usos_programados` | `integer` | no | Contador de usos programados con esta lista |  |
| 10 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 11 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 12 | `deleted_at` | `timestamp without time zone` | sí | Fecha de eliminación (soft delete) |  |
| 13 | `auditoria_id` | `uuid` | sí | _Por documentar_ |  |
| 14 | `nombre_auditoria` | `character varying(500)` | sí | _Por documentar_ |  |
| 15 | `auditor_responsable` | `character varying(255)` | sí | _Por documentar_ |  |
| 16 | `fecha_aplicacion` | `date` | sí | _Por documentar_ |  |
| 17 | `fecha_diligenciamiento` | `date` | sí | _Por documentar_ |  |
| 18 | `items_completados` | `integer` | sí | _Por documentar_ |  |
| 19 | `cumplimiento` | `integer` | sí | _Por documentar_ |  |
| 20 | `no_cumplimientos` | `integer` | sí | _Por documentar_ |  |
| 21 | `no_aplica` | `integer` | sí | _Por documentar_ |  |
| 22 | `hallazgos_generados` | `integer` | sí | _Por documentar_ |  |
| 23 | `version` | `character varying(50)` | sí | _Por documentar_ |  |
| 24 | `estado` | `character varying(50)` | sí | _Por documentar_ |  |
| 25 | `aplicable_para` | `jsonb` | sí | _Por documentar_ |  |
| 26 | `created_by` | `character varying(255)` | sí | _Por documentar_ |  |
| 27 | `items_json` | `jsonb` | sí | _Por documentar_ |  |
| 28 | `proceso` | `character varying(255)` | sí | _Por documentar_ |  |
| 29 | `subproceso` | `character varying(255)` | sí | _Por documentar_ |  |
| 30 | `categoria_esap` | `character varying(100)` | sí | _Por documentar_ |  |
| 31 | `normativa_aplicable` | `text` | sí | _Por documentar_ |  |
| 32 | `objetivo` | `text` | sí | _Por documentar_ |  |
| 33 | `version_base` | `character varying(50)` | sí | _Por documentar_ |  |
| 34 | `permite_no_aplica` | `boolean` | sí | _Por documentar_ |  |
| 35 | `requiere_evidencias` | `boolean` | sí | _Por documentar_ |  |
| 36 | `genera_hallazgos_automaticos` | `boolean` | sí | _Por documentar_ |  |
| 37 | `fase_planeacion` | `boolean` | sí | _Por documentar_ |  |
| 38 | `fase_ejecucion` | `boolean` | sí | _Por documentar_ |  |
| 39 | `fase_comunicacion` | `boolean` | sí | _Por documentar_ |  |
| 40 | `fase_seguimiento` | `boolean` | sí | _Por documentar_ |  |
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
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `usuario_id` | `uuid` | sí | _Por documentar_ | FK→control_interno.usuarios_esap.id |
| 3 | `accion` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `entidad` | `character varying(255)` | sí | _Por documentar_ |  |
| 5 | `entidad_id` | `uuid` | sí | _Por documentar_ |  |
| 6 | `detalles` | `jsonb` | sí | _Por documentar_ |  |
| 7 | `ip_address` | `character varying(45)` | sí | _Por documentar_ | Identificador en línea (IP) |
| 8 | `user_agent` | `text` | sí | _Por documentar_ |  |
| 9 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## normatividad_aplicable

Normatividad aplicable a la auditoría (decretos, leyes, manuales, políticas)

- Clave primaria: `id`
- Filas: 0
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `auditoria_id` | `uuid` | no | _Por documentar_ | FK→control_interno.auditoria.id |
| 3 | `normatividad` | `text` | no | _Por documentar_ |  |
| 4 | `tipo` | `character varying(100)` | sí | _Por documentar_ |  |
| 5 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 6 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 7 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## nota_auditoria

Notas y observaciones de las auditorías. Similar a un sistema de comentarios con categorización. Las notas marcadas como importantes (importante=true) aparecen destacadas en amarillo.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..1 → 1); `autor_id` → `auth.personas` (0..1 → 1); `editor_id` → `auth.personas` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `auditoria_id` | `uuid` | no | _Por documentar_ | FK→control_interno.auditoria.id |
| 3 | `contenido` | `text` | no | _Por documentar_ |  |
| 4 | `categoria` | `character varying(50)` | no | Categoría de la nota: General, Hallazgo, Seguimiento, Evidencia, Recomendación, Observación |  |
| 5 | `autor_id` | `uuid` | no | _Por documentar_ | FK→auth.personas.id_person |
| 6 | `fecha` | `date` | no | _Por documentar_ |  |
| 7 | `hora` | `time without time zone` | no | _Por documentar_ |  |
| 8 | `importante` | `boolean` | sí | Si es true, la nota se marca como importante y aparece destacada con fondo amarillo en el frontend |  |
| 9 | `editada` | `boolean` | sí | _Por documentar_ |  |
| 10 | `fecha_edicion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `editor_id` | `uuid` | sí | _Por documentar_ | FK→auth.personas.id_person |
| 12 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 13 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## notificacion

Sistema de notificaciones (RF014)

- Clave primaria: `id`
- Filas: 945

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `usuario_id` | `character varying(255)` | no | _Por documentar_ |  |
| 3 | `tipo_notificacion` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `titulo` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `mensaje` | `text` | no | _Por documentar_ |  |
| 6 | `estado` | `character varying(50)` | sí | _Por documentar_ |  |
| 7 | `canal` | `character varying(50)` | sí | _Por documentar_ |  |
| 8 | `leida` | `boolean` | sí | _Por documentar_ |  |
| 9 | `fecha_lectura` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 10 | `enviada_email` | `boolean` | sí | _Por documentar_ |  |
| 11 | `fecha_envio_email` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `metadata` | `jsonb` | sí | _Por documentar_ |  |
| 13 | `accion_url` | `character varying(500)` | sí | _Por documentar_ |  |
| 14 | `prioridad` | `character varying(20)` | sí | _Por documentar_ |  |
| 15 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 16 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## objetivo_auditoria

Objetivos específicos de cada auditoría. Cada auditoría puede tener múltiples objetivos.

- Clave primaria: `id`
- Filas: 39
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `auditoria_id` | `uuid` | no | _Por documentar_ | FK→control_interno.auditoria.id |
| 3 | `descripcion` | `text` | no | _Por documentar_ |  |
| 4 | `orden` | `integer` | sí | _Por documentar_ |  |
| 5 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 6 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 7 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## parametro_sistema

Parámetros de configuración del sistema (RF020)

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `clave` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `valor` | `text` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `tipo` | `character varying(50)` | sí | _Por documentar_ |  |
| 6 | `categoria` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `editable` | `boolean` | sí | _Por documentar_ |  |
| 8 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## paso_workflow_informe

Pasos individuales del workflow de aprobación

- Clave primaria: `id`
- Filas: 0
- Referencia a: `workflow_id` → `control_interno.workflow_aprobacion_informe` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `workflow_id` | `uuid` | no | _Por documentar_ | FK→control_interno.workflow_aprobacion_informe.id |
| 3 | `numero_paso` | `integer` | no | _Por documentar_ |  |
| 4 | `nombre` | `character varying(100)` | no | _Por documentar_ |  |
| 5 | `nombre_display` | `character varying(255)` | no | _Por documentar_ |  |
| 6 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 7 | `responsable` | `character varying(255)` | sí | _Por documentar_ |  |
| 8 | `rol_responsable` | `character varying(255)` | sí | _Por documentar_ |  |
| 9 | `estado` | `character varying(50)` | sí | _Por documentar_ |  |
| 10 | `fecha_inicio` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `fecha_fin` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 13 | `accion` | `character varying(50)` | sí | _Por documentar_ |  |
| 14 | `es_obligatorio` | `boolean` | sí | _Por documentar_ |  |
| 15 | `orden` | `integer` | no | _Por documentar_ |  |
| 16 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 17 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## plan_anual

Planes anuales de auditoría

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `año` | `integer` | no | _Por documentar_ |  |
| 3 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `estado` | `character varying(50)` | sí | _Por documentar_ |  |
| 5 | `fecha_creacion` | `date` | no | _Por documentar_ |  |
| 6 | `fecha_aprobacion` | `date` | sí | _Por documentar_ |  |
| 7 | `creado_por` | `character varying(255)` | no | _Por documentar_ |  |
| 8 | `version` | `character varying(50)` | sí | _Por documentar_ |  |
| 9 | `total_actividades` | `integer` | sí | _Por documentar_ |  |
| 10 | `actividades_completadas` | `integer` | sí | _Por documentar_ |  |
| 11 | `porcentaje_cumplimiento` | `integer` | sí | _Por documentar_ |  |
| 12 | `enfoques` | `jsonb` | sí | _Por documentar_ |  |
| 13 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## plan_anual_5_roles

_Por documentar._

- Clave primaria: `id`
- Filas: 63

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `ano` | `integer` | no | _Por documentar_ | única |
| 3 | `fecha_creacion` | `date` | no | _Por documentar_ |  |
| 4 | `responsable` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `estado` | `character varying(50)` | no | Estado del plan anual: borrador, en-revision, aprobado, en-ejecucion, completado |  |
| 6 | `porcentaje_cumplimiento_general` | `integer` | sí | _Por documentar_ |  |
| 7 | `total_actividades` | `integer` | sí | _Por documentar_ |  |
| 8 | `actividades_completadas` | `integer` | sí | _Por documentar_ |  |
| 9 | `actividades_en_progreso` | `integer` | sí | _Por documentar_ |  |
| 10 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `fecha_inicio` | `date` | sí | Fecha de inicio del periodo de ejecución del plan anual |  |
| 13 | `fecha_fin` | `date` | sí | Fecha de finalización del periodo de ejecución del plan anual |  |
| 14 | `responsable_id` | `uuid` | sí | UUID del profesional OCIG responsable/líder del plan (FK a configuracion_profesionales_ocig) |  |
| 15 | `equipo_aprobacion` | `jsonb` | sí | _Por documentar_ |  |
| 16 | `orden_aprobacion` | `character varying(20)` | sí | _Por documentar_ |  |
| 17 | `firma_activacion` | `jsonb` | sí | _Por documentar_ |  |

## plan_anual_wizard_borrador

_Por documentar._

- Clave primaria: `id`
- Filas: 2

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `usuario_id` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `payload` | `jsonb` | no | _Por documentar_ |  |
| 4 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 5 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |

## plan_individual

Planes individuales de auditoría

- Clave primaria: `id`
- Filas: 0
- Referencia a: `auditoria_id` → `control_interno.auditoria_programada` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `auditoria_id` | `uuid` | no | _Por documentar_ | FK→control_interno.auditoria_programada.id |
| 4 | `auditoria_codigo` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 6 | `alcance` | `text` | no | _Por documentar_ |  |
| 7 | `objetivo` | `text` | no | _Por documentar_ |  |
| 8 | `proceso_auditar` | `character varying(255)` | no | _Por documentar_ |  |
| 9 | `riesgos` | `jsonb` | no | _Por documentar_ |  |
| 10 | `criterios_auditoria` | `jsonb` | no | _Por documentar_ |  |
| 11 | `normativa_aplicable` | `jsonb` | no | _Por documentar_ |  |
| 12 | `equipo_auditor` | `jsonb` | no | _Por documentar_ |  |
| 13 | `documentos` | `jsonb` | no | _Por documentar_ |  |
| 14 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 15 | `fecha_creacion` | `date` | no | _Por documentar_ |  |
| 16 | `fecha_envio` | `date` | sí | _Por documentar_ |  |
| 17 | `enviado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 18 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 19 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## plan_mejoramiento

Planes de mejoramiento derivados de hallazgos

- Clave primaria: `id`
- Filas: 14
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..1 → 0..1); `hallazgo_id` → `control_interno.hallazgo` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `hallazgo_id` | `uuid` | sí | _Por documentar_ | FK→control_interno.hallazgo.id |
| 4 | `hallazgo_codigo` | `character varying(255)` | sí | _Por documentar_ |  |
| 5 | `auditoria_id` | `uuid` | sí | _Por documentar_ | FK→control_interno.auditoria.id |
| 6 | `titulo` | `character varying(255)` | no | _Por documentar_ |  |
| 7 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 8 | `objetivos` | `jsonb` | no | _Por documentar_ |  |
| 9 | `area_responsable` | `character varying(255)` | no | _Por documentar_ |  |
| 10 | `responsable_implementacion` | `character varying(255)` | no | _Por documentar_ |  |
| 11 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 12 | `fecha_creacion` | `date` | sí | _Por documentar_ |  |
| 13 | `fecha_aprobacion` | `date` | sí | _Por documentar_ |  |
| 14 | `fecha_inicio_ejecucion` | `date` | sí | _Por documentar_ |  |
| 15 | `fecha_limite` | `date` | no | _Por documentar_ |  |
| 16 | `fecha_cierre` | `date` | sí | _Por documentar_ |  |
| 17 | `recursos` | `jsonb` | sí | _Por documentar_ |  |
| 18 | `indicadores` | `jsonb` | sí | _Por documentar_ |  |
| 19 | `avance_global` | `integer` | sí | _Por documentar_ |  |
| 20 | `aprobado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 21 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 22 | `observaciones_aprobacion` | `text` | sí | _Por documentar_ |  |
| 23 | `motivo_rechazo` | `text` | sí | _Por documentar_ |  |
| 24 | `seguimientos` | `jsonb` | sí | _Por documentar_ |  |
| 25 | `codigo_auditoria` | `character varying(255)` | sí | _Por documentar_ |  |
| 26 | `porcentaje_efectividad` | `integer` | sí | _Por documentar_ |  |
| 27 | `seguimientos_realizados` | `integer` | sí | _Por documentar_ |  |
| 28 | `seguimientos_totales` | `integer` | sí | _Por documentar_ |  |
| 29 | `proximo_seguimiento` | `date` | sí | _Por documentar_ |  |
| 30 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 31 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## plantilla_email

Plantillas de correo electrónico (RF020)

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `asunto` | `character varying(500)` | no | _Por documentar_ |  |
| 5 | `cuerpo` | `text` | no | _Por documentar_ |  |
| 6 | `variables_disponibles` | `jsonb` | sí | _Por documentar_ |  |
| 7 | `activa` | `boolean` | sí | _Por documentar_ |  |
| 8 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## plantilla_informe_ley

Plantillas para generación automática de informes de ley

- Clave primaria: `id`
- Filas: 16

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `tipo_formato` | `character varying(50)` | no | _Por documentar_ |  |
| 6 | `ruta_plantilla` | `character varying(500)` | no | _Por documentar_ |  |
| 7 | `variables_disponibles` | `jsonb` | sí | Variables disponibles en la plantilla. Las marcadas como requeridas deben estar presentes. |  |
| 8 | `estructura_datos` | `jsonb` | sí | Estructura esperada de datos. Campos con "requerido": false son opcionales. |  |
| 9 | `activa` | `boolean` | sí | _Por documentar_ |  |
| 10 | `version` | `character varying(50)` | sí | _Por documentar_ |  |
| 11 | `creado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 12 | `actualizado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 13 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## plantilla_reporte

Plantillas para generación de reportes

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `tipo` | `character varying(100)` | no | _Por documentar_ |  |
| 5 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 6 | `formato` | `character varying(50)` | no | _Por documentar_ |  |
| 7 | `ruta_template` | `character varying(500)` | sí | _Por documentar_ |  |
| 8 | `variables_disponibles` | `jsonb` | sí | _Por documentar_ |  |
| 9 | `activa` | `boolean` | sí | _Por documentar_ |  |
| 10 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## plantillas_documentos_esap

Plantillas de documentos personalizadas

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `tipo_documento` | `character varying(100)` | no | _Por documentar_ |  |
| 6 | `contenido` | `text` | no | _Por documentar_ |  |
| 7 | `variables_disponibles` | `jsonb` | sí | _Por documentar_ |  |
| 8 | `activa` | `boolean` | sí | _Por documentar_ |  |
| 9 | `version` | `integer` | sí | _Por documentar_ |  |
| 10 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## preferencia_notificacion

Preferencias de notificación por usuario (RF014)

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `usuario_id` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `notificaciones_email` | `boolean` | sí | _Por documentar_ |  |
| 4 | `notificaciones_sistema` | `boolean` | sí | _Por documentar_ |  |
| 5 | `tipos_notificacion` | `jsonb` | sí | _Por documentar_ |  |
| 6 | `frecuencia_recordatorios` | `character varying(50)` | sí | _Por documentar_ |  |
| 7 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 8 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 9 | `horario_preferido` | `character varying(50)` | sí | Horario preferido del usuario para recibir notificaciones |  |

## proceso_auditable

Procesos auditables del universo de auditorías

- Clave primaria: `id`
- Filas: 36
- Referencia a: `tipo_proceso_id` → `control_interno.tipo_proceso` (1..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | no | _Por documentar_ |  |
| 5 | `tipo` | `character varying(50)` | no | _Por documentar_ |  |
| 6 | `macroproceso` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `responsable` | `character varying(255)` | no | _Por documentar_ |  |
| 8 | `dependencia` | `character varying(255)` | no | _Por documentar_ |  |
| 9 | `territorial` | `character varying(255)` | sí | _Por documentar_ |  |
| 10 | `evaluacion_riesgo` | `jsonb` | no | _Por documentar_ |  |
| 11 | `frecuencia_auditoria` | `character varying(255)` | no | _Por documentar_ |  |
| 12 | `ultima_auditoria` | `date` | sí | _Por documentar_ |  |
| 13 | `proxima_auditoria` | `date` | sí | _Por documentar_ |  |
| 14 | `prioridad` | `integer` | no | _Por documentar_ |  |
| 15 | `priorizacion_anos` | `integer` | no | _Por documentar_ |  |
| 16 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 17 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 18 | `resultado_ultima_auditoria` | `character varying(255)` | sí | Resultado de la última auditoría realizada (Adecuado, Con observaciones, etc.) |  |
| 19 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 20 | `unidades_auditables` | `jsonb` | sí | _Por documentar_ |  |
| 21 | `tipo_proceso_id` | `uuid` | sí | Relación al catálogo control_interno.tipo_proceso | FK→control_interno.tipo_proceso.id |
| 22 | `es_especial` | `boolean` | no | Proceso Especial (EFDS-1923): va directo a Programación sin pasar por Universo Auditable. El subtipo lo determina tipo_proceso_id. |  |

## programa_anual_ajuste

Ajustes del Programa Anual (EFDS-1919): borrador de la siguiente versión; la versión que se genera lo cierra.

- Clave primaria: `id`
- Filas: 3

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `vigencia` | `integer` | no | _Por documentar_ |  |
| 3 | `iniciado_por` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `iniciado_por_id` | `character varying(64)` | sí | _Por documentar_ |  |
| 5 | `iniciado_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 6 | `cerrado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 7 | `version_resultante` | `integer` | sí | _Por documentar_ |  |

## registro_seguimiento

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `accion_id` → `control_interno.accion_correctiva` (0..1 → 1); `seguimiento_id` → `control_interno.seguimiento_trimestral` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `accion_id` | `uuid` | no | _Por documentar_ | FK→control_interno.accion_correctiva.id |
| 3 | `seguimiento_id` | `uuid` | no | _Por documentar_ | FK→control_interno.seguimiento_trimestral.id |
| 4 | `accion_descripcion` | `text` | no | _Por documentar_ |  |
| 5 | `acciones_programadas` | `integer` | sí | _Por documentar_ |  |
| 6 | `acciones_implementadas` | `integer` | sí | _Por documentar_ |  |
| 7 | `puntaje_cumplimiento` | `integer` | sí | _Por documentar_ |  |
| 8 | `controles_implementados` | `character varying(20)` | no | _Por documentar_ |  |
| 9 | `hallazgo_se_repite` | `character varying(20)` | no | _Por documentar_ |  |
| 10 | `puntaje_efectividad` | `integer` | sí | _Por documentar_ |  |
| 11 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 12 | `evidencias` | `jsonb` | sí | _Por documentar_ |  |
| 13 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## reunion_apertura

Información de la reunión de apertura de la auditoría

- Clave primaria: `id`
- Filas: 15
- Referencia a: `documento_biblioteca_id` → `control_interno.documento` (0..1 → 0..1); `auditoria_id` → `control_interno.auditoria` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `auditoria_id` | `uuid` | no | _Por documentar_ | única FK→control_interno.auditoria.id |
| 3 | `fecha` | `timestamp without time zone` | no | _Por documentar_ |  |
| 4 | `modalidad` | `character varying(50)` | no | _Por documentar_ |  |
| 5 | `lugar` | `character varying(255)` | sí | _Por documentar_ |  |
| 6 | `enlace_virtual` | `character varying(500)` | sí | _Por documentar_ |  |
| 7 | `agenda` | `jsonb` | sí | _Por documentar_ |  |
| 8 | `participantes` | `jsonb` | sí | _Por documentar_ |  |
| 9 | `estado_acta` | `character varying(50)` | sí | _Por documentar_ |  |
| 10 | `acta_ruta` | `character varying(500)` | sí | _Por documentar_ |  |
| 11 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 12 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 13 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 14 | `documento_biblioteca_id` | `uuid` | sí | _Por documentar_ | FK→control_interno.documento.id |
| 15 | `elaborado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 16 | `revisado_por` | `character varying(255)` | sí | _Por documentar_ |  |

## reunion_cierre

Información de la reunión de cierre de la auditoría

- Clave primaria: `id`
- Filas: 11
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..1 → 1); `documento_biblioteca_id` → `control_interno.documento` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `auditoria_id` | `uuid` | no | _Por documentar_ | única FK→control_interno.auditoria.id |
| 3 | `fecha` | `timestamp without time zone` | no | _Por documentar_ |  |
| 4 | `modalidad` | `character varying(50)` | no | _Por documentar_ |  |
| 5 | `lugar` | `character varying(255)` | sí | _Por documentar_ |  |
| 6 | `enlace_virtual` | `character varying(500)` | sí | _Por documentar_ |  |
| 7 | `agenda` | `jsonb` | sí | _Por documentar_ |  |
| 8 | `participantes` | `jsonb` | sí | _Por documentar_ |  |
| 9 | `estado_acta` | `character varying(50)` | sí | _Por documentar_ |  |
| 10 | `acta_ruta` | `character varying(500)` | sí | _Por documentar_ |  |
| 11 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 12 | `elaborado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 13 | `revisado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 14 | `documento_biblioteca_id` | `uuid` | sí | _Por documentar_ | FK→control_interno.documento.id |
| 15 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 16 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## rol_decreto_648

Roles del Decreto 648 configurable (RF020)

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `orden` | `integer` | sí | _Por documentar_ |  |
| 6 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 7 | `editable` | `boolean` | sí | _Por documentar_ |  |
| 8 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## rol_decreto_648_template

_Por documentar._

- Clave primaria: `id`
- Filas: 5

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `rol_numero` | `integer` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | no | _Por documentar_ |  |
| 5 | `color` | `character varying(7)` | no | _Por documentar_ |  |
| 6 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 7 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 8 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## rol_plan_anual

Roles y disponibilidad de auditores en el plan anual

- Clave primaria: `id`
- Filas: 0
- Referencia a: `plan_id` → `control_interno.plan_anual` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `plan_id` | `uuid` | no | _Por documentar_ | FK→control_interno.plan_anual.id |
| 3 | `tipo` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `nombre` | `character varying(255)` | sí | _Por documentar_ |  |
| 5 | `email` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 6 | `disponibilidad` | `character varying(50)` | sí | _Por documentar_ |  |
| 7 | `horas_totales` | `integer` | sí | _Por documentar_ |  |
| 8 | `horas_asignadas` | `integer` | sí | _Por documentar_ |  |
| 9 | `auditorias_asignadas` | `integer` | sí | _Por documentar_ |  |
| 10 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## rol_plan_anual_5

Roles del plan anual (5 roles)

- Clave primaria: `id`
- Filas: 405

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `plan_id` | `uuid` | no | _Por documentar_ |  |
| 3 | `rol_numero` | `integer` | no | _Por documentar_ |  |
| 4 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `descripcion` | `text` | no | _Por documentar_ |  |
| 6 | `color` | `character varying(7)` | no | _Por documentar_ |  |
| 7 | `porcentaje_cumplimiento` | `integer` | sí | _Por documentar_ |  |
| 8 | `total_actividades` | `integer` | sí | _Por documentar_ |  |
| 9 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 10 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
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
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `lista_id` | `uuid` | no | _Por documentar_ |  |
| 3 | `orden` | `integer` | no | _Por documentar_ |  |
| 4 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 6 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 7 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## seguimiento_plan

_Por documentar._

- Clave primaria: `id`
- Filas: 7
- Referencia a: `plan_id` → `control_interno.plan_mejoramiento` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `plan_id` | `uuid` | no | _Por documentar_ | FK→control_interno.plan_mejoramiento.id |
| 3 | `periodicidad` | `character varying(20)` | no | _Por documentar_ |  |
| 4 | `tipo_control` | `character varying(20)` | no | _Por documentar_ |  |
| 5 | `fecha_corte` | `timestamp without time zone` | no | _Por documentar_ |  |
| 6 | `responsable_id` | `character varying(255)` | no | _Por documentar_ |  |
| 7 | `responsable_nombre` | `character varying(255)` | sí | _Por documentar_ |  |
| 8 | `resumen` | `text` | sí | _Por documentar_ |  |
| 9 | `informe_ref` | `character varying(500)` | sí | _Por documentar_ |  |
| 10 | `total_acciones_evaluadas` | `integer` | sí | _Por documentar_ |  |
| 11 | `acciones_cumplen` | `integer` | sí | _Por documentar_ |  |
| 12 | `acciones_parcial` | `integer` | sí | _Por documentar_ |  |
| 13 | `acciones_no_cumplen` | `integer` | sí | _Por documentar_ |  |
| 14 | `alertas_generadas` | `integer` | sí | _Por documentar_ |  |
| 15 | `automatico` | `boolean` | sí | _Por documentar_ |  |
| 16 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## seguimiento_plan_mejoramiento

Seguimientos trimestrales de planes de mejoramiento

- Clave primaria: `id`
- Filas: 0
- Referencia a: `plan_id` → `control_interno.plan_mejoramiento` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `plan_id` | `uuid` | no | _Por documentar_ | FK→control_interno.plan_mejoramiento.id |
| 3 | `numero_seguimiento` | `integer` | no | _Por documentar_ |  |
| 4 | `fecha_seguimiento` | `date` | no | _Por documentar_ |  |
| 5 | `realizado_por` | `character varying(255)` | no | _Por documentar_ |  |
| 6 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 7 | `cumplimiento` | `integer` | sí | _Por documentar_ |  |
| 8 | `efectividad` | `integer` | sí | _Por documentar_ |  |
| 9 | `acciones_implementadas` | `integer` | sí | _Por documentar_ |  |
| 10 | `acciones_totales` | `integer` | sí | _Por documentar_ |  |
| 11 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## seguimiento_trimestral

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `plan_id` → `control_interno.plan_mejoramiento` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `plan_id` | `uuid` | no | _Por documentar_ | FK→control_interno.plan_mejoramiento.id |
| 3 | `trimestre` | `integer` | no | _Por documentar_ |  |
| 4 | `año` | `integer` | no | _Por documentar_ |  |
| 5 | `fecha_inicio` | `date` | no | _Por documentar_ |  |
| 6 | `fecha_fin` | `date` | no | _Por documentar_ |  |
| 7 | `fecha_seguimiento` | `date` | sí | _Por documentar_ |  |
| 8 | `avance_global` | `integer` | sí | _Por documentar_ |  |
| 9 | `porcentaje_cumplimiento` | `integer` | sí | _Por documentar_ |  |
| 10 | `porcentaje_efectividad` | `integer` | sí | _Por documentar_ |  |
| 11 | `acciones_revisadas` | `integer` | sí | _Por documentar_ |  |
| 12 | `acciones_totales` | `integer` | sí | _Por documentar_ |  |
| 13 | `observaciones_generales` | `text` | sí | _Por documentar_ |  |
| 14 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 15 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## sesiones_esap

Sesiones activas de usuarios

- Clave primaria: `id`
- Filas: 0
- Referencia a: `usuario_id` → `control_interno.usuarios_esap` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `usuario_id` | `uuid` | no | _Por documentar_ | FK→control_interno.usuarios_esap.id |
| 3 | `token` | `character varying(500)` | no | _Por documentar_ | única Credencial de acceso |
| 4 | `ip_address` | `character varying(45)` | sí | _Por documentar_ | Identificador en línea (IP) |
| 5 | `user_agent` | `text` | sí | _Por documentar_ |  |
| 6 | `fecha_inicio` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 7 | `fecha_expiracion` | `timestamp without time zone` | no | _Por documentar_ |  |
| 8 | `activa` | `boolean` | sí | _Por documentar_ |  |
| 9 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## tablero_kanban

Configuración de tableros Kanban para auditorías y planes de mejoramiento

- Clave primaria: `id`
- Filas: 2

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 3 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 4 | `tipo` | `character varying(50)` | no | Tipo de tablero: auditorias o planes_mejoramiento |  |
| 5 | `activo` | `boolean` | no | _Por documentar_ |  |
| 6 | `created_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 7 | `updated_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 8 | `deleted_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 9 | `configuracion_visual` | `jsonb` | sí | _Por documentar_ |  |

## tareas_auditoria

Tareas personalizadas asignadas a auditorías

- Clave primaria: `id`
- Filas: 0
- Referencia a: `auditoria_id` → `control_interno.auditoria` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `auditoria_id` | `uuid` | no | _Por documentar_ | FK→control_interno.auditoria.id |
| 3 | `titulo` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `estado` | `control_interno.estado_tarea` | no | _Por documentar_ |  |
| 6 | `prioridad` | `control_interno.prioridad_tarea` | no | _Por documentar_ |  |
| 7 | `fase` | `control_interno.fase_tarea` | sí | _Por documentar_ |  |
| 8 | `responsable_id` | `uuid` | no | _Por documentar_ |  |
| 9 | `responsable_nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 10 | `fecha_vencimiento` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `fecha_completado` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `progreso` | `integer` | sí | _Por documentar_ |  |
| 13 | `notas` | `text` | sí | _Por documentar_ |  |
| 14 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 15 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |

## tipo_auditoria

Tipos de auditoría configurables del sistema (Regular, Territorial, Especial)

- Clave primaria: `id`
- Filas: 5

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(255)` | no | Código único del tipo (ej: AUD-REG, AUD-TERR) | única |
| 3 | `nombre` | `character varying(255)` | no | Nombre descriptivo del tipo de auditoría |  |
| 4 | `descripcion` | `text` | sí | Descripción detallada del tipo de auditoría |  |
| 5 | `alcance` | `text` | sí | Alcance general del tipo de auditoría |  |
| 6 | `duracion_promedio` | `integer` | no | Duración promedio en días |  |
| 7 | `equipo_promedio` | `integer` | no | Número promedio de personas en el equipo |  |
| 8 | `color` | `character varying(7)` | no | Color hexadecimal para representación visual |  |
| 9 | `activa` | `boolean` | no | Indica si el tipo está activo y disponible |  |
| 10 | `auditorias_programadas` | `integer` | no | Contador de auditorías programadas con este tipo |  |
| 11 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 13 | `deleted_at` | `timestamp without time zone` | sí | Fecha de eliminación (soft delete) |  |

## tipo_proceso

Catálogo parametrizable de tipos de procesos auditables

- Clave primaria: `id`
- Filas: 7

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(80)` | no | Código estable usado por frontend y procesos existentes | única |
| 3 | `nombre` | `character varying(120)` | no | Nombre visible del tipo de proceso |  |
| 4 | `color` | `character varying(120)` | no | Clases CSS del distintivo visual en frontend |  |
| 5 | `orden` | `integer` | no | _Por documentar_ |  |
| 6 | `activo` | `boolean` | no | _Por documentar_ |  |
| 7 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 8 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |

## usuarios_esap

Usuarios del sistema ESAP

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(255)` | no | _Por documentar_ | única |
| 3 | `nombre_completo` | `character varying(255)` | no | _Por documentar_ | Nombre de persona |
| 4 | `email` | `character varying(255)` | no | _Por documentar_ | única Contacto |
| 5 | `cargo` | `character varying(255)` | sí | _Por documentar_ |  |
| 6 | `area` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `rol` | `character varying(100)` | sí | _Por documentar_ |  |
| 8 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 9 | `ultimo_acceso` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 10 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

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
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `lista_id` | `uuid` | no | _Por documentar_ |  |
| 3 | `version` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `fecha` | `date` | no | _Por documentar_ |  |
| 5 | `usuario` | `character varying(255)` | no | _Por documentar_ |  |
| 6 | `cambios` | `text` | no | _Por documentar_ |  |
| 7 | `motivo_cambio` | `text` | no | _Por documentar_ |  |
| 8 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## version_programa_anual

Versiones del Programa Anual de Auditoría por vigencia (EFDS-1919). Se generan al exportar si cambió lo que el documento imprime.

- Clave primaria: `id`
- Filas: 25

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `vigencia` | `integer` | no | _Por documentar_ |  |
| 3 | `version` | `integer` | no | _Por documentar_ |  |
| 4 | `huella` | `character varying(64)` | no | _Por documentar_ |  |
| 5 | `filas` | `jsonb` | no | _Por documentar_ |  |
| 6 | `cambios` | `jsonb` | no | _Por documentar_ |  |
| 7 | `generada_por` | `character varying(255)` | no | _Por documentar_ |  |
| 8 | `generada_por_id` | `character varying(64)` | sí | _Por documentar_ |  |
| 9 | `created_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 10 | `motivo` | `text` | sí | _Por documentar_ |  |

## workflow_aprobacion_informe

Workflow de aprobación para informes de ley (US-033)

- Clave primaria: `id`
- Filas: 0
- Referencia a: `entrega_id` → `control_interno.entrega_informe_ley` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `entrega_id` | `uuid` | no | _Por documentar_ | FK→control_interno.entrega_informe_ley.id |
| 3 | `paso_actual` | `integer` | sí | _Por documentar_ |  |
| 4 | `estado_workflow` | `character varying(50)` | sí | _Por documentar_ |  |
| 5 | `completado` | `boolean` | sí | _Por documentar_ |  |
| 6 | `fecha_completado` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 7 | `creado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 8 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
