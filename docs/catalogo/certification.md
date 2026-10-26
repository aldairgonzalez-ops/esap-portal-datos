# Certificaciones laborales (`certification`)

Certificados laborales: solicitudes de los servidores, certificados emitidos con código QR y su validación, perfiles y funciones de los cargos, bonificación técnica, plantillas, firmantes y solicitudes de corrección.

13 tablas · 0 vistas · 208 columnas · 15.908 filas · 0 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`certificate_correction_requests`](#certificate_correction_requests) | Tabla | 9 | Employee correction requests and coordinator resolutions for labor certificates |
| [`certificate_requests`](#certificate_requests) | Tabla | 15250 | Labor certificate requests submitted by employees |
| [`certificate_template_config`](#certificate_template_config) | Tabla | 3 | Labor-certificate template configuration |
| [`certificate_templates`](#certificate_templates) | Tabla | 1 | HTML templates used to generate certificates |
| [`certificate_validations`](#certificate_validations) | Tabla | 42 | Labor-certificate validation history |
| [`certificates`](#certificates) | Tabla | 130 | Labor certificates generated with a QR verification code |
| [`labor_function_profiles`](#labor_function_profiles) | Tabla | 19 | Position profiles imported from Matriz Funciones ESAP and used to associate employees by normalized codes and organizational context |
| [`labor_functions`](#labor_functions) | Tabla | 190 | Normalized, ordered labor functions belonging to a position profile |
| [`signers`](#signers) | Tabla | 1 | Authorized signers captured on issued certificates |
| [`technical_bonus_assignments`](#technical_bonus_assignments) | Tabla | 53 | Technical-bonus percentage assignments by employee and category |
| [`technical_bonus_templates`](#technical_bonus_templates) | Tabla | 3 | Paragraph templates for technical-bonus sections in labor certificates |
| [`template_config_changes`](#template_config_changes) | Tabla | 206 | Certificate-template configuration change history |
| [`template_signers`](#template_signers) | Tabla | 1 | Signers available for labor-certificate templates |

## certificate_correction_requests

Employee correction requests and coordinator resolutions for labor certificates

- Clave primaria: `id`
- Filas: 9
- Referencia a: `certificate_id` → `certification.certificates` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla certificate_correction_requests. Se genera automáticamente. | PK |
| 2 | `request_number` | `character varying(50)` | no | Número de la solicitud de corrección; es único en la tabla. | única |
| 3 | `certificate_id` | `uuid` | no | Referencia al registro de certification.certificates (id). | FK→certification.certificates.id |
| 4 | `status` | `character varying(20)` | no | Estado de la solicitud de corrección del certificado laboral (APPROVED, IN_REVIEW, PENDING o REJECTED). |  |
| 5 | `description` | `text` | no | Descripción de la corrección solicitada para el certificado laboral. |  |
| 6 | `requester_name` | `character varying(255)` | no | Nombre de la persona que solicita la corrección del certificado. |  |
| 7 | `requester_email` | `character varying(255)` | no | Correo electrónico de la persona que solicita la corrección del certificado. | Contacto |
| 8 | `submitted_evidence` | `jsonb` | no | Archivos de evidencia presentados por el solicitante con la solicitud de corrección, en formato JSON: lista con nombre original, nombre almacenado, tipo MIME, tamaño y ruta relativa de cada archivo (hasta tres). Por defecto, una lista vacía. |  |
| 9 | `certificate_snapshot` | `jsonb` | no | Immutable snapshot of the certificate when the correction was submitted |  |
| 10 | `due_date` | `date` | no | Maximum response date calculated as fifteen business days after submission |  |
| 11 | `reviewed_by_id` | `uuid` | sí | Identificador del usuario (auth.user.id_user) del coordinador que revisa o resuelve la solicitud de corrección, tomado del token de sesión o de la cabecera x-user-id. |  |
| 12 | `reviewed_by_name` | `character varying(255)` | sí | Nombre del coordinador que revisa la solicitud de corrección. |  |
| 13 | `reviewed_by_email` | `character varying(255)` | sí | Correo electrónico del coordinador que revisa la solicitud de corrección. | Contacto |
| 14 | `review_started_at` | `timestamp without time zone` | sí | Fecha y hora en que inició la revisión de la solicitud de corrección. |  |
| 15 | `resolution_description` | `text` | sí | Descripción de la resolución del coordinador sobre la solicitud de corrección. |  |
| 16 | `resolution_evidence` | `jsonb` | no | Archivos de evidencia de la resolución de la solicitud de corrección, en formato JSON: lista con nombre original, nombre almacenado, tipo MIME, tamaño y ruta relativa de cada archivo (hasta dos). Por defecto, una lista vacía. |  |
| 17 | `corrected_data` | `jsonb` | sí | Datos completos del certificado después de aplicar la corrección aprobada, en formato JSON (instantánea del certificado, no solo los campos modificados). |  |
| 18 | `resolved_at` | `timestamp without time zone` | sí | Fecha y hora en que se resolvió la solicitud de corrección. |  |
| 19 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 20 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 21 | `traceability` | `jsonb` | no | Chronological and immutable business audit trail for the correction request |  |

## certificate_requests

Labor certificate requests submitted by employees

- Clave primaria: `id`
- Filas: 15250

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla certificate_requests. Se genera automáticamente. | PK |
| 2 | `request_number` | `character varying(50)` | no | Unique request number format: 12_620_700_20_CD 001 | única |
| 3 | `person_id` | `uuid` | sí | Identificador opcional de la persona que solicita el certificado laboral. Queda vacío en las solicitudes sincronizadas desde Oracle. |  |
| 4 | `full_name` | `character varying(255)` | no | Nombre completo del empleado (dato DATA1 del certificado). | Nombre de persona |
| 5 | `id_number` | `character varying(50)` | no | Número de identificación del empleado (dato DATA2 del certificado). |  |
| 6 | `career_category` | `character varying(100)` | no | DATA3: Administrative Career, Free Appointment, etc. |  |
| 7 | `hiring_date` | `date` | no | Fecha de vinculación del empleado, correspondiente al inicio del contrato (dato DATA4 del certificado). |  |
| 8 | `position_category` | `character varying(100)` | no | DATA5: TITULAR Teacher, OCCASIONAL, CHAIR |  |
| 9 | `position_location` | `character varying(150)` | sí | Ciudad de ubicación del cargo (dato DATA6 del certificado). |  |
| 10 | `monthly_salary` | `numeric(12,2)` | no | DATA7: Monthly salary in number |  |
| 11 | `salary_text` | `character varying(255)` | sí | DATA8: Salary in text (forty forty-five pesos m/cte) |  |
| 12 | `department` | `character varying(255)` | sí | Dependencia o dirección territorial del empleado (por ejemplo, Dirección Territorial Bogotá). |  |
| 13 | `campus` | `character varying(100)` | sí | Sede del empleado (por ejemplo, Sede Central, Bogotá D.C.). |  |
| 14 | `email` | `character varying(100)` | sí | Correo electrónico del solicitante del certificado laboral. | Contacto |
| 15 | `phone` | `character varying(20)` | sí | Número de teléfono del solicitante del certificado laboral. | Contacto |
| 16 | `status` | `character varying(50)` | no | Estado de la solicitud del certificado laboral. Valores previstos: PENDING, APPROVED, REJECTED, GENERATED; por defecto PENDING. |  |
| 17 | `request_date` | `timestamp without time zone` | sí | Fecha y hora de la solicitud del certificado. Por defecto, la fecha y hora del registro. |  |
| 18 | `observations` | `text` | sí | Observaciones sobre la solicitud del certificado laboral. |  |
| 19 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 20 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 21 | `validation_code` | `character varying(10)` | sí | Código de seis dígitos que se envía al correo del empleado para confirmar su identidad en el autoservicio antes de generar el certificado laboral. Vence a los 15 minutos (validation_expires_at) y se borra al usarse o si falla el envío. |  |
| 22 | `validation_expires_at` | `timestamp without time zone` | sí | Fecha y hora de vencimiento del código de validación. |  |
| 23 | `position_code` | `character varying(255)` | sí | Position code received from the authoritative human-resources source |  |
| 24 | `grade_code` | `character varying(255)` | sí | Position grade code received from the authoritative human-resources source |  |
| 25 | `document_type` | `character varying(10)` | sí | Document type provided through labor-certificate self-service (CC, CE, PP) |  |
| 26 | `base_position_code` | `character varying(20)` | sí | Código del cargo base del empleado, sin el grado: se toma de CODIGO_CARGO_BASE o CODIGO_EMPLEO de Oracle o se deriva de COD_CARGO quitando el grado. position_code guarda el código del cargo tal como llega de la fuente. |  |
| 27 | `hierarchical_level` | `character varying(100)` | sí | Nivel jerárquico del cargo del empleado. |  |
| 28 | `position_name` | `character varying(255)` | sí | Nombre del cargo del empleado. |  |
| 29 | `organization_department` | `character varying(500)` | sí | Dependencia de la estructura organizacional del empleado (DEPENDENCIA en Oracle). Es la primera fuente de la variable [DEPENDENCIA] del certificado; department puede guardar el centro de costo en las filas de Oracle. |  |
| 30 | `internal_group` | `character varying(500)` | sí | Grupo interno de trabajo al que pertenece el empleado. |  |
| 31 | `cost_center` | `character varying(255)` | sí | Centro de costo al que está asociado el empleado. |  |

## certificate_template_config

Labor-certificate template configuration

- Clave primaria: `id`
- Filas: 3
- Referencia a: `signer_id` → `certification.template_signers` (1..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla certificate_template_config. Se genera automáticamente. | PK |
| 2 | `signer_id` | `uuid` | sí | Reference to the signer assigned to this template | FK→certification.template_signers.id |
| 3 | `entity_logo_url` | `text` | sí | URL of the institutional ESAP logo |  |
| 4 | `entity_logo_filename` | `character varying(255)` | sí | Nombre del archivo del logo de la entidad usado en la plantilla del certificado. |  |
| 5 | `entity_logo_size` | `character varying(50)` | sí | Tamaño del archivo del logo de la entidad en la plantilla del certificado, en texto con la unidad KB (N/D si no se conoce). |  |
| 6 | `typography_font` | `character varying(100)` | sí | Font family applied to the certificate |  |
| 7 | `signer_title` | `text` | sí | Signer title displayed in the certificate heading |  |
| 8 | `certificate_content_html` | `text` | sí | Certificate HTML content with dynamic placeholders |  |
| 9 | `version` | `character varying(20)` | sí | Versión de la configuración de la plantilla del certificado laboral. |  |
| 10 | `status` | `character varying(50)` | sí | Estado de la configuración de la plantilla del certificado laboral. |  |
| 11 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 13 | `created_by` | `character varying(255)` | sí | Usuario que creó el registro. |  |
| 14 | `updated_by` | `character varying(255)` | sí | Usuario que realizó la última actualización del registro. |  |
| 15 | `is_active` | `boolean` | sí | Indicates whether this configuration is active |  |
| 16 | `template_type` | `character varying(30)` | no | Tipo de plantilla de certificado laboral: docente o administrador. Por defecto, docente. |  |
| 17 | `signature_url` | `text` | sí | Dirección (URL) del archivo de la imagen de la firma usada en el certificado. |  |
| 18 | `signature_filename` | `text` | sí | Nombre del archivo de la imagen de la firma usada en el certificado. |  |
| 19 | `signature_size` | `text` | sí | Tamaño del archivo de la imagen de la firma en el certificado, en texto con la unidad KB. |  |
| 20 | `signer_name_override` | `text` | sí | Nombre del firmante que se muestra en el certificado en lugar del nombre registrado del firmante asociado a signer_id. Vacío para usar el nombre registrado. |  |

## certificate_templates

HTML templates used to generate certificates

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla certificate_templates. Se genera automáticamente. | PK |
| 2 | `name` | `character varying(255)` | no | Nombre de la plantilla HTML de certificado. |  |
| 3 | `description` | `text` | sí | Descripción de la plantilla HTML de certificado. |  |
| 4 | `html_content` | `text` | no | Contenido HTML de la plantilla del certificado, con marcadores como {{NAME}} e {{ID_NUMBER}}. |  |
| 5 | `certificate_type` | `character varying(100)` | sí | Tipo de certificado que genera la plantilla; por defecto LABOR_TEACHER. |  |
| 6 | `is_active` | `boolean` | sí | Indica si la plantilla está activa; por defecto verdadero. |  |
| 7 | `version` | `integer` | sí | Número de versión de la plantilla de certificado. |  |
| 8 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## certificate_validations

Labor-certificate validation history

- Clave primaria: `id`
- Filas: 42
- Referencia a: `certificate_id` → `certification.certificates` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla certificate_validations. Se genera automáticamente. | PK |
| 2 | `certificate_id` | `uuid` | no | Reference to the validated certificate | FK→certification.certificates.id |
| 3 | `validation_date` | `timestamp without time zone` | no | Fecha y hora en que se validó el certificado laboral; por defecto el momento de registro. |  |
| 4 | `ip_address` | `character varying(50)` | sí | Dirección IP desde la que se consultó la validación del certificado. | Identificador en línea (IP) |
| 5 | `user_agent` | `text` | sí | Agente de usuario (navegador) desde el que se consultó la validación del certificado laboral. |  |
| 6 | `location` | `character varying(255)` | sí | Ciudad y país desde donde se validó el certificado. |  |
| 7 | `result` | `character varying(50)` | no | Certificate validation result |  |
| 8 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `country` | `character varying(100)` | sí | Country detected by IP |  |
| 10 | `region` | `character varying(120)` | sí | Region detected by IP |  |
| 11 | `city` | `character varying(120)` | sí | City detected by IP |  |
| 12 | `latitude` | `double precision` | sí | Latitude detected by IP |  |
| 13 | `longitude` | `double precision` | sí | Longitude detected by IP |  |
| 14 | `isp` | `character varying(255)` | sí | Internet service provider |  |

## certificates

Labor certificates generated with a QR verification code

- Clave primaria: `id`
- Filas: 130
- Referencia a: `request_id` → `certification.certificate_requests` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla certificates. Se genera automáticamente. | PK |
| 2 | `verification_code` | `character varying(100)` | no | Código QR único para validar el certificado laboral. | única |
| 3 | `certificate_number` | `character varying(50)` | no | Número oficial único del certificado laboral. | única |
| 4 | `request_id` | `uuid` | no | Referencia al registro de certification.certificate_requests (id). | FK→certification.certificate_requests.id |
| 5 | `full_name` | `character varying(255)` | no | Nombre completo del empleado, copiado en el certificado para conservar el histórico. | Nombre de persona |
| 6 | `id_number` | `character varying(50)` | no | Número de identificación del empleado a quien se expide el certificado laboral. |  |
| 7 | `career_category` | `character varying(100)` | no | Cargo del empleado registrado en el certificado: denominación del cargo seguida del grado (CARGO Grado GRADO en Oracle); NO REGISTRADO si la fuente no lo trae. |  |
| 8 | `hiring_date` | `date` | no | Fecha de vinculación del empleado a la entidad, informada en el certificado laboral. |  |
| 9 | `position_category` | `character varying(100)` | no | Tipo de vinculación del empleado registrado en el certificado: tipo de acto administrativo de Oracle (TIPOACTOADMINISTRATIVO) o, en su defecto, el tipo de vinculación; NO REGISTRADO si la fuente no lo trae. |  |
| 10 | `position_location` | `character varying(150)` | sí | Ubicación del cargo del empleado según el certificado: en las filas de Oracle, la dependencia o, si falta, la sucursal; en las filas locales, el grupo o la dependencia. |  |
| 11 | `monthly_salary` | `numeric(12,2)` | no | Asignación básica mensual del empleado incluida en el certificado (SUELDO_BASICO en Oracle), en pesos; el certificado la imprime redondeada a pesos enteros. |  |
| 12 | `salary_text` | `character varying(255)` | sí | Valor del salario mensual escrito en letras, tal como aparece en el certificado. |  |
| 13 | `department` | `character varying(255)` | sí | Dependencia organizacional del empleado registrada en el certificado; en las filas sincronizadas desde Oracle guarda el centro de costo o, si falta, la dependencia. |  |
| 14 | `campus` | `character varying(100)` | sí | Sede del empleado según el certificado, copiada de la solicitud; se guarda como texto. |  |
| 15 | `issue_date` | `date` | no | Fecha de expedición del certificado. |  |
| 16 | `issuance_timestamp` | `timestamp without time zone` | no | Fecha y hora en que se generó el certificado. |  |
| 17 | `signer_name` | `character varying(255)` | sí | Nombre del firmante del certificado. |  |
| 18 | `signer_position` | `character varying(255)` | sí | Cargo del firmante del certificado (por ejemplo, Director Técnico de Talento Humano). |  |
| 19 | `signer_department` | `character varying(255)` | sí | Dependencia del firmante del certificado, copiada al momento de la expedición. |  |
| 20 | `pdf_url` | `character varying(500)` | sí | Ruta o URL del archivo PDF generado del certificado. |  |
| 21 | `status` | `character varying(50)` | no | Estado del certificado laboral. Valores previstos: VALID, REVOKED, EXPIRED; por defecto VALID. |  |
| 22 | `validation_count` | `integer` | sí | Número de veces que se ha validado el certificado; por defecto 0. |  |
| 23 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 24 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 25 | `position_code` | `character varying(255)` | sí | Position code captured when the certificate was issued |  |
| 26 | `technical_bonus` | `numeric(12,2)` | sí | Valor en pesos de la prima técnica o de coordinación incluida en el certificado: suma, para cada asignación activa de technical_bonus_assignments del empleado, del salario mensual por su porcentaje. El detalle por categoría queda en technical_bonuses; 0 si no aplica. |  |
| 27 | `grade_code` | `character varying(255)` | sí | Position grade code captured when the certificate was issued |  |
| 28 | `template_snapshot` | `jsonb` | sí | Snapshot of the template used to issue the certificate |  |
| 29 | `template_type` | `character varying(20)` | sí | Template type used to issue the certificate |  |
| 30 | `template_version` | `character varying(20)` | sí | Version of the template used to issue the certificate |  |
| 31 | `include_salary` | `boolean` | no | Indicates whether the certificate displays salary information |  |
| 32 | `include_technical_bonus` | `boolean` | no | Indicates whether the certificate displays technical-bonus information |  |
| 33 | `document_type` | `character varying(10)` | sí | Document type stored with the generated labor certificate (CC, CE, PP) |  |
| 34 | `technical_bonus_category` | `character varying(80)` | sí | Technical-bonus category captured when the certificate was issued |  |
| 35 | `technical_bonuses` | `jsonb` | sí | JSON snapshot of technical bonuses included when the certificate was issued |  |
| 36 | `is_corrected` | `boolean` | no | Makes corrected certificate values take precedence over the original HR request snapshot |  |
| 37 | `last_corrected_at` | `timestamp without time zone` | sí | Fecha y hora de la última corrección del certificado. |  |
| 38 | `assignment_type` | `character varying(1)` | sí | Assignment indicator rendered by the labor certificate: E shows the encargo suffix and N omits it |  |
| 39 | `include_functions` | `boolean` | no | Whether the requester selected the option to include labor functions |  |
| 40 | `functions_snapshot` | `jsonb` | sí | Immutable snapshot of the matched profile and ordered functions at issuance time |  |

## labor_function_profiles

Position profiles imported from Matriz Funciones ESAP and used to associate employees by normalized codes and organizational context

- Clave primaria: `id`
- Filas: 19

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla labor_function_profiles. Se genera automáticamente. | PK |
| 2 | `position_code` | `character varying(20)` | sí | Código del cargo del perfil de funciones; las funciones se asignan por id_number (match_key document\|<número>). |  |
| 3 | `grade_code` | `character varying(20)` | sí | Código del grado del cargo en el perfil de funciones, según la Matriz de Funciones ESAP. |  |
| 4 | `combined_code` | `character varying(40)` | sí | Normalized cargo key (base position code plus grade when applicable) |  |
| 5 | `match_key` | `character varying(500)` | no | Unique normalized fingerprint combining codes, level, position name, department, internal group and cost center | única |
| 6 | `hierarchical_level` | `character varying(100)` | sí | Nivel jerárquico del cargo del perfil de funciones. |  |
| 7 | `position_name` | `character varying(255)` | sí | Denominación del cargo del perfil de funciones. |  |
| 8 | `department_name` | `character varying(500)` | sí | Nombre de la dependencia a la que pertenece el cargo, según la Matriz de Funciones ESAP. |  |
| 9 | `department_key` | `character varying(500)` | sí | Clave del nombre de la dependencia del perfil de funciones, conservada del catálogo inicial. |  |
| 10 | `internal_group` | `character varying(500)` | sí | Nombre del grupo interno de trabajo al que pertenece el cargo. |  |
| 11 | `internal_group_key` | `character varying(500)` | sí | Clave del nombre del grupo interno de trabajo del perfil de funciones, conservada del catálogo inicial. |  |
| 12 | `cost_center` | `character varying(255)` | sí | Centro de costo del cargo (CENTROCOSTO), que corresponde al nombre del grupo interno de trabajo y se usa cuando internal_group está vacío. |  |
| 13 | `source_sheet` | `character varying(255)` | sí | Nombre de la hoja de la Matriz de Funciones ESAP de la que se importó el perfil. |  |
| 14 | `is_active` | `boolean` | no | Indica si el perfil de funciones del cargo está activo. |  |
| 15 | `created_by` | `character varying(255)` | sí | Usuario que creó el registro. |  |
| 16 | `updated_by` | `character varying(255)` | sí | Usuario que realizó la última actualización del registro. |  |
| 17 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 18 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 19 | `id_number` | `character varying(50)` | sí | Número de identificación del empleado al que se asignan las funciones del perfil; solo dígitos (hasta 50) y único. Queda vacío en los perfiles anteriores pendientes de asignación. |  |

## labor_functions

Normalized, ordered labor functions belonging to a position profile

- Clave primaria: `id`
- Filas: 190
- Referencia a: `profile_id` → `certification.labor_function_profiles` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla labor_functions. Se genera automáticamente. | PK |
| 2 | `profile_id` | `uuid` | no | Referencia al registro de certification.labor_function_profiles (id). | FK→certification.labor_function_profiles.id |
| 3 | `ordinal` | `integer` | no | Número de orden de la función dentro del perfil del cargo; único por perfil. |  |
| 4 | `description` | `text` | no | Descripción de la función laboral del perfil del cargo. |  |
| 5 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 6 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## signers

Authorized signers captured on issued certificates

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla signers. Se genera automáticamente. | PK |
| 2 | `full_name` | `character varying(255)` | no | Nombre completo del firmante autorizado de certificados laborales. | Nombre de persona |
| 3 | `position` | `character varying(255)` | no | Cargo del firmante autorizado. |  |
| 4 | `department` | `character varying(255)` | sí | Dependencia a la que pertenece el firmante autorizado. |  |
| 5 | `signature_url` | `character varying(500)` | sí | Ruta o URL de la imagen de la firma digital del firmante. |  |
| 6 | `is_active` | `boolean` | sí | Indica si el firmante está activo; por defecto verdadero. |  |
| 7 | `is_primary` | `boolean` | sí | Indica si es el firmante principal, usado por defecto; por defecto falso. |  |
| 8 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## technical_bonus_assignments

Technical-bonus percentage assignments by employee and category

- Clave primaria: `id`
- Filas: 53
- Referencia a: `request_id` → `certification.certificate_requests` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla technical_bonus_assignments. Se genera automáticamente. | PK |
| 2 | `request_id` | `uuid` | sí | Referencia al registro de certification.certificate_requests (id). | FK→certification.certificate_requests.id |
| 3 | `category` | `character varying(80)` | no | Technical-bonus category code |  |
| 4 | `full_name` | `character varying(255)` | no | Nombre completo del empleado al que se asigna el porcentaje de bonificación técnica. | Nombre de persona |
| 5 | `id_number` | `character varying(50)` | no | Normalized employee identification number |  |
| 6 | `percentage` | `numeric(5,2)` | no | Assigned technical-bonus percentage (greater than 0 and at most 100) |  |
| 7 | `created_by` | `character varying(255)` | sí | Usuario que creó el registro. |  |
| 8 | `updated_by` | `character varying(255)` | sí | Usuario que realizó la última actualización del registro. |  |
| 9 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 10 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## technical_bonus_templates

Paragraph templates for technical-bonus sections in labor certificates

- Clave primaria: `id`
- Filas: 3

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla technical_bonus_templates. Se genera automáticamente. | PK |
| 2 | `category` | `character varying(80)` | no | Stable technical-bonus category code | única |
| 3 | `template_text` | `text` | no | Template with placeholders rendered in institutional order: numeric amount followed by amount in words |  |
| 4 | `updated_at` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 5 | `updated_by` | `character varying(255)` | sí | Usuario que realizó la última actualización del registro. |  |
| 6 | `label` | `character varying(120)` | sí | Nombre visible de la categoría de prima técnica de la plantilla; si está vacío se deriva de la categoría. |  |
| 7 | `description` | `character varying(255)` | sí | Descripción de la plantilla de párrafo de bonificación técnica. |  |
| 8 | `display_order` | `integer` | no | Orden de presentación de la plantilla en las listas; 0 por defecto. |  |
| 9 | `is_system` | `boolean` | no | Indica si la plantilla de bonificación técnica es del sistema. |  |
| 10 | `is_active` | `boolean` | no | Indica si la plantilla de bonificación técnica está activa. |  |
| 11 | `created_at` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |

## template_config_changes

Certificate-template configuration change history

- Clave primaria: `id`
- Filas: 206
- Referencia a: `template_config_id` → `certification.certificate_template_config` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla template_config_changes. Se genera automáticamente. | PK |
| 2 | `template_config_id` | `integer` | sí | Referencia al registro de certification.certificate_template_config (id). | FK→certification.certificate_template_config.id |
| 3 | `change_type` | `character varying(50)` | no | Template configuration change category |  |
| 4 | `field_name` | `character varying(100)` | no | Physical configuration field modified by the change |  |
| 5 | `old_value` | `text` | sí | Field value before the change |  |
| 6 | `new_value` | `text` | sí | Field value after the change |  |
| 7 | `metadata` | `jsonb` | sí | Additional change metadata stored as JSON |  |
| 8 | `changed_at` | `timestamp without time zone` | sí | Fecha y hora en que se registró el cambio de configuración de la plantilla. |  |
| 9 | `changed_by` | `character varying(255)` | sí | Nombre de usuario que realizó el cambio de configuración de la plantilla, enviado por el cliente o tomado de la cabecera x-user-username; Usuario si no se informa. |  |

## template_signers

Signers available for labor-certificate templates

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla template_signers. Se genera automáticamente. | PK |
| 2 | `full_name` | `character varying(255)` | no | Nombre completo del firmante disponible para las plantillas de certificado laboral. | Nombre de persona |
| 3 | `position` | `character varying(150)` | no | Cargo del firmante. |  |
| 4 | `department` | `character varying(255)` | no | Dependencia a la que pertenece el firmante. |  |
| 5 | `is_active` | `boolean` | sí | Indica si el firmante de plantillas de certificado laboral está activo. |  |
| 6 | `is_primary` | `boolean` | sí | Indicates whether this is the default template signer |  |
| 7 | `signature_url` | `text` | sí | URL of the signer signature image |  |
| 8 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
