# Plan de trabajo académico (`academic_work_plan`)

Plan de trabajo académico (PTA) y registro de docentes (RUND): personas y docentes, programas, asignaturas, CETAP y periodos, planes de trabajo con sus revisiones y aprobaciones, y los datos, soportes y documentos del perfil RUND.

57 tablas · 0 vistas · 731 columnas · 39.324 filas · 6 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`AprobacionJefatura`](#aprobacionjefatura) | Tabla | 8 | Aprobaciones de las jefaturas territoriales sobre los planes de trabajo académico (PTA). Un registro por aprobación requerida de una jefatura territorial cuando el docente tiene asignaturas en varias territoriales, relacionado con academic_work_plan.PlanTrabajoAcademico; registra la decisión (pendiente, aprobado, aprobado con cambios o devuelto), el usuario y rol de la jefatura y sus comentarios. |
| [`AuditLog`](#auditlog) | Tabla | 2 | Registro de auditoría de las acciones de los usuarios en el plan de trabajo académico. Un registro por acción, con la fecha y hora, el usuario que la realizó, el módulo, la entidad afectada, el detalle, el resultado y la dirección IP de origen. |
| [`BancoDocentesInvitaciones`](#bancodocentesinvitaciones) | Tabla | 3 | Invitaciones de autogestión RUND (Canal 3): link público + OTP por correo. Estados: Enviada, Abierta, OTP validado, En proceso, Gestionada, Vencida. |
| [`CarpetaDigital`](#carpetadigital) | Tabla | 278 | Carpetas digitales de las personas del plan de trabajo académico. Un registro por carpeta de una persona (academic_work_plan.Persona), con su estado, el total de documentos, los documentos rechazados y la fecha de la última actualización. |
| [`Certificado`](#certificado) | Tabla | 0 | Certificados emitidos a personas en el plan de trabajo académico. Un registro por certificado, con la persona a la que se emite, el tipo, el estado, el código QR de verificación y la fecha de emisión. |
| [`Concertacion`](#concertacion) | Tabla | 0 | Mensajes de concertación de los planes de trabajo académico. Un registro por mensaje intercambiado sobre un plan (academic_work_plan.PlanTrabajoAcademico), con el autor, su rol, el texto y la fecha de creación. |
| [`ConfiguracionSistema`](#configuracionsistema) | Tabla | 3 | Parámetros de configuración del plan de trabajo académico. Un registro por parámetro, identificado por su clave, con su valor en formato JSON, la descripción y la fecha de la última actualización. |
| [`DetallesPta`](#detallespta) | Tabla | 0 | Detalle de las asignaturas de los planes de trabajo académico. Un registro por asignatura y grupo asignados en un plan (academic_work_plan.PlanTrabajoAcademico), con las horas, la modalidad, el número de estudiantes, la territorial y el CETAP donde se dicta, las fechas de inicio y fin y observaciones. |
| [`Docente`](#docente) | Tabla | 814 | Registro de docentes del RUND. Un registro por docente y periodo de carga, con su vinculación, dedicación, sede, territorial, formación, situación administrativa, bolsa de horas del PTA y estado de aprobación (PENDIENTE_APROBACION, ACTIVO_RUND o DEVUELTO); se relaciona con auth.personas. Se diligencia por carga masiva, registro individual o autogestión del docente. |
| [`Documento`](#documento) | Tabla | 2 | Documentos asociados a una persona del plan de trabajo académico. Un registro por documento, con su nombre, tipo, categoría, URL, tamaño, versión vigente, estado y el usuario que lo aprobó; se relaciona con academic_work_plan.Persona. |
| [`DocumentoVersion`](#documentoversion) | Tabla | 0 | Historial de versiones de los documentos del plan de trabajo académico. Un registro por versión de un documento (academic_work_plan.Documento), con el número de versión, la URL y el nombre del archivo, el tamaño, el usuario que la creó y comentarios. |
| [`HistorialEstadoPTA`](#historialestadopta) | Tabla | 51 | Historial de cambios de estado de los planes de trabajo académico (PTA). Un registro por transición de un plan (academic_work_plan.PlanTrabajoAcademico), con el estado anterior y el nuevo, quién la realizó y su rol, el tipo de acción, los comentarios, la versión del plan y una copia del plan en el momento de la transición. |
| [`PTAUserData`](#ptauserdata) | Tabla | 55 | Preferencias de los usuarios en el plan de trabajo académico. Un registro por usuario, con sus etiquetas, notas, planes fijados y orden de prioridad, guardados en formato JSON. |
| [`Permiso`](#permiso) | Tabla | 58 | Catálogo de permisos del plan de trabajo académico. Un registro por combinación de recurso y acción permitida, con su descripción; los permisos se asignan a los roles mediante academic_work_plan.RolPermiso. |
| [`Persona`](#persona) | Tabla | 283 | Datos personales y de vinculación de las personas del plan de trabajo académico. Un registro por persona, asociado a su usuario (academic_work_plan.Usuario), con identificación, nombres y apellidos, datos de contacto, tipo de usuario, dependencia, cargo y datos de contrato; se relaciona con su carpeta digital, sus documentos y sus programas. |
| [`PersonaPrograma`](#personaprograma) | Tabla | 267 | Vinculación de las personas con los programas académicos en el plan de trabajo académico. Un registro por persona (academic_work_plan.Persona) y programa, con el rol en el programa, el semestre actual y el estado de la vinculación. |
| [`PlanTrabajoAcademico`](#plantrabajoacademico) | Tabla | 8 | Planes de trabajo académico (PTA) de los docentes. Un registro por plan de un docente (academic_work_plan.Docente) en un periodo, con su estado, dedicación, tipo de vinculación, horas totales y asignables, contenido estructurado del formulario, versión, nivel y motivo de devolución y datos del cierre por periodo. Se relaciona con sus aprobaciones, revisiones, eventos, evidencias, detalles e historial de estados. |
| [`PtaComponentApproval`](#ptacomponentapproval) | Tabla | 99 | Aprobaciones por componente de los planes de trabajo académico (PTA). Un registro por componente de un plan (academic_work_plan.PlanTrabajoAcademico) y ámbito de aprobación, con su estado (pendiente, aprobado o devuelto), el usuario aprobador, su rol, comentarios, fecha de aprobación y la respuesta del docente al reenviar un componente devuelto. |
| [`PtaComponentReview`](#ptacomponentreview) | Tabla | 23 | Revisiones por componente de los planes de trabajo académico (PTA), etapa de preaprobación previa a la aprobación definitiva registrada en academic_work_plan.PtaComponentApproval. Un registro por componente y subsección revisados de un plan (academic_work_plan.PlanTrabajoAcademico), con su estado (pendiente, revisado o devuelto), el revisor, su rol, comentarios, la respuesta del docente y la fecha de revisión. |
| [`PtaEvento`](#ptaevento) | Tabla | 83 | Eventos de los planes de trabajo académico (PTA) para notificaciones y trazabilidad entre el portal y el backoffice. Un registro por evento de un plan (academic_work_plan.PlanTrabajoAcademico): cambio de estado, notificación, respuesta del docente, escalamiento, edición administrativa o guardado, con el actor, su rol, el sistema de origen, el mensaje y si fue leído en cada sistema. |
| [`PtaEvidencia`](#ptaevidencia) | Tabla | 2 | Evidencias de avance de los planes de trabajo académico (PTA). Un registro por archivo de evidencia cargado para un plan (academic_work_plan.PlanTrabajoAcademico), con el componente y la sección a la que corresponde, las horas que justifica, la ubicación del archivo, quién lo cargó y la revisión (pendiente, aprobado o rechazado) con su revisor, fecha y comentario. |
| [`PtaTerritorialApproval`](#ptaterritorialapproval) | Tabla | 3 | Aprobaciones territoriales de los planes de trabajo académico (PTA). Un registro por territorial, nivel de formación (pregrado o posgrado) y componente territorial de un plan (academic_work_plan.PlanTrabajoAcademico), con su estado (pendiente, aprobado o devuelto), el usuario que registra la decisión, su rol, comentarios, la fecha de decisión y, cuando aplica, la concertación de Programación Académica que la originó. |
| [`PtaTerritorialReview`](#ptaterritorialreview) | Tabla | 3 | Revisiones territoriales de los planes de trabajo académico (PTA). Un registro por territorial, nivel de formación (pregrado o posgrado) y componente territorial revisado de un plan (academic_work_plan.PlanTrabajoAcademico), con su estado (pendiente, revisado o devuelto), el revisor, su rol, comentarios y la fecha de revisión. |
| [`Rol`](#rol) | Tabla | 12 | Catálogo de roles del plan de trabajo académico. Un registro por rol, con su nombre, descripción, estado y si es un rol del sistema; se relaciona con los permisos (academic_work_plan.RolPermiso) y los usuarios (academic_work_plan.UsuarioRol). |
| [`RolPermiso`](#rolpermiso) | Tabla | 55 | Asignación de permisos a roles del plan de trabajo académico. Un registro por par de rol (academic_work_plan.Rol) y permiso (academic_work_plan.Permiso). |
| [`RundAccesoDatosLog`](#rundaccesodatoslog) | Tabla | 9141 | Bitácora de accesos a los datos de docentes del RUND. Un registro por consulta, con el usuario y sus roles, el servicio consultado, el recurso, los docentes y campos consultados, el resultado del control de acceso (completo, enmascarado o denegado) y la IP de origen. |
| [`RundAccesoExterno`](#rundaccesoexterno) | Tabla | 0 | Accesos temporales de entidades externas al Macro Docente (REQ-RUND-F022). Un registro por acceso otorgado, con la entidad, su contacto, el token, el docente que puede consultar, el motivo, la vigencia y quién lo otorgó o revocó; el acceso lo otorga GGP o la Dirección y las consultas hechas con él se registran en RundMacroDocenteConsultaLog. |
| [`RundAprobacionLog`](#rundaprobacionlog) | Tabla | 6760 | Log de auditoría inmutable del RUND (BR-056). Sólo INSERT: registra crear/aprobar/devolver/editar/vincular soporte. |
| [`RundCampoEstado`](#rundcampoestado) | Tabla | 6594 | Estado de aprobación de los bloques de campos del perfil RUND (BR-044). Un registro por docente y bloque (IDENTIDAD, FORMACION, VINCULACION, CONTACTO), con quién lo cargó y revisó, la observación, la versión, el canal de origen y los soportes vinculados. Ciclo: Pendiente, En revisión, Aprobado, Devuelto o Soporte faltante. |
| [`RundCargaMasiva`](#rundcargamasiva) | Tabla | 0 | Soporte documental inmutable de cada importación masiva de perfiles RUND. |
| [`RundDocumentoCategoria`](#runddocumentocategoria) | Tabla | 10 | Catálogo de categorías de documento del RUND. Un registro por categoría, con su código, nombre, descripción, tipos MIME permitidos, tamaño máximo de archivo, orden y si está activa; lo referencian los documentos del perfil (RundDocumentoPerfil). |
| [`RundDocumentoPerfil`](#runddocumentoperfil) | Tabla | 11 | REQ-RUND-F010: documentos PDF versionados del perfil docente, almacenados en OpenKM o proveedor local de desarrollo. |
| [`RundExtraccionInicio`](#rundextraccioninicio) | Tabla | 0 | Parámetro de inicio de la extracción de datos de documentos del RUND (REQ-RUND-F014). Guarda la fecha y hora desde la que aplica la extracción. |
| [`RundExtraccionSugerencia`](#rundextraccionsugerencia) | Tabla | 0 | Sugerencias de valores extraídos de documentos del perfil RUND (REQ-RUND-F014). Un registro por campo sugerido en un trabajo de extracción, con el valor sugerido, el valor previo, la página y el fragmento de evidencia, la confianza y la decisión del revisor; se relaciona con RundExtraccionTrabajo. Ciclo: pendiente, aprobada, corregida o descartada. |
| [`RundExtraccionTrabajo`](#rundextracciontrabajo) | Tabla | 0 | Trabajos de extracción de datos de los documentos del perfil RUND. Un registro por documento procesado de un docente, con el estado, los intentos, la reserva del proceso que lo toma, el perfil base, el motor de procesamiento, el error y el aviso de fin; se relaciona con RundDocumentoPerfil y sus sugerencias están en RundExtraccionSugerencia. Ciclo: pendiente, procesando, completado, error u obsoleto. |
| [`RundInvitacionDocente`](#rundinvitaciondocente) | Tabla | 0 | Invitaciones enviadas a docentes para ingresar al RUND con verificación por código de un solo uso (OTP). Un registro por invitación, con el correo institucional y el documento del docente, el token y su vencimiento, los intentos de OTP, el bloqueo y las fechas de envío, apertura y última actividad. |
| [`RundMacroDocenteConsultaLog`](#rundmacrodocenteconsultalog) | Tabla | 0 | Bitácora de consultas al Macro Docente (REQ-RUND-F020/F022). Un registro por consulta, con su tipo (macro docente, consulta puntual o externa), quién la hizo y con qué roles, los filtros, el docente y periodo consultados, el número de resultados y la IP; se relaciona con RundAccesoExterno cuando la consulta se hace con un acceso externo. Solo admite inserciones. |
| [`RundSoporteCampo`](#rundsoportecampo) | Tabla | 12 | Soportes de los bloques de campos del perfil RUND (BR-038, BR-039, BR-041). Un registro por soporte de un docente y bloque, con el tipo de soporte, la referencia al documento en la Carpeta Digital o en RundDocumentoPerfil, el estado (Pendiente, Aprobado o Rechazado), la observación del revisor, la fecha de vencimiento y la revisión de cada campo. |
| [`Sede`](#sede) | Tabla | 280 | Sedes territoriales del plan de trabajo académico. Un registro por sede, con su código, nombre, municipio y la territorial a la que pertenece (academic_work_plan.Territorial). |
| [`SistemaAlerta`](#sistemaalerta) | Tabla | 1 | Alertas del sistema en el plan de trabajo académico. Un registro por alerta, con su tipo, severidad, mensaje, la entidad que la origina y si está resuelta. |
| [`SolicitudPTA`](#solicitudpta) | Tabla | 13 | Solicitudes de los docentes sobre sus planes de trabajo académico (PTA): de creación y de edición de componentes. Un registro por solicitud de un docente (academic_work_plan.Docente), con el caso, la razón, la justificación, los documentos de soporte, los componentes solicitados, el estado y la resolución (quién la resolvió, fecha, motivo, acción y decisión por componente). |
| [`Territorial`](#territorial) | Tabla | 21 | Catálogo de territoriales del plan de trabajo académico. Un registro por territorial, con su código y nombre; agrupa las sedes de academic_work_plan.Sede. |
| [`Usuario`](#usuario) | Tabla | 283 | Usuarios del plan de trabajo académico. Un registro por usuario, con su correo, nombre y si está activo; se relaciona con sus datos personales (academic_work_plan.Persona) y sus roles (academic_work_plan.UsuarioRol). |
| [`UsuarioRol`](#usuariorol) | Tabla | 278 | Asignación de roles a usuarios del plan de trabajo académico. Un registro por par de usuario (academic_work_plan.Usuario) y rol (academic_work_plan.Rol). |
| [`asignatura`](#asignatura) | Tabla | 503 | Catálogo de asignaturas de los programas académicos. Un registro por asignatura, identificada por su código (llave del SNIES, RN-01), con su nombre, modalidad, tipo, créditos, horas de clase y del PTA, excepción de la Circular 003, pensum, ubicación semestral, programa, núcleo temático y facultad. Se carga desde una plantilla de importación y lo consulta la programación académica (academic-schedule). |
| [`cetap`](#cetap) | Tabla | 290 | Catálogo de CETAP y sedes de la ESAP. Un registro por ubicación (sede central, CETAP u otra), con su código, nombre, nombre normalizado, coordenadas geográficas y la dirección territorial a la que pertenece (academic_work_plan.direccion_territorial); se relaciona con la oferta de programas, los periodos y los alias del CETAP. |
| [`cetap_alias`](#cetap_alias) | Tabla | 0 | Nombres alternativos de los CETAP. Un registro por alias con el que se identifica un CETAP (academic_work_plan.cetap) en las fuentes de datos, con su forma normalizada para la comparación y el origen del alias. |
| [`direccion_territorial`](#direccion_territorial) | Tabla | 18 | Catálogo de direcciones territoriales de la ESAP. Un registro por dirección territorial, con su código, nombre, nombre normalizado, orden de visualización y si está activa; agrupa los CETAP (academic_work_plan.cetap) y las jefaturas territoriales de la programación académica. |
| [`docencia_concertada`](#docencia_concertada) | Tabla | 0 | Decisiones de concertación de la docencia recibidas de Programación Académica (EFDS-2315). Un registro por docente, periodo y nivel de formación, con las asignaturas y horas concertadas, las firmas, la huella de lo firmado y el estado de su aplicación al componente de Docencia del plan de trabajo académico (PTA). |
| [`facultad`](#facultad) | Tabla | 4 | Catálogo de facultades. Un registro por facultad, con su código, nombre y si está activa; se relaciona con los programas y las asignaturas. |
| [`nucleo_tematico`](#nucleo_tematico) | Tabla | 42 | Catálogo de núcleos temáticos de los programas académicos. Un registro por núcleo temático de un programa (academic_work_plan.programa), con su código, nombre, descripción y si está activo; agrupa asignaturas. |
| [`oferta_cetap_programa`](#oferta_cetap_programa) | Tabla | 337 | Oferta de programas académicos por CETAP y periodo. Un registro por programa (academic_work_plan.programa) ofrecido en un CETAP (academic_work_plan.cetap) en un periodo académico (academic_work_plan.periodo_academico), con los cupos estimados, observaciones y si está activa; se relaciona con los grupos de la programación académica. |
| [`periodo_academico`](#periodo_academico) | Tabla | 2 | Catálogo de periodos académicos. Un registro por periodo (año y semestre), con su código, fechas de inicio y fin y estado (planeación, concertación, en curso o cerrado); se relaciona con la oferta de programas, los CETAP por periodo y la programación académica. |
| [`periodo_cetap`](#periodo_cetap) | Tabla | 576 | Relación entre periodos académicos y CETAP. Un registro por CETAP (academic_work_plan.cetap) en un periodo académico (academic_work_plan.periodo_academico), con la indicación de si está activo en ese periodo. |
| [`programa`](#programa) | Tabla | 20 | Catálogo de programas académicos. Un registro por programa, con su código, nombre, facultad, nivel de formación, modalidad, periodo académico, factores de cálculo de horas y categoría de horas según la Circular 003; se relaciona con las asignaturas, los núcleos temáticos, la oferta por CETAP y la programación académica. Es la fuente del catálogo de programas que consulta la programación académica (RN-01/RN-02). |
| [`ubicacion_semestral`](#ubicacion_semestral) | Tabla | 16 | Catálogo de ubicaciones semestrales del plan de estudios. Un registro por semestre, con su código, etiqueta, tipo de programa (pregrado o posgrado) y orden de presentación del catálogo agrupado (AC-01); se relaciona con las asignaturas. |
| [`validacion_documental`](#validacion_documental) | Tabla | 12000 | Validación documental de los campos del RUND de los docentes. Un registro por docente (academic_work_plan.Docente) y campo del RUND, con el grupo de soporte documental, el documento de la carpeta digital que lo soporta, su estado de validación (aceptado, no aplica, pendiente, rechazado o sin cargar), las fechas de carga y validación, quién lo validó y la observación. |

## AprobacionJefatura

Aprobaciones de las jefaturas territoriales sobre los planes de trabajo académico (PTA). Un registro por aprobación requerida de una jefatura territorial cuando el docente tiene asignaturas en varias territoriales, relacionado con academic_work_plan.PlanTrabajoAcademico; registra la decisión (pendiente, aprobado, aprobado con cambios o devuelto), el usuario y rol de la jefatura y sus comentarios.

- Clave primaria: `id`
- Filas: 8
- Referencia a: `ptaId` → `academic_work_plan.PlanTrabajoAcademico` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla AprobacionJefatura. Se genera automáticamente. | PK |
| 2 | `ptaId` | `text` | no | Referencia al registro de academic_work_plan.PlanTrabajoAcademico (id). | FK→academic_work_plan.PlanTrabajoAcademico.id |
| 3 | `jefaturaUserId` | `text` | no | Identificador del usuario de la jefatura que registró la decisión (id_user de auth."user", tomado del token de sesión); cadena vacía mientras la aprobación está pendiente. |  |
| 4 | `jefaturaRol` | `text` | no | Rol de la jefatura que registra la decisión; por defecto, «Jefatura de Zona». |  |
| 5 | `territorialId` | `text` | no | Identificador de la dirección territorial (id_seccional de auth.seccionales, como texto) a la que corresponde la aprobación. |  |
| 6 | `territorialNombre` | `text` | sí | Nombre de la territorial a la que corresponde la aprobación. |  |
| 7 | `decision` | `text` | no | Decisión de la jefatura sobre el PTA (plan de trabajo académico). Valores previstos: pendiente, aprobado, aprobado_con_cambios, devuelto; por defecto pendiente. |  |
| 8 | `comentarios` | `text` | sí | Comentarios de la jefatura sobre su decisión. |  |
| 9 | `camposModificados` | `jsonb` | sí | Campos del plan de trabajo modificados por la jefatura, en formato JSON. |  |
| 10 | `componentesBloqueados` | `jsonb` | sí | Componentes del plan de trabajo bloqueados por la jefatura, en formato JSON. |  |
| 11 | `firmaId` | `text` | sí | Identificador de la firma asociada a la decisión de la jefatura. |  |
| 12 | `createdAt` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 13 | `updatedAt` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## AuditLog

Registro de auditoría de las acciones de los usuarios en el plan de trabajo académico. Un registro por acción, con la fecha y hora, el usuario que la realizó, el módulo, la entidad afectada, el detalle, el resultado y la dirección IP de origen.

- Clave primaria: `id`
- Filas: 2
- Relaciones implícitas: `usuario_id` ↝ `academic_work_plan.Usuario` (100.0 % con padre)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla AuditLog. Se genera automáticamente. | PK |
| 2 | `timestamp` | `timestamp(3) without time zone` | no | Fecha y hora del evento auditado; por defecto, la fecha y hora de registro. |  |
| 3 | `usuario_id` | `text` | sí | Identificador del usuario que realizó la acción. | ↝academic_work_plan.Usuario.id |
| 4 | `usuario_nombre` | `text` | sí | Nombre del usuario que realizó la acción. |  |
| 5 | `usuario_email` | `text` | sí | Correo electrónico del usuario que realizó la acción. | Contacto |
| 6 | `accion` | `text` | no | Acción realizada por el usuario. |  |
| 7 | `modulo` | `text` | no | Módulo del sistema en que se realizó la acción. |  |
| 8 | `entidad_tipo` | `text` | sí | Tipo de entidad afectada por la acción. |  |
| 9 | `entidad_id` | `text` | sí | Identificador del registro afectado por la acción. |  |
| 10 | `detalles` | `text` | no | Detalle de la acción realizada; vacío por defecto. |  |
| 11 | `resultado` | `text` | no | Resultado de la acción; por defecto, «EXITO». |  |
| 12 | `ip_address` | `text` | sí | Dirección IP desde la que se realizó la acción. | Identificador en línea (IP) |

## BancoDocentesInvitaciones

Invitaciones de autogestión RUND (Canal 3): link público + OTP por correo. Estados: Enviada, Abierta, OTP validado, En proceso, Gestionada, Vencida.

- Clave primaria: `id`
- Filas: 3

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla BancoDocentesInvitaciones. Se genera automáticamente. | PK |
| 2 | `correo_institucional` | `text` | no | Correo institucional al que se envía la invitación de autogestión RUND. |  |
| 3 | `token_acceso` | `text` | no | Token único del enlace público de la invitación. | única Credencial de acceso |
| 4 | `otp_codigo` | `text` | sí | Código OTP enviado por correo para validar el acceso a la invitación. |  |
| 5 | `otp_expira_en` | `timestamp without time zone` | sí | Fecha y hora en que vence el código OTP. |  |
| 6 | `intentos_otp` | `integer` | no | Número de intentos de validación del código OTP; inicia en 0. |  |
| 7 | `estado` | `text` | no | Estado de la invitación de autogestión RUND. Valores: Enviada, Abierta, OTP validado, En proceso, Gestionada, Vencida; por defecto Enviada. |  |
| 8 | `fecha_expiracion` | `timestamp without time zone` | no | Fecha y hora en que vence la invitación de autogestión RUND. |  |
| 9 | `borrador_json` | `jsonb` | sí | Borrador del formulario de autogestión que diligencia el docente invitado, como objeto JSON con los campos del formulario; no conserva el puntaje salarial. |  |
| 10 | `createdAt` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 11 | `updatedAt` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 12 | `sesion_token_hash` | `text` | sí | Hash SHA-256 (hexadecimal) del token de sesión que se entrega tras validar el OTP; la sesión dura dos horas. | Credencial de acceso |
| 13 | `sesion_expira_en` | `timestamp with time zone` | sí | Fecha y hora en que vence la sesión de la invitación. |  |

## CarpetaDigital

Carpetas digitales de las personas del plan de trabajo académico. Un registro por carpeta de una persona (academic_work_plan.Persona), con su estado, el total de documentos, los documentos rechazados y la fecha de la última actualización.

- Clave primaria: `id`
- Filas: 278
- Referencia a: `personaId` → `academic_work_plan.Persona` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla CarpetaDigital. Se genera automáticamente. | PK |
| 2 | `personaId` | `text` | no | Referencia al registro de academic_work_plan.Persona (id). | FK→academic_work_plan.Persona.id |
| 3 | `estado` | `text` | no | Estado de la carpeta digital. |  |
| 4 | `totalDocumentos` | `integer` | no | Número total de documentos de la carpeta digital; inicia en 0. |  |
| 5 | `documentosRechazados` | `integer` | no | Número de documentos rechazados de la carpeta digital; inicia en 0. |  |
| 6 | `ultimaActualizacion` | `timestamp(3) without time zone` | no | Fecha y hora de la última actualización de la carpeta digital. |  |
| 7 | `createdAt` | `timestamp(3) without time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `updatedAt` | `timestamp(3) without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## Certificado

Certificados emitidos a personas en el plan de trabajo académico. Un registro por certificado, con la persona a la que se emite, el tipo, el estado, el código QR de verificación y la fecha de emisión.

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla Certificado. Se genera automáticamente. | PK |
| 2 | `personaId` | `text` | no | Identificador de la persona a la que se emite el certificado. |  |
| 3 | `tipo` | `text` | no | Tipo de certificado. |  |
| 4 | `estado` | `text` | no | Estado del certificado. |  |
| 5 | `codigoQR` | `text` | sí | Código QR de verificación del certificado. |  |
| 6 | `fechaEmision` | `timestamp(3) without time zone` | sí | Fecha y hora de emisión del certificado. |  |
| 7 | `createdAt` | `timestamp(3) without time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `updatedAt` | `timestamp(3) without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## Concertacion

Mensajes de concertación de los planes de trabajo académico. Un registro por mensaje intercambiado sobre un plan (academic_work_plan.PlanTrabajoAcademico), con el autor, su rol, el texto y la fecha de creación.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `ptaId` → `academic_work_plan.PlanTrabajoAcademico` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla Concertacion. Se genera automáticamente. | PK |
| 2 | `ptaId` | `text` | no | Referencia al registro de academic_work_plan.PlanTrabajoAcademico (id). | FK→academic_work_plan.PlanTrabajoAcademico.id |
| 3 | `autorId` | `text` | no | Identificador del autor del mensaje de concertación del plan de trabajo académico. |  |
| 4 | `autorRol` | `text` | no | Rol del autor del mensaje de concertación. |  |
| 5 | `mensaje` | `text` | no | Texto del mensaje de concertación del plan de trabajo académico. |  |
| 6 | `createdAt` | `timestamp(3) without time zone` | no | Fecha y hora de creación del registro. |  |

## ConfiguracionSistema

Parámetros de configuración del plan de trabajo académico. Un registro por parámetro, identificado por su clave, con su valor en formato JSON, la descripción y la fecha de la última actualización.

- Clave primaria: `clave`
- Filas: 3

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `clave` | `text` | no | Clave primaria de la tabla ConfiguracionSistema: clave. | PK |
| 2 | `valor` | `jsonb` | no | Valor del parámetro de configuración identificado por la clave, en formato JSON. |  |
| 3 | `descripcion` | `text` | sí | Descripción del parámetro de configuración del sistema. |  |
| 4 | `updatedAt` | `timestamp(3) without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## DetallesPta

Detalle de las asignaturas de los planes de trabajo académico. Un registro por asignatura y grupo asignados en un plan (academic_work_plan.PlanTrabajoAcademico), con las horas, la modalidad, el número de estudiantes, la territorial y el CETAP donde se dicta, las fechas de inicio y fin y observaciones.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `ptaId` → `academic_work_plan.PlanTrabajoAcademico` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla DetallesPta. Se genera automáticamente. | PK |
| 2 | `ptaId` | `text` | no | Referencia al registro de academic_work_plan.PlanTrabajoAcademico (id). | FK→academic_work_plan.PlanTrabajoAcademico.id |
| 3 | `asignaturaId` | `text` | no | Identificador de la asignatura asignada en el plan de trabajo académico. |  |
| 4 | `grupo` | `text` | sí | Grupo de la asignatura. |  |
| 5 | `horas` | `integer` | no | Número de horas asignadas a la asignatura en el plan. |  |
| 6 | `modalidad` | `text` | no | Modalidad de la asignatura; por defecto, «PRESENCIAL». |  |
| 7 | `createdAt` | `timestamp(3) without time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `estudiantes` | `integer` | no | Número de estudiantes del grupo; por defecto, 25. |  |
| 9 | `territorialId` | `text` | sí | Identificador de la territorial donde se dicta la asignatura. |  |
| 10 | `cetapId` | `text` | sí | Identificador del CETAP donde se dicta la asignatura. |  |
| 11 | `fechaInicio` | `date` | sí | Fecha de inicio de la asignatura. |  |
| 12 | `fechaFin` | `date` | sí | Fecha de finalización de la asignatura. |  |
| 13 | `observaciones` | `text` | sí | Observaciones sobre el detalle del plan de trabajo académico. |  |

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
| 9 | `escalafon` | `text` | sí | Categoría o nivel del docente en el escalafón, en texto, tomada de la carga masiva (CATEGORIA_ESCALAFON) o de la resolución de escalafón. |  |
| 10 | `horasAsignables` | `integer` | no | Bolsa de horas del PTA del docente para el periodo. Se toma de la columna HORAS_PTA de la carga o se calcula por vinculación y dedicación: 720 para Carrera1, 800 para tiempo completo y 400 para medio tiempo, proporcional si la vinculación dura menos de 20 semanas. Por defecto, 0. |  |
| 11 | `sedeId` | `text` | sí | Identificador de la sede a la que está adscrito el docente. |  |
| 12 | `ordenListado` | `integer` | sí | Posición del docente en los listados, tomada de la columna ORDEN_LISTADO de la carga masiva; los listados ordenan por este valor de menor a mayor. |  |
| 13 | `vinculacionDisplay` | `text` | sí | Texto de la vinculación del docente para mostrar en pantalla. |  |
| 14 | `dedicacionDisplay` | `text` | sí | Texto de la dedicación del docente para mostrar en pantalla. |  |
| 15 | `nucleoTematico` | `text` | sí | Núcleo temático asignado al docente, en texto, tomado de la carga masiva o del acto de asignación de núcleo. |  |
| 16 | `nivelFormacion` | `text` | sí | Nivel de formación del docente, en texto, tomado de la columna NIVEL_FORMACION de la carga masiva; no se calcula a partir de los títulos. |  |
| 17 | `perfilAcademicoPro` | `text` | sí | Perfil académico PRO del docente, en texto, tomado de la columna «Perfil académico PRO» de la carga masiva. |  |
| 18 | `perfilAcademico` | `text` | sí | Áreas académicas o de docencia declaradas por el docente, en texto libre (hasta 1000 caracteres), tomadas de la carga masiva o de la hoja de vida PRO. |  |
| 19 | `pregrado` | `text` | sí | Nombre del título profesional de pregrado del docente, en texto, tomado de la carga masiva (TITULO_PREGRADO) o del diploma o acta de grado. |  |
| 20 | `especializacion` | `text` | sí | Nombre del título de especialización del docente, en texto, tomado de la carga masiva (TITULO_ESPECIALIZACION) o del diploma o acta de grado; no guarda la institución. |  |
| 21 | `maestria` | `text` | sí | Nombre del título de maestría del docente, en texto, tomado de la carga masiva (TITULO_MAESTRIA) o del diploma o acta de grado; no guarda la institución. |  |
| 22 | `doctorado` | `text` | sí | Nombre del título de doctorado del docente, en texto, tomado de la carga masiva (TITULO_DOCTORADO) o del diploma o acta de grado; no guarda la institución. |  |
| 23 | `posDoctorado` | `text` | sí | Nombre del programa o estancia posdoctoral del docente, en texto, tomado de la carga masiva (TITULO_POSDOCTORADO) o del certificado posdoctoral. |  |
| 24 | `investigacion` | `text` | sí | Grupo, proyecto, línea o actividad de investigación del docente, en texto, tomado de la carga masiva (INVESTIGACION_ACTIVA) o de la certificación de investigación. |  |
| 25 | `origenVinculacion` | `text` | sí | Fuente o modalidad de ingreso del docente, en texto, tomada de la carga masiva (ORIGEN_VINCULACION) o de la resolución de convocatoria. |  |
| 26 | `actoAdministrativoVinculacion` | `text` | sí | Tipo, número y año del contrato, resolución o acto administrativo que vincula al docente, en texto; la fecha de inicio se guarda aparte en fechaInicioVinculacion. |  |
| 27 | `correoInstitucional` | `text` | sí | Correo electrónico institucional del docente. |  |
| 28 | `ultimaEvaluacion` | `text` | sí | Periodo o resultado de la última evaluación docente, en texto, tomado de la carga masiva (ULTIMA_EVALUACION) o del acta de evaluación de desempeño. |  |
| 29 | `situacionAdministrativa` | `text` | sí | Situación administrativa del docente, en texto libre (por ejemplo, servicio activo, comisión, licencia o el nombre del cargo directivo), tomada de la carga masiva o del acto administrativo de situación. Si indica retiro, el docente queda INACTIVO. |  |
| 30 | `fechaInicioVinculacion` | `timestamp(3) without time zone` | sí | Fecha de inicio de la vinculación del docente. |  |
| 31 | `fechaFinVinculacion` | `timestamp(3) without time zone` | sí | Fecha de finalización de la vinculación del docente. Vacía si la vinculación no tiene fecha de fin. |  |
| 32 | `puntajeSalarial` | `double precision` | sí | Puntaje salarial del docente, numérico, tomado de la carga masiva (PUNTAJE_SALARIAL) o de la resolución de puntaje salarial. |  |
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
| 47 | `sexoBiologico` | `text` | sí | Sexo biológico del docente, en texto, tomado de la carga masiva (SEXO_BIOLOGICO) o del documento de identidad (Mujer u Hombre). | Dato personal |
| 48 | `dedicacionHorasSemana` | `integer` | sí | Número de horas semanales de dedicación del docente. |  |
| 49 | `situacionCategoria` | `text` | sí | Categoría de la situación administrativa del docente: Servicio Activo, Año Sabático, Dedicación Exclusiva, Comisión de Estudios, Comisión de Servicios, En Periodo de Prueba, Cargo Directivo u Otra. Se calcula a partir de situacionAdministrativa (texto libre) si la carga no la trae. |  |
| 50 | `territorialReportada` | `text` | sí | Nombre informativo reportado en RUND; no concede acceso ni asigna una territorial PTA. |  |
| 51 | `datosCargaMasiva` | `jsonb` | sí | Valores originales de las 38 columnas RUND de la última carga; protegidos por RBAC al consultar. |  |

## Documento

Documentos asociados a una persona del plan de trabajo académico. Un registro por documento, con su nombre, tipo, categoría, URL, tamaño, versión vigente, estado y el usuario que lo aprobó; se relaciona con academic_work_plan.Persona.

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
| 7 | `categoria` | `text` | sí | Categoría del documento. Por defecto, general. |  |
| 8 | `comentarios` | `text` | sí | Comentarios sobre el documento. |  |
| 9 | `estado` | `text` | no | Estado del documento. |  |
| 10 | `tamanoBytes` | `integer` | no | Tamaño del archivo en bytes. |  |
| 11 | `tipoDocumentoId` | `text` | sí | Identificador del tipo de documento. |  |
| 12 | `updatedAt` | `timestamp(3) without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 13 | `versionActual` | `integer` | no | Número de la versión vigente del documento. Por defecto, 1. |  |
| 14 | `aprobadoPorId` | `text` | sí | Identificador del usuario que aprobó el documento. |  |
| 15 | `aprobadoPorNombre` | `text` | sí | Nombre del usuario que aprobó el documento. |  |

## DocumentoVersion

Historial de versiones de los documentos del plan de trabajo académico. Un registro por versión de un documento (academic_work_plan.Documento), con el número de versión, la URL y el nombre del archivo, el tamaño, el usuario que la creó y comentarios.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `documentoId` → `academic_work_plan.Documento` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla DocumentoVersion. Se genera automáticamente. | PK |
| 2 | `documentoId` | `text` | no | Referencia al registro de academic_work_plan.Documento (id). | FK→academic_work_plan.Documento.id |
| 3 | `version` | `integer` | no | Número de la versión del documento. |  |
| 4 | `url` | `text` | no | Dirección web (URL) del archivo de la versión del documento. |  |
| 5 | `nombre` | `text` | no | Nombre del archivo de la versión del documento. |  |
| 6 | `tamanoBytes` | `integer` | no | Tamaño en bytes de la versión del documento; por defecto, 0. |  |
| 7 | `creadoPor` | `text` | sí | Identificador del usuario que creó la versión del documento. |  |
| 8 | `comentarios` | `text` | sí | Comentarios sobre la versión del documento. |  |
| 9 | `createdAt` | `timestamp(3) without time zone` | no | Fecha y hora de creación del registro. |  |

## HistorialEstadoPTA

Historial de cambios de estado de los planes de trabajo académico (PTA). Un registro por transición de un plan (academic_work_plan.PlanTrabajoAcademico), con el estado anterior y el nuevo, quién la realizó y su rol, el tipo de acción, los comentarios, la versión del plan y una copia del plan en el momento de la transición.

- Clave primaria: `id`
- Filas: 51
- Referencia a: `ptaId` → `academic_work_plan.PlanTrabajoAcademico` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla HistorialEstadoPTA. Se genera automáticamente. | PK |
| 2 | `ptaId` | `text` | no | Referencia al registro de academic_work_plan.PlanTrabajoAcademico (id). | FK→academic_work_plan.PlanTrabajoAcademico.id |
| 3 | `estadoAnterior` | `text` | sí | Estado del plan de trabajo académico antes de la transición. |  |
| 4 | `estadoNuevo` | `text` | no | Estado del plan de trabajo académico después de la transición. |  |
| 5 | `actorId` | `text` | sí | Identificador de quien realizó la transición de estado: el id_user de auth."user" del usuario autenticado o, en movimientos registrados en nombre del docente, el identificador del docente en la tabla Docente. |  |
| 6 | `actorRol` | `text` | sí | Rol del usuario que realizó la transición de estado. |  |
| 7 | `detallesTransicion` | `text` | sí | Detalle técnico de la transición: texto enviado por la aplicación o JSON serializado con los datos del movimiento (por ejemplo, solicitud, componentes, subsección y estado); los comentarios del actor van en comentarios. |  |
| 8 | `comentarios` | `text` | sí | Comentarios registrados en la transición de estado. |  |
| 9 | `createdAt` | `timestamp(3) without time zone` | no | Fecha y hora de creación del registro. |  |
| 10 | `version` | `integer` | sí | Número de versión del plan de trabajo académico registrado en el cambio de estado. |  |
| 11 | `camposModificados` | `jsonb` | sí | Campos del plan modificados en la transición, en formato JSON. |  |
| 12 | `tipoAccion` | `text` | sí | Clasificación de la acción para filtrado en la UI del historial. |  |
| 13 | `snapshotPta` | `jsonb` | sí | Copia del plan de trabajo académico en el momento de la transición, en formato JSON. |  |

## PTAUserData

Preferencias de los usuarios en el plan de trabajo académico. Un registro por usuario, con sus etiquetas, notas, planes fijados y orden de prioridad, guardados en formato JSON.

- Clave primaria: `id`
- Filas: 55

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla PTAUserData. Se genera automáticamente. | PK |
| 2 | `userId` | `text` | no | Identificador del usuario al que pertenecen las preferencias; valor único. | única |
| 3 | `tags` | `jsonb` | no | Etiquetas guardadas por el usuario, como objeto JSON (alias saved_tags). |  |
| 4 | `notes` | `jsonb` | no | Notas del usuario, como objeto JSON. |  |
| 5 | `pinned` | `jsonb` | no | Lista JSON de identificadores de planes de trabajo académico fijados por el usuario (alias pinned_pta_ids). |  |
| 6 | `priority` | `jsonb` | no | Lista JSON ordenada de elementos priorizados por el usuario (alias priorityOrder y favorite_views). |  |
| 7 | `createdAt` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `updatedAt` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## Permiso

Catálogo de permisos del plan de trabajo académico. Un registro por combinación de recurso y acción permitida, con su descripción; los permisos se asignan a los roles mediante academic_work_plan.RolPermiso.

- Clave primaria: `id`
- Filas: 58

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla Permiso. Se genera automáticamente. | PK |
| 2 | `recurso` | `text` | no | Recurso del sistema al que aplica el permiso; junto con accion es único. |  |
| 3 | `accion` | `text` | no | Acción permitida sobre el recurso; junto con recurso es única. |  |
| 4 | `descripcion` | `text` | sí | Descripción del permiso. |  |
| 5 | `createdAt` | `timestamp(3) without time zone` | no | Fecha y hora de creación del registro. |  |

## Persona

Datos personales y de vinculación de las personas del plan de trabajo académico. Un registro por persona, asociado a su usuario (academic_work_plan.Usuario), con identificación, nombres y apellidos, datos de contacto, tipo de usuario, dependencia, cargo y datos de contrato; se relaciona con su carpeta digital, sus documentos y sus programas.

- Clave primaria: `id`
- Filas: 283
- Referencia a: `usuarioId` → `academic_work_plan.Usuario` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla Persona. Se genera automáticamente. | PK |
| 2 | `usuarioId` | `text` | no | Referencia al registro de academic_work_plan.Usuario (id). | FK→academic_work_plan.Usuario.id |
| 3 | `identificacion` | `text` | sí | Número de identificación de la persona. |  |
| 4 | `tipo_identificacion` | `text` | sí | Tipo de documento de identidad de la persona. |  |
| 5 | `telefono` | `text` | sí | Número de teléfono de la persona. | Contacto |
| 6 | `direccion` | `text` | sí | Dirección de la persona. | Contacto |
| 7 | `createdAt` | `timestamp(3) without time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `updatedAt` | `timestamp(3) without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 9 | `primer_nombre` | `text` | sí | Primer nombre de la persona. | Nombre de persona |
| 10 | `segundo_nombre` | `text` | sí | Segundo nombre de la persona. | Nombre de persona |
| 11 | `primer_apellido` | `text` | sí | Primer apellido de la persona. | Nombre de persona |
| 12 | `segundo_apellido` | `text` | sí | Segundo apellido de la persona. | Nombre de persona |
| 13 | `genero` | `text` | sí | Género de la persona. | Dato personal |
| 14 | `fecha_nacimiento` | `timestamp(3) without time zone` | sí | Fecha de nacimiento de la persona. | Dato personal |
| 15 | `extension_telefonica` | `text` | sí | Extensión telefónica institucional de la persona. |  |
| 16 | `correo_alternativo` | `text` | sí | Correo electrónico alternativo de la persona. | Contacto |
| 17 | `tipo_usuario` | `text` | sí | Tipo de usuario de la persona en el sistema. |  |
| 18 | `empresa_contratista` | `text` | sí | Empresa contratista a la que pertenece la persona. |  |
| 19 | `dependencia_grupo_programa` | `text` | sí | Dependencia, grupo o programa al que está adscrita la persona. |  |
| 20 | `ubicacion_fisica` | `text` | sí | Ubicación física de trabajo de la persona. |  |
| 21 | `cargo_semestre` | `text` | sí | Cargo de la persona o semestre que cursa, según su tipo de usuario. |  |
| 22 | `nombre_jefe_dependencia` | `text` | sí | Nombre del jefe de la dependencia de la persona. |  |
| 23 | `contrato` | `text` | sí | Número o identificación del contrato de la persona. |  |
| 24 | `tiempo_contrato_resolucion` | `text` | sí | Duración del contrato o resolución de vinculación de la persona. |  |
| 25 | `fecha_fin_contrato` | `timestamp(3) without time zone` | sí | Fecha de finalización del contrato de la persona. |  |
| 26 | `aplicacion` | `text` | sí | Aplicación desde la que se registró la persona. |  |
| 27 | `observaciones` | `text` | sí | Observaciones sobre la persona. |  |

## PersonaPrograma

Vinculación de las personas con los programas académicos en el plan de trabajo académico. Un registro por persona (academic_work_plan.Persona) y programa, con el rol en el programa, el semestre actual y el estado de la vinculación.

- Clave primaria: `id`
- Filas: 267
- Referencia a: `personaId` → `academic_work_plan.Persona` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla PersonaPrograma. Se genera automáticamente. | PK |
| 2 | `personaId` | `text` | no | Referencia al registro de academic_work_plan.Persona (id). | FK→academic_work_plan.Persona.id |
| 3 | `programaId` | `text` | no | Identificador del programa académico al que está vinculada la persona. |  |
| 4 | `rolEnPrograma` | `text` | no | Rol de la persona en el programa; por defecto, «Estudiante». |  |
| 5 | `semestreActual` | `text` | sí | Semestre que cursa actualmente la persona en el programa. |  |
| 6 | `estado` | `text` | no | Estado de la vinculación de la persona al programa. |  |
| 7 | `createdAt` | `timestamp(3) without time zone` | no | Fecha y hora de creación del registro. |  |

## PlanTrabajoAcademico

Planes de trabajo académico (PTA) de los docentes. Un registro por plan de un docente (academic_work_plan.Docente) en un periodo, con su estado, dedicación, tipo de vinculación, horas totales y asignables, contenido estructurado del formulario, versión, nivel y motivo de devolución y datos del cierre por periodo. Se relaciona con sus aprobaciones, revisiones, eventos, evidencias, detalles e historial de estados.

- Clave primaria: `id`
- Filas: 8
- Referencia a: `docenteId` → `academic_work_plan.Docente` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla PlanTrabajoAcademico. Se genera automáticamente. | PK |
| 2 | `docenteId` | `text` | no | Referencia al registro de academic_work_plan.Docente (id). | FK→academic_work_plan.Docente.id |
| 3 | `periodo` | `text` | no | Periodo académico del plan de trabajo, con el código del periodo académico en formato año-semestre (por ejemplo, 2026-1). |  |
| 4 | `estado` | `text` | no | Estado del plan de trabajo académico. |  |
| 5 | `horasTotales` | `integer` | no | Número total de horas programadas en el plan (suma de docencia, investigación, extensión y complementarias), calculado por el sistema al guardar; por defecto, 0. |  |
| 6 | `observaciones` | `text` | sí | Observaciones sobre el plan de trabajo académico. |  |
| 7 | `createdAt` | `timestamp(3) without time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `updatedAt` | `timestamp(3) without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 9 | `datosEstructurados` | `jsonb` | sí | Contenido completo del plan de trabajo académico en formato JSON, tal como se registra en el formulario (asignaturas, actividades de investigación, extensión y complementarias, horas a programar, entre otros), con campos de control añadidos por el sistema. |  |
| 10 | `dedicacion` | `text` | sí | Dedicación del docente registrada en el plan, tomada del formulario del plan o de la vinculación del docente. |  |
| 11 | `horasAsignables` | `integer` | sí | Número de horas del periodo que se pueden programar al docente en el plan: se toman de las horas asignables del Banco de Docentes, prorrateadas por semanas sobre 16; si no existen, se calculan según el tipo de vinculación y la dedicación. |  |
| 12 | `semanasVinculacion` | `integer` | sí | Número de semanas de vinculación del docente en el periodo. |  |
| 13 | `tipoVinculacion` | `text` | sí | Tipo de vinculación del docente registrado en el plan, tomado del formulario. |  |
| 14 | `version` | `integer` | no | Versión lógica del PTA. Inicia en 1. Incrementa cada vez que el docente re-envía el PTA tras una devolución. |  |
| 15 | `nivelDevolucion` | `integer` | sí | Nivel al que regresa el PTA cuando el docente lo re-envíe tras una revisión. 1=Jefatura, 2=Decanatura, 3=G.Profesoral. |  |
| 16 | `camposModificadosPorRevisor` | `jsonb` | sí | Mapa de campos que el revisor modificó en la última iteración. Usado para highlighting visual en el portal del docente. Se limpia al iniciar la siguiente fase. |  |
| 17 | `snapshotAntesRevision` | `jsonb` | sí | Copia de datosEstructurados justo antes de que el revisor lo modificara. Permite comparación visual. |  |
| 18 | `motivoDevolucion` | `text` | sí | Motivo de la devolución del plan de trabajo al docente. |  |
| 19 | `ultimoActorRol` | `text` | sí | Rol del último usuario que actuó sobre el plan de trabajo. |  |
| 20 | `estadoAntesCierrePeriodo` | `text` | sí | Estado funcional del PTA antes del cierre reversible causado por cambio de periodo. |  |
| 21 | `cerradoPorPeriodo` | `text` | sí | Código del periodo cuya activación puso temporalmente el PTA en Terminado. |  |

## PtaComponentApproval

Aprobaciones por componente de los planes de trabajo académico (PTA). Un registro por componente de un plan (academic_work_plan.PlanTrabajoAcademico) y ámbito de aprobación, con su estado (pendiente, aprobado o devuelto), el usuario aprobador, su rol, comentarios, fecha de aprobación y la respuesta del docente al reenviar un componente devuelto.

- Clave primaria: `id`
- Filas: 99
- Referencia a: `pta_id` → `academic_work_plan.PlanTrabajoAcademico` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla PtaComponentApproval. Se genera automáticamente. | PK |
| 2 | `pta_id` | `text` | no | Referencia al registro de academic_work_plan.PlanTrabajoAcademico (id). | FK→academic_work_plan.PlanTrabajoAcademico.id |
| 3 | `componente` | `character varying(100)` | no | Componente del PTA que se aprueba. Valores previstos: academica, investigacion, ext_capacitacion, ext_procesos, ext_fortalecimiento, ext_gobierno, ext_secciones, complementarias, academicas_admin. |  |
| 4 | `estado` | `character varying(50)` | no | Estado de aprobación del componente. Valores previstos: pendiente, aprobado, devuelto; por defecto pendiente. |  |
| 5 | `aprobador_id` | `character varying(100)` | sí | Identificador del usuario que aprueba el componente del plan: id_user de auth."user", tomado del token de sesión; nulo en las aprobaciones registradas por la concertación de Programación Académica. |  |
| 6 | `aprobador_nombre` | `character varying(200)` | sí | Nombre del usuario que aprueba el componente del plan. |  |
| 7 | `aprobador_rol` | `character varying(100)` | sí | Rol del usuario que aprueba el componente del plan. |  |
| 8 | `comentarios` | `text` | sí | Comentarios del aprobador sobre el componente. |  |
| 9 | `fecha_aprobacion` | `timestamp without time zone` | sí | Fecha y hora de aprobación del componente del plan de trabajo académico. |  |
| 10 | `scope` | `character varying(50)` | sí | Ámbito de la aprobación del componente. Valores previstos: cetap, territorial, nacional. |  |
| 11 | `scope_id` | `character varying(100)` | sí | Identificador del ámbito de la aprobación según scope: número de nivel (1 a 3) cuando scope es nivel_aprobacion, identificador de la solicitud de edición (SolicitudPTA) cuando es solicitud_edicion e identificador de la concertación cuando es programacion. |  |
| 12 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 13 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 14 | `respuesta_docente` | `text` | sí | Respuesta del docente al reenviar un componente devuelto: por qué lo reenvía / qué corrigió. |  |

## PtaComponentReview

Revisiones por componente de los planes de trabajo académico (PTA), etapa de preaprobación previa a la aprobación definitiva registrada en academic_work_plan.PtaComponentApproval. Un registro por componente y subsección revisados de un plan (academic_work_plan.PlanTrabajoAcademico), con su estado (pendiente, revisado o devuelto), el revisor, su rol, comentarios, la respuesta del docente y la fecha de revisión.

- Clave primaria: `id`
- Filas: 23
- Referencia a: `pta_id` → `academic_work_plan.PlanTrabajoAcademico` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla PtaComponentReview. Se genera automáticamente. | PK |
| 2 | `pta_id` | `text` | no | Referencia al registro de academic_work_plan.PlanTrabajoAcademico (id). | FK→academic_work_plan.PlanTrabajoAcademico.id |
| 3 | `componente` | `character varying(100)` | no | Componente del PTA revisado; usa las mismas claves que PtaComponentApproval.componente. |  |
| 4 | `subseccion` | `character varying(50)` | no | Subsección del componente revisado: general para los componentes de revisión única (investigacion, ext_*); pregrado o posgrado para academica; docencia o academico_administrativas para complementarias. Por defecto general. |  |
| 5 | `estado` | `character varying(50)` | no | Estado de la revisión del componente. Valores previstos: pendiente, revisado, devuelto; por defecto pendiente. |  |
| 6 | `revisor_id` | `character varying(100)` | sí | Identificador del usuario que revisa el componente del plan: id_user de auth."user", tomado del token de sesión. |  |
| 7 | `revisor_nombre` | `character varying(200)` | sí | Nombre del usuario que revisa el componente del plan. |  |
| 8 | `revisor_rol` | `character varying(100)` | sí | Rol del usuario que revisa el componente del plan. |  |
| 9 | `comentarios` | `text` | sí | Comentarios del revisor sobre el componente. |  |
| 10 | `respuesta_docente` | `text` | sí | Respuesta del docente al reenviar el componente tras una devolución en la etapa de revisión. |  |
| 11 | `fecha_revision` | `timestamp without time zone` | sí | Fecha y hora de revisión del componente del plan de trabajo académico. |  |
| 12 | `scope` | `character varying(50)` | sí | Ámbito de la revisión; toma el valor solicitud_edicion cuando se reabre un componente ya aprobado. |  |
| 13 | `scope_id` | `character varying(100)` | sí | Identificador del ámbito de la revisión según scope. |  |
| 14 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 15 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## PtaEvento

Eventos de los planes de trabajo académico (PTA) para notificaciones y trazabilidad entre el portal y el backoffice. Un registro por evento de un plan (academic_work_plan.PlanTrabajoAcademico): cambio de estado, notificación, respuesta del docente, escalamiento, edición administrativa o guardado, con el actor, su rol, el sistema de origen, el mensaje y si fue leído en cada sistema.

- Clave primaria: `id`
- Filas: 83
- Referencia a: `ptaId` → `academic_work_plan.PlanTrabajoAcademico` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla PtaEvento. Se genera automáticamente. | PK |
| 2 | `ptaId` | `text` | no | Referencia al registro de academic_work_plan.PlanTrabajoAcademico (id). | FK→academic_work_plan.PlanTrabajoAcademico.id |
| 3 | `docenteId` | `text` | sí | Identificador del docente titular del plan de trabajo. |  |
| 4 | `docenteNombre` | `text` | sí | Nombre del docente titular del plan de trabajo. |  |
| 5 | `tipo` | `text` | no | Tipo de evento del PTA. Valores previstos: cambio_estado, notificacion, respuesta_docente, escalamiento, edicion_admin, guardado. |  |
| 6 | `estadoAnterior` | `text` | sí | Estado del plan antes del evento. |  |
| 7 | `estadoNuevo` | `text` | sí | Estado del plan después del evento. |  |
| 8 | `actor` | `text` | sí | Identificador de quien generó el evento: el identificador del docente en acciones del portal, el id_user del usuario autenticado en acciones del backoffice o «sistema» en procesos automáticos. |  |
| 9 | `actorRol` | `text` | sí | Rol del usuario que generó el evento. |  |
| 10 | `sistemaOrigen` | `text` | no | Sistema donde se originó el evento. Valores previstos: backoffice, portal, sistema; por defecto sistema. |  |
| 11 | `mensaje` | `text` | sí | Mensaje descriptivo del evento (por ejemplo, la transición de estado o la decisión sobre un componente); se entrega en la consulta de eventos recientes, que lleva marcas de lectura separadas para el backoffice y el portal. |  |
| 12 | `leidoBackoffice` | `boolean` | no | Indica si el evento del plan de trabajo académico fue leído en el backoffice. |  |
| 13 | `leidoPortal` | `boolean` | no | Indica si el evento del plan de trabajo académico fue leído en el portal. |  |
| 14 | `metadata` | `jsonb` | sí | Metadatos adicionales del evento del plan de trabajo académico, en formato JSON. |  |
| 15 | `createdAt` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |

## PtaEvidencia

Evidencias de avance de los planes de trabajo académico (PTA). Un registro por archivo de evidencia cargado para un plan (academic_work_plan.PlanTrabajoAcademico), con el componente y la sección a la que corresponde, las horas que justifica, la ubicación del archivo, quién lo cargó y la revisión (pendiente, aprobado o rechazado) con su revisor, fecha y comentario.

- Clave primaria: `id`
- Filas: 2
- Referencia a: `ptaId` → `academic_work_plan.PlanTrabajoAcademico` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla PtaEvidencia. Se genera automáticamente. | PK |
| 2 | `ptaId` | `text` | no | Referencia al registro de academic_work_plan.PlanTrabajoAcademico (id). | FK→academic_work_plan.PlanTrabajoAcademico.id |
| 3 | `nombre` | `text` | no | Nombre de la evidencia del plan de trabajo académico. |  |
| 4 | `tipoArchivo` | `text` | no | Tipo de archivo de la evidencia; por defecto, «pdf». |  |
| 5 | `tamanioBytes` | `integer` | no | Tamaño en bytes del archivo de evidencia; por defecto, 0. |  |
| 6 | `categoria` | `text` | sí | Categoría de la evidencia; para la resolución del proyecto de investigación se asigna una categoría propia del sistema. |  |
| 7 | `componentePta` | `text` | sí | Componente del plan de trabajo al que corresponde la evidencia. |  |
| 8 | `horasAvance` | `integer` | no | Número de horas que justifica la evidencia; por defecto, 0. No puede superar las horas del componente y solo las evidencias aprobadas y no eliminadas suman al cumplimiento del componente. |  |
| 9 | `storagePath` | `text` | sí | Ruta del archivo de evidencia en el almacenamiento. |  |
| 10 | `storageUrl` | `text` | sí | URL de acceso al archivo de evidencia. |  |
| 11 | `subidoPor` | `text` | sí | Persona que cargó la evidencia, según el valor que envía la aplicación; en la resolución de investigación, nombre del docente. |  |
| 12 | `descripcion` | `text` | sí | Descripción de la evidencia del plan de trabajo académico. |  |
| 13 | `estado` | `text` | no | Estado de la evidencia del plan de trabajo académico. |  |
| 14 | `estadoRevision` | `text` | no | Estado de la revisión de la evidencia: pendiente (por defecto), aprobado o rechazado. La columna estado indica si la evidencia está activa (por defecto, «activo») o eliminada. |  |
| 15 | `revisadoPor` | `text` | sí | Nombre del usuario que revisó la evidencia, tomado de la sesión (o su correo o id_user si falta el nombre); «Sistema» en la resolución de investigación aprobada automáticamente. |  |
| 16 | `fechaRevision` | `timestamp with time zone` | sí | Fecha y hora de revisión de la evidencia. |  |
| 17 | `comentarioRevision` | `text` | sí | Comentario del revisor sobre la evidencia. |  |
| 18 | `createdAt` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 19 | `updatedAt` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 20 | `seccionExtension` | `text` | sí | Sección de extensión de la evidencia, solo cuando componentePta es extension. Valores previstos: capacitacion, seleccion, fortalecimiento, alto_gobierno; nulo en los demás casos. |  |

## PtaTerritorialApproval

Aprobaciones territoriales de los planes de trabajo académico (PTA). Un registro por territorial, nivel de formación (pregrado o posgrado) y componente territorial de un plan (academic_work_plan.PlanTrabajoAcademico), con su estado (pendiente, aprobado o devuelto), el usuario que registra la decisión, su rol, comentarios, la fecha de decisión y, cuando aplica, la concertación de Programación Académica que la originó.

- Clave primaria: `id`
- Filas: 3
- Referencia a: `pta_id` → `academic_work_plan.PlanTrabajoAcademico` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla PtaTerritorialApproval. Se genera automáticamente. | PK |
| 2 | `pta_id` | `text` | no | Referencia al registro de academic_work_plan.PlanTrabajoAcademico (id). | FK→academic_work_plan.PlanTrabajoAcademico.id |
| 3 | `territorial_id` | `text` | no | Identificador de la dirección territorial (id_seccional de auth.seccionales, como texto) a la que corresponde la aprobación. |  |
| 4 | `territorial_nombre` | `text` | sí | Nombre de la territorial que emite la aprobación. |  |
| 5 | `estado` | `character varying(50)` | no | Estado de la aprobación territorial del PTA. Valores previstos: pendiente, aprobado, devuelto; por defecto pendiente. |  |
| 6 | `actor_id` | `character varying(100)` | sí | Identificador del usuario que registró la decisión territorial: id_user de auth."user", tomado del token de sesión; nulo en las aprobaciones registradas por la concertación de Programación Académica. |  |
| 7 | `actor_nombre` | `character varying(200)` | sí | Nombre del usuario que registra la decisión territorial. |  |
| 8 | `actor_rol` | `character varying(100)` | sí | Rol del usuario que registra la decisión territorial. |  |
| 9 | `comentarios` | `text` | sí | Comentarios sobre la decisión territorial. |  |
| 10 | `fecha_decision` | `timestamp without time zone` | sí | Fecha y hora de la decisión de la territorial sobre el plan de trabajo académico. |  |
| 11 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 12 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 13 | `nivel` | `character varying(20)` | no | Nivel de formación al que corresponde la aprobación: pregrado o posgrado, con el mismo criterio de clasificación por tipo de programa usado para Sede Central. Por defecto pregrado. |  |
| 14 | `componente` | `character varying(60)` | no | Componente territorial que aprueba el registro. Valores previstos: academica_territorial, complementarias_territorial; por defecto academica_territorial (EFDS-1353). |  |
| 15 | `scope` | `character varying(50)` | sí | Origen de la aprobación territorial: «programacion» cuando la da la concertación de Programación Académica; nulo cuando se aprueba en el plan de trabajo. |  |
| 16 | `scope_id` | `character varying(100)` | sí | Identificador de la concertación de Programación Académica que dio la aprobación, cuando scope es «programacion»; nulo en los demás casos. |  |

## PtaTerritorialReview

Revisiones territoriales de los planes de trabajo académico (PTA). Un registro por territorial, nivel de formación (pregrado o posgrado) y componente territorial revisado de un plan (academic_work_plan.PlanTrabajoAcademico), con su estado (pendiente, revisado o devuelto), el revisor, su rol, comentarios y la fecha de revisión.

- Clave primaria: `id`
- Filas: 3
- Referencia a: `pta_id` → `academic_work_plan.PlanTrabajoAcademico` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla PtaTerritorialReview. Se genera automáticamente. | PK |
| 2 | `pta_id` | `text` | no | Referencia al registro de academic_work_plan.PlanTrabajoAcademico (id). | FK→academic_work_plan.PlanTrabajoAcademico.id |
| 3 | `territorial_id` | `text` | no | Identificador de la dirección territorial (id_seccional de auth.seccionales, como texto) a la que corresponde la revisión. |  |
| 4 | `territorial_nombre` | `text` | sí | Nombre de la territorial que realiza la revisión. |  |
| 5 | `nivel` | `character varying(20)` | no | Nivel de formación al que corresponde la revisión: pregrado o posgrado, con el mismo criterio de clasificación por tipo de programa usado para Sede Central. Por defecto pregrado. |  |
| 6 | `estado` | `character varying(50)` | no | Estado de la revisión territorial del PTA. Valores previstos: pendiente, revisado, devuelto; por defecto pendiente. |  |
| 7 | `revisor_id` | `character varying(100)` | sí | Identificador del usuario que realiza la revisión territorial: id_user de auth."user", tomado del token de sesión. |  |
| 8 | `revisor_nombre` | `character varying(200)` | sí | Nombre del usuario que realiza la revisión territorial. |  |
| 9 | `revisor_rol` | `character varying(100)` | sí | Rol del usuario que realiza la revisión territorial. |  |
| 10 | `comentarios` | `text` | sí | Comentarios de la revisión territorial. |  |
| 11 | `fecha_revision` | `timestamp without time zone` | sí | Fecha y hora de la revisión territorial del plan de trabajo académico. |  |
| 12 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 13 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 14 | `componente` | `character varying(60)` | no | Componente territorial revisado: distingue la revisión de Docencia territorial (academica_territorial) de la de Complementarias territoriales (complementarias_territorial). Por defecto academica_territorial (EFDS-1353). |  |

## Rol

Catálogo de roles del plan de trabajo académico. Un registro por rol, con su nombre, descripción, estado y si es un rol del sistema; se relaciona con los permisos (academic_work_plan.RolPermiso) y los usuarios (academic_work_plan.UsuarioRol).

- Clave primaria: `id`
- Filas: 12

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla Rol. Se genera automáticamente. | PK |
| 2 | `nombre` | `text` | no | Nombre del rol. |  |
| 3 | `descripcion` | `text` | sí | Descripción del rol. |  |
| 4 | `isSystem` | `boolean` | no | Indica si el rol es del sistema. |  |
| 5 | `estado` | `text` | no | Estado del rol. |  |
| 6 | `createdAt` | `timestamp(3) without time zone` | no | Fecha y hora de creación del registro. |  |
| 7 | `updatedAt` | `timestamp(3) without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## RolPermiso

Asignación de permisos a roles del plan de trabajo académico. Un registro por par de rol (academic_work_plan.Rol) y permiso (academic_work_plan.Permiso).

- Clave primaria: `id`
- Filas: 55
- Referencia a: `permisoId` → `academic_work_plan.Permiso` (0..1 → 1); `rolId` → `academic_work_plan.Rol` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla RolPermiso. Se genera automáticamente. | PK |
| 2 | `rolId` | `text` | no | Referencia al registro de academic_work_plan.Rol (id). | FK→academic_work_plan.Rol.id |
| 3 | `permisoId` | `text` | no | Referencia al registro de academic_work_plan.Permiso (id). | FK→academic_work_plan.Permiso.id |
| 4 | `createdAt` | `timestamp(3) without time zone` | no | Fecha y hora de creación del registro. |  |

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
| 6 | `tipo_soporte` | `text` | sí | Tipo de soporte que acredita el documento, de la lista definida por bloque (por ejemplo, documento_identidad, diploma_pregrado, contrato, resolucion_escalafon, autorizacion_habeas_data). |  |
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

Parámetro de inicio de la extracción de datos de documentos del RUND (REQ-RUND-F014). Guarda la fecha y hora desde la que aplica la extracción.

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `boolean` | no | Identificador único del registro en la tabla RundExtraccionInicio. | PK |
| 2 | `desde` | `timestamp with time zone` | no | Fecha y hora desde la que se toman los registros para la extracción, con zona horaria. |  |

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
| 6 | `disponible_en` | `timestamp with time zone` | no | Fecha y hora a partir de la cual el trabajo queda disponible para que un proceso lo tome de la cola. |  |
| 7 | `lease_id` | `uuid` | sí | Identificador aleatorio de la reserva con la que un proceso toma el trabajo; se asigna al reservar el trabajo y se limpia al terminar, fallar o vencer la reserva. |  |
| 8 | `lease_hasta` | `timestamp with time zone` | sí | Fecha y hora en que vence la reserva del trabajo: 90 segundos, renovados cada 20 segundos mientras se procesa. Si vence, el trabajo vuelve a PENDIENTE (o a ERROR con 3 intentos) con código PROCESAMIENTO_INTERRUMPIDO. |  |
| 9 | `perfil_base` | `jsonb` | no | Valores del perfil del docente en los campos de extracción al momento del análisis, en JSON (campo: valor); sirven como valor previo de cada sugerencia. |  |
| 10 | `motor` | `jsonb` | no | Identificación del procesamiento en JSON: modelo de lenguaje local, motor OCR (por ejemplo, PaddleOCR), SHA-256 del PDF, número de páginas y versión del contrato de extracción. |  |
| 11 | `error_codigo` | `text` | sí | Código del error del último intento, si lo hubo, de una lista fija (por ejemplo, OCR_NO_DISPONIBLE, MODELO_TIMEOUT, PDF_INVALIDO, DOCUMENTO_MODIFICADO, PROCESAMIENTO_INTERRUMPIDO o EXTRACCION_NO_DISPONIBLE). Se borra al completar. |  |
| 12 | `creado_por` | `text` | no | Usuario que creó el registro. |  |
| 13 | `creado_en` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 14 | `actualizado_en` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 15 | `etapa` | `text` | no | Etapa actual del trabajo de extracción dentro de su procesamiento. Valor inicial: EN_COLA. |  |
| 16 | `etapa_desde` | `timestamp with time zone` | no | Fecha y hora en que el trabajo entró a su etapa actual. |  |
| 17 | `iniciado_en` | `timestamp with time zone` | sí | Fecha y hora del inicio. |  |
| 18 | `notificacion_id` | `uuid` | no | Clave de idempotencia del aviso de fin de la extracción que se envía al servicio de notificaciones; evita avisos duplicados. Se genera automáticamente. |  |
| 19 | `notificado_en` | `timestamp with time zone` | sí | Fecha y hora de la notificación. |  |
| 20 | `notificacion_proxima` | `timestamp with time zone` | no | Fecha y hora programada para el próximo intento de aviso de fin de la extracción a quien la solicitó o cargó el soporte; se reprograma un minuto después en cada intento y un día después si no se encuentra el usuario. |  |

## RundInvitacionDocente

Invitaciones enviadas a docentes para ingresar al RUND con verificación por código de un solo uso (OTP). Un registro por invitación, con el correo institucional y el documento del docente, el token y su vencimiento, los intentos de OTP, el bloqueo y las fechas de envío, apertura y última actividad.

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla RundInvitacionDocente. Se genera automáticamente. | PK |
| 2 | `correo_institucional` | `character varying(255)` | no | Correo electrónico institucional del docente al que se envía la invitación. |  |
| 3 | `documento_identidad` | `character varying(100)` | sí | Número del documento de identidad del docente invitado. | Identificación |
| 4 | `token_invitacion` | `character varying(255)` | no | Token único del enlace de invitación enviado al docente. | única Credencial de acceso |
| 5 | `otp_hash` | `character varying(255)` | sí | Hash del código de un solo uso (OTP) enviado al docente para validar el acceso. |  |
| 6 | `estado_invitacion` | `character varying(50)` | no | Estado de la invitación al docente. Valor inicial: Enviada. |  |
| 7 | `caducidad_token` | `timestamp without time zone` | no | Fecha y hora en que vence el token de invitación. |  |
| 8 | `intentos_otp` | `integer` | sí | Número de intentos de validación del código OTP. Por defecto, 0. |  |
| 9 | `bloqueo_hasta` | `timestamp without time zone` | sí | Fecha y hora hasta la cual la invitación queda bloqueada para validar el OTP. |  |
| 10 | `fecha_envio` | `timestamp without time zone` | sí | Fecha y hora de envío de la invitación al docente. |  |
| 11 | `fecha_apertura` | `timestamp without time zone` | sí | Fecha y hora en que el docente abrió la invitación. |  |
| 12 | `ultima_actividad` | `timestamp without time zone` | sí | Fecha y hora de la última actividad sobre la invitación. |  |
| 13 | `docente_id` | `text` | sí | Identificador del docente asociado a la invitación, en texto. |  |
| 14 | `operador_id` | `character varying(255)` | sí | Identificador del operador que generó la invitación. |  |
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
| 7 | `periodo` | `text` | sí | Periodo académico consultado, tal como se envió en el filtro de la consulta; se compara con el periodo del PTA. |  |
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

## Sede

Sedes territoriales del plan de trabajo académico. Un registro por sede, con su código, nombre, municipio y la territorial a la que pertenece (academic_work_plan.Territorial).

- Clave primaria: `id`
- Filas: 280
- Referencia a: `territorialId` → `academic_work_plan.Territorial` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla Sede. Se genera automáticamente. | PK |
| 2 | `territorialId` | `text` | no | Referencia al registro de academic_work_plan.Territorial (id). | FK→academic_work_plan.Territorial.id |
| 3 | `nombre` | `text` | no | Nombre de la sede. |  |
| 4 | `municipio` | `text` | sí | Municipio donde se ubica la sede. |  |
| 5 | `createdAt` | `timestamp(3) without time zone` | no | Fecha y hora de creación del registro. |  |
| 6 | `updatedAt` | `timestamp(3) without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 7 | `codigo` | `text` | sí | Código de la sede, único en la tabla. | única |

## SistemaAlerta

Alertas del sistema en el plan de trabajo académico. Un registro por alerta, con su tipo, severidad, mensaje, la entidad que la origina y si está resuelta.

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla SistemaAlerta. Se genera automáticamente. | PK |
| 2 | `tipo` | `text` | no | Tipo de alerta del sistema. |  |
| 3 | `severidad` | `text` | no | Nivel de severidad de la alerta; por defecto, «ALTA». |  |
| 4 | `mensaje` | `text` | no | Mensaje descriptivo de la alerta. |  |
| 5 | `entidadId` | `text` | sí | Identificador del registro que origina la alerta. |  |
| 6 | `entidadRef` | `text` | sí | Referencia o tipo de la entidad que origina la alerta. |  |
| 7 | `resuelta` | `boolean` | no | Indica si la alerta del sistema está resuelta. |  |
| 8 | `createdAt` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `updatedAt` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## SolicitudPTA

Solicitudes de los docentes sobre sus planes de trabajo académico (PTA): de creación y de edición de componentes. Un registro por solicitud de un docente (academic_work_plan.Docente), con el caso, la razón, la justificación, los documentos de soporte, los componentes solicitados, el estado y la resolución (quién la resolvió, fecha, motivo, acción y decisión por componente).

- Clave primaria: `id`
- Filas: 13
- Referencia a: `docenteId` → `academic_work_plan.Docente` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla SolicitudPTA. Se genera automáticamente. | PK |
| 2 | `docenteId` | `text` | no | Referencia al registro de academic_work_plan.Docente (id). | FK→academic_work_plan.Docente.id |
| 3 | `docenteNombre` | `text` | no | Nombre del docente que presenta la solicitud. |  |
| 4 | `docenteEmail` | `text` | sí | Correo electrónico del docente que presenta la solicitud. | Contacto |
| 5 | `caso` | `text` | no | Caso que motiva la solicitud, enviado por la aplicación; «edicion_pta» en las solicitudes de edición de componentes. |  |
| 6 | `razon` | `text` | no | Razón de la solicitud, enviada por la aplicación; en las solicitudes de edición, por defecto «Edición de componentes del PTA». |  |
| 7 | `justificacion` | `text` | no | Justificación detallada de la solicitud. |  |
| 8 | `casoLibre` | `text` | sí | Descripción libre del caso de la solicitud. |  |
| 9 | `archivos` | `jsonb` | sí | Documentos de soporte de la solicitud: arreglo JSON de hasta cinco archivos PDF de máximo 10 MB, cada uno con url (en /uploads/pta-solicitudes/), nombre, tipo («pdf») y tamaño en bytes. |  |
| 10 | `estado` | `text` | no | Estado de la solicitud sobre el plan de trabajo académico. |  |
| 11 | `resueltoPor` | `text` | sí | Nombre del usuario que resolvió la solicitud, tomado de la sesión; «Administrador» si no se identifica. |  |
| 12 | `resolucionFecha` | `timestamp with time zone` | sí | Fecha y hora de resolución de la solicitud. |  |
| 13 | `resolucionMotivo` | `text` | sí | Motivo de la resolución de la solicitud. |  |
| 14 | `resolucionAccion` | `text` | sí | Acción tomada al resolver la solicitud. En las solicitudes de edición toma habilitar_edicion_componentes, denegar_edicion_componentes, edicion_componentes_aprobada o edicion_componentes_aprobada_automaticamente; en las de creación, el valor que envía la aplicación. |  |
| 15 | `territorialNueva` | `text` | sí | Territorial nueva registrada al resolver la solicitud, según el valor que envía la aplicación. |  |
| 16 | `horasPtaOriginal` | `integer` | sí | Número de horas del plan de trabajo antes de la solicitud. |  |
| 17 | `horasPtaNuevo` | `integer` | sí | Número de horas del plan de trabajo solicitadas. |  |
| 18 | `notificacionLeida` | `boolean` | no | Indica si se leyó la notificación de la solicitud. |  |
| 19 | `createdAt` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 20 | `updatedAt` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 21 | `tipoSolicitud` | `text` | no | Tipo de solicitud del docente. Valores previstos: creacion (flujo de creación del PTA) y edicion_componentes (edición de componentes del mismo PTA, sin crear un plan adicional); por defecto creacion. |  |
| 22 | `ptaId` | `uuid` | sí | Identificador del plan de trabajo académico al que se refiere la solicitud. |  |
| 23 | `componentes` | `jsonb` | sí | Componentes funcionales del PTA seleccionados por el docente en la solicitud (docencia, investigacion, extension o complementarias), en formato JSON. |  |
| 24 | `estadoPtaAnterior` | `text` | sí | Estado consolidado que tenía el PTA antes de autorizar su reapertura. |  |
| 25 | `decisionesComponentes` | `jsonb` | sí | Estado y trazabilidad de la decisión independiente por componente solicitado. |  |

## Territorial

Catálogo de territoriales del plan de trabajo académico. Un registro por territorial, con su código y nombre; agrupa las sedes de academic_work_plan.Sede.

- Clave primaria: `id`
- Filas: 21

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla Territorial. Se genera automáticamente. | PK |
| 2 | `nombre` | `text` | no | Nombre de la territorial. |  |
| 3 | `codigo` | `text` | sí | Código de la territorial. |  |
| 4 | `createdAt` | `timestamp(3) without time zone` | no | Fecha y hora de creación del registro. |  |
| 5 | `updatedAt` | `timestamp(3) without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## Usuario

Usuarios del plan de trabajo académico. Un registro por usuario, con su correo, nombre y si está activo; se relaciona con sus datos personales (academic_work_plan.Persona) y sus roles (academic_work_plan.UsuarioRol).

- Clave primaria: `id`
- Filas: 283

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla Usuario. Se genera automáticamente. | PK |
| 2 | `email` | `text` | no | Correo electrónico del usuario. | Contacto |
| 3 | `password` | `text` | no | Contraseña del usuario en la tabla de usuarios del plan de trabajo; la autenticación se realiza contra auth."user". | Credencial de acceso |
| 4 | `nombre` | `text` | sí | Nombre del usuario. |  |
| 5 | `activo` | `boolean` | no | Indica si el usuario está activo. |  |
| 6 | `createdAt` | `timestamp(3) without time zone` | no | Fecha y hora de creación del registro. |  |
| 7 | `updatedAt` | `timestamp(3) without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## UsuarioRol

Asignación de roles a usuarios del plan de trabajo académico. Un registro por par de usuario (academic_work_plan.Usuario) y rol (academic_work_plan.Rol).

- Clave primaria: `id`
- Filas: 278
- Referencia a: `rolId` → `academic_work_plan.Rol` (0..* → 1); `usuarioId` → `academic_work_plan.Usuario` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `text` | no | Identificador único del registro en la tabla UsuarioRol. Se genera automáticamente. | PK |
| 2 | `usuarioId` | `text` | no | Referencia al registro de academic_work_plan.Usuario (id). | FK→academic_work_plan.Usuario.id |
| 3 | `rolId` | `text` | no | Referencia al registro de academic_work_plan.Rol (id). | FK→academic_work_plan.Rol.id |
| 4 | `createdAt` | `timestamp(3) without time zone` | no | Fecha y hora de creación del registro. |  |

## asignatura

Catálogo de asignaturas de los programas académicos. Un registro por asignatura, identificada por su código (llave del SNIES, RN-01), con su nombre, modalidad, tipo, créditos, horas de clase y del PTA, excepción de la Circular 003, pensum, ubicación semestral, programa, núcleo temático y facultad. Se carga desde una plantilla de importación y lo consulta la programación académica (academic-schedule).

- Clave primaria: `id`
- Filas: 503
- Referencia a: `id_facultad` → `academic_work_plan.facultad` (1..* → 1); `id_nucleo_tematico` → `academic_work_plan.nucleo_tematico` (0..* → 1); `id_programa` → `academic_work_plan.programa` (0..* → 1); `id_ubicacion_semestral` → `academic_work_plan.ubicacion_semestral` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | Identificador único del registro en la tabla asignatura. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(20)` | no | Código único de la asignatura; llave maestra del SNIES (RN-01). La importación lo exige y admite hasta 20 caracteres. | única |
| 3 | `nombre` | `character varying(200)` | no | Nombre de la asignatura. |  |
| 4 | `nombre_base` | `character varying(200)` | sí | Nombre de la asignatura que se muestra en las interfaces y en el plan de trabajo académico; se carga desde la columna nombre_base de la plantilla de importación y no se calcula. |  |
| 5 | `modalidad_sufijo` | `character varying(30)` | sí | Texto de modalidad tal como viene en la plantilla de importación; la columna modalidad guarda su valor normalizado (presencial, presencial_dia, presencial_noche, virtual, distancia, mixta o sin_definir). |  |
| 6 | `modalidad` | `character varying(30)` | no | Modalidad de oferta de la asignatura. Valores permitidos: presencial, presencial_dia, presencial_noche, virtual, distancia, mixta, sin_definir; por defecto sin_definir. |  |
| 7 | `requiere_revision_modalidad` | `boolean` | no | Indica si la modalidad de la asignatura requiere revisión. |  |
| 8 | `creditos` | `smallint` | no | Número de créditos académicos de la asignatura. |  |
| 9 | `id_ubicacion_semestral` | `smallint` | no | Referencia al registro de academic_work_plan.ubicacion_semestral (id). | FK→academic_work_plan.ubicacion_semestral.id |
| 10 | `id_programa` | `bigint` | no | Referencia al registro de academic_work_plan.programa (id). | FK→academic_work_plan.programa.id |
| 11 | `id_nucleo_tematico` | `bigint` | no | Referencia al registro de academic_work_plan.nucleo_tematico (id). | FK→academic_work_plan.nucleo_tematico.id |
| 12 | `id_facultad` | `bigint` | no | Referencia al registro de academic_work_plan.facultad (id). | FK→academic_work_plan.facultad.id |
| 13 | `horas_fijas_pta` | `integer` | sí | Número fijo de horas en el plan de trabajo académico (PTA) para las asignaturas con tipo_excepcion: 384 para seminario_enfasis, 20 para opciones_grado_ap y 144 para seminario_opciones_apt; nulo en las demás, que se calculan por créditos. |  |
| 14 | `tipo_excepcion` | `character varying(40)` | sí | Tipo de excepción de la Circular 003 que aplica a la asignatura. Valores permitidos: seminario_enfasis, opciones_grado_ap, seminario_opciones_apt. |  |
| 15 | `activa` | `boolean` | no | Indica si la asignatura está activa. |  |
| 16 | `observaciones` | `text` | sí | Observaciones sobre la asignatura. |  |
| 17 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 18 | `created_by` | `bigint` | sí | Usuario que creó el registro. |  |
| 19 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 20 | `updated_by` | `bigint` | sí | Usuario que realizó la última actualización del registro. |  |
| 21 | `deleted_at` | `timestamp without time zone` | sí | Fecha y hora de la eliminación. |  |
| 22 | `deleted_by` | `bigint` | sí | Identificador del usuario que eliminó lógicamente el registro. |  |
| 23 | `tipo_asignatura` | `character varying(30)` | no | Tipo de asignatura según su forma de desarrollo. Valores permitidos: laboratorio, practica, seminario, taller, teorica. Por defecto, teorica. |  |
| 24 | `pensum` | `character varying(50)` | sí | Plan de estudios (pensum) al que pertenece la asignatura, cargado desde la columna Pensum de la plantilla de importación; se usa para filtrar asignaturas por programa y pensum. |  |
| 25 | `horas_clase` | `integer` | sí | Número de horas de clase de la asignatura, cargado desde la plantilla de importación; si falta, se calcula como las horas PTA divididas por 3. |  |
| 26 | `horas_pta` | `integer` | sí | Horas de la asignatura en el PTA, con el factor de carga ya aplicado. |  |

## cetap

Catálogo de CETAP y sedes de la ESAP. Un registro por ubicación (sede central, CETAP u otra), con su código, nombre, nombre normalizado, coordenadas geográficas y la dirección territorial a la que pertenece (academic_work_plan.direccion_territorial); se relaciona con la oferta de programas, los periodos y los alias del CETAP.

- Clave primaria: `id`
- Filas: 290
- Referencia a: `id_direccion_territorial` → `academic_work_plan.direccion_territorial` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | Identificador único del registro en la tabla cetap. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(20)` | no | Código del CETAP, único en la tabla. | única |
| 3 | `nombre` | `character varying(100)` | no | Nombre del CETAP. |  |
| 4 | `nombre_normalizado` | `character varying(100)` | no | Nombre del CETAP normalizado: sin tildes, sin espacios repetidos y en mayúsculas. Se usa para encontrar el CETAP en las cargas y es único dentro de cada dirección territorial. |  |
| 5 | `id_direccion_territorial` | `bigint` | no | Referencia al registro de academic_work_plan.direccion_territorial (id). | FK→academic_work_plan.direccion_territorial.id |
| 6 | `tipo` | `character varying(20)` | no | Tipo de ubicación registrada en el catálogo de CETAP. Valores permitidos: sede_central, cetap, otro; por defecto cetap. |  |
| 7 | `latitud` | `numeric(10,7)` | sí | Latitud geográfica de la ubicación del CETAP, tomada del archivo de carga de estructura. |  |
| 8 | `longitud` | `numeric(10,7)` | sí | Longitud geográfica de la ubicación del CETAP, en grados decimales. |  |
| 9 | `activo` | `boolean` | no | Indica si el CETAP está activo. |  |
| 10 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 11 | `created_by` | `bigint` | sí | Usuario que creó el registro. |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 13 | `updated_by` | `bigint` | sí | Usuario que realizó la última actualización del registro. |  |
| 14 | `deleted_at` | `timestamp without time zone` | sí | Fecha y hora de la eliminación. |  |
| 15 | `deleted_by` | `bigint` | sí | Identificador del usuario que eliminó lógicamente el registro. |  |

## cetap_alias

Nombres alternativos de los CETAP. Un registro por alias con el que se identifica un CETAP (academic_work_plan.cetap) en las fuentes de datos, con su forma normalizada para la comparación y el origen del alias.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `id_cetap` → `academic_work_plan.cetap` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | Identificador único del registro en la tabla cetap_alias. Se genera automáticamente. | PK |
| 2 | `id_cetap` | `bigint` | no | Referencia al registro de academic_work_plan.cetap (id). | FK→academic_work_plan.cetap.id |
| 3 | `alias` | `character varying(100)` | no | Nombre alternativo con el que se identifica el CETAP en las fuentes de datos. |  |
| 4 | `alias_normalizado` | `character varying(100)` | no | Alias del CETAP normalizado para la comparación; es único en la tabla. | única |
| 5 | `origen` | `character varying(50)` | sí | Fuente de la que proviene el alias. Por defecto, excel_2025_2. |  |
| 6 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 7 | `created_by` | `bigint` | sí | Usuario que creó el registro. |  |

## direccion_territorial

Catálogo de direcciones territoriales de la ESAP. Un registro por dirección territorial, con su código, nombre, nombre normalizado, orden de visualización y si está activa; agrupa los CETAP (academic_work_plan.cetap) y las jefaturas territoriales de la programación académica.

- Clave primaria: `id`
- Filas: 18

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | Identificador único del registro en la tabla direccion_territorial. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(20)` | no | Código de la dirección territorial, único en la tabla. | única |
| 3 | `nombre` | `character varying(50)` | no | Nombre de la dirección territorial. | única |
| 4 | `nombre_normalizado` | `character varying(50)` | no | Nombre de la dirección territorial normalizado: sin tildes, sin espacios repetidos y en mayúsculas. Se usa para encontrar la dirección territorial en las cargas y es único en la tabla. | única |
| 5 | `activo` | `boolean` | no | Indica si la dirección territorial está activa. |  |
| 6 | `orden_visualizacion` | `integer` | no | Posición de la dirección territorial en las listas de presentación. Por defecto, 999. |  |
| 7 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `created_by` | `bigint` | sí | Usuario que creó el registro. |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 10 | `updated_by` | `bigint` | sí | Usuario que realizó la última actualización del registro. |  |
| 11 | `deleted_at` | `timestamp without time zone` | sí | Fecha y hora de la eliminación. |  |
| 12 | `deleted_by` | `bigint` | sí | Identificador del usuario que eliminó lógicamente el registro. |  |

## docencia_concertada

Decisiones de concertación de la docencia recibidas de Programación Académica (EFDS-2315). Un registro por docente, periodo y nivel de formación, con las asignaturas y horas concertadas, las firmas, la huella de lo firmado y el estado de su aplicación al componente de Docencia del plan de trabajo académico (PTA).

- Clave primaria: `id_concertacion`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_concertacion` | `uuid` | no | Identificador único del registro en la tabla docencia_concertada. | PK |
| 2 | `documento_docente` | `character varying(40)` | no | Número de documento de identidad del docente al que corresponde la docencia concertada. | Identificación |
| 3 | `periodo` | `character varying(40)` | sí | Código del periodo académico de la docencia concertada, con la forma AAAA-S (año y semestre 1 o 2). Viene de periodo_academico.codigo del plan de trabajo o del código del periodo de programación. |  |
| 4 | `nivel` | `character varying(10)` | no | Nivel de formación de la docencia concertada. Valores permitidos: posgrado, pregrado. |  |
| 5 | `horas` | `numeric(8,1)` | no | Total de horas de docencia concertadas para el docente en el periodo y nivel, igual a la suma de las horas de los grupos concertados. Admite un decimal y no puede ser negativo. |  |
| 6 | `huella` | `character(64)` | no | Huella SHA-256 en hexadecimal (64 caracteres) de lo firmado en la concertación: docente, periodo, nivel y franjas, serializados en forma canónica. Permite verificar que lo aprobado no cambió. |  |
| 7 | `asignaturas` | `jsonb` | no | Lista de asignaturas concertadas, en JSON. Cada elemento lleva idGrupo, asignaturaId, codigo, nombre, programaId, pensum, creditos, semestre, modalidad, fechaInicio, fechaFin, horas y territorialId (seccional donde se dicta). |  |
| 8 | `firmas` | `jsonb` | no | Firmas de la concertación, en JSON. Cada firma lleva rol (docente, revisor o aprobador), idUser, firmadoEn y modoOtp; son obligatorias la del docente y la del aprobador. |  |
| 9 | `registrada_por` | `character varying(80)` | sí | Usuario que realizó el registro. |  |
| 10 | `aplicada_en` | `timestamp with time zone` | sí | Fecha y hora en que el PTA aplicó la docencia concertada a su componente de Docencia. |  |
| 11 | `recibida_en` | `timestamp with time zone` | no | Fecha y hora en que se recibió la docencia concertada. Por defecto, la fecha y hora del registro. |  |
| 12 | `actualizada_en` | `timestamp with time zone` | no | Fecha y hora de la actualización. |  |
| 13 | `estado_aplicacion` | `character varying(40)` | sí | Estado de la aplicación de la docencia concertada al PTA del docente. Valores: aplicada, no_aplica_apagada, pendiente_sin_pta, pendiente_pta_flujo_anterior, pendiente_pta_firmado, pendiente_pta_en_aprobacion. Queda nulo si la concertación está apagada y solo se registra. |  |
| 14 | `detalle_aplicacion` | `text` | sí | Mensaje que explica el estado de aplicación de la decisión al PTA: por qué quedó pendiente o qué ajustes se hicieron al aplicarla. Puede ser nulo. |  |
| 15 | `id_pta` | `text` | sí | Identificador del plan de trabajo académico (PlanTrabajoAcademico.id, UUID guardado como texto) al que se aplicó o se intentó aplicar la decisión. Es nulo cuando el docente aún no tiene PTA o la concertación está apagada. |  |

## facultad

Catálogo de facultades. Un registro por facultad, con su código, nombre y si está activa; se relaciona con los programas y las asignaturas.

- Clave primaria: `id`
- Filas: 4

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | Identificador único del registro en la tabla facultad. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(20)` | no | Código de la facultad, único en la tabla. | única |
| 3 | `nombre` | `character varying(50)` | no | Nombre de la facultad. | única |
| 4 | `activo` | `boolean` | no | Indica si la facultad está activa. |  |
| 5 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 6 | `created_by` | `bigint` | sí | Usuario que creó el registro. |  |
| 7 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 8 | `updated_by` | `bigint` | sí | Usuario que realizó la última actualización del registro. |  |
| 9 | `deleted_at` | `timestamp without time zone` | sí | Fecha y hora de la eliminación. |  |
| 10 | `deleted_by` | `bigint` | sí | Identificador del usuario que eliminó lógicamente el registro. |  |

## nucleo_tematico

Catálogo de núcleos temáticos de los programas académicos. Un registro por núcleo temático de un programa (academic_work_plan.programa), con su código, nombre, descripción y si está activo; agrupa asignaturas.

- Clave primaria: `id`
- Filas: 42
- Referencia a: `id_programa` → `academic_work_plan.programa` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | Identificador único del registro en la tabla nucleo_tematico. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(20)` | no | Código del núcleo temático, único en la tabla. | única |
| 3 | `nombre` | `character varying(100)` | no | Nombre del núcleo temático. | única |
| 4 | `id_programa` | `bigint` | sí | Referencia al registro de academic_work_plan.programa (id). | FK→academic_work_plan.programa.id |
| 5 | `descripcion` | `text` | sí | Descripción del núcleo temático. |  |
| 6 | `activo` | `boolean` | no | Indica si el núcleo temático está activo. |  |
| 7 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `created_by` | `bigint` | sí | Usuario que creó el registro. |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 10 | `updated_by` | `bigint` | sí | Usuario que realizó la última actualización del registro. |  |
| 11 | `deleted_at` | `timestamp without time zone` | sí | Fecha y hora de la eliminación. |  |
| 12 | `deleted_by` | `bigint` | sí | Identificador del usuario que eliminó lógicamente el registro. |  |

## oferta_cetap_programa

Oferta de programas académicos por CETAP y periodo. Un registro por programa (academic_work_plan.programa) ofrecido en un CETAP (academic_work_plan.cetap) en un periodo académico (academic_work_plan.periodo_academico), con los cupos estimados, observaciones y si está activa; se relaciona con los grupos de la programación académica.

- Clave primaria: `id`
- Filas: 337
- Referencia a: `id_cetap` → `academic_work_plan.cetap` (0..* → 1); `id_periodo_academico` → `academic_work_plan.periodo_academico` (1..* → 1); `id_programa` → `academic_work_plan.programa` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | Identificador único del registro en la tabla oferta_cetap_programa. Se genera automáticamente. | PK |
| 2 | `id_cetap` | `bigint` | no | Referencia al registro de academic_work_plan.cetap (id). | FK→academic_work_plan.cetap.id |
| 3 | `id_programa` | `bigint` | no | Referencia al registro de academic_work_plan.programa (id). | FK→academic_work_plan.programa.id |
| 4 | `id_periodo_academico` | `bigint` | no | Referencia al registro de academic_work_plan.periodo_academico (id). | FK→academic_work_plan.periodo_academico.id |
| 5 | `cupos_estimados` | `integer` | sí | Número estimado de cupos del programa en el CETAP para el periodo académico. |  |
| 6 | `observaciones` | `text` | sí | Observaciones sobre la oferta del programa en el CETAP. |  |
| 7 | `activa` | `boolean` | no | Indica si la oferta del programa en el CETAP está activa. |  |
| 8 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `created_by` | `bigint` | sí | Usuario que creó el registro. |  |
| 10 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 11 | `updated_by` | `bigint` | sí | Usuario que realizó la última actualización del registro. |  |
| 12 | `deleted_at` | `timestamp without time zone` | sí | Fecha y hora de la eliminación. |  |
| 13 | `deleted_by` | `bigint` | sí | Identificador del usuario que eliminó lógicamente el registro. |  |

## periodo_academico

Catálogo de periodos académicos. Un registro por periodo (año y semestre), con su código, fechas de inicio y fin y estado (planeación, concertación, en curso o cerrado); se relaciona con la oferta de programas, los CETAP por periodo y la programación académica.

- Clave primaria: `id`
- Filas: 2

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | Identificador único del registro en la tabla periodo_academico. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(10)` | no | Código del periodo académico, único en la tabla. | única |
| 3 | `anio` | `integer` | no | Año del periodo académico. |  |
| 4 | `semestre` | `smallint` | no | Número del semestre del año al que corresponde el periodo académico. |  |
| 5 | `fecha_inicio` | `date` | no | Fecha de inicio del periodo académico. |  |
| 6 | `fecha_fin` | `date` | no | Fecha de finalización del periodo académico. |  |
| 7 | `estado` | `character varying(20)` | no | Estado del periodo académico. Valores permitidos: planeacion, concertacion, en_curso, cerrado; por defecto planeacion. |  |
| 8 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `created_by` | `bigint` | sí | Usuario que creó el registro. |  |
| 10 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 11 | `updated_by` | `bigint` | sí | Usuario que realizó la última actualización del registro. |  |

## periodo_cetap

Relación entre periodos académicos y CETAP. Un registro por CETAP (academic_work_plan.cetap) en un periodo académico (academic_work_plan.periodo_academico), con la indicación de si está activo en ese periodo.

- Clave primaria: `id`
- Filas: 576
- Referencia a: `id_cetap` → `academic_work_plan.cetap` (1..* → 1); `id_periodo_academico` → `academic_work_plan.periodo_academico` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | Identificador único del registro en la tabla periodo_cetap. Se genera automáticamente. | PK |
| 2 | `id_periodo_academico` | `bigint` | no | Referencia al registro de academic_work_plan.periodo_academico (id). | FK→academic_work_plan.periodo_academico.id |
| 3 | `id_cetap` | `bigint` | no | Referencia al registro de academic_work_plan.cetap (id). | FK→academic_work_plan.cetap.id |
| 4 | `activo` | `boolean` | sí | Indica si el CETAP está activo en el periodo académico. |  |
| 5 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 6 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## programa

Catálogo de programas académicos. Un registro por programa, con su código, nombre, facultad, nivel de formación, modalidad, periodo académico, factores de cálculo de horas y categoría de horas según la Circular 003; se relaciona con las asignaturas, los núcleos temáticos, la oferta por CETAP y la programación académica. Es la fuente del catálogo de programas que consulta la programación académica (RN-01/RN-02).

- Clave primaria: `id`
- Filas: 20
- Referencia a: `id_periodo_academico` → `academic_work_plan.periodo_academico` (0..* → 0..1); `id_facultad` → `academic_work_plan.facultad` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | Identificador único del registro en la tabla programa. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(20)` | no | Código del programa, único en la tabla. | única |
| 3 | `nombre` | `character varying(100)` | no | Nombre del programa. |  |
| 4 | `nombre_excel` | `character varying(100)` | no | Nombre del programa tal como aparece en la columna nombre_excel_origen de la hoja PROGRAMAS del archivo Excel de carga del catálogo académico; si viene vacío se usa el nombre del programa. Se usa para asociar las asignaturas con su programa al validar la carga. |  |
| 5 | `nombre_corto` | `character varying(30)` | no | Nombre abreviado del programa. |  |
| 6 | `id_facultad` | `bigint` | no | Referencia al registro de academic_work_plan.facultad (id). | FK→academic_work_plan.facultad.id |
| 7 | `tipo` | `character varying(20)` | no | Nivel de formación del programa académico. Valores permitidos: pregrado, tecnico_profesional, tecnologico, especializacion, maestria, doctorado. |  |
| 8 | `modalidad` | `character varying(20)` | no | Modalidad del programa académico. Valores permitidos: presencial, distancia, mixto. |  |
| 9 | `horas_base_por_credito` | `integer` | no | Factor de horas por crédito con el que se calculan las horas de cada asignatura en el plan de trabajo académico del docente (créditos × factor × 3), según la Circular 003. Por defecto, 16. |  |
| 10 | `horas_pregrado_central` | `integer` | sí | Horas clase fijas de las asignaturas de los pregrados de la sede central. Si es mayor que cero, las horas de la asignatura en el plan de trabajo académico son este valor × 3 y no se calculan por crédito; nulo o cero indica que no aplica. |  |
| 11 | `activo` | `boolean` | no | Indica si el programa está activo. |  |
| 12 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 13 | `created_by` | `bigint` | sí | Usuario que creó el registro. |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 15 | `updated_by` | `bigint` | sí | Usuario que realizó la última actualización del registro. |  |
| 16 | `deleted_at` | `timestamp without time zone` | sí | Fecha y hora de la eliminación. |  |
| 17 | `deleted_by` | `bigint` | sí | Identificador del usuario que eliminó lógicamente el registro. |  |
| 18 | `id_periodo_academico` | `bigint` | sí | Referencia al registro de academic_work_plan.periodo_academico (id). | FK→academic_work_plan.periodo_academico.id |
| 19 | `categoria_horas_circular003` | `character varying(50)` | sí | Categoría de horas del programa según la Circular 003: pregrado_sede_central, pregrado_territorial, especializacion o maestria. Se toma del archivo de carga (en minúsculas) o se infiere del tipo de programa y de las horas de pregrado central. |  |
| 20 | `descripcion_categoria_circular003` | `text` | sí | Descripción de la categoría de horas del programa según la Circular 003. Se toma del archivo de carga o, si no viene, el sistema asigna un texto fijo según la categoría. |  |
| 21 | `horas_pta_referencia_circular003` | `character varying(150)` | sí | Horas de referencia del plan de trabajo académico para el programa según la Circular 003, en texto, tal como vienen en el archivo de carga. |  |
| 22 | `formula_calculo_horas` | `text` | sí | Fórmula de cálculo de las horas del programa, en texto descriptivo tomado del archivo de carga. El sistema no la interpreta: el cálculo lo hace la lógica del plan de trabajo académico con el factor por crédito y las horas de pregrado central. |  |

## ubicacion_semestral

Catálogo de ubicaciones semestrales del plan de estudios. Un registro por semestre, con su código, etiqueta, tipo de programa (pregrado o posgrado) y orden de presentación del catálogo agrupado (AC-01); se relaciona con las asignaturas.

- Clave primaria: `id`
- Filas: 16

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `smallint` | no | Identificador único del registro en la tabla ubicacion_semestral. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(10)` | no | Código de la ubicación semestral, único en la tabla. | única |
| 3 | `etiqueta` | `character varying(30)` | no | Texto con el que se muestra el semestre del plan de estudios; es único en la tabla. | única |
| 4 | `tipo_programa` | `character varying(20)` | no | Tipo de programa al que corresponde la ubicación semestral. Valores permitidos: pregrado, posgrado. |  |
| 5 | `orden` | `smallint` | no | Posición de la ubicación semestral en el ordenamiento. |  |

## validacion_documental

Validación documental de los campos del RUND de los docentes. Un registro por docente (academic_work_plan.Docente) y campo del RUND, con el grupo de soporte documental, el documento de la carpeta digital que lo soporta, su estado de validación (aceptado, no aplica, pendiente, rechazado o sin cargar), las fechas de carga y validación, quién lo validó y la observación.

- Clave primaria: `id`
- Filas: 12000
- Referencia a: `docente_id` → `academic_work_plan.Docente` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla validacion_documental. Se genera automáticamente. | PK |
| 2 | `docente_id` | `text` | no | Referencia al registro de academic_work_plan.Docente (id). | FK→academic_work_plan.Docente.id |
| 3 | `campo_rund` | `character varying(100)` | no | Campo del RUND al que corresponde el documento de soporte del docente. Valores posibles: DOCUMENTO_IDENTIDAD, TIPO_DOCUMENTO, NOMBRE_COMPLETO, FECHA_NACIMIENTO, GENERO, CORREO_INSTITUCIONAL, VINCULACION, TERRITORIAL, DEDICACION, CATEGORIA_ESCALAFON, INICIO_VINCULACION, FIN_VINCULACION, ACTO_ADMINISTRATIVO, PUNTAJE_SALARIAL, SITUACION_ADMINISTRATIVA, NIVEL_FORMACION, TITULO_PREGRADO, TITULO_ESPECIALIZACION, TITULO_MAESTRIA, TITULO_DOCTORADO, TITULO_POSDOCTORADO, NUCLEO_TEMATICO, PERFIL_ACADEMICO y ULTIMA_EVALUACION. Es único por docente. |  |
| 4 | `tipo_documento_soporte` | `character varying(100)` | no | Grupo de soporte documental que exige el campo del RUND: IDENTIDAD, CONTACTO, VINCULACION, ESCALAFON, SITUACION, FORMACION o EVALUACION. Código fijo del sistema, independiente de auth.tipo_documento. |  |
| 5 | `id_documento_carpeta` | `text` | sí | Identificador del documento de la carpeta digital (auth.documento_carpeta_digital.id_documento, UUID) que soporta el campo; se guarda como texto y sin FK porque está en otro esquema. Lo asigna la sincronización de documentos del RUND. |  |
| 6 | `estado_documento` | `character varying(30)` | no | Estado de validación del documento de soporte. Valores permitidos: Aceptado, No aplica, Pendiente, Rechazado, Sin cargar. Por defecto, Sin cargar. |  |
| 7 | `fecha_carga` | `timestamp without time zone` | sí | Fecha y hora de carga del documento soporte. |  |
| 8 | `fecha_validacion` | `timestamp without time zone` | sí | Fecha y hora de validación del documento soporte. |  |
| 9 | `validado_por` | `character varying(150)` | sí | Usuario que realizó la validación. |  |
| 10 | `observacion` | `text` | sí | Observación sobre la validación del documento soporte. |  |
| 11 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 12 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |
