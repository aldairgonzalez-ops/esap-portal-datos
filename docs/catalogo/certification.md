# Certificaciones (`certification`)

Solicitud y expedición de certificados.

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
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `request_number` | `character varying(50)` | no | _Por documentar_ | única |
| 3 | `certificate_id` | `uuid` | no | _Por documentar_ | FK→certification.certificates.id |
| 4 | `status` | `character varying(20)` | no | _Por documentar_ |  |
| 5 | `description` | `text` | no | _Por documentar_ |  |
| 6 | `requester_name` | `character varying(255)` | no | _Por documentar_ |  |
| 7 | `requester_email` | `character varying(255)` | no | _Por documentar_ | Contacto |
| 8 | `submitted_evidence` | `jsonb` | no | _Por documentar_ |  |
| 9 | `certificate_snapshot` | `jsonb` | no | Immutable snapshot of the certificate when the correction was submitted |  |
| 10 | `due_date` | `date` | no | Maximum response date calculated as fifteen business days after submission |  |
| 11 | `reviewed_by_id` | `uuid` | sí | _Por documentar_ |  |
| 12 | `reviewed_by_name` | `character varying(255)` | sí | _Por documentar_ |  |
| 13 | `reviewed_by_email` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 14 | `review_started_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 15 | `resolution_description` | `text` | sí | _Por documentar_ |  |
| 16 | `resolution_evidence` | `jsonb` | no | _Por documentar_ |  |
| 17 | `corrected_data` | `jsonb` | sí | _Por documentar_ |  |
| 18 | `resolved_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 19 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 20 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 21 | `traceability` | `jsonb` | no | Chronological and immutable business audit trail for the correction request |  |

## certificate_requests

Labor certificate requests submitted by employees

