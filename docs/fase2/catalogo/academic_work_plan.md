# RUND (`academic_work_plan`)

Tablas del módulo RUND (prefijo Rund) del esquema academic_work_plan y las tablas Docente y Documento, a las que hacen referencia por nombre de columna (docente_id, documento_id).

15 tablas · 0 vistas · 236 columnas · 23.344 filas · 4 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`Docente`](#docente) | Tabla | 814 | _Por documentar_ |
| [`Documento`](#documento) | Tabla | 2 | _Por documentar_ |
| [`RundAccesoDatosLog`](#rundaccesodatoslog) | Tabla | 9141 | _Por documentar_ |
| [`RundAccesoExterno`](#rundaccesoexterno) | Tabla | 0 | _Por documentar_ |
| [`RundAprobacionLog`](#rundaprobacionlog) | Tabla | 6760 | Log de auditoría inmutable del RUND (BR-056). Sólo INSERT: registra crear/aprobar/devolver/editar/vincular soporte. |
| [`RundCampoEstado`](#rundcampoestado) | Tabla | 6594 | _Por documentar_ |
| [`RundCargaMasiva`](#rundcargamasiva) | Tabla | 0 | Soporte documental inmutable de cada importación masiva de perfiles RUND. |
| [`RundDocumentoCategoria`](#runddocumentocategoria) | Tabla | 10 | _Por documentar_ |
| [`RundDocumentoPerfil`](#runddocumentoperfil) | Tabla | 11 | REQ-RUND-F010: documentos PDF versionados del perfil docente, almacenados en OpenKM o proveedor local de desarrollo. |
| [`RundExtraccionInicio`](#rundextraccioninicio) | Tabla | 0 | _Por documentar_ |
| [`RundExtraccionSugerencia`](#rundextraccionsugerencia) | Tabla | 0 | _Por documentar_ |
| [`RundExtraccionTrabajo`](#rundextracciontrabajo) | Tabla | 0 | _Por documentar_ |
| [`RundInvitacionDocente`](#rundinvitaciondocente) | Tabla | 0 | _Por documentar_ |
| [`RundMacroDocenteConsultaLog`](#rundmacrodocenteconsultalog) | Tabla | 0 | _Por documentar_ |
| [`RundSoporteCampo`](#rundsoportecampo) | Tabla | 12 | _Por documentar_ |

## Docente

_Por documentar._

- Clave primaria: `id`
- Filas: 814
- Referencia a: `personaId` → `auth.personas` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla Docente. Se genera automáticamente. | PK |
| 2 | `personaId` | `uuid` | no | Referencia al registro de auth.personas (id_person). | FK→auth.personas.id_person |
| 3 | `territorialId` | `text` | no | _Por documentar_ |  |
| 4 | `tipoVinculacion` | `text` | no | _Por documentar_ |  |
| 5 | `dedicacion` | `text` | no | _Por documentar_ |  |
| 6 | `estado` | `text` | no | _Por documentar_ |  |
| 7 | `createdAt` | `timestamp(3) without time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `updatedAt` | `timestamp(3) without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 9 | `escalafon` | `text` | sí | _Por documentar_ |  |
| 10 | `horasAsignables` | `integer` | no | _Por documentar_ |  |
| 11 | `sedeId` | `text` | sí | _Por documentar_ |  |
| 12 | `ordenListado` | `integer` | sí | _Por documentar_ |  |
| 13 | `vinculacionDisplay` | `text` | sí | _Por documentar_ |  |
| 14 | `dedicacionDisplay` | `text` | sí | _Por documentar_ |  |
| 15 | `nucleoTematico` | `text` | sí | _Por documentar_ |  |
| 16 | `nivelFormacion` | `text` | sí | _Por documentar_ |  |
| 17 | `perfilAcademicoPro` | `text` | sí | _Por documentar_ |  |
| 18 | `perfilAcademico` | `text` | sí | _Por documentar_ |  |
| 19 | `pregrado` | `text` | sí | _Por documentar_ |  |
| 20 | `especializacion` | `text` | sí | _Por documentar_ |  |
| 21 | `maestria` | `text` | sí | _Por documentar_ |  |
| 22 | `doctorado` | `text` | sí | _Por documentar_ |  |
| 23 | `posDoctorado` | `text` | sí | _Por documentar_ |  |
| 24 | `investigacion` | `text` | sí | _Por documentar_ |  |
| 25 | `origenVinculacion` | `text` | sí | _Por documentar_ |  |
| 26 | `actoAdministrativoVinculacion` | `text` | sí | _Por documentar_ |  |
| 27 | `correoInstitucional` | `text` | sí | _Por documentar_ |  |
| 28 | `ultimaEvaluacion` | `text` | sí | _Por documentar_ |  |
| 29 | `situacionAdministrativa` | `text` | sí | _Por documentar_ |  |
| 30 | `fechaInicioVinculacion` | `timestamp(3) without time zone` | sí | _Por documentar_ |  |
| 31 | `fechaFinVinculacion` | `timestamp(3) without time zone` | sí | _Por documentar_ |  |
| 32 | `puntajeSalarial` | `double precision` | sí | _Por documentar_ |  |
| 33 | `edadReferencia` | `integer` | sí | _Por documentar_ | Dato personal |
| 34 | `rangoEdad` | `text` | sí | _Por documentar_ |  |
| 35 | `regimenNormativo` | `text` | sí | _Por documentar_ |  |
| 36 | `periodoCarga` | `text` | sí | _Por documentar_ |  |
| 37 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 38 | `idRund` | `text` | sí | _Por documentar_ |  |
| 39 | `estadoAprobacion` | `text` | sí | _Por documentar_ |  |
| 40 | `completitud` | `jsonb` | sí | _Por documentar_ |  |
| 41 | `canal_origen` | `text` | sí | _Por documentar_ |  |
| 42 | `cetapId` | `text` | sí | Identificador opcional del CETAP asociado al docente. |  |
| 43 | `correoAlternativo` | `text` | sí | Correo personal o alternativo del docente para flujos RUND. | Contacto |
| 44 | `acepta_habeas_data` | `boolean` | sí | _Por documentar_ |  |
| 45 | `fecha_aceptacion_habeas_data` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 46 | `ip_creacion` | `character varying(50)` | sí | _Por documentar_ | Identificador en línea (IP) |
| 47 | `sexoBiologico` | `text` | sí | _Por documentar_ | Dato personal |
| 48 | `dedicacionHorasSemana` | `integer` | sí | _Por documentar_ |  |
| 49 | `situacionCategoria` | `text` | sí | _Por documentar_ |  |
| 50 | `territorialReportada` | `text` | sí | Nombre informativo reportado en RUND; no concede acceso ni asigna una territorial PTA. |  |
| 51 | `datosCargaMasiva` | `jsonb` | sí | Valores originales de las 38 columnas RUND de la última carga; protegidos por RBAC al consultar. |  |

## Documento

_Por documentar._

- Clave primaria: `id`
- Filas: 2
- Referencia a: `personaId` → `academic_work_plan.Persona` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla Documento. Se genera automáticamente. | PK |
| 2 | `personaId` | `text` | no | Referencia al registro de academic_work_plan.Persona (id). | FK→academic_work_plan.Persona.id |
| 3 | `nombre` | `text` | no | _Por documentar_ |  |
| 4 | `url` | `text` | no | _Por documentar_ |  |
| 5 | `tipo` | `text` | no | _Por documentar_ |  |
| 6 | `createdAt` | `timestamp(3) without time zone` | no | Fecha y hora de creación del registro. |  |
| 7 | `categoria` | `text` | sí | _Por documentar_ |  |
| 8 | `comentarios` | `text` | sí | _Por documentar_ |  |
| 9 | `estado` | `text` | no | _Por documentar_ |  |
| 10 | `tamanoBytes` | `integer` | no | _Por documentar_ |  |
| 11 | `tipoDocumentoId` | `text` | sí | _Por documentar_ |  |
| 12 | `updatedAt` | `timestamp(3) without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 13 | `versionActual` | `integer` | no | _Por documentar_ |  |
| 14 | `aprobadoPorId` | `text` | sí | _Por documentar_ |  |
| 15 | `aprobadoPorNombre` | `text` | sí | _Por documentar_ |  |

## RundAccesoDatosLog

_Por documentar._

- Clave primaria: `id`
- Filas: 9141

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundAccesoDatosLog. | PK |
| 2 | `actor_id` | `text` | no | _Por documentar_ |  |
| 3 | `roles` | `text[]` | no | _Por documentar_ |  |
| 4 | `endpoint` | `text` | no | _Por documentar_ |  |
| 5 | `recurso_id` | `text` | sí | _Por documentar_ |  |
| 6 | `docentes` | `text[]` | no | _Por documentar_ |  |
| 7 | `campos` | `text[]` | no | _Por documentar_ |  |
| 8 | `resultado` | `text` | no | _Por documentar_ |  |
| 9 | `ip` | `text` | sí | _Por documentar_ | Identificador en línea (IP) |
| 10 | `createdAt` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## RundAccesoExterno

_Por documentar._

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundAccesoExterno. Se genera automáticamente. | PK |
| 2 | `ente_nombre` | `text` | no | _Por documentar_ |  |
| 3 | `ente_contacto` | `text` | sí | _Por documentar_ |  |
| 4 | `token` | `text` | no | _Por documentar_ | única Credencial de acceso |
| 5 | `docente_id` | `text` | no | _Por documentar_ |  |
| 6 | `motivo` | `text` | sí | _Por documentar_ |  |
| 7 | `fecha_inicio` | `timestamp with time zone` | no | _Por documentar_ |  |
| 8 | `fecha_fin` | `timestamp with time zone` | no | _Por documentar_ |  |
| 9 | `activo` | `boolean` | no | _Por documentar_ |  |
| 10 | `otorgado_por` | `text` | no | _Por documentar_ |  |
| 11 | `revoked_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 12 | `revoked_by` | `text` | sí | _Por documentar_ |  |
| 13 | `createdAt` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## RundAprobacionLog

Log de auditoría inmutable del RUND (BR-056). Sólo INSERT: registra crear/aprobar/devolver/editar/vincular soporte.

- Clave primaria: `id`
- Filas: 6760

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundAprobacionLog. Se genera automáticamente. | PK |
| 2 | `docente_id` | `uuid` | no | _Por documentar_ |  |
| 3 | `bloque` | `text` | sí | _Por documentar_ |  |
| 4 | `accion` | `text` | no | _Por documentar_ |  |
| 5 | `actor_id` | `text` | no | _Por documentar_ |  |
| 6 | `canal_origen` | `text` | sí | _Por documentar_ |  |
| 7 | `campo_afectado` | `text` | sí | _Por documentar_ |  |
| 8 | `dato_previo` | `text` | sí | _Por documentar_ |  |
| 9 | `dato_nuevo` | `text` | sí | _Por documentar_ |  |
| 10 | `observacion` | `text` | sí | _Por documentar_ |  |
| 11 | `soporte_id` | `text` | sí | _Por documentar_ |  |
| 12 | `ip` | `text` | sí | _Por documentar_ | Identificador en línea (IP) |
| 13 | `metadata` | `jsonb` | sí | _Por documentar_ |  |
| 14 | `createdAt` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |

## RundCampoEstado

_Por documentar._

- Clave primaria: `id`
- Filas: 6594

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundCampoEstado. Se genera automáticamente. | PK |
| 2 | `docente_id` | `character varying(255)` | no | _Por documentar_ |  |
| 3 | `bloque` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 5 | `cargado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 6 | `revisado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `observacion` | `text` | sí | _Por documentar_ |  |
| 8 | `version` | `integer` | no | _Por documentar_ |  |
| 9 | `canal_origen` | `character varying(50)` | sí | _Por documentar_ |  |
| 10 | `soporte_ids` | `jsonb` | no | _Por documentar_ |  |
| 11 | `fecha_revision` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `createdAt` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 13 | `updatedAt` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## RundCargaMasiva

Soporte documental inmutable de cada importación masiva de perfiles RUND.

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundCargaMasiva. Se genera automáticamente. | PK |
| 2 | `nombre_archivo` | `text` | no | _Por documentar_ |  |
| 3 | `tipo_mime` | `text` | no | _Por documentar_ |  |
| 4 | `tamano_bytes` | `bigint` | no | _Por documentar_ |  |
| 5 | `sha256` | `character varying(64)` | no | _Por documentar_ |  |
| 6 | `contenido` | `bytea` | no | _Por documentar_ |  |
| 7 | `actor_id` | `text` | no | _Por documentar_ |  |
| 8 | `justificacion` | `text` | no | _Por documentar_ |  |
| 9 | `ip` | `text` | sí | _Por documentar_ | Identificador en línea (IP) |
| 10 | `estado` | `text` | no | _Por documentar_ |  |
| 11 | `resumen` | `jsonb` | no | _Por documentar_ |  |
| 12 | `createdAt` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 13 | `updatedAt` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## RundDocumentoCategoria

_Por documentar._

- Clave primaria: `codigo`
- Filas: 10

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `codigo` | `text` | no | Clave primaria de la tabla RundDocumentoCategoria: código. | PK |
| 2 | `nombre` | `text` | no | _Por documentar_ |  |
| 3 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 4 | `mime_permitidos` | `text[]` | no | _Por documentar_ |  |
| 5 | `tamano_maximo_bytes` | `bigint` | no | _Por documentar_ |  |
| 6 | `activo` | `boolean` | no | _Por documentar_ |  |
| 7 | `orden` | `integer` | no | _Por documentar_ |  |
| 8 | `createdAt` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `updatedAt` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## RundDocumentoPerfil

REQ-RUND-F010: documentos PDF versionados del perfil docente, almacenados en OpenKM o proveedor local de desarrollo.

- Clave primaria: `id`
- Filas: 11
- Referencia a: `categoria_codigo` → `academic_work_plan.RundDocumentoCategoria` (0..* → 1); `reemplaza_id` → `academic_work_plan.RundDocumentoPerfil` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundDocumentoPerfil. Se genera automáticamente. | PK |
| 2 | `documento_logico_id` | `uuid` | no | _Por documentar_ |  |
| 3 | `docente_id` | `uuid` | no | _Por documentar_ |  |
| 4 | `categoria_codigo` | `text` | no | Referencia al registro de academic_work_plan.RundDocumentoCategoria (codigo). | FK→academic_work_plan.RundDocumentoCategoria.codigo |
| 5 | `bloque` | `text` | sí | _Por documentar_ |  |
| 6 | `tipo_soporte` | `text` | sí | _Por documentar_ |  |
| 7 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 8 | `version` | `integer` | no | _Por documentar_ |  |
| 9 | `nombre_archivo` | `text` | no | _Por documentar_ |  |
| 10 | `mime_type` | `text` | no | _Por documentar_ |  |
| 11 | `tamano_bytes` | `bigint` | no | _Por documentar_ |  |
| 12 | `checksum_sha256` | `text` | no | _Por documentar_ |  |
| 13 | `proveedor_almacenamiento` | `text` | no | _Por documentar_ |  |
| 14 | `almacenamiento_id` | `text` | sí | _Por documentar_ |  |
| 15 | `almacenamiento_ruta` | `text` | no | _Por documentar_ |  |
| 16 | `estado` | `text` | no | _Por documentar_ |  |
| 17 | `reemplaza_id` | `uuid` | sí | Referencia al registro de academic_work_plan.RundDocumentoPerfil (id). | FK→academic_work_plan.RundDocumentoPerfil.id |
| 18 | `rund_soporte_id` | `uuid` | sí | _Por documentar_ |  |
| 19 | `creado_por` | `text` | no | Usuario que creó el registro. |  |
| 20 | `eliminado_por` | `text` | sí | _Por documentar_ |  |
| 21 | `eliminado_en` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 22 | `createdAt` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |

## RundExtraccionInicio

_Por documentar._

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `boolean` | no | Identificador único del registro en la tabla RundExtraccionInicio. | PK |
| 2 | `desde` | `timestamp with time zone` | no | _Por documentar_ |  |

## RundExtraccionSugerencia

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `trabajo_id` → `academic_work_plan.RundExtraccionTrabajo` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundExtraccionSugerencia. Se genera automáticamente. | PK |
| 2 | `trabajo_id` | `uuid` | no | Referencia al registro de academic_work_plan.RundExtraccionTrabajo (id). | FK→academic_work_plan.RundExtraccionTrabajo.id |
| 3 | `campo` | `text` | no | _Por documentar_ |  |
| 4 | `valor` | `text` | no | _Por documentar_ |  |
| 5 | `valor_previo` | `text` | sí | _Por documentar_ |  |
| 6 | `pagina` | `integer` | no | _Por documentar_ |  |
| 7 | `evidencia` | `text` | no | _Por documentar_ |  |
| 8 | `confianza` | `numeric` | no | _Por documentar_ |  |
| 9 | `baja_confianza` | `boolean` | no | _Por documentar_ |  |
| 10 | `estado` | `text` | no | _Por documentar_ |  |
| 11 | `valor_confirmado` | `text` | sí | _Por documentar_ |  |
| 12 | `revisado_por` | `text` | sí | _Por documentar_ |  |
| 13 | `motivo` | `text` | sí | _Por documentar_ |  |
| 14 | `revisado_en` | `timestamp with time zone` | sí | _Por documentar_ |  |

## RundExtraccionTrabajo

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `documento_id` → `academic_work_plan.RundDocumentoPerfil` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundExtraccionTrabajo. Se genera automáticamente. | PK |
| 2 | `documento_id` | `uuid` | no | Referencia al registro de academic_work_plan.RundDocumentoPerfil (id). | FK→academic_work_plan.RundDocumentoPerfil.id |
| 3 | `docente_id` | `uuid` | no | _Por documentar_ |  |
| 4 | `estado` | `text` | no | _Por documentar_ |  |
| 5 | `intentos` | `integer` | no | _Por documentar_ |  |
| 6 | `disponible_en` | `timestamp with time zone` | no | _Por documentar_ |  |
| 7 | `lease_id` | `uuid` | sí | _Por documentar_ |  |
| 8 | `lease_hasta` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 9 | `perfil_base` | `jsonb` | no | _Por documentar_ |  |
| 10 | `motor` | `jsonb` | no | _Por documentar_ |  |
| 11 | `error_codigo` | `text` | sí | _Por documentar_ |  |
| 12 | `creado_por` | `text` | no | Usuario que creó el registro. |  |
| 13 | `creado_en` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 14 | `actualizado_en` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 15 | `etapa` | `text` | no | _Por documentar_ |  |
| 16 | `etapa_desde` | `timestamp with time zone` | no | _Por documentar_ |  |
| 17 | `iniciado_en` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 18 | `notificacion_id` | `uuid` | no | _Por documentar_ |  |
| 19 | `notificado_en` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 20 | `notificacion_proxima` | `timestamp with time zone` | no | _Por documentar_ |  |

## RundInvitacionDocente

_Por documentar._

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundInvitacionDocente. Se genera automáticamente. | PK |
| 2 | `correo_institucional` | `character varying(255)` | no | _Por documentar_ |  |
| 3 | `documento_identidad` | `character varying(100)` | sí | _Por documentar_ | Identificación |
| 4 | `token_invitacion` | `character varying(255)` | no | _Por documentar_ | única Credencial de acceso |
| 5 | `otp_hash` | `character varying(255)` | sí | _Por documentar_ |  |
| 6 | `estado_invitacion` | `character varying(50)` | no | _Por documentar_ |  |
| 7 | `caducidad_token` | `timestamp without time zone` | no | _Por documentar_ |  |
| 8 | `intentos_otp` | `integer` | sí | _Por documentar_ |  |
| 9 | `bloqueo_hasta` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 10 | `fecha_envio` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `fecha_apertura` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `ultima_actividad` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 13 | `docente_id` | `text` | sí | _Por documentar_ |  |
| 14 | `operador_id` | `character varying(255)` | sí | _Por documentar_ |  |
| 15 | `createdAt` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 16 | `updatedAt` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## RundMacroDocenteConsultaLog

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `acceso_externo_id` → `academic_work_plan.RundAccesoExterno` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundMacroDocenteConsultaLog. Se genera automáticamente. | PK |
| 2 | `tipo_consulta` | `text` | no | _Por documentar_ |  |
| 3 | `actor_id` | `text` | no | _Por documentar_ |  |
| 4 | `roles` | `text[]` | sí | _Por documentar_ |  |
| 5 | `acceso_externo_id` | `uuid` | sí | Referencia al registro de academic_work_plan.RundAccesoExterno (id). | FK→academic_work_plan.RundAccesoExterno.id |
| 6 | `docente_id` | `text` | sí | _Por documentar_ |  |
| 7 | `periodo` | `text` | sí | _Por documentar_ |  |
| 8 | `filtros` | `jsonb` | sí | _Por documentar_ |  |
| 9 | `total_resultados` | `integer` | sí | _Por documentar_ |  |
| 10 | `ip` | `text` | sí | _Por documentar_ | Identificador en línea (IP) |
| 11 | `createdAt` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## RundSoporteCampo

_Por documentar._

- Clave primaria: `id`
- Filas: 12

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundSoporteCampo. Se genera automáticamente. | PK |
| 2 | `docente_id` | `uuid` | sí | _Por documentar_ |  |
| 3 | `bloque` | `text` | sí | _Por documentar_ |  |
| 4 | `tipo_soporte` | `text` | sí | _Por documentar_ |  |
| 5 | `documento_carpeta_id` | `text` | sí | _Por documentar_ |  |
| 6 | `nombre_archivo` | `text` | sí | _Por documentar_ |  |
| 7 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 8 | `cargado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 9 | `observacion` | `text` | sí | _Por documentar_ |  |
| 10 | `fecha_vencimiento` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `createdAt` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 12 | `documento_perfil_id` | `uuid` | sí | _Por documentar_ |  |
| 13 | `revisiones_campos` | `jsonb` | no | _Por documentar_ |  |
