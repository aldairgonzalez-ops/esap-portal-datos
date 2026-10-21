# Registro académico (`academic_registration`)

Inscripción, admisión y matrícula de estudiantes en los programas académicos.

10 tablas · 0 vistas · 183 columnas · 11.215 filas · 2 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`certificate_template_config`](#certificate_template_config) | Tabla | 1 | Certificate template configuration |
| [`certificate_validations`](#certificate_validations) | Tabla | 153 | Public certificate validation history |
| [`graduate_files`](#graduate_files) | Tabla | 41 | _Por documentar_ |
| [`graduate_program_catalog`](#graduate_program_catalog) | Tabla | 1 | Catálogo central de programas usado por la gestión y revisión de graduados. |
| [`graduates`](#graduates) | Tabla | 10429 | Graduates from the supported academic program types |
| [`graduation_certificate_requests`](#graduation_certificate_requests) | Tabla | 392 | Graduation certificate requests across workflow states |
| [`graduation_certificates`](#graduation_certificates) | Tabla | 161 | Issued graduation certificates with valid QR codes |
| [`graduation_request_review_files`](#graduation_request_review_files) | Tabla | 30 | _Por documentar_ |
| [`signers`](#signers) | Tabla | 1 | Authorized certificate signers |
| [`template_config_changes`](#template_config_changes) | Tabla | 6 | Certificate template change history |

## certificate_template_config

Certificate template configuration

- Clave primaria: `id`
- Filas: 1
- Referencia a: `signer_id` → `academic_registration.signers` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | _Por documentar_ | PK |
| 2 | `signer_id` | `uuid` | sí | _Por documentar_ | FK→academic_registration.signers.id |
| 3 | `institution_logo_url` | `text` | sí | _Por documentar_ |  |
| 4 | `institution_logo_filename` | `character varying(255)` | sí | _Por documentar_ |  |
| 5 | `typography_font` | `character varying(100)` | sí | _Por documentar_ |  |
| 6 | `signer_title_override` | `character varying(255)` | sí | Signer position or title displayed below the electronic signature or as the default closing title |  |
| 7 | `certificate_content_html` | `text` | no | _Por documentar_ |  |
| 8 | `version` | `character varying(50)` | sí | _Por documentar_ |  |
| 9 | `status` | `character varying(50)` | sí | _Por documentar_ |  |
| 10 | `signature_url_override` | `text` | sí | Electronic signature image for the template; supports a base64 data URL or a historical path |  |
| 11 | `signature_filename_override` | `character varying(255)` | sí | Original or normalized electronic signature filename |  |
| 12 | `signer_name_override` | `character varying(255)` | sí | Signer name displayed on the certificate when the electronic signature is active |  |
| 13 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 15 | `created_by` | `character varying(255)` | sí | _Por documentar_ |  |
| 16 | `updated_by` | `character varying(255)` | sí | _Por documentar_ |  |
| 17 | `is_active` | `boolean` | sí | _Por documentar_ |  |
| 18 | `footer_logo_url` | `text` | sí | _Por documentar_ |  |
| 19 | `footer_logo_filename` | `character varying(255)` | sí | _Por documentar_ |  |

## certificate_validations

Public certificate validation history

- Clave primaria: `id`
- Filas: 153
- Referencia a: `certificate_id` → `academic_registration.graduation_certificates` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `certificate_id` | `uuid` | no | _Por documentar_ | FK→academic_registration.graduation_certificates.id |
| 3 | `validation_date` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 4 | `ip_address` | `character varying(50)` | sí | _Por documentar_ | Identificador en línea (IP) |
| 5 | `user_agent` | `text` | sí | _Por documentar_ |  |
| 6 | `location` | `character varying(255)` | sí | _Por documentar_ |  |
| 7 | `result` | `character varying(50)` | no | _Por documentar_ |  |
| 8 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## graduate_files

_Por documentar._

- Clave primaria: `id`
- Filas: 41
- Referencia a: `graduate_id` → `academic_registration.graduates` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `graduate_id` | `uuid` | no | _Por documentar_ | FK→academic_registration.graduates.id |
| 3 | `original_name` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `stored_name` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `mime_type` | `character varying(150)` | no | _Por documentar_ |  |
| 6 | `size_bytes` | `integer` | no | _Por documentar_ |  |
| 7 | `uploaded_by` | `character varying(255)` | sí | _Por documentar_ |  |
| 8 | `uploaded_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## graduate_program_catalog

Catálogo central de programas usado por la gestión y revisión de graduados.

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `name` | `character varying(255)` | no | _Por documentar_ |  |
| 3 | `normalized_name` | `character varying(255)` | no | _Por documentar_ | única |
| 4 | `created_by` | `character varying(255)` | sí | _Por documentar_ |  |
| 5 | `created_at` | `timestamp with time zone` | no | _Por documentar_ |  |

## graduates

Graduates from the supported academic program types

- Clave primaria: `id`
- Filas: 10429

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `person_id` | `uuid` | no | _Por documentar_ |  |
| 3 | `full_name` | `character varying(255)` | no | _Por documentar_ | Nombre de persona |
| 4 | `id_number` | `character varying(50)` | no | _Por documentar_ |  |
| 5 | `email` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 6 | `phone` | `character varying(50)` | sí | _Por documentar_ | Contacto |
| 7 | `program_id` | `uuid` | no | _Por documentar_ |  |
| 8 | `program_name` | `character varying(255)` | no | _Por documentar_ |  |
| 9 | `program_type` | `character varying(50)` | no | _Por documentar_ |  |
| 10 | `enrollment_date` | `date` | sí | _Por documentar_ |  |
| 11 | `graduation_date` | `date` | no | _Por documentar_ |  |
| 12 | `ceremony_date` | `date` | sí | _Por documentar_ |  |
| 13 | `degree_title` | `character varying(255)` | no | _Por documentar_ |  |
| 14 | `diploma_number` | `character varying(100)` | sí | _Por documentar_ | única |
| 15 | `registry_reference` | `character varying(100)` | sí | Composite registry, folio and book reference used by issued certificates |  |
| 16 | `resolution_number` | `character varying(100)` | sí | _Por documentar_ |  |
| 17 | `status` | `character varying(50)` | sí | _Por documentar_ |  |
| 18 | `is_verified` | `boolean` | sí | _Por documentar_ |  |
| 19 | `campus` | `character varying(100)` | sí | _Por documentar_ |  |
| 20 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 21 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 22 | `created_by` | `character varying(255)` | sí | _Por documentar_ |  |
| 23 | `updated_by` | `character varying(255)` | sí | _Por documentar_ |  |
| 24 | `id_issue_date` | `date` | sí | Identity document issue date |  |
| 25 | `regional_office_name` | `character varying(255)` | sí | Regional office assigned to the graduate |  |
| 26 | `first_name` | `character varying(255)` | sí | _Por documentar_ | Nombre de persona |
| 27 | `last_name` | `character varying(255)` | sí | _Por documentar_ | Nombre de persona |
| 28 | `graduation_record_number` | `character varying(100)` | sí | Graduation record number received from the academic source system |  |
| 29 | `folio_number` | `character varying(100)` | sí | Academic registry folio number |  |
| 30 | `book_number` | `character varying(100)` | sí | Academic registry book number |  |
| 31 | `registry_number` | `character varying(100)` | sí | Academic registry number |  |

## graduation_certificate_requests

Graduation certificate requests across workflow states

- Clave primaria: `id`
- Filas: 392

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `request_number` | `character varying(100)` | no | _Por documentar_ | única |
| 3 | `requester_type` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `graduate_id` | `uuid` | sí | _Por documentar_ |  |
| 5 | `id_number` | `character varying(50)` | no | _Por documentar_ |  |
| 6 | `full_name` | `character varying(255)` | no | _Por documentar_ | Nombre de persona |
| 7 | `program_name` | `character varying(255)` | no | _Por documentar_ |  |
| 8 | `graduation_date` | `date` | sí | _Por documentar_ |  |
| 9 | `requester_name` | `character varying(255)` | sí | _Por documentar_ |  |
| 10 | `requester_email` | `character varying(255)` | no | _Por documentar_ | Contacto |
| 11 | `requester_phone` | `character varying(50)` | sí | _Por documentar_ | Contacto |
| 12 | `company_name` | `character varying(255)` | sí | _Por documentar_ |  |
| 13 | `certificate_type` | `character varying(50)` | sí | _Por documentar_ |  |
| 14 | `validation_code` | `character varying(10)` | sí | _Por documentar_ |  |
| 15 | `validation_expires_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 16 | `is_validated` | `boolean` | sí | _Por documentar_ |  |
| 17 | `status` | `character varying(50)` | sí | _Por documentar_ |  |
| 18 | `observations` | `text` | sí | _Por documentar_ |  |
| 19 | `rejection_reason` | `text` | sí | _Por documentar_ |  |
| 20 | `request_date` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 21 | `validation_date` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 22 | `completion_date` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 23 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 24 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 25 | `id_issue_date` | `date` | sí | _Por documentar_ |  |
| 26 | `manual_review` | `boolean` | sí | _Por documentar_ |  |
| 27 | `reviewed_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 28 | `reviewed_by` | `character varying(100)` | sí | _Por documentar_ |  |
| 29 | `reviewer_name` | `character varying(255)` | sí | _Por documentar_ |  |
| 30 | `review_notes` | `text` | sí | _Por documentar_ |  |
| 31 | `review_resolution` | `character varying(50)` | sí | _Por documentar_ |  |
| 32 | `graduate_last_name` | `character varying(255)` | sí | _Por documentar_ | Nombre de persona |
| 33 | `graduate_email` | `character varying(255)` | sí | _Por documentar_ | Contacto |
| 34 | `graduate_phone` | `character varying(50)` | sí | _Por documentar_ | Contacto |
| 35 | `company_tax_id` | `character varying(50)` | sí | Company tax identifier supplied by the requester |  |
| 36 | `contact_person` | `character varying(255)` | sí | _Por documentar_ |  |
| 37 | `approval_status` | `character varying(50)` | sí | Workflow state: PENDING_APPROVAL, PENDING_HEAD_APPROVAL, APPROVED_FINAL, REJECTED_FINAL, OBSERVATION or HEAD_OBSERVATION |  |
| 38 | `review_recommendation` | `character varying(50)` | sí | Reviewer recommendation: APPROVED or REJECTED; OBSERVATION is reserved for the approver |  |
| 39 | `review_recommendation_reason` | `text` | sí | _Por documentar_ |  |
| 40 | `review_payload` | `jsonb` | sí | Data verified by the reviewer before final approval |  |
| 41 | `review_submitted_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 42 | `review_submitted_by` | `character varying(100)` | sí | _Por documentar_ |  |
| 43 | `review_submitted_by_name` | `character varying(255)` | sí | _Por documentar_ |  |
| 44 | `approver_decision` | `character varying(50)` | sí | _Por documentar_ |  |
| 45 | `approver_notes` | `text` | sí | _Por documentar_ |  |
| 46 | `approved_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 47 | `approved_by` | `character varying(100)` | sí | _Por documentar_ |  |
| 48 | `approver_name` | `character varying(255)` | sí | _Por documentar_ |  |
| 49 | `review_timeline` | `jsonb` | no | Chronological reviewer and approver workflow trace |  |
| 50 | `head_decision` | `character varying(50)` | sí | Academic registration head decision: APPROVED, REJECTED or OBSERVATION |  |
| 51 | `head_notes` | `text` | sí | Notes or justification from the academic registration head |  |
| 52 | `head_reviewed_at` | `timestamp without time zone` | sí | Date and time when the academic registration head issued a final decision or observation |  |
| 53 | `head_reviewed_by` | `character varying(100)` | sí | Identifier of the academic registration head who issued the decision |  |
| 54 | `head_reviewer_name` | `character varying(255)` | sí | Name of the academic registration head who issued the decision |  |
| 55 | `requester_support_original_name` | `character varying(255)` | sí | _Por documentar_ |  |
| 56 | `requester_support_stored_name` | `character varying(255)` | sí | _Por documentar_ |  |
| 57 | `requester_support_mime_type` | `character varying(150)` | sí | _Por documentar_ |  |
| 58 | `requester_support_size_bytes` | `integer` | sí | _Por documentar_ |  |
| 59 | `requester_support_uploaded_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## graduation_certificates

Issued graduation certificates with valid QR codes

- Clave primaria: `id`
- Filas: 161
- Referencia a: `graduate_id` → `academic_registration.graduates` (0..* → 0..1); `request_id` → `academic_registration.graduation_certificate_requests` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `request_id` | `uuid` | no | _Por documentar_ | FK→academic_registration.graduation_certificate_requests.id |
| 3 | `graduate_id` | `uuid` | sí | _Por documentar_ | FK→academic_registration.graduates.id |
| 4 | `certificate_number` | `character varying(100)` | no | _Por documentar_ | única |
| 5 | `verification_code` | `character varying(50)` | no | _Por documentar_ | única |
| 6 | `full_name` | `character varying(255)` | no | _Por documentar_ | Nombre de persona |
| 7 | `id_number` | `character varying(50)` | no | _Por documentar_ |  |
| 8 | `program_name` | `character varying(255)` | no | _Por documentar_ |  |
| 9 | `program_type` | `character varying(50)` | no | _Por documentar_ |  |
| 10 | `degree_title` | `character varying(255)` | no | _Por documentar_ |  |
| 11 | `graduation_date` | `date` | no | _Por documentar_ |  |
| 12 | `diploma_number` | `character varying(100)` | sí | _Por documentar_ |  |
| 13 | `registry_reference` | `character varying(100)` | sí | Composite registry, folio and book reference stored when the certificate is issued |  |
| 14 | `campus` | `character varying(100)` | sí | _Por documentar_ |  |
| 15 | `signer_name` | `character varying(255)` | no | _Por documentar_ |  |
| 16 | `signer_position` | `character varying(255)` | no | _Por documentar_ |  |
| 17 | `signature_url` | `text` | sí | _Por documentar_ |  |
| 18 | `pdf_url` | `text` | sí | _Por documentar_ |  |
| 19 | `pdf_filename` | `character varying(255)` | sí | _Por documentar_ |  |
| 20 | `status` | `character varying(50)` | sí | _Por documentar_ |  |
| 21 | `issue_date` | `date` | sí | _Por documentar_ |  |
| 22 | `expiry_date` | `date` | sí | _Por documentar_ |  |
| 23 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 24 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 25 | `created_by` | `character varying(255)` | sí | _Por documentar_ |  |
| 26 | `regional_office_name` | `character varying(150)` | sí | Regional office associated with the certificate and persisted from manual approvals |  |
| 27 | `template_snapshot` | `jsonb` | sí | JSON snapshot of the template used when the certificate was issued |  |

## graduation_request_review_files

_Por documentar._

- Clave primaria: `id`
- Filas: 30
- Referencia a: `request_id` → `academic_registration.graduation_certificate_requests` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `request_id` | `uuid` | no | _Por documentar_ | FK→academic_registration.graduation_certificate_requests.id |
| 3 | `original_name` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `stored_name` | `character varying(255)` | no | _Por documentar_ |  |
| 5 | `mime_type` | `character varying(150)` | no | _Por documentar_ |  |
| 6 | `size_bytes` | `integer` | no | _Por documentar_ |  |
| 7 | `uploaded_by` | `character varying(255)` | sí | _Por documentar_ |  |
| 8 | `uploaded_at` | `timestamp without time zone` | no | _Por documentar_ |  |

## signers

Authorized certificate signers

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `full_name` | `character varying(255)` | no | _Por documentar_ | Nombre de persona |
| 3 | `position` | `character varying(255)` | no | _Por documentar_ |  |
| 4 | `department` | `character varying(255)` | sí | _Por documentar_ |  |
| 5 | `signature_url` | `text` | sí | _Por documentar_ |  |
| 6 | `is_active` | `boolean` | sí | _Por documentar_ |  |
| 7 | `is_primary` | `boolean` | sí | _Por documentar_ |  |
| 8 | `created_at` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | _Por documentar_ |  |

## template_config_changes

Certificate template change history

- Clave primaria: `id`
- Filas: 6
- Referencia a: `template_config_id` → `academic_registration.certificate_template_config` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | _Por documentar_ | PK |
| 2 | `template_config_id` | `integer` | no | _Por documentar_ | FK→academic_registration.certificate_template_config.id |
| 3 | `change_type` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `field_changed` | `character varying(100)` | sí | _Por documentar_ |  |
| 5 | `old_value` | `text` | sí | _Por documentar_ |  |
| 6 | `new_value` | `text` | sí | _Por documentar_ |  |
| 7 | `changed_by` | `character varying(255)` | no | _Por documentar_ |  |
| 8 | `change_date` | `timestamp without time zone` | sí | _Por documentar_ |  |
| 9 | `observations` | `text` | sí | _Por documentar_ |  |