- Clave primaria: `id`
- Filas: 15250

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `request_number` | `character varying(50)` | no | Unique request number format: 12_620_700_20_CD 001 | única |
| 3 | `person_id` | `uuid` | sí | _Por documentar_ |  |
| 4 | `full_name` | `character varying(255)` | no | _Por documentar_ | Nombre de persona |
| 5 | `id_number` | `character varying(50)` | no | _Por documentar_ |  |
| 6 | `career_category` | `character varying(100)` | no | DATA3: Administrative Career, Free Appointment, etc. |  |
| 7 | `hiring_date` | `date` | no | _Por documentar_ |  |
| 8 | `position_category` | `character varying(100)` | no | DATA5: TITULAR Teacher, OCCASIONAL, CHAIR |  |
| 9 | `position_location` | `character varying(150)` | sí | _Por documentar_ |  |
| 10 | `monthly_salary` | `numeric(12,2)` | no | DATA7: Monthly salary in number |  |
| 11 | `salary_text` | `character varying(255)` | sí | DATA8: Salary in text (forty forty-five pesos m/cte) |  |
| 12 | `department` | `character varying(255)` | sí | _Por documentar_ |  |
| 13 | `campus` | `character varying(100)` | sí | _Por documentar_ |  |
| 14 | `email` | `character varying(100)` | sí | _Por documentar_ | Contacto |
| 15 | `phone` | `character varying(20)` | sí | _Por documentar_ | Contacto |
| 16 | `status` | `character varying(50)` | no | _Por documentar_ |  |
| 17 | `request_date` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 18 | `observations` | `text` | sí | _Por documentar_ |  |
| 19 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 20 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 21 | `validation_code` | `character varying(10)` | sí | _Por documentar_ |  |
| 22 | `validation_expires_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 23 | `position_code` | `character varying(255)` | sí | Position code received from the authoritative human-resources source |  |
| 24 | `grade_code` | `character varying(255)` | sí | Position grade code received from the authoritative human-resources source |  |
| 25 | `document_type` | `character varying(10)` | sí | Document type provided through labor-certificate self-service (CC, CE, PP) |  |
| 26 | `base_position_code` | `character varying(20)` | sí | _Por documentar_ |  |
| 27 | `hierarchical_level` | `character varying(100)` | sí | _Por documentar_ |  |
| 28 | `position_name` | `character varying(255)` | sí | _Por documentar_ |  |
| 29 | `organization_department` | `character varying(500)` | sí | _Por documentar_ |  |
| 30 | `internal_group` | `character varying(500)` | sí | _Por documentar_ |  |
| 31 | `cost_center` | `character varying(255)` | sí | _Por documentar_ |  |

## certificate_template_config

Labor-certificate template configuration

- Clave primaria: `id`
- Filas: 3
- Referencia a: `signer_id` → `certification.template_signers` (1..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | _Por documentar_ | PK |
| 2 | `signer_id` | `uuid` | sí | Reference to the signer assigned to this template | FK→certification.template_signers.id |
| 3 | `entity_logo_url` | `text` | sí | URL of the institutional ESAP logo |  |
| 4 | `entity_logo_filename` | `character varying(255)` | sí | _Por documentar_ |  |
| 5 | `entity_logo_size` | `character varying(50)` | sí | _Por documentar_ |  |
| 6 | `typography_font` | `character varying(100)` | sí | Font family applied to the certificate |  |
| 7 | `signer_title` | `text` | sí | Signer title displayed in the certificate heading |  |
| 8 | `certificate_content_html` | `text` | sí | Certificate HTML content with dynamic placeholders |  |
| 9 | `version` | `character varying(20)` | sí | _Por documentar_ |  |
| 10 | `status` | `character varying(50)` | sí | _Por documentar_ |  |
| 11 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 13 | `created_by` | `character varying(255)` | sí | _Por documentar_ |  |
| 14 | `updated_by` | `character varying(255)` | sí | _Por documentar_ |  |
| 15 | `is_active` | `boolean` | sí | Indicates whether this configuration is active |  |
| 16 | `template_type` | `character varying(30)` | no | _Por documentar_ |  |
| 17 | `signature_url` | `text` | sí | _Por documentar_ |  |
| 18 | `signature_filename` | `text` | sí | _Por documentar_ |  |
| 19 | `signature_size` | `text` | sí | _Por documentar_ |  |
| 20 | `signer_name_override` | `text` | sí | _Por documentar_ |  |

## certificate_templates

HTML templates used to generate certificates

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `name` | `character varying(255)` | no | _Por documentar_ |  |
| 3 | `description` | `text` | sí | _Por documentar_ |  |
| 4 | `html_content` | `text` | no | _Por documentar_ |  |
| 5 | `certificate_type` | `character varying(100)` | sí | _Por documentar_ |  |
| 6 | `is_active` | `boolean` | sí | _Por documentar_ |  |
| 7 | `version` | `integer` | sí | _Por documentar_ |  |
| 8 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 9 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |

## certificate_validations

Labor-certificate validation history

- Clave primaria: `id`
- Filas: 42
- Referencia a: `certificate_id` → `certification.certificates` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `certificate_id` | `uuid` | no | Reference to the validated certificate | FK→certification.certificates.id |
| 3 | `validation_date` | `timestamp without time zone` | no | _Por documentar_ |  |
| 4 | `ip_address` | `character varying(50)` | sí | _Por documentar_ | Identificador en línea (IP) |
| 5 | `user_agent` | `text` | sí | _Por documentar_ |  |
| 6 | `location` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `result` | `character varying(50)` | no | Certificate validation result |  |
| 8 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
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
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `verification_code` | `character varying(100)` | no | _Por documentar_ | única |
| 3 | `certificate_number` | `character varying(50)` | no | _Por documentar_ | única |
| 4 | `request_id` | `uuid` | no | _Por documentar_ | FK→certification.certificate_requests.id |
| 5 | `full_name` | `character varying(255)` | no | _Por documentar_ | Nombre de persona |
| 6 | `id_number` | `character varying(50)` | no | _Por documentar_ |  |
| 7 | `career_category` | `character varying(100)` | no | _Por documentar_ |  |
| 8 | `hiring_date` | `date` | no | _Por documentar_ |  |
| 9 | `position_category` | `character varying(100)` | no | _Por documentar_ |  |
| 10 | `position_location` | `character varying(150)` | sí | _Por documentar_ |  |
| 11 | `monthly_salary` | `numeric(12,2)` | no | _Por documentar_ |  |
| 12 | `salary_text` | `character varying(255)` | sí | _Por documentar_ |  |
| 13 | `department` | `character varying(255)` | sí | _Por documentar_ |  |
| 14 | `campus` | `character varying(100)` | sí | _Por documentar_ |  |
| 15 | `issue_date` | `date` | no | _Por documentar_ |  |
| 16 | `issuance_timestamp` | `timestamp without time zone` | no | _Por documentar_ |  |
| 17 | `signer_name` | `character varying(255)` | sí | _Por documentar_ |  |
| 18 | `signer_position` | `character varying(255)` | sí | _Por documentar_ |  |
| 19 | `signer_department` | `character varying(255)` | sí | _Por documentar_ |  |
| 20 | `pdf_url` | `character varying(500)` | sí | _Por documentar_ |  |
| 21 | `status` | `character varying(50)` | no | _Por documentar_ |  |
| 22 | `validation_count` | `integer` | sí | _Por documentar_ |  |
| 23 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 24 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 25 | `position_code` | `character varying(255)` | sí | Position code captured when the certificate was issued |  |
| 26 | `technical_bonus` | `numeric(12,2)` | sí | _Por documentar_ |  |
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
| 37 | `last_corrected_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 38 | `assignment_type` | `character varying(1)` | sí | Assignment indicator rendered by the labor certificate: E shows the encargo suffix and N omits it |  |
| 39 | `include_functions` | `boolean` | no | Whether the requester selected the option to include labor functions |  |
| 40 | `functions_snapshot` | `jsonb` | sí | Immutable snapshot of the matched profile and ordered functions at issuance time |  |

