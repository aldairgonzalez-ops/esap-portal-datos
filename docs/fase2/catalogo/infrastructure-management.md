# Gestión de infraestructura (`infrastructure-management`)

Esquema para la gestión de infraestructura física, sedes territoriales, bloques, aulas, espacios y solicitudes de mantenimiento ESAP

8 tablas · 0 vistas · 143 columnas · 162 filas · 0 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`bloque_edificio`](#bloque_edificio) | Tabla | 23 | _Por documentar_ |
| [`catalogo_item`](#catalogo_item) | Tabla | 45 | Catálogo genérico para listas parametrizables de infraestructura (tipos, prioridades, estados) |
| [`espacio_fisico`](#espacio_fisico) | Tabla | 81 | _Por documentar_ |
| [`sede`](#sede) | Tabla | 7 | _Por documentar_ |
| [`solicitud_evidencia`](#solicitud_evidencia) | Tabla | 6 | Evidencias/adjuntos subidos por el usuario al radicar o gestionar una solicitud de mantenimiento (fotos, PDFs, planos). Almacenado en MinIO, referenciado por URL |
| [`solicitud_mantenimiento`](#solicitud_mantenimiento) | Tabla | 0 | _Por documentar_ |
| [`solicitud_valoracion`](#solicitud_valoracion) | Tabla | 0 | EFDS-1735 RF-INF-006. Cada fila es una visita técnica de inspección previa. 1-N con solicitud (se permiten revalorizaciones o segundas visitas). |
| [`solicitud_valoracion_insumo`](#solicitud_valoracion_insumo) | Tabla | 0 | EFDS-1735. Detalle fila-a-fila de materiales y repuestos requeridos para la ejecución de una visita de valoración. Restricción a nivel fila chk_tiempo_adquisicion_si_no_disponible: si disponibilidad=NO_DISPONIBLE_A_SOLICITAR, es obligatorio tiempo_adquisicion_dias para extender el SLA. |

## bloque_edificio

_Por documentar._

- Clave primaria: `id_bloque`
- Filas: 23
- Referencia a: `id_sede` → `infrastructure-management.sede` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_bloque` | `uuid` | no | _Por documentar_ | PK |
| 2 | `id_sede` | `uuid` | no | _Por documentar_ | FK→infrastructure-management.sede.id_sede |
| 3 | `codigo` | `character varying(30)` | no | _Por documentar_ |  |
| 4 | `nombre` | `character varying(100)` | no | _Por documentar_ |  |
| 5 | `pisos` | `integer` | no | _Por documentar_ |  |
| 6 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 7 | `is_activo` | `boolean` | no | _Por documentar_ |  |
| 8 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 9 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |

## catalogo_item

Catálogo genérico para listas parametrizables de infraestructura (tipos, prioridades, estados)

- Clave primaria: `id_catalogo`
- Filas: 45

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_catalogo` | `integer` | no | _Por documentar_ | PK |
| 2 | `catalogo` | `character varying(50)` | no | Nombre lógico del catálogo: TIPO_MANTENIMIENTO, PRIORIDAD, TIPO_ATENCION, ESTADO_SOLICITUD |  |
| 3 | `codigo` | `character varying(40)` | no | Valor stable que usa el frontend/backend (PK lógica visible) |  |
| 4 | `nombre` | `character varying(120)` | no | _Por documentar_ |  |
| 5 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 6 | `orden` | `integer` | sí | _Por documentar_ |  |
| 7 | `is_activo` | `boolean` | sí | _Por documentar_ |  |
| 8 | `metadata` | `jsonb` | sí | JSON con estilo visual, íconos, agrupadores, SLA, etc. |  |

## espacio_fisico

_Por documentar._

- Clave primaria: `id_espacio`
- Filas: 81
- Referencia a: `id_bloque` → `infrastructure-management.bloque_edificio` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_espacio` | `uuid` | no | _Por documentar_ | PK |
| 2 | `id_bloque` | `uuid` | no | _Por documentar_ | FK→infrastructure-management.bloque_edificio.id_bloque |
| 3 | `codigo` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `nombre` | `character varying(150)` | no | _Por documentar_ |  |
| 5 | `tipo` | `character varying(50)` | no | _Por documentar_ |  |
| 6 | `capacidad` | `integer` | no | _Por documentar_ |  |
| 7 | `piso` | `integer` | no | _Por documentar_ |  |
| 8 | `area_m2` | `numeric(8,2)` | sí | _Por documentar_ |  |
| 9 | `tiene_aire_acondicionado` | `boolean` | sí | _Por documentar_ |  |
| 10 | `tiene_videobeam` | `boolean` | sí | _Por documentar_ |  |
| 11 | `tiene_computadores` | `boolean` | sí | _Por documentar_ |  |
| 12 | `estado` | `character varying(30)` | no | _Por documentar_ |  |
| 13 | `is_activo` | `boolean` | no | _Por documentar_ |  |
| 14 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 15 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |

## sede

_Por documentar._

- Clave primaria: `id_sede`
- Filas: 7

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_sede` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(30)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(150)` | no | _Por documentar_ |  |
| 4 | `tipo` | `character varying(50)` | no | _Por documentar_ |  |
| 5 | `departamento` | `character varying(100)` | no | _Por documentar_ |  |
| 6 | `municipio` | `character varying(100)` | no | _Por documentar_ |  |
| 7 | `direccion` | `character varying(255)` | no | _Por documentar_ |  |
| 8 | `telefono` | `character varying(50)` | sí | _Por documentar_ |  |
| 9 | `email_contacto` | `character varying(100)` | sí | _Por documentar_ |  |
| 10 | `is_activo` | `boolean` | no | _Por documentar_ |  |
| 11 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 12 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 13 | `alcance_umi` | `boolean` | sí | TRUE si la sede pertenece al alcance directo de la UMI (central o alternas; territoriales por ahora NO) |  |

## solicitud_evidencia

Evidencias/adjuntos subidos por el usuario al radicar o gestionar una solicitud de mantenimiento (fotos, PDFs, planos). Almacenado en MinIO, referenciado por URL

- Clave primaria: `id_evidencia`
- Filas: 6
- Referencia a: `id_solicitud` → `infrastructure-management.solicitud_mantenimiento` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_evidencia` | `uuid` | no | _Por documentar_ | PK |
| 2 | `id_solicitud` | `uuid` | sí | FK a solicitud_mantenimiento. Puede ser NULL temporalmente cuando el usuario sube adjuntos ANTES de radicar; el create de solicitud lo actualiza a valor real vía uploadedEvidenciaIds. | FK→infrastructure-management.solicitud_mantenimiento.id_solicitud |
| 3 | `nombre_original` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `nombre_almacenado` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `ruta_objeto` | `character varying(512)` | no | key del objeto en MinIO sin protocolo (path dentro del bucket) |  |
| 6 | `bucket` | `character varying(80)` | no | _Por documentar_ |  |
| 7 | `url_publica` | `text` | sí | _Por documentar_ |  |
| 8 | `url_presigned` | `text` | sí | _Por documentar_ |  |
| 9 | `vencimiento_presigned` | `timestamp with time zone` | sí | Fecha a partir de la cual la URL pre-firmada ya no sirve y hay que regenerarla |  |
| 10 | `mime_type` | `character varying(120)` | sí | _Por documentar_ |  |
| 11 | `tamano_bytes` | `bigint` | no | _Por documentar_ |  |
| 12 | `usuario_que_subio_id` | `uuid` | sí | _Por documentar_ |  |
| 13 | `usuario_que_subio_email` | `character varying(180)` | sí | _Por documentar_ | Contacto |
| 14 | `orden` | `integer` | sí | _Por documentar_ |  |
| 15 | `notas` | `text` | sí | _Por documentar_ |  |
| 16 | `fecha_subida` | `timestamp with time zone` | no | _Por documentar_ |  |

## solicitud_mantenimiento

_Por documentar._

- Clave primaria: `id_solicitud`
- Filas: 0
- Referencia a: `id_espacio` → `infrastructure-management.espacio_fisico` (0..1 → 0..1); `id_sede` → `infrastructure-management.sede` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_solicitud` | `uuid` | no | _Por documentar_ | PK |
| 2 | `consecutivo` | `character varying(50)` | no | _Por documentar_ | única |
| 3 | `id_espacio` | `uuid` | sí | _Por documentar_ | FK→infrastructure-management.espacio_fisico.id_espacio |
| 4 | `id_sede` | `uuid` | no | _Por documentar_ | FK→infrastructure-management.sede.id_sede |
| 5 | `tipo_mantenimiento` | `character varying(50)` | no | _Por documentar_ |  |
| 6 | `prioridad` | `character varying(30)` | no | _Por documentar_ |  |
| 7 | `descripcion` | `text` | no | _Por documentar_ |  |
| 8 | `solicitante_email` | `character varying(150)` | no | _Por documentar_ | Contacto |
| 9 | `solicitante_nombre` | `character varying(150)` | no | _Por documentar_ |  |
| 10 | `responsable_asignado` | `character varying(150)` | sí | _Por documentar_ |  |
| 11 | `fecha_programada` | `date` | sí | _Por documentar_ |  |
| 12 | `fecha_ejecucion` | `date` | sí | _Por documentar_ |  |
| 13 | `estado` | `character varying(30)` | no | Estado formal de la solicitud (EFDS-1728). Válidos: RECIBIDA, EN_ANALISIS, PENDIENTE_CLASIFICACION, PENDIENTE_COTIZACION, PENDIENTE_APROBACION, EN_VALORACION, EN_PROCESO, ASIGNADA, EN_CAMPO_VALORACION, EN_ESPERA_DE_INSUMOS, EN_PROGRESO, EN_EJECUCION, PENDIENTE_RECURSO, COMPLETADA, CERRADA, CERRADA_SIN_ATENCION, RECHAZADA, REMITIDA_TI. |  |
| 14 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 15 | `costo_estimado` | `numeric(14,2)` | sí | _Por documentar_ |  |
| 16 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 17 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 18 | `id_area_solicitante` | `uuid` | sí | FK (opcional por ahora) a la dependencia/area solicitante en auth.dependencias |  |
| 19 | `nombre_area_solicitante` | `character varying(150)` | sí | Nombre descriptivo del area solicitante, redundante para auditoria |  |
| 20 | `piso` | `character varying(20)` | sí | Piso o nivel de la ubicacion de la solicitud |  |
| 21 | `salon` | `character varying(100)` | sí | Salon, oficina o ubicacion especifica |  |
| 22 | `ubicacion_detalle` | `text` | sí | Detalle adicional de ubicacion cuando piso/salon no son suficientes |  |
| 23 | `tipo_atencion` | `character varying(20)` | no | FISICA (UMI) o TECNOLOGICA (TI). Para EFDS-1730 siempre FISICA, en EFDS-1731 se habilita la eleccion |  |
| 24 | `id_categoria` | `integer` | sí | FK catalogo_item.id_catalogo (CATEGORIA_SERVICIO oficial). INT, NULL en Fase2 opcional, obligatorio en EFDS-1732-v2 |  |
| 25 | `fecha_radicacion` | `timestamp with time zone` | sí | Fecha y hora oficial de radicacion generada en backend |  |
| 26 | `usuario_solicitante_id` | `uuid` | sí | Identificador del usuario autenticado que radico la solicitud (auth.user.id_user) |  |
| 27 | `usuario_solicitante_email` | `character varying(150)` | sí | Email del usuario autenticado que radico, redundante para trazabilidad | Contacto |
| 28 | `evidencia_inicial_url` | `text` | sí | URL legacy opcional de evidencia inicial cuando el usuario adjunta por link en vez de archivo. Preferible usar la relación 1:N en solicitud_evidencia. |  |
| 29 | `area_responsable_actual` | `character varying(30)` | no | EFDS-1731: Dueño actual del ticket. Distinto a tipo_atencion (clasificación). FISICA->UMI, TECNOLOGICA->TI. Filtro bandeja UMI. |  |
| 30 | `remisiones` | `jsonb` | no | EFDS-1731 AC-03: Array trazabilidad remisiones. Item: {fecha,usuario_id,usuario_email,origen_area,destino_area,motivo,canal_remision,consecutivo_cruzado_ti,estado_remision} |  |
| 31 | `id_subcategoria` | `integer` | sí | AC02 EFDS-1732 Subcategoria: id_catalogo hijo CATEGORIA_SERVICIO metadata.parentCodigo = categoriaPadre.codigo. Opcional Entrega1, admin puede agregar sin alterar 8 oficiales |  |
| 32 | `fecha_limite_atencion` | `timestamp with time zone` | sí | EFDS-1733 RF-INF-004: fecha_limite = fecha_radicacion + TIEMPO_RESPUESTA_DIAS (1..3) |  |
| 33 | `asignaciones` | `jsonb` | no | EFDS-1733: historial asignaciones reasignaciones [{fecha, tecnico_codigo, tecnico_nombre, motivo, modo AUTO_SUGERIDO/MANUAL, usuario}] |  |
| 34 | `motivo_rechazo` | `text` | sí | Hotfix 012 / EFDS-1734 RF-INF-005 AC02: Motivo rechazo encabezado UMI length>=10 visible solicitante. NULL cuando la solicitud no esta RECHAZADA. Backfill retroactivo con placeholder para registros RECHAZADA pre-migracion. |  |
| 35 | `estado_valoracion` | `character varying(20)` | no | Estado interno del proceso de valoración técnica previa (EFDS-1735). NO_APLICA cuando la solicitud salta directo a ejecución. |  |
| 36 | `fecha_inicio_valoracion` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 37 | `fecha_fin_valoracion` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 38 | `riesgo_valoracion` | `character varying(10)` | sí | _Por documentar_ |  |
| 39 | `requiere_apagado_electrico` | `boolean` | no | _Por documentar_ |  |
| 40 | `total_estimado_insumos_cop` | `numeric(15,2)` | no | _Por documentar_ |  |
| 41 | `espera_insumos_flag` | `boolean` | no | _Por documentar_ |  |
| 42 | `fecha_limite_original_antes_extension` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 43 | `dias_extendidos_por_insumos` | `smallint` | no | _Por documentar_ |  |
| 44 | `fecha_cierre_tecnico` | `timestamp with time zone` | sí | Momento oficial del cierre técnico en estado COMPLETADA. EFDS-1736 RF-INF-007. |  |
| 45 | `usuario_cierre_tecnico_id` | `uuid` | sí | _Por documentar_ |  |
| 46 | `responsable_cierre_display` | `text` | sí | _Por documentar_ |  |
| 47 | `evidencias_cierre` | `jsonb` | no | Array jsonb de objetos {name,size,type,url,bucket,key} subidos a MinIO mantenimiento/cierre-tecnico/{idSolicitud}/. Mínimo 1 obligatorio. |  |
| 48 | `costo_final_efectivo_cop` | `numeric(15,2)` | no | Valor real ejecutado COP (incluye MO + materiales propios del técnico. Diferencia con costo_estimado para BI EFDS-1739. |  |
| 49 | `trabajo_realizado` | `text` | sí | Descripción min 15 chars del trabajo realizado por el técnico ejecutor. |  |
| 50 | `observaciones_cierre` | `text` | sí | _Por documentar_ |  |
| 51 | `requiere_seguimiento` | `boolean` | no | Si true el cierre marcado para seguimiento futuro en EFDS-1737 Conformidad o EFDS-1739 Reportes. |  |
| 52 | `id_tecnico_asignado` | `uuid` | sí | FK logico a auth.user.id_user del tecnico asignado para ejecutar la solicitud. Source of Truth = auth.user_roles (cod P3/P4). Reemplaza la columna legacy responsable_asignado varchar(TEC-xxx). |  |

## solicitud_valoracion

EFDS-1735 RF-INF-006. Cada fila es una visita técnica de inspección previa. 1-N con solicitud (se permiten revalorizaciones o segundas visitas).

- Clave primaria: `id_valoracion`
- Filas: 0
- Referencia a: `id_solicitud_mantenimiento` → `infrastructure-management.solicitud_mantenimiento` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_valoracion` | `uuid` | no | _Por documentar_ | PK |
| 2 | `id_solicitud_mantenimiento` | `uuid` | no | _Por documentar_ | FK→infrastructure-management.solicitud_mantenimiento.id_solicitud |
| 3 | `id_tecnico_valorador` | `uuid` | sí | _Por documentar_ |  |
| 4 | `tecnico_codigo` | `character varying(20)` | sí | _Por documentar_ |  |
| 5 | `tecnico_nombre` | `character varying(200)` | no | _Por documentar_ |  |
| 6 | `estado_al_finalizar` | `character varying(30)` | no | _Por documentar_ |  |
| 7 | `diagnostico` | `text` | no | _Por documentar_ |  |
| 8 | `alcance_identificado` | `text` | no | _Por documentar_ |  |
| 9 | `tiempo_estimado_horas` | `numeric(6,2)` | no | _Por documentar_ |  |
| 10 | `nivel_riesgo` | `character varying(10)` | no | _Por documentar_ |  |
| 11 | `requiere_apagado_electrico` | `boolean` | no | _Por documentar_ |  |
| 12 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 13 | `evidencias` | `jsonb` | no | Arreglo JSON de evidencias fotográficas/pdf de la inspección: [{nombre, url, tamaño_bytes, bucket_path}]. |  |
| 14 | `fecha_inicio_valoracion` | `timestamp with time zone` | no | _Por documentar_ |  |
| 15 | `fecha_fin_valoracion` | `timestamp with time zone` | no | _Por documentar_ |  |
| 16 | `es_version_corregida_por_encargado` | `boolean` | no | _Por documentar_ |  |
| 17 | `id_usuario_corrector` | `uuid` | sí | _Por documentar_ |  |
| 18 | `created_at` | `timestamp with time zone` | no | _Por documentar_ |  |

## solicitud_valoracion_insumo

EFDS-1735. Detalle fila-a-fila de materiales y repuestos requeridos para la ejecución de una visita de valoración. Restricción a nivel fila chk_tiempo_adquisicion_si_no_disponible: si disponibilidad=NO_DISPONIBLE_A_SOLICITAR, es obligatorio tiempo_adquisicion_dias para extender el SLA.

- Clave primaria: `id_insumo`
- Filas: 0
- Referencia a: `id_valoracion` → `infrastructure-management.solicitud_valoracion` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_insumo` | `uuid` | no | _Por documentar_ | PK |
| 2 | `id_valoracion` | `uuid` | no | _Por documentar_ | FK→infrastructure-management.solicitud_valoracion.id_valoracion |
| 3 | `codigo_insumo` | `character varying(50)` | sí | _Por documentar_ |  |
| 4 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `cantidad` | `numeric(12,3)` | no | _Por documentar_ |  |
| 6 | `unidad_medida` | `character varying(4)` | no | _Por documentar_ |  |
| 7 | `costo_unitario_cop` | `numeric(15,2)` | no | _Por documentar_ |  |
| 8 | `subtotal_cop` | `numeric(15,2)` | sí | _Por documentar_ |  |
| 9 | `disponibilidad` | `character varying(30)` | no | _Por documentar_ |  |
| 10 | `tiempo_adquisicion_dias` | `smallint` | sí | _Por documentar_ |  |
| 11 | `orden_item` | `smallint` | no | _Por documentar_ |  |
| 12 | `created_at` | `timestamp with time zone` | no | _Por documentar_ |  |
