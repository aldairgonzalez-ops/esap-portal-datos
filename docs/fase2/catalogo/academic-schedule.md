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
| 1 | `id_asignacion` | `uuid` | no | _Por documentar_ | PK |
| 2 | `id_grupo` | `uuid` | no | _Por documentar_ | única FK→academic-schedule.grupo.id_grupo |
| 3 | `id_docente` | `uuid` | no | _Por documentar_ | FK→auth.personas.id_person |
| 4 | `horas_asignadas` | `integer` | sí | Horas consumidas por esta asignacion, congeladas al asignar (RN-06). |  |
| 5 | `estado` | `character varying(30)` | no | _Por documentar_ |  |
| 6 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 7 | `asignado_por` | `character varying(120)` | sí | _Por documentar_ |  |
| 8 | `created_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 9 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 10 | `disponibilidad_confirmada_por` | `text` | sí | Quién confirmó que se contactó al docente y está disponible en el periodo (AC-03). |  |
| 11 | `disponibilidad_confirmada_en` | `timestamp with time zone` | sí | Cuándo se registró la confirmación de disponibilidad (AC-03). |  |

## aula

Catálogo de aulas. Desde el Lote 1 son las 28 reales de Sede Central (provisional=FALSE); capacidad pendiente del CRUD de NUEVA-6.

- Clave primaria: `codigo`
- Filas: 28

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `codigo` | `character varying(40)` | no | _Por documentar_ | PK |
| 2 | `nombre` | `character varying(120)` | no | _Por documentar_ |  |
| 3 | `sede_codigo` | `character varying(40)` | sí | _Por documentar_ |  |
| 4 | `capacidad` | `integer` | sí | _Por documentar_ |  |
| 5 | `provisional` | `boolean` | no | _Por documentar_ |  |
| 6 | `created_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 7 | `tipo` | `character varying(20)` | sí | _Por documentar_ |  |
| 8 | `piso` | `smallint` | sí | _Por documentar_ |  |
| 9 | `codigo_cetap` | `character varying(20)` | sí | _Por documentar_ |  |
| 10 | `origen` | `character varying(60)` | sí | _Por documentar_ |  |

## cetap_sin_catalogo

CETAPs declarados en el detalle territorial que no tienen contraparte en el catálogo oficial. Pendientes de código. No inventar: resolver con Gestión Profesoral.

- Clave primaria: `id`
- Filas: 46

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `smallint` | no | _Por documentar_ | PK |
| 2 | `territorial` | `character varying(60)` | no | _Por documentar_ |  |
| 3 | `nombre_declarado` | `character varying(120)` | no | _Por documentar_ |  |
| 4 | `registrado_en` | `timestamp with time zone` | no | _Por documentar_ |  |

## concertacion_docencia

_Por documentar._

- Clave primaria: `id_concertacion`
- Filas: 0
- Referencia a: `id_docente` → `auth.personas` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_concertacion` | `uuid` | no | _Por documentar_ | PK |
| 2 | `id_docente` | `uuid` | no | _Por documentar_ | FK→auth.personas.id_person |
| 3 | `periodo_ref` | `character varying(40)` | no | _Por documentar_ |  |
| 4 | `nivel` | `character varying(10)` | no | _Por documentar_ |  |
| 5 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 6 | `horas` | `numeric(8,1)` | no | _Por documentar_ |  |
| 7 | `franjas` | `jsonb` | no | _Por documentar_ |  |
| 8 | `huella` | `character(64)` | no | _Por documentar_ |  |
| 9 | `comentario` | `text` | sí | _Por documentar_ |  |
| 10 | `notificada_pta_en` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 11 | `error_notificacion` | `text` | sí | _Por documentar_ |  |
| 12 | `created_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 13 | `updated_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 14 | `aplicacion_pta` | `character varying(40)` | sí | _Por documentar_ |  |

## concertacion_firma

_Por documentar._

- Clave primaria: `id_firma`
- Filas: 0
- Referencia a: `id_concertacion` → `academic-schedule.concertacion_docencia` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_firma` | `uuid` | no | _Por documentar_ | PK |
| 2 | `id_concertacion` | `uuid` | no | _Por documentar_ | FK→academic-schedule.concertacion_docencia.id_concertacion |
| 3 | `rol` | `character varying(20)` | no | _Por documentar_ |  |
| 4 | `id_user` | `uuid` | no | _Por documentar_ |  |
| 5 | `firmado_en` | `timestamp with time zone` | no | _Por documentar_ |  |
| 6 | `modo_otp` | `character varying(10)` | no | _Por documentar_ |  |
| 7 | `huella` | `character(64)` | no | _Por documentar_ |  |
| 8 | `contexto` | `character varying(160)` | no | _Por documentar_ |  |

