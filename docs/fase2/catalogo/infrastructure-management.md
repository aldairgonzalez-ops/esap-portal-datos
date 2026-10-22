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
| 1 | `id_bloque` | `uuid` | no | Identificador único del registro en la tabla bloque_edificio. Se genera automáticamente. | PK |
| 2 | `id_sede` | `uuid` | no | Referencia al registro de infrastructure-management.sede (id_sede). | FK→infrastructure-management.sede.id_sede |
| 3 | `codigo` | `character varying(30)` | no | Código del bloque o edificio. |  |
| 4 | `nombre` | `character varying(100)` | no | Nombre del bloque o edificio. |  |
| 5 | `pisos` | `integer` | no | Número de pisos del bloque o edificio. Por defecto, 1. |  |
| 6 | `descripcion` | `text` | sí | Descripción del bloque o edificio. |  |
| 7 | `is_activo` | `boolean` | no | Indica si el bloque o edificio está activo. |  |
| 8 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 9 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## catalogo_item

Catálogo genérico para listas parametrizables de infraestructura (tipos, prioridades, estados)

- Clave primaria: `id_catalogo`
- Filas: 45

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_catalogo` | `integer` | no | Identificador único del registro en la tabla catalogo_item. Se genera automáticamente. | PK |
| 2 | `catalogo` | `character varying(50)` | no | Nombre lógico del catálogo: TIPO_MANTENIMIENTO, PRIORIDAD, TIPO_ATENCION, ESTADO_SOLICITUD |  |
| 3 | `codigo` | `character varying(40)` | no | Valor stable que usa el frontend/backend (PK lógica visible) |  |
| 4 | `nombre` | `character varying(120)` | no | Nombre del elemento del catálogo. |  |
| 5 | `descripcion` | `text` | sí | Descripción del elemento del catálogo. |  |
| 6 | `orden` | `integer` | sí | Posición del elemento en el orden de presentación del catálogo. |  |
| 7 | `is_activo` | `boolean` | sí | Indica si el elemento del catálogo está activo. |  |
| 8 | `metadata` | `jsonb` | sí | JSON con estilo visual, íconos, agrupadores, SLA, etc. |  |

## espacio_fisico

_Por documentar._

- Clave primaria: `id_espacio`
- Filas: 81
- Referencia a: `id_bloque` → `infrastructure-management.bloque_edificio` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_espacio` | `uuid` | no | Identificador único del registro en la tabla espacio_fisico. Se genera automáticamente. | PK |
| 2 | `id_bloque` | `uuid` | no | Referencia al registro de infrastructure-management.bloque_edificio (id_bloque). | FK→infrastructure-management.bloque_edificio.id_bloque |
| 3 | `codigo` | `character varying(50)` | no | Código del espacio físico. |  |
| 4 | `nombre` | `character varying(150)` | no | Nombre del espacio físico. |  |
| 5 | `tipo` | `character varying(50)` | no | Tipo de espacio físico, por ejemplo AULA, AUDITORIO, LABORATORIO, OFICINA, BIBLIOTECA o SALA_CONSEJO. |  |
| 6 | `capacidad` | `integer` | no | Número de puestos del espacio físico; mínimo 1, por defecto 30. |  |
| 7 | `piso` | `integer` | no | Piso del bloque en que está el espacio. Por defecto, 1. |  |
| 8 | `area_m2` | `numeric(8,2)` | sí | Área del espacio en metros cuadrados. |  |
| 9 | `tiene_aire_acondicionado` | `boolean` | sí | Indica si el espacio físico tiene aire acondicionado. |  |
| 10 | `tiene_videobeam` | `boolean` | sí | Indica si el espacio físico tiene videobeam. |  |
| 11 | `tiene_computadores` | `boolean` | sí | Indica si el espacio físico tiene computadores. |  |
| 12 | `estado` | `character varying(30)` | no | Estado del espacio físico: DISPONIBLE, MANTENIMIENTO, INACTIVO o RESERVADO; por defecto DISPONIBLE. |  |
| 13 | `is_activo` | `boolean` | no | Indica si el espacio físico está activo. |  |
| 14 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 15 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## sede

