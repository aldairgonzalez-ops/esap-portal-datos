# Identidad y acceso (`auth`)

Personas (fuente maestra), cuentas de usuario, roles, permisos y módulos de la SuperApp, y los catálogos institucionales de sedes, seccionales, dependencias, cargos y división geopolítica.

23 tablas · 0 vistas · 275 columnas · 9.012 filas · 4 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`acreditaciones_programa`](#acreditaciones_programa) | Tabla | 5 | Acreditaciones de los programas académicos. Un registro por acreditación de un programa (auth.programas_academicos), con su tipo (por ejemplo, Alta Calidad o Internacional) y la fecha de vigencia; un programa puede tener más de una. |
| [`cargos`](#cargos) | Tabla | 17 | Catálogo de cargos de la institución. Un registro por cargo, con su código, nombre, descripción, nivel jerárquico y si está activo; se relaciona con las personas (auth.personas) y con las dependencias (auth.dependencias_cargos). |
| [`carpeta_digital`](#carpeta_digital) | Tabla | 409 | Carpetas digitales de las personas. Un registro por carpeta, asociada a una persona de auth.personas, con su nombre, estado y metadatos; agrupa los tipos de documento y los documentos cargados (auth.tipo_documento, auth.documento_carpeta_digital). |
| [`dependencias`](#dependencias) | Tabla | 7 | Catálogo transversal de dependencias ESAP. Referenciada por travel_expenses.saldos_tiquetes y otros microservicios. |
| [`dependencias_cargos`](#dependencias_cargos) | Tabla | 30 | Relación entre dependencias y cargos. Un registro por cada cargo asignado a una dependencia (auth.dependencias, auth.cargos), con la marca de si la asignación está activa. |
| [`documento_carpeta_digital`](#documento_carpeta_digital) | Tabla | 0 | Documentos físicos subidos por la persona en su Carpeta Digital. Une las 3 vistas (portal docente, backoffice carpeta digital, backoffice RUND). |
| [`festivos_colombia`](#festivos_colombia) | Tabla | 18 | Catálogo de los días festivos oficiales de Colombia, de uso transversal en el sistema. Un registro por fecha festiva, con su descripción, origen y regla de cálculo; se usa para computar días hábiles, por ejemplo en las solicitudes de viáticos (RF-PRE-003). |
| [`geopolitica`](#geopolitica) | Tabla | 1155 | Catálogo de la división geopolítica: países, departamentos y ciudades o municipios. Un registro por división, con sus códigos (DANE, DIAN, internacional), nombre, tipo, coordenadas e idioma; cada división puede apuntar a su división padre en la misma tabla y es referenciada por seccionales y sedes. |
| [`migrations_db_log`](#migrations_db_log) | Tabla · apoyo | 1221 | Registro de los archivos de migración de base de datos ejecutados. Un registro por archivo, con la fecha y hora de su ejecución. |
| [`module`](#module) | Tabla | 23 | Catálogo de los módulos funcionales de la aplicación. Un registro por módulo, con su código, nombre, descripción, categoría (backoffice o portal), ícono, color, orden de presentación y estado activo; agrupa los permisos de auth.permission. |
| [`permission`](#permission) | Tabla | 704 | Catálogo de permisos de la aplicación. Un registro por permiso, con su código, nombre, descripción y módulo al que pertenece (auth.module); los permisos se asignan a los roles en auth.role_permissions. |
| [`personas`](#personas) | Tabla | 409 | Registro maestro de las personas del sistema. Un registro por persona, con identificación, nombres y apellidos, datos de contacto, fecha de nacimiento y su ubicación organizacional (seccional, sede, dependencia y cargo); id_person es el identificador con el que la enlazan los usuarios (auth.user) y las tablas de los demás dominios. |
| [`programas_academicos`](#programas_academicos) | Tabla | 12 | Catálogo de programas académicos. Un registro por programa, con código, nombre, nivel de formación, modalidad, jornada, duración, créditos, sede, facultad, estado y cifras de estudiantes, graduados y docentes; se relaciona con sus registros calificados y acreditaciones. |
| [`registros_calificados`](#registros_calificados) | Tabla | 12 | Registros calificados de los programas académicos. Un registro por registro calificado, asociado a un programa de auth.programas_academicos, con su número, fecha de emisión y vigencia. |
| [`role`](#role) | Tabla | 132 | Catálogo de roles de la aplicación. Un registro por rol, con su código, nombre, descripción, categoría, tipo (sistema o personalizado), sistema al que aplica, alcance administrativo y si exige autenticación de dos factores; los roles agrupan permisos (auth.role_permissions) y se asignan a usuarios (auth.user_roles). |
| [`role_permissions`](#role_permissions) | Tabla | 3112 | Asignación de permisos a roles (relación N:M). Un registro por cada permiso (auth.permission) asignado a un rol (auth.role), con la marca de si la asignación está activa. |
| [`seccionales`](#seccionales) | Tabla | 38 | Catálogo de seccionales de la ESAP. Un registro por seccional, con su código, nombre, dirección, NIT, ubicación en la división geopolítica y los firmantes y dependencias firmantes de certificados; agrupa las sedes y se asigna a las personas. |
| [`sede_cetap_mapping`](#sede_cetap_mapping) | Tabla | 290 | Relaciona una sede histórica con el CETAP académico usado para activación por periodo. |
| [`sedes`](#sedes) | Tabla | 615 | Catálogo de sedes de la ESAP. Un registro por sede, con su código, nombre, seccional, ubicación geopolítica, dirección, coordenadas, contacto, capacidad de estudiantes y docentes, estado y si permite inscripciones, matrículas y visibilidad en el portal; se asigna a personas y programas académicos. |
| [`system_settings`](#system_settings) | Tabla | 1 | Parámetros globales del sistema en formato clave-valor. Un registro por parámetro, con su valor y fecha de actualización; se usa, por ejemplo, para el SMMLV o para habilitar el inicio de sesión con correo y contraseña. |
| [`tipo_documento`](#tipo_documento) | Tabla | 4 | Tipos de documento que se configuran para la carpeta digital. Un registro por tipo, con su nombre, categoría, si es obligatorio o requiere validación, el rol validador, los formatos y el tamaño máximo permitidos, y el criterio de asignación a las personas (todos, territorial, seccional, sede o persona). |
| [`user`](#user) | Tabla | 390 | Cuentas de usuario para el acceso al sistema. Un registro por usuario, enlazado a una persona de auth.personas, con su nombre de usuario, contraseña cifrada, estado, identificador público, datos de inicio de sesión con Microsoft y de autenticación de dos factores; los roles del usuario se asignan en auth.user_roles. |
| [`user_roles`](#user_roles) | Tabla | 408 | Asignación de roles a usuarios (relación N:M). Un registro por cada rol (auth.role) asignado a un usuario (auth.user), con la marca de si la asignación está activa. |

## acreditaciones_programa

Acreditaciones de los programas académicos. Un registro por acreditación de un programa (auth.programas_academicos), con su tipo (por ejemplo, Alta Calidad o Internacional) y la fecha de vigencia; un programa puede tener más de una.

- Clave primaria: `id`
- Filas: 5
- Referencia a: `programa_id` → `auth.programas_academicos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | Identificador único del registro en la tabla acreditaciones_programa. Se genera automáticamente. | PK |
| 2 | `programa_id` | `bigint` | no | Referencia al registro de auth.programas_academicos (id). | FK→auth.programas_academicos.id |
| 3 | `tipo` | `text` | no | Tipo de acreditación del programa académico (por ejemplo, Alta Calidad, Internacional). |  |
| 4 | `vigencia` | `date` | no | Fecha hasta la que está vigente la acreditación del programa académico. |  |
| 5 | `creado_en` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 6 | `actualizado_en` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## cargos

Catálogo de cargos de la institución. Un registro por cargo, con su código, nombre, descripción, nivel jerárquico y si está activo; se relaciona con las personas (auth.personas) y con las dependencias (auth.dependencias_cargos).

- Clave primaria: `id_cargo`
- Filas: 17

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_cargo` | `bigint` | no | Identificador único del registro en la tabla cargos. Se genera automáticamente. | PK |
| 2 | `cod_cargo` | `character varying(50)` | no | Código del cargo; es único en la tabla (máximo 50 caracteres). | única |
| 3 | `nom_cargo` | `character varying(250)` | no | Nombre del cargo (máximo 250 caracteres). |  |
| 4 | `descripcion` | `character varying(500)` | sí | Descripción del cargo. |  |
| 5 | `nivel_jerarquico` | `character varying(50)` | sí | Nivel jerárquico del cargo, en texto libre de hasta 50 caracteres. Por defecto, Profesional. |  |
| 6 | `activo` | `boolean` | no | Indica si el cargo está activo. |  |
| 7 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## carpeta_digital

Carpetas digitales de las personas. Un registro por carpeta, asociada a una persona de auth.personas, con su nombre, estado y metadatos; agrupa los tipos de documento y los documentos cargados (auth.tipo_documento, auth.documento_carpeta_digital).

- Clave primaria: `id_carpeta_digital`
- Filas: 409
- Referencia a: `persona_id` → `auth.personas` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_carpeta_digital` | `uuid` | no | Identificador único del registro en la tabla carpeta_digital. Se genera automáticamente. | PK |
| 2 | `persona_id` | `uuid` | no | Referencia al registro de auth.personas (id_person). | única FK→auth.personas.id_person |
| 3 | `nombre_carpeta` | `character varying(255)` | sí | Nombre de la carpeta digital de la persona. |  |
| 4 | `estado` | `character varying(30)` | no | Estado de la carpeta digital de la persona. |  |
| 5 | `metadata` | `jsonb` | sí | Metadatos adicionales de la carpeta digital, en formato JSON. |  |
| 6 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 7 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## dependencias

Catálogo transversal de dependencias ESAP. Referenciada por travel_expenses.saldos_tiquetes y otros microservicios.

- Clave primaria: `id_dependencia`
- Filas: 7
- Relaciones implícitas: `id_sede` ↝ `auth.sedes` (100.0 % con padre)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_dependencia` | `numeric(11,0)` | no | Identificador único del registro en la tabla dependencias. | PK |
| 2 | `id_empresa` | `numeric(11,0)` | no | Identificador de la empresa o entidad a la que pertenece la dependencia; el sistema asigna el valor 1. |  |
| 3 | `cod_dependencia` | `character varying(20)` | no | Código de la dependencia; es único en la tabla (máximo 20 caracteres). | única |
| 4 | `nom_dependencia` | `character varying(250)` | no | Nombre de la dependencia (máximo 250 caracteres). |  |
| 5 | `dir_dependencia` | `character varying(250)` | sí | Dirección de la dependencia, en texto de hasta 250 caracteres. |  |
| 6 | `dir_email` | `character varying(250)` | sí | Correo electrónico institucional de la dependencia. |  |
| 7 | `url_dependencia` | `character varying(250)` | sí | Dirección web (URL) de la dependencia. |  |
| 8 | `id_geopolitica` | `numeric(11,0)` | sí | Identificador de la división geopolítica donde se ubica la dependencia (auth.geopolitica.id_geopolitica); se verifica su existencia al crear o actualizar la dependencia. |  |
| 9 | `id_sede` | `numeric(11,0)` | sí | Sede a la que pertenece la dependencia; referencia a sedes (id_sede) sin llave foránea declarada. | ↝auth.sedes.id_sede |
| 10 | `id_cargo` | `numeric(11,0)` | sí | Identificador del cargo asociado a la dependencia (auth.cargos.id_cargo). |  |
| 11 | `id_tercero` | `numeric(11,0)` | sí | Identificador de la persona responsable de la dependencia (auth.personas.id_tercero). |  |
| 12 | `tip_unidad` | `numeric(1,0)` | sí | Código numérico (un dígito) del tipo de unidad organizacional de la dependencia. |  |
| 13 | `gen_tip_unidad` | `character varying(6)` | sí | Código de la lista genérica que define los tipos de unidad. Por defecto, TIUORG. |  |
| 14 | `descripcion` | `character varying(500)` | sí | Descripción de la dependencia. |  |
| 15 | `activo` | `boolean` | no | Indica si la dependencia está activa. |  |
| 16 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 17 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 18 | `sede_umi_id` | `uuid` | sí | FK lógica cross-schema a infrastructure-management.sede.id_sede (UUID). Populada por match de código en migración 020. La columna id_sede numeric original se conserva intacta por backward-compatibility con auth.sedes (vacía a sep-2026). |  |

## dependencias_cargos

Relación entre dependencias y cargos. Un registro por cada cargo asignado a una dependencia (auth.dependencias, auth.cargos), con la marca de si la asignación está activa.

- Clave primaria: `id_dependencia_cargo`
- Filas: 30
- Referencia a: `id_cargo` → `auth.cargos` (0..* → 1); `id_dependencia` → `auth.dependencias` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_dependencia_cargo` | `bigint` | no | Identificador único del registro en la tabla dependencias_cargos. Se genera automáticamente. | PK |
| 2 | `id_dependencia` | `numeric(11,0)` | no | Referencia al registro de auth.dependencias (id_dependencia). | FK→auth.dependencias.id_dependencia |
| 3 | `id_cargo` | `bigint` | no | Referencia al registro de auth.cargos (id_cargo). | FK→auth.cargos.id_cargo |
| 4 | `activo` | `boolean` | no | Indica si la asignación del cargo a la dependencia está activa. |  |
| 5 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 6 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## documento_carpeta_digital

Documentos físicos subidos por la persona en su Carpeta Digital. Une las 3 vistas (portal docente, backoffice carpeta digital, backoffice RUND).

- Clave primaria: `id_documento`
- Filas: 0
- Referencia a: `carpeta_digital_id` → `auth.carpeta_digital` (0..1 → 1); `tipo_documento_id` → `auth.tipo_documento` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_documento` | `uuid` | no | Identificador único del registro en la tabla documento_carpeta_digital. Se genera automáticamente. | PK |
| 2 | `carpeta_digital_id` | `uuid` | no | Referencia al registro de auth.carpeta_digital (id_carpeta_digital). | FK→auth.carpeta_digital.id_carpeta_digital |
| 3 | `tipo_documento_id` | `uuid` | sí | Referencia al registro de auth.tipo_documento (id_tipo_documento). | FK→auth.tipo_documento.id_tipo_documento |
| 4 | `rund_soporte_id` | `uuid` | sí | Enlace OPCIONAL al soporte RUND en academic_work_plan.RundSoporteCampo. Cross-schema, no es FK física. |  |
| 5 | `nombre` | `character varying(255)` | no | Nombre original del archivo subido a la Carpeta Digital. Para los soportes del RUND se usa el nombre del archivo del soporte. |  |
| 6 | `categoria` | `character varying(80)` | no | Categoría del documento en la Carpeta Digital, en texto. Por defecto, otros; los soportes del RUND usan rund. |  |
| 7 | `tipo_archivo` | `character varying(40)` | sí | Extensión del archivo subido, en minúsculas y sin punto (por ejemplo, pdf). Si no se puede obtener, pdf. |  |
| 8 | `tamano_bytes` | `bigint` | sí | Tamaño en bytes del archivo cargado en la carpeta digital. |  |
| 9 | `url_archivo` | `text` | no | Ruta relativa del archivo (gateway-friendly), ej: /pta/api/v1/uploads/carpeta-digital/{nombre}/{tipo}/{file} |  |
| 10 | `estado` | `character varying(30)` | no | Estado de validación del documento. Valores permitidos: pendiente, validado, rechazado, vencido; por defecto pendiente. |  |
| 11 | `comentarios` | `text` | sí | Comentarios sobre el documento: al subirlo, la descripción que escribe quien lo carga; al validarlo o rechazarlo, el comentario de quien valida, que reemplaza al anterior. En los soportes del RUND, la observación del soporte. |  |
| 12 | `validado_por` | `uuid` | sí | Usuario que realizó la validación. |  |
| 13 | `fecha_validacion` | `timestamp without time zone` | sí | Fecha y hora en que se validó el documento de la carpeta digital. |  |
| 14 | `fecha_subida` | `timestamp without time zone` | no | Fecha y hora en que la persona cargó el documento; por defecto el momento de creación. |  |
| 15 | `fecha_vencimiento` | `timestamp without time zone` | sí | Fecha y hora de vencimiento del documento de la carpeta digital. |  |
| 16 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 17 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## festivos_colombia

Catálogo de los días festivos oficiales de Colombia, de uso transversal en el sistema. Un registro por fecha festiva, con su descripción, origen y regla de cálculo; se usa para computar días hábiles, por ejemplo en las solicitudes de viáticos (RF-PRE-003).

- Clave primaria: `id`
- Filas: 18

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla festivos_colombia. Se genera automáticamente. | PK |
| 2 | `fecha` | `date` | no | Fecha del día festivo; es única en la tabla. | única |
| 3 | `descripcion` | `character varying(150)` | no | Descripción del día festivo. |  |
| 4 | `origen` | `character varying(150)` | sí | Fuente del festivo: la que informa el calendario nacional al sincronizar (por defecto, Ley 51/1983) o «Manual / Ajuste Interno» cuando se registra a mano. |  |
| 5 | `regla` | `character varying(50)` | sí | Regla con la que se determina la fecha del festivo, tomada del calendario nacional al sincronizar. Por defecto, fixed (fecha fija). |  |
| 6 | `creado_en` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 7 | `actualizado_en` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## geopolitica

Catálogo de la división geopolítica: países, departamentos y ciudades o municipios. Un registro por división, con sus códigos (DANE, DIAN, internacional), nombre, tipo, coordenadas e idioma; cada división puede apuntar a su división padre en la misma tabla y es referenciada por seccionales y sedes.

- Clave primaria: `id_geopolitica`
- Filas: 1155
- Referencia a: `id_padre` → `auth.geopolitica` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_geopolitica` | `bigint` | no | Identificador único del registro en la tabla geopolitica. | PK |
| 2 | `cod_geopolitica` | `character varying(20)` | no | Código de la división geopolítica. |  |
| 3 | `cod_pais` | `smallint` | sí | Código del país de la división geopolítica. |  |
| 4 | `cod_departamento` | `smallint` | sí | Código DANE del departamento de la división geopolítica; permite listar las ciudades de cada departamento. |  |
| 5 | `cod_ciudad` | `smallint` | sí | Código de la ciudad o municipio de la división geopolítica. |  |
| 6 | `nom_div_geopolitica` | `character varying(250)` | sí | Nombre de la división geopolítica. |  |
| 7 | `num_habitantes` | `bigint` | sí | Número de habitantes de la división geopolítica. |  |
| 8 | `tip_division` | `character varying(6)` | sí | Código del tipo de división geopolítica: DEPTO para departamentos y CIUDAD para ciudades o municipios. |  |
| 9 | `cod_division` | `character varying(6)` | sí | Código de la clase de división geopolítica. |  |
| 10 | `cod_zon_geografica` | `character varying(6)` | sí | Código de la zona geográfica a la que pertenece la división. |  |
| 11 | `fec_ult_act` | `date` | sí | Fecha de la última actualización del registro. |  |
| 12 | `fec_creacion` | `date` | sí | Fecha de creación del registro. |  |
| 13 | `usu_creacion` | `character varying(20)` | sí | Usuario que creó el registro. |  |
| 14 | `usu_actualizacion` | `character varying(20)` | sí | Usuario que hizo la última actualización del registro. |  |
| 15 | `cod_intl_pais` | `character varying(3)` | sí | Código internacional del país (tres caracteres). |  |
| 16 | `cod_unso` | `character varying(3)` | sí | Código del país de tres caracteres; su codificación está por confirmar. |  |
| 17 | `cod_dian` | `character varying(3)` | sí | Código del país o división asignado por la DIAN. |  |
| 18 | `cod_lat` | `numeric(11,8)` | sí | Latitud geográfica de la división, en grados decimales. |  |
| 19 | `cod_lon` | `numeric(11,8)` | sí | Longitud geográfica de la división, en grados decimales. |  |
| 20 | `id_padre` | `bigint` | sí | Referencia al registro de auth.geopolitica (id_geopolitica). | FK→auth.geopolitica.id_geopolitica |
| 21 | `cod_idioma` | `character varying(3)` | sí | Código del idioma principal de la división geopolítica. |  |
| 22 | `nom_idioma` | `character varying(250)` | sí | Nombre del idioma principal de la división geopolítica. |  |
| 23 | `cod_idm` | `character varying(3)` | sí | Código de idioma abreviado de la división geopolítica. |  |
| 24 | `nom_div_geopolitica_tot` | `character varying(200)` | sí | Nombre completo de la división geopolítica. |  |
| 25 | `cod_are_tel` | `character varying(6)` | sí | Código de área telefónica (indicativo) de la división geopolítica. |  |
| 26 | `cod_pais_defecto` | `character varying(3)` | sí | Código del país por defecto asociado a la división geopolítica. |  |
| 27 | `ind_oculto` | `smallint` | no | Indicador numérico de si la división geopolítica se oculta. Por defecto, 0. |  |

## migrations_db_log

Registro de los archivos de migración de base de datos ejecutados. Un registro por archivo, con la fecha y hora de su ejecución.

- Clave primaria: `filename`
- Filas: 1221

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `filename` | `text` | no | Clave primaria de la tabla migrations_db_log: filename. | PK |
| 2 | `executed_at` | `timestamp without time zone` | sí | Fecha y hora en que se ejecutó el archivo de migración. Por defecto, la fecha y hora del registro. |  |

## module

Catálogo de los módulos funcionales de la aplicación. Un registro por módulo, con su código, nombre, descripción, categoría (backoffice o portal), ícono, color, orden de presentación y estado activo; agrupa los permisos de auth.permission.

- Clave primaria: `id_module`
- Filas: 23

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_module` | `uuid` | no | Identificador único del registro en la tabla module. Se genera automáticamente. | PK |
| 2 | `code` | `character varying(50)` | no | Código del módulo, único en la tabla; la aplicación lo valida con seis dígitos. | única |
| 3 | `name` | `character varying(100)` | no | Nombre del módulo. |  |
| 4 | `description` | `text` | sí | Descripción del módulo. |  |
| 5 | `icon` | `character varying(50)` | sí | Nombre del ícono con que se muestra el módulo en la interfaz. Por defecto, Shield. |  |
| 6 | `color` | `character varying(20)` | sí | Color del módulo en la interfaz, en formato hexadecimal. Por defecto, #003DA5. |  |
| 7 | `display_order` | `integer` | sí | Posición del módulo en las listas de presentación. Por defecto, 0. |  |
| 8 | `category` | `character varying(30)` | no | Categoría del módulo según la aplicación donde se presenta. Valores previstos: backoffice, portal; por defecto backoffice. |  |
| 9 | `is_active` | `boolean` | sí | Indica si el módulo está activo. |  |
| 10 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 11 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## permission

Catálogo de permisos de la aplicación. Un registro por permiso, con su código, nombre, descripción y módulo al que pertenece (auth.module); los permisos se asignan a los roles en auth.role_permissions.

- Clave primaria: `id_permission`
- Filas: 704
- Referencia a: `id_module` → `auth.module` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_permission` | `uuid` | no | Identificador único del registro en la tabla permission. Se genera automáticamente. | PK |
| 2 | `code` | `character varying(100)` | no | Código del permiso, único en la tabla; la aplicación lo valida con seis dígitos. | única |
| 3 | `name` | `character varying(150)` | no | Nombre del permiso. |  |
| 4 | `description` | `text` | sí | Descripción del permiso. |  |
| 5 | `id_module` | `uuid` | no | Referencia al registro de auth.module (id_module). | FK→auth.module.id_module |
| 6 | `is_active` | `boolean` | sí | Indica si el permiso está activo. |  |
| 7 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 8 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## personas

Registro maestro de las personas del sistema. Un registro por persona, con identificación, nombres y apellidos, datos de contacto, fecha de nacimiento y su ubicación organizacional (seccional, sede, dependencia y cargo); id_person es el identificador con el que la enlazan los usuarios (auth.user) y las tablas de los demás dominios.

- Clave primaria: no declarada
- Filas: 409
- Referencia a: `id_cargo` → `auth.cargos` (0..1 → 0..1); `id_dependencia` → `auth.dependencias` (0..* → 0..1); `id_seccional` → `auth.seccionales` (0..* → 0..1); `id_sede` → `auth.sedes` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `num_identificacion` | `character varying(30)` | no | Número de identificación de la persona. | Identificación |
| 2 | `tip_identificacion` | `character varying(6)` | no | Código del tipo de documento de identidad de la persona, en mayúsculas. Para CC, CE y TI se valida la longitud del número. |  |
| 3 | `nom_largo` | `character varying(1000)` | no | Nombre completo de la persona, formado por el sistema al unir nom_tercero (nombres) y pri_apellido (primer apellido) con un espacio. Se recalcula cuando cambian los nombres o el apellido. | Nombre de persona |
| 4 | `nom_tercero` | `character varying(250)` | no | Nombres de la persona, sin apellidos. El apellido se guarda en pri_apellido. | Nombre de persona |
| 5 | `pri_apellido` | `character varying(250)` | sí | Primer apellido de la persona. | Nombre de persona |
| 6 | `seg_apellido` | `character varying(250)` | sí | Segundo apellido de la persona. | Nombre de persona |
| 7 | `gen_tercero` | `character varying(6)` | no | Código del género de la persona, en mayúsculas. Si no se informa, N (no especificado). | Dato personal |
| 8 | `fec_nacimiento` | `date` | sí | Fecha de nacimiento de la persona. | Dato personal |
| 9 | `dir_residencia` | `character varying(250)` | sí | Dirección de residencia de la persona. | Contacto |
| 10 | `dir_email` | `character varying(100)` | sí | Correo electrónico de la persona, guardado en minúsculas. | Contacto |
| 11 | `tel_celular` | `character varying(255)` | sí | Número de teléfono celular de la persona. | Contacto |
| 12 | `fec_creacion` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. Por defecto, la fecha y hora del registro. |  |
| 13 | `fec_modificacion` | `timestamp with time zone` | sí | Fecha y hora de la última modificación del registro. |  |
| 14 | `usu_creacion` | `character varying(20)` | sí | Usuario que creó el registro. |  |
| 15 | `usu_modificacion` | `character varying(20)` | sí | Usuario que hizo la última modificación del registro. |  |
| 16 | `id_seccional` | `bigint` | sí | Referencia al registro de auth.seccionales (id_seccional). | FK→auth.seccionales.id_seccional |
| 17 | `id_sede` | `bigint` | sí | Referencia al registro de auth.sedes (id_sede). | FK→auth.sedes.id_sede |
| 18 | `id_person` | `uuid` | no | Identificador único (UUID) de la persona, usado por las demás tablas para enlazarla; se genera automáticamente. | única |
| 19 | `id_dependencia` | `bigint` | sí | Referencia al registro de auth.dependencias (id_dependencia). | FK→auth.dependencias.id_dependencia |
| 20 | `id_cargo` | `bigint` | sí | Referencia al registro de auth.cargos (id_cargo). | FK→auth.cargos.id_cargo |
| 21 | `city` | `character varying(255)` | sí | Ciudad de la persona, en texto libre. |  |

## programas_academicos

Catálogo de programas académicos. Un registro por programa, con código, nombre, nivel de formación, modalidad, jornada, duración, créditos, sede, facultad, estado y cifras de estudiantes, graduados y docentes; se relaciona con sus registros calificados y acreditaciones.

- Clave primaria: `id`
- Filas: 12
- Referencia a: `sede_id` → `auth.sedes` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | Identificador único del registro en la tabla programas_academicos. Se genera automáticamente. | PK |
| 2 | `codigo` | `text` | no | Código del programa académico, único en la tabla. | única |
| 3 | `nombre` | `text` | no | Nombre del programa académico. |  |
| 4 | `nivel_formacion` | `text` | no | Nivel de formación del programa (por ejemplo, Pregrado, Especialización, Maestría, Doctorado). |  |
| 5 | `modalidad` | `text` | no | Modalidad del programa (por ejemplo, Presencial, Virtual, Distancia, Dual). |  |
| 6 | `jornada` | `text` | no | Jornada del programa (por ejemplo, Diurna, Nocturna, Mixta, Flexible). |  |
| 7 | `duracion_semestres` | `integer` | no | Duración del programa académico, en semestres. |  |
| 8 | `creditos` | `integer` | no | Número total de créditos académicos del programa. |  |
| 9 | `sede_id` | `integer` | no | Referencia al registro de auth.sedes (id_sede). | FK→auth.sedes.id_sede |
| 10 | `facultad` | `text` | sí | Facultad a la que pertenece el programa, en texto. |  |
| 11 | `estado` | `text` | no | Estado del programa académico. |  |
| 12 | `descripcion` | `text` | sí | Descripción del programa académico. |  |
| 13 | `perfil_egresado` | `text` | sí | Descripción del perfil del egresado del programa. |  |
| 14 | `requisitos_ingreso` | `text[]` | sí | Lista de requisitos de ingreso al programa. |  |
| 15 | `costo_matricula` | `numeric(14,2)` | sí | Valor de la matrícula del programa. |  |
| 16 | `estudiantes_activos` | `integer` | sí | Número de estudiantes activos en el programa. Por defecto, 0. |  |
| 17 | `graduados` | `integer` | sí | Número de graduados del programa. Por defecto, 0. |  |
| 18 | `docentes_asignados` | `integer` | sí | Número de docentes asignados al programa. Por defecto, 0. |  |
| 19 | `fecha_creacion` | `date` | sí | Fecha y hora de creación del registro. |  |
| 20 | `ultima_actualizacion` | `date` | sí | Fecha de actualización de la información del programa; toma la fecha actual al crear el registro y no se actualiza automáticamente. actualizado_en, en cambio, lo actualiza un trigger en cada modificación. |  |
| 21 | `creado_en` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 22 | `actualizado_en` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## registros_calificados

Registros calificados de los programas académicos. Un registro por registro calificado, asociado a un programa de auth.programas_academicos, con su número, fecha de emisión y vigencia.

- Clave primaria: `id`
- Filas: 12
- Referencia a: `programa_id` → `auth.programas_academicos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | Identificador único del registro en la tabla registros_calificados. Se genera automáticamente. | PK |
| 2 | `programa_id` | `bigint` | no | Referencia al registro de auth.programas_academicos (id). | única FK→auth.programas_academicos.id |
| 3 | `numero` | `text` | no | Número del registro calificado del programa académico. |  |
| 4 | `fecha_emision` | `date` | no | Fecha de emisión del registro calificado. |  |
| 5 | `vigencia` | `date` | no | Fecha hasta la que está vigente el registro calificado. |  |
| 6 | `creado_en` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 7 | `actualizado_en` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## role

Catálogo de roles de la aplicación. Un registro por rol, con su código, nombre, descripción, categoría, tipo (sistema o personalizado), sistema al que aplica, alcance administrativo y si exige autenticación de dos factores; los roles agrupan permisos (auth.role_permissions) y se asignan a usuarios (auth.user_roles).

- Clave primaria: `id`
- Filas: 132

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla role. | PK |
| 2 | `code` | `character varying(50)` | no | Código técnico único del rol, de seis dígitos, usado por el sistema. | única |
| 3 | `name` | `character varying(100)` | no | Nombre único del rol que se muestra en la interfaz. | única |
| 4 | `description` | `text` | sí | Descripción del rol. |  |
| 5 | `category` | `character varying(20)` | no | Categoría del rol. Valores admitidos: backoffice, portal, sistema, academico, directivo y administrativo. Por defecto, sistema. |  |
| 6 | `icon` | `character varying(50)` | sí | Nombre del ícono del rol en la interfaz; por defecto Shield. |  |
| 7 | `color` | `character varying(20)` | sí | Color del rol en la interfaz, en código hexadecimal; por defecto #003DA5. |  |
| 8 | `type` | `character varying(20)` | sí | Tipo de rol. Valores previstos: sistema, personalizado; por defecto personalizado. |  |
| 9 | `is_active` | `boolean` | sí | Indica si el rol está activo. |  |
| 10 | `requires_2fa` | `boolean` | sí | Indica si el rol requiere autenticación de dos factores; por defecto falso. |  |
| 11 | `created_by` | `character varying(100)` | sí | Usuario que creó el registro. |  |
| 12 | `updated_by` | `character varying(100)` | sí | Usuario que realizó la última actualización del registro. |  |
| 13 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 14 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 15 | `sistema_destino` | `text` | sí | Sistema al que aplica el rol: Backoffice, Portal o Ambos. Por defecto, Backoffice. |  |
| 16 | `alcance` | `jsonb` | sí | Configuración del alcance administrativo del rol, en formato JSON. |  |

## role_permissions

Asignación de permisos a roles (relación N:M). Un registro por cada permiso (auth.permission) asignado a un rol (auth.role), con la marca de si la asignación está activa.

- Clave primaria: `id_rol`, `id_permission`
- Filas: 3112
- Referencia a: `id_permission` → `auth.permission` (0..* → 1); `id_rol` → `auth.role` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_rol` | `uuid` | no | Identificador único del registro en la tabla role_permissions. | PK FK→auth.role.id |
| 2 | `id_permission` | `uuid` | no | Identificador único del registro en la tabla role_permissions. | PK FK→auth.permission.id_permission |
| 3 | `is_active` | `boolean` | sí | Indica si la asignación del permiso al rol está activa. |  |
| 4 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 5 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## seccionales

Catálogo de seccionales de la ESAP. Un registro por seccional, con su código, nombre, dirección, NIT, ubicación en la división geopolítica y los firmantes y dependencias firmantes de certificados; agrupa las sedes y se asigna a las personas.

- Clave primaria: `id_seccional`
- Filas: 38
- Referencia a: `id_ubi_seccional` → `auth.geopolitica` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_seccional` | `bigint` | no | Identificador único del registro en la tabla seccionales. | PK |
| 2 | `nom_seccional` | `character varying(100)` | no | Nombre de la seccional (máximo 100 caracteres). |  |
| 3 | `dir_seccional` | `character varying(250)` | sí | Dirección física de la seccional. |  |
| 4 | `id_ubi_seccional` | `bigint` | sí | Referencia al registro de auth.geopolitica (id_geopolitica). | FK→auth.geopolitica.id_geopolitica |
| 5 | `fec_creacion` | `date` | sí | Fecha de creación del registro. |  |
| 6 | `fec_ult_act` | `date` | sí | Fecha de la última actualización del registro. |  |
| 7 | `usu_creacion` | `character varying(20)` | sí | Usuario que creó el registro. La carga de estructura organizacional escribe el valor sistema. |  |
| 8 | `usu_actualizacion` | `character varying(20)` | sí | Usuario que hizo la última actualización del registro. La carga de estructura organizacional escribe el valor sistema. |  |
| 9 | `cod_seccional` | `character varying(20)` | sí | Código de la seccional (máximo 20 caracteres). |  |
| 10 | `id_empresa` | `bigint` | sí | Identificador de la empresa o entidad a la que pertenece la seccional. |  |
| 11 | `nit_seccional` | `character varying(15)` | sí | Número de identificación tributaria (NIT) de la seccional. |  |
| 12 | `fir_seccional1` | `bigint` | sí | Identificador del firmante 1 asociado a la seccional para la expedición de documentos. |  |
| 13 | `fir_seccional2` | `bigint` | sí | Identificador del firmante 2 asociado a la seccional para la expedición de documentos. |  |
| 14 | `fir_seccional3` | `bigint` | sí | Identificador del firmante 3 asociado a la seccional para la expedición de documentos. |  |
| 15 | `fir_seccional4` | `bigint` | sí | Identificador del firmante 4 asociado a la seccional para la expedición de documentos. |  |
| 16 | `id_dep_fir_cer1` | `bigint` | sí | Identificador de la dependencia del firmante 1 de certificados de la seccional. |  |
| 17 | `id_dep_fir_cer2` | `bigint` | sí | Identificador de la dependencia del firmante 2 de certificados de la seccional. |  |
| 18 | `id_dep_fir_cer3` | `bigint` | sí | Identificador de la dependencia del firmante 3 de certificados de la seccional. |  |
| 19 | `id_dep_fir_cer4` | `bigint` | sí | Identificador de la dependencia del firmante 4 de certificados de la seccional. |  |

## sede_cetap_mapping

Relaciona una sede histórica con el CETAP académico usado para activación por periodo.

- Clave primaria: `id_sede`
- Filas: 290
- Referencia a: `id_cetap` → `academic_work_plan.cetap` (0..1 → 1); `id_sede` → `auth.sedes` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_sede` | `bigint` | no | Identificador único del registro en la tabla sede_cetap_mapping. | PK FK→auth.sedes.id_sede |
| 2 | `id_cetap` | `bigint` | no | Referencia al registro de academic_work_plan.cetap (id). | FK→academic_work_plan.cetap.id |
| 3 | `origen` | `character varying(20)` | no | Origen de la relación entre la sede y el CETAP. Valores permitidos: legacy, official. Por defecto, official. |  |
| 4 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 5 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## sedes

Catálogo de sedes de la ESAP. Un registro por sede, con su código, nombre, seccional, ubicación geopolítica, dirección, coordenadas, contacto, capacidad de estudiantes y docentes, estado y si permite inscripciones, matrículas y visibilidad en el portal; se asigna a personas y programas académicos.

- Clave primaria: `id_sede`
- Filas: 615
- Referencia a: `id_geopolitica` → `auth.geopolitica` (0..* → 1); `id_seccional` → `auth.seccionales` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_sede` | `bigint` | no | Identificador único del registro en la tabla sedes. | PK |
| 2 | `id_empresa` | `bigint` | no | Identificador de la empresa o entidad a la que pertenece la sede. Los servicios siempre asignan 1. |  |
| 3 | `cod_sede` | `character varying(20)` | no | Código de la sede (máximo 20 caracteres). |  |
| 4 | `nom_sede` | `character varying(50)` | no | Nombre de la sede (máximo 50 caracteres). |  |
| 5 | `id_geopolitica` | `bigint` | no | Referencia al registro de auth.geopolitica (id_geopolitica). | FK→auth.geopolitica.id_geopolitica |
| 6 | `dir_sede` | `character varying(250)` | sí | Dirección física de la sede. |  |
| 7 | `fec_ult_act` | `date` | sí | Fecha de la última actualización del registro. |  |
| 8 | `fec_creacion` | `date` | sí | Fecha de creación del registro. |  |
| 9 | `usu_creacion` | `character varying(20)` | sí | Usuario que creó el registro. La carga de estructura organizacional escribe el valor sistema. |  |
| 10 | `usu_actualizacion` | `character varying(20)` | sí | Usuario que hizo la última actualización del registro. La carga de estructura organizacional escribe el valor sistema. |  |
| 11 | `cod_atributo` | `character varying(10)` | sí | Código de atributo de la sede, de hasta 10 caracteres. Cuando la carga de estructura reemplaza el código de la sede por el del CETAP, guarda aquí el código anterior si el campo está vacío. |  |
| 12 | `id_seccional` | `bigint` | sí | Referencia al registro de auth.seccionales (id_seccional). | FK→auth.seccionales.id_seccional |
| 13 | `sede_act` | `character varying(30)` | sí | Estado de la sede: ACTIVO o INACTIVO (también se reconocen ACTIVA e INACTIVA). |  |
| 14 | `num_latitud` | `numeric(32,29)` | sí | Latitud geográfica de la sede, en grados decimales. |  |
| 15 | `num_longitud` | `numeric(32,29)` | sí | Longitud geográfica de la sede, en grados decimales. |  |
| 16 | `tel_sede` | `character varying(50)` | sí | Número de teléfono de contacto de la sede. |  |
| 17 | `email_sede` | `character varying(100)` | sí | Correo electrónico de contacto de la sede. |  |
| 18 | `capacidad_estudiantes` | `integer` | sí | Número de estudiantes que puede atender la sede. Se suma en los totales de capacidad de la estructura organizacional. |  |
| 19 | `capacidad_docentes` | `integer` | sí | Número de docentes que puede atender la sede. Se suma en los totales de capacidad de la estructura organizacional. |  |
| 20 | `permite_inscripciones` | `boolean` | sí | Indica si la sede permite inscripciones. Por defecto, verdadero. |  |
| 21 | `permite_matriculas` | `boolean` | sí | Indica si la sede permite matrículas. Por defecto, verdadero. |  |
| 22 | `visible_portal` | `boolean` | sí | Indica si la sede se muestra en el portal. Por defecto, verdadero. |  |
| 23 | `observaciones` | `text` | sí | Observaciones registradas sobre la sede. |  |

## system_settings

Parámetros globales del sistema en formato clave-valor. Un registro por parámetro, con su valor y fecha de actualización; se usa, por ejemplo, para el SMMLV o para habilitar el inicio de sesión con correo y contraseña.

- Clave primaria: `key`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `key` | `character varying(100)` | no | Clave primaria de la tabla system_settings: key. | PK |
| 2 | `value` | `text` | sí | Valor del parámetro global identificado por key (por ejemplo, el SMMLV), en texto de 1 a 100 caracteres. |  |
| 3 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## tipo_documento

Tipos de documento que se configuran para la carpeta digital. Un registro por tipo, con su nombre, categoría, si es obligatorio o requiere validación, el rol validador, los formatos y el tamaño máximo permitidos, y el criterio de asignación a las personas (todos, territorial, seccional, sede o persona).

- Clave primaria: `id_tipo_documento`
- Filas: 4
- Referencia a: `carpeta_digital_id` → `auth.carpeta_digital` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_tipo_documento` | `uuid` | no | Identificador único del registro en la tabla tipo_documento. Se genera automáticamente. | PK |
| 2 | `carpeta_digital_id` | `uuid` | sí | Referencia al registro de auth.carpeta_digital (id_carpeta_digital). | FK→auth.carpeta_digital.id_carpeta_digital |
| 3 | `nombre` | `character varying(150)` | no | Nombre del documento requerido configurado, por ejemplo Cedula, Hoja de vida o Certificado laboral. |  |
| 4 | `descripcion` | `text` | sí | Descripción del tipo de documento. |  |
| 5 | `categoria` | `character varying(80)` | no | Categoria funcional del documento: personal, academico, laboral, certificados, administrativo u otros. |  |
| 6 | `icono` | `character varying(80)` | no | Nombre del ícono con que se muestra el tipo de documento en la interfaz. Por defecto, file-text. |  |
| 7 | `color` | `character varying(20)` | no | Color del tipo de documento en la interfaz, en formato hexadecimal. Por defecto, #2962FF. |  |
| 8 | `obligatorio` | `boolean` | no | Indica si el tipo de documento es obligatorio en la carpeta digital. |  |
| 9 | `requiere_validacion` | `boolean` | no | Indica si los documentos de este tipo requieren validación. |  |
| 10 | `formatos_permitidos` | `text[]` | no | Lista de formatos de archivo permitidos para el tipo de documento. Por defecto, pdf. |  |
| 11 | `tamano_max_mb` | `integer` | no | Tamaño máximo del archivo permitido para el tipo de documento, en megabytes. Por defecto, 10. |  |
| 12 | `activo` | `boolean` | no | Indica si el tipo de documento está activo. |  |
| 13 | `es_sistema` | `boolean` | no | Indica si el tipo de documento es del sistema. |  |
| 14 | `rol_validador` | `character varying(120)` | sí | Rol encargado de validar los documentos de este tipo, registrado como texto. |  |
| 15 | `orden` | `integer` | no | Posición del tipo de documento en el ordenamiento de la lista. |  |
| 16 | `asignacion_tipo` | `character varying(40)` | no | Criterio con que se asigna el tipo de documento a las personas: todos, territorial, seccional, sede o persona. Por defecto, todos. |  |
| 17 | `asignacion_valor` | `character varying(255)` | sí | Valor del criterio de asignación del tipo de documento: identificador, nombre o código de la seccional (territorial o seccional) o de la sede (sede), o identificador, número de identificación o correo de la persona (persona). Se compara sin distinguir mayúsculas; vacío aplica a todos. |  |
| 18 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 19 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## user

Cuentas de usuario para el acceso al sistema. Un registro por usuario, enlazado a una persona de auth.personas, con su nombre de usuario, contraseña cifrada, estado, identificador público, datos de inicio de sesión con Microsoft y de autenticación de dos factores; los roles del usuario se asignan en auth.user_roles.

- Clave primaria: `id_user`
- Filas: 390
- Referencia a: `id_person` → `auth.personas` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_user` | `uuid` | no | Identificador único del registro en la tabla user. | PK |
| 2 | `username` | `character varying(100)` | no | Nombre de usuario con el que la persona inicia sesión. |  |
| 3 | `password_hash` | `character varying(255)` | no | Contraseña del usuario cifrada con una función de hash. | Credencial de acceso |
| 4 | `is_active` | `boolean` | sí | Indica si el usuario está activo. |  |
| 5 | `token` | `integer` | sí | Código numérico de seis dígitos de un solo uso que se envía al correo del usuario para recuperar la contraseña o firmar un documento. Vence a los 10 minutos (recuperación) o 5 minutos (firma) desde la última actualización del usuario y se borra al usarse. |  |
| 6 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 7 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 8 | `id_person` | `uuid` | sí | Referencia al registro de auth.personas (id_person). | FK→auth.personas.id_person |
| 9 | `password_temp` | `boolean` | sí | Indica si la contraseña del usuario es temporal. |  |
| 10 | `token_microsoft` | `character varying(255)` | sí | Identificador de objeto (oid) de la cuenta Microsoft del usuario, registrado al iniciar sesión con Microsoft. No guarda el token de acceso ni el de actualización. | Credencial de acceso |
| 11 | `2fa` | `boolean` | sí | Indica si el usuario tiene habilitada la autenticación de dos factores. |  |
| 12 | `public_id` | `uuid` | no | Identificador público (UUID) del usuario, único y generado automáticamente; la API lo expone en lugar de id_user, salvo para servicios internos, y lo usa para buscar al usuario. | única |
| 13 | `signature_otp_context` | `character varying(128)` | sí | Contexto del código de un solo uso (OTP) de firma de documento, con formato paz-y-salvo:<identificador del paz y salvo>:<hash SHA-256 del contenido>. Vacío cuando el código es de recuperación de contraseña; se borra al usar el código. |  |

## user_roles

Asignación de roles a usuarios (relación N:M). Un registro por cada rol (auth.role) asignado a un usuario (auth.user), con la marca de si la asignación está activa.

- Clave primaria: `id_user`, `id_rol`
- Filas: 408
- Referencia a: `id_rol` → `auth.role` (0..* → 1); `id_user` → `auth.user` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id_user` | `uuid` | no | Identificador único del registro en la tabla user_roles. | PK FK→auth.user.id_user |
| 2 | `id_rol` | `uuid` | no | Identificador único del registro en la tabla user_roles. | PK FK→auth.role.id |
| 3 | `is_active` | `boolean` | sí | Indica si la asignación del rol al usuario está activa. |  |
| 4 | `created_at` | `timestamp with time zone` | sí | Fecha y hora de creación del registro. |  |
| 5 | `updated_at` | `timestamp with time zone` | sí | Fecha y hora de la última actualización del registro. |  |