## concertacion_historial

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `id_concertacion` → `academic-schedule.concertacion_docencia` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | _Por documentar_ | PK |
| 2 | `id_concertacion` | `uuid` | no | _Por documentar_ | FK→academic-schedule.concertacion_docencia.id_concertacion |
| 3 | `accion` | `character varying(20)` | no | _Por documentar_ |  |
| 4 | `estado_anterior` | `character varying(20)` | sí | _Por documentar_ |  |
| 5 | `estado_nuevo` | `character varying(20)` | no | _Por documentar_ |  |
| 6 | `id_user` | `uuid` | no | _Por documentar_ |  |
| 7 | `comentario` | `text` | sí | _Por documentar_ |  |
| 8 | `en` | `timestamp with time zone` | no | _Por documentar_ |  |

## concertacion_revision

_Por documentar._

- Clave primaria: `id_concertacion`, `tipo`
- Filas: 0
- Referencia a: `id_concertacion` → `academic-schedule.concertacion_docencia` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_concertacion` | `uuid` | no | _Por documentar_ | PK FK→academic-schedule.concertacion_docencia.id_concertacion |
| 2 | `tipo` | `character varying(20)` | no | _Por documentar_ | PK |
| 3 | `id_user` | `uuid` | no | _Por documentar_ |  |
| 4 | `revisado_en` | `timestamp with time zone` | no | _Por documentar_ |  |

## equivalencia_periodo

_Por documentar._

- Clave primaria: `codigo_programacion`
- Filas: 5
- Referencia a: `codigo_programacion` → `academic-schedule.periodo_programacion` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `codigo_programacion` | `character varying(20)` | no | _Por documentar_ | PK FK→academic-schedule.periodo_programacion.codigo |
| 2 | `codigo_periodo_academico` | `character varying(10)` | sí | _Por documentar_ |  |
| 3 | `tipo_oferta` | `character varying(30)` | no | _Por documentar_ |  |
| 4 | `motivo` | `text` | no | _Por documentar_ |  |

## franja_horaria

_Por documentar._

- Clave primaria: `id_franja`
- Filas: 5
- Referencia a: `id_asignatura` → `academic_work_plan.asignatura` (0..* → 0..1); `id_grupo` → `academic-schedule.grupo` (1..* → 0..1); `id_programa` → `academic_work_plan.programa` (0..1 → 0..1); `id_periodo` → `academic-schedule.periodo_programacion` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_franja` | `uuid` | no | _Por documentar_ | PK |
| 2 | `id_periodo` | `uuid` | sí | _Por documentar_ | FK→academic-schedule.periodo_programacion.id_periodo |
| 3 | `id_docente` | `uuid` | sí | _Por documentar_ |  |
| 4 | `sede_codigo` | `character varying(50)` | sí | _Por documentar_ |  |
| 5 | `aula_codigo` | `character varying(50)` | sí | _Por documentar_ |  |
| 6 | `dia_semana` | `character varying(15)` | no | _Por documentar_ |  |
| 7 | `hora_inicio` | `time without time zone` | no | _Por documentar_ |  |
| 8 | `hora_fin` | `time without time zone` | no | _Por documentar_ |  |
| 9 | `jornada` | `character varying(30)` | sí | _Por documentar_ |  |
| 10 | `cupo_maximo` | `integer` | sí | _Por documentar_ |  |
| 11 | `estado` | `character varying(30)` | sí | _Por documentar_ |  |
| 12 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 13 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 14 | `id_programa` | `bigint` | sí | FK a academic_work_plan.programa. El catálogo es autoritativo (SNIES): aquí solo se referencia, nunca se copia. | FK→academic_work_plan.programa.id |
| 15 | `id_asignatura` | `bigint` | sí | Denormalización de consulta, sincronizada por trigger desde el grupo. No escribir directamente. | FK→academic_work_plan.asignatura.id |
| 16 | `id_grupo` | `uuid` | sí | Dueño de la franja (RN-11). El horario y las fechas cuelgan del grupo, no de la asignatura. | FK→academic-schedule.grupo.id_grupo |
| 17 | `tipo_sesion` | `character varying(30)` | no | Presencial o mediada por tecnologia. Es de la SESION y NO tiene relacion con asignatura.modalidad, que es dato maestro del SNIES. |  |
| 18 | `comentario_jefatura` | `text` | sí | _Por documentar_ |  |
| 19 | `excepcion` | `boolean` | no | _Por documentar_ |  |