## labor_function_profiles

Position profiles imported from Matriz Funciones ESAP and used to associate employees by normalized codes and organizational context

- Clave primaria: `id`
- Filas: 19

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `position_code` | `character varying(20)` | sí | _Por documentar_ |  |
| 3 | `grade_code` | `character varying(20)` | sí | _Por documentar_ |  |
| 4 | `combined_code` | `character varying(40)` | sí | Normalized cargo key (base position code plus grade when applicable) |  |
| 5 | `match_key` | `character varying(500)` | no | Unique normalized fingerprint combining codes, level, position name, department, internal group and cost center | única |
| 6 | `hierarchical_level` | `character varying(100)` | sí | _Por documentar_ |  |
| 7 | `position_name` | `character varying(255)` | sí | _Por documentar_ |  |
| 8 | `department_name` | `character varying(500)` | sí | _Por documentar_ |  |
| 9 | `department_key` | `character varying(500)` | sí | _Por documentar_ |  |
| 10 | `internal_group` | `character varying(500)` | sí | _Por documentar_ |  |
| 11 | `internal_group_key` | `character varying(500)` | sí | _Por documentar_ |  |
| 12 | `cost_center` | `character varying(255)` | sí | _Por documentar_ |  |
| 13 | `source_sheet` | `character varying(255)` | sí | _Por documentar_ |  |
| 14 | `is_active` | `boolean` | no | _Por documentar_ |  |
| 15 | `created_by` | `character varying(255)` | sí | _Por documentar_ |  |
| 16 | `updated_by` | `character varying(255)` | sí | _Por documentar_ |  |
| 17 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 18 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 19 | `id_number` | `character varying(50)` | sí | _Por documentar_ |  |

## labor_functions

Normalized, ordered labor functions belonging to a position profile

- Clave primaria: `id`
- Filas: 190
- Referencia a: `profile_id` → `certification.labor_function_profiles` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `profile_id` | `uuid` | no | _Por documentar_ | FK→certification.labor_function_profiles.id |
| 3 | `ordinal` | `integer` | no | _Por documentar_ |  |
| 4 | `description` | `text` | no | _Por documentar_ |  |
| 5 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 6 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |

