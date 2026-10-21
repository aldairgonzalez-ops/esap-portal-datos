# Notificaciones (`notifications`)

Mensajes y notificaciones enviados por la plataforma.

1 tablas · 0 vistas · 26 columnas · 6.324 filas · 0 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`notificacion`](#notificacion) | Tabla | 6324 | _Por documentar_ |

## notificacion

_Por documentar._

- Clave primaria: `id_notificacion`
- Filas: 6324

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_notificacion` | `uuid` | no | _Por documentar_ | PK |
| 2 | `id_usuario_destinatario` | `uuid` | no | _Por documentar_ |  |
| 3 | `tipo_notificacion` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `titulo` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `mensaje` | `text` | no | _Por documentar_ |  |
| 6 | `descripcion_corta` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `icono` | `character varying(100)` | sí | _Por documentar_ |  |
| 8 | `color` | `character varying(50)` | sí | _Por documentar_ |  |
| 9 | `prioridad` | `character varying(20)` | no | _Por documentar_ |  |
| 10 | `categoria` | `character varying(100)` | sí | _Por documentar_ |  |
| 11 | `leida` | `boolean` | no | _Por documentar_ |  |
| 12 | `archivada` | `boolean` | no | _Por documentar_ |  |
| 13 | `fecha_creacion` | `timestamp with time zone` | no | _Por documentar_ |  |
| 14 | `fecha_lectura` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 15 | `fecha_archivado` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 16 | `tiene_accion` | `boolean` | no | _Por documentar_ |  |
| 17 | `texto_boton_accion` | `character varying(100)` | sí | _Por documentar_ |  |
| 18 | `url_accion` | `character varying(500)` | sí | _Por documentar_ |  |
| 19 | `datos_adicionales` | `jsonb` | sí | _Por documentar_ |  |
| 20 | `email_enviado` | `boolean` | no | _Por documentar_ |  |
| 21 | `email_entregado` | `boolean` | no | _Por documentar_ |  |
| 22 | `email_abierto` | `boolean` | no | _Por documentar_ |  |
| 23 | `email_click` | `boolean` | no | _Por documentar_ |  |
| 24 | `fecha_envio_email` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 25 | `fecha_apertura_email` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 26 | `es_favorito` | `boolean` | no | _Por documentar_ |  |