## grupo

Instancia independiente de programación de una asignatura (RN-11). El horario y las fechas cuelgan del GRUPO, no de la asignatura.

- Clave primaria: `id_grupo`
- Filas: 2
- Referencia a: `id_asignatura` → `academic_work_plan.asignatura` (0..1 → 1); `id_oferta_cetap` → `academic_work_plan.oferta_cetap_programa` (0..1 → 0..1); `id_periodo_academico` → `academic_work_plan.periodo_academico` (0..1 → 0..1); `id_periodo` → `academic-schedule.periodo_programacion` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_grupo` | `uuid` | no | _Por documentar_ | PK |
| 2 | `id_asignatura` | `bigint` | no | _Por documentar_ | FK→academic_work_plan.asignatura.id |
| 3 | `id_periodo` | `uuid` | sí | _Por documentar_ | FK→academic-schedule.periodo_programacion.id_periodo |
| 4 | `numero_grupo` | `smallint` | no | _Por documentar_ |  |
| 5 | `id_docente` | `uuid` | sí | Nullable: el grupo se numera antes de asignar docente y horario. Sin UNIQUE contra id_asignatura — un docente puede dictar varios grupos de la misma asignatura (AC-03). |  |
| 6 | `cupo_maximo` | `integer` | no | _Por documentar_ |  |
| 7 | `estado` | `character varying(30)` | no | _Por documentar_ |  |
| 8 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 9 | `created_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 10 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 11 | `fecha_inicio` | `date` | sí | Inicio del ciclo de clases de ESTE grupo. Cada grupo tiene su ventana propia. |  |
| 12 | `fecha_fin` | `date` | sí | _Por documentar_ |  |
| 13 | `publicado_en` | `timestamp with time zone` | sí | Cuándo se publicó la oferta del grupo. Publicar exige aula en todas las franjas (EFDS-1374). |  |
| 14 | `id_periodo_academico` | `bigint` | sí | _Por documentar_ | FK→academic_work_plan.periodo_academico.id |
| 15 | `tipo_oferta` | `character varying(30)` | sí | _Por documentar_ |  |
| 16 | `id_oferta_cetap` | `bigint` | sí | _Por documentar_ | FK→academic_work_plan.oferta_cetap_programa.id |

## jefatura_territorial

Qué territorial(es) gobierna cada usuario con el rol JEFATURA_TERRITORIAL. Referencia la territorial por id: un nombre puede divergir, un id no.

- Clave primaria: `id_user`, `id_direccion_territorial`
- Filas: 0
- Referencia a: `id_direccion_territorial` → `academic_work_plan.direccion_territorial` (0..1 → 1); `id_user` → `auth.user` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_user` | `uuid` | no | _Por documentar_ | PK FK→auth.user.id_user |
| 2 | `id_direccion_territorial` | `bigint` | no | _Por documentar_ | PK FK→academic_work_plan.direccion_territorial.id |
| 3 | `asignado_en` | `timestamp with time zone` | no | _Por documentar_ |  |

## periodo_programacion

_Por documentar._

- Clave primaria: `id_periodo`
- Filas: 5

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_periodo` | `uuid` | no | _Por documentar_ | PK |
| 2 | `codigo` | `character varying(20)` | no | _Por documentar_ | única |
| 3 | `nombre` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `fecha_inicio` | `date` | no | _Por documentar_ |  |
| 5 | `fecha_fin` | `date` | no | _Por documentar_ |  |
| 6 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 7 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 8 | `tipo` | `character varying(30)` | sí | Tipo de oferta académica (EFDS-1375): periodo_regular, creditos_virtual o interperiodo. |  |
| 9 | `estado` | `character varying(20)` | no | Ciclo de vida del periodo (NUEVA-5a): planeacion, activo o cerrado. Reemplaza a is_activo, que no podía expresar el tercer estado. Un periodo cerrado es inmutable (NUEVA-5b). OJO: "borrador" pertenece a la publicación de la programación (NUEVA-1), no al periodo: no reintroducir ese nombre aquí. |  |

