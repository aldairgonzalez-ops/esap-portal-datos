# RUND (`academic_work_plan`)

Tablas del módulo RUND (prefijo Rund) del esquema academic_work_plan y las tablas Docente y Documento, a las que hacen referencia por nombre de columna (docente_id, documento_id).

15 tablas · 0 vistas · 236 columnas · 23.344 filas · 4 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`Docente`](#docente) | Tabla | 814 | Registro de docentes del RUND. Un registro por docente y periodo de carga, con su vinculación, dedicación, sede, territorial, formación, situación administrativa, bolsa de horas del PTA y estado de aprobación (PENDIENTE_APROBACION, ACTIVO_RUND o DEVUELTO); se relaciona con auth.personas. Se diligencia por carga masiva, registro individual o autogestión del docente. |
| [`Documento`](#documento) | Tabla | 2 | _Por documentar_ |
| [`RundAccesoDatosLog`](#rundaccesodatoslog) | Tabla | 9141 | Bitácora de accesos a los datos de docentes del RUND. Un registro por consulta, con el usuario y sus roles, el servicio consultado, el recurso, los docentes y campos consultados, el resultado del control de acceso (completo, enmascarado o denegado) y la IP de origen. |
| [`RundAccesoExterno`](#rundaccesoexterno) | Tabla | 0 | Accesos temporales de entidades externas al Macro Docente (REQ-RUND-F022). Un registro por acceso otorgado, con la entidad, su contacto, el token, el docente que puede consultar, el motivo, la vigencia y quién lo otorgó o revocó; el acceso lo otorga GGP o la Dirección y las consultas hechas con él se registran en RundMacroDocenteConsultaLog. |
| [`RundAprobacionLog`](#rundaprobacionlog) | Tabla | 6760 | Log de auditoría inmutable del RUND (BR-056). Sólo INSERT: registra crear/aprobar/devolver/editar/vincular soporte. |
| [`RundCampoEstado`](#rundcampoestado) | Tabla | 6594 | Estado de aprobación de los bloques de campos del perfil RUND (BR-044). Un registro por docente y bloque (IDENTIDAD, FORMACION, VINCULACION, CONTACTO), con quién lo cargó y revisó, la observación, la versión, el canal de origen y los soportes vinculados. Ciclo: Pendiente, En revisión, Aprobado, Devuelto o Soporte faltante. |
| [`RundCargaMasiva`](#rundcargamasiva) | Tabla | 0 | Soporte documental inmutable de cada importación masiva de perfiles RUND. |
| [`RundDocumentoCategoria`](#runddocumentocategoria) | Tabla | 10 | Catálogo de categorías de documento del RUND. Un registro por categoría, con su código, nombre, descripción, tipos MIME permitidos, tamaño máximo de archivo, orden y si está activa; lo referencian los documentos del perfil (RundDocumentoPerfil). |
| [`RundDocumentoPerfil`](#runddocumentoperfil) | Tabla | 11 | REQ-RUND-F010: documentos PDF versionados del perfil docente, almacenados en OpenKM o proveedor local de desarrollo. |
| [`RundExtraccionInicio`](#rundextraccioninicio) | Tabla | 0 | _Por documentar_ |
| [`RundExtraccionSugerencia`](#rundextraccionsugerencia) | Tabla | 0 | Sugerencias de valores extraídos de documentos del perfil RUND (REQ-RUND-F014). Un registro por campo sugerido en un trabajo de extracción, con el valor sugerido, el valor previo, la página y el fragmento de evidencia, la confianza y la decisión del revisor; se relaciona con RundExtraccionTrabajo. Ciclo: pendiente, aprobada, corregida o descartada. |
| [`RundExtraccionTrabajo`](#rundextracciontrabajo) | Tabla | 0 | Trabajos de extracción de datos de los documentos del perfil RUND. Un registro por documento procesado de un docente, con el estado, los intentos, la reserva del proceso que lo toma, el perfil base, el motor de procesamiento, el error y el aviso de fin; se relaciona con RundDocumentoPerfil y sus sugerencias están en RundExtraccionSugerencia. Ciclo: pendiente, procesando, completado, error u obsoleto. |
| [`RundInvitacionDocente`](#rundinvitaciondocente) | Tabla | 0 | _Por documentar_ |
| [`RundMacroDocenteConsultaLog`](#rundmacrodocenteconsultalog) | Tabla | 0 | Bitácora de consultas al Macro Docente (REQ-RUND-F020/F022). Un registro por consulta, con su tipo (macro docente, consulta puntual o externa), quién la hizo y con qué roles, los filtros, el docente y periodo consultados, el número de resultados y la IP; se relaciona con RundAccesoExterno cuando la consulta se hace con un acceso externo. Solo admite inserciones. |
| [`RundSoporteCampo`](#rundsoportecampo) | Tabla | 12 | Soportes de los bloques de campos del perfil RUND (BR-038, BR-039, BR-041). Un registro por soporte de un docente y bloque, con el tipo de soporte, la referencia al documento en la Carpeta Digital o en RundDocumentoPerfil, el estado (Pendiente, Aprobado o Rechazado), la observación del revisor, la fecha de vencimiento y la revisión de cada campo. |

## Docente

Registro de docentes del RUND. Un registro por docente y periodo de carga, con su vinculación, dedicación, sede, territorial, formación, situación administrativa, bolsa de horas del PTA y estado de aprobación (PENDIENTE_APROBACION, ACTIVO_RUND o DEVUELTO); se relaciona con auth.personas. Se diligencia por carga masiva, registro individual o autogestión del docente.

- Clave primaria: `id`
- Filas: 814
- Referencia a: `personaId` → `auth.personas` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla Docente. Se genera automáticamente. | PK |
| 2 | `personaId` | `uuid` | no | Referencia al registro de auth.personas (id_person). | FK→auth.personas.id_person |
| 3 | `territorialId` | `text` | no | Identificador de la dirección territorial a la que pertenece el docente. |  |
| 4 | `tipoVinculacion` | `text` | no | Código del tipo de vinculación del docente: CARRERA1, CARRERA2, PERIODO_DE_PRUEBA, OCASIONAL, ESPECIAL, VISITANTE o CATEDRA; otros textos se guardan en mayúsculas. Por defecto, OCASIONAL. |  |
| 5 | `dedicacion` | `text` | no | Código de dedicación del docente: TC (tiempo completo), MT (medio tiempo) o HC (hora cátedra). Por defecto, TC. |  |
| 6 | `estado` | `text` | no | Estado del docente. |  |
| 7 | `createdAt` | `timestamp(3) without time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `updatedAt` | `timestamp(3) without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 9 | `escalafon` | `text` | sí | _Por documentar_ |  |
| 10 | `horasAsignables` | `integer` | no | Bolsa de horas del PTA del docente para el periodo. Se toma de la columna HORAS_PTA de la carga o se calcula por vinculación y dedicación: 720 para Carrera1, 800 para tiempo completo y 400 para medio tiempo, proporcional si la vinculación dura menos de 20 semanas. Por defecto, 0. |  |
| 11 | `sedeId` | `text` | sí | Identificador de la sede a la que está adscrito el docente. |  |
| 12 | `ordenListado` | `integer` | sí | Posición del docente en los listados, tomada de la columna ORDEN_LISTADO de la carga masiva; los listados ordenan por este valor de menor a mayor. |  |
| 13 | `vinculacionDisplay` | `text` | sí | Texto de la vinculación del docente para mostrar en pantalla. |  |
| 14 | `dedicacionDisplay` | `text` | sí | Texto de la dedicación del docente para mostrar en pantalla. |  |
| 15 | `nucleoTematico` | `text` | sí | _Por documentar_ |  |
| 16 | `nivelFormacion` | `text` | sí | _Por documentar_ |  |
| 17 | `perfilAcademicoPro` | `text` | sí | _Por documentar_ |  |
| 18 | `perfilAcademico` | `text` | sí | Áreas académicas o de docencia declaradas por el docente, en texto libre (hasta 1000 caracteres), tomadas de la carga masiva o de la hoja de vida PRO. |  |
| 19 | `pregrado` | `text` | sí | _Por documentar_ |  |
| 20 | `especializacion` | `text` | sí | Nombre del título de especialización del docente, en texto, tomado de la carga masiva (TITULO_ESPECIALIZACION) o del diploma o acta de grado; no guarda la institución. |  |
| 21 | `maestria` | `text` | sí | Nombre del título de maestría del docente, en texto, tomado de la carga masiva (TITULO_MAESTRIA) o del diploma o acta de grado; no guarda la institución. |  |
| 22 | `doctorado` | `text` | sí | Nombre del título de doctorado del docente, en texto, tomado de la carga masiva (TITULO_DOCTORADO) o del diploma o acta de grado; no guarda la institución. |  |
| 23 | `posDoctorado` | `text` | sí | Nombre del programa o estancia posdoctoral del docente, en texto, tomado de la carga masiva (TITULO_POSDOCTORADO) o del certificado posdoctoral. |  |
| 24 | `investigacion` | `text` | sí | Grupo, proyecto, línea o actividad de investigación del docente, en texto, tomado de la carga masiva (INVESTIGACION_ACTIVA) o de la certificación de investigación. |  |
| 25 | `origenVinculacion` | `text` | sí | _Por documentar_ |  |
| 26 | `actoAdministrativoVinculacion` | `text` | sí | Tipo, número y año del contrato, resolución o acto administrativo que vincula al docente, en texto; la fecha de inicio se guarda aparte en fechaInicioVinculacion. |  |
| 27 | `correoInstitucional` | `text` | sí | Correo electrónico institucional del docente. |  |
| 28 | `ultimaEvaluacion` | `text` | sí | Periodo o resultado de la última evaluación docente, en texto, tomado de la carga masiva (ULTIMA_EVALUACION) o del acta de evaluación de desempeño. |  |
| 29 | `situacionAdministrativa` | `text` | sí | Situación administrativa del docente, en texto libre (por ejemplo, servicio activo, comisión, licencia o el nombre del cargo directivo), tomada de la carga masiva o del acto administrativo de situación. Si indica retiro, el docente queda INACTIVO. |  |
| 30 | `fechaInicioVinculacion` | `timestamp(3) without time zone` | sí | Fecha de inicio de la vinculación del docente. |  |
| 31 | `fechaFinVinculacion` | `timestamp(3) without time zone` | sí | Fecha de finalización de la vinculación del docente. Vacía si la vinculación no tiene fecha de fin. |  |
| 32 | `puntajeSalarial` | `double precision` | sí | _Por documentar_ |  |
| 33 | `edadReferencia` | `integer` | sí | Edad del docente en años. Se calcula a partir de la fecha de nacimiento en la fecha de la carga o de la confirmación del dato; si no hay fecha, se toma la columna EDAD de la carga. | Dato personal |
| 34 | `rangoEdad` | `text` | sí | Rango de edad del docente: Menor de 35 años, De 36 a 45 años, De 46 a 55 años, De 56 a 65 años o Mayor de 65 años. Se calcula a partir de edadReferencia si la carga no lo trae. |  |
| 35 | `regimenNormativo` | `text` | sí | Régimen normativo de la vinculación del docente: Acuerdo 009/2004 (Carrera1), Acuerdo 003/2018 (Carrera2), Circular Dispositiva 003/2025 (periodo de prueba, ocasional, especial o visitante) o N/A; la columna REGIMEN_NORMATIVO de la carga lo reemplaza. |  |
| 36 | `periodoCarga` | `text` | sí | Periodo académico al que corresponde el registro del docente, tomado de la columna PERIODO_CARGA de la carga masiva; el mismo profesor tiene una fila por periodo. |  |
| 37 | `observaciones` | `text` | sí | Observaciones sobre el docente. |  |
| 38 | `idRund` | `text` | sí | Identificador del docente en el RUND. Se toma de la columna ID_RUND de la carga o, si no viene, el sistema lo genera con el formato RUND-0001 (secuencia docente_id_rund_seq). |  |
| 39 | `estadoAprobacion` | `text` | sí | Estado de aprobación global del registro del docente en el RUND: PENDIENTE_APROBACION (por defecto), ACTIVO_RUND o DEVUELTO. Pasa a activo solo cuando todos los bloques obligatorios están aprobados (BR-047). |  |
| 40 | `completitud` | `jsonb` | sí | Semáforo de completitud del perfil del docente por bloque, en formato JSON: a cada bloque (IDENTIDAD, FORMACION, VINCULACION, CONTACTO) le asigna un estado como Aprobado, Pendiente o Soporte faltante (BR-047). |  |
| 41 | `canal_origen` | `text` | sí | Canal por el que se creó el registro: MASIVO (por defecto), MODAL o AUTOGESTION. |  |
| 42 | `cetapId` | `text` | sí | Identificador opcional del CETAP asociado al docente. |  |
| 43 | `correoAlternativo` | `text` | sí | Correo personal o alternativo del docente para flujos RUND. | Contacto |
| 44 | `acepta_habeas_data` | `boolean` | sí | Indica si el docente aceptó el tratamiento de datos personales (habeas data). |  |
| 45 | `fecha_aceptacion_habeas_data` | `timestamp without time zone` | sí | Fecha y hora en que el docente aceptó el tratamiento de datos personales (habeas data). |  |
| 46 | `ip_creacion` | `character varying(50)` | sí | Dirección IP desde la que se creó el registro. | Identificador en línea (IP) |
| 47 | `sexoBiologico` | `text` | sí | _Por documentar_ | Dato personal |
| 48 | `dedicacionHorasSemana` | `integer` | sí | Número de horas semanales de dedicación del docente. |  |
| 49 | `situacionCategoria` | `text` | sí | Categoría de la situación administrativa del docente: Servicio Activo, Año Sabático, Dedicación Exclusiva, Comisión de Estudios, Comisión de Servicios, En Periodo de Prueba, Cargo Directivo u Otra. Se calcula a partir de situacionAdministrativa (texto libre) si la carga no la trae. |  |
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
| 3 | `nombre` | `text` | no | Nombre del documento. |  |
| 4 | `url` | `text` | no | Dirección web (URL) del documento. |  |
| 5 | `tipo` | `text` | no | Tipo de documento. |  |
| 6 | `createdAt` | `timestamp(3) without time zone` | no | Fecha y hora de creación del registro. |  |
| 7 | `categoria` | `text` | sí | _Por documentar_ |  |
| 8 | `comentarios` | `text` | sí | _Por documentar_ |  |
| 9 | `estado` | `text` | no | Estado del documento. |  |
| 10 | `tamanoBytes` | `integer` | no | Tamaño del archivo en bytes. |  |
| 11 | `tipoDocumentoId` | `text` | sí | Identificador del tipo de documento. |  |
| 12 | `updatedAt` | `timestamp(3) without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 13 | `versionActual` | `integer` | no | Número de la versión vigente del documento. Por defecto, 1. |  |
| 14 | `aprobadoPorId` | `text` | sí | Identificador del usuario que aprobó el documento. |  |
| 15 | `aprobadoPorNombre` | `text` | sí | Nombre del usuario que aprobó el documento. |  |

## RundAccesoDatosLog

Bitácora de accesos a los datos de docentes del RUND. Un registro por consulta, con el usuario y sus roles, el servicio consultado, el recurso, los docentes y campos consultados, el resultado del control de acceso (completo, enmascarado o denegado) y la IP de origen.

- Clave primaria: `id`
- Filas: 9141

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundAccesoDatosLog. | PK |
| 2 | `actor_id` | `text` | no | Identificador del usuario que accedió a los datos. |  |
| 3 | `roles` | `text[]` | no | Roles que tenía el usuario al momento del acceso (lista). |  |
| 4 | `endpoint` | `text` | no | Ruta del servicio (endpoint) consultado. |  |
| 5 | `recurso_id` | `text` | sí | Identificador del recurso consultado; depende del endpoint registrado: documento del perfil, sugerencia o trabajo de extracción, carga masiva, invitación, o hash SHA-256 de la ruta en los archivos estáticos. |  |
| 6 | `docentes` | `text[]` | no | Identificadores de los docentes cuyos datos se consultaron (lista). |  |
| 7 | `campos` | `text[]` | no | Nombres de los campos consultados (lista). |  |
| 8 | `resultado` | `text` | no | Resultado del control de acceso. Valores permitidos: COMPLETO, ENMASCARADO, DENEGADO. |  |
| 9 | `ip` | `text` | sí | Dirección IP desde la que se hizo el acceso a los datos del RUND. | Identificador en línea (IP) |
| 10 | `createdAt` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## RundAccesoExterno

Accesos temporales de entidades externas al Macro Docente (REQ-RUND-F022). Un registro por acceso otorgado, con la entidad, su contacto, el token, el docente que puede consultar, el motivo, la vigencia y quién lo otorgó o revocó; el acceso lo otorga GGP o la Dirección y las consultas hechas con él se registran en RundMacroDocenteConsultaLog.

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundAccesoExterno. Se genera automáticamente. | PK |
| 2 | `ente_nombre` | `text` | no | Nombre de la entidad externa a la que se otorga el acceso. |  |
| 3 | `ente_contacto` | `text` | sí | Correo de contacto de la entidad externa; a esta dirección se envía la notificación del acceso otorgado. |  |
| 4 | `token` | `text` | no | Token de acceso que se entrega a la entidad externa. No se repite. | única Credencial de acceso |
| 5 | `docente_id` | `text` | no | Identificador del único docente cuyos datos puede consultar la entidad externa con este acceso; si necesita ver varios docentes, se otorgan varios accesos (REQ-RUND-F022). |  |
| 6 | `motivo` | `text` | sí | Motivo por el que se otorga el acceso. |  |
| 7 | `fecha_inicio` | `timestamp with time zone` | no | Fecha y hora de inicio del acceso externo al RUND. |  |
| 8 | `fecha_fin` | `timestamp with time zone` | no | Fecha y hora de finalización del acceso externo al RUND. |  |
| 9 | `activo` | `boolean` | no | Indica si el acceso externo al RUND está activo. |  |
| 10 | `otorgado_por` | `text` | no | Identificador del usuario que otorgó el acceso. |  |
| 11 | `revoked_at` | `timestamp with time zone` | sí | Fecha y hora en que se revocó el acceso, con zona horaria. Vacía si sigue vigente. |  |
| 12 | `revoked_by` | `text` | sí | Identificador del usuario que revocó el acceso. |  |
| 13 | `createdAt` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## RundAprobacionLog

Log de auditoría inmutable del RUND (BR-056). Sólo INSERT: registra crear/aprobar/devolver/editar/vincular soporte.

- Clave primaria: `id`
- Filas: 6760

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundAprobacionLog. Se genera automáticamente. | PK |
| 2 | `docente_id` | `uuid` | no | Identificador del docente al que corresponde el evento. |  |
| 3 | `bloque` | `text` | sí | Bloque del perfil RUND afectado por el evento: IDENTIDAD, FORMACION, VINCULACION, CONTACTO o GENERAL. |  |
| 4 | `accion` | `text` | no | Acción registrada en la bitácora: CREAR, APROBAR, DEVOLVER, EDITAR, VINCULAR_SOPORTE, DESVINCULAR_SOPORTE o CONSULTAR_DATOS_SENSIBLES. |  |
| 5 | `actor_id` | `text` | no | Identificador del usuario que realizó la acción, o el valor SISTEMA cuando la acción es automática. |  |
| 6 | `canal_origen` | `text` | sí | Canal por el que se realizó la acción: MASIVO, MODAL o AUTOGESTION. |  |
| 7 | `campo_afectado` | `text` | sí | Nombre del campo específico afectado por la acción (por ejemplo, TITULO_PREGRADO o TIPO_VINCULACION). |  |
| 8 | `dato_previo` | `text` | sí | Valor del campo antes de la acción, usado para el reversionamiento (BR-046). |  |
| 9 | `dato_nuevo` | `text` | sí | Valor del campo después de la acción. |  |
| 10 | `observacion` | `text` | sí | Observación registrada con la acción; es obligatoria en las devoluciones (BR-045). |  |
| 11 | `soporte_id` | `text` | sí | Identificador del soporte documental vinculado o desvinculado en la acción, cuando aplica. |  |
| 12 | `ip` | `text` | sí | Dirección IP del cliente que realizó la acción, registrada para el canal de autogestión. | Identificador en línea (IP) |
| 13 | `metadata` | `jsonb` | sí | Metadatos adicionales de la acción en formato JSON (por ejemplo, habeasData o invitacionId). |  |
| 14 | `createdAt` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |

## RundCampoEstado

Estado de aprobación de los bloques de campos del perfil RUND (BR-044). Un registro por docente y bloque (IDENTIDAD, FORMACION, VINCULACION, CONTACTO), con quién lo cargó y revisó, la observación, la versión, el canal de origen y los soportes vinculados. Ciclo: Pendiente, En revisión, Aprobado, Devuelto o Soporte faltante.

- Clave primaria: `id`
- Filas: 6594

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundCampoEstado. Se genera automáticamente. | PK |
| 2 | `docente_id` | `character varying(255)` | no | Identificador del docente. |  |
| 3 | `bloque` | `character varying(50)` | no | Bloque de campos del perfil RUND al que corresponde el estado: IDENTIDAD (documento, nombre, fecha de nacimiento, género), FORMACION (niveles de formación), VINCULACION (tipo, régimen, categoría, dedicación, acto administrativo, puntaje salarial) o CONTACTO (correos y teléfono). |  |
| 4 | `estado` | `character varying(50)` | no | Estado de aprobación del bloque: Pendiente, En revisión, Aprobado, Devuelto o Soporte faltante (BR-044). |  |
| 5 | `cargado_por` | `character varying(255)` | sí | Usuario que cargó o editó los datos del bloque. |  |
| 6 | `revisado_por` | `character varying(255)` | sí | Usuario que revisó o aprobó el bloque; puede coincidir con cargado_por si tiene permisos de revisión. |  |
| 7 | `observacion` | `text` | sí | Observación sobre el bloque; es obligatoria al devolverlo (BR-045). |  |
| 8 | `version` | `integer` | no | Versión del bloque; se incrementa en cada cambio de dato aprobado (BR-046). |  |
| 9 | `canal_origen` | `character varying(50)` | sí | Canal de origen del último cambio del bloque: MASIVO, MODAL o AUTOGESTION. |  |
| 10 | `soporte_ids` | `jsonb` | no | Identificadores de los soportes vinculados al bloque, en formato JSON (lista), que referencian documentos de la Carpeta Digital (BR-038). |  |
| 11 | `fecha_revision` | `timestamp without time zone` | sí | Fecha de la última revisión o aprobación del bloque. |  |
| 12 | `createdAt` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 13 | `updatedAt` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## RundCargaMasiva

Soporte documental inmutable de cada importación masiva de perfiles RUND.

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundCargaMasiva. Se genera automáticamente. | PK |
| 2 | `nombre_archivo` | `text` | no | Nombre del archivo importado. |  |
| 3 | `tipo_mime` | `text` | no | Tipo MIME del archivo importado. |  |
| 4 | `tamano_bytes` | `bigint` | no | Tamaño en bytes del archivo de la carga masiva. |  |
| 5 | `sha256` | `character varying(64)` | no | Hash SHA-256 del archivo, en 64 caracteres hexadecimales. |  |
| 6 | `contenido` | `bytea` | no | Contenido binario del archivo importado. |  |
| 7 | `actor_id` | `text` | no | Identificador del usuario que realizó la importación. |  |
| 8 | `justificacion` | `text` | no | Justificación de la importación masiva. |  |
| 9 | `ip` | `text` | sí | Dirección IP desde la que se hizo la carga masiva. | Identificador en línea (IP) |
| 10 | `estado` | `text` | no | Estado de la carga masiva: procesando, completada, completada con errores o fallida. |  |
| 11 | `resumen` | `jsonb` | no | Resumen de la importación en JSON: total, created, updated, unchanged y errors (o error si falló), más trazabilidad con versión, periodos, registros (resultado por fila: CREADO, ACTUALIZADO, SIN_CAMBIOS, NO_CARGADO, NO_PROCESADO) y resumenPorPeriodo. |  |
| 12 | `createdAt` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 13 | `updatedAt` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## RundDocumentoCategoria

Catálogo de categorías de documento del RUND. Un registro por categoría, con su código, nombre, descripción, tipos MIME permitidos, tamaño máximo de archivo, orden y si está activa; lo referencian los documentos del perfil (RundDocumentoPerfil).

- Clave primaria: `codigo`
- Filas: 10

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `codigo` | `text` | no | Clave primaria de la tabla RundDocumentoCategoria: código. | PK |
| 2 | `nombre` | `text` | no | Nombre de la categoría de documento del RUND. |  |
| 3 | `descripcion` | `text` | sí | Descripción de la categoría de documento del RUND. |  |
| 4 | `mime_permitidos` | `text[]` | no | Tipos MIME permitidos para los documentos de la categoría (lista). Por defecto, application/pdf. |  |
| 5 | `tamano_maximo_bytes` | `bigint` | no | Tamaño máximo permitido del archivo, en bytes. Por defecto, 10485760 (10 MB). |  |
| 6 | `activo` | `boolean` | no | Indica si la categoría de documento está activa. |  |
| 7 | `orden` | `integer` | no | Posición de la categoría de documento en el orden de presentación. |  |
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
| 2 | `documento_logico_id` | `uuid` | no | Identificador común a todas las versiones de un mismo documento. Junto con version no se repite. |  |
| 3 | `docente_id` | `uuid` | no | Identificador del docente dueño del documento. |  |
| 4 | `categoria_codigo` | `text` | no | Referencia al registro de academic_work_plan.RundDocumentoCategoria (codigo). | FK→academic_work_plan.RundDocumentoCategoria.codigo |
| 5 | `bloque` | `text` | sí | Bloque del perfil RUND al que se asocia el documento: IDENTIDAD, CONTACTO, FORMACION, VINCULACION, ACADEMICO o TRANSVERSAL. |  |
| 6 | `tipo_soporte` | `text` | sí | Tipo de soporte que acredita el documento, de la lista definida por bloque en el código (por ejemplo, documento_identidad, diploma_pregrado, contrato, resolucion_escalafon, autorizacion_habeas_data). |  |
| 7 | `descripcion` | `text` | sí | Descripción del documento del perfil docente. |  |
| 8 | `version` | `integer` | no | Número de versión del documento del perfil docente. |  |
| 9 | `nombre_archivo` | `text` | no | Nombre original del archivo cargado. |  |
| 10 | `mime_type` | `text` | no | Tipo MIME del archivo del documento del perfil docente. |  |
| 11 | `tamano_bytes` | `bigint` | no | Tamaño en bytes del archivo del documento del perfil docente. |  |
| 12 | `checksum_sha256` | `text` | no | Hash SHA-256 del archivo. |  |
| 13 | `proveedor_almacenamiento` | `text` | no | Proveedor donde se almacena el archivo: OPENKM, LOCAL (almacenamiento local de desarrollo) o LEGACY_LOCAL (soportes históricos incorporados sin mover el archivo). |  |
| 14 | `almacenamiento_id` | `text` | sí | Identificador del archivo en el proveedor de almacenamiento. |  |
| 15 | `almacenamiento_ruta` | `text` | no | Ruta del archivo en el proveedor de almacenamiento. |  |
| 16 | `estado` | `text` | no | Estado del documento del perfil docente: activo, reemplazado o eliminado. |  |
| 17 | `reemplaza_id` | `uuid` | sí | Referencia al registro de academic_work_plan.RundDocumentoPerfil (id). | FK→academic_work_plan.RundDocumentoPerfil.id |
| 18 | `rund_soporte_id` | `uuid` | sí | Identificador del soporte en academic_work_plan."RundSoporteCampo" al que corresponde el documento. |  |
| 19 | `creado_por` | `text` | no | Usuario que creó el registro. |  |
| 20 | `eliminado_por` | `text` | sí | Usuario que realizó la eliminación. |  |
| 21 | `eliminado_en` | `timestamp without time zone` | sí | Fecha y hora de la eliminación. |  |
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

Sugerencias de valores extraídos de documentos del perfil RUND (REQ-RUND-F014). Un registro por campo sugerido en un trabajo de extracción, con el valor sugerido, el valor previo, la página y el fragmento de evidencia, la confianza y la decisión del revisor; se relaciona con RundExtraccionTrabajo. Ciclo: pendiente, aprobada, corregida o descartada.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `trabajo_id` → `academic_work_plan.RundExtraccionTrabajo` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundExtraccionSugerencia. Se genera automáticamente. | PK |
| 2 | `trabajo_id` | `uuid` | no | Referencia al registro de academic_work_plan.RundExtraccionTrabajo (id). | FK→academic_work_plan.RundExtraccionTrabajo.id |
| 3 | `campo` | `text` | no | Nombre del campo del perfil para el que se sugiere un valor (por ejemplo, documentNumber). |  |
| 4 | `valor` | `text` | no | Valor sugerido, extraído del documento. |  |
| 5 | `valor_previo` | `text` | sí | Valor que tenía el campo antes de la sugerencia. |  |
| 6 | `pagina` | `integer` | no | Número de la página del documento de donde se extrajo el valor. Debe ser mayor que cero. |  |
| 7 | `evidencia` | `text` | no | Fragmento literal continuo del texto OCR, de la misma página y de hasta 600 caracteres, que respalda el valor sugerido. |  |
| 8 | `confianza` | `numeric` | no | Nivel de confianza de la extracción, entre 0 y 1. |  |
| 9 | `baja_confianza` | `boolean` | no | Indica si la sugerencia extraída tiene baja confianza. |  |
| 10 | `estado` | `text` | no | Estado de la sugerencia de extracción: pendiente, aprobada, corregida o descartada. |  |
| 11 | `valor_confirmado` | `text` | sí | Valor confirmado por el revisor. |  |
| 12 | `revisado_por` | `text` | sí | Usuario que realizó la revisión. |  |
| 13 | `motivo` | `text` | sí | Motivo de la decisión del revisor sobre la sugerencia: obligatorio al descartar o corregir; al confirmar sin corrección, el sistema registra un texto estándar. |  |
| 14 | `revisado_en` | `timestamp with time zone` | sí | Fecha y hora de la revisión. |  |

## RundExtraccionTrabajo

Trabajos de extracción de datos de los documentos del perfil RUND. Un registro por documento procesado de un docente, con el estado, los intentos, la reserva del proceso que lo toma, el perfil base, el motor de procesamiento, el error y el aviso de fin; se relaciona con RundDocumentoPerfil y sus sugerencias están en RundExtraccionSugerencia. Ciclo: pendiente, procesando, completado, error u obsoleto.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `documento_id` → `academic_work_plan.RundDocumentoPerfil` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundExtraccionTrabajo. Se genera automáticamente. | PK |
| 2 | `documento_id` | `uuid` | no | Referencia al registro de academic_work_plan.RundDocumentoPerfil (id). | FK→academic_work_plan.RundDocumentoPerfil.id |
| 3 | `docente_id` | `uuid` | no | Identificador del docente cuyo documento RUND se procesa en este trabajo de extracción. Referencia a academic_work_plan."Docente". |  |
| 4 | `estado` | `text` | no | Estado del trabajo de extracción: pendiente, procesando, completado, error u obsoleto. |  |
| 5 | `intentos` | `integer` | no | Número de veces que un proceso tomó el trabajo de extracción; se incrementa en cada toma. Con 3 intentos fallidos el trabajo pasa a ERROR. |  |
| 6 | `disponible_en` | `timestamp with time zone` | no | _Por documentar_ |  |
| 7 | `lease_id` | `uuid` | sí | Identificador aleatorio de la reserva con la que un proceso toma el trabajo; lo asigna el servicio de extracción al reservarlo y se limpia al terminar, fallar o vencer la reserva. |  |
| 8 | `lease_hasta` | `timestamp with time zone` | sí | Fecha y hora en que vence la reserva del trabajo: 90 segundos, renovados cada 20 segundos mientras se procesa. Si vence, el trabajo vuelve a PENDIENTE (o a ERROR con 3 intentos) con código PROCESAMIENTO_INTERRUMPIDO. |  |
| 9 | `perfil_base` | `jsonb` | no | Valores del perfil del docente en los campos de extracción al momento del análisis, en JSON (campo: valor); sirven como valor previo de cada sugerencia. |  |
| 10 | `motor` | `jsonb` | no | Identificación del procesamiento en JSON: modelo de lenguaje local, motor OCR (por ejemplo, PaddleOCR), SHA-256 del PDF, número de páginas y versión del contrato de extracción. |  |
| 11 | `error_codigo` | `text` | sí | Código del error del último intento, si lo hubo, de una lista fija (por ejemplo, OCR_NO_DISPONIBLE, MODELO_TIMEOUT, PDF_INVALIDO, DOCUMENTO_MODIFICADO, PROCESAMIENTO_INTERRUMPIDO o EXTRACCION_NO_DISPONIBLE). Se borra al completar. |  |
| 12 | `creado_por` | `text` | no | Usuario que creó el registro. |  |
| 13 | `creado_en` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 14 | `actualizado_en` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 15 | `etapa` | `text` | no | _Por documentar_ |  |
| 16 | `etapa_desde` | `timestamp with time zone` | no | Fecha y hora en que el trabajo entró a su etapa actual. |  |
| 17 | `iniciado_en` | `timestamp with time zone` | sí | Fecha y hora del inicio. |  |
| 18 | `notificacion_id` | `uuid` | no | Clave de idempotencia del aviso de fin de la extracción que se envía al servicio de notificaciones; evita avisos duplicados. Se genera automáticamente. |  |
| 19 | `notificado_en` | `timestamp with time zone` | sí | Fecha y hora de la notificación. |  |
| 20 | `notificacion_proxima` | `timestamp with time zone` | no | Fecha y hora programada para el próximo intento de aviso de fin de la extracción a quien la solicitó o cargó el soporte; se reprograma un minuto después en cada intento y un día después si no se encuentra el usuario. |  |

## RundInvitacionDocente

_Por documentar._

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundInvitacionDocente. Se genera automáticamente. | PK |
| 2 | `correo_institucional` | `character varying(255)` | no | Correo electrónico institucional del docente al que se envía la invitación. |  |
| 3 | `documento_identidad` | `character varying(100)` | sí | Número del documento de identidad del docente invitado. | Identificación |
| 4 | `token_invitacion` | `character varying(255)` | no | Token único del enlace de invitación enviado al docente. | única Credencial de acceso |
| 5 | `otp_hash` | `character varying(255)` | sí | _Por documentar_ |  |
| 6 | `estado_invitacion` | `character varying(50)` | no | _Por documentar_ |  |
| 7 | `caducidad_token` | `timestamp without time zone` | no | Fecha y hora en que vence el token de invitación. |  |
| 8 | `intentos_otp` | `integer` | sí | _Por documentar_ |  |
| 9 | `bloqueo_hasta` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 10 | `fecha_envio` | `timestamp without time zone` | sí | Fecha y hora de envío de la invitación al docente. |  |
| 11 | `fecha_apertura` | `timestamp without time zone` | sí | Fecha y hora en que el docente abrió la invitación. |  |
| 12 | `ultima_actividad` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 13 | `docente_id` | `text` | sí | _Por documentar_ |  |
| 14 | `operador_id` | `character varying(255)` | sí | _Por documentar_ |  |
| 15 | `createdAt` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 16 | `updatedAt` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## RundMacroDocenteConsultaLog

Bitácora de consultas al Macro Docente (REQ-RUND-F020/F022). Un registro por consulta, con su tipo (macro docente, consulta puntual o externa), quién la hizo y con qué roles, los filtros, el docente y periodo consultados, el número de resultados y la IP; se relaciona con RundAccesoExterno cuando la consulta se hace con un acceso externo. Solo admite inserciones.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `acceso_externo_id` → `academic_work_plan.RundAccesoExterno` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundMacroDocenteConsultaLog. Se genera automáticamente. | PK |
| 2 | `tipo_consulta` | `text` | no | Tipo de consulta realizada sobre el Macro Docente: MACRO_DOCENTE, CONSULTA_PUNTUAL o EXTERNA. |  |
| 3 | `actor_id` | `text` | no | Identificador de quien realizó la consulta: el id de usuario del token (o, en su defecto, el correo o el nombre de usuario), SISTEMA, o ENTE_EXTERNO:<nombre del ente> en los accesos externos. |  |
| 4 | `roles` | `text[]` | sí | Roles que tenía el usuario al momento de la consulta, como lista de textos. |  |
| 5 | `acceso_externo_id` | `uuid` | sí | Referencia al registro de academic_work_plan.RundAccesoExterno (id). | FK→academic_work_plan.RundAccesoExterno.id |
| 6 | `docente_id` | `text` | sí | Identificador del docente consultado (academic_work_plan."Docente".id, el mismo de PlanTrabajoAcademico.docenteId), cuando la consulta se refiere a un docente específico. |  |
| 7 | `periodo` | `text` | sí | _Por documentar_ |  |
| 8 | `filtros` | `jsonb` | sí | Filtros aplicados en la consulta, en formato JSON. |  |
| 9 | `total_resultados` | `integer` | sí | Número de registros devueltos por la consulta. |  |
| 10 | `ip` | `text` | sí | Dirección IP desde la que se hizo la consulta del macro de docentes. | Identificador en línea (IP) |
| 11 | `createdAt` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## RundSoporteCampo

Soportes de los bloques de campos del perfil RUND (BR-038, BR-039, BR-041). Un registro por soporte de un docente y bloque, con el tipo de soporte, la referencia al documento en la Carpeta Digital o en RundDocumentoPerfil, el estado (Pendiente, Aprobado o Rechazado), la observación del revisor, la fecha de vencimiento y la revisión de cada campo.

- Clave primaria: `id`
- Filas: 12

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundSoporteCampo. Se genera automáticamente. | PK |
| 2 | `docente_id` | `uuid` | sí | Identificador del docente al que pertenece el soporte. |  |
| 3 | `bloque` | `text` | sí | Bloque de campos RUND al que aplica el soporte: IDENTIDAD, FORMACION, VINCULACION o CONTACTO. |  |
| 4 | `tipo_soporte` | `text` | sí | Tipo de soporte según el catálogo por bloque (BR-039): por ejemplo, documento_identidad (IDENTIDAD), diploma_pregrado o convalidacion_men (FORMACION) y acto_administrativo o contrato (VINCULACION). CONTACTO no requiere soporte. |  |
| 5 | `documento_carpeta_id` | `text` | sí | Referencia al documento en la Carpeta Digital, sin duplicar el archivo: puede ser el identificador del tipo_documento o el del archivo en la Carpeta Digital (BR-058). |  |
| 6 | `nombre_archivo` | `text` | sí | Nombre descriptivo del archivo del soporte, para mostrar. |  |
| 7 | `estado` | `character varying(50)` | no | Estado del soporte: Pendiente, Aprobado o Rechazado. |  |
| 8 | `cargado_por` | `character varying(255)` | sí | Usuario que cargó el soporte. |  |
| 9 | `observacion` | `text` | sí | Observación del revisor sobre el soporte, como el motivo de rechazo. |  |
| 10 | `fecha_vencimiento` | `timestamp without time zone` | sí | Fecha de vencimiento del soporte, solo para soportes con vigencia (certificaciones, evaluaciones); vacía si no caduca, como los diplomas (BR-055). |  |
| 11 | `createdAt` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 12 | `documento_perfil_id` | `uuid` | sí | Identificador del documento versionado del perfil en academic_work_plan."RundDocumentoPerfil" que respalda el soporte. |  |
| 13 | `revisiones_campos` | `jsonb` | no | Revisión individual de cada campo del soporte, en JSON: objeto cuya clave es el campo y cuyo valor tiene estado, observacion (solo si es Rechazado), documentoVersionId, revisadoPor y fechaRevision. Se vacía al reemplazar el soporte. |  |
