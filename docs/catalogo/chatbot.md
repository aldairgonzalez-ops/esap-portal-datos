# Asistente virtual (chatbot) (`chatbot`)

Esquema para el módulo Asistente Virtual y ChatBot institucional ESAP

3 tablas · 0 vistas · 25 columnas · 0 filas · 0 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`conversacion`](#conversacion) | Tabla | 0 | _Por documentar_ |
| [`mensaje`](#mensaje) | Tabla | 0 | _Por documentar_ |
| [`prompt_template`](#prompt_template) | Tabla | 0 | _Por documentar_ |

## conversacion

_Por documentar._

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `usuario_id` | `uuid` | sí | _Por documentar_ |  |
| 3 | `usuario_email` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 4 | `usuario_nombre` | `character varying(255)` | sí | _Por documentar_ |  |
| 5 | `titulo` | `character varying(255)` | no | _Por documentar_ |  |
| 6 | `contexto` | `character varying(100)` | sí | _Por documentar_ |  |
| 7 | `metadatos` | `jsonb` | sí | _Por documentar_ |  |
| 8 | `is_activo` | `boolean` | no | _Por documentar_ |  |
| 9 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 10 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |

## mensaje

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `conversacion_id` → `chatbot.conversacion` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `conversacion_id` | `uuid` | no | _Por documentar_ | FK→chatbot.conversacion.id |
| 3 | `rol` | `character varying(30)` | no | _Por documentar_ |  |
| 4 | `contenido` | `text` | no | _Por documentar_ |  |
| 5 | `tokens` | `integer` | sí | _Por documentar_ |  |
| 6 | `metadatos` | `jsonb` | sí | _Por documentar_ |  |
| 7 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |

## prompt_template

_Por documentar._

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(50)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(150)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `system_prompt` | `text` | no | _Por documentar_ |  |
| 6 | `is_activo` | `boolean` | no | _Por documentar_ |  |
| 7 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 8 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