## programacion_historica

Programación 2026-1 y 2026-V1 tal como llegó. Sin FK: cod_asigna es PROGRAMA_PENSUM, no código de materia. No pasa por el guard de publicación.

- Clave primaria: `id`
- Filas: 575

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | _Por documentar_ | PK |
| 2 | `periodo` | `character varying(20)` | sí | _Por documentar_ |  |
| 3 | `tipo_oferta` | `character varying(40)` | sí | _Por documentar_ |  |
| 4 | `cod_sede` | `character varying(10)` | sí | _Por documentar_ |  |
| 5 | `seccional` | `character varying(80)` | sí | _Por documentar_ |  |
| 6 | `sede` | `character varying(80)` | sí | _Por documentar_ |  |
| 7 | `pensum` | `character varying(10)` | sí | _Por documentar_ |  |
| 8 | `programa` | `character varying(20)` | sí | _Por documentar_ |  |
| 9 | `cod_asigna` | `character varying(30)` | sí | _Por documentar_ |  |
| 10 | `asignatura` | `character varying(200)` | sí | _Por documentar_ |  |
| 11 | `detalle_asignatura` | `text` | sí | _Por documentar_ |  |
| 12 | `creditos` | `smallint` | sí | _Por documentar_ |  |
| 13 | `semestre` | `smallint` | sí | _Por documentar_ |  |
| 14 | `horas` | `smallint` | sí | _Por documentar_ |  |
| 15 | `grupo_original` | `character varying(10)` | sí | Etiqueta de grupo del origen, VERBATIM (A/B/C/I/V). No renombrar. |  |
| 16 | `jornada` | `character varying(30)` | sí | _Por documentar_ |  |
| 17 | `cedula_docente` | `character varying(20)` | sí | _Por documentar_ | Identificación |
| 18 | `nombre_docente` | `character varying(150)` | sí | _Por documentar_ |  |
| 19 | `vinculacion_docente` | `character varying(40)` | sí | _Por documentar_ |  |
| 20 | `fecha_inicio` | `character varying(20)` | sí | _Por documentar_ |  |
| 21 | `fecha_fin` | `character varying(20)` | sí | _Por documentar_ |  |
| 22 | `dia` | `character varying(15)` | sí | _Por documentar_ |  |
| 23 | `hora_inicio` | `character varying(10)` | sí | _Por documentar_ |  |
| 24 | `hora_fin` | `character varying(10)` | sí | _Por documentar_ |  |
| 25 | `hrs_clase` | `character varying(10)` | sí | _Por documentar_ |  |
| 26 | `aula` | `character varying(60)` | sí | _Por documentar_ |  |
| 27 | `estado_aula` | `character varying(20)` | sí | _Por documentar_ |  |
| 28 | `estado_docente` | `character varying(20)` | sí | _Por documentar_ |  |
| 29 | `id_asignatura_sugerido` | `bigint` | sí | SUGERENCIA best-effort por nombre normalizado + semestre. Nunca autoritativa. |  |
| 30 | `importado_en` | `timestamp with time zone` | no | _Por documentar_ |  |
| 31 | `n_candidatos` | `smallint` | sí | Cuántas asignaturas del catálogo coinciden por nombre normalizado. >1 significa que la sugerencia se dejó en NULL a propósito. |  |

## programacion_periodo

_Por documentar._

- Clave primaria: `id_periodo_academico`
- Filas: 0
- Referencia a: `id_periodo_academico` → `academic_work_plan.periodo_academico` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_periodo_academico` | `bigint` | no | _Por documentar_ | PK FK→academic_work_plan.periodo_academico.id |
| 2 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 3 | `cerrada_en` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 4 | `cerrada_por` | `uuid` | sí | _Por documentar_ |  |
| 5 | `created_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 6 | `updated_at` | `timestamp with time zone` | no | _Por documentar_ |  |
