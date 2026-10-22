# Programación académica (`academic-schedule`)

Esquema para la gestión de franjas horarias, aulas, jornadas y programación académica institucional ESAP

14 tablas · 0 vistas · 147 columnas · 666 filas · 3 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`asignacion_docente`](#asignacion_docente) | Tabla | 0 | Docente asignado a un grupo. La llave es auth.personas.id_person (identidad estable), no Docente.id, que cambia por periodo de carga. |
| [`aula`](#aula) | Tabla | 28 | Catálogo de aulas. Desde el Lote 1 son las 28 reales de Sede Central (provisional=FALSE); capacidad pendiente del CRUD de NUEVA-6. |
| [`cetap_sin_catalogo`](#cetap_sin_catalogo) | Tabla | 46 | CETAPs declarados en el detalle territorial que no tienen contraparte en el catálogo oficial. Pendientes de código. No inventar: resolver con Gestión Profesoral. |
| [`concertacion_docencia`](#concertacion_docencia) | Tabla | 0 | _Por documentar_ |
| [`concertacion_firma`](#concertacion_firma) | Tabla | 0 | _Por documentar_ |
| [`concertacion_historial`](#concertacion_historial) | Tabla | 0 | _Por documentar_ |
| [`concertacion_revision`](#concertacion_revision) | Tabla | 0 | _Por documentar_ |
| [`equivalencia_periodo`](#equivalencia_periodo) | Tabla | 5 | _Por documentar_ |
| [`franja_horaria`](#franja_horaria) | Tabla | 5 | _Por documentar_ |
| [`grupo`](#grupo) | Tabla | 2 | Instancia independiente de programación de una asignatura (RN-11). El horario y las fechas cuelgan del GRUPO, no de la asignatura. |
| [`jefatura_territorial`](#jefatura_territorial) | Tabla | 0 | Qué territorial(es) gobierna cada usuario con el rol JEFATURA_TERRITORIAL. Referencia la territorial por id: un nombre puede divergir, un id no. |
| [`periodo_programacion`](#periodo_programacion) | Tabla | 5 | _Por documentar_ |
| [`programacion_historica`](#programacion_historica) | Tabla | 575 | Programación 2026-1 y 2026-V1 tal como llegó. Sin FK: cod_asigna es PROGRAMA_PENSUM, no código de materia. No pasa por el guard de publicación. |
| [`programacion_periodo`](#programacion_periodo) | Tabla | 0 | _Por documentar_ |

## asignacion_docente

Docente asignado a un grupo. La llave es auth.personas.id_person (identidad estable), no Docente.id, que cambia por periodo de carga.

- Clave primaria: `id_asignacion`
- Filas: 0
- Referencia a: `id_docente` → `auth.personas` (0..1 → 1); `id_grupo` → `academic-schedule.grupo` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_asignacion` | `uuid` | no | Identificador único del registro en la tabla asignacion_docente. Se genera automáticamente. | PK |
| 2 | `id_grupo` | `uuid` | no | Referencia al registro de academic-schedule.grupo (id_grupo). | única FK→academic-schedule.grupo.id_grupo |
| 3 | `id_docente` | `uuid` | no | Referencia al registro de auth.personas (id_person). | FK→auth.personas.id_person |
| 4 | `horas_asignadas` | `integer` | sí | Horas consumidas por esta asignacion, congeladas al asignar (RN-06). |  |
| 5 | `estado` | `character varying(30)` | no | Estado de la asignación del docente al grupo. |  |
| 6 | `observaciones` | `text` | sí | Observaciones sobre la asignación del docente al grupo. |  |
| 7 | `asignado_por` | `character varying(120)` | sí | Usuario de la decanatura que realizó la asignación del docente. |  |
| 8 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 10 | `disponibilidad_confirmada_por` | `text` | sí | Quién confirmó que se contactó al docente y está disponible en el periodo (AC-03). |  |
| 11 | `disponibilidad_confirmada_en` | `timestamp with time zone` | sí | Cuándo se registró la confirmación de disponibilidad (AC-03). |  |

## aula

Catálogo de aulas. Desde el Lote 1 son las 28 reales de Sede Central (provisional=FALSE); capacidad pendiente del CRUD de NUEVA-6.

- Clave primaria: `codigo`
- Filas: 28

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `codigo` | `character varying(40)` | no | Clave primaria de la tabla aula: código. | PK |
| 2 | `nombre` | `character varying(120)` | no | Nombre del aula. |  |
| 3 | `sede_codigo` | `character varying(40)` | sí | Código de la sede donde se ubica el aula. |  |
| 4 | `capacidad` | `integer` | sí | Número máximo de personas que admite el aula. Debe ser mayor o igual a cero; puede quedar vacío mientras no se registre. |  |
| 5 | `provisional` | `boolean` | no | Indica si el aula se registró como aprovisionamiento provisional y no como dato oficial. |  |
| 6 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 7 | `tipo` | `character varying(20)` | sí | Tipo de espacio: aula o auditorio. |  |
| 8 | `piso` | `smallint` | sí | _Por documentar_ |  |
| 9 | `codigo_cetap` | `character varying(20)` | sí | Código del CETAP (formato CET-XXXX) al que pertenece el aula, según el catálogo academic_work_plan.cetap; las aulas de la Sede Central usan CET-0288. |  |
| 10 | `origen` | `character varying(60)` | sí | Origen del registro del aula: PROGRAMACION_2026-1 para las aulas cargadas por migración y gestion-manual para las creadas por el administrador. Lo asigna el sistema. |  |

## cetap_sin_catalogo

CETAPs declarados en el detalle territorial que no tienen contraparte en el catálogo oficial. Pendientes de código. No inventar: resolver con Gestión Profesoral.

- Clave primaria: `id`
- Filas: 46

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `smallint` | no | Identificador único del registro en la tabla cetap_sin_catalogo. Se genera automáticamente. | PK |
| 2 | `territorial` | `character varying(60)` | no | Nombre de la dirección territorial que declaró el CETAP. Junto con nombre_declarado no se repite. |  |
| 3 | `nombre_declarado` | `character varying(120)` | no | Nombre del CETAP tal como aparece en el detalle territorial, sin contraparte en el catálogo oficial. |  |
| 4 | `registrado_en` | `timestamp with time zone` | no | Fecha y hora del registro. |  |

## concertacion_docencia

_Por documentar._

- Clave primaria: `id_concertacion`
- Filas: 0
- Referencia a: `id_docente` → `auth.personas` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_concertacion` | `uuid` | no | Identificador único del registro en la tabla concertacion_docencia. Se genera automáticamente. | PK |
| 2 | `id_docente` | `uuid` | no | Referencia al registro de auth.personas (id_person). | FK→auth.personas.id_person |
| 3 | `periodo_ref` | `character varying(40)` | no | Identificador del periodo académico de la concertación: id de periodo_academico (plataforma) o UUID (legado). Junto con el docente y el nivel no se repite. |  |
| 4 | `nivel` | `character varying(10)` | no | Nivel de formación de la docencia concertada. Valores permitidos: pregrado, posgrado. |  |
| 5 | `estado` | `character varying(20)` | no | Estado de la concertación de docencia: enviada, revisada, aprobada o devuelta. |  |
| 6 | `horas` | `numeric(8,1)` | no | Total de horas de docencia del periodo concertadas para el nivel, con un decimal. Se calcula sumando las horas de impacto en el PTA de cada grupo (horas de clase de la asignatura por el factor de vinculación), repartidas entre docentes del grupo. |  |
| 7 | `franjas` | `jsonb` | no | Foto de las franjas tomadas por el docente al enviar la concertación, en JSON: lista de objetos con idFranja, idGrupo, codigoAsignatura, asignatura y horas. |  |
| 8 | `huella` | `character(64)` | no | Huella SHA-256 en hexadecimal (64 caracteres) del JSON canónico con el docente, el periodo, el nivel y las franjas enviadas. Es lo que se firma. |  |
| 9 | `comentario` | `text` | sí | Comentario u observación sobre la concertación. |  |
| 10 | `notificada_pta_en` | `timestamp with time zone` | sí | Fecha y hora, con zona horaria, en que la concertación aprobada se entregó al PTA (Plan de Trabajo Académico) por el contrato; si está vacía, la entrega está pendiente y se reintenta (EFDS-2315). |  |
| 11 | `error_notificacion` | `text` | sí | Mensaje de error registrado si falló la notificación al PTA. |  |
| 12 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 13 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 14 | `aplicacion_pta` | `character varying(40)` | sí | Estado de aplicación que devuelve el PTA al registrar la decisión concertada: aplicada, pendiente_sin_pta, pendiente_pta_firmado, pendiente_pta_flujo_anterior o pendiente_pta_en_aprobacion. |  |

## concertacion_firma

_Por documentar._

- Clave primaria: `id_firma`
- Filas: 0
- Referencia a: `id_concertacion` → `academic-schedule.concertacion_docencia` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_firma` | `uuid` | no | Identificador único del registro en la tabla concertacion_firma. Se genera automáticamente. | PK |
| 2 | `id_concertacion` | `uuid` | no | Referencia al registro de academic-schedule.concertacion_docencia (id_concertacion). | FK→academic-schedule.concertacion_docencia.id_concertacion |
| 3 | `rol` | `character varying(20)` | no | Rol con que firma el usuario la concertación. Valores permitidos: docente, revisor, aprobador. |  |
| 4 | `id_user` | `uuid` | no | Identificador del usuario que firma. |  |
| 5 | `firmado_en` | `timestamp with time zone` | no | Fecha y hora de la firma. |  |
| 6 | `modo_otp` | `character varying(10)` | no | Modo de la verificación por código de un solo uso (OTP) usada en la firma. Valores permitidos: real, simulado. |  |
| 7 | `huella` | `character(64)` | no | Huella SHA-256 (64 caracteres hexadecimales) de la concertación sobre la que se firma; se copia de concertacion_docencia.huella en el momento de la firma. |  |
| 8 | `contexto` | `character varying(160)` | no | Contexto del OTP de la firma, con formato prog-docencia:<id>:<huella>:<rol>. |  |

## concertacion_historial

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `id_concertacion` → `academic-schedule.concertacion_docencia` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | Identificador único del registro en la tabla concertacion_historial. Se genera automáticamente. | PK |
| 2 | `id_concertacion` | `uuid` | no | Referencia al registro de academic-schedule.concertacion_docencia (id_concertacion). | FK→academic-schedule.concertacion_docencia.id_concertacion |
| 3 | `accion` | `character varying(20)` | no | Acción realizada sobre la concertación: ENVIAR, REVISAR_ACADEMICA (REVISAR_<tipo de revisión>), DEVOLVER o APROBAR. |  |
| 4 | `estado_anterior` | `character varying(20)` | sí | Estado de la concertación antes de la acción. Vacío cuando no había estado previo. |  |
| 5 | `estado_nuevo` | `character varying(20)` | no | Estado de la concertación después de la acción. |  |
| 6 | `id_user` | `uuid` | no | Identificador del usuario que realizó la acción. |  |
| 7 | `comentario` | `text` | sí | Comentario registrado con la acción. |  |
| 8 | `en` | `timestamp with time zone` | no | Fecha y hora en que se registró la acción, con zona horaria. |  |

## concertacion_revision

_Por documentar._

- Clave primaria: `id_concertacion`, `tipo`
- Filas: 0
- Referencia a: `id_concertacion` → `academic-schedule.concertacion_docencia` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_concertacion` | `uuid` | no | Identificador único del registro en la tabla concertacion_revision. | PK FK→academic-schedule.concertacion_docencia.id_concertacion |
| 2 | `tipo` | `character varying(20)` | no | Clave primaria de la tabla concertacion_revision: tipo. | PK |
| 3 | `id_user` | `uuid` | no | Identificador del usuario que hizo la revisión. |  |
| 4 | `revisado_en` | `timestamp with time zone` | no | Fecha y hora de la revisión. |  |

## equivalencia_periodo

_Por documentar._

- Clave primaria: `codigo_programacion`
- Filas: 5
- Referencia a: `codigo_programacion` → `academic-schedule.periodo_programacion` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `codigo_programacion` | `character varying(20)` | no | Clave primaria de la tabla equivalencia_periodo: código programación. | PK FK→academic-schedule.periodo_programacion.codigo |
| 2 | `codigo_periodo_academico` | `character varying(10)` | sí | Código del periodo académico (academic_work_plan.periodo_academico) equivalente al código de programación. |  |
| 3 | `tipo_oferta` | `character varying(30)` | no | Tipo de oferta que se asigna a los grupos del periodo equivalente. Valores permitidos: periodo_regular, interperiodo, creditos_virtual. |  |
| 4 | `motivo` | `text` | no | Justificación de la equivalencia entre periodos. |  |

## franja_horaria

_Por documentar._

- Clave primaria: `id_franja`
- Filas: 5
- Referencia a: `id_asignatura` → `academic_work_plan.asignatura` (0..* → 0..1); `id_grupo` → `academic-schedule.grupo` (1..* → 0..1); `id_programa` → `academic_work_plan.programa` (0..1 → 0..1); `id_periodo` → `academic-schedule.periodo_programacion` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_franja` | `uuid` | no | Identificador único del registro en la tabla franja_horaria. Se genera automáticamente. | PK |
| 2 | `id_periodo` | `uuid` | sí | Referencia al registro de academic-schedule.periodo_programacion (id_periodo). | FK→academic-schedule.periodo_programacion.id_periodo |
| 3 | `id_docente` | `uuid` | sí | Identificador del docente (auth.personas.id_person) asignado a la franja. Se propaga desde la asignación del grupo con fn_propagar_docente_a_franjas o se fija cuando el docente toma la franja. Una franja PUBLICADA no puede tener docente. |  |
| 4 | `sede_codigo` | `character varying(50)` | sí | _Por documentar_ |  |
| 5 | `aula_codigo` | `character varying(50)` | sí | Código del aula donde se dicta la franja. |  |
| 6 | `dia_semana` | `character varying(15)` | no | Día de la semana de la franja. Valores permitidos: LUNES, MARTES, MIERCOLES, JUEVES, VIERNES, SABADO, DOMINGO. |  |
| 7 | `hora_inicio` | `time without time zone` | no | Hora de inicio de la franja, en formato HH:MM o HH:MM:SS; admite horas arbitrarias (por ejemplo, 11:05). Debe ser anterior a hora_fin (AC-03). |  |
| 8 | `hora_fin` | `time without time zone` | no | Hora de finalización de la franja. Debe ser posterior a hora_inicio. |  |
| 9 | `jornada` | `character varying(30)` | sí | Jornada de la franja. Valores permitidos: DIURNA, NOCTURNA, FIN_DE_SEMANA, DISTANCIA. Por defecto, DIURNA. |  |
| 10 | `cupo_maximo` | `integer` | sí | _Por documentar_ |  |
| 11 | `estado` | `character varying(30)` | sí | Estado de la franja horaria: programado, tomada, aprobada, devuelta o publicada. |  |
| 12 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 13 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 14 | `id_programa` | `bigint` | sí | FK a academic_work_plan.programa. El catálogo es autoritativo (SNIES): aquí solo se referencia, nunca se copia. | FK→academic_work_plan.programa.id |
| 15 | `id_asignatura` | `bigint` | sí | Denormalización de consulta, sincronizada por trigger desde el grupo. No escribir directamente. | FK→academic_work_plan.asignatura.id |
| 16 | `id_grupo` | `uuid` | sí | Dueño de la franja (RN-11). El horario y las fechas cuelgan del grupo, no de la asignatura. | FK→academic-schedule.grupo.id_grupo |
| 17 | `tipo_sesion` | `character varying(30)` | no | Presencial o mediada por tecnologia. Es de la SESION y NO tiene relacion con asignatura.modalidad, que es dato maestro del SNIES. |  |
| 18 | `comentario_jefatura` | `text` | sí | Comentario con el que la jefatura territorial o el revisor de la concertación devuelve la franja al docente. Se registra al pasar la franja a DEVUELTA y se borra al aprobarla o cuando el docente la vuelve a tomar. |  |
| 19 | `excepcion` | `boolean` | no | Indica si la franja horaria se registró como excepción. |  |

## grupo

Instancia independiente de programación de una asignatura (RN-11). El horario y las fechas cuelgan del GRUPO, no de la asignatura.

- Clave primaria: `id_grupo`
- Filas: 2
- Referencia a: `id_asignatura` → `academic_work_plan.asignatura` (0..1 → 1); `id_oferta_cetap` → `academic_work_plan.oferta_cetap_programa` (0..1 → 0..1); `id_periodo_academico` → `academic_work_plan.periodo_academico` (0..1 → 0..1); `id_periodo` → `academic-schedule.periodo_programacion` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_grupo` | `uuid` | no | Identificador único del registro en la tabla grupo. Se genera automáticamente. | PK |
| 2 | `id_asignatura` | `bigint` | no | Referencia al registro de academic_work_plan.asignatura (id). | FK→academic_work_plan.asignatura.id |
| 3 | `id_periodo` | `uuid` | sí | Referencia al registro de academic-schedule.periodo_programacion (id_periodo). | FK→academic-schedule.periodo_programacion.id_periodo |
| 4 | `numero_grupo` | `smallint` | no | _Por documentar_ |  |
| 5 | `id_docente` | `uuid` | sí | Nullable: el grupo se numera antes de asignar docente y horario. Sin UNIQUE contra id_asignatura — un docente puede dictar varios grupos de la misma asignatura (AC-03). |  |
| 6 | `cupo_maximo` | `integer` | no | Número máximo de estudiantes del grupo. Debe ser mayor que cero; por defecto, 30. |  |
| 7 | `estado` | `character varying(30)` | no | Estado del grupo de programación. |  |
| 8 | `observaciones` | `text` | sí | Observaciones sobre el grupo de programación. |  |
| 9 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 10 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 11 | `fecha_inicio` | `date` | sí | Inicio del ciclo de clases de ESTE grupo. Cada grupo tiene su ventana propia. |  |
| 12 | `fecha_fin` | `date` | sí | Fecha de finalización de las clases del grupo. |  |
| 13 | `publicado_en` | `timestamp with time zone` | sí | Cuándo se publicó la oferta del grupo. Publicar exige aula en todas las franjas (EFDS-1374). |  |
| 14 | `id_periodo_academico` | `bigint` | sí | Referencia al registro de academic_work_plan.periodo_academico (id). | FK→academic_work_plan.periodo_academico.id |
| 15 | `tipo_oferta` | `character varying(30)` | sí | Tipo de oferta del grupo dentro del periodo de plataforma. Valores permitidos: periodo_regular, interperiodo, creditos_virtual. |  |
| 16 | `id_oferta_cetap` | `bigint` | sí | Referencia al registro de academic_work_plan.oferta_cetap_programa (id). | FK→academic_work_plan.oferta_cetap_programa.id |

## jefatura_territorial

Qué territorial(es) gobierna cada usuario con el rol JEFATURA_TERRITORIAL. Referencia la territorial por id: un nombre puede divergir, un id no.

- Clave primaria: `id_user`, `id_direccion_territorial`
- Filas: 0
- Referencia a: `id_direccion_territorial` → `academic_work_plan.direccion_territorial` (0..1 → 1); `id_user` → `auth.user` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_user` | `uuid` | no | Identificador único del registro en la tabla jefatura_territorial. | PK FK→auth.user.id_user |
| 2 | `id_direccion_territorial` | `bigint` | no | Identificador único del registro en la tabla jefatura_territorial. | PK FK→academic_work_plan.direccion_territorial.id |
| 3 | `asignado_en` | `timestamp with time zone` | no | Fecha y hora de la asignación. |  |

## periodo_programacion

_Por documentar._

- Clave primaria: `id_periodo`
- Filas: 5

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_periodo` | `uuid` | no | Identificador único del registro en la tabla periodo_programacion. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(20)` | no | Código único del periodo de programación. | única |
| 3 | `nombre` | `character varying(100)` | no | Nombre del periodo de programación. |  |
| 4 | `fecha_inicio` | `date` | no | Fecha de inicio del periodo de programación. |  |
| 5 | `fecha_fin` | `date` | no | Fecha de finalización del periodo de programación. |  |
| 6 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 7 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 8 | `tipo` | `character varying(30)` | sí | Tipo de oferta académica (EFDS-1375): periodo_regular, creditos_virtual o interperiodo. |  |
| 9 | `estado` | `character varying(20)` | no | Ciclo de vida del periodo (NUEVA-5a): planeacion, activo o cerrado. Reemplaza a is_activo, que no podía expresar el tercer estado. Un periodo cerrado es inmutable (NUEVA-5b). OJO: "borrador" pertenece a la publicación de la programación (NUEVA-1), no al periodo: no reintroducir ese nombre aquí. |  |

## programacion_historica

Programación 2026-1 y 2026-V1 tal como llegó. Sin FK: cod_asigna es PROGRAMA_PENSUM, no código de materia. No pasa por el guard de publicación.

- Clave primaria: `id`
- Filas: 575

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | Identificador único del registro en la tabla programacion_historica. Se genera automáticamente. | PK |
| 2 | `periodo` | `character varying(20)` | sí | Periodo académico de la programación (por ejemplo, 2026-1 o 2026-V1), tal como llegó en la programación histórica. |  |
| 3 | `tipo_oferta` | `character varying(40)` | sí | _Por documentar_ |  |
| 4 | `cod_sede` | `character varying(10)` | sí | Código de la sede, tal como llegó en la programación histórica. |  |
| 5 | `seccional` | `character varying(80)` | sí | Nombre de la seccional, tal como llegó en la programación histórica. |  |
| 6 | `sede` | `character varying(80)` | sí | Nombre de la sede, tal como llegó en la programación histórica. |  |
| 7 | `pensum` | `character varying(10)` | sí | _Por documentar_ |  |
| 8 | `programa` | `character varying(20)` | sí | _Por documentar_ |  |
| 9 | `cod_asigna` | `character varying(30)` | sí | Código compuesto PROGRAMA_PENSUM de la asignatura; no es el código de la materia. |  |
| 10 | `asignatura` | `character varying(200)` | sí | Nombre de la asignatura, tal como llegó en la programación histórica. |  |
| 11 | `detalle_asignatura` | `text` | sí | _Por documentar_ |  |
| 12 | `creditos` | `smallint` | sí | Número de créditos académicos de la asignatura. |  |
| 13 | `semestre` | `smallint` | sí | Semestre del plan de estudios en que se ubica la asignatura. |  |
| 14 | `horas` | `smallint` | sí | _Por documentar_ |  |
| 15 | `grupo_original` | `character varying(10)` | sí | Etiqueta de grupo del origen, VERBATIM (A/B/C/I/V). No renombrar. |  |
| 16 | `jornada` | `character varying(30)` | sí | Jornada del grupo, tal como llegó en la programación histórica. |  |
| 17 | `cedula_docente` | `character varying(20)` | sí | Número de cédula del docente asignado, tal como llegó en la programación histórica. | Identificación |
| 18 | `nombre_docente` | `character varying(150)` | sí | Nombre completo del docente asignado, tal como llegó en la programación histórica. |  |
| 19 | `vinculacion_docente` | `character varying(40)` | sí | _Por documentar_ |  |
| 20 | `fecha_inicio` | `character varying(20)` | sí | Fecha de inicio de la programación histórica, en el texto en que llegó de la fuente. |  |
| 21 | `fecha_fin` | `character varying(20)` | sí | Fecha de finalización de la programación histórica, en el texto en que llegó de la fuente. |  |
| 22 | `dia` | `character varying(15)` | sí | Día de la semana de la sesión, en texto, tal como llegó en la programación histórica. |  |
| 23 | `hora_inicio` | `character varying(10)` | sí | Hora de inicio de la sesión, en texto, tal como llegó en la programación histórica. |  |
| 24 | `hora_fin` | `character varying(10)` | sí | Hora de finalización de la sesión, en texto, tal como llegó en la programación histórica. |  |
| 25 | `hrs_clase` | `character varying(10)` | sí | _Por documentar_ |  |
| 26 | `aula` | `character varying(60)` | sí | Nombre o código del aula, tal como llegó en la programación histórica. |  |
| 27 | `estado_aula` | `character varying(20)` | sí | _Por documentar_ |  |
| 28 | `estado_docente` | `character varying(20)` | sí | _Por documentar_ |  |
| 29 | `id_asignatura_sugerido` | `bigint` | sí | SUGERENCIA best-effort por nombre normalizado + semestre. Nunca autoritativa. |  |
| 30 | `importado_en` | `timestamp with time zone` | no | Fecha y hora en que se importó el registro, con zona horaria. |  |
| 31 | `n_candidatos` | `smallint` | sí | Cuántas asignaturas del catálogo coinciden por nombre normalizado. >1 significa que la sugerencia se dejó en NULL a propósito. |  |

## programacion_periodo

_Por documentar._

- Clave primaria: `id_periodo_academico`
- Filas: 0
- Referencia a: `id_periodo_academico` → `academic_work_plan.periodo_academico` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_periodo_academico` | `bigint` | no | Identificador único del registro en la tabla programacion_periodo. | PK FK→academic_work_plan.periodo_academico.id |
| 2 | `estado` | `character varying(20)` | no | Estado de la programación del periodo académico: abierta o cerrada. |  |
| 3 | `cerrada_en` | `timestamp with time zone` | sí | Fecha y hora del cierre. |  |
| 4 | `cerrada_por` | `uuid` | sí | Usuario que realizó el cierre. |  |
| 5 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 6 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