_Por documentar._

- Clave primaria: `id_sede`
- Filas: 7

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_sede` | `uuid` | no | Identificador único del registro en la tabla sede. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(30)` | no | Código único de la sede. | única |
| 3 | `nombre` | `character varying(150)` | no | Nombre de la sede. |  |
| 4 | `tipo` | `character varying(50)` | no | Tipo de sede: SEDE_CENTRAL, TERRITORIAL o CETAP. |  |
| 5 | `departamento` | `character varying(100)` | no | Departamento donde está la sede. |  |
| 6 | `municipio` | `character varying(100)` | no | Municipio donde está la sede. |  |
| 7 | `direccion` | `character varying(255)` | no | Dirección de la sede. |  |
| 8 | `telefono` | `character varying(50)` | sí | Número de teléfono de la sede. |  |
| 9 | `email_contacto` | `character varying(100)` | sí | Correo electrónico de contacto de la sede. |  |
| 10 | `is_activo` | `boolean` | no | Indica si la sede está activa. |  |
| 11 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 12 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 13 | `alcance_umi` | `boolean` | sí | TRUE si la sede pertenece al alcance directo de la UMI (central o alternas; territoriales por ahora NO) |  |

## solicitud_evidencia

Evidencias/adjuntos subidos por el usuario al radicar o gestionar una solicitud de mantenimiento (fotos, PDFs, planos). Almacenado en MinIO, referenciado por URL

- Clave primaria: `id_evidencia`
- Filas: 6
- Referencia a: `id_solicitud` → `infrastructure-management.solicitud_mantenimiento` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_evidencia` | `uuid` | no | Identificador único del registro en la tabla solicitud_evidencia. Se genera automáticamente. | PK |
| 2 | `id_solicitud` | `uuid` | sí | FK a solicitud_mantenimiento. Puede ser NULL temporalmente cuando el usuario sube adjuntos ANTES de radicar; el create de solicitud lo actualiza a valor real vía uploadedEvidenciaIds. | FK→infrastructure-management.solicitud_mantenimiento.id_solicitud |
| 3 | `nombre_original` | `character varying(255)` | no | Nombre original del archivo subido por el usuario. |  |
| 4 | `nombre_almacenado` | `character varying(255)` | no | Nombre con que se guardó el archivo en el almacenamiento de objetos. |  |
| 5 | `ruta_objeto` | `character varying(512)` | no | key del objeto en MinIO sin protocolo (path dentro del bucket) |  |
| 6 | `bucket` | `character varying(80)` | no | Bucket de MinIO donde se guarda el archivo. Por defecto, infraestructura-evidencias. |  |
| 7 | `url_publica` | `text` | sí | URL relativa del archivo bajo el prefijo público del servicio, servida por el gateway en el mismo origen; no es una URL de bucket público y no expira. |  |
| 8 | `url_presigned` | `text` | sí | URL prefirmada de acceso temporal al archivo; vence en la fecha de vencimiento_presigned. |  |
| 9 | `vencimiento_presigned` | `timestamp with time zone` | sí | Fecha a partir de la cual la URL pre-firmada ya no sirve y hay que regenerarla |  |
| 10 | `mime_type` | `character varying(120)` | sí | Tipo MIME del archivo de evidencia. |  |
| 11 | `tamano_bytes` | `bigint` | no | Tamaño en bytes del archivo de evidencia. |  |
| 12 | `usuario_que_subio_id` | `uuid` | sí | Identificador del usuario que subió el archivo (auth."user".id_user, tomado del token). |  |
| 13 | `usuario_que_subio_email` | `character varying(180)` | sí | Correo electrónico del usuario que subió el archivo. | Contacto |
| 14 | `orden` | `integer` | sí | Posición de la evidencia en el orden de presentación. |  |
| 15 | `notas` | `text` | sí | Notas sobre la evidencia. |  |
| 16 | `fecha_subida` | `timestamp with time zone` | no | Fecha y hora en que se subió la evidencia. |  |

## solicitud_mantenimiento

_Por documentar._

- Clave primaria: `id_solicitud`
- Filas: 0
- Referencia a: `id_espacio` → `infrastructure-management.espacio_fisico` (0..1 → 0..1); `id_sede` → `infrastructure-management.sede` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_solicitud` | `uuid` | no | Identificador único del registro en la tabla solicitud_mantenimiento. Se genera automáticamente. | PK |
| 2 | `consecutivo` | `character varying(50)` | no | Consecutivo único de la solicitud de mantenimiento. | única |
| 3 | `id_espacio` | `uuid` | sí | Referencia al registro de infrastructure-management.espacio_fisico (id_espacio). | FK→infrastructure-management.espacio_fisico.id_espacio |
| 4 | `id_sede` | `uuid` | no | Referencia al registro de infrastructure-management.sede (id_sede). | FK→infrastructure-management.sede.id_sede |
| 5 | `tipo_mantenimiento` | `character varying(50)` | no | Tipo de mantenimiento solicitado: PREVENTIVO, CORRECTIVO, LOCATIVO o TECNOLOGICO. |  |
| 6 | `prioridad` | `character varying(30)` | no | Prioridad de la solicitud de mantenimiento: BAJA, MEDIA, ALTA o URGENTE. Por defecto, MEDIA. |  |
| 7 | `descripcion` | `text` | no | Descripción de la solicitud de mantenimiento. |  |
| 8 | `solicitante_email` | `character varying(150)` | no | Correo electrónico de quien solicita el mantenimiento. | Contacto |
| 9 | `solicitante_nombre` | `character varying(150)` | no | Nombre de quien solicita el mantenimiento. |  |
| 10 | `responsable_asignado` | `character varying(150)` | sí | Texto de visualización del técnico asignado, con el formato «código · nombre» (por ejemplo, TEC-CAR-001 · nombre), o el nombre de la oficina responsable. Es una columna heredada; la referencia vigente es id_tecnico_asignado. |  |
| 11 | `fecha_programada` | `date` | sí | Fecha programada para el mantenimiento. |  |
| 12 | `fecha_ejecucion` | `date` | sí | Fecha de ejecución del mantenimiento. |  |
| 13 | `estado` | `character varying(30)` | no | Estado formal de la solicitud (EFDS-1728). Válidos: RECIBIDA, EN_ANALISIS, PENDIENTE_CLASIFICACION, PENDIENTE_COTIZACION, PENDIENTE_APROBACION, EN_VALORACION, EN_PROCESO, ASIGNADA, EN_CAMPO_VALORACION, EN_ESPERA_DE_INSUMOS, EN_PROGRESO, EN_EJECUCION, PENDIENTE_RECURSO, COMPLETADA, CERRADA, CERRADA_SIN_ATENCION, RECHAZADA, REMITIDA_TI. |  |
| 14 | `observaciones` | `text` | sí | Observaciones sobre la solicitud de mantenimiento. |  |
| 15 | `costo_estimado` | `numeric(14,2)` | sí | _Por documentar_ |  |
| 16 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 17 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |
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
| 36 | `fecha_inicio_valoracion` | `timestamp with time zone` | sí | Fecha y hora de inicio de la valoración de la solicitud de mantenimiento. |  |
| 37 | `fecha_fin_valoracion` | `timestamp with time zone` | sí | Fecha y hora de finalización de la valoración de la solicitud de mantenimiento. |  |
| 38 | `riesgo_valoracion` | `character varying(10)` | sí | Nivel de riesgo identificado en la valoración técnica. Valores permitidos: ALTO, BAJO, MEDIO. |  |
| 39 | `requiere_apagado_electrico` | `boolean` | no | Indica si el mantenimiento requiere apagado eléctrico. |  |
| 40 | `total_estimado_insumos_cop` | `numeric(15,2)` | no | Valor total estimado de los insumos de la valoración, en pesos colombianos. Se calcula como la suma de cantidad por costo unitario de cada insumo al finalizar la valoración. Por defecto, 0. |  |
| 41 | `espera_insumos_flag` | `boolean` | no | Indica si la solicitud de mantenimiento está en espera de insumos. |  |
| 42 | `fecha_limite_original_antes_extension` | `timestamp with time zone` | sí | Fecha límite original de atención, antes de la extensión por espera de insumos. |  |
| 43 | `dias_extendidos_por_insumos` | `smallint` | no | Días calendario en que se extendió la fecha límite de atención por insumos no disponibles; corresponde al mayor tiempo de adquisición de los insumos. Por defecto, 0. |  |
| 44 | `fecha_cierre_tecnico` | `timestamp with time zone` | sí | Momento oficial del cierre técnico en estado COMPLETADA. EFDS-1736 RF-INF-007. |  |
| 45 | `usuario_cierre_tecnico_id` | `uuid` | sí | Identificador del usuario (auth."user".id_user) que hizo el cierre técnico de la solicitud. |  |
| 46 | `responsable_cierre_display` | `text` | sí | Nombre del responsable del cierre técnico para mostrar, con el formato «código · nombre» del técnico; lo arma el sistema al cerrar (si no hay técnico, usa el nombre de usuario). |  |
| 47 | `evidencias_cierre` | `jsonb` | no | Array jsonb de objetos {name,size,type,url,bucket,key} subidos a MinIO mantenimiento/cierre-tecnico/{idSolicitud}/. Mínimo 1 obligatorio. |  |
| 48 | `costo_final_efectivo_cop` | `numeric(15,2)` | no | Valor real ejecutado COP (incluye MO + materiales propios del técnico. Diferencia con costo_estimado para BI EFDS-1739. |  |
| 49 | `trabajo_realizado` | `text` | sí | Descripción min 15 chars del trabajo realizado por el técnico ejecutor. |  |
| 50 | `observaciones_cierre` | `text` | sí | Observaciones registradas en el cierre de la solicitud. |  |
| 51 | `requiere_seguimiento` | `boolean` | no | Si true el cierre marcado para seguimiento futuro en EFDS-1737 Conformidad o EFDS-1739 Reportes. |  |
| 52 | `id_tecnico_asignado` | `uuid` | sí | FK logico a auth.user.id_user del tecnico asignado para ejecutar la solicitud. Source of Truth = auth.user_roles (cod P3/P4). Reemplaza la columna legacy responsable_asignado varchar(TEC-xxx). |  |

## solicitud_valoracion

EFDS-1735 RF-INF-006. Cada fila es una visita técnica de inspección previa. 1-N con solicitud (se permiten revalorizaciones o segundas visitas).

- Clave primaria: `id_valoracion`
- Filas: 0
- Referencia a: `id_solicitud_mantenimiento` → `infrastructure-management.solicitud_mantenimiento` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_valoracion` | `uuid` | no | Identificador único del registro en la tabla solicitud_valoracion. Se genera automáticamente. | PK |
| 2 | `id_solicitud_mantenimiento` | `uuid` | no | Referencia al registro de infrastructure-management.solicitud_mantenimiento (id_solicitud). | FK→infrastructure-management.solicitud_mantenimiento.id_solicitud |
| 3 | `id_tecnico_valorador` | `uuid` | sí | Identificador del usuario (auth."user".id_user) del técnico que hizo la visita de valoración. |  |
| 4 | `tecnico_codigo` | `character varying(20)` | sí | Código del técnico en el catálogo TECNICO_MANTENIMIENTO (por ejemplo, TEC-CAR-001), tomado del prefijo de responsable_asignado de la solicitud. |  |
| 5 | `tecnico_nombre` | `character varying(200)` | no | Nombre del técnico que hizo la valoración. |  |
| 6 | `estado_al_finalizar` | `character varying(30)` | no | Estado en que queda la solicitud al terminar la valoración. Valores permitidos: EN_ESPERA_DE_INSUMOS, EN_PROGRESO. |  |
| 7 | `diagnostico` | `text` | no | Diagnóstico técnico de la visita de valoración. Mínimo 10 caracteres. |  |
| 8 | `alcance_identificado` | `text` | no | Alcance del trabajo identificado en la valoración. Mínimo 10 caracteres. |  |
| 9 | `tiempo_estimado_horas` | `numeric(6,2)` | no | Tiempo estimado del trabajo, en horas. Entre 0,25 y 240. |  |
| 10 | `nivel_riesgo` | `character varying(10)` | no | Nivel de riesgo identificado en la valoración. Valores permitidos: ALTO, BAJO, MEDIO. |  |
| 11 | `requiere_apagado_electrico` | `boolean` | no | Indica si la visita de valoración determinó que se requiere apagado eléctrico. |  |
| 12 | `observaciones` | `text` | sí | Observaciones de la visita de valoración. |  |
| 13 | `evidencias` | `jsonb` | no | Arreglo JSON de evidencias fotográficas/pdf de la inspección: [{nombre, url, tamaño_bytes, bucket_path}]. |  |
| 14 | `fecha_inicio_valoracion` | `timestamp with time zone` | no | Fecha y hora de inicio de la visita de valoración. |  |
| 15 | `fecha_fin_valoracion` | `timestamp with time zone` | no | Fecha y hora de finalización de la visita de valoración. |  |
| 16 | `es_version_corregida_por_encargado` | `boolean` | no | Indica si la valoración es una versión corregida por el encargado. |  |
| 17 | `id_usuario_corrector` | `uuid` | sí | _Por documentar_ |  |
| 18 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## solicitud_valoracion_insumo

EFDS-1735. Detalle fila-a-fila de materiales y repuestos requeridos para la ejecución de una visita de valoración. Restricción a nivel fila chk_tiempo_adquisicion_si_no_disponible: si disponibilidad=NO_DISPONIBLE_A_SOLICITAR, es obligatorio tiempo_adquisicion_dias para extender el SLA.

- Clave primaria: `id_insumo`
- Filas: 0
- Referencia a: `id_valoracion` → `infrastructure-management.solicitud_valoracion` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_insumo` | `uuid` | no | Identificador único del registro en la tabla solicitud_valoracion_insumo. Se genera automáticamente. | PK |
| 2 | `id_valoracion` | `uuid` | no | Referencia al registro de infrastructure-management.solicitud_valoracion (id_valoracion). | FK→infrastructure-management.solicitud_valoracion.id_valoracion |
| 3 | `codigo_insumo` | `character varying(50)` | sí | _Por documentar_ |  |
| 4 | `nombre` | `character varying(255)` | no | Nombre del insumo requerido para la valoración. |  |
| 5 | `cantidad` | `numeric(12,3)` | no | Cantidad requerida del insumo, expresada en la unidad de medida de la fila. Debe ser mayor que cero. |  |
| 6 | `unidad_medida` | `character varying(4)` | no | Unidad de medida del insumo. Valores permitidos: L, cj, glb, kg, m, m2, otro, paq, rol, un. |  |
| 7 | `costo_unitario_cop` | `numeric(15,2)` | no | Costo por unidad del insumo, en pesos colombianos. No puede ser negativo. |  |
| 8 | `subtotal_cop` | `numeric(15,2)` | sí | Subtotal del insumo en pesos colombianos: cantidad por costo unitario. |  |
| 9 | `disponibilidad` | `character varying(30)` | no | Disponibilidad del insumo para la visita. Valores permitidos: DISPONIBLE_EN_BODEGA, NO_DISPONIBLE_A_SOLICITAR. |  |
| 10 | `tiempo_adquisicion_dias` | `smallint` | sí | Tiempo estimado para adquirir el insumo, en días calendario (0 a 90). Es obligatorio cuando la disponibilidad es NO_DISPONIBLE_A_SOLICITAR y extiende la fecha límite de la solicitud. |  |
| 11 | `orden_item` | `smallint` | no | Posición del insumo en el listado de la valoración. |  |
| 12 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
