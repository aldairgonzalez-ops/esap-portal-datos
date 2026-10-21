# Identidad y acceso (`auth`)

Personas, usuarios, roles, permisos, sedes, seccionales y división geopolítica. Contiene la fuente maestra de personas (auth.personas).

23 tablas · 0 vistas · 275 columnas · 9.012 filas · 4 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`acreditaciones_programa`](#acreditaciones_programa) | Tabla | 5 | _Por documentar_ |
| [`cargos`](#cargos) | Tabla | 17 | _Por documentar_ |
| [`carpeta_digital`](#carpeta_digital) | Tabla | 409 | _Por documentar_ |
| [`dependencias`](#dependencias) | Tabla | 7 | Catálogo transversal de dependencias ESAP. Referenciada por travel_expenses.saldos_tiquetes y otros microservicios. |
| [`dependencias_cargos`](#dependencias_cargos) | Tabla | 30 | _Por documentar_ |
| [`documento_carpeta_digital`](#documento_carpeta_digital) | Tabla | 0 | Documentos físicos subidos por la persona en su Carpeta Digital. Une las 3 vistas (portal docente, backoffice carpeta digital, backoffice RUND). |
| [`festivos_colombia`](#festivos_colombia) | Tabla | 18 | _Por documentar_ |
| [`geopolitica`](#geopolitica) | Tabla | 1155 | _Por documentar_ |
| [`migrations_db_log`](#migrations_db_log) | Tabla · apoyo | 1221 | _Por documentar_ |
| [`module`](#module) | Tabla | 23 | _Por documentar_ |
| [`permission`](#permission) | Tabla | 704 | _Por documentar_ |
| [`personas`](#personas) | Tabla | 409 | _Por documentar_ |
| [`programas_academicos`](#programas_academicos) | Tabla | 12 | _Por documentar_ |
| [`registros_calificados`](#registros_calificados) | Tabla | 12 | _Por documentar_ |
| [`role`](#role) | Tabla | 132 | _Por documentar_ |
| [`role_permissions`](#role_permissions) | Tabla | 3112 | _Por documentar_ |
| [`seccionales`](#seccionales) | Tabla | 38 | _Por documentar_ |
| [`sede_cetap_mapping`](#sede_cetap_mapping) | Tabla | 290 | Relaciona una sede histórica con el CETAP académico usado para activación por periodo. |
| [`sedes`](#sedes) | Tabla | 615 | _Por documentar_ |
| [`system_settings`](#system_settings) | Tabla | 1 | _Por documentar_ |
| [`tipo_documento`](#tipo_documento) | Tabla | 4 | _Por documentar_ |
| [`user`](#user) | Tabla | 390 | _Por documentar_ |
| [`user_roles`](#user_roles) | Tabla | 408 | _Por documentar_ |

## acreditaciones_programa

_Por documentar._

- Clave primaria: `id`
- Filas: 5
- Referencia a: `programa_id` → `auth.programas_academicos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | _Por documentar_ | PK |
| 2 | `programa_id` | `bigint` | no | _Por documentar_ | FK→auth.programas_academicos.id |
| 3 | `tipo` | `text` | no | _Por documentar_ |  |
| 4 | `vigencia` | `date` | no | _Por documentar_ |  |
| 5 | `creado_en` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 6 | `actualizado_en` | `timestamp without time zone` | sí | _Por documentar_ |  |

## cargos

_Por documentar._

- Clave primaria: `id_cargo`
- Filas: 17

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_cargo` | `bigint` | no | _Por documentar_ | PK |
| 2 | `cod_cargo` | `character varying(50)` | no | _Por documentar_ | única |
| 3 | `nom_cargo` | `character varying(250)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `character varying(500)` | sí | _Por documentar_ |  |
| 5 | `nivel_jerarquico` | `character varying(50)` | sí | _Por documentar_ |  |
| 6 | `activo` | `boolean` | no | _Por documentar_ |  |
| 7 | `creado_en` | `timestamp without time zone` | no | _Por documentar_ |  |
| 8 | `actualizado_en` | `timestamp without time zone` | no | _Por documentar_ |  |

## carpeta_digital

_Por documentar._

- Clave primaria: `id_carpeta_digital`
- Filas: 409
- Referencia a: `persona_id` → `auth.personas` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_carpeta_digital` | `uuid` | no | _Por documentar_ | PK |
| 2 | `persona_id` | `uuid` | no | _Por documentar_ | única FK→auth.personas.id_person |
| 3 | `nombre_carpeta` | `character varying(255)` | sí | _Por documentar_ |  |
| 4 | `estado` | `character varying(30)` | no | _Por documentar_ |  |
| 5 | `metadata` | `jsonb` | sí | _Por documentar_ |  |
| 6 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 7 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |

## dependencias

Catálogo transversal de dependencias ESAP. Referenciada por travel_expenses.saldos_tiquetes y otros microservicios.

- Clave primaria: `id_dependencia`
- Filas: 7
- Relaciones implícitas: `id_sede` ↝ `auth.sedes` (100.0 % con padre)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_dependencia` | `numeric(11,0)` | no | _Por documentar_ | PK |
| 2 | `id_empresa` | `numeric(11,0)` | no | _Por documentar_ |  |
| 3 | `cod_dependencia` | `character varying(20)` | no | _Por documentar_ | única |
| 4 | `nom_dependencia` | `character varying(250)` | no | _Por documentar_ |  |
| 5 | `dir_dependencia` | `character varying(250)` | sí | _Por documentar_ |  |
| 6 | `dir_email` | `character varying(250)` | sí | _Por documentar_ |  |
| 7 | `url_dependencia` | `character varying(250)` | sí | _Por documentar_ |  |
| 8 | `id_geopolitica` | `numeric(11,0)` | sí | _Por documentar_ |  |
| 9 | `id_sede` | `numeric(11,0)` | sí | _Por documentar_ | ↝auth.sedes.id_sede |
| 10 | `id_cargo` | `numeric(11,0)` | sí | _Por documentar_ |  |
| 11 | `id_tercero` | `numeric(11,0)` | sí | _Por documentar_ |  |
| 12 | `tip_unidad` | `numeric(1,0)` | sí | _Por documentar_ |  |
| 13 | `gen_tip_unidad` | `character varying(6)` | sí | _Por documentar_ |  |
| 14 | `descripcion` | `character varying(500)` | sí | _Por documentar_ |  |
| 15 | `activo` | `boolean` | no | _Por documentar_ |  |
| 16 | `creado_en` | `timestamp without time zone` | no | _Por documentar_ |  |
| 17 | `actualizado_en` | `timestamp without time zone` | no | _Por documentar_ |  |
| 18 | `sede_umi_id` | `uuid` | sí | FK lógica cross-schema a infrastructure-management.sede.id_sede (UUID). Populada por match de código en migración 020. La columna id_sede numeric original se conserva intacta por backward-compatibility con auth.sedes (vacía a sep-2026). |  |

## dependencias_cargos

_Por documentar._

- Clave primaria: `id_dependencia_cargo`
- Filas: 30
- Referencia a: `id_cargo` → `auth.cargos` (0..* → 1); `id_dependencia` → `auth.dependencias` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_dependencia_cargo` | `bigint` | no | _Por documentar_ | PK |
| 2 | `id_dependencia` | `numeric(11,0)` | no | _Por documentar_ | FK→auth.dependencias.id_dependencia |
| 3 | `id_cargo` | `bigint` | no | _Por documentar_ | FK→auth.cargos.id_cargo |
| 4 | `activo` | `boolean` | no | _Por documentar_ |  |
| 5 | `creado_en` | `timestamp without time zone` | no | _Por documentar_ |  |
| 6 | `actualizado_en` | `timestamp without time zone` | no | _Por documentar_ |  |

## documento_carpeta_digital

Documentos físicos subidos por la persona en su Carpeta Digital. Une las 3 vistas (portal docente, backoffice carpeta digital, backoffice RUND).

- Clave primaria: `id_documento`
- Filas: 0
- Referencia a: `carpeta_digital_id` → `auth.carpeta_digital` (0..1 → 1); `tipo_documento_id` → `auth.tipo_documento` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_documento` | `uuid` | no | _Por documentar_ | PK |
| 2 | `carpeta_digital_id` | `uuid` | no | _Por documentar_ | FK→auth.carpeta_digital.id_carpeta_digital |
| 3 | `tipo_documento_id` | `uuid` | sí | _Por documentar_ | FK→auth.tipo_documento.id_tipo_documento |
| 4 | `rund_soporte_id` | `uuid` | sí | Enlace OPCIONAL al soporte RUND en academic_work_plan.RundSoporteCampo. Cross-schema, no es FK física. |  |
| 5 | `nombre` | `character varying(255)` | no | _Por documentar_ |  |
| 6 | `categoria` | `character varying(80)` | no | _Por documentar_ |  |
| 7 | `tipo_archivo` | `character varying(40)` | sí | _Por documentar_ |  |
| 8 | `tamano_bytes` | `bigint` | sí | _Por documentar_ |  |
| 9 | `url_archivo` | `text` | no | Ruta relativa del archivo (gateway-friendly), ej: /pta/api/v1/uploads/carpeta-digital/{nombre}/{tipo}/{file} |  |
| 10 | `estado` | `character varying(30)` | no | _Por documentar_ |  |
| 11 | `comentarios` | `text` | sí | _Por documentar_ |  |
| 12 | `validado_por` | `uuid` | sí | _Por documentar_ |  |
| 13 | `fecha_validacion` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 14 | `fecha_subida` | `timestamp without time zone` | no | _Por documentar_ |  |
| 15 | `fecha_vencimiento` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 16 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 17 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |

## festivos_colombia

_Por documentar._

- Clave primaria: `id`
- Filas: 18

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | _Por documentar_ | PK |
| 2 | `fecha` | `date` | no | _Por documentar_ | única |
| 3 | `descripcion` | `character varying(150)` | no | _Por documentar_ |  |
| 4 | `origen` | `character varying(150)` | sí | _Por documentar_ |  |
| 5 | `regla` | `character varying(50)` | sí | _Por documentar_ |  |
| 6 | `creado_en` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 7 | `actualizado_en` | `timestamp without time zone` | sí | _Por documentar_ |  |

## geopolitica

_Por documentar._

- Clave primaria: `id_geopolitica`
- Filas: 1155
- Referencia a: `id_padre` → `auth.geopolitica` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_geopolitica` | `bigint` | no | _Por documentar_ | PK |
| 2 | `cod_geopolitica` | `character varying(20)` | no | _Por documentar_ |  |
| 3 | `cod_pais` | `smallint` | sí | _Por documentar_ |  |
| 4 | `cod_departamento` | `smallint` | sí | _Por documentar_ |  |
| 5 | `cod_ciudad` | `smallint` | sí | _Por documentar_ |  |
| 6 | `nom_div_geopolitica` | `character varying(250)` | sí | _Por documentar_ |  |
| 7 | `num_habitantes` | `bigint` | sí | _Por documentar_ |  |
| 8 | `tip_division` | `character varying(6)` | sí | _Por documentar_ |  |
| 9 | `cod_division` | `character varying(6)` | sí | _Por documentar_ |  |
| 10 | `cod_zon_geografica` | `character varying(6)` | sí | _Por documentar_ |  |
| 11 | `fec_ult_act` | `date` | sí | _Por documentar_ |  |
| 12 | `fec_creacion` | `date` | sí | _Por documentar_ |  |
| 13 | `usu_creacion` | `character varying(20)` | sí | _Por documentar_ |  |
| 14 | `usu_actualizacion` | `character varying(20)` | sí | _Por documentar_ |  |
| 15 | `cod_intl_pais` | `character varying(3)` | sí | _Por documentar_ |  |
| 16 | `cod_unso` | `character varying(3)` | sí | _Por documentar_ |  |
| 17 | `cod_dian` | `character varying(3)` | sí | _Por documentar_ |  |
| 18 | `cod_lat` | `numeric(11,8)` | sí | _Por documentar_ |  |
| 19 | `cod_lon` | `numeric(11,8)` | sí | _Por documentar_ |  |
| 20 | `id_padre` | `bigint` | sí | _Por documentar_ | FK→auth.geopolitica.id_geopolitica |
| 21 | `cod_idioma` | `character varying(3)` | sí | _Por documentar_ |  |
| 22 | `nom_idioma` | `character varying(250)` | sí | _Por documentar_ |  |
| 23 | `cod_idm` | `character varying(3)` | sí | _Por documentar_ |  |
| 24 | `nom_div_geopolitica_tot` | `character varying(200)` | sí | _Por documentar_ |  |
| 25 | `cod_are_tel` | `character varying(6)` | sí | _Por documentar_ |  |
| 26 | `cod_pais_defecto` | `character varying(3)` | sí | _Por documentar_ |  |
| 27 | `ind_oculto` | `smallint` | no | _Por documentar_ |  |

## migrations_db_log

_Por documentar._

- Clave primaria: `filename`
- Filas: 1221

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `filename` | `text` | no | _Por documentar_ | PK |
| 2 | `executed_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## module

_Por documentar._

- Clave primaria: `id_module`
- Filas: 23

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_module` | `uuid` | no | _Por documentar_ | PK |
| 2 | `code` | `character varying(50)` | no | _Por documentar_ | única |
| 3 | `name` | `character varying(100)` | no | _Por documentar_ |  |
| 4 | `description` | `text` | sí | _Por documentar_ |  |
| 5 | `icon` | `character varying(50)` | sí | _Por documentar_ |  |
| 6 | `color` | `character varying(20)` | sí | _Por documentar_ |  |
| 7 | `display_order` | `integer` | sí | _Por documentar_ |  |
| 8 | `category` | `character varying(30)` | no | _Por documentar_ |  |
| 9 | `is_active` | `boolean` | sí | _Por documentar_ |  |
| 10 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 11 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |

## permission

_Por documentar._

- Clave primaria: `id_permission`
- Filas: 704
- Referencia a: `id_module` → `auth.module` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_permission` | `uuid` | no | _Por documentar_ | PK |
| 2 | `code` | `character varying(100)` | no | _Por documentar_ | única |
| 3 | `name` | `character varying(150)` | no | _Por documentar_ |  |
| 4 | `description` | `text` | sí | _Por documentar_ |  |
| 5 | `id_module` | `uuid` | no | _Por documentar_ | FK→auth.module.id_module |
| 6 | `is_active` | `boolean` | sí | _Por documentar_ |  |
| 7 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 8 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |

## personas

_Por documentar._

- Clave primaria: no declarada
- Filas: 409
- Referencia a: `id_cargo` → `auth.cargos` (0..1 → 0..1); `id_dependencia` → `auth.dependencias` (0..* → 0..1); `id_seccional` → `auth.seccionales` (0..* → 0..1); `id_sede` → `auth.sedes` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `num_identificacion` | `character varying(30)` | no | _Por documentar_ | Identificación |
| 2 | `tip_identificacion` | `character varying(6)` | no | _Por documentar_ |  |
| 3 | `nom_largo` | `character varying(1000)` | no | _Por documentar_ | Nombre de persona |
| 4 | `nom_tercero` | `character varying(250)` | no | _Por documentar_ | Nombre de persona |
| 5 | `pri_apellido` | `character varying(250)` | sí | _Por documentar_ | Nombre de persona |
| 6 | `seg_apellido` | `character varying(250)` | sí | _Por documentar_ | Nombre de persona |
| 7 | `gen_tercero` | `character varying(6)` | no | _Por documentar_ | Dato personal |
| 8 | `fec_nacimiento` | `date` | sí | _Por documentar_ |  |
| 9 | `dir_residencia` | `character varying(250)` | sí | _Por documentar_ | Contacto |
| 10 | `dir_email` | `character varying(100)` | sí | _Por documentar_ | Contacto |
| 11 | `tel_celular` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 12 | `fec_creacion` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 13 | `fec_modificacion` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 14 | `usu_creacion` | `character varying(20)` | sí | _Por documentar_ |  |
| 15 | `usu_modificacion` | `character varying(20)` | sí | _Por documentar_ |  |
| 16 | `id_seccional` | `bigint` | sí | _Por documentar_ | FK→auth.seccionales.id_seccional |
| 17 | `id_sede` | `bigint` | sí | _Por documentar_ | FK→auth.sedes.id_sede |
| 18 | `id_person` | `uuid` | no | _Por documentar_ | única |
| 19 | `id_dependencia` | `bigint` | sí | _Por documentar_ | FK→auth.dependencias.id_dependencia |
| 20 | `id_cargo` | `bigint` | sí | _Por documentar_ | FK→auth.cargos.id_cargo |
| 21 | `city` | `character varying(255)` | sí | _Por documentar_ |  |

## programas_academicos

_Por documentar._

- Clave primaria: `id`
- Filas: 12
- Referencia a: `sede_id` → `auth.sedes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | _Por documentar_ | PK |
| 2 | `codigo` | `text` | no | _Por documentar_ | única |
| 3 | `nombre` | `text` | no | _Por documentar_ |  |
| 4 | `nivel_formacion` | `text` | no | _Por documentar_ |  |
| 5 | `modalidad` | `text` | no | _Por documentar_ |  |
| 6 | `jornada` | `text` | no | _Por documentar_ |  |
| 7 | `duracion_semestres` | `integer` | no | _Por documentar_ |  |
| 8 | `creditos` | `integer` | no | _Por documentar_ |  |
| 9 | `sede_id` | `integer` | no | _Por documentar_ | FK→auth.sedes.id_sede |
| 10 | `facultad` | `text` | sí | _Por documentar_ |  |
| 11 | `estado` | `text` | no | _Por documentar_ |  |
| 12 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 13 | `perfil_egresado` | `text` | sí | _Por documentar_ |  |
| 14 | `requisitos_ingreso` | `text[]` | sí | _Por documentar_ |  |
| 15 | `costo_matricula` | `numeric(14,2)` | sí | _Por documentar_ |  |
| 16 | `estudiantes_activos` | `integer` | sí | _Por documentar_ |  |
| 17 | `graduados` | `integer` | sí | _Por documentar_ |  |
| 18 | `docentes_asignados` | `integer` | sí | _Por documentar_ |  |
| 19 | `fecha_creacion` | `date` | sí | _Por documentar_ |  |
| 20 | `ultima_actualizacion` | `date` | sí | _Por documentar_ |  |
| 21 | `creado_en` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 22 | `actualizado_en` | `timestamp without time zone` | sí | _Por documentar_ |  |

## registros_calificados

_Por documentar._

- Clave primaria: `id`
- Filas: 12
- Referencia a: `programa_id` → `auth.programas_academicos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | _Por documentar_ | PK |
| 2 | `programa_id` | `bigint` | no | _Por documentar_ | única FK→auth.programas_academicos.id |
| 3 | `numero` | `text` | no | _Por documentar_ |  |
| 4 | `fecha_emision` | `date` | no | _Por documentar_ |  |
| 5 | `vigencia` | `date` | no | _Por documentar_ |  |
| 6 | `creado_en` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 7 | `actualizado_en` | `timestamp without time zone` | sí | _Por documentar_ |  |

## role

_Por documentar._

- Clave primaria: `id`
- Filas: 132

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `code` | `character varying(50)` | no | _Por documentar_ | única |
| 3 | `name` | `character varying(100)` | no | _Por documentar_ | única |
| 4 | `description` | `text` | sí | _Por documentar_ |  |
| 5 | `category` | `character varying(20)` | no | _Por documentar_ |  |
| 6 | `icon` | `character varying(50)` | sí | _Por documentar_ |  |
| 7 | `color` | `character varying(20)` | sí | _Por documentar_ |  |
| 8 | `type` | `character varying(20)` | sí | _Por documentar_ |  |
| 9 | `is_active` | `boolean` | sí | _Por documentar_ |  |
| 10 | `requires_2fa` | `boolean` | sí | _Por documentar_ |  |
| 11 | `created_by` | `character varying(100)` | sí | _Por documentar_ |  |
| 12 | `updated_by` | `character varying(100)` | sí | _Por documentar_ |  |
| 13 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 14 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 15 | `sistema_destino` | `text` | sí | _Por documentar_ |  |
| 16 | `alcance` | `jsonb` | sí | _Por documentar_ |  |

## role_permissions

_Por documentar._

- Clave primaria: `id_rol`, `id_permission`
- Filas: 3112
- Referencia a: `id_permission` → `auth.permission` (0..* → 1); `id_rol` → `auth.role` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_rol` | `uuid` | no | _Por documentar_ | PK FK→auth.role.id |
| 2 | `id_permission` | `uuid` | no | _Por documentar_ | PK FK→auth.permission.id_permission |
| 3 | `is_active` | `boolean` | sí | _Por documentar_ |  |
| 4 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 5 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |

## seccionales

_Por documentar._

- Clave primaria: `id_seccional`
- Filas: 38
- Referencia a: `id_ubi_seccional` → `auth.geopolitica` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_seccional` | `bigint` | no | _Por documentar_ | PK |
| 2 | `nom_seccional` | `character varying(100)` | no | _Por documentar_ |  |
| 3 | `dir_seccional` | `character varying(250)` | sí | _Por documentar_ |  |
| 4 | `id_ubi_seccional` | `bigint` | sí | _Por documentar_ | FK→auth.geopolitica.id_geopolitica |
| 5 | `fec_creacion` | `date` | sí | _Por documentar_ |  |
| 6 | `fec_ult_act` | `date` | sí | _Por documentar_ |  |
| 7 | `usu_creacion` | `character varying(20)` | sí | _Por documentar_ |  |
| 8 | `usu_actualizacion` | `character varying(20)` | sí | _Por documentar_ |  |
| 9 | `cod_seccional` | `character varying(20)` | sí | _Por documentar_ |  |
| 10 | `id_empresa` | `bigint` | sí | _Por documentar_ |  |
| 11 | `nit_seccional` | `character varying(15)` | sí | _Por documentar_ |  |
| 12 | `fir_seccional1` | `bigint` | sí | _Por documentar_ |  |
| 13 | `fir_seccional2` | `bigint` | sí | _Por documentar_ |  |
| 14 | `fir_seccional3` | `bigint` | sí | _Por documentar_ |  |
| 15 | `fir_seccional4` | `bigint` | sí | _Por documentar_ |  |
| 16 | `id_dep_fir_cer1` | `bigint` | sí | _Por documentar_ |  |
| 17 | `id_dep_fir_cer2` | `bigint` | sí | _Por documentar_ |  |
| 18 | `id_dep_fir_cer3` | `bigint` | sí | _Por documentar_ |  |
| 19 | `id_dep_fir_cer4` | `bigint` | sí | _Por documentar_ |  |

## sede_cetap_mapping

Relaciona una sede histórica con el CETAP académico usado para activación por periodo.

- Clave primaria: `id_sede`
- Filas: 290
- Referencia a: `id_cetap` → `academic_work_plan.cetap` (0..1 → 1); `id_sede` → `auth.sedes` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_sede` | `bigint` | no | _Por documentar_ | PK FK→auth.sedes.id_sede |
| 2 | `id_cetap` | `bigint` | no | _Por documentar_ | FK→academic_work_plan.cetap.id |
| 3 | `origen` | `character varying(20)` | no | _Por documentar_ |  |
| 4 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 5 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |

## sedes

_Por documentar._

- Clave primaria: `id_sede`
- Filas: 615
- Referencia a: `id_geopolitica` → `auth.geopolitica` (0..* → 1); `id_seccional` → `auth.seccionales` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_sede` | `bigint` | no | _Por documentar_ | PK |
| 2 | `id_empresa` | `bigint` | no | _Por documentar_ |  |
| 3 | `cod_sede` | `character varying(20)` | no | _Por documentar_ |  |
| 4 | `nom_sede` | `character varying(50)` | no | _Por documentar_ |  |
| 5 | `id_geopolitica` | `bigint` | no | _Por documentar_ | FK→auth.geopolitica.id_geopolitica |
| 6 | `dir_sede` | `character varying(250)` | sí | _Por documentar_ |  |
| 7 | `fec_ult_act` | `date` | sí | _Por documentar_ |  |
| 8 | `fec_creacion` | `date` | sí | _Por documentar_ |  |
| 9 | `usu_creacion` | `character varying(20)` | sí | _Por documentar_ |  |
| 10 | `usu_actualizacion` | `character varying(20)` | sí | _Por documentar_ |  |
| 11 | `cod_atributo` | `character varying(10)` | sí | _Por documentar_ |  |
| 12 | `id_seccional` | `bigint` | sí | _Por documentar_ | FK→auth.seccionales.id_seccional |
| 13 | `sede_act` | `character varying(30)` | sí | _Por documentar_ |  |
| 14 | `num_latitud` | `numeric(32,29)` | sí | _Por documentar_ |  |
| 15 | `num_longitud` | `numeric(32,29)` | sí | _Por documentar_ |  |
| 16 | `tel_sede` | `character varying(50)` | sí | _Por documentar_ |  |
| 17 | `email_sede` | `character varying(100)` | sí | _Por documentar_ |  |
| 18 | `capacidad_estudiantes` | `integer` | sí | _Por documentar_ |  |
| 19 | `capacidad_docentes` | `integer` | sí | _Por documentar_ |  |
| 20 | `permite_inscripciones` | `boolean` | sí | _Por documentar_ |  |
| 21 | `permite_matriculas` | `boolean` | sí | _Por documentar_ |  |
| 22 | `visible_portal` | `boolean` | sí | _Por documentar_ |  |
| 23 | `observaciones` | `text` | sí | _Por documentar_ |  |

## system_settings

_Por documentar._

- Clave primaria: `key`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `key` | `character varying(100)` | no | _Por documentar_ | PK |
| 2 | `value` | `text` | sí | _Por documentar_ |  |
| 3 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## tipo_documento

_Por documentar._

- Clave primaria: `id_tipo_documento`
- Filas: 4
- Referencia a: `carpeta_digital_id` → `auth.carpeta_digital` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_tipo_documento` | `uuid` | no | _Por documentar_ | PK |
| 2 | `carpeta_digital_id` | `uuid` | sí | _Por documentar_ | FK→auth.carpeta_digital.id_carpeta_digital |
| 3 | `nombre` | `character varying(150)` | no | Nombre del documento requerido configurado, por ejemplo Cedula, Hoja de vida o Certificado laboral. |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `categoria` | `character varying(80)` | no | Categoria funcional del documento: personal, academico, laboral, certificados, administrativo u otros. |  |
| 6 | `icono` | `character varying(80)` | no | _Por documentar_ |  |
| 7 | `color` | `character varying(20)` | no | _Por documentar_ |  |
| 8 | `obligatorio` | `boolean` | no | _Por documentar_ |  |
| 9 | `requiere_validacion` | `boolean` | no | _Por documentar_ |  |
| 10 | `formatos_permitidos` | `text[]` | no | _Por documentar_ |  |
| 11 | `tamano_max_mb` | `integer` | no | _Por documentar_ |  |
| 12 | `activo` | `boolean` | no | _Por documentar_ |  |
| 13 | `es_sistema` | `boolean` | no | _Por documentar_ |  |
| 14 | `rol_validador` | `character varying(120)` | sí | _Por documentar_ |  |
| 15 | `orden` | `integer` | no | _Por documentar_ |  |
| 16 | `asignacion_tipo` | `character varying(40)` | no | _Por documentar_ |  |
| 17 | `asignacion_valor` | `character varying(255)` | sí | _Por documentar_ |  |
| 18 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 19 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |

## user

_Por documentar._

- Clave primaria: `id_user`
- Filas: 390
- Referencia a: `id_person` → `auth.personas` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_user` | `uuid` | no | _Por documentar_ | PK |
| 2 | `username` | `character varying(100)` | no | _Por documentar_ |  |
| 3 | `password_hash` | `character varying(255)` | no | _Por documentar_ | Credencial de acceso |
| 4 | `is_active` | `boolean` | sí | _Por documentar_ |  |
| 5 | `token` | `integer` | sí | _Por documentar_ |  |
| 6 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 7 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 8 | `id_person` | `uuid` | sí | _Por documentar_ | FK→auth.personas.id_person |
| 9 | `password_temp` | `boolean` | sí | _Por documentar_ |  |
| 10 | `token_microsoft` | `character varying(255)` | sí | _Por documentar_ | Credencial de acceso |
| 11 | `2fa` | `boolean` | sí | _Por documentar_ |  |
| 12 | `public_id` | `uuid` | no | _Por documentar_ | única |
| 13 | `signature_otp_context` | `character varying(128)` | sí | _Por documentar_ |  |

## user_roles

_Por documentar._

- Clave primaria: `id_user`, `id_rol`
- Filas: 408
- Referencia a: `id_rol` → `auth.role` (0..* → 1); `id_user` → `auth.user` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_user` | `uuid` | no | _Por documentar_ | PK FK→auth.user.id_user |
| 2 | `id_rol` | `uuid` | no | _Por documentar_ | PK FK→auth.role.id |
| 3 | `is_active` | `boolean` | sí | _Por documentar_ |  |
| 4 | `created_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 5 | `updated_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
