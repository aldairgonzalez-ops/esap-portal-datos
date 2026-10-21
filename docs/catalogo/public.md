# Esquema público (`public`)

standard public schema

3 tablas · 0 vistas · 21 columnas · 12 filas · 3 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`config_entes_control`](#config_entes_control) | Tabla | 4 | _Por documentar_ |
| [`stage_configuration`](#stage_configuration) | Tabla | 7 | _Por documentar_ |
| [`system_configuration`](#system_configuration) | Tabla | 1 | _Por documentar_ |

## config_entes_control

_Por documentar._

- Clave primaria: `id`
- Filas: 4

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(50)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `color` | `character varying(20)` | sí | _Por documentar_ |  |
| 6 | `orden` | `integer` | sí | _Por documentar_ |  |
| 7 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 8 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 9 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |

## stage_configuration

_Por documentar._

- Clave primaria: `id`
- Filas: 7

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `etapa` | `character varying` | no | _Por documentar_ |  |
| 3 | `diasHabiles` | `integer` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `activo` | `boolean` | no | _Por documentar_ |  |
| 6 | `createdAt` | `timestamp without time zone` | no | _Por documentar_ |  |
| 7 | `updatedAt` | `timestamp without time zone` | no | _Por documentar_ |  |

## system_configuration

_Por documentar._

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `roleCapacities` | `jsonb` | no | _Por documentar_ |  |
| 3 | `notificationSettings` | `jsonb` | no | _Por documentar_ |  |
| 4 | `alertSettings` | `jsonb` | no | _Por documentar_ |  |
| 5 | `securitySettings` | `jsonb` | no | _Por documentar_ |  |