## signers

Authorized signers captured on issued certificates

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `full_name` | `character varying(255)` | no | _Por documentar_ | Nombre de persona |
| 3 | `position` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `department` | `character varying(255)` | sí | _Por documentar_ |  |
| 5 | `signature_url` | `character varying(500)` | sí | _Por documentar_ |  |
| 6 | `is_active` | `boolean` | sí | _Por documentar_ |  |
| 7 | `is_primary` | `boolean` | sí | _Por documentar_ |  |
| 8 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 9 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |

## technical_bonus_assignments

Technical-bonus percentage assignments by employee and category

- Clave primaria: `id`
- Filas: 53
- Referencia a: `request_id` → `certification.certificate_requests` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `request_id` | `uuid` | sí | _Por documentar_ | FK→certification.certificate_requests.id |
| 3 | `category` | `character varying(80)` | no | Technical-bonus category code |  |
| 4 | `full_name` | `character varying(255)` | no | _Por documentar_ | Nombre de persona |
| 5 | `id_number` | `character varying(50)` | no | Normalized employee identification number |  |
| 6 | `percentage` | `numeric(5,2)` | no | Assigned technical-bonus percentage (greater than 0 and at most 100) |  |
| 7 | `created_by` | `character varying(255)` | sí | _Por documentar_ |  |
| 8 | `updated_by` | `character varying(255)` | sí | _Por documentar_ |  |
| 9 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 10 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |

## technical_bonus_templates

Paragraph templates for technical-bonus sections in labor certificates

- Clave primaria: `id`
- Filas: 3

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `category` | `character varying(80)` | no | Stable technical-bonus category code | única |
| 3 | `template_text` | `text` | no | Template with placeholders rendered in institutional order: numeric amount followed by amount in words |  |
| 4 | `updated_at` | `timestamp without time zone` | no | _Por documentar_ |  |
| 5 | `updated_by` | `character varying(255)` | sí | _Por documentar_ |  |
| 6 | `label` | `character varying(120)` | sí | _Por documentar_ |  |
| 7 | `description` | `character varying(255)` | sí | _Por documentar_ |  |
| 8 | `display_order` | `integer` | no | _Por documentar_ |  |
| 9 | `is_system` | `boolean` | no | _Por documentar_ |  |
| 10 | `is_active` | `boolean` | no | _Por documentar_ |  |
| 11 | `created_at` | `timestamp without time zone` | no | _Por documentar_ |  |

## template_config_changes

Certificate-template configuration change history

- Clave primaria: `id`
- Filas: 206
- Referencia a: `template_config_id` → `certification.certificate_template_config` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | _Por documentar_ | PK |
| 2 | `template_config_id` | `integer` | sí | _Por documentar_ | FK→certification.certificate_template_config.id |
| 3 | `change_type` | `character varying(50)` | no | Template configuration change category |  |
| 4 | `field_name` | `character varying(100)` | no | Physical configuration field modified by the change |  |
| 5 | `old_value` | `text` | sí | Field value before the change |  |
| 6 | `new_value` | `text` | sí | Field value after the change |  |
| 7 | `metadata` | `jsonb` | sí | Additional change metadata stored as JSON |  |
| 8 | `changed_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 9 | `changed_by` | `character varying(255)` | sí | _Por documentar_ |  |

## template_signers

Signers available for labor-certificate templates

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `full_name` | `character varying(255)` | no | _Por documentar_ | Nombre de persona |
| 3 | `position` | `character varying(150)` | no | _Por documentar_ |  |
| 4 | `department` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `is_active` | `boolean` | sí | _Por documentar_ |  |
| 6 | `is_primary` | `boolean` | sí | Indicates whether this is the default template signer |  |
| 7 | `signature_url` | `text` | sí | URL of the signer signature image |  |
| 8 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
