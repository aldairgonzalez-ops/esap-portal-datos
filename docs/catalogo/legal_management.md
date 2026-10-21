# Gestión jurídica (`legal_management`)

Procesos, actuaciones y abogados de la gestión jurídica.

54 tablas · 0 vistas · 791 columnas · 33.017 filas · 7 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`actas`](#actas) | Tabla | 0 | _Por documentar_ |
| [`actors`](#actors) | Tabla | 168 | _Por documentar_ |
| [`actuaciones`](#actuaciones) | Tabla | 427 | _Por documentar_ |
| [`adjuntos_correo`](#adjuntos_correo) | Tabla | 2552 | Adjuntos de correos electrónicos sincronizados desde Microsoft Graph |
| [`audiencias`](#audiencias) | Tabla | 18 | _Por documentar_ |
| [`autos`](#autos) | Tabla | 4 | _Por documentar_ |
| [`borradores_correos`](#borradores_correos) | Tabla | 2 | Borradores privados de correos nuevos del Centro de Comunicaciones (Redactar Correo). Se autoguardan y se eliminan al enviarse. |
| [`cat_tipos_requerimiento`](#cat_tipos_requerimiento) | Tabla | 9 | _Por documentar_ |
| [`coactivos_historial`](#coactivos_historial) | Tabla | 48 | _Por documentar_ |
| [`comentarios`](#comentarios) | Tabla | 9 | _Por documentar_ |
| [`comentarios_consulta`](#comentarios_consulta) | Tabla | 2 | _Por documentar_ |
| [`comentarios_correo`](#comentarios_correo) | Tabla | 2 | Comentarios del tab "Comentarios" en el Detalle de Comunicación (Centro de Comunicaciones). |
| [`comentarios_oc`](#comentarios_oc) | Tabla | 28 | _Por documentar_ |
| [`conceptos_juridicos`](#conceptos_juridicos) | Tabla | 0 | _Por documentar_ |
| [`consulta_juridica_historial`](#consulta_juridica_historial) | Tabla | 132 | _Por documentar_ |
| [`consultas_juridicas`](#consultas_juridicas) | Tabla | 31 | Registro de consultas y asesorías jurídicas internas de ESAP |
| [`correo_juridico_historial`](#correo_juridico_historial) | Tabla | 14552 | _Por documentar_ |
| [`correo_tracking_tokens`](#correo_tracking_tokens) | Tabla | 100 | _Por documentar_ |
| [`correos_juridicos`](#correos_juridicos) | Tabla | 14036 | _Por documentar_ |
| [`decisiones_disciplinarias`](#decisiones_disciplinarias) | Tabla | 6 | Tabla para almacenar decisiones de procesos disciplinarios en el módulo de juzgamiento |
| [`documentos`](#documentos) | Tabla | 157 | Documentos asociados a expedientes judiciales |
| [`documentos_consulta`](#documentos_consulta) | Tabla | 25 | Documentos adjuntos a consultas jurídicas |
| [`documentos_oc`](#documentos_oc) | Tabla | 21 | _Por documentar_ |
| [`evidencias`](#evidencias) | Tabla | 16 | _Por documentar_ |
| [`excepciones_procesales`](#excepciones_procesales) | Tabla | 2 | Excepciones procesales del módulo de Juzgamiento Disciplinario |
| [`expedientes`](#expedientes) | Tabla | 91 | _Por documentar_ |
| [`hallazgos`](#hallazgos) | Tabla | 0 | _Por documentar_ |
| [`historial_consultas`](#historial_consultas) | Tabla | 0 | _Por documentar_ |
| [`notas_expediente`](#notas_expediente) | Tabla | 3 | Notas internas de los abogados sobre el expediente |
| [`oficios_enviados`](#oficios_enviados) | Tabla | 4 | Oficios judiciales enviados desde el sistema, con soporte para plantillas institucionales ESAP |
| [`organismos_control`](#organismos_control) | Tabla | 9 | _Por documentar_ |
| [`pagos_coactivos`](#pagos_coactivos) | Tabla | 10 | _Por documentar_ |
| [`pei_indicadores`](#pei_indicadores) | Tabla | 24 | _Por documentar_ |
| [`pei_registros_avance`](#pei_registros_avance) | Tabla | 24 | _Por documentar_ |
| [`planes_comentarios`](#planes_comentarios) | Tabla | 0 | _Por documentar_ |
| [`planes_evidencias`](#planes_evidencias) | Tabla | 14 | _Por documentar_ |
| [`planes_hallazgos`](#planes_hallazgos) | Tabla | 4 | _Por documentar_ |
| [`planes_mejoramiento`](#planes_mejoramiento) | Tabla | 22 | _Por documentar_ |
| [`planes_seguimientos`](#planes_seguimientos) | Tabla | 22 | _Por documentar_ |
| [`plantillas_documentos`](#plantillas_documentos) | Tabla | 5 | _Por documentar_ |
| [`procesos_coactivos`](#procesos_coactivos) | Tabla | 7 | Tabla de procesos de cobro coactivo - Módulo Gestión Legal |
| [`procesos_coactivos_adjuntos`](#procesos_coactivos_adjuntos) | Tabla | 13 | _Por documentar_ |
| [`requerimientos_oc`](#requerimientos_oc) | Tabla | 14 | _Por documentar_ |
| [`respuesta_borrador_oc`](#respuesta_borrador_oc) | Tabla | 2 | Almacena borradores de respuestas a requerimientos de órganos de control |
| [`riesgo_historial`](#riesgo_historial) | Tabla | 8 | Historial de cambios y eventos de riesgos para trazabilidad |
| [`riesgos`](#riesgos) | Tabla | 6 | _Por documentar_ |
| [`sequences`](#sequences) | Tabla | 1 | _Por documentar_ |
| [`solicitudes_insumos`](#solicitudes_insumos) | Tabla | 0 | _Por documentar_ |
| [`system_configurations`](#system_configurations) | Tabla | 8 | _Por documentar_ |
| [`tareas_expediente`](#tareas_expediente) | Tabla | 35 | Tareas asociadas a expedientes judiciales para control de actividades |
| [`tasas_referencia`](#tasas_referencia) | Tabla | 0 | _Por documentar_ |
| [`terminos_alertas_enviadas`](#terminos_alertas_enviadas) | Tabla | 109 | _Por documentar_ |
| [`terminos_procesales`](#terminos_procesales) | Tabla | 233 | Torre de control transversal para vencimientos de términos procesales de todos los módulos |
| [`terminos_reglas_alerta`](#terminos_reglas_alerta) | Tabla | 2 | _Por documentar_ |

## actas

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `expediente_id` | `uuid` | no | _Por documentar_ | FK→legal_management.expedientes.id |
| 3 | `numero_acta` | `character varying(100)` | sí | _Por documentar_ |  |
| 4 | `fecha` | `date` | sí | _Por documentar_ |  |
| 5 | `horario` | `character varying(50)` | sí | _Por documentar_ |  |
| 6 | `duracion` | `character varying(50)` | sí | _Por documentar_ |  |
| 7 | `lugar` | `character varying(255)` | sí | _Por documentar_ |  |
| 8 | `presidente` | `character varying(255)` | sí | _Por documentar_ |  |
| 9 | `participantes` | `text` | sí | _Por documentar_ |  |
| 10 | `resumen` | `text` | sí | _Por documentar_ |  |
| 11 | `decisiones_tomadas` | `text` | sí | _Por documentar_ |  |
| 12 | `estado` | `character varying(50)` | sí | _Por documentar_ |  |
| 13 | `archivo_nombre` | `character varying(255)` | sí | _Por documentar_ |  |
| 14 | `archivo_url` | `text` | sí | _Por documentar_ |  |
| 15 | `archivo_tamano` | `integer` | sí | _Por documentar_ |  |
| 16 | `tipo` | `character varying(100)` | sí | _Por documentar_ |  |
| 17 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 18 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |

## actors

_Por documentar._

- Clave primaria: `id`
- Filas: 168
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `expediente_id` | `uuid` | no | _Por documentar_ | FK→legal_management.expedientes.id |
| 3 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `tipo_persona` | `character varying(50)` | no | _Por documentar_ |  |
| 5 | `identificacion` | `character varying(50)` | sí | _Por documentar_ |  |
| 6 | `rol` | `character varying(50)` | no | _Por documentar_ |  |
| 7 | `cargo` | `character varying(100)` | sí | _Por documentar_ |  |
| 8 | `email` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 9 | `telefono` | `character varying(50)` | sí | _Por documentar_ | Contacto |
| 10 | `direccion` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 11 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 13 | `apoderado` | `character varying(255)` | sí | _Por documentar_ |  |
| 14 | `dependencia` | `character varying(150)` | sí | _Por documentar_ |  |

## actuaciones

_Por documentar._

- Clave primaria: `id`
- Filas: 427

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `expediente_id` | `character varying(255)` | no | _Por documentar_ |  |
| 3 | `tipo_actuacion` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `fecha_actuacion` | `timestamp without time zone` | no | _Por documentar_ |  |
| 6 | `documento_url` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `documento_nombre` | `character varying(255)` | sí | _Por documentar_ |  |
| 8 | `usuario_responsable` | `character varying(100)` | sí | _Por documentar_ |  |
| 9 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 10 | `origen` | `character varying(50)` | sí | _Por documentar_ |  |
| 11 | `referencia_id` | `uuid` | sí | _Por documentar_ |  |
| 12 | `metadata` | `jsonb` | sí | _Por documentar_ |  |
| 13 | `responsable_id` | `character varying(255)` | sí | _Por documentar_ |  |

## adjuntos_correo

Adjuntos de correos electrónicos sincronizados desde Microsoft Graph

- Clave primaria: `id`
- Filas: 2552
- Referencia a: `correo_id` → `legal_management.correos_juridicos` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `correo_id` | `uuid` | no | _Por documentar_ | FK→legal_management.correos_juridicos.id |
| 3 | `graph_message_id` | `character varying(500)` | no | _Por documentar_ |  |
| 4 | `graph_attachment_id` | `character varying(500)` | no | ID del adjunto en Graph API, usado para descarga bajo demanda |  |
| 5 | `nombre` | `character varying(500)` | no | _Por documentar_ |  |
| 6 | `content_type` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `tamanio` | `integer` | sí | _Por documentar_ |  |
| 8 | `archivo_local_url` | `text` | sí | Ruta local si el archivo fue descargado al servidor |  |
| 9 | `descargado` | `boolean` | sí | _Por documentar_ |  |
| 10 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## audiencias

_Por documentar._

- Clave primaria: `id`
- Filas: 18
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `expediente_id` | `uuid` | no | _Por documentar_ | FK→legal_management.expedientes.id |
| 3 | `abogado_id` | `uuid` | no | _Por documentar_ |  |
| 4 | `titulo` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `fecha_hora_inicio` | `timestamp without time zone` | no | _Por documentar_ |  |
| 6 | `duracion_minutos` | `integer` | no | _Por documentar_ |  |
| 7 | `modalidad` | `character varying(50)` | no | _Por documentar_ |  |
| 8 | `ubicacion` | `character varying(255)` | sí | _Por documentar_ |  |
| 9 | `link_reunion` | `text` | sí | _Por documentar_ |  |
| 10 | `estado` | `character varying(50)` | sí | _Por documentar_ |  |
| 11 | `notas_preparacion` | `text` | sí | _Por documentar_ |  |
| 12 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 13 | `historial` | `jsonb` | sí | _Por documentar_ |  |
| 14 | `abogado_nombre` | `character varying(255)` | sí | _Por documentar_ |  |
| 15 | `abogado_email` | `character varying(255)` | sí | _Por documentar_ | Contacto |

## autos

_Por documentar._

- Clave primaria: `id`
- Filas: 4
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `expediente_id` | `uuid` | no | _Por documentar_ | FK→legal_management.expedientes.id |
| 3 | `numero` | `character varying` | no | _Por documentar_ |  |
| 4 | `tipo` | `character varying` | no | _Por documentar_ |  |
| 5 | `fecha_auto` | `timestamp without time zone` | no | _Por documentar_ |  |
| 6 | `juzgado` | `character varying` | no | _Por documentar_ |  |
| 7 | `resumen` | `text` | sí | _Por documentar_ |  |
| 8 | `estado` | `character varying` | no | _Por documentar_ |  |
| 9 | `fecha_notificacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 10 | `archivo_url` | `character varying` | no | _Por documentar_ |  |
| 11 | `archivo_nombre` | `character varying` | no | _Por documentar_ |  |
| 12 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 13 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## borradores_correos

Borradores privados de correos nuevos del Centro de Comunicaciones (Redactar Correo). Se autoguardan y se eliminan al enviarse.

- Clave primaria: `id`
- Filas: 2

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `usuario_id` | `character varying(100)` | no | _Por documentar_ |  |
| 3 | `usuario_nombre` | `character varying(255)` | sí | _Por documentar_ |  |
| 4 | `buzon` | `character varying(20)` | no | Cuenta remitente/bandeja de origen (JUDICIAL \| CORREOS) para restaurar el remitente correcto al reabrir. |  |
| 5 | `destinatarios_to` | `text` | sí | _Por documentar_ |  |
| 6 | `destinatarios_cc` | `text` | sí | _Por documentar_ |  |
| 7 | `destinatarios_cco` | `text` | sí | _Por documentar_ |  |
| 8 | `asunto` | `character varying(500)` | sí | _Por documentar_ |  |
| 9 | `cuerpo` | `text` | sí | _Por documentar_ |  |
| 10 | `adjuntos` | `jsonb` | no | Adjuntos embebidos como arreglo JSON base64: [{ name, contentType, contentBytes, size }]. Límite ~25MB aplicado en el frontend. |  |
| 11 | `solicitar_acuse` | `boolean` | no | _Por documentar_ |  |
| 12 | `created_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 13 | `updated_at` | `timestamp with time zone` | no | _Por documentar_ |  |

## cat_tipos_requerimiento

_Por documentar._

- Clave primaria: `id`
- Filas: 9

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `character varying(50)` | no | _Por documentar_ | PK |
| 2 | `nombre` | `character varying(200)` | no | _Por documentar_ |  |
| 3 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 4 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 5 | `orden` | `integer` | sí | _Por documentar_ |  |
| 6 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 7 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## coactivos_historial

_Por documentar._

- Clave primaria: `id`
- Filas: 48
- Referencia a: `proceso_id` → `legal_management.procesos_coactivos` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `proceso_id` | `uuid` | no | _Por documentar_ | FK→legal_management.procesos_coactivos.id |
| 3 | `tipo_evento` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `campo_modificado` | `character varying(100)` | sí | _Por documentar_ |  |
| 5 | `valor_anterior` | `text` | sí | _Por documentar_ |  |
| 6 | `valor_nuevo` | `text` | sí | _Por documentar_ |  |
| 7 | `usuario` | `character varying(100)` | sí | _Por documentar_ |  |
| 8 | `detalles` | `text` | sí | _Por documentar_ |  |
| 9 | `fecha_evento` | `timestamp without time zone` | sí | _Por documentar_ |  |

## comentarios

_Por documentar._

- Clave primaria: `id`
- Filas: 9
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `expediente_id` | `uuid` | no | _Por documentar_ | FK→legal_management.expedientes.id |
| 3 | `contenido` | `text` | no | _Por documentar_ |  |
| 4 | `usuario_id` | `character varying(255)` | sí | _Por documentar_ |  |
| 5 | `usuario_nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 6 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 7 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## comentarios_consulta

_Por documentar._

- Clave primaria: `id`
- Filas: 2
- Referencia a: `consulta_id` → `legal_management.consultas_juridicas` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `consulta_id` | `uuid` | no | _Por documentar_ | FK→legal_management.consultas_juridicas.id |
| 3 | `mensaje` | `text` | no | _Por documentar_ |  |
| 4 | `usuario` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `cargo` | `character varying(255)` | sí | _Por documentar_ |  |
| 6 | `fecha` | `timestamp without time zone` | sí | _Por documentar_ |  |

## comentarios_correo

Comentarios del tab "Comentarios" en el Detalle de Comunicación (Centro de Comunicaciones).

- Clave primaria: `id`
- Filas: 2
- Referencia a: `correo_id` → `legal_management.correos_juridicos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `correo_id` | `uuid` | no | _Por documentar_ | FK→legal_management.correos_juridicos.id |
| 3 | `mensaje` | `character varying` | no | _Por documentar_ |  |
| 4 | `usuario` | `character varying` | no | _Por documentar_ |  |
| 5 | `cargo` | `character varying` | sí | _Por documentar_ |  |
| 6 | `fecha` | `timestamp without time zone` | sí | _Por documentar_ |  |

## comentarios_oc

_Por documentar._

- Clave primaria: `id`
- Filas: 28
- Referencia a: `requerimiento_id` → `legal_management.requerimientos_oc` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `requerimiento_id` | `uuid` | no | _Por documentar_ | FK→legal_management.requerimientos_oc.id |
| 3 | `contenido` | `text` | no | _Por documentar_ |  |
| 4 | `tipo` | `character varying(30)` | sí | _Por documentar_ |  |
| 5 | `autor_id` | `uuid` | sí | _Por documentar_ |  |
| 6 | `autor_nombre` | `character varying(200)` | sí | _Por documentar_ |  |
| 7 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 8 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## conceptos_juridicos

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `consulta_id` → `legal_management.consultas_juridicas` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `consulta_id` | `uuid` | no | _Por documentar_ | FK→legal_management.consultas_juridicas.id |
| 3 | `numero_concepto` | `character varying(50)` | no | _Por documentar_ | única |
| 4 | `tipo_documento` | `character varying(30)` | sí | _Por documentar_ |  |
| 5 | `titulo` | `character varying(300)` | no | _Por documentar_ |  |
| 6 | `resumen` | `text` | sí | _Por documentar_ |  |
| 7 | `analisis_juridico` | `text` | no | _Por documentar_ |  |
| 8 | `normatividad_aplicable` | `text` | sí | _Por documentar_ |  |
| 9 | `conclusion` | `text` | no | _Por documentar_ |  |
| 10 | `recomendaciones` | `text` | sí | _Por documentar_ |  |
| 11 | `documento_pdf_url` | `character varying(500)` | sí | _Por documentar_ |  |
| 12 | `estado` | `character varying(20)` | sí | _Por documentar_ |  |
| 13 | `abogado_redactor_id` | `uuid` | sí | _Por documentar_ |  |
| 14 | `abogado_redactor_nombre` | `character varying(150)` | sí | _Por documentar_ |  |
| 15 | `revisor_id` | `uuid` | sí | _Por documentar_ |  |
| 16 | `revisor_nombre` | `character varying(150)` | sí | _Por documentar_ |  |
| 17 | `fecha_revision` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 18 | `comentarios_revision` | `text` | sí | _Por documentar_ |  |
| 19 | `aprobado_por` | `character varying(150)` | sí | _Por documentar_ |  |
| 20 | `fecha_aprobacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 21 | `fecha_emision` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 22 | `notificado_a` | `character varying(300)` | sí | _Por documentar_ |  |
| 23 | `visible_banco` | `boolean` | sí | _Por documentar_ |  |
| 24 | `etiquetas` | `text[]` | sí | _Por documentar_ |  |
| 25 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 26 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## consulta_juridica_historial

_Por documentar._

- Clave primaria: `id`
- Filas: 132
- Referencia a: `consulta_id` → `legal_management.consultas_juridicas` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `consulta_id` | `uuid` | no | _Por documentar_ | FK→legal_management.consultas_juridicas.id |
| 3 | `tipo_evento` | `character varying` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | no | _Por documentar_ |  |
| 5 | `detalle` | `text` | sí | _Por documentar_ |  |
| 6 | `usuario` | `character varying` | sí | _Por documentar_ |  |
| 7 | `fecha` | `timestamp without time zone` | no | _Por documentar_ |  |

## consultas_juridicas

Registro de consultas y asesorías jurídicas internas de ESAP

- Clave primaria: `id`
- Filas: 31

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `numero_radicado` | `character varying(50)` | no | _Por documentar_ | única |
| 3 | `tipo_solicitud` | `character varying(30)` | sí | _Por documentar_ |  |
| 4 | `area_solicitante` | `character varying(100)` | sí | _Por documentar_ |  |
| 5 | `funcionario_solicitante` | `character varying(150)` | sí | _Por documentar_ |  |
| 6 | `cargo_solicitante` | `character varying(100)` | sí | _Por documentar_ |  |
| 7 | `email_solicitante` | `character varying(150)` | sí | _Por documentar_ | Contacto |
| 8 | `telefono_solicitante` | `character varying(20)` | sí | _Por documentar_ | Contacto |
| 9 | `asunto` | `character varying(300)` | sí | _Por documentar_ |  |
| 10 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 11 | `antecedentes` | `text` | sí | _Por documentar_ |  |
| 12 | `documentos_soporte_urls` | `text[]` | sí | _Por documentar_ |  |
| 13 | `tema_principal` | `character varying(100)` | sí | _Por documentar_ |  |
| 14 | `palabras_clave` | `text[]` | sí | _Por documentar_ |  |
| 15 | `abogado_asignado_id` | `uuid` | sí | _Por documentar_ |  |
| 16 | `abogado_asignado_nombre` | `character varying(150)` | sí | _Por documentar_ |  |
| 17 | `fecha_asignacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 18 | `estado` | `character varying(30)` | sí | _Por documentar_ |  |
| 19 | `fecha_radicacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 20 | `fecha_vencimiento` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 21 | `dias_termino` | `integer` | sí | _Por documentar_ |  |
| 22 | `dias_transcurridos` | `integer` | sí | _Por documentar_ |  |
| 23 | `suspendida` | `boolean` | sí | _Por documentar_ |  |
| 24 | `fecha_suspension` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 25 | `motivo_suspension` | `text` | sí | _Por documentar_ |  |
| 26 | `confidencial` | `boolean` | sí | _Por documentar_ |  |
| 27 | `areas_con_acceso` | `text[]` | sí | _Por documentar_ |  |
| 28 | `prioridad` | `character varying(20)` | sí | _Por documentar_ |  |
| 29 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 30 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 31 | `created_by` | `character varying(150)` | sí | _Por documentar_ |  |
| 32 | `updated_by` | `character varying(150)` | sí | _Por documentar_ |  |
| 33 | `fecha_recepcion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 34 | `termino_legal_dias` | `integer` | sí | Término legal de 30 días hábiles según CPACA Art. 50 |  |
| 35 | `fecha_maxima_respuesta` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 36 | `fecha_respuesta` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 37 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 38 | `canal_entrada` | `character varying(30)` | sí | _Por documentar_ |  |
| 39 | `dependencia_solicitante` | `character varying(200)` | sí | _Por documentar_ |  |
| 40 | `nombre_solicitante` | `character varying(200)` | sí | _Por documentar_ |  |
| 41 | `tipo_usuario` | `character varying(20)` | sí | _Por documentar_ |  |
| 42 | `materia_juridica` | `character varying(30)` | sí | _Por documentar_ |  |
| 43 | `complejidad` | `character varying(10)` | sí | _Por documentar_ |  |
| 44 | `numero_oficio_respuesta` | `character varying(50)` | sí | _Por documentar_ |  |
| 45 | `tipo_respuesta` | `character varying(30)` | sí | _Por documentar_ |  |
| 46 | `documento_respuesta_url` | `text` | sí | _Por documentar_ |  |
| 47 | `respuesta` | `text` | sí | _Por documentar_ |  |
| 48 | `estado_archivo` | `character varying` | sí | _Por documentar_ |  |
| 49 | `fecha_archivo` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 50 | `usuario_archivo` | `character varying` | sí | _Por documentar_ |  |
| 51 | `motivo_archivo` | `text` | sí | _Por documentar_ |  |
| 52 | `destinatarios_adicionales` | `text` | sí | JSON array con los emails adicionales a los que se envió la respuesta, ej: ["a@b.com","c@d.com"] |  |
| 53 | `comentario_devolucion_jefe` | `text` | sí | _Por documentar_ |  |
| 54 | `origen_comunicacion_id` | `uuid` | sí | _Por documentar_ |  |

## correo_juridico_historial

_Por documentar._

- Clave primaria: `id`
- Filas: 14552
- Referencia a: `correo_juridico_id` → `legal_management.correos_juridicos` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `correo_juridico_id` | `uuid` | no | _Por documentar_ | FK→legal_management.correos_juridicos.id |
| 3 | `tipo_evento` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | no | _Por documentar_ |  |
| 5 | `detalle_json` | `jsonb` | sí | _Por documentar_ |  |
| 6 | `usuario` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `fecha_creacion` | `timestamp without time zone` | sí | _Por documentar_ |  |

## correo_tracking_tokens

_Por documentar._

- Clave primaria: `id`
- Filas: 100
- Referencia a: `adjunto_id` → `legal_management.adjuntos_correo` (0..1 → 0..1); `correo_id` → `legal_management.correos_juridicos` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `correo_id` | `uuid` | no | _Por documentar_ | FK→legal_management.correos_juridicos.id |
| 3 | `adjunto_id` | `uuid` | sí | _Por documentar_ | FK→legal_management.adjuntos_correo.id |
| 4 | `token` | `character varying(100)` | no | _Por documentar_ | única Credencial de acceso |
| 5 | `tipo` | `character varying(20)` | no | _Por documentar_ |  |
| 6 | `abierto` | `boolean` | no | _Por documentar_ |  |
| 7 | `fecha_apertura` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 8 | `ip_apertura` | `character varying(50)` | sí | _Por documentar_ | Identificador en línea (IP) |
| 9 | `user_agent` | `text` | sí | _Por documentar_ |  |
| 10 | `destinatario_email` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 11 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |

## correos_juridicos

_Por documentar._

- Clave primaria: `id`
- Filas: 14036
- Referencia a: `parent_email_id` → `legal_management.correos_juridicos` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `graph_message_id` | `character varying(500)` | no | _Por documentar_ | única |
| 3 | `asunto` | `character varying(500)` | no | _Por documentar_ |  |
| 4 | `remitente_email` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `remitente_nombre` | `character varying(255)` | sí | _Por documentar_ |  |
| 6 | `destinatarios` | `text` | sí | _Por documentar_ |  |
| 7 | `fecha_recepcion` | `timestamp without time zone` | no | _Por documentar_ |  |
| 8 | `cuerpo_html` | `text` | sí | _Por documentar_ |  |
| 9 | `cuerpo_texto` | `text` | sí | _Por documentar_ |  |
| 10 | `tiene_adjuntos` | `boolean` | sí | _Por documentar_ |  |
| 11 | `leido` | `boolean` | sí | _Por documentar_ |  |
| 12 | `archivado` | `boolean` | sí | _Por documentar_ |  |
| 13 | `urgente` | `boolean` | sí | _Por documentar_ |  |
| 14 | `tipo` | `character varying(20)` | sí | _Por documentar_ |  |
| 15 | `categoria` | `character varying(100)` | sí | _Por documentar_ |  |
| 16 | `modulo_sugerido` | `character varying(100)` | sí | _Por documentar_ |  |
| 17 | `confianza_clasificacion` | `double precision` | sí | _Por documentar_ |  |
| 18 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 19 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 20 | `ai_suggested_category` | `character varying(100)` | sí | _Por documentar_ |  |
| 21 | `is_trained` | `boolean` | sí | _Por documentar_ |  |
| 22 | `expediente_id` | `character varying(255)` | sí | _Por documentar_ |  |
| 23 | `direccion` | `character varying(20)` | sí | _Por documentar_ |  |
| 24 | `destinatarios_to` | `text` | sí | _Por documentar_ |  |
| 25 | `is_forwarded` | `boolean` | sí | _Por documentar_ |  |
| 26 | `is_replied` | `boolean` | sí | _Por documentar_ |  |
| 27 | `parent_email_id` | `uuid` | sí | _Por documentar_ | FK→legal_management.correos_juridicos.id |
| 28 | `thread_id` | `character varying(500)` | sí | _Por documentar_ |  |
| 29 | `internet_message_id` | `character varying(500)` | sí | _Por documentar_ |  |
| 30 | `proceso_id_sugerido` | `character varying(100)` | sí | _Por documentar_ |  |
| 31 | `implicado_sugerido` | `character varying(255)` | sí | _Por documentar_ |  |
| 32 | `submodulo_sugerido` | `character varying(100)` | sí | _Por documentar_ |  |
| 33 | `buzon` | `character varying(20)` | no | _Por documentar_ |  |
| 34 | `destinatarios_cco` | `text` | sí | Destinatarios en Copia Oculta (CCO/BCC), como arreglo JSON de correos. No visibles para los demás destinatarios; se conservan para trazabilidad. |  |
| 35 | `consulta_id` | `uuid` | sí | _Por documentar_ |  |
| 36 | `modulo_destino` | `character varying(50)` | sí | _Por documentar_ |  |

## decisiones_disciplinarias

Tabla para almacenar decisiones de procesos disciplinarios en el módulo de juzgamiento

- Clave primaria: `id`
- Filas: 6
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `tipo_decision` | `character varying(100)` | no | Tipo de decisión: AUTO_DE_FALLO, ARCHIVO, SUSPENSION, etc. |  |
| 3 | `tipo_fallo` | `character varying(100)` | no | Tipo de fallo: ABSOLUTORIO, CONDENATORIO, INHIBITORIO |  |
| 4 | `sancion` | `character varying(255)` | sí | _Por documentar_ |  |
| 5 | `consideraciones` | `text` | no | _Por documentar_ |  |
| 6 | `fundamentos_juridicos` | `text` | sí | _Por documentar_ |  |
| 7 | `responsable` | `character varying(255)` | no | _Por documentar_ |  |
| 8 | `cargo_responsable` | `character varying(255)` | sí | _Por documentar_ |  |
| 9 | `fecha` | `date` | no | _Por documentar_ |  |
| 10 | `expediente_id` | `uuid` | no | _Por documentar_ | FK→legal_management.expedientes.id |
| 11 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |

## documentos

Documentos asociados a expedientes judiciales

- Clave primaria: `id`
- Filas: 157
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `expediente_id` | `uuid` | no | _Por documentar_ | FK→legal_management.expedientes.id |
| 3 | `nombre` | `character varying(500)` | no | _Por documentar_ |  |
| 4 | `tipo` | `character varying(100)` | no | Tipo de documento: DEMANDA, AUTO, MEMORIAL, PRUEBA, SENTENCIA, NOTIFICACION, OTRO |  |
| 5 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 6 | `archivo_url` | `text` | sí | URL o ruta al archivo físico o en storage |  |
| 7 | `archivo_nombre_original` | `character varying(500)` | sí | _Por documentar_ |  |
| 8 | `archivo_tamano` | `integer` | sí | _Por documentar_ |  |
| 9 | `archivo_mime_type` | `character varying(100)` | sí | _Por documentar_ |  |
| 10 | `fecha_documento` | `date` | sí | _Por documentar_ |  |
| 11 | `numero_folios` | `integer` | sí | _Por documentar_ |  |
| 12 | `confidencial` | `boolean` | sí | _Por documentar_ |  |
| 13 | `subido_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 14 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 15 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 16 | `categoria` | `character varying(50)` | sí | _Por documentar_ |  |
| 17 | `etapa` | `character varying(100)` | sí | Etapa procesal en la que fue incorporado el documento |  |

## documentos_consulta

Documentos adjuntos a consultas jurídicas

- Clave primaria: `id`
- Filas: 25
- Referencia a: `consulta_id` → `legal_management.consultas_juridicas` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `consulta_id` | `uuid` | no | Referencia a la consulta jurídica | FK→legal_management.consultas_juridicas.id |
| 3 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `tipo_documento` | `character varying(50)` | sí | Tipo: solicitud, normativa, concepto, respuesta, otro |  |
| 5 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 6 | `archivo_url` | `text` | sí | _Por documentar_ |  |
| 7 | `archivo_nombre_original` | `character varying(255)` | sí | _Por documentar_ |  |
| 8 | `tamano_bytes` | `bigint` | sí | _Por documentar_ |  |
| 9 | `mime_type` | `character varying(100)` | sí | _Por documentar_ |  |
| 10 | `subido_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 11 | `fecha_documento` | `date` | sí | _Por documentar_ |  |
| 12 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 13 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 14 | `firmado` | `boolean` | sí | Indica si el documento ha sido firmado (true=firmado, false=sin firmar) |  |

## documentos_oc

_Por documentar._

- Clave primaria: `id`
- Filas: 21
- Referencia a: `requerimiento_id` → `legal_management.requerimientos_oc` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `requerimiento_id` | `uuid` | no | _Por documentar_ | FK→legal_management.requerimientos_oc.id |
| 3 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `tipo_documento` | `character varying(50)` | sí | _Por documentar_ |  |
| 5 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 6 | `archivo_url` | `text` | sí | _Por documentar_ |  |
| 7 | `tamano_bytes` | `bigint` | sí | _Por documentar_ |  |
| 8 | `mime_type` | `character varying(100)` | sí | _Por documentar_ |  |
| 9 | `subido_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 10 | `fecha_documento` | `date` | sí | _Por documentar_ |  |
| 11 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## evidencias

_Por documentar._

- Clave primaria: `id`
- Filas: 16
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `expediente_id` | `uuid` | no | _Por documentar_ | FK→legal_management.expedientes.id |
| 3 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 4 | `aportado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 5 | `fecha_presentacion` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 6 | `archivo_nombre` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `archivo_url` | `text` | sí | _Por documentar_ |  |
| 8 | `archivo_tamano` | `integer` | sí | _Por documentar_ |  |
| 9 | `tipo` | `character varying(100)` | sí | _Por documentar_ |  |
| 10 | `prioridad` | `character varying(20)` | sí | _Por documentar_ |  |
| 11 | `estado` | `character varying(50)` | sí | _Por documentar_ |  |
| 12 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 13 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 14 | `tipo_archivo` | `character varying(50)` | sí | File extension (e.g., jpg, pdf, png) for correct icon display |  |

## excepciones_procesales

Excepciones procesales del módulo de Juzgamiento Disciplinario

- Clave primaria: `id`
- Filas: 2
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `tipo` | `character varying(100)` | no | Exception type - now configurable via ConfiguracionesSIGL, not restricted to fixed ENUM values |  |
| 3 | `descripcion` | `text` | no | _Por documentar_ |  |
| 4 | `fundamento` | `text` | sí | _Por documentar_ |  |
| 5 | `estado` | `character varying(20)` | no | Estado de la excepción: PENDIENTE, RESUELTA, RECHAZADA |  |
| 6 | `resolucion` | `text` | sí | _Por documentar_ |  |
| 7 | `fecha_presentacion` | `date` | no | _Por documentar_ |  |
| 8 | `fecha_resolucion` | `date` | sí | _Por documentar_ |  |
| 9 | `presentado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 10 | `expediente_id` | `uuid` | no | _Por documentar_ | FK→legal_management.expedientes.id |
| 11 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 12 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |

## expedientes

_Por documentar._

- Clave primaria: `id`
- Filas: 91
- Referencia a: `proceso_principal_id` → `legal_management.expedientes` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `radicado` | `character varying(50)` | no | _Por documentar_ | única |
| 3 | `jurisdiccion` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `tipo_proceso` | `character varying(100)` | no | _Por documentar_ |  |
| 5 | `demandante` | `character varying(255)` | no | _Por documentar_ |  |
| 6 | `demandado` | `character varying(255)` | no | _Por documentar_ |  |
| 7 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 8 | `fecha_radicacion` | `timestamp without time zone` | no | _Por documentar_ |  |
| 9 | `cuantia` | `numeric(15,2)` | sí | _Por documentar_ |  |
| 10 | `abogado_sustanciador` | `character varying(255)` | sí | _Por documentar_ |  |
| 11 | `fecha_prescripcion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `riesgo_prescripcion` | `boolean` | sí | _Por documentar_ |  |
| 13 | `termino_procesal_dias` | `integer` | sí | _Por documentar_ |  |
| 14 | `ultima_actuacion` | `character varying(255)` | sí | _Por documentar_ |  |
| 15 | `ubicacion_fisica` | `character varying(255)` | sí | _Por documentar_ |  |
| 16 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 17 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 18 | `sancion_proyectada` | `character varying` | sí | _Por documentar_ |  |
| 19 | `etapa` | `character varying(50)` | sí | Stage of the process: AVOCAMIENTO, PRUEBAS, ALEGATOS, etc. |  |
| 20 | `cargo_investigado` | `character varying(255)` | sí | Job title of the investigated person |  |
| 21 | `ley_aplicable` | `character varying(100)` | sí | Applicable law, e.g., Ley 1952/2019 |  |
| 22 | `hechos` | `text` | sí | _Por documentar_ |  |
| 23 | `fecha_limite_etapa` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 24 | `tipo_solicitud` | `character varying(100)` | sí | Type of report/request, e.g. Informe Pormenorizado |  |
| 25 | `radicado_externo` | `character varying(50)` | sí | External ID from the requesting entity |  |
| 26 | `asunto` | `character varying(255)` | sí | Short title or subject of the request |  |
| 27 | `datos_requeridos` | `text` | sí | JSON or text listing required data points |  |
| 28 | `medio_control` | `character varying(255)` | sí | _Por documentar_ |  |
| 29 | `juzgado_conocimiento` | `character varying(255)` | sí | _Por documentar_ |  |
| 30 | `pretension_demandante` | `text` | sí | _Por documentar_ |  |
| 31 | `acto_administrativo_demandado` | `text` | sí | _Por documentar_ |  |
| 32 | `fecha_notificacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 33 | `fecha_vencimiento_termino` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 34 | `tipo_id_demandante` | `character varying(10)` | sí | _Por documentar_ |  |
| 35 | `numero_id_demandante` | `character varying(20)` | sí | _Por documentar_ |  |
| 36 | `tipo_id_demandado` | `character varying(10)` | sí | _Por documentar_ |  |
| 37 | `numero_id_demandado` | `character varying(20)` | sí | _Por documentar_ |  |
| 38 | `etapa_procesal` | `character varying(100)` | sí | _Por documentar_ |  |
| 39 | `documentos_iniciales_urls` | `text[]` | sí | _Por documentar_ |  |
| 40 | `tipo_falta` | `character varying(50)` | sí | Severity: Leve, Grave, Gravísima |  |
| 41 | `dependencia_investigado` | `character varying(150)` | sí | Department of the investigated person |  |
| 42 | `demandante_direccion` | `character varying(500)` | sí | Dirección de notificaciones del demandante | Contacto |
| 43 | `demandante_telefono` | `character varying(50)` | sí | Teléfono de contacto del demandante | Contacto |
| 44 | `demandante_email` | `character varying(255)` | sí | Correo electrónico del demandante | Contacto |
| 45 | `demandante_apoderado` | `character varying(255)` | sí | Nombre del apoderado del demandante |  |
| 46 | `demandado_direccion` | `character varying(500)` | sí | _Por documentar_ | Contacto |
| 47 | `demandado_telefono` | `character varying(50)` | sí | _Por documentar_ | Contacto |
| 48 | `demandado_email` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 49 | `tipo_conteo_termino` | `character varying(20)` | sí | _Por documentar_ |  |
| 50 | `estado_archivo` | `character varying(20)` | no | Estado de archivo: ACTIVO (en Kanban), ARCHIVADO (guardado), ELIMINADO (soft delete) |  |
| 51 | `fecha_archivo` | `timestamp without time zone` | sí | Fecha en que se archivó o eliminó el expediente |  |
| 52 | `usuario_archivo` | `character varying(255)` | sí | Usuario que realizó la acción de archivar/eliminar |  |
| 53 | `motivo_archivo` | `text` | sí | Razón o motivo del archivo/eliminación |  |
| 54 | `nivel_riesgo` | `character varying(255)` | sí | _Por documentar_ |  |
| 55 | `provision_contable` | `numeric(15,2)` | sí | _Por documentar_ |  |
| 56 | `fecha_estimacion_provision` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 57 | `observacion_provision` | `text` | sí | _Por documentar_ |  |
| 58 | `proceso_principal_id` | `uuid` | sí | _Por documentar_ | FK→legal_management.expedientes.id |
| 59 | `abogados_anteriores` | `text[]` | sí | Array of previously assigned lawyer names, populated when abogado_sustanciador is changed via reassignment |  |
| 60 | `fecha_hechos` | `timestamp without time zone` | sí | Fecha en que ocurrieron los hechos disciplinarios. Determina la ley aplicable: anterior al 30/06/2021 = Ley 734/2002, igual o posterior = Ley 1952/2019. |  |
| 61 | `es_delito_admin_publica` | `boolean` | sí | Indica si el proceso penal corresponde a delitos contra la administración pública |  |
| 62 | `es_conducta_patrimonio_publico` | `boolean` | sí | Indica si el proceso penal involucra conductas que afecten el patrimonio público |  |
| 63 | `es_otro_delito_penal` | `boolean` | no | Indica si el proceso penal corresponde a una categoría distinta a las definidas (otros delitos penales) |  |
| 64 | `otro_delito_penal_descripcion` | `character varying(200)` | sí | Descripción libre del tipo de delito penal cuando es_otro_delito_penal = true |  |
| 65 | `campos_adicionales` | `jsonb` | sí | _Por documentar_ |  |
| 66 | `origen` | `character varying(50)` | sí | _Por documentar_ |  |
| 67 | `territorial` | `character varying(150)` | sí | _Por documentar_ |  |
| 68 | `presunta_conducta` | `text` | sí | _Por documentar_ |  |
| 69 | `hechos_list` | `jsonb` | no | _Por documentar_ |  |
| 70 | `origen_comunicacion_id` | `uuid` | sí | _Por documentar_ |  |

## hallazgos

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `requerimiento_id` → `legal_management.requerimientos_oc` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `requerimiento_id` | `uuid` | sí | _Por documentar_ | FK→legal_management.requerimientos_oc.id |
| 3 | `codigo_hallazgo` | `character varying(50)` | no | _Por documentar_ | única |
| 4 | `numero_interno` | `character varying(50)` | sí | _Por documentar_ |  |
| 5 | `tipo_hallazgo` | `character varying(30)` | sí | _Por documentar_ |  |
| 6 | `titulo` | `character varying(300)` | no | _Por documentar_ |  |
| 7 | `descripcion` | `text` | no | _Por documentar_ |  |
| 8 | `causa_raiz` | `text` | sí | _Por documentar_ |  |
| 9 | `efecto` | `text` | sí | _Por documentar_ |  |
| 10 | `area_responsable` | `character varying(150)` | sí | _Por documentar_ |  |
| 11 | `funcionario_responsable` | `character varying(200)` | sí | _Por documentar_ |  |
| 12 | `accion_correctiva` | `text` | no | _Por documentar_ |  |
| 13 | `fecha_compromiso` | `date` | no | _Por documentar_ |  |
| 14 | `indicador_cumplimiento` | `text` | sí | _Por documentar_ |  |
| 15 | `meta_indicador` | `character varying(100)` | sí | _Por documentar_ |  |
| 16 | `estado` | `character varying(30)` | sí | _Por documentar_ |  |
| 17 | `porcentaje_avance` | `integer` | sí | _Por documentar_ |  |
| 18 | `fecha_ultimo_reporte` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 19 | `fecha_proximo_reporte` | `date` | sí | _Por documentar_ |  |
| 20 | `periodicidad_reporte` | `character varying(20)` | sí | _Por documentar_ |  |
| 21 | `documento_plan_url` | `text` | sí | _Por documentar_ |  |
| 22 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 23 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 24 | `created_by` | `character varying(150)` | sí | _Por documentar_ |  |

## historial_consultas

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `consulta_id` → `legal_management.consultas_juridicas` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `consulta_id` | `uuid` | no | _Por documentar_ | FK→legal_management.consultas_juridicas.id |
| 3 | `accion` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `estado_anterior` | `character varying(30)` | sí | _Por documentar_ |  |
| 6 | `estado_nuevo` | `character varying(30)` | sí | _Por documentar_ |  |
| 7 | `usuario_nombre` | `character varying(150)` | sí | _Por documentar_ |  |
| 8 | `fecha` | `timestamp without time zone` | sí | _Por documentar_ |  |

## notas_expediente

Notas internas de los abogados sobre el expediente

- Clave primaria: `id`
- Filas: 3
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `expediente_id` | `uuid` | no | _Por documentar_ | FK→legal_management.expedientes.id |
| 3 | `contenido` | `text` | no | _Por documentar_ |  |
| 4 | `tipo` | `character varying(30)` | sí | Tipo de nota: importante, seguimiento, informacion, general, alerta |  |
| 5 | `autor_id` | `uuid` | sí | _Por documentar_ |  |
| 6 | `autor_nombre` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 8 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## oficios_enviados

Oficios judiciales enviados desde el sistema, con soporte para plantillas institucionales ESAP

- Clave primaria: `id`
- Filas: 4

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `numero` | `character varying(50)` | no | _Por documentar_ |  |
| 3 | `expediente_id` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `modulo` | `character varying(50)` | sí | _Por documentar_ |  |
| 5 | `asunto` | `character varying(500)` | no | _Por documentar_ |  |
| 6 | `destinatario` | `character varying(300)` | no | _Por documentar_ |  |
| 7 | `destinatario_email` | `character varying(200)` | sí | _Por documentar_ | Contacto |
| 8 | `contenido` | `text` | no | _Por documentar_ |  |
| 9 | `contenido_html` | `text` | sí | _Por documentar_ |  |
| 10 | `firma` | `character varying(200)` | sí | _Por documentar_ |  |
| 11 | `plantilla` | `character varying(50)` | sí | _Por documentar_ |  |
| 12 | `estado` | `character varying(30)` | sí | _Por documentar_ |  |
| 13 | `fecha_envio` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 14 | `archivos_adjuntos` | `jsonb` | sí | _Por documentar_ |  |
| 15 | `graph_message_id` | `character varying(200)` | sí | _Por documentar_ |  |
| 16 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 17 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## organismos_control

_Por documentar._

- Clave primaria: `id`
- Filas: 9

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | _Por documentar_ | PK |
| 2 | `sigla` | `character varying(20)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(200)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 6 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 7 | `correos` | `jsonb` | no | _Por documentar_ |  |
| 8 | `updated_at` | `timestamp with time zone` | no | _Por documentar_ |  |

## pagos_coactivos

_Por documentar._

- Clave primaria: `id`
- Filas: 10
- Referencia a: `proceso_id` → `legal_management.procesos_coactivos` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `proceso_id` | `uuid` | no | _Por documentar_ | FK→legal_management.procesos_coactivos.id |
| 3 | `valor` | `numeric(15,2)` | no | _Por documentar_ |  |
| 4 | `fecha_pago` | `timestamp without time zone` | no | _Por documentar_ |  |
| 5 | `soporte_url` | `text` | sí | _Por documentar_ |  |
| 6 | `origen` | `character varying(50)` | sí | _Por documentar_ |  |
| 7 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 8 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 10 | `abono_capital` | `numeric(15,2)` | sí | _Por documentar_ |  |
| 11 | `abono_intereses` | `numeric(15,2)` | sí | _Por documentar_ |  |
| 12 | `abono_costas` | `numeric(15,2)` | sí | _Por documentar_ |  |

## pei_indicadores

_Por documentar._

- Clave primaria: `id`
- Filas: 24

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | _Por documentar_ | PK |
| 2 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 3 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 4 | `eje_estrategico` | `character varying(50)` | no | _Por documentar_ |  |
| 5 | `meta_objetivo` | `numeric(10,2)` | no | _Por documentar_ |  |
| 6 | `unidad_medida` | `character varying(20)` | sí | _Por documentar_ |  |
| 7 | `fecha_inicio` | `date` | no | _Por documentar_ |  |
| 8 | `fecha_fin` | `date` | no | _Por documentar_ |  |
| 9 | `frecuencia_medicion` | `character varying(20)` | sí | _Por documentar_ |  |
| 10 | `responsable_id` | `uuid` | sí | _Por documentar_ |  |
| 11 | `responsable_nombre` | `character varying(200)` | sí | _Por documentar_ |  |
| 12 | `estado` | `character varying(20)` | sí | _Por documentar_ |  |
| 13 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 15 | `prioridad` | `character varying(20)` | sí | _Por documentar_ |  |
| 16 | `tipo_indicador` | `character varying(50)` | sí | _Por documentar_ |  |
| 17 | `archived_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 18 | `archived_by` | `character varying(255)` | sí | _Por documentar_ |  |
| 19 | `archive_reason` | `text` | sí | _Por documentar_ |  |

## pei_registros_avance

_Por documentar._

- Clave primaria: `id`
- Filas: 24
- Referencia a: `indicador_id` → `legal_management.pei_indicadores` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | _Por documentar_ | PK |
| 2 | `indicador_id` | `integer` | sí | _Por documentar_ | FK→legal_management.pei_indicadores.id |
| 3 | `valor_reportado` | `numeric(10,2)` | no | _Por documentar_ |  |
| 4 | `porcentaje_avance` | `numeric(5,2)` | sí | _Por documentar_ |  |
| 5 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 6 | `evidencia_url` | `text` | sí | _Por documentar_ |  |
| 7 | `fecha_registro` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 8 | `usuario_registra_id` | `uuid` | sí | _Por documentar_ |  |

## planes_comentarios

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `plan_id` → `legal_management.planes_mejoramiento` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `plan_id` | `uuid` | sí | _Por documentar_ | FK→legal_management.planes_mejoramiento.id |
| 3 | `mensaje` | `text` | no | _Por documentar_ |  |
| 4 | `usuario_id` | `uuid` | sí | _Por documentar_ |  |
| 5 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## planes_evidencias

_Por documentar._

- Clave primaria: `id`
- Filas: 14
- Referencia a: `plan_id` → `legal_management.planes_mejoramiento` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `plan_id` | `uuid` | sí | _Por documentar_ | FK→legal_management.planes_mejoramiento.id |
| 3 | `titulo` | `character varying(150)` | no | _Por documentar_ |  |
| 4 | `url_archivo` | `text` | no | _Por documentar_ |  |
| 5 | `tipo_archivo` | `character varying(255)` | sí | _Por documentar_ |  |
| 6 | `uploaded_by` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## planes_hallazgos

_Por documentar._

- Clave primaria: `id`
- Filas: 4
- Referencia a: `plan_id` → `legal_management.planes_mejoramiento` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `plan_id` | `uuid` | no | _Por documentar_ | FK→legal_management.planes_mejoramiento.id |
| 3 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `porcentaje_avance` | `integer` | no | _Por documentar_ |  |
| 6 | `archivo_url` | `text` | sí | _Por documentar_ |  |
| 7 | `archivo_nombre` | `character varying(255)` | sí | _Por documentar_ |  |
| 8 | `archivo_mime` | `character varying(100)` | sí | _Por documentar_ |  |
| 9 | `created_by` | `character varying(150)` | sí | _Por documentar_ |  |
| 10 | `created_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 11 | `updated_at` | `timestamp with time zone` | no | _Por documentar_ |  |

## planes_mejoramiento

_Por documentar._

- Clave primaria: `id`
- Filas: 22

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(50)` | no | _Por documentar_ | única |
| 3 | `titulo` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `origen` | `character varying(50)` | no | _Por documentar_ |  |
| 6 | `origen_id` | `uuid` | sí | _Por documentar_ |  |
| 7 | `responsable_id` | `uuid` | sí | _Por documentar_ |  |
| 8 | `fecha_inicio` | `date` | no | _Por documentar_ |  |
| 9 | `fecha_fin_estimada` | `date` | no | _Por documentar_ |  |
| 10 | `fecha_cierre_real` | `date` | sí | _Por documentar_ |  |
| 11 | `avance_porcentaje` | `numeric(5,2)` | sí | _Por documentar_ |  |
| 12 | `presupuesto` | `numeric(15,2)` | sí | _Por documentar_ |  |
| 13 | `estado` | `character varying(20)` | sí | _Por documentar_ |  |
| 14 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 15 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 16 | `documento_origen` | `character varying(255)` | sí | Identificador o nombre del documento base (ej: Informe de Auditoría) |  |
| 17 | `area_responsable` | `character varying(255)` | sí | Nombre del área encargada dentro de la entidad |  |
| 18 | `fecha_recepcion` | `date` | sí | _Por documentar_ |  |
| 19 | `fecha_respuesta` | `date` | sí | _Por documentar_ |  |
| 20 | `severidad` | `character varying(50)` | sí | Nivel de criticidad: CRITICO, ALTO, MEDIO, BAJO |  |
| 21 | `responsable_nombre` | `character varying(255)` | sí | Text name of responsible person when no abogado is linked |  |
| 22 | `archived_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 23 | `archived_by` | `character varying(255)` | sí | _Por documentar_ |  |
| 24 | `archive_reason` | `text` | sí | _Por documentar_ |  |

## planes_seguimientos

_Por documentar._

- Clave primaria: `id`
- Filas: 22
- Referencia a: `plan_id` → `legal_management.planes_mejoramiento` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `plan_id` | `uuid` | sí | _Por documentar_ | FK→legal_management.planes_mejoramiento.id |
| 3 | `descripcion_avance` | `text` | no | _Por documentar_ |  |
| 4 | `porcentaje_reportado` | `numeric(5,2)` | sí | _Por documentar_ |  |
| 5 | `fecha_reporte` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 6 | `usuario_id` | `uuid` | sí | _Por documentar_ |  |

## plantillas_documentos

_Por documentar._

- Clave primaria: `id`
- Filas: 5

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `nombre` | `character varying(500)` | no | _Por documentar_ |  |
| 3 | `categoria` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `nombre_original` | `character varying(500)` | no | _Por documentar_ |  |
| 5 | `mime_type` | `character varying(100)` | no | _Por documentar_ |  |
| 6 | `tamano` | `integer` | no | _Por documentar_ |  |
| 7 | `contenido_base64` | `text` | no | _Por documentar_ |  |
| 8 | `subido_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 9 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 10 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |

## procesos_coactivos

Tabla de procesos de cobro coactivo - Módulo Gestión Legal

- Clave primaria: `id`
- Filas: 7

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `radicado` | `character varying(50)` | no | _Por documentar_ | única |
| 3 | `deudor` | `jsonb` | no | Información del deudor en formato JSON (nombre, identificacion, telefono, email, direccion) |  |
| 4 | `obligacion` | `jsonb` | no | Información de la obligación en formato JSON (concepto, valor, fechaVencimiento) |  |
| 5 | `estado` | `legal_management.estado_proceso_coactivo` | sí | _Por documentar_ |  |
| 6 | `responsable` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `documentos_adjuntos` | `integer` | sí | _Por documentar_ |  |
| 8 | `notificaciones_enviadas` | `integer` | sí | _Por documentar_ |  |
| 9 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 10 | `ultima_actuacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `fecha_creacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 13 | `valor_pagado` | `numeric(15,2)` | sí | _Por documentar_ |  |
| 14 | `saldo_pendiente` | `numeric(15,2)` | sí | _Por documentar_ |  |
| 15 | `estado_archivo` | `character varying(20)` | sí | _Por documentar_ |  |
| 16 | `fecha_archivo` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 17 | `usuario_archivo` | `character varying(150)` | sí | _Por documentar_ |  |
| 18 | `motivo_archivo` | `text` | sí | _Por documentar_ |  |
| 19 | `fecha_ejecutoria` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 20 | `tipo_interes_aplicable` | `character varying(20)` | sí | _Por documentar_ |  |
| 21 | `valor_costas` | `numeric(15,2)` | sí | _Por documentar_ |  |

## procesos_coactivos_adjuntos

_Por documentar._

- Clave primaria: `id`
- Filas: 13
- Referencia a: `proceso_id` → `legal_management.procesos_coactivos` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `proceso_id` | `uuid` | no | _Por documentar_ | FK→legal_management.procesos_coactivos.id |
| 3 | `nombre_original` | `character varying` | no | _Por documentar_ |  |
| 4 | `nombre_archivo` | `character varying` | no | _Por documentar_ |  |
| 5 | `mime_type` | `character varying` | no | _Por documentar_ |  |
| 6 | `tamano` | `integer` | no | _Por documentar_ |  |
| 7 | `fecha_creacion` | `timestamp without time zone` | no | _Por documentar_ |  |
| 8 | `tipo` | `character varying(100)` | sí | _Por documentar_ |  |
| 9 | `archivo_url` | `character varying(500)` | sí | _Por documentar_ |  |
| 10 | `es_titulo_ejecutivo` | `boolean` | sí | _Por documentar_ |  |

## requerimientos_oc

_Por documentar._

- Clave primaria: `id`
- Filas: 14

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `radicado_externo` | `character varying(100)` | no | _Por documentar_ |  |
| 3 | `radicado_interno` | `character varying(30)` | no | _Por documentar_ | única |
| 4 | `organismo_id` | `character varying(255)` | sí | _Por documentar_ |  |
| 5 | `tipo_requerimiento` | `character varying(50)` | no | _Por documentar_ |  |
| 6 | `asunto` | `text` | no | _Por documentar_ |  |
| 7 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 8 | `fecha_recepcion` | `timestamp without time zone` | no | _Por documentar_ |  |
| 9 | `unidad_tiempo` | `character varying(20)` | sí | _Por documentar_ |  |
| 10 | `plazo_otorgado` | `integer` | no | _Por documentar_ |  |
| 11 | `fecha_vencimiento` | `timestamp without time zone` | no | _Por documentar_ |  |
| 12 | `funcionario_responsable` | `character varying(200)` | sí | _Por documentar_ |  |
| 13 | `area_responsable` | `character varying(150)` | sí | _Por documentar_ |  |
| 14 | `abogado_asignado_id` | `uuid` | sí | _Por documentar_ |  |
| 15 | `estado` | `character varying(30)` | sí | _Por documentar_ |  |
| 16 | `prioridad` | `character varying(15)` | sí | _Por documentar_ |  |
| 17 | `archivo_adjunto_url` | `text` | sí | _Por documentar_ |  |
| 18 | `oficio_respuesta_url` | `text` | sí | _Por documentar_ |  |
| 19 | `acuse_recibo_url` | `text` | sí | _Por documentar_ |  |
| 20 | `fecha_respuesta` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 21 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 22 | `created_by` | `character varying(150)` | sí | _Por documentar_ |  |
| 23 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 24 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 25 | `estado_archivo` | `character varying` | sí | Estado del requerimiento en el sistema de archivo: ACTIVO, ARCHIVADO, ELIMINADO |  |
| 26 | `fecha_archivo` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 27 | `usuario_archivo` | `character varying` | sí | _Por documentar_ |  |
| 28 | `motivo_archivo` | `text` | sí | _Por documentar_ |  |

## respuesta_borrador_oc

Almacena borradores de respuestas a requerimientos de órganos de control

- Clave primaria: `id`
- Filas: 2
- Referencia a: `requerimiento_id` → `legal_management.requerimientos_oc` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `requerimiento_id` | `uuid` | no | _Por documentar_ | única FK→legal_management.requerimientos_oc.id |
| 3 | `destinatario_nombre` | `character varying(200)` | sí | _Por documentar_ |  |
| 4 | `destinatario_email` | `character varying(200)` | sí | _Por documentar_ | Contacto |
| 5 | `destinatario_cargo` | `character varying(150)` | sí | _Por documentar_ |  |
| 6 | `tipo_respuesta` | `character varying(50)` | sí | _Por documentar_ |  |
| 7 | `contenido` | `text` | sí | _Por documentar_ |  |
| 8 | `documentos_adjuntos` | `jsonb` | sí | _Por documentar_ |  |
| 9 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 10 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## riesgo_historial

Historial de cambios y eventos de riesgos para trazabilidad

- Clave primaria: `id`
- Filas: 8
- Referencia a: `riesgo_id` → `legal_management.riesgos` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `riesgo_id` | `uuid` | no | _Por documentar_ | FK→legal_management.riesgos.id |
| 3 | `tipo_evento` | `character varying(50)` | no | Tipo: CREACION, ACTUALIZACION, CAMBIO_ETAPA, CAMBIO_ZONA, ARCHIVADO, CONTROL_AGREGADO, etc. |  |
| 4 | `descripcion` | `text` | no | _Por documentar_ |  |
| 5 | `campo_modificado` | `character varying(100)` | sí | Campo que fue modificado (e.g. etapa, probabilidad, impacto) |  |
| 6 | `valor_anterior` | `text` | sí | Valor antes del cambio |  |
| 7 | `valor_nuevo` | `text` | sí | Valor después del cambio |  |
| 8 | `usuario` | `character varying(200)` | sí | _Por documentar_ |  |
| 9 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## riesgos

_Por documentar._

- Clave primaria: `id`
- Filas: 6

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(30)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | no | _Por documentar_ |  |
| 5 | `proceso` | `character varying(100)` | no | _Por documentar_ |  |
| 6 | `tipo_riesgo` | `character varying(30)` | no | _Por documentar_ |  |
| 7 | `etapa` | `character varying(30)` | sí | _Por documentar_ |  |
| 8 | `probabilidad_inherente` | `integer` | sí | _Por documentar_ |  |
| 9 | `impacto_inherente` | `integer` | sí | _Por documentar_ |  |
| 10 | `zona_inherente` | `character varying(20)` | sí | _Por documentar_ |  |
| 11 | `probabilidad_residual` | `integer` | sí | _Por documentar_ |  |
| 12 | `impacto_residual` | `integer` | sí | _Por documentar_ |  |
| 13 | `zona_residual` | `character varying(20)` | sí | _Por documentar_ |  |
| 14 | `causas` | `jsonb` | sí | _Por documentar_ |  |
| 15 | `consecuencias` | `jsonb` | sí | _Por documentar_ |  |
| 16 | `controles_existentes` | `jsonb` | sí | _Por documentar_ |  |
| 17 | `plan_tratamiento` | `jsonb` | sí | _Por documentar_ |  |
| 18 | `responsable` | `character varying(200)` | no | _Por documentar_ |  |
| 19 | `responsable_id` | `uuid` | sí | _Por documentar_ |  |
| 20 | `estado` | `character varying(20)` | sí | _Por documentar_ |  |
| 21 | `created_by` | `character varying(200)` | sí | _Por documentar_ |  |
| 22 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 23 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 24 | `cuantia_estimada` | `numeric(15,2)` | sí | Valor monetario estimado del riesgo |  |
| 25 | `provision_contable` | `numeric(15,2)` | sí | Provisión contable calculada = cuantía × porcentaje |  |
| 26 | `porcentaje_provision` | `integer` | sí | Porcentaje aplicado según zona: EXTREMO=100, ALTO=75, MODERADO=50, BAJO=25 |  |
| 27 | `fecha_calculo_provision` | `timestamp without time zone` | sí | Fecha del último cálculo de provisión |  |
| 28 | `modulo_origen` | `character varying(50)` | sí | Módulo fuente: DEFENSA_JUDICIAL, JUZGAMIENTO, ASESORIA_JURIDICA, COACTIVOS, ORGANOS_CONTROL |  |
| 29 | `proceso_id` | `uuid` | sí | UUID del proceso asociado en el módulo correspondiente |  |
| 30 | `proceso_radicado` | `character varying(100)` | sí | Radicado o número del proceso para referencia rápida |  |
| 31 | `motivo_archivo` | `text` | sí | _Por documentar_ |  |

## sequences

_Por documentar._

- Clave primaria: `name`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `name` | `character varying(100)` | no | _Por documentar_ | PK |
| 2 | `current_value` | `integer` | no | _Por documentar_ |  |
| 3 | `updated_at` | `timestamp with time zone` | no | _Por documentar_ |  |

## solicitudes_insumos

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `requerimiento_id` → `legal_management.requerimientos_oc` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `requerimiento_id` | `uuid` | no | _Por documentar_ | FK→legal_management.requerimientos_oc.id |
| 3 | `area_destino` | `character varying(150)` | no | _Por documentar_ |  |
| 4 | `funcionario_destino` | `character varying(200)` | sí | _Por documentar_ |  |
| 5 | `email_destino` | `character varying(150)` | sí | _Por documentar_ | Contacto |
| 6 | `descripcion_solicitud` | `text` | no | _Por documentar_ |  |
| 7 | `documentos_solicitados` | `text` | sí | _Por documentar_ |  |
| 8 | `fecha_solicitud` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 9 | `fecha_vencimiento_interna` | `timestamp without time zone` | no | _Por documentar_ |  |
| 10 | `fecha_respuesta` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `estado` | `character varying(25)` | sí | _Por documentar_ |  |
| 12 | `documentos_entregados_url` | `text` | sí | _Por documentar_ |  |
| 13 | `comentario_respuesta` | `text` | sí | _Por documentar_ |  |
| 14 | `solicitado_por` | `character varying(150)` | sí | _Por documentar_ |  |
| 15 | `respondido_por` | `character varying(150)` | sí | _Por documentar_ |  |
| 16 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 17 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## system_configurations

_Por documentar._

- Clave primaria: `key`
- Filas: 8

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `key` | `character varying` | no | _Por documentar_ | PK |
| 2 | `module` | `character varying` | no | _Por documentar_ |  |
| 3 | `value` | `jsonb` | no | _Por documentar_ |  |
| 4 | `description` | `text` | sí | _Por documentar_ |  |
| 5 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 6 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |

## tareas_expediente

Tareas asociadas a expedientes judiciales para control de actividades

- Clave primaria: `id`
- Filas: 35
- Referencia a: `expediente_id` → `legal_management.expedientes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `expediente_id` | `uuid` | no | _Por documentar_ | FK→legal_management.expedientes.id |
| 3 | `titulo` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `fecha_vencimiento` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 6 | `prioridad` | `character varying(20)` | sí | Nivel de prioridad: alta, media, baja |  |
| 7 | `estado` | `character varying(30)` | sí | Estado de la tarea: pendiente, en_proceso, completada, cancelada |  |
| 8 | `responsable_id` | `uuid` | sí | _Por documentar_ |  |
| 9 | `responsable_nombre` | `character varying(255)` | sí | _Por documentar_ |  |
| 10 | `fecha_creacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `fecha_completada` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `creado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 13 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## tasas_referencia

_Por documentar._

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `anio` | `integer` | no | _Por documentar_ |  |
| 3 | `mes` | `integer` | no | _Por documentar_ |  |
| 4 | `valor_tasa` | `numeric(5,2)` | no | _Por documentar_ |  |
| 5 | `tipo_tasa` | `character varying(20)` | no | _Por documentar_ |  |
| 6 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 7 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## terminos_alertas_enviadas

_Por documentar._

- Clave primaria: `id`
- Filas: 109
- Referencia a: `regla_id` → `legal_management.terminos_reglas_alerta` (1..* → 0..1); `termino_id` → `legal_management.terminos_procesales` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `termino_id` | `uuid` | no | _Por documentar_ | FK→legal_management.terminos_procesales.id |
| 3 | `regla_id` | `uuid` | sí | _Por documentar_ | FK→legal_management.terminos_reglas_alerta.id |
| 4 | `fecha_envio` | `timestamp with time zone` | no | _Por documentar_ |  |

## terminos_procesales

Torre de control transversal para vencimientos de términos procesales de todos los módulos

- Clave primaria: `id`
- Filas: 233

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `origen_modulo` | `character varying(50)` | no | _Por documentar_ |  |
| 3 | `referencia_id` | `uuid` | sí | _Por documentar_ |  |
| 4 | `numero_radicado` | `character varying(100)` | sí | _Por documentar_ |  |
| 5 | `nombre_actuacion` | `character varying(255)` | no | _Por documentar_ |  |
| 6 | `fecha_base` | `timestamp with time zone` | no | _Por documentar_ |  |
| 7 | `dias_termino` | `integer` | no | _Por documentar_ |  |
| 8 | `tipo_dias` | `character varying(20)` | sí | _Por documentar_ |  |
| 9 | `fecha_vencimiento` | `timestamp with time zone` | no | _Por documentar_ |  |
| 10 | `fecha_alerta_preventiva` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 11 | `fecha_alerta_critica` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 12 | `estado` | `character varying(20)` | sí | _Por documentar_ |  |
| 13 | `prioridad` | `character varying(10)` | sí | _Por documentar_ |  |
| 14 | `responsable_id` | `uuid` | sí | _Por documentar_ |  |
| 15 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 16 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 17 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 18 | `closed_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 19 | `responsable_nombre` | `character varying(255)` | sí | _Por documentar_ |  |
| 20 | `destinatario` | `character varying(255)` | sí | _Por documentar_ |  |
| 21 | `fundamento_normativo` | `jsonb` | sí | _Por documentar_ |  |
| 22 | `ente_solicitante` | `character varying(255)` | sí | _Por documentar_ |  |
| 23 | `horas_anticipacion_alerta_personalizada` | `integer` | sí | _Por documentar_ |  |
| 24 | `recordatorio_manual_horas_anticipacion` | `integer` | sí | _Por documentar_ |  |
| 25 | `ultimo_recordatorio_recurrente_en` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 26 | `alerta_vencimiento_enviada_en` | `timestamp with time zone` | sí | _Por documentar_ |  |

## terminos_reglas_alerta

_Por documentar._

- Clave primaria: `id`
- Filas: 2

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `horas_anticipacion` | `integer` | no | _Por documentar_ | única |
| 3 | `activa` | `boolean` | no | _Por documentar_ |  |
| 4 | `enviar_email` | `boolean` | no | _Por documentar_ |  |
| 5 | `notificar_in_app` | `boolean` | no | _Por documentar_ |  |
| 6 | `descripcion` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `created_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 8 | `updated_at` | `timestamp with time zone` | no | _Por documentar_ |  |
