# Asistente virtual (chatbot) (`chatbot`)

Esquema para el módulo Asistente Virtual y ChatBot institucional ESAP

3 tablas · 0 vistas · 25 columnas · 0 filas · 0 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`conversacion`](#conversacion) | Tabla | 0 | Conversaciones del asistente virtual. Un registro por conversación de un usuario, con su correo, nombre, título, contexto, metadatos y si está activa; sus mensajes están en chatbot.mensaje. |
| [`mensaje`](#mensaje) | Tabla | 0 | Mensajes de las conversaciones del asistente virtual. Un registro por mensaje, con el autor (usuario, asistente o sistema), el texto, los tokens y los metadatos; se relaciona con chatbot.conversacion. |
| [`prompt_template`](#prompt_template) | Tabla | 0 | Catálogo de plantillas de instrucciones (prompts) de sistema del asistente virtual. Un registro por plantilla, con su código, nombre, descripción, el texto de instrucciones que se envía al modelo de lenguaje y si está activa. |

## conversacion

Conversaciones del asistente virtual. Un registro por conversación de un usuario, con su correo, nombre, título, contexto, metadatos y si está activa; sus mensajes están en chatbot.mensaje.

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla conversacion. Se genera automáticamente. | PK |
| 2 | `usuario_id` | `uuid` | sí | _Por documentar_ |  |
| 3 | `usuario_email` | `character varying(255)` | sí | Correo electrónico del usuario de la conversación. | Contacto |
| 4 | `usuario_nombre` | `character varying(255)` | sí | Nombre del usuario de la conversación. |  |
| 5 | `titulo` | `character varying(255)` | no | Título de la conversación. Valor inicial: «Nueva conversación». |  |
| 6 | `contexto` | `character varying(100)` | sí | _Por documentar_ |  |
| 7 | `metadatos` | `jsonb` | sí | Metadatos adicionales de la conversación, en formato JSON. |  |
| 8 | `is_activo` | `boolean` | no | Indica si la conversación está activa. |  |
| 9 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 10 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## mensaje

Mensajes de las conversaciones del asistente virtual. Un registro por mensaje, con el autor (usuario, asistente o sistema), el texto, los tokens y los metadatos; se relaciona con chatbot.conversacion.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `conversacion_id` → `chatbot.conversacion` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla mensaje. Se genera automáticamente. | PK |
| 2 | `conversacion_id` | `uuid` | no | Referencia al registro de chatbot.conversacion (id). | FK→chatbot.conversacion.id |
| 3 | `rol` | `character varying(30)` | no | Autor del mensaje dentro de la conversación. Valores permitidos: assistant, system, user. |  |
| 4 | `contenido` | `text` | no | Texto del mensaje. |  |
| 5 | `tokens` | `integer` | sí | _Por documentar_ |  |
| 6 | `metadatos` | `jsonb` | sí | Metadatos adicionales del mensaje, en formato JSON. |  |
| 7 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |

## prompt_template

Catálogo de plantillas de instrucciones (prompts) de sistema del asistente virtual. Un registro por plantilla, con su código, nombre, descripción, el texto de instrucciones que se envía al modelo de lenguaje y si está activa.

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla prompt_template. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(50)` | no | Código único de la plantilla de instrucciones (prompt). | única |
| 3 | `nombre` | `character varying(150)` | no | Nombre de la plantilla de instrucciones (prompt). |  |
| 4 | `descripcion` | `text` | sí | Descripción de la plantilla de instrucciones (prompt). |  |
| 5 | `system_prompt` | `text` | no | Texto de instrucciones de sistema (system prompt) que se envía al modelo de lenguaje con esta plantilla. |  |
| 6 | `is_activo` | `boolean` | no | Indica si la plantilla de instrucciones (prompt) está activa. |  |
| 7 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 8 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |
