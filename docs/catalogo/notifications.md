# Notificaciones (`notifications`)

Notificaciones de la plataforma dirigidas a los usuarios.

1 tablas · 0 vistas · 26 columnas · 6.345 filas · 0 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`notificacion`](#notificacion) | Tabla | 6345 | Notificaciones de la plataforma dirigidas a los usuarios (RF014). Un registro por notificación a un usuario destinatario, con su tipo de evento, módulo, título, mensaje, prioridad, acción asociada y datos adicionales; registra su lectura, archivo y marca de favorita, y el envío, entrega, apertura y clic del correo electrónico correspondiente. |

## notificacion

Notificaciones de la plataforma dirigidas a los usuarios (RF014). Un registro por notificación a un usuario destinatario, con su tipo de evento, módulo, título, mensaje, prioridad, acción asociada y datos adicionales; registra su lectura, archivo y marca de favorita, y el envío, entrega, apertura y clic del correo electrónico correspondiente.

- Clave primaria: `id_notificacion`
- Filas: 6345

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_notificacion` | `uuid` | no | Identificador único del registro en la tabla notificacion. Se genera automáticamente. | PK |
| 2 | `id_usuario_destinatario` | `uuid` | no | Identificador del usuario destinatario de la notificación. |  |
| 3 | `tipo_notificacion` | `character varying(100)` | no | Código del tipo de evento que genera la notificación, definido por cada servicio emisor; por ejemplo, PROCESO_ASIGNADO o VIATICOS_RADICADA. |  |
| 4 | `titulo` | `character varying(255)` | no | Título de la notificación. |  |
| 5 | `mensaje` | `text` | no | Texto del mensaje de la notificación. |  |
| 6 | `descripcion_corta` | `character varying(255)` | sí | Resumen corto de la notificación. |  |
| 7 | `icono` | `character varying(100)` | sí | Nombre del ícono que se muestra con la notificación; por ejemplo, AlertTriangle o FileCheck. |  |
| 8 | `color` | `character varying(50)` | sí | Color con que se muestra la notificación, como código hexadecimal (por ejemplo, #DC2626). |  |
| 9 | `prioridad` | `character varying(20)` | no | Prioridad de la notificación. Valores permitidos: Baja, Media, Alta, Crítica. Por defecto, Media. |  |
| 10 | `categoria` | `character varying(100)` | sí | Módulo o área de la notificación, usada para filtrar la bandeja; por ejemplo, VIATICOS, gestion-legal, DISCIPLINARIO o PTA. tipo_notificacion identifica el evento concreto. |  |
| 11 | `leida` | `boolean` | no | Indica si el destinatario leyó la notificación. |  |
| 12 | `archivada` | `boolean` | no | Indica si la notificación está archivada. |  |
| 13 | `fecha_creacion` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 14 | `fecha_lectura` | `timestamp with time zone` | sí | Fecha y hora en que se leyó la notificación. |  |
| 15 | `fecha_archivado` | `timestamp with time zone` | sí | Fecha y hora en que se archivó la notificación. |  |
| 16 | `tiene_accion` | `boolean` | no | Indica si la notificación tiene una acción asociada. |  |
| 17 | `texto_boton_accion` | `character varying(100)` | sí | Texto del botón de acción de la notificación. |  |
| 18 | `url_accion` | `character varying(500)` | sí | URL a la que dirige el botón de acción de la notificación. |  |
| 19 | `datos_adicionales` | `jsonb` | sí | Datos adicionales de la notificación, en formato JSON; las claves dependen del módulo emisor (por ejemplo, ptaId, componentes y periodo en el plan de trabajo académico). |  |
| 20 | `email_enviado` | `boolean` | no | Indica si la notificación se envió por correo electrónico. |  |
| 21 | `email_entregado` | `boolean` | no | Indica si el correo electrónico de la notificación fue entregado. |  |
| 22 | `email_abierto` | `boolean` | no | Indica si el destinatario abrió el correo electrónico de la notificación. |  |
| 23 | `email_click` | `boolean` | no | Indica si el destinatario hizo clic en el correo electrónico de la notificación. |  |
| 24 | `fecha_envio_email` | `timestamp with time zone` | sí | Fecha y hora del envío de la notificación por correo electrónico. |  |
| 25 | `fecha_apertura_email` | `timestamp with time zone` | sí | Fecha y hora en que se abrió el correo electrónico de la notificación. |  |
| 26 | `es_favorito` | `boolean` | no | Indica si el destinatario marcó la notificación como favorita. |  |
