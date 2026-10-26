# Auditoría y trazabilidad (`audit`)

Schema para almacenar logs de auditoría de todas las peticiones HTTP del sistema

1 tablas · 1 vistas · 34 columnas · 74.668 filas · 3 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`request_logs`](#request_logs) | Tabla particionada | 74668 | Registro de todas las peticiones HTTP del sistema para auditoría. Tabla particionada por mes. |
| [`request_logs_2026_06`](#request_logs_2026_06) | Partición |  | _Por documentar_ |
| [`request_logs_2026_07`](#request_logs_2026_07) | Partición |  | _Por documentar_ |
| [`request_logs_2026_08`](#request_logs_2026_08) | Partición |  | _Por documentar_ |
| [`request_logs_2026_09`](#request_logs_2026_09) | Partición |  | _Por documentar_ |
| [`request_logs_2026_10`](#request_logs_2026_10) | Partición |  | _Por documentar_ |
| [`request_logs_current`](#request_logs_current) | Partición |  | _Por documentar_ |
| [`request_logs_next_month`](#request_logs_next_month) | Partición |  | _Por documentar_ |
| [`request_logs_prev_month`](#request_logs_prev_month) | Partición |  | _Por documentar_ |
| [`request_logs_stats`](#request_logs_stats) | Vista |  | _Por documentar_ |

## request_logs

Registro de todas las peticiones HTTP del sistema para auditoría. Tabla particionada por mes.

- Clave primaria: `id`, `timestamp`
- Filas: 74668

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla request_logs. Se genera automáticamente. | PK |
| 2 | `method` | `character varying(10)` | no | Método HTTP de la petición registrada, por ejemplo GET, POST, PUT, DELETE o PATCH. |  |
| 3 | `url` | `text` | no | Dirección web (URL) de la petición HTTP. |  |
| 4 | `path` | `text` | no | Ruta de la URL solicitada, sin el dominio ni los parámetros de consulta. |  |
| 5 | `query_params` | `jsonb` | sí | Parámetros de consulta de la petición, en formato JSON. |  |
| 6 | `module` | `character varying(100)` | sí | Módulo del sistema: auth, certificados, control-interno, legal, etc. |  |
| 7 | `submodule` | `character varying(100)` | sí | Submódulo o recurso específico dentro del módulo: expedientes, juzgamiento, users, roles, etc. |  |
| 8 | `version` | `character varying(10)` | sí | Versión indicada en la petición HTTP. |  |
| 9 | `ip_address` | `character varying(45)` | sí | Dirección IP (IPv4 o IPv6) desde la que se hizo la petición. | Identificador en línea (IP) |
| 10 | `user_agent` | `text` | sí | Agente de usuario (navegador) que realizó la petición. |  |
| 11 | `origin` | `text` | sí | Valor del encabezado HTTP Origin de la petición. |  |
| 12 | `referer` | `text` | sí | Valor del encabezado HTTP Referer de la petición. |  |
| 13 | `user_id` | `bigint` | sí | Identificador del usuario autenticado que hizo la petición (auth."user".id_user), tomado del token. Es nulo si la petición no trae usuario. |  |
| 14 | `user_email` | `character varying(255)` | sí | Correo electrónico del usuario autenticado que hizo la petición. | Contacto |
| 15 | `user_role` | `character varying(100)` | sí | Rol del usuario autenticado al momento de la petición. |  |
| 16 | `status_code` | `integer` | no | Código de estado HTTP de la respuesta. |  |
| 17 | `response_time_ms` | `integer` | no | Tiempo de respuesta de la petición, en milisegundos. |  |
| 18 | `response_size_bytes` | `integer` | sí | Tamaño de la respuesta, en bytes. Por defecto, 0. |  |
| 19 | `request_body` | `jsonb` | sí | Cuerpo de la petición, en formato JSON. |  |
| 20 | `request_body_size` | `integer` | sí | Tamaño del cuerpo de la petición, en bytes. Por defecto, 0. |  |
| 21 | `has_large_body` | `boolean` | sí | Indica si el cuerpo de la petición supera el tamaño definido para almacenarse completo. |  |
| 22 | `response_body` | `jsonb` | sí | Cuerpo de la respuesta, en formato JSON. |  |
| 23 | `response_body_size` | `integer` | sí | Tamaño del cuerpo de la respuesta, en bytes. Por defecto, 0. |  |
| 24 | `has_large_response` | `boolean` | sí | Indica si el cuerpo de la respuesta supera el tamaño definido para almacenarse completo. |  |
| 25 | `error_message` | `text` | sí | Mensaje de error devuelto cuando la petición falla. |  |
| 26 | `error_stack` | `text` | sí | Traza de la pila del error cuando la petición falla. |  |
| 27 | `timestamp` | `timestamp without time zone` | no | Clave primaria de la tabla request_logs: timestamp. | PK |
| 28 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 29 | `action` | `character varying(100)` | sí | Acción legible realizada en la petición (ej: "crear auditoria", "iniciar sesión", "actualizar hallazgo") |  |
| 30 | `entity_name` | `character varying(100)` | sí | Nombre de la entidad/tabla que fue modificada |  |
| 31 | `entity_id` | `character varying(100)` | sí | ID del registro que fue modificado |  |
| 32 | `previous_data` | `jsonb` | sí | Datos ANTES de la modificación (payload viejo/original) |  |
| 33 | `new_data` | `jsonb` | sí | Datos DESPUÉS de la modificación (payload nuevo/actual) |  |
| 34 | `changes` | `jsonb` | sí | Array JSON con el detalle de cambios: [{field, oldValue, newValue}] |  |

## request_logs_2026_06

_Por documentar._

- Clave primaria: `id`, `timestamp`
- Filas: —

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `method` | `character varying(10)` | no | _Por documentar_ |  |
| 3 | `url` | `text` | no | _Por documentar_ |  |
| 4 | `path` | `text` | no | _Por documentar_ |  |
| 5 | `query_params` | `jsonb` | sí | _Por documentar_ |  |
| 6 | `module` | `character varying(100)` | sí | _Por documentar_ |  |
| 7 | `submodule` | `character varying(100)` | sí | _Por documentar_ |  |
| 8 | `version` | `character varying(10)` | sí | _Por documentar_ |  |
| 9 | `ip_address` | `character varying(45)` | sí | _Por documentar_ | Identificador en línea (IP) |
| 10 | `user_agent` | `text` | sí | _Por documentar_ |  |
| 11 | `origin` | `text` | sí | _Por documentar_ |  |
| 12 | `referer` | `text` | sí | _Por documentar_ |  |
| 13 | `user_id` | `bigint` | sí | _Por documentar_ |  |
| 14 | `user_email` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 15 | `user_role` | `character varying(100)` | sí | _Por documentar_ |  |
| 16 | `status_code` | `integer` | no | _Por documentar_ |  |
| 17 | `response_time_ms` | `integer` | no | _Por documentar_ |  |
| 18 | `response_size_bytes` | `integer` | sí | _Por documentar_ |  |
| 19 | `request_body` | `jsonb` | sí | _Por documentar_ |  |
| 20 | `request_body_size` | `integer` | sí | _Por documentar_ |  |
| 21 | `has_large_body` | `boolean` | sí | _Por documentar_ |  |
| 22 | `response_body` | `jsonb` | sí | _Por documentar_ |  |
| 23 | `response_body_size` | `integer` | sí | _Por documentar_ |  |
| 24 | `has_large_response` | `boolean` | sí | _Por documentar_ |  |
| 25 | `error_message` | `text` | sí | _Por documentar_ |  |
| 26 | `error_stack` | `text` | sí | _Por documentar_ |  |
| 27 | `timestamp` | `timestamp without time zone` | no | _Por documentar_ | PK |
| 28 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 29 | `action` | `character varying(100)` | sí | _Por documentar_ |  |
| 30 | `entity_name` | `character varying(100)` | sí | _Por documentar_ |  |
| 31 | `entity_id` | `character varying(100)` | sí | _Por documentar_ |  |
| 32 | `previous_data` | `jsonb` | sí | _Por documentar_ |  |
| 33 | `new_data` | `jsonb` | sí | _Por documentar_ |  |
| 34 | `changes` | `jsonb` | sí | _Por documentar_ |  |

## request_logs_2026_07

_Por documentar._

- Clave primaria: `id`, `timestamp`
- Filas: —

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `method` | `character varying(10)` | no | _Por documentar_ |  |
| 3 | `url` | `text` | no | _Por documentar_ |  |
| 4 | `path` | `text` | no | _Por documentar_ |  |
| 5 | `query_params` | `jsonb` | sí | _Por documentar_ |  |
| 6 | `module` | `character varying(100)` | sí | _Por documentar_ |  |
| 7 | `submodule` | `character varying(100)` | sí | _Por documentar_ |  |
| 8 | `version` | `character varying(10)` | sí | _Por documentar_ |  |
| 9 | `ip_address` | `character varying(45)` | sí | _Por documentar_ | Identificador en línea (IP) |
| 10 | `user_agent` | `text` | sí | _Por documentar_ |  |
| 11 | `origin` | `text` | sí | _Por documentar_ |  |
| 12 | `referer` | `text` | sí | _Por documentar_ |  |
| 13 | `user_id` | `bigint` | sí | _Por documentar_ |  |
| 14 | `user_email` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 15 | `user_role` | `character varying(100)` | sí | _Por documentar_ |  |
| 16 | `status_code` | `integer` | no | _Por documentar_ |  |
| 17 | `response_time_ms` | `integer` | no | _Por documentar_ |  |
| 18 | `response_size_bytes` | `integer` | sí | _Por documentar_ |  |
| 19 | `request_body` | `jsonb` | sí | _Por documentar_ |  |
| 20 | `request_body_size` | `integer` | sí | _Por documentar_ |  |
| 21 | `has_large_body` | `boolean` | sí | _Por documentar_ |  |
| 22 | `response_body` | `jsonb` | sí | _Por documentar_ |  |
| 23 | `response_body_size` | `integer` | sí | _Por documentar_ |  |
| 24 | `has_large_response` | `boolean` | sí | _Por documentar_ |  |
| 25 | `error_message` | `text` | sí | _Por documentar_ |  |
| 26 | `error_stack` | `text` | sí | _Por documentar_ |  |
| 27 | `timestamp` | `timestamp without time zone` | no | _Por documentar_ | PK |
| 28 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 29 | `action` | `character varying(100)` | sí | _Por documentar_ |  |
| 30 | `entity_name` | `character varying(100)` | sí | _Por documentar_ |  |
| 31 | `entity_id` | `character varying(100)` | sí | _Por documentar_ |  |
| 32 | `previous_data` | `jsonb` | sí | _Por documentar_ |  |
| 33 | `new_data` | `jsonb` | sí | _Por documentar_ |  |
| 34 | `changes` | `jsonb` | sí | _Por documentar_ |  |

## request_logs_2026_08

_Por documentar._

- Clave primaria: `id`, `timestamp`
- Filas: —

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `method` | `character varying(10)` | no | _Por documentar_ |  |
| 3 | `url` | `text` | no | _Por documentar_ |  |
| 4 | `path` | `text` | no | _Por documentar_ |  |
| 5 | `query_params` | `jsonb` | sí | _Por documentar_ |  |
| 6 | `module` | `character varying(100)` | sí | _Por documentar_ |  |
| 7 | `submodule` | `character varying(100)` | sí | _Por documentar_ |  |
| 8 | `version` | `character varying(10)` | sí | _Por documentar_ |  |
| 9 | `ip_address` | `character varying(45)` | sí | _Por documentar_ | Identificador en línea (IP) |
| 10 | `user_agent` | `text` | sí | _Por documentar_ |  |
| 11 | `origin` | `text` | sí | _Por documentar_ |  |
| 12 | `referer` | `text` | sí | _Por documentar_ |  |
| 13 | `user_id` | `bigint` | sí | _Por documentar_ |  |
| 14 | `user_email` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 15 | `user_role` | `character varying(100)` | sí | _Por documentar_ |  |
| 16 | `status_code` | `integer` | no | _Por documentar_ |  |
| 17 | `response_time_ms` | `integer` | no | _Por documentar_ |  |
| 18 | `response_size_bytes` | `integer` | sí | _Por documentar_ |  |
| 19 | `request_body` | `jsonb` | sí | _Por documentar_ |  |
| 20 | `request_body_size` | `integer` | sí | _Por documentar_ |  |
| 21 | `has_large_body` | `boolean` | sí | _Por documentar_ |  |
| 22 | `response_body` | `jsonb` | sí | _Por documentar_ |  |
| 23 | `response_body_size` | `integer` | sí | _Por documentar_ |  |
| 24 | `has_large_response` | `boolean` | sí | _Por documentar_ |  |
| 25 | `error_message` | `text` | sí | _Por documentar_ |  |
| 26 | `error_stack` | `text` | sí | _Por documentar_ |  |
| 27 | `timestamp` | `timestamp without time zone` | no | _Por documentar_ | PK |
| 28 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 29 | `action` | `character varying(100)` | sí | _Por documentar_ |  |
| 30 | `entity_name` | `character varying(100)` | sí | _Por documentar_ |  |
| 31 | `entity_id` | `character varying(100)` | sí | _Por documentar_ |  |
| 32 | `previous_data` | `jsonb` | sí | _Por documentar_ |  |
| 33 | `new_data` | `jsonb` | sí | _Por documentar_ |  |
| 34 | `changes` | `jsonb` | sí | _Por documentar_ |  |

## request_logs_2026_09

_Por documentar._

- Clave primaria: `id`, `timestamp`
- Filas: —

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `method` | `character varying(10)` | no | _Por documentar_ |  |
| 3 | `url` | `text` | no | _Por documentar_ |  |
| 4 | `path` | `text` | no | _Por documentar_ |  |
| 5 | `query_params` | `jsonb` | sí | _Por documentar_ |  |
| 6 | `module` | `character varying(100)` | sí | _Por documentar_ |  |
| 7 | `submodule` | `character varying(100)` | sí | _Por documentar_ |  |
| 8 | `version` | `character varying(10)` | sí | _Por documentar_ |  |
| 9 | `ip_address` | `character varying(45)` | sí | _Por documentar_ | Identificador en línea (IP) |
| 10 | `user_agent` | `text` | sí | _Por documentar_ |  |
| 11 | `origin` | `text` | sí | _Por documentar_ |  |
| 12 | `referer` | `text` | sí | _Por documentar_ |  |
| 13 | `user_id` | `bigint` | sí | _Por documentar_ |  |
| 14 | `user_email` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 15 | `user_role` | `character varying(100)` | sí | _Por documentar_ |  |
| 16 | `status_code` | `integer` | no | _Por documentar_ |  |
| 17 | `response_time_ms` | `integer` | no | _Por documentar_ |  |
| 18 | `response_size_bytes` | `integer` | sí | _Por documentar_ |  |
| 19 | `request_body` | `jsonb` | sí | _Por documentar_ |  |
| 20 | `request_body_size` | `integer` | sí | _Por documentar_ |  |
| 21 | `has_large_body` | `boolean` | sí | _Por documentar_ |  |
| 22 | `response_body` | `jsonb` | sí | _Por documentar_ |  |
| 23 | `response_body_size` | `integer` | sí | _Por documentar_ |  |
| 24 | `has_large_response` | `boolean` | sí | _Por documentar_ |  |
| 25 | `error_message` | `text` | sí | _Por documentar_ |  |
| 26 | `error_stack` | `text` | sí | _Por documentar_ |  |
| 27 | `timestamp` | `timestamp without time zone` | no | _Por documentar_ | PK |
| 28 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 29 | `action` | `character varying(100)` | sí | _Por documentar_ |  |
| 30 | `entity_name` | `character varying(100)` | sí | _Por documentar_ |  |
| 31 | `entity_id` | `character varying(100)` | sí | _Por documentar_ |  |
| 32 | `previous_data` | `jsonb` | sí | _Por documentar_ |  |
| 33 | `new_data` | `jsonb` | sí | _Por documentar_ |  |
| 34 | `changes` | `jsonb` | sí | _Por documentar_ |  |

## request_logs_2026_10

_Por documentar._

- Clave primaria: `id`, `timestamp`
- Filas: —

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `method` | `character varying(10)` | no | _Por documentar_ |  |
| 3 | `url` | `text` | no | _Por documentar_ |  |
| 4 | `path` | `text` | no | _Por documentar_ |  |
| 5 | `query_params` | `jsonb` | sí | _Por documentar_ |  |
| 6 | `module` | `character varying(100)` | sí | _Por documentar_ |  |
| 7 | `submodule` | `character varying(100)` | sí | _Por documentar_ |  |
| 8 | `version` | `character varying(10)` | sí | _Por documentar_ |  |
| 9 | `ip_address` | `character varying(45)` | sí | _Por documentar_ | Identificador en línea (IP) |
| 10 | `user_agent` | `text` | sí | _Por documentar_ |  |
| 11 | `origin` | `text` | sí | _Por documentar_ |  |
| 12 | `referer` | `text` | sí | _Por documentar_ |  |
| 13 | `user_id` | `bigint` | sí | _Por documentar_ |  |
| 14 | `user_email` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 15 | `user_role` | `character varying(100)` | sí | _Por documentar_ |  |
| 16 | `status_code` | `integer` | no | _Por documentar_ |  |
| 17 | `response_time_ms` | `integer` | no | _Por documentar_ |  |
| 18 | `response_size_bytes` | `integer` | sí | _Por documentar_ |  |
| 19 | `request_body` | `jsonb` | sí | _Por documentar_ |  |
| 20 | `request_body_size` | `integer` | sí | _Por documentar_ |  |
| 21 | `has_large_body` | `boolean` | sí | _Por documentar_ |  |
| 22 | `response_body` | `jsonb` | sí | _Por documentar_ |  |
| 23 | `response_body_size` | `integer` | sí | _Por documentar_ |  |
| 24 | `has_large_response` | `boolean` | sí | _Por documentar_ |  |
| 25 | `error_message` | `text` | sí | _Por documentar_ |  |
| 26 | `error_stack` | `text` | sí | _Por documentar_ |  |
| 27 | `timestamp` | `timestamp without time zone` | no | _Por documentar_ | PK |
| 28 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 29 | `action` | `character varying(100)` | sí | _Por documentar_ |  |
| 30 | `entity_name` | `character varying(100)` | sí | _Por documentar_ |  |
| 31 | `entity_id` | `character varying(100)` | sí | _Por documentar_ |  |
| 32 | `previous_data` | `jsonb` | sí | _Por documentar_ |  |
| 33 | `new_data` | `jsonb` | sí | _Por documentar_ |  |
| 34 | `changes` | `jsonb` | sí | _Por documentar_ |  |

## request_logs_current

_Por documentar._

- Clave primaria: `id`, `timestamp`
- Filas: —

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `method` | `character varying(10)` | no | _Por documentar_ |  |
| 3 | `url` | `text` | no | _Por documentar_ |  |
| 4 | `path` | `text` | no | _Por documentar_ |  |
| 5 | `query_params` | `jsonb` | sí | _Por documentar_ |  |
| 6 | `module` | `character varying(100)` | sí | _Por documentar_ |  |
| 7 | `submodule` | `character varying(100)` | sí | _Por documentar_ |  |
| 8 | `version` | `character varying(10)` | sí | _Por documentar_ |  |
| 9 | `ip_address` | `character varying(45)` | sí | _Por documentar_ | Identificador en línea (IP) |
| 10 | `user_agent` | `text` | sí | _Por documentar_ |  |
| 11 | `origin` | `text` | sí | _Por documentar_ |  |
| 12 | `referer` | `text` | sí | _Por documentar_ |  |
| 13 | `user_id` | `bigint` | sí | _Por documentar_ |  |
| 14 | `user_email` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 15 | `user_role` | `character varying(100)` | sí | _Por documentar_ |  |
| 16 | `status_code` | `integer` | no | _Por documentar_ |  |
| 17 | `response_time_ms` | `integer` | no | _Por documentar_ |  |
| 18 | `response_size_bytes` | `integer` | sí | _Por documentar_ |  |
| 19 | `request_body` | `jsonb` | sí | _Por documentar_ |  |
| 20 | `request_body_size` | `integer` | sí | _Por documentar_ |  |
| 21 | `has_large_body` | `boolean` | sí | _Por documentar_ |  |
| 22 | `response_body` | `jsonb` | sí | _Por documentar_ |  |
| 23 | `response_body_size` | `integer` | sí | _Por documentar_ |  |
| 24 | `has_large_response` | `boolean` | sí | _Por documentar_ |  |
| 25 | `error_message` | `text` | sí | _Por documentar_ |  |
| 26 | `error_stack` | `text` | sí | _Por documentar_ |  |
| 27 | `timestamp` | `timestamp without time zone` | no | _Por documentar_ | PK |
| 28 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 29 | `action` | `character varying(100)` | sí | _Por documentar_ |  |
| 30 | `entity_name` | `character varying(100)` | sí | _Por documentar_ |  |
| 31 | `entity_id` | `character varying(100)` | sí | _Por documentar_ |  |
| 32 | `previous_data` | `jsonb` | sí | _Por documentar_ |  |
| 33 | `new_data` | `jsonb` | sí | _Por documentar_ |  |
| 34 | `changes` | `jsonb` | sí | _Por documentar_ |  |

## request_logs_next_month

_Por documentar._

- Clave primaria: `id`, `timestamp`
- Filas: —

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `method` | `character varying(10)` | no | _Por documentar_ |  |
| 3 | `url` | `text` | no | _Por documentar_ |  |
| 4 | `path` | `text` | no | _Por documentar_ |  |
| 5 | `query_params` | `jsonb` | sí | _Por documentar_ |  |
| 6 | `module` | `character varying(100)` | sí | _Por documentar_ |  |
| 7 | `submodule` | `character varying(100)` | sí | _Por documentar_ |  |
| 8 | `version` | `character varying(10)` | sí | _Por documentar_ |  |
| 9 | `ip_address` | `character varying(45)` | sí | _Por documentar_ | Identificador en línea (IP) |
| 10 | `user_agent` | `text` | sí | _Por documentar_ |  |
| 11 | `origin` | `text` | sí | _Por documentar_ |  |
| 12 | `referer` | `text` | sí | _Por documentar_ |  |
| 13 | `user_id` | `bigint` | sí | _Por documentar_ |  |
| 14 | `user_email` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 15 | `user_role` | `character varying(100)` | sí | _Por documentar_ |  |
| 16 | `status_code` | `integer` | no | _Por documentar_ |  |
| 17 | `response_time_ms` | `integer` | no | _Por documentar_ |  |
| 18 | `response_size_bytes` | `integer` | sí | _Por documentar_ |  |
| 19 | `request_body` | `jsonb` | sí | _Por documentar_ |  |
| 20 | `request_body_size` | `integer` | sí | _Por documentar_ |  |
| 21 | `has_large_body` | `boolean` | sí | _Por documentar_ |  |
| 22 | `response_body` | `jsonb` | sí | _Por documentar_ |  |
| 23 | `response_body_size` | `integer` | sí | _Por documentar_ |  |
| 24 | `has_large_response` | `boolean` | sí | _Por documentar_ |  |
| 25 | `error_message` | `text` | sí | _Por documentar_ |  |
| 26 | `error_stack` | `text` | sí | _Por documentar_ |  |
| 27 | `timestamp` | `timestamp without time zone` | no | _Por documentar_ | PK |
| 28 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 29 | `action` | `character varying(100)` | sí | _Por documentar_ |  |
| 30 | `entity_name` | `character varying(100)` | sí | _Por documentar_ |  |
| 31 | `entity_id` | `character varying(100)` | sí | _Por documentar_ |  |
| 32 | `previous_data` | `jsonb` | sí | _Por documentar_ |  |
| 33 | `new_data` | `jsonb` | sí | _Por documentar_ |  |
| 34 | `changes` | `jsonb` | sí | _Por documentar_ |  |

## request_logs_prev_month

_Por documentar._

- Clave primaria: `id`, `timestamp`
- Filas: —

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `method` | `character varying(10)` | no | _Por documentar_ |  |
| 3 | `url` | `text` | no | _Por documentar_ |  |
| 4 | `path` | `text` | no | _Por documentar_ |  |
| 5 | `query_params` | `jsonb` | sí | _Por documentar_ |  |
| 6 | `module` | `character varying(100)` | sí | _Por documentar_ |  |
| 7 | `submodule` | `character varying(100)` | sí | _Por documentar_ |  |
| 8 | `version` | `character varying(10)` | sí | _Por documentar_ |  |
| 9 | `ip_address` | `character varying(45)` | sí | _Por documentar_ | Identificador en línea (IP) |
| 10 | `user_agent` | `text` | sí | _Por documentar_ |  |
| 11 | `origin` | `text` | sí | _Por documentar_ |  |
| 12 | `referer` | `text` | sí | _Por documentar_ |  |
| 13 | `user_id` | `bigint` | sí | _Por documentar_ |  |
| 14 | `user_email` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 15 | `user_role` | `character varying(100)` | sí | _Por documentar_ |  |
| 16 | `status_code` | `integer` | no | _Por documentar_ |  |
| 17 | `response_time_ms` | `integer` | no | _Por documentar_ |  |
| 18 | `response_size_bytes` | `integer` | sí | _Por documentar_ |  |
| 19 | `request_body` | `jsonb` | sí | _Por documentar_ |  |
| 20 | `request_body_size` | `integer` | sí | _Por documentar_ |  |
| 21 | `has_large_body` | `boolean` | sí | _Por documentar_ |  |
| 22 | `response_body` | `jsonb` | sí | _Por documentar_ |  |
| 23 | `response_body_size` | `integer` | sí | _Por documentar_ |  |
| 24 | `has_large_response` | `boolean` | sí | _Por documentar_ |  |
| 25 | `error_message` | `text` | sí | _Por documentar_ |  |
| 26 | `error_stack` | `text` | sí | _Por documentar_ |  |
| 27 | `timestamp` | `timestamp without time zone` | no | _Por documentar_ | PK |
| 28 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 29 | `action` | `character varying(100)` | sí | _Por documentar_ |  |
| 30 | `entity_name` | `character varying(100)` | sí | _Por documentar_ |  |
| 31 | `entity_id` | `character varying(100)` | sí | _Por documentar_ |  |
| 32 | `previous_data` | `jsonb` | sí | _Por documentar_ |  |
| 33 | `new_data` | `jsonb` | sí | _Por documentar_ |  |
| 34 | `changes` | `jsonb` | sí | _Por documentar_ |  |

## request_logs_stats

_Por documentar._

- Clave primaria: no declarada
- Filas: —
- Vista que usa: `audit.request_logs`

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `date` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 2 | `method` | `character varying(10)` | sí | _Por documentar_ |  |
| 3 | `module` | `character varying(100)` | sí | _Por documentar_ |  |
| 4 | `submodule` | `character varying(100)` | sí | _Por documentar_ |  |
| 5 | `status_code` | `integer` | sí | _Por documentar_ |  |
| 6 | `request_count` | `bigint` | sí | _Por documentar_ |  |
| 7 | `avg_response_time` | `numeric` | sí | _Por documentar_ |  |
| 8 | `median_response_time` | `double precision` | sí | _Por documentar_ |  |
| 9 | `max_response_time` | `integer` | sí | _Por documentar_ |  |
| 10 | `min_response_time` | `integer` | sí | _Por documentar_ |  |
