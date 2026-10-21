# Plan de trabajo académico (`academic_work_plan`)

Planes de trabajo y asignación académica de docentes.

57 tablas · 0 vistas · 731 columnas · 39.324 filas · 6 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`AprobacionJefatura`](#aprobacionjefatura) | Tabla | 8 | _Por documentar_ |
| [`AuditLog`](#auditlog) | Tabla | 2 | _Por documentar_ |
| [`BancoDocentesInvitaciones`](#bancodocentesinvitaciones) | Tabla | 3 | Invitaciones de autogestión RUND (Canal 3): link público + OTP por correo. Estados: Enviada, Abierta, OTP validado, En proceso, Gestionada, Vencida. |
| [`CarpetaDigital`](#carpetadigital) | Tabla | 278 | _Por documentar_ |
| [`Certificado`](#certificado) | Tabla | 0 | _Por documentar_ |
| [`Concertacion`](#concertacion) | Tabla | 0 | _Por documentar_ |
| [`ConfiguracionSistema`](#configuracionsistema) | Tabla | 3 | _Por documentar_ |
| [`DetallesPta`](#detallespta) | Tabla | 0 | _Por documentar_ |
| [`Docente`](#docente) | Tabla | 814 | _Por documentar_ |
| [`Documento`](#documento) | Tabla | 2 | _Por documentar_ |
| [`DocumentoVersion`](#documentoversion) | Tabla | 0 | _Por documentar_ |
| [`HistorialEstadoPTA`](#historialestadopta) | Tabla | 51 | _Por documentar_ |
| [`PTAUserData`](#ptauserdata) | Tabla | 55 | _Por documentar_ |
| [`Permiso`](#permiso) | Tabla | 58 | _Por documentar_ |
| [`Persona`](#persona) | Tabla | 283 | _Por documentar_ |
| [`PersonaPrograma`](#personaprograma) | Tabla | 267 | _Por documentar_ |
| [`PlanTrabajoAcademico`](#plantrabajoacademico) | Tabla | 8 | _Por documentar_ |
| [`PtaComponentApproval`](#ptacomponentapproval) | Tabla | 99 | _Por documentar_ |
| [`PtaComponentReview`](#ptacomponentreview) | Tabla | 23 | _Por documentar_ |
| [`PtaEvento`](#ptaevento) | Tabla | 83 | _Por documentar_ |
| [`PtaEvidencia`](#ptaevidencia) | Tabla | 2 | _Por documentar_ |
| [`PtaTerritorialApproval`](#ptaterritorialapproval) | Tabla | 3 | _Por documentar_ |
| [`PtaTerritorialReview`](#ptaterritorialreview) | Tabla | 3 | _Por documentar_ |
| [`Rol`](#rol) | Tabla | 12 | _Por documentar_ |
| [`RolPermiso`](#rolpermiso) | Tabla | 55 | _Por documentar_ |
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
| [`Sede`](#sede) | Tabla | 280 | _Por documentar_ |
| [`SistemaAlerta`](#sistemaalerta) | Tabla | 1 | _Por documentar_ |
| [`SolicitudPTA`](#solicitudpta) | Tabla | 13 | _Por documentar_ |
| [`Territorial`](#territorial) | Tabla | 21 | _Por documentar_ |
| [`Usuario`](#usuario) | Tabla | 283 | _Por documentar_ |
| [`UsuarioRol`](#usuariorol) | Tabla | 278 | _Por documentar_ |
| [`asignatura`](#asignatura) | Tabla | 503 | _Por documentar_ |
| [`cetap`](#cetap) | Tabla | 290 | _Por documentar_ |
| [`cetap_alias`](#cetap_alias) | Tabla | 0 | _Por documentar_ |
| [`direccion_territorial`](#direccion_territorial) | Tabla | 18 | _Por documentar_ |
| [`docencia_concertada`](#docencia_concertada) | Tabla | 0 | _Por documentar_ |
| [`facultad`](#facultad) | Tabla | 4 | _Por documentar_ |
| [`nucleo_tematico`](#nucleo_tematico) | Tabla | 42 | _Por documentar_ |
| [`oferta_cetap_programa`](#oferta_cetap_programa) | Tabla | 337 | _Por documentar_ |
| [`periodo_academico`](#periodo_academico) | Tabla | 2 | _Por documentar_ |
| [`periodo_cetap`](#periodo_cetap) | Tabla | 576 | _Por documentar_ |
| [`programa`](#programa) | Tabla | 20 | _Por documentar_ |
| [`ubicacion_semestral`](#ubicacion_semestral) | Tabla | 16 | _Por documentar_ |
| [`validacion_documental`](#validacion_documental) | Tabla | 12000 | _Por documentar_ |

## AprobacionJefatura

_Por documentar._

- Clave primaria: `id`
- Filas: 8
- Referencia a: `ptaId` → `academic_work_plan.PlanTrabajoAcademico` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `ptaId` | `text` | no | _Por documentar_ | FK→academic_work_plan.PlanTrabajoAcademico.id |
| 3 | `jefaturaUserId` | `text` | no | _Por documentar_ |  |
| 4 | `jefaturaRol` | `text` | no | _Por documentar_ |  |
| 5 | `territorialId` | `text` | no | _Por documentar_ |  |
| 6 | `territorialNombre` | `text` | sí | _Por documentar_ |  |
| 7 | `decision` | `text` | no | _Por documentar_ |  |
| 8 | `comentarios` | `text` | sí | _Por documentar_ |  |
| 9 | `camposModificados` | `jsonb` | sí | _Por documentar_ |  |
| 10 | `componentesBloqueados` | `jsonb` | sí | _Por documentar_ |  |
| 11 | `firmaId` | `text` | sí | _Por documentar_ |  |
| 12 | `createdAt` | `timestamp with time zone` | no | _Por documentar_ |  |
| 13 | `updatedAt` | `timestamp with time zone` | no | _Por documentar_ |  |

## AuditLog

_Por documentar._

- Clave primaria: `id`
- Filas: 2

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `timestamp` | `timestamp(3) without time zone` | no | _Por documentar_ |  |
| 3 | `usuario_id` | `text` | sí | _Por documentar_ |  |
| 4 | `usuario_nombre` | `text` | sí | _Por documentar_ |  |
| 5 | `usuario_email` | `text` | sí | _Por documentar_ | Contacto |
| 6 | `accion` | `text` | no | _Por documentar_ |  |
| 7 | `modulo` | `text` | no | _Por documentar_ |  |
| 8 | `entidad_tipo` | `text` | sí | _Por documentar_ |  |
| 9 | `entidad_id` | `text` | sí | _Por documentar_ |  |
| 10 | `detalles` | `text` | no | _Por documentar_ |  |
| 11 | `resultado` | `text` | no | _Por documentar_ |  |
| 12 | `ip_address` | `text` | sí | _Por documentar_ | Identificador en línea (IP) |

## BancoDocentesInvitaciones

Invitaciones de autogestión RUND (Canal 3): link público + OTP por correo. Estados: Enviada, Abierta, OTP validado, En proceso, Gestionada, Vencida.

- Clave primaria: `id`
- Filas: 3

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `correo_institucional` | `text` | no | _Por documentar_ |  |
| 3 | `token_acceso` | `text` | no | _Por documentar_ | única Credencial de acceso |
| 4 | `otp_codigo` | `text` | sí | _Por documentar_ |  |
| 5 | `otp_expira_en` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 6 | `intentos_otp` | `integer` | no | _Por documentar_ |  |
| 7 | `estado` | `text` | no | _Por documentar_ |  |
| 8 | `fecha_expiracion` | `timestamp without time zone` | no | _Por documentar_ |  |
| 9 | `borrador_json` | `jsonb` | sí | _Por documentar_ |  |
| 10 | `createdAt` | `timestamp without time zone` | no | _Por documentar_ |  |
| 11 | `updatedAt` | `timestamp without time zone` | no | _Por documentar_ |  |
| 12 | `sesion_token_hash` | `text` | sí | _Por documentar_ | Credencial de acceso |
| 13 | `sesion_expira_en` | `timestamp with time zone` | sí | _Por documentar_ |  |

## CarpetaDigital

_Por documentar._

- Clave primaria: `id`
- Filas: 278
- Referencia a: `personaId` → `academic_work_plan.Persona` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `personaId` | `text` | no | _Por documentar_ | FK→academic_work_plan.Persona.id |
| 3 | `estado` | `text` | no | _Por documentar_ |  |
| 4 | `totalDocumentos` | `integer` | no | _Por documentar_ |  |
| 5 | `documentosRechazados` | `integer` | no | _Por documentar_ |  |
| 6 | `ultimaActualizacion` | `timestamp(3) without time zone` | no | _Por documentar_ |  |
| 7 | `createdAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |
| 8 | `updatedAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |

## Certificado

_Por documentar._

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `personaId` | `text` | no | _Por documentar_ |  |
| 3 | `tipo` | `text` | no | _Por documentar_ |  |
| 4 | `estado` | `text` | no | _Por documentar_ |  |
| 5 | `codigoQR` | `text` | sí | _Por documentar_ |  |
| 6 | `fechaEmision` | `timestamp(3) without time zone` | sí | _Por documentar_ |  |
| 7 | `createdAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |
| 8 | `updatedAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |

## Concertacion

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `ptaId` → `academic_work_plan.PlanTrabajoAcademico` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `ptaId` | `text` | no | _Por documentar_ | FK→academic_work_plan.PlanTrabajoAcademico.id |
| 3 | `autorId` | `text` | no | _Por documentar_ |  |
| 4 | `autorRol` | `text` | no | _Por documentar_ |  |
| 5 | `mensaje` | `text` | no | _Por documentar_ |  |
| 6 | `createdAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |

## ConfiguracionSistema

_Por documentar._

- Clave primaria: `clave`
- Filas: 3

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `clave` | `text` | no | _Por documentar_ | PK |
| 2 | `valor` | `jsonb` | no | _Por documentar_ |  |
| 3 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 4 | `updatedAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |

## DetallesPta

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `ptaId` → `academic_work_plan.PlanTrabajoAcademico` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `ptaId` | `text` | no | _Por documentar_ | FK→academic_work_plan.PlanTrabajoAcademico.id |
| 3 | `asignaturaId` | `text` | no | _Por documentar_ |  |
| 4 | `grupo` | `text` | sí | _Por documentar_ |  |
| 5 | `horas` | `integer` | no | _Por documentar_ |  |
| 6 | `modalidad` | `text` | no | _Por documentar_ |  |
| 7 | `createdAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |
| 8 | `estudiantes` | `integer` | no | _Por documentar_ |  |
| 9 | `territorialId` | `text` | sí | _Por documentar_ |  |
| 10 | `cetapId` | `text` | sí | _Por documentar_ |  |
| 11 | `fechaInicio` | `date` | sí | _Por documentar_ |  |
| 12 | `fechaFin` | `date` | sí | _Por documentar_ |  |
| 13 | `observaciones` | `text` | sí | _Por documentar_ |  |

## Docente

_Por documentar._

- Clave primaria: `id`
- Filas: 814
- Referencia a: `personaId` → `auth.personas` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `personaId` | `uuid` | no | _Por documentar_ | FK→auth.personas.id_person |
| 3 | `territorialId` | `text` | no | _Por documentar_ |  |
| 4 | `tipoVinculacion` | `text` | no | _Por documentar_ |  |
| 5 | `dedicacion` | `text` | no | _Por documentar_ |  |
| 6 | `estado` | `text` | no | _Por documentar_ |  |
| 7 | `createdAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |
| 8 | `updatedAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |
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
| 33 | `edadReferencia` | `integer` | sí | _Por documentar_ |  |
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
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `personaId` | `text` | no | _Por documentar_ | FK→academic_work_plan.Persona.id |
| 3 | `nombre` | `text` | no | _Por documentar_ |  |
| 4 | `url` | `text` | no | _Por documentar_ |  |
| 5 | `tipo` | `text` | no | _Por documentar_ |  |
| 6 | `createdAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |
| 7 | `categoria` | `text` | sí | _Por documentar_ |  |
| 8 | `comentarios` | `text` | sí | _Por documentar_ |  |
| 9 | `estado` | `text` | no | _Por documentar_ |  |
| 10 | `tamanoBytes` | `integer` | no | _Por documentar_ |  |
| 11 | `tipoDocumentoId` | `text` | sí | _Por documentar_ |  |
| 12 | `updatedAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |
| 13 | `versionActual` | `integer` | no | _Por documentar_ |  |
| 14 | `aprobadoPorId` | `text` | sí | _Por documentar_ |  |
| 15 | `aprobadoPorNombre` | `text` | sí | _Por documentar_ |  |

## DocumentoVersion

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `documentoId` → `academic_work_plan.Documento` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `documentoId` | `text` | no | _Por documentar_ | FK→academic_work_plan.Documento.id |
| 3 | `version` | `integer` | no | _Por documentar_ |  |
| 4 | `url` | `text` | no | _Por documentar_ |  |
| 5 | `nombre` | `text` | no | _Por documentar_ |  |
| 6 | `tamanoBytes` | `integer` | no | _Por documentar_ |  |
| 7 | `creadoPor` | `text` | sí | _Por documentar_ |  |
| 8 | `comentarios` | `text` | sí | _Por documentar_ |  |
| 9 | `createdAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |

## HistorialEstadoPTA

_Por documentar._

- Clave primaria: `id`
- Filas: 51
- Referencia a: `ptaId` → `academic_work_plan.PlanTrabajoAcademico` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `ptaId` | `text` | no | _Por documentar_ | FK→academic_work_plan.PlanTrabajoAcademico.id |
| 3 | `estadoAnterior` | `text` | sí | _Por documentar_ |  |
| 4 | `estadoNuevo` | `text` | no | _Por documentar_ |  |
| 5 | `actorId` | `text` | sí | _Por documentar_ |  |
| 6 | `actorRol` | `text` | sí | _Por documentar_ |  |
| 7 | `detallesTransicion` | `text` | sí | _Por documentar_ |  |
| 8 | `comentarios` | `text` | sí | _Por documentar_ |  |
| 9 | `createdAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |
| 10 | `version` | `integer` | sí | _Por documentar_ |  |
| 11 | `camposModificados` | `jsonb` | sí | _Por documentar_ |  |
| 12 | `tipoAccion` | `text` | sí | Clasificación de la acción para filtrado en la UI del historial. |  |
| 13 | `snapshotPta` | `jsonb` | sí | _Por documentar_ |  |

## PTAUserData

_Por documentar._

- Clave primaria: `id`
- Filas: 55

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `userId` | `text` | no | _Por documentar_ | única |
| 3 | `tags` | `jsonb` | no | _Por documentar_ |  |
| 4 | `notes` | `jsonb` | no | _Por documentar_ |  |
| 5 | `pinned` | `jsonb` | no | _Por documentar_ |  |
| 6 | `priority` | `jsonb` | no | _Por documentar_ |  |
| 7 | `createdAt` | `timestamp with time zone` | no | _Por documentar_ |  |
| 8 | `updatedAt` | `timestamp with time zone` | no | _Por documentar_ |  |

## Permiso

_Por documentar._

- Clave primaria: `id`
- Filas: 58

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `recurso` | `text` | no | _Por documentar_ |  |
| 3 | `accion` | `text` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `createdAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |

## Persona

_Por documentar._

- Clave primaria: `id`
- Filas: 283
- Referencia a: `usuarioId` → `academic_work_plan.Usuario` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `usuarioId` | `text` | no | _Por documentar_ | FK→academic_work_plan.Usuario.id |
| 3 | `identificacion` | `text` | sí | _Por documentar_ |  |
| 4 | `tipo_identificacion` | `text` | sí | _Por documentar_ |  |
| 5 | `telefono` | `text` | sí | _Por documentar_ | Contacto |
| 6 | `direccion` | `text` | sí | _Por documentar_ | Contacto |
| 7 | `createdAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |
| 8 | `updatedAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |
| 9 | `primer_nombre` | `text` | sí | _Por documentar_ | Nombre de persona |
| 10 | `segundo_nombre` | `text` | sí | _Por documentar_ | Nombre de persona |
| 11 | `primer_apellido` | `text` | sí | _Por documentar_ | Nombre de persona |
| 12 | `segundo_apellido` | `text` | sí | _Por documentar_ | Nombre de persona |
| 13 | `genero` | `text` | sí | _Por documentar_ | Dato personal |
| 14 | `fecha_nacimiento` | `timestamp(3) without time zone` | sí | _Por documentar_ |  |
| 15 | `extension_telefonica` | `text` | sí | _Por documentar_ |  |
| 16 | `correo_alternativo` | `text` | sí | _Por documentar_ | Contacto |
| 17 | `tipo_usuario` | `text` | sí | _Por documentar_ |  |
| 18 | `empresa_contratista` | `text` | sí | _Por documentar_ |  |
| 19 | `dependencia_grupo_programa` | `text` | sí | _Por documentar_ |  |
| 20 | `ubicacion_fisica` | `text` | sí | _Por documentar_ |  |
| 21 | `cargo_semestre` | `text` | sí | _Por documentar_ |  |
| 22 | `nombre_jefe_dependencia` | `text` | sí | _Por documentar_ |  |
| 23 | `contrato` | `text` | sí | _Por documentar_ |  |
| 24 | `tiempo_contrato_resolucion` | `text` | sí | _Por documentar_ |  |
| 25 | `fecha_fin_contrato` | `timestamp(3) without time zone` | sí | _Por documentar_ |  |
| 26 | `aplicacion` | `text` | sí | _Por documentar_ |  |
| 27 | `observaciones` | `text` | sí | _Por documentar_ |  |

## PersonaPrograma

_Por documentar._

- Clave primaria: `id`
- Filas: 267
- Referencia a: `personaId` → `academic_work_plan.Persona` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `personaId` | `text` | no | _Por documentar_ | FK→academic_work_plan.Persona.id |
| 3 | `programaId` | `text` | no | _Por documentar_ |  |
| 4 | `rolEnPrograma` | `text` | no | _Por documentar_ |  |
| 5 | `semestreActual` | `text` | sí | _Por documentar_ |  |
| 6 | `estado` | `text` | no | _Por documentar_ |  |
| 7 | `createdAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |

## PlanTrabajoAcademico

_Por documentar._

- Clave primaria: `id`
- Filas: 8
- Referencia a: `docenteId` → `academic_work_plan.Docente` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `docenteId` | `text` | no | _Por documentar_ | FK→academic_work_plan.Docente.id |
| 3 | `periodo` | `text` | no | _Por documentar_ |  |
| 4 | `estado` | `text` | no | _Por documentar_ |  |
| 5 | `horasTotales` | `integer` | no | _Por documentar_ |  |
| 6 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 7 | `createdAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |
| 8 | `updatedAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |
| 9 | `datosEstructurados` | `jsonb` | sí | _Por documentar_ |  |
| 10 | `dedicacion` | `text` | sí | _Por documentar_ |  |
| 11 | `horasAsignables` | `integer` | sí | _Por documentar_ |  |
| 12 | `semanasVinculacion` | `integer` | sí | _Por documentar_ |  |
| 13 | `tipoVinculacion` | `text` | sí | _Por documentar_ |  |
| 14 | `version` | `integer` | no | Versión lógica del PTA. Inicia en 1. Incrementa cada vez que el docente re-envía el PTA tras una devolución. |  |
| 15 | `nivelDevolucion` | `integer` | sí | Nivel al que regresa el PTA cuando el docente lo re-envíe tras una revisión. 1=Jefatura, 2=Decanatura, 3=G.Profesoral. |  |
| 16 | `camposModificadosPorRevisor` | `jsonb` | sí | Mapa de campos que el revisor modificó en la última iteración. Usado para highlighting visual en el portal del docente. Se limpia al iniciar la siguiente fase. |  |
| 17 | `snapshotAntesRevision` | `jsonb` | sí | Copia de datosEstructurados justo antes de que el revisor lo modificara. Permite comparación visual. |  |
| 18 | `motivoDevolucion` | `text` | sí | _Por documentar_ |  |
| 19 | `ultimoActorRol` | `text` | sí | _Por documentar_ |  |
| 20 | `estadoAntesCierrePeriodo` | `text` | sí | Estado funcional del PTA antes del cierre reversible causado por cambio de periodo. |  |
| 21 | `cerradoPorPeriodo` | `text` | sí | Código del periodo cuya activación puso temporalmente el PTA en Terminado. |  |

## PtaComponentApproval

_Por documentar._

- Clave primaria: `id`
- Filas: 99
- Referencia a: `pta_id` → `academic_work_plan.PlanTrabajoAcademico` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `pta_id` | `text` | no | _Por documentar_ | FK→academic_work_plan.PlanTrabajoAcademico.id |
| 3 | `componente` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 5 | `aprobador_id` | `character varying(100)` | sí | _Por documentar_ |  |
| 6 | `aprobador_nombre` | `character varying(200)` | sí | _Por documentar_ |  |
| 7 | `aprobador_rol` | `character varying(100)` | sí | _Por documentar_ |  |
| 8 | `comentarios` | `text` | sí | _Por documentar_ |  |
| 9 | `fecha_aprobacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 10 | `scope` | `character varying(50)` | sí | _Por documentar_ |  |
| 11 | `scope_id` | `character varying(100)` | sí | _Por documentar_ |  |
| 12 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 13 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 14 | `respuesta_docente` | `text` | sí | Respuesta del docente al reenviar un componente devuelto: por qué lo reenvía / qué corrigió. |  |

## PtaComponentReview

_Por documentar._

- Clave primaria: `id`
- Filas: 23
- Referencia a: `pta_id` → `academic_work_plan.PlanTrabajoAcademico` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `pta_id` | `text` | no | _Por documentar_ | FK→academic_work_plan.PlanTrabajoAcademico.id |
| 3 | `componente` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `subseccion` | `character varying(50)` | no | _Por documentar_ |  |
| 5 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 6 | `revisor_id` | `character varying(100)` | sí | _Por documentar_ |  |
| 7 | `revisor_nombre` | `character varying(200)` | sí | _Por documentar_ |  |
| 8 | `revisor_rol` | `character varying(100)` | sí | _Por documentar_ |  |
| 9 | `comentarios` | `text` | sí | _Por documentar_ |  |
| 10 | `respuesta_docente` | `text` | sí | _Por documentar_ |  |
| 11 | `fecha_revision` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `scope` | `character varying(50)` | sí | _Por documentar_ |  |
| 13 | `scope_id` | `character varying(100)` | sí | _Por documentar_ |  |
| 14 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 15 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |

## PtaEvento

_Por documentar._

- Clave primaria: `id`
- Filas: 83
- Referencia a: `ptaId` → `academic_work_plan.PlanTrabajoAcademico` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `ptaId` | `text` | no | _Por documentar_ | FK→academic_work_plan.PlanTrabajoAcademico.id |
| 3 | `docenteId` | `text` | sí | _Por documentar_ |  |
| 4 | `docenteNombre` | `text` | sí | _Por documentar_ |  |
| 5 | `tipo` | `text` | no | _Por documentar_ |  |
| 6 | `estadoAnterior` | `text` | sí | _Por documentar_ |  |
| 7 | `estadoNuevo` | `text` | sí | _Por documentar_ |  |
| 8 | `actor` | `text` | sí | _Por documentar_ |  |
| 9 | `actorRol` | `text` | sí | _Por documentar_ |  |
| 10 | `sistemaOrigen` | `text` | no | _Por documentar_ |  |
| 11 | `mensaje` | `text` | sí | _Por documentar_ |  |
| 12 | `leidoBackoffice` | `boolean` | no | _Por documentar_ |  |
| 13 | `leidoPortal` | `boolean` | no | _Por documentar_ |  |
| 14 | `metadata` | `jsonb` | sí | _Por documentar_ |  |
| 15 | `createdAt` | `timestamp without time zone` | no | _Por documentar_ |  |

## PtaEvidencia

_Por documentar._

- Clave primaria: `id`
- Filas: 2
- Referencia a: `ptaId` → `academic_work_plan.PlanTrabajoAcademico` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `ptaId` | `text` | no | _Por documentar_ | FK→academic_work_plan.PlanTrabajoAcademico.id |
| 3 | `nombre` | `text` | no | _Por documentar_ |  |
| 4 | `tipoArchivo` | `text` | no | _Por documentar_ |  |
| 5 | `tamanioBytes` | `integer` | no | _Por documentar_ |  |
| 6 | `categoria` | `text` | sí | _Por documentar_ |  |
| 7 | `componentePta` | `text` | sí | _Por documentar_ |  |
| 8 | `horasAvance` | `integer` | no | _Por documentar_ |  |
| 9 | `storagePath` | `text` | sí | _Por documentar_ |  |
| 10 | `storageUrl` | `text` | sí | _Por documentar_ |  |
| 11 | `subidoPor` | `text` | sí | _Por documentar_ |  |
| 12 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 13 | `estado` | `text` | no | _Por documentar_ |  |
| 14 | `estadoRevision` | `text` | no | _Por documentar_ |  |
| 15 | `revisadoPor` | `text` | sí | _Por documentar_ |  |
| 16 | `fechaRevision` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 17 | `comentarioRevision` | `text` | sí | _Por documentar_ |  |
| 18 | `createdAt` | `timestamp with time zone` | no | _Por documentar_ |  |
| 19 | `updatedAt` | `timestamp with time zone` | no | _Por documentar_ |  |
| 20 | `seccionExtension` | `text` | sí | _Por documentar_ |  |

## PtaTerritorialApproval

_Por documentar._

- Clave primaria: `id`
- Filas: 3
- Referencia a: `pta_id` → `academic_work_plan.PlanTrabajoAcademico` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `pta_id` | `text` | no | _Por documentar_ | FK→academic_work_plan.PlanTrabajoAcademico.id |
| 3 | `territorial_id` | `text` | no | _Por documentar_ |  |
| 4 | `territorial_nombre` | `text` | sí | _Por documentar_ |  |
| 5 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 6 | `actor_id` | `character varying(100)` | sí | _Por documentar_ |  |
| 7 | `actor_nombre` | `character varying(200)` | sí | _Por documentar_ |  |
| 8 | `actor_rol` | `character varying(100)` | sí | _Por documentar_ |  |
| 9 | `comentarios` | `text` | sí | _Por documentar_ |  |
| 10 | `fecha_decision` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 12 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 13 | `nivel` | `character varying(20)` | no | _Por documentar_ |  |
| 14 | `componente` | `character varying(60)` | no | _Por documentar_ |  |
| 15 | `scope` | `character varying(50)` | sí | _Por documentar_ |  |
| 16 | `scope_id` | `character varying(100)` | sí | _Por documentar_ |  |

## PtaTerritorialReview

_Por documentar._

- Clave primaria: `id`
- Filas: 3
- Referencia a: `pta_id` → `academic_work_plan.PlanTrabajoAcademico` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `pta_id` | `text` | no | _Por documentar_ | FK→academic_work_plan.PlanTrabajoAcademico.id |
| 3 | `territorial_id` | `text` | no | _Por documentar_ |  |
| 4 | `territorial_nombre` | `text` | sí | _Por documentar_ |  |
| 5 | `nivel` | `character varying(20)` | no | _Por documentar_ |  |
| 6 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 7 | `revisor_id` | `character varying(100)` | sí | _Por documentar_ |  |
| 8 | `revisor_nombre` | `character varying(200)` | sí | _Por documentar_ |  |
| 9 | `revisor_rol` | `character varying(100)` | sí | _Por documentar_ |  |
| 10 | `comentarios` | `text` | sí | _Por documentar_ |  |
| 11 | `fecha_revision` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 13 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 14 | `componente` | `character varying(60)` | no | _Por documentar_ |  |

## Rol

_Por documentar._

- Clave primaria: `id`
- Filas: 12

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `nombre` | `text` | no | _Por documentar_ |  |
| 3 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 4 | `isSystem` | `boolean` | no | _Por documentar_ |  |
| 5 | `estado` | `text` | no | _Por documentar_ |  |
| 6 | `createdAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |
| 7 | `updatedAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |

## RolPermiso

_Por documentar._

- Clave primaria: `id`
- Filas: 55
- Referencia a: `permisoId` → `academic_work_plan.Permiso` (0..1 → 1); `rolId` → `academic_work_plan.Rol` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `rolId` | `text` | no | _Por documentar_ | FK→academic_work_plan.Rol.id |
| 3 | `permisoId` | `text` | no | _Por documentar_ | FK→academic_work_plan.Permiso.id |
| 4 | `createdAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |

## RundAccesoDatosLog

_Por documentar._

- Clave primaria: `id`
- Filas: 9141

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `actor_id` | `text` | no | _Por documentar_ |  |
| 3 | `roles` | `text[]` | no | _Por documentar_ |  |
| 4 | `endpoint` | `text` | no | _Por documentar_ |  |
| 5 | `recurso_id` | `text` | sí | _Por documentar_ |  |
| 6 | `docentes` | `text[]` | no | _Por documentar_ |  |
| 7 | `campos` | `text[]` | no | _Por documentar_ |  |
| 8 | `resultado` | `text` | no | _Por documentar_ |  |
| 9 | `ip` | `text` | sí | _Por documentar_ | Identificador en línea (IP) |
| 10 | `createdAt` | `timestamp with time zone` | no | _Por documentar_ |  |

## RundAccesoExterno

_Por documentar._

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
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
| 13 | `createdAt` | `timestamp with time zone` | no | _Por documentar_ |  |

## RundAprobacionLog

Log de auditoría inmutable del RUND (BR-056). Sólo INSERT: registra crear/aprobar/devolver/editar/vincular soporte.

- Clave primaria: `id`
- Filas: 6760

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
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
| 14 | `createdAt` | `timestamp without time zone` | no | _Por documentar_ |  |

## RundCampoEstado

_Por documentar._

- Clave primaria: `id`
- Filas: 6594

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
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
| 12 | `createdAt` | `timestamp without time zone` | no | _Por documentar_ |  |
| 13 | `updatedAt` | `timestamp without time zone` | no | _Por documentar_ |  |

## RundCargaMasiva

Soporte documental inmutable de cada importación masiva de perfiles RUND.

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
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
| 12 | `createdAt` | `timestamp without time zone` | no | _Por documentar_ |  |
| 13 | `updatedAt` | `timestamp without time zone` | no | _Por documentar_ |  |

## RundDocumentoCategoria

_Por documentar._

- Clave primaria: `codigo`
- Filas: 10

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `codigo` | `text` | no | _Por documentar_ | PK |
| 2 | `nombre` | `text` | no | _Por documentar_ |  |
| 3 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 4 | `mime_permitidos` | `text[]` | no | _Por documentar_ |  |
| 5 | `tamano_maximo_bytes` | `bigint` | no | _Por documentar_ |  |
| 6 | `activo` | `boolean` | no | _Por documentar_ |  |
| 7 | `orden` | `integer` | no | _Por documentar_ |  |
| 8 | `createdAt` | `timestamp without time zone` | no | _Por documentar_ |  |
| 9 | `updatedAt` | `timestamp without time zone` | no | _Por documentar_ |  |

## RundDocumentoPerfil

REQ-RUND-F010: documentos PDF versionados del perfil docente, almacenados en OpenKM o proveedor local de desarrollo.

- Clave primaria: `id`
- Filas: 11
- Referencia a: `categoria_codigo` → `academic_work_plan.RundDocumentoCategoria` (0..* → 1); `reemplaza_id` → `academic_work_plan.RundDocumentoPerfil` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `documento_logico_id` | `uuid` | no | _Por documentar_ |  |
| 3 | `docente_id` | `uuid` | no | _Por documentar_ |  |
| 4 | `categoria_codigo` | `text` | no | _Por documentar_ | FK→academic_work_plan.RundDocumentoCategoria.codigo |
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
| 17 | `reemplaza_id` | `uuid` | sí | _Por documentar_ | FK→academic_work_plan.RundDocumentoPerfil.id |
| 18 | `rund_soporte_id` | `uuid` | sí | _Por documentar_ |  |
| 19 | `creado_por` | `text` | no | _Por documentar_ |  |
| 20 | `eliminado_por` | `text` | sí | _Por documentar_ |  |
| 21 | `eliminado_en` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 22 | `createdAt` | `timestamp without time zone` | no | _Por documentar_ |  |

## RundExtraccionInicio

_Por documentar._

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `boolean` | no | _Por documentar_ | PK |
| 2 | `desde` | `timestamp with time zone` | no | _Por documentar_ |  |

## RundExtraccionSugerencia

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `trabajo_id` → `academic_work_plan.RundExtraccionTrabajo` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `trabajo_id` | `uuid` | no | _Por documentar_ | FK→academic_work_plan.RundExtraccionTrabajo.id |
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
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `documento_id` | `uuid` | no | _Por documentar_ | FK→academic_work_plan.RundDocumentoPerfil.id |
| 3 | `docente_id` | `uuid` | no | _Por documentar_ |  |
| 4 | `estado` | `text` | no | _Por documentar_ |  |
| 5 | `intentos` | `integer` | no | _Por documentar_ |  |
| 6 | `disponible_en` | `timestamp with time zone` | no | _Por documentar_ |  |
| 7 | `lease_id` | `uuid` | sí | _Por documentar_ |  |
| 8 | `lease_hasta` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 9 | `perfil_base` | `jsonb` | no | _Por documentar_ |  |
| 10 | `motor` | `jsonb` | no | _Por documentar_ |  |
| 11 | `error_codigo` | `text` | sí | _Por documentar_ |  |
| 12 | `creado_por` | `text` | no | _Por documentar_ |  |
| 13 | `creado_en` | `timestamp with time zone` | no | _Por documentar_ |  |
| 14 | `actualizado_en` | `timestamp with time zone` | no | _Por documentar_ |  |
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
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
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
| 15 | `createdAt` | `timestamp without time zone` | no | _Por documentar_ |  |
| 16 | `updatedAt` | `timestamp without time zone` | no | _Por documentar_ |  |

## RundMacroDocenteConsultaLog

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `acceso_externo_id` → `academic_work_plan.RundAccesoExterno` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `tipo_consulta` | `text` | no | _Por documentar_ |  |
| 3 | `actor_id` | `text` | no | _Por documentar_ |  |
| 4 | `roles` | `text[]` | sí | _Por documentar_ |  |
| 5 | `acceso_externo_id` | `uuid` | sí | _Por documentar_ | FK→academic_work_plan.RundAccesoExterno.id |
| 6 | `docente_id` | `text` | sí | _Por documentar_ |  |
| 7 | `periodo` | `text` | sí | _Por documentar_ |  |
| 8 | `filtros` | `jsonb` | sí | _Por documentar_ |  |
| 9 | `total_resultados` | `integer` | sí | _Por documentar_ |  |
| 10 | `ip` | `text` | sí | _Por documentar_ | Identificador en línea (IP) |
| 11 | `createdAt` | `timestamp with time zone` | no | _Por documentar_ |  |

## RundSoporteCampo

_Por documentar._

- Clave primaria: `id`
- Filas: 12

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `docente_id` | `uuid` | sí | _Por documentar_ |  |
| 3 | `bloque` | `text` | sí | _Por documentar_ |  |
| 4 | `tipo_soporte` | `text` | sí | _Por documentar_ |  |
| 5 | `documento_carpeta_id` | `text` | sí | _Por documentar_ |  |
| 6 | `nombre_archivo` | `text` | sí | _Por documentar_ |  |
| 7 | `estado` | `character varying(50)` | no | _Por documentar_ |  |
| 8 | `cargado_por` | `character varying(255)` | sí | _Por documentar_ |  |
| 9 | `observacion` | `text` | sí | _Por documentar_ |  |
| 10 | `fecha_vencimiento` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `createdAt` | `timestamp without time zone` | no | _Por documentar_ |  |
| 12 | `documento_perfil_id` | `uuid` | sí | _Por documentar_ |  |
| 13 | `revisiones_campos` | `jsonb` | no | _Por documentar_ |  |

## Sede

_Por documentar._

- Clave primaria: `id`
- Filas: 280
- Referencia a: `territorialId` → `academic_work_plan.Territorial` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `territorialId` | `text` | no | _Por documentar_ | FK→academic_work_plan.Territorial.id |
| 3 | `nombre` | `text` | no | _Por documentar_ |  |
| 4 | `municipio` | `text` | sí | _Por documentar_ |  |
| 5 | `createdAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |
| 6 | `updatedAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |
| 7 | `codigo` | `text` | sí | _Por documentar_ | única |

## SistemaAlerta

_Por documentar._

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `tipo` | `text` | no | _Por documentar_ |  |
| 3 | `severidad` | `text` | no | _Por documentar_ |  |
| 4 | `mensaje` | `text` | no | _Por documentar_ |  |
| 5 | `entidadId` | `text` | sí | _Por documentar_ |  |
| 6 | `entidadRef` | `text` | sí | _Por documentar_ |  |
| 7 | `resuelta` | `boolean` | no | _Por documentar_ |  |
| 8 | `createdAt` | `timestamp with time zone` | no | _Por documentar_ |  |
| 9 | `updatedAt` | `timestamp with time zone` | no | _Por documentar_ |  |

## SolicitudPTA

_Por documentar._

- Clave primaria: `id`
- Filas: 13
- Referencia a: `docenteId` → `academic_work_plan.Docente` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `docenteId` | `text` | no | _Por documentar_ | FK→academic_work_plan.Docente.id |
| 3 | `docenteNombre` | `text` | no | _Por documentar_ |  |
| 4 | `docenteEmail` | `text` | sí | _Por documentar_ | Contacto |
| 5 | `caso` | `text` | no | _Por documentar_ |  |
| 6 | `razon` | `text` | no | _Por documentar_ |  |
| 7 | `justificacion` | `text` | no | _Por documentar_ |  |
| 8 | `casoLibre` | `text` | sí | _Por documentar_ |  |
| 9 | `archivos` | `jsonb` | sí | _Por documentar_ |  |
| 10 | `estado` | `text` | no | _Por documentar_ |  |
| 11 | `resueltoPor` | `text` | sí | _Por documentar_ |  |
| 12 | `resolucionFecha` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 13 | `resolucionMotivo` | `text` | sí | _Por documentar_ |  |
| 14 | `resolucionAccion` | `text` | sí | _Por documentar_ |  |
| 15 | `territorialNueva` | `text` | sí | _Por documentar_ |  |
| 16 | `horasPtaOriginal` | `integer` | sí | _Por documentar_ |  |
| 17 | `horasPtaNuevo` | `integer` | sí | _Por documentar_ |  |
| 18 | `notificacionLeida` | `boolean` | no | _Por documentar_ |  |
| 19 | `createdAt` | `timestamp with time zone` | no | _Por documentar_ |  |
| 20 | `updatedAt` | `timestamp with time zone` | no | _Por documentar_ |  |
| 21 | `tipoSolicitud` | `text` | no | _Por documentar_ |  |
| 22 | `ptaId` | `uuid` | sí | _Por documentar_ |  |
| 23 | `componentes` | `jsonb` | sí | _Por documentar_ |  |
| 24 | `estadoPtaAnterior` | `text` | sí | _Por documentar_ |  |
| 25 | `decisionesComponentes` | `jsonb` | sí | Estado y trazabilidad de la decisión independiente por componente solicitado. |  |

## Territorial

_Por documentar._

- Clave primaria: `id`
- Filas: 21

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `nombre` | `text` | no | _Por documentar_ |  |
| 3 | `codigo` | `text` | sí | _Por documentar_ |  |
| 4 | `createdAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |
| 5 | `updatedAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |

## Usuario

_Por documentar._

- Clave primaria: `id`
- Filas: 283

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `email` | `text` | no | _Por documentar_ | Contacto |
| 3 | `password` | `text` | no | _Por documentar_ | Credencial de acceso |
| 4 | `nombre` | `text` | sí | _Por documentar_ |  |
| 5 | `activo` | `boolean` | no | _Por documentar_ |  |
| 6 | `createdAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |
| 7 | `updatedAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |

## UsuarioRol

_Por documentar._

- Clave primaria: `id`
- Filas: 278
- Referencia a: `rolId` → `academic_work_plan.Rol` (0..* → 1); `usuarioId` → `academic_work_plan.Usuario` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | _Por documentar_ | PK |
| 2 | `usuarioId` | `text` | no | _Por documentar_ | FK→academic_work_plan.Usuario.id |
| 3 | `rolId` | `text` | no | _Por documentar_ | FK→academic_work_plan.Rol.id |
| 4 | `createdAt` | `timestamp(3) without time zone` | no | _Por documentar_ |  |

## asignatura

_Por documentar._

- Clave primaria: `id`
- Filas: 503
- Referencia a: `id_facultad` → `academic_work_plan.facultad` (1..* → 1); `id_nucleo_tematico` → `academic_work_plan.nucleo_tematico` (0..* → 1); `id_programa` → `academic_work_plan.programa` (0..* → 1); `id_ubicacion_semestral` → `academic_work_plan.ubicacion_semestral` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(20)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(200)` | no | _Por documentar_ |  |
| 4 | `nombre_base` | `character varying(200)` | sí | _Por documentar_ |  |
| 5 | `modalidad_sufijo` | `character varying(30)` | sí | _Por documentar_ |  |
| 6 | `modalidad` | `character varying(30)` | no | _Por documentar_ |  |
| 7 | `requiere_revision_modalidad` | `boolean` | no | _Por documentar_ |  |
| 8 | `creditos` | `smallint` | no | _Por documentar_ |  |
| 9 | `id_ubicacion_semestral` | `smallint` | no | _Por documentar_ | FK→academic_work_plan.ubicacion_semestral.id |
| 10 | `id_programa` | `bigint` | no | _Por documentar_ | FK→academic_work_plan.programa.id |
| 11 | `id_nucleo_tematico` | `bigint` | no | _Por documentar_ | FK→academic_work_plan.nucleo_tematico.id |
| 12 | `id_facultad` | `bigint` | no | _Por documentar_ | FK→academic_work_plan.facultad.id |
| 13 | `horas_fijas_pta` | `integer` | sí | _Por documentar_ |  |
| 14 | `tipo_excepcion` | `character varying(40)` | sí | _Por documentar_ |  |
| 15 | `activa` | `boolean` | no | _Por documentar_ |  |
| 16 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 17 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 18 | `created_by` | `bigint` | sí | _Por documentar_ |  |
| 19 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 20 | `updated_by` | `bigint` | sí | _Por documentar_ |  |
| 21 | `deleted_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 22 | `deleted_by` | `bigint` | sí | _Por documentar_ |  |
| 23 | `tipo_asignatura` | `character varying(30)` | no | _Por documentar_ |  |
| 24 | `pensum` | `character varying(50)` | sí | _Por documentar_ |  |
| 25 | `horas_clase` | `integer` | sí | _Por documentar_ |  |
| 26 | `horas_pta` | `integer` | sí | _Por documentar_ |  |

## cetap

_Por documentar._

- Clave primaria: `id`
- Filas: 290
- Referencia a: `id_direccion_territorial` → `academic_work_plan.direccion_territorial` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(20)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `nombre_normalizado` | `character varying(100)` | no | _Por documentar_ |  |
| 5 | `id_direccion_territorial` | `bigint` | no | _Por documentar_ | FK→academic_work_plan.direccion_territorial.id |
| 6 | `tipo` | `character varying(20)` | no | _Por documentar_ |  |
| 7 | `latitud` | `numeric(10,7)` | sí | _Por documentar_ |  |
| 8 | `longitud` | `numeric(10,7)` | sí | _Por documentar_ |  |
| 9 | `activo` | `boolean` | no | _Por documentar_ |  |
| 10 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 11 | `created_by` | `bigint` | sí | _Por documentar_ |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 13 | `updated_by` | `bigint` | sí | _Por documentar_ |  |
| 14 | `deleted_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 15 | `deleted_by` | `bigint` | sí | _Por documentar_ |  |

## cetap_alias

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `id_cetap` → `academic_work_plan.cetap` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | _Por documentar_ | PK |
| 2 | `id_cetap` | `bigint` | no | _Por documentar_ | FK→academic_work_plan.cetap.id |
| 3 | `alias` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `alias_normalizado` | `character varying(100)` | no | _Por documentar_ | única |
| 5 | `origen` | `character varying(50)` | sí | _Por documentar_ |  |
| 6 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 7 | `created_by` | `bigint` | sí | _Por documentar_ |  |

## direccion_territorial

_Por documentar._

- Clave primaria: `id`
- Filas: 18

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(20)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(50)` | no | _Por documentar_ | única |
| 4 | `nombre_normalizado` | `character varying(50)` | no | _Por documentar_ | única |
| 5 | `activo` | `boolean` | no | _Por documentar_ |  |
| 6 | `orden_visualizacion` | `integer` | no | _Por documentar_ |  |
| 7 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 8 | `created_by` | `bigint` | sí | _Por documentar_ |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 10 | `updated_by` | `bigint` | sí | _Por documentar_ |  |
| 11 | `deleted_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `deleted_by` | `bigint` | sí | _Por documentar_ |  |

## docencia_concertada

_Por documentar._

- Clave primaria: `id_concertacion`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_concertacion` | `uuid` | no | _Por documentar_ | PK |
| 2 | `documento_docente` | `character varying(40)` | no | _Por documentar_ | Identificación |
| 3 | `periodo` | `character varying(40)` | sí | _Por documentar_ |  |
| 4 | `nivel` | `character varying(10)` | no | _Por documentar_ |  |
| 5 | `horas` | `numeric(8,1)` | no | _Por documentar_ |  |
| 6 | `huella` | `character(64)` | no | _Por documentar_ |  |
| 7 | `asignaturas` | `jsonb` | no | _Por documentar_ |  |
| 8 | `firmas` | `jsonb` | no | _Por documentar_ |  |
| 9 | `registrada_por` | `character varying(80)` | sí | _Por documentar_ |  |
| 10 | `aplicada_en` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 11 | `recibida_en` | `timestamp with time zone` | no | _Por documentar_ |  |
| 12 | `actualizada_en` | `timestamp with time zone` | no | _Por documentar_ |  |
| 13 | `estado_aplicacion` | `character varying(40)` | sí | _Por documentar_ |  |
| 14 | `detalle_aplicacion` | `text` | sí | _Por documentar_ |  |
| 15 | `id_pta` | `text` | sí | _Por documentar_ |  |

## facultad

_Por documentar._

- Clave primaria: `id`
- Filas: 4

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(20)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(50)` | no | _Por documentar_ | única |
| 4 | `activo` | `boolean` | no | _Por documentar_ |  |
| 5 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 6 | `created_by` | `bigint` | sí | _Por documentar_ |  |
| 7 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 8 | `updated_by` | `bigint` | sí | _Por documentar_ |  |
| 9 | `deleted_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 10 | `deleted_by` | `bigint` | sí | _Por documentar_ |  |

## nucleo_tematico

_Por documentar._

- Clave primaria: `id`
- Filas: 42
- Referencia a: `id_programa` → `academic_work_plan.programa` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(20)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(100)` | no | _Por documentar_ | única |
| 4 | `id_programa` | `bigint` | sí | _Por documentar_ | FK→academic_work_plan.programa.id |
| 5 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 6 | `activo` | `boolean` | no | _Por documentar_ |  |
| 7 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 8 | `created_by` | `bigint` | sí | _Por documentar_ |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 10 | `updated_by` | `bigint` | sí | _Por documentar_ |  |
| 11 | `deleted_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `deleted_by` | `bigint` | sí | _Por documentar_ |  |

## oferta_cetap_programa

_Por documentar._

- Clave primaria: `id`
- Filas: 337
- Referencia a: `id_cetap` → `academic_work_plan.cetap` (0..* → 1); `id_periodo_academico` → `academic_work_plan.periodo_academico` (1..* → 1); `id_programa` → `academic_work_plan.programa` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | _Por documentar_ | PK |
| 2 | `id_cetap` | `bigint` | no | _Por documentar_ | FK→academic_work_plan.cetap.id |
| 3 | `id_programa` | `bigint` | no | _Por documentar_ | FK→academic_work_plan.programa.id |
| 4 | `id_periodo_academico` | `bigint` | no | _Por documentar_ | FK→academic_work_plan.periodo_academico.id |
| 5 | `cupos_estimados` | `integer` | sí | _Por documentar_ |  |
| 6 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 7 | `activa` | `boolean` | no | _Por documentar_ |  |
| 8 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 9 | `created_by` | `bigint` | sí | _Por documentar_ |  |
| 10 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `updated_by` | `bigint` | sí | _Por documentar_ |  |
| 12 | `deleted_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 13 | `deleted_by` | `bigint` | sí | _Por documentar_ |  |

## periodo_academico

_Por documentar._

- Clave primaria: `id`
- Filas: 2

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(10)` | no | _Por documentar_ | única |
| 3 | `anio` | `integer` | no | _Por documentar_ |  |
| 4 | `semestre` | `smallint` | no | _Por documentar_ |  |
| 5 | `fecha_inicio` | `date` | no | _Por documentar_ |  |
| 6 | `fecha_fin` | `date` | no | _Por documentar_ |  |
| 7 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 8 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 9 | `created_by` | `bigint` | sí | _Por documentar_ |  |
| 10 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 11 | `updated_by` | `bigint` | sí | _Por documentar_ |  |

## periodo_cetap

_Por documentar._

- Clave primaria: `id`
- Filas: 576
- Referencia a: `id_cetap` → `academic_work_plan.cetap` (1..* → 1); `id_periodo_academico` → `academic_work_plan.periodo_academico` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | _Por documentar_ | PK |
| 2 | `id_periodo_academico` | `bigint` | no | _Por documentar_ | FK→academic_work_plan.periodo_academico.id |
| 3 | `id_cetap` | `bigint` | no | _Por documentar_ | FK→academic_work_plan.cetap.id |
| 4 | `activo` | `boolean` | sí | _Por documentar_ |  |
| 5 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 6 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## programa

_Por documentar._

- Clave primaria: `id`
- Filas: 20
- Referencia a: `id_periodo_academico` → `academic_work_plan.periodo_academico` (0..* → 0..1); `id_facultad` → `academic_work_plan.facultad` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(20)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `nombre_excel` | `character varying(100)` | no | _Por documentar_ |  |
| 5 | `nombre_corto` | `character varying(30)` | no | _Por documentar_ |  |
| 6 | `id_facultad` | `bigint` | no | _Por documentar_ | FK→academic_work_plan.facultad.id |
| 7 | `tipo` | `character varying(20)` | no | _Por documentar_ |  |
| 8 | `modalidad` | `character varying(20)` | no | _Por documentar_ |  |
| 9 | `horas_base_por_credito` | `integer` | no | _Por documentar_ |  |
| 10 | `horas_pregrado_central` | `integer` | sí | _Por documentar_ |  |
| 11 | `activo` | `boolean` | no | _Por documentar_ |  |
| 12 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 13 | `created_by` | `bigint` | sí | _Por documentar_ |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 15 | `updated_by` | `bigint` | sí | _Por documentar_ |  |
| 16 | `deleted_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 17 | `deleted_by` | `bigint` | sí | _Por documentar_ |  |
| 18 | `id_periodo_academico` | `bigint` | sí | _Por documentar_ | FK→academic_work_plan.periodo_academico.id |
| 19 | `categoria_horas_circular003` | `character varying(50)` | sí | _Por documentar_ |  |
| 20 | `descripcion_categoria_circular003` | `text` | sí | _Por documentar_ |  |
| 21 | `horas_pta_referencia_circular003` | `character varying(150)` | sí | _Por documentar_ |  |
| 22 | `formula_calculo_horas` | `text` | sí | _Por documentar_ |  |

## ubicacion_semestral

_Por documentar._

- Clave primaria: `id`
- Filas: 16

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `smallint` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(10)` | no | _Por documentar_ | única |
| 3 | `etiqueta` | `character varying(30)` | no | _Por documentar_ | única |
| 4 | `tipo_programa` | `character varying(20)` | no | _Por documentar_ |  |
| 5 | `orden` | `smallint` | no | _Por documentar_ |  |

## validacion_documental

_Por documentar._

- Clave primaria: `id`
- Filas: 12000
- Referencia a: `docente_id` → `academic_work_plan.Docente` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `docente_id` | `text` | no | _Por documentar_ | FK→academic_work_plan.Docente.id |
| 3 | `campo_rund` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `tipo_documento_soporte` | `character varying(100)` | no | _Por documentar_ |  |
| 5 | `id_documento_carpeta` | `text` | sí | _Por documentar_ |  |
| 6 | `estado_documento` | `character varying(30)` | no | _Por documentar_ |  |
| 7 | `fecha_carga` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 8 | `fecha_validacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 9 | `validado_por` | `character varying(150)` | sí | _Por documentar_ |  |
| 10 | `observacion` | `text` | sí | _Por documentar_ |  |
| 11 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 12 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |
