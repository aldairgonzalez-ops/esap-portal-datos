# Viáticos y gastos de viaje (`travel_expenses`)

_Descripción del dominio por documentar._

30 tablas · 0 vistas · 402 columnas · 208 filas · 7 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`analistas_viaticos`](#analistas_viaticos) | Tabla | 0 | Catalogo de analistas del Grupo de Viaticos para asignacion de comisiones y calculo de carga laboral |
| [`comisionados`](#comisionados) | Tabla | 4 | _Por documentar_ |
| [`config_campos_formulario`](#config_campos_formulario) | Tabla | 19 | _Por documentar_ |
| [`config_jornada_laboral`](#config_jornada_laboral) | Tabla | 1 | _Por documentar_ |
| [`config_legalizacion`](#config_legalizacion) | Tabla | 2 | EFDS-1309 — Disparador, plazo (días hábiles) y aviso de la legalización por modalidad de pago. |
| [`config_legalizacion_documentos`](#config_legalizacion_documentos) | Tabla | 42 | EFDS-1309 — Soportes exigidos para legalizar, por tipo de comisionado. Configuración, no código (D-2). |
| [`config_tipo_comisionado`](#config_tipo_comisionado) | Tabla | 7 | _Por documentar_ |
| [`config_tipo_comisionado_documentos`](#config_tipo_comisionado_documentos) | Tabla | 24 | _Por documentar_ |
| [`configuraciones_globales`](#configuraciones_globales) | Tabla | 6 | _Por documentar_ |
| [`documentos_soporte`](#documentos_soporte) | Tabla | 0 | _Por documentar_ |
| [`escalas_viaticos`](#escalas_viaticos) | Tabla | 11 | _Por documentar_ |
| [`excepciones_autorizadas_tiquetes`](#excepciones_autorizadas_tiquetes) | Tabla | 0 | _Por documentar_ |
| [`legalizacion_reversiones`](#legalizacion_reversiones) | Tabla | 0 | EFDS-1310 — Solicitudes de reversión de una revisión de legalización aprobada. La solicita el analista y la resuelve otra persona; solo antes del registro en SIIF. |
| [`legalizacion_revisiones`](#legalizacion_revisiones) | Tabla | 0 | EFDS-1310 — Trazabilidad de la revisión de la legalización (quién, qué, cuándo). Solo inserción. |
| [`legalizacion_soportes`](#legalizacion_soportes) | Tabla | 0 | EFDS-1309 — PDF de soporte de la legalización, validados por contenido (%PDF-), no por extensión. |
| [`legalizaciones_comision`](#legalizaciones_comision) | Tabla | 0 | EFDS-1309 — Legalización de una comisión: plazo en días hábiles y envío a revisión. |
| [`liquidation_params`](#liquidation_params) | Tabla | 5 | _Por documentar_ |
| [`parametros_globales`](#parametros_globales) | Tabla | 1 | Parametros globales configurables del modulo de viaticos y comisiones |
| [`paz_y_salvo_eventos`](#paz_y_salvo_eventos) | Tabla | 0 | _Por documentar_ |
| [`paz_y_salvos`](#paz_y_salvos) | Tabla | 0 | _Por documentar_ |
| [`reintegros_comision`](#reintegros_comision) | Tabla | 0 | Reintegros de comisiones pagadas por avance no realizadas o ejecutadas por menos días (RF-PAG-004). |
| [`rutas_restringidas`](#rutas_restringidas) | Tabla | 4 | _Por documentar_ |
| [`saldos_tiquetes`](#saldos_tiquetes) | Tabla | 0 | _Por documentar_ |
| [`solicitudes_comision`](#solicitudes_comision) | Tabla | 3 | _Por documentar_ |
| [`solicitudes_historial_estados`](#solicitudes_historial_estados) | Tabla | 0 | Auditoría append-only de transiciones de estado del expediente de comisión (RF-SIS-001 / RF-LIQ-004). |
| [`tarifas_investigadores`](#tarifas_investigadores) | Tabla | 3 | _Por documentar_ |
| [`tarifas_referencia_tiquetes`](#tarifas_referencia_tiquetes) | Tabla | 42 | _Por documentar_ |
| [`tarifas_regionales_excepcion`](#tarifas_regionales_excepcion) | Tabla | 8 | _Por documentar_ |
| [`tarifas_transporte_terminal`](#tarifas_transporte_terminal) | Tabla | 11 | _Por documentar_ |
| [`tipos_documento_soporte`](#tipos_documento_soporte) | Tabla | 15 | _Por documentar_ |

## analistas_viaticos

Catalogo de analistas del Grupo de Viaticos para asignacion de comisiones y calculo de carga laboral

- Clave primaria: `id`
- Filas: 0
- Referencia a: `usuario_id` → `auth.user` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla analistas_viaticos. Se genera automáticamente. | PK |
| 2 | `usuario_id` | `uuid` | no | Referencia al usuario del sistema (auth.user.id_user) | única FK→auth.user.id_user |
| 3 | `id_persona` | `uuid` | sí | Referencia a la persona en auth.personas |  |
| 4 | `identificacion` | `character varying(50)` | sí | Numero de identificacion del analista | única |
| 5 | `nombre_completo` | `character varying(255)` | no | Nombre completo del analista | Nombre de persona |
| 6 | `username` | `character varying(100)` | no | Usuario de acceso del analista |  |
| 7 | `email` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 8 | `telefono` | `character varying(50)` | sí | _Por documentar_ | Contacto |
| 9 | `cargo` | `character varying(255)` | sí | _Por documentar_ |  |
| 10 | `activo` | `boolean` | sí | Indica si el analista esta activo para recibir asignaciones |  |
| 11 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 13 | `dependencia_id` | `bigint` | sí | ID de la dependencia a la que pertenece el analista (auth.dependencias.id_dependencia). |  |

## comisionados

_Por documentar._

- Clave primaria: `id`
- Filas: 4

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla comisionados. Se genera automáticamente. | PK |
| 2 | `numero_documento` | `character varying(20)` | no | _Por documentar_ | única Identificación |
| 3 | `primer_nombre` | `character varying(100)` | no | _Por documentar_ | Nombre de persona |
| 4 | `segundo_nombre` | `character varying(100)` | sí | _Por documentar_ | Nombre de persona |
| 5 | `primer_apellido` | `character varying(100)` | no | _Por documentar_ | Nombre de persona |
| 6 | `segundo_apellido` | `character varying(100)` | sí | _Por documentar_ | Nombre de persona |
| 7 | `email` | `character varying(150)` | no | _Por documentar_ | Contacto |
| 8 | `telefono_contacto` | `character varying(150)` | no | _Por documentar_ | Contacto |
| 9 | `tipo_comisionado` | `character varying(50)` | no | _Por documentar_ |  |
| 10 | `origen_datos` | `character varying(50)` | no | _Por documentar_ |  |
| 11 | `autorizacion_habeas_data` | `boolean` | no | _Por documentar_ |  |
| 12 | `fecha_autorizacion_habeas_data` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 13 | `ip_registro_habeas_data` | `character varying(45)` | sí | _Por documentar_ | Identificador en línea (IP) |
| 14 | `creado_en` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 15 | `actualizado_en` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 16 | `id_dependencia` | `bigint` | sí | ID de la dependencia institucional (auth.dependencias) del comisionado. Se obtiene desde auth.personas.id_dependencia al consultar por número de documento. |  |
| 17 | `es_facturador_electronico` | `boolean` | no | Indica si el comisionado contratista es facturador electrónico registrado ante la DIAN. |  |
| 18 | `fecha_inicio_contrato` | `date` | sí | Fecha de inicio de la vinculación contractual o laboral. |  |
| 19 | `fecha_fin_contrato` | `date` | sí | Fecha de terminación o vencimiento del contrato/vinculación laboral. |  |
| 20 | `cuentas_bancarias` | `jsonb` | sí | Historial y lista de cuentas bancarias del comisionado (banco, tipo_cuenta, numero_cuenta, url_certificado, etc.). |  |
| 21 | `cargos` | `jsonb` | sí | Historial y asignación de cargos del comisionado con su respectivo salario relacional (formato JSONB). Reemplaza y unifica las columnas cargo y salario_basico. |  |

## config_campos_formulario

_Por documentar._

- Clave primaria: `id`
- Filas: 19

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla config_campos_formulario. Se genera automáticamente. | PK |
| 2 | `clave` | `character varying(100)` | no | _Por documentar_ | única |
| 3 | `etiqueta` | `character varying(200)` | no | _Por documentar_ |  |
| 4 | `tipo_campo` | `character varying(50)` | no | _Por documentar_ |  |
| 5 | `placeholder` | `character varying(200)` | sí | _Por documentar_ |  |
| 6 | `opciones` | `jsonb` | sí | _Por documentar_ |  |
| 7 | `grupo` | `character varying(50)` | sí | _Por documentar_ |  |
| 8 | `orden` | `integer` | no | _Por documentar_ |  |
| 9 | `activo` | `boolean` | no | _Por documentar_ |  |
| 10 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 11 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 12 | `limite_caracteres` | `integer` | sí | Límite máximo de caracteres permitido para el campo. Por defecto 250 caracteres, configurable por administrador. |  |

## config_jornada_laboral

_Por documentar._

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla config_jornada_laboral. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(50)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `hora_inicio` | `character varying(5)` | no | _Por documentar_ |  |
| 5 | `hora_fin` | `character varying(5)` | no | _Por documentar_ |  |
| 6 | `dias_laborales` | `jsonb` | no | _Por documentar_ |  |
| 7 | `dias_anticipacion_minima` | `integer` | no | _Por documentar_ |  |
| 8 | `dias_umbral_avance` | `integer` | no | _Por documentar_ |  |
| 9 | `activo` | `boolean` | no | _Por documentar_ |  |
| 10 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 11 | `creado_en` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 12 | `actualizado_en` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 13 | `actualizado_por` | `character varying(100)` | sí | Usuario que realizó la última actualización del registro. |  |

## config_legalizacion

EFDS-1309 — Disparador, plazo (días hábiles) y aviso de la legalización por modalidad de pago.

- Clave primaria: `modalidad_pago`
- Filas: 2

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `modalidad_pago` | `character varying(50)` | no | Clave primaria de la tabla config_legalizacion: modalidad pago. | PK |
| 2 | `estado_disparador` | `character varying(50)` | no | Estado de la solicitud a partir del cual se abre la legalización. Pendiente D-1 para RECONOCIMIENTO_POSTERIOR. |  |
| 3 | `plazo_dias_habiles` | `integer` | no | _Por documentar_ |  |
| 4 | `dias_aviso_por_vencer` | `integer` | no | _Por documentar_ |  |
| 5 | `hora_corte` | `character varying(5)` | no | Hora (Colombia, HH:MM) en que vence el último día hábil del plazo. Alineada con el corte de jornada de 16:30. |  |
| 6 | `activo` | `boolean` | no | _Por documentar_ |  |
| 7 | `actualizado_por_id` | `uuid` | sí | _Por documentar_ |  |
| 8 | `creado_en` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `actualizado_en` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## config_legalizacion_documentos

EFDS-1309 — Soportes exigidos para legalizar, por tipo de comisionado. Configuración, no código (D-2).

- Clave primaria: `id`
- Filas: 42
- Referencia a: `config_tipo_comisionado_id` → `travel_expenses.config_tipo_comisionado` (1..* → 1); `tipo_documento_soporte_id` → `travel_expenses.tipos_documento_soporte` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla config_legalizacion_documentos. Se genera automáticamente. | PK |
| 2 | `config_tipo_comisionado_id` | `uuid` | no | Referencia al registro de travel_expenses.config_tipo_comisionado (id). | FK→travel_expenses.config_tipo_comisionado.id |
| 3 | `tipo_documento_soporte_id` | `uuid` | no | Referencia al registro de travel_expenses.tipos_documento_soporte (id). | FK→travel_expenses.tipos_documento_soporte.id |
| 4 | `tipo_requisito` | `character varying(20)` | no | _Por documentar_ |  |
| 5 | `condicion` | `character varying(40)` | sí | Cuándo aplica: NULL = siempre; TRANSPORTE_AEREO = solo con tramo aéreo; COMISION_EXTERNA = solo si se cumplió fuera de la ESAP. |  |
| 6 | `orden` | `integer` | no | _Por documentar_ |  |
| 7 | `activo` | `boolean` | no | _Por documentar_ |  |
| 8 | `creado_en` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `actualizado_en` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## config_tipo_comisionado

_Por documentar._

- Clave primaria: `id`
- Filas: 7

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla config_tipo_comisionado. Se genera automáticamente. | PK |
| 2 | `tipo_comisionado` | `character varying(50)` | no | _Por documentar_ | única |
| 3 | `codigo_formulario` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `campos_obligatorios` | `jsonb` | no | _Por documentar_ |  |
| 5 | `campos_opcionales` | `jsonb` | no | _Por documentar_ |  |
| 6 | `campos_ocultos` | `jsonb` | no | _Por documentar_ |  |
| 7 | `activo` | `boolean` | no | _Por documentar_ |  |
| 8 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## config_tipo_comisionado_documentos

_Por documentar._

- Clave primaria: `id`
- Filas: 24
- Referencia a: `config_tipo_comisionado_id` → `travel_expenses.config_tipo_comisionado` (1..* → 1); `tipo_documento_soporte_id` → `travel_expenses.tipos_documento_soporte` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla config_tipo_comisionado_documentos. Se genera automáticamente. | PK |
| 2 | `config_tipo_comisionado_id` | `uuid` | no | Referencia al registro de travel_expenses.config_tipo_comisionado (id). | FK→travel_expenses.config_tipo_comisionado.id |
| 3 | `tipo_documento_soporte_id` | `uuid` | no | Referencia al registro de travel_expenses.tipos_documento_soporte (id). | FK→travel_expenses.tipos_documento_soporte.id |
| 4 | `tipo_requisito` | `character varying(20)` | no | _Por documentar_ |  |
| 5 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 6 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## configuraciones_globales

_Por documentar._

- Clave primaria: `clave`
- Filas: 6

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `clave` | `character varying(100)` | no | Clave primaria de la tabla configuraciones_globales: clave. | PK |
| 2 | `valor` | `text` | no | _Por documentar_ |  |
| 3 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 4 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 5 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## documentos_soporte

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `solicitud_id` → `travel_expenses.solicitudes_comision` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla documentos_soporte. Se genera automáticamente. | PK |
| 2 | `solicitud_id` | `uuid` | no | Referencia al registro de travel_expenses.solicitudes_comision (id). | FK→travel_expenses.solicitudes_comision.id |
| 3 | `tipo_documento` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `nombre_archivo_original` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `nombre_archivo_seguro` | `character varying(255)` | no | _Por documentar_ |  |
| 6 | `url_repositorio` | `character varying(512)` | no | _Por documentar_ |  |
| 7 | `creado_en` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 8 | `tipo_mime` | `character varying(100)` | sí | _Por documentar_ |  |

## escalas_viaticos

_Por documentar._

- Clave primaria: `id`
- Filas: 11

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla escalas_viaticos. Se genera automáticamente. | PK |
| 2 | `decreto_vigente` | `character varying(50)` | no | _Por documentar_ |  |
| 3 | `ano_vigencia` | `integer` | no | _Por documentar_ |  |
| 4 | `rango_minimo` | `numeric(12,2)` | no | _Por documentar_ |  |
| 5 | `rango_maximo` | `numeric(12,2)` | no | _Por documentar_ |  |
| 6 | `tarifa_diaria` | `numeric(12,2)` | no | _Por documentar_ |  |
| 7 | `creado_en` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 8 | `activo` | `boolean` | no | _Por documentar_ |  |

## excepciones_autorizadas_tiquetes

_Por documentar._

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla excepciones_autorizadas_tiquetes. Se genera automáticamente. | PK |
| 2 | `solicitud_id` | `uuid` | no | _Por documentar_ |  |
| 3 | `tipo_excepcion` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `autorizado_por` | `character varying(150)` | no | _Por documentar_ |  |
| 5 | `numero_documento_soporte` | `character varying(100)` | no | _Por documentar_ |  |
| 6 | `documento_soporte_url` | `character varying(500)` | sí | _Por documentar_ |  |
| 7 | `comentarios` | `text` | sí | _Por documentar_ |  |
| 8 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |

## legalizacion_reversiones

EFDS-1310 — Solicitudes de reversión de una revisión de legalización aprobada. La solicita el analista y la resuelve otra persona; solo antes del registro en SIIF.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `legalizacion_id` → `travel_expenses.legalizaciones_comision` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla legalizacion_reversiones. Se genera automáticamente. | PK |
| 2 | `legalizacion_id` | `uuid` | no | Referencia al registro de travel_expenses.legalizaciones_comision (id). | FK→travel_expenses.legalizaciones_comision.id |
| 3 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 4 | `motivo` | `text` | no | _Por documentar_ |  |
| 5 | `solicitada_por_id` | `uuid` | no | _Por documentar_ |  |
| 6 | `solicitada_en` | `timestamp with time zone` | no | _Por documentar_ |  |
| 7 | `resuelta_por_id` | `uuid` | sí | _Por documentar_ |  |
| 8 | `resuelta_en` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 9 | `observacion_resolucion` | `text` | sí | _Por documentar_ |  |

## legalizacion_revisiones

EFDS-1310 — Trazabilidad de la revisión de la legalización (quién, qué, cuándo). Solo inserción.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `legalizacion_id` → `travel_expenses.legalizaciones_comision` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla legalizacion_revisiones. Se genera automáticamente. | PK |
| 2 | `legalizacion_id` | `uuid` | no | Referencia al registro de travel_expenses.legalizaciones_comision (id). | FK→travel_expenses.legalizaciones_comision.id |
| 3 | `soporte_id` | `uuid` | sí | _Por documentar_ |  |
| 4 | `accion` | `character varying(40)` | no | _Por documentar_ |  |
| 5 | `observacion` | `text` | sí | _Por documentar_ |  |
| 6 | `detalle` | `jsonb` | sí | _Por documentar_ |  |
| 7 | `usuario_id` | `uuid` | no | _Por documentar_ |  |
| 8 | `creado_en` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## legalizacion_soportes

EFDS-1309 — PDF de soporte de la legalización, validados por contenido (%PDF-), no por extensión.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `legalizacion_id` → `travel_expenses.legalizaciones_comision` (0..1 → 1); `tipo_documento_soporte_id` → `travel_expenses.tipos_documento_soporte` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla legalizacion_soportes. Se genera automáticamente. | PK |
| 2 | `legalizacion_id` | `uuid` | no | Referencia al registro de travel_expenses.legalizaciones_comision (id). | FK→travel_expenses.legalizaciones_comision.id |
| 3 | `tipo_documento_soporte_id` | `uuid` | no | Referencia al registro de travel_expenses.tipos_documento_soporte (id). | FK→travel_expenses.tipos_documento_soporte.id |
| 4 | `nombre_archivo_original` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `ruta_relativa` | `character varying(512)` | no | _Por documentar_ |  |
| 6 | `tamano_bytes` | `integer` | no | _Por documentar_ |  |
| 7 | `sha256` | `character(64)` | no | _Por documentar_ |  |
| 8 | `cargado_por_id` | `uuid` | no | _Por documentar_ |  |
| 9 | `creado_en` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 10 | `revision` | `character varying(20)` | sí | _Por documentar_ |  |
| 11 | `observacion_revision` | `text` | sí | _Por documentar_ |  |
| 12 | `revisado_por_id` | `uuid` | sí | _Por documentar_ |  |
| 13 | `revisado_en` | `timestamp with time zone` | sí | _Por documentar_ |  |

## legalizaciones_comision

EFDS-1309 — Legalización de una comisión: plazo en días hábiles y envío a revisión.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `solicitud_id` → `travel_expenses.solicitudes_comision` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla legalizaciones_comision. Se genera automáticamente. | PK |
| 2 | `solicitud_id` | `uuid` | no | Referencia al registro de travel_expenses.solicitudes_comision (id). | única FK→travel_expenses.solicitudes_comision.id |
| 3 | `modalidad_pago` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `estado_disparador` | `character varying(50)` | no | _Por documentar_ |  |
| 5 | `fecha_disparo` | `timestamp with time zone` | no | _Por documentar_ |  |
| 6 | `fecha_base_plazo` | `timestamp with time zone` | no | Desde cuándo corre el plazo: el fin del día más tardío entre el regreso planeado (fecha_fin) y el pago (fecha_pago), en hora de Colombia. Migración 453. |  |
| 7 | `plazo_dias_habiles` | `integer` | no | _Por documentar_ |  |
| 8 | `hora_corte` | `character varying(5)` | no | _Por documentar_ |  |
| 9 | `fecha_limite` | `timestamp with time zone` | no | _Por documentar_ |  |
| 10 | `calendario_incompleto` | `boolean` | no | TRUE si el plazo cruzó un año sin festivos cargados en auth.festivos_colombia: la fecha límite puede adelantarse. |  |
| 11 | `fecha_envio` | `timestamp with time zone` | sí | Momento en que el comisionado envió la legalización completa a revisión. NULL = aún en cargue. |  |
| 12 | `enviada_por_id` | `uuid` | sí | _Por documentar_ |  |
| 13 | `notificado_por_vencer_en` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 14 | `notificado_vencido_en` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 15 | `creado_en` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 16 | `actualizado_en` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 17 | `revision_aprobada_en` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 18 | `revision_aprobada_por_id` | `uuid` | sí | _Por documentar_ |  |
| 19 | `devuelta_en` | `timestamp with time zone` | sí | EFDS-1310 — Última devolución al comisionado. La solicitud sigue en PENDIENTE_LEGALIZACION (C-2). |  |
| 20 | `devuelta_por_id` | `uuid` | sí | _Por documentar_ |  |
| 21 | `observacion_devolucion` | `text` | sí | _Por documentar_ |  |
| 22 | `numero_devoluciones` | `integer` | no | _Por documentar_ |  |
| 23 | `siif_exportado_en` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 24 | `siif_exportado_por_id` | `uuid` | sí | _Por documentar_ |  |
| 25 | `numero_registro_siif` | `character varying(100)` | sí | _Por documentar_ |  |
| 26 | `fecha_registro_siif` | `date` | sí | _Por documentar_ |  |
| 27 | `registrado_siif_por_id` | `uuid` | sí | _Por documentar_ |  |
| 28 | `valor_pagado` | `numeric(14,2)` | sí | _Por documentar_ |  |
| 29 | `valor_legalizado` | `numeric(14,2)` | sí | _Por documentar_ |  |
| 30 | `valor_reintegro` | `numeric(14,2)` | sí | EFDS-1310 — valor_pagado - valor_legalizado cuando el viaje fue menor; > 0 dispara el evento de reintegro (EFDS-1308). |  |
| 31 | `dias_reales` | `numeric(6,2)` | sí | _Por documentar_ |  |
| 32 | `observaciones_cierre` | `text` | sí | _Por documentar_ |  |
| 33 | `cerrada_en` | `timestamp with time zone` | sí | EFDS-1310 — Expediente de legalización cerrado: la fila y sus soportes quedan inmutables (triggers). |  |
| 34 | `cerrada_por_id` | `uuid` | sí | _Por documentar_ |  |
| 35 | `fecha_inicio_real` | `date` | sí | Fecha en que el comisionado realmente inició la comisión, según el GF-FO-032 V2. |  |
| 36 | `fecha_fin_real` | `date` | sí | Fecha en que el comisionado realmente terminó la comisión, según el GF-FO-032 V2. No cambia el plazo, que sale de la fecha planeada. |  |
| 37 | `comision_externa` | `boolean` | sí | TRUE si la comisión se cumplió fuera de la ESAP: exige el certificado de la entidad externa. NULL = no declarado. |  |
| 38 | `entidad_externa` | `character varying(200)` | sí | _Por documentar_ |  |
| 39 | `cumplimiento_registrado_en` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 40 | `cumplimiento_registrado_por_id` | `uuid` | sí | _Por documentar_ |  |
| 41 | `reintegro_viaje_corto` | `numeric(14,2)` | sí | Al cerrar: parte del reintegro por los días no viajados, con las tarifas de la liquidación pagada. |  |

## liquidation_params

_Por documentar._

- Clave primaria: `id`
- Filas: 5

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla liquidation_params. Se genera automáticamente. | PK |
| 2 | `clave` | `character varying(50)` | no | _Por documentar_ | única |
| 3 | `valor` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `tipo` | `character varying(20)` | no | _Por documentar_ |  |
| 5 | `descripcion` | `character varying(255)` | sí | _Por documentar_ |  |
| 6 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 7 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## parametros_globales

Parametros globales configurables del modulo de viaticos y comisiones

- Clave primaria: `clave`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `clave` | `character varying(100)` | no | Clave primaria de la tabla parametros_globales: clave. | PK |
| 2 | `valor` | `character varying(255)` | no | _Por documentar_ |  |
| 3 | `tipo` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `editable` | `boolean` | sí | _Por documentar_ |  |
| 6 | `creado_en` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 7 | `actualizado_en` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## paz_y_salvo_eventos

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `paz_y_salvo_id` → `travel_expenses.paz_y_salvos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | Identificador único del registro en la tabla paz_y_salvo_eventos. Se genera automáticamente. | PK |
| 2 | `paz_y_salvo_id` | `uuid` | no | Referencia al registro de travel_expenses.paz_y_salvos (id). | FK→travel_expenses.paz_y_salvos.id |
| 3 | `usuario_id` | `uuid` | no | _Por documentar_ |  |
| 4 | `accion` | `character varying(30)` | no | _Por documentar_ |  |
| 5 | `creado_en` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 6 | `detalle` | `jsonb` | no | _Por documentar_ |  |

## paz_y_salvos

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `comisionado_id` → `travel_expenses.comisionados` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla paz_y_salvos. | PK |
| 2 | `comisionado_id` | `uuid` | no | Referencia al registro de travel_expenses.comisionados (id). | FK→travel_expenses.comisionados.id |
| 3 | `solicitado_por_id` | `uuid` | no | _Por documentar_ |  |
| 4 | `contenido` | `jsonb` | no | _Por documentar_ |  |
| 5 | `contenido_sha256` | `character varying(64)` | no | _Por documentar_ |  |
| 6 | `creado_en` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 7 | `firma` | `jsonb` | sí | _Por documentar_ |  |
| 8 | `firmado_en` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 9 | `archivo_sha256` | `character varying(64)` | sí | _Por documentar_ |  |

## reintegros_comision

Reintegros de comisiones pagadas por avance no realizadas o ejecutadas por menos días (RF-PAG-004).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `solicitud_id` → `travel_expenses.solicitudes_comision` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla reintegros_comision. Se genera automáticamente. | PK |
| 2 | `solicitud_id` | `uuid` | no | Referencia al registro de travel_expenses.solicitudes_comision (id). | FK→travel_expenses.solicitudes_comision.id |
| 3 | `origen` | `character varying(30)` | no | COMISION_NO_REALIZADA: la comisión pagada se canceló sin viajar. VIAJE_MENOR: se ejecutaron menos días de los pagados. |  |
| 4 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 5 | `valor_pagado` | `numeric(14,2)` | no | _Por documentar_ |  |
| 6 | `valor_a_reintegrar` | `numeric(14,2)` | no | Valor calculado según los días efectivamente ejecutados. |  |
| 7 | `dias_comision` | `numeric(6,2)` | sí | _Por documentar_ |  |
| 8 | `dias_ejecutados` | `numeric(6,2)` | sí | _Por documentar_ |  |
| 9 | `valor_reintegrado` | `numeric(14,2)` | sí | _Por documentar_ |  |
| 10 | `fecha_reintegro` | `date` | sí | _Por documentar_ |  |
| 11 | `soporte_path` | `character varying(255)` | sí | Ruta del soporte de la consignación del reintegro. |  |
| 12 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 13 | `registrado_por_id` | `uuid` | sí | _Por documentar_ |  |
| 14 | `fecha_registro` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 15 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 16 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## rutas_restringidas

_Por documentar._

- Clave primaria: `id`
- Filas: 4

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla rutas_restringidas. Se genera automáticamente. | PK |
| 2 | `origen_ciudad` | `character varying(100)` | no | _Por documentar_ |  |
| 3 | `destino_ciudad` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `descripcion_restriccion` | `character varying(255)` | sí | _Por documentar_ |  |
| 5 | `activo` | `boolean` | no | _Por documentar_ |  |
| 6 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |

## saldos_tiquetes

_Por documentar._

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla saldos_tiquetes. Se genera automáticamente. | PK |
| 2 | `dependencia_id` | `character varying(100)` | no | _Por documentar_ | única |
| 3 | `nombre_dependencia` | `character varying(150)` | no | _Por documentar_ |  |
| 4 | `presupuesto_inicial` | `numeric(12,2)` | no | _Por documentar_ |  |
| 5 | `presupuesto_reservado` | `numeric(12,2)` | no | _Por documentar_ |  |
| 6 | `presupuesto_disponible` | `numeric(12,2)` | no | _Por documentar_ |  |
| 7 | `holgura_porcentaje` | `numeric(5,2)` | no | _Por documentar_ |  |
| 8 | `activo` | `boolean` | no | _Por documentar_ |  |
| 9 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 10 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## solicitudes_comision

_Por documentar._

- Clave primaria: `id`
- Filas: 3
- Referencia a: `autorizador_id` → `auth.user` (0..1 → 0..1); `cancelado_por_usuario_id` → `auth.user` (0..1 → 0..1); `revisor_control_id` → `auth.user` (0..1 → 0..1); `enviado_presupuesto_por_id` → `auth.user` (0..1 → 0..1); `expedido_rp_por_id` → `auth.user` (0..1 → 0..1); `obligado_por_id` → `auth.user` (0..1 → 0..1); `pagado_por_id` → `auth.user` (0..1 → 0..1); `comisionado_id` → `travel_expenses.comisionados` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla solicitudes_comision. Se genera automáticamente. | PK |
| 2 | `consecutivo_unico` | `character varying(50)` | no | _Por documentar_ | única |
| 3 | `comisionado_id` | `uuid` | no | Referencia al registro de travel_expenses.comisionados (id). | FK→travel_expenses.comisionados.id |
| 4 | `destino_ciudad` | `text` | no | _Por documentar_ |  |
| 5 | `destino_departamento` | `text` | no | _Por documentar_ |  |
| 6 | `fecha_inicio` | `timestamp without time zone` | no | _Por documentar_ |  |
| 7 | `fecha_fin` | `timestamp without time zone` | no | _Por documentar_ |  |
| 8 | `objeto_comision` | `text` | no | _Por documentar_ |  |
| 9 | `prioridad` | `character varying(10)` | no | _Por documentar_ |  |
| 10 | `rubro_presupuestal` | `text` | no | _Por documentar_ |  |
| 11 | `requiere_tiquetes` | `boolean` | no | _Por documentar_ |  |
| 12 | `estado_solicitud` | `character varying(50)` | no | _Por documentar_ |  |
| 13 | `radicado_fuera_jornada` | `boolean` | no | _Por documentar_ |  |
| 14 | `creado_por_usuario_id` | `uuid` | no | _Por documentar_ |  |
| 15 | `creado_en` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 16 | `actualizado_en` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 17 | `monto_viaticos` | `numeric(12,2)` | no | _Por documentar_ |  |
| 18 | `monto_gastos_viaje` | `numeric(12,2)` | no | _Por documentar_ |  |
| 19 | `dias_comision` | `numeric(5,2)` | no | Número de días de la comisión con soporte decimal (ej: 0.5, 1.5, 2.0). |  |
| 20 | `extemporanea` | `boolean` | no | _Por documentar_ |  |
| 21 | `tipo_comision` | `character varying(50)` | sí | _Por documentar_ |  |
| 22 | `es_internacional` | `boolean` | no | _Por documentar_ |  |
| 23 | `motivo_devolucion` | `text` | sí | Motivo de la devolución del expediente por parte del secretario o analista (RF-REC-001). |  |
| 24 | `fecha_revision` | `timestamp without time zone` | sí | Marca temporal de la primera revisión del expediente por parte del secretario/a (RF-REC-001). |  |
| 25 | `salario_basico` | `numeric(12,2)` | no | Salario básico mensual del comisionado (mayor salario en caso de doble rol). Se usa para cálculos de liquidación y consulta en detalle. |  |
| 26 | `costo_estimado_tiquete` | `numeric(12,2)` | no | Costo estimado del tiquete aéreo ingresado por el usuario en la solicitud. |  |
| 27 | `analista_asignado_id` | `uuid` | sí | ID del usuario analista asignado para resolver la comision (auth.user.id_user) |  |
| 28 | `siif_exportado` | `boolean` | no | Indica si la solicitud ya fue exportada a SIIF Nacion. |  |
| 29 | `fecha_exportacion_siif` | `timestamp without time zone` | sí | Marca temporal en que se exporto la solicitud a SIIF. |  |
| 30 | `usuario_exportador_id` | `uuid` | sí | ID del usuario que exporto la solicitud a SIIF. |  |
| 31 | `consulta_rut_facturador` | `boolean` | no | Indica si el analista consulto el RUT del comisionado durante la verificacion. |  |
| 32 | `id_dependencia` | `bigint` | sí | _Por documentar_ |  |
| 33 | `revisor_control_id` | `uuid` | sí | ID del usuario de Control Viaticos que ejecuta la segunda revision. | FK→auth.user.id_user |
| 34 | `fecha_segunda_revision` | `timestamp without time zone` | sí | Marca temporal de la aprobacion o devolucion en la segunda revision. |  |
| 35 | `observaciones_segunda_revision` | `text` | sí | Hallazgos u observaciones registrados cuando la solicitud se devuelve al analista. |  |
| 36 | `autorizador_id` | `uuid` | sí | ID del usuario de la Subdirección de Gestión Corporativa que autoriza la comisión. | FK→auth.user.id_user |
| 37 | `fecha_autorizacion` | `timestamp without time zone` | sí | Marca temporal en la que la Subdirección emite la autorización o devolución. |  |
| 38 | `observaciones_autorizacion` | `text` | sí | Observaciones, justificación o reparos de la Subdirección de Gestión Corporativa. |  |
| 39 | `autorizador_direccion_id` | `uuid` | sí | ID del usuario de Dirección Nacional o delegado que autorizó/negó la extemporaneidad (auth.user.id_user). |  |
| 40 | `fecha_autorizacion_direccion` | `timestamp with time zone` | sí | Marca temporal en que la Dirección Nacional emitió la decisión (Etapa 6 - RF-AUT-002). |  |
| 41 | `decision_direccion` | `character varying(20)` | sí | Resultado de la decisión de Dirección Nacional: AUTORIZADA o RECHAZADA. |  |
| 42 | `justificacion_direccion` | `text` | sí | Justificación motivada de la decisión emitida por Dirección Nacional. |  |
| 43 | `es_delegado_direccion` | `boolean` | sí | Indica si la autorización/negación fue emitida por un delegado formal de la Dirección Nacional. |  |
| 44 | `motivo_cancelacion` | `text` | sí | Motivo obligatorio detallado de la cancelación de la comisión (RF-AUT-003). |  |
| 45 | `fecha_cancelacion` | `timestamp with time zone` | sí | Marca temporal (UTC) en la que se confirmó la cancelación de la comisión. |  |
| 46 | `cancelado_por_usuario_id` | `uuid` | sí | ID del usuario del sistema que ejecutó y confirmó la cancelación (auth.user.id_user). | FK→auth.user.id_user |
| 47 | `responsable_cancelacion` | `character varying(255)` | sí | Nombre, cargo o dependencia solicitante/responsable de la orden de cancelación. |  |
| 48 | `pendiente_reintegro` | `boolean` | no | Indica si la comisión contaba con recursos comprometidos (SIIF/RP/Tiquetes) y requiere reintegro/liberación en Etapa 8. |  |
| 49 | `enviado_presupuesto` | `boolean` | no | _Por documentar_ |  |
| 50 | `fecha_envio_presupuesto` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 51 | `enviado_presupuesto_por_id` | `uuid` | sí | Referencia al registro de auth.user (id_user). | FK→auth.user.id_user |
| 52 | `observaciones_envio_presupuesto` | `text` | sí | _Por documentar_ |  |
| 53 | `numero_rp` | `character varying(50)` | sí | _Por documentar_ |  |
| 54 | `fecha_rp` | `date` | sí | _Por documentar_ |  |
| 55 | `valor_comprometido` | `numeric(14,2)` | sí | _Por documentar_ |  |
| 56 | `rubro_rp` | `character varying(100)` | sí | _Por documentar_ |  |
| 57 | `soporte_rp_path` | `character varying(255)` | sí | _Por documentar_ |  |
| 58 | `fecha_expedicion_rp` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 59 | `expedido_rp_por_id` | `uuid` | sí | Referencia al registro de auth.user (id_user). | FK→auth.user.id_user |
| 60 | `codigo_rp` | `character varying(150)` | sí | Código oficial del RP con nomenclatura Fecha_RP_Número expedido en SIIF Nación. |  |
| 61 | `observaciones_rp` | `text` | sí | _Por documentar_ |  |
| 62 | `modalidad_pago` | `character varying(50)` | no | _Por documentar_ |  |
| 63 | `dias_habiles_previos` | `integer` | no | _Por documentar_ |  |
| 64 | `fecha_calculo_modalidad` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 65 | `numero_obligacion` | `character varying(100)` | sí | _Por documentar_ |  |
| 66 | `fecha_obligacion` | `date` | sí | _Por documentar_ |  |
| 67 | `valor_obligacion` | `numeric(12,2)` | sí | _Por documentar_ |  |
| 68 | `observaciones_obligacion` | `text` | sí | _Por documentar_ |  |
| 69 | `soporte_obligacion_path` | `character varying(255)` | sí | _Por documentar_ |  |
| 70 | `obligado_por_id` | `uuid` | sí | Referencia al registro de auth.user (id_user). | FK→auth.user.id_user |
| 71 | `fecha_registro_obligacion` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 72 | `notificado_sst` | `boolean` | no | _Por documentar_ |  |
| 73 | `fecha_pago` | `date` | sí | _Por documentar_ |  |
| 74 | `valor_pagado` | `numeric(12,2)` | sí | _Por documentar_ |  |
| 75 | `soporte_pago_path` | `character varying(255)` | sí | _Por documentar_ |  |
| 76 | `numero_orden_pago` | `character varying(100)` | sí | _Por documentar_ |  |
| 77 | `observaciones_pago` | `text` | sí | _Por documentar_ |  |
| 78 | `pagado_por_id` | `uuid` | sí | Referencia al registro de auth.user (id_user). | FK→auth.user.id_user |
| 79 | `fecha_registro_pago` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 80 | `campos_adicionales` | `jsonb` | no | Metadatos y campos dinámicos configurables gobernados por travel_expenses.config_campos_formulario (JSONB). |  |
| 81 | `itinerario` | `jsonb` | no | Arreglo de tramos/rutas de la comisión (RutaItinerario[]) con origen, destino, trayecto, fechas, días y horario militar estimado. |  |
| 82 | `dias_pernoctados` | `numeric(5,2)` | sí | _Por documentar_ |  |
| 83 | `tarifa_dia_pernoctado` | `numeric(14,2)` | sí | _Por documentar_ |  |
| 84 | `total_pernoctados` | `numeric(14,2)` | sí | _Por documentar_ |  |
| 85 | `dias_no_pernoctados` | `numeric(5,2)` | sí | _Por documentar_ |  |
| 86 | `tarifa_dia_no_pernoctado` | `numeric(14,2)` | sí | _Por documentar_ |  |
| 87 | `total_no_pernoctados` | `numeric(14,2)` | sí | _Por documentar_ |  |
| 88 | `factor_comisionado` | `numeric(4,2)` | sí | _Por documentar_ |  |
| 89 | `factor_pernocta` | `numeric(4,2)` | sí | _Por documentar_ |  |
| 90 | `tarifa_diaria_base` | `numeric(14,2)` | sí | _Por documentar_ |  |
| 91 | `tarifa_final_aplicada_dia` | `numeric(14,2)` | sí | _Por documentar_ |  |
| 92 | `salario_base_aplicado` | `numeric(14,2)` | sí | _Por documentar_ |  |
| 93 | `decreto_aplicado` | `character varying(100)` | sí | _Por documentar_ |  |
| 94 | `numero_cdp` | `text` | sí | _Por documentar_ |  |
| 95 | `fecha_cdp` | `text` | sí | _Por documentar_ |  |
| 96 | `fecha_radicacion` | `timestamp without time zone` | sí | Marca temporal en la que la solicitud se radicó e ingresó por primera vez a la bandeja del Grupo de Viáticos. |  |
| 97 | `cargo` | `text` | sí | Cargo institucional asignado a la comisión GF-FO-023 para trazabilidad, liquidación y KPIs de analítica. |  |
| 98 | `id_cargo` | `bigint` | sí | Identificador referencial del cargo institucional (auth.cargos). |  |

## solicitudes_historial_estados

Auditoría append-only de transiciones de estado del expediente de comisión (RF-SIS-001 / RF-LIQ-004).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `solicitud_id` → `travel_expenses.solicitudes_comision` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla solicitudes_historial_estados. Se genera automáticamente. | PK |
| 2 | `solicitud_id` | `uuid` | no | Referencia al registro de travel_expenses.solicitudes_comision (id). | FK→travel_expenses.solicitudes_comision.id |
| 3 | `estado_anterior` | `character varying(50)` | sí | _Por documentar_ |  |
| 4 | `estado_nuevo` | `character varying(50)` | no | Estado posterior a la transición. Ej: SOLICITADO (la solicitud queda consolidada y en revisión del Grupo de Viáticos). |  |
| 5 | `usuario_id` | `uuid` | no | _Por documentar_ |  |
| 6 | `comentarios` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |

## tarifas_investigadores

_Por documentar._

- Clave primaria: `id`
- Filas: 3

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla tarifas_investigadores. Se genera automáticamente. | PK |
| 2 | `categoria_investigador` | `character varying(50)` | no | _Por documentar_ | única |
| 3 | `tarifa_diaria` | `numeric(12,2)` | no | _Por documentar_ |  |
| 4 | `creado_en` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 5 | `activo` | `boolean` | no | _Por documentar_ |  |

## tarifas_referencia_tiquetes

_Por documentar._

- Clave primaria: `id`
- Filas: 42

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla tarifas_referencia_tiquetes. Se genera automáticamente. | PK |
| 2 | `origen_ciudad` | `character varying(100)` | no | _Por documentar_ |  |
| 3 | `destino_ciudad` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `origen_iata` | `character varying(10)` | no | _Por documentar_ |  |
| 5 | `destino_iata` | `character varying(10)` | no | _Por documentar_ |  |
| 6 | `tarifa_estimada` | `numeric(14,2)` | no | _Por documentar_ |  |
| 7 | `tarifa_minima` | `numeric(14,2)` | sí | _Por documentar_ |  |
| 8 | `tarifa_maxima` | `numeric(14,2)` | sí | _Por documentar_ |  |
| 9 | `fuente` | `character varying(50)` | no | _Por documentar_ |  |
| 10 | `notas` | `character varying(255)` | sí | _Por documentar_ |  |
| 11 | `ultima_actualizacion` | `timestamp without time zone` | no | _Por documentar_ |  |
| 12 | `activo` | `boolean` | no | _Por documentar_ |  |
| 13 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 14 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## tarifas_regionales_excepcion

_Por documentar._

- Clave primaria: `id`
- Filas: 8

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla tarifas_regionales_excepcion. Se genera automáticamente. | PK |
| 2 | `departamento` | `character varying(100)` | no | _Por documentar_ | única |
| 3 | `es_nuevo_departamento` | `boolean` | no | _Por documentar_ |  |
| 4 | `tarifa_diaria` | `numeric(12,2)` | no | _Por documentar_ |  |
| 5 | `decreto_referencia` | `character varying(100)` | sí | _Por documentar_ |  |
| 6 | `activo` | `boolean` | no | _Por documentar_ |  |
| 7 | `creado_en` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |

## tarifas_transporte_terminal

_Por documentar._

- Clave primaria: `id`
- Filas: 11

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla tarifas_transporte_terminal. Se genera automáticamente. | PK |
| 2 | `departamento` | `character varying(100)` | no | _Por documentar_ |  |
| 3 | `departamento_id` | `integer` | sí | _Por documentar_ |  |
| 4 | `ciudad` | `character varying(100)` | sí | _Por documentar_ |  |
| 5 | `ciudad_aeropuerto` | `character varying(150)` | no | _Por documentar_ |  |
| 6 | `valor_maximo` | `numeric(12,2)` | no | _Por documentar_ |  |
| 7 | `activo` | `boolean` | no | _Por documentar_ |  |
| 8 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## tipos_documento_soporte

_Por documentar._

- Clave primaria: `id`
- Filas: 15

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla tipos_documento_soporte. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(50)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `character varying(255)` | sí | _Por documentar_ |  |
| 5 | `activo` | `boolean` | no | _Por documentar_ |  |
| 6 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 7 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 8 | `instrucciones_validacion` | `text` | sí | _Por documentar_ |  |
| 9 | `campos_a_validar` | `jsonb` | sí | _Por documentar_ |  |
