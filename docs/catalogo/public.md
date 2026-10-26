# Configuración del control disciplinario (`public`)

Configuración del módulo de control disciplinario interno: días hábiles por etapa, entes de control y parámetros globales.

3 tablas · 0 vistas · 21 columnas · 12 filas · 3 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`config_entes_control`](#config_entes_control) | Tabla | 4 | Catálogo de configuración de los entes de control (por ejemplo, Contraloría y Procuraduría). Un registro por ente, con su código, nombre, descripción, color de identificación en la interfaz, orden e indicador de activo. |
| [`stage_configuration`](#stage_configuration) | Tabla | 7 | Configuración de días hábiles por etapa del proceso disciplinario. Un registro por etapa, con su descripción, el número de días hábiles asignados e indicador de activa. |
| [`system_configuration`](#system_configuration) | Tabla | 1 | Configuración global del módulo de control disciplinario interno. Registra, en formato JSON, la capacidad de procesos por cargo y los parámetros de notificaciones, alertas y seguridad. |

## config_entes_control

Catálogo de configuración de los entes de control (por ejemplo, Contraloría y Procuraduría). Un registro por ente, con su código, nombre, descripción, color de identificación en la interfaz, orden e indicador de activo.

- Clave primaria: `id`
- Filas: 4

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla config_entes_control. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(50)` | no | Código único del ente de control (por ejemplo, CONTRALORIA, PROCURADURIA). | única |
| 3 | `nombre` | `character varying(255)` | no | Nombre del ente de control. |  |
| 4 | `descripcion` | `text` | sí | Descripción del ente de control. |  |
| 5 | `color` | `character varying(20)` | sí | Color con que se identifica el ente de control en la interfaz, en código hexadecimal. Por defecto, #3B82F6. |  |
| 6 | `orden` | `integer` | sí | Posición del ente de control en el listado. |  |
| 7 | `activo` | `boolean` | sí | Indica si el ente de control está activo. |  |
| 8 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 9 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## stage_configuration

Configuración de días hábiles por etapa del proceso disciplinario. Un registro por etapa, con su descripción, el número de días hábiles asignados e indicador de activa.

- Clave primaria: `id`
- Filas: 7

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla stage_configuration. Se genera automáticamente. | PK |
| 2 | `etapa` | `character varying` | no | Nombre de la etapa del proceso disciplinario configurada, con sus días hábiles. La tabla se creó con la configuración del módulo de control disciplinario interno. |  |
| 3 | `diasHabiles` | `integer` | no | Número de días hábiles asignados a la etapa. Por defecto, 30. |  |
| 4 | `descripcion` | `text` | sí | Descripción de la etapa. |  |
| 5 | `activo` | `boolean` | no | Indica si la configuración de la etapa está activa. |  |
| 6 | `createdAt` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 7 | `updatedAt` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## system_configuration

Configuración global del módulo de control disciplinario interno. Registra, en formato JSON, la capacidad de procesos por cargo y los parámetros de notificaciones, alertas y seguridad.

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla system_configuration. Se genera automáticamente. | PK |
| 2 | `roleCapacities` | `jsonb` | no | Capacidad de procesos por cargo del módulo de control disciplinario interno, en formato JSON: cada clave es un cargo y su valor la capacidad. |  |
| 3 | `notificationSettings` | `jsonb` | no | Configuración de notificaciones del módulo de control disciplinario interno, en formato JSON: interruptores booleanos como vencimiento7dias, procesoVencido, cambioEtapa, resumenDiario o emailMasterSwitch. |  |
| 4 | `alertSettings` | `jsonb` | no | Configuración de alertas del módulo de control disciplinario interno, en formato JSON: umbrales numéricos como porcentajeRiesgo, porcentajeCritico, capacidadAlerta y diasAnticipacion. |  |
| 5 | `securitySettings` | `jsonb` | no | Configuración de seguridad y auditoría del módulo de control disciplinario interno, en formato JSON: banderas auditEnabled, digitalSignature y backupEnabled. |  |
