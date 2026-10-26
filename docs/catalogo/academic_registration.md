# Registro académico y grados (`academic_registration`)

Graduados y certificados de grado: registro de graduados y sus archivos, solicitudes de certificado y su revisión, certificados emitidos con código QR, validación pública, firmantes y configuración de plantillas.

10 tablas · 0 vistas · 183 columnas · 11.215 filas · 2 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`certificate_template_config`](#certificate_template_config) | Tabla | 1 | Certificate template configuration |
| [`certificate_validations`](#certificate_validations) | Tabla | 153 | Public certificate validation history |
| [`graduate_files`](#graduate_files) | Tabla | 41 | Archivos asociados a los graduados del registro académico. Un registro por archivo cargado para un graduado (academic_registration.graduates), con su nombre original, nombre de almacenamiento, tipo MIME, tamaño, quién lo cargó y la fecha de carga; incluye archivos copiados desde la revisión de la solicitud de certificado de grado. |
| [`graduate_program_catalog`](#graduate_program_catalog) | Tabla | 1 | Catálogo central de programas usado por la gestión y revisión de graduados. |
| [`graduates`](#graduates) | Tabla | 10429 | Graduates from the supported academic program types |
| [`graduation_certificate_requests`](#graduation_certificate_requests) | Tabla | 392 | Graduation certificate requests across workflow states |
| [`graduation_certificates`](#graduation_certificates) | Tabla | 161 | Issued graduation certificates with valid QR codes |
| [`graduation_request_review_files`](#graduation_request_review_files) | Tabla | 30 | Archivos cargados durante la revisión de las solicitudes de certificado de grado. Un registro por archivo adjunto a una solicitud (academic_registration.graduation_certificate_requests), con su nombre original, nombre de almacenamiento, tipo MIME, tamaño, quién lo cargó y la fecha de carga. |
| [`signers`](#signers) | Tabla | 1 | Authorized certificate signers |
| [`template_config_changes`](#template_config_changes) | Tabla | 6 | Certificate template change history |

## certificate_template_config

Certificate template configuration

- Clave primaria: `id`
- Filas: 1
- Referencia a: `signer_id` → `academic_registration.signers` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla certificate_template_config. Se genera automáticamente. | PK |
| 2 | `signer_id` | `uuid` | sí | Referencia al registro de academic_registration.signers (id). | FK→academic_registration.signers.id |
| 3 | `institution_logo_url` | `text` | sí | URL del logo institucional que se muestra en la plantilla del certificado de grado. |  |
| 4 | `institution_logo_filename` | `character varying(255)` | sí | Nombre del archivo del logo institucional usado en la plantilla de certificado; acompaña a institution_logo_url. |  |
| 5 | `typography_font` | `character varying(100)` | sí | Tipografía (familia de fuentes CSS) del certificado de grado. Valor por defecto: Arial Narrow, Arial, sans-serif. |  |
| 6 | `signer_title_override` | `character varying(255)` | sí | Signer position or title displayed below the electronic signature or as the default closing title |  |
| 7 | `certificate_content_html` | `text` | no | Contenido HTML del certificado de grado. |  |
| 8 | `version` | `character varying(50)` | sí | Número de versión de la configuración de la plantilla, en formato semántico; por defecto 1.0.0. |  |
| 9 | `status` | `character varying(50)` | sí | Estado de publicación de la configuración de la plantilla de certificado. Valores permitidos: draft (borrador), published (publicada); por defecto draft. |  |
| 10 | `signature_url_override` | `text` | sí | Electronic signature image for the template; supports a base64 data URL or a historical path |  |
| 11 | `signature_filename_override` | `character varying(255)` | sí | Original or normalized electronic signature filename |  |
| 12 | `signer_name_override` | `character varying(255)` | sí | Signer name displayed on the certificate when the electronic signature is active |  |
| 13 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 14 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 15 | `created_by` | `character varying(255)` | sí | Usuario que creó el registro. |  |
| 16 | `updated_by` | `character varying(255)` | sí | Usuario que realizó la última actualización del registro. |  |
| 17 | `is_active` | `boolean` | sí | Indica si la configuración de la plantilla de certificado está activa. |  |
| 18 | `footer_logo_url` | `text` | sí | URL del logo del pie de página del certificado (logo de la ESAP). |  |
| 19 | `footer_logo_filename` | `character varying(255)` | sí | Nombre del archivo del logo del pie de página de la plantilla de certificado; acompaña a footer_logo_url. |  |

## certificate_validations

Public certificate validation history

- Clave primaria: `id`
- Filas: 153
- Referencia a: `certificate_id` → `academic_registration.graduation_certificates` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla certificate_validations. Se genera automáticamente. | PK |
| 2 | `certificate_id` | `uuid` | no | Referencia al registro de academic_registration.graduation_certificates (id). | FK→academic_registration.graduation_certificates.id |
| 3 | `validation_date` | `timestamp without time zone` | sí | Fecha y hora en que se realizó la validación pública del certificado de grado. |  |
| 4 | `ip_address` | `character varying(50)` | sí | Dirección IP desde la que se realizó la validación del certificado. | Identificador en línea (IP) |
| 5 | `user_agent` | `text` | sí | Agente de usuario (navegador) desde el que se consultó la validación pública del certificado. |  |
| 6 | `location` | `character varying(255)` | sí | Ciudad y país desde donde se realizó la validación, cuando está disponible. |  |
| 7 | `result` | `character varying(50)` | no | Resultado de la validación pública del certificado. Valores permitidos: VALID, REVOKED, EXPIRED, NOT_FOUND. |  |
| 8 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |

## graduate_files

Archivos asociados a los graduados del registro académico. Un registro por archivo cargado para un graduado (academic_registration.graduates), con su nombre original, nombre de almacenamiento, tipo MIME, tamaño, quién lo cargó y la fecha de carga; incluye archivos copiados desde la revisión de la solicitud de certificado de grado.

- Clave primaria: `id`
- Filas: 41
- Referencia a: `graduate_id` → `academic_registration.graduates` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla graduate_files. Se genera automáticamente. | PK |
| 2 | `graduate_id` | `uuid` | no | Referencia al registro de academic_registration.graduates (id). | FK→academic_registration.graduates.id |
| 3 | `original_name` | `character varying(255)` | no | Nombre original del archivo cargado para el graduado, tal como lo subió el usuario. |  |
| 4 | `stored_name` | `character varying(255)` | no | Nombre con el que se guarda el archivo en el almacenamiento del sistema. |  |
| 5 | `mime_type` | `character varying(150)` | no | Tipo MIME del archivo adjunto del graduado. |  |
| 6 | `size_bytes` | `integer` | no | Tamaño en bytes del archivo adjunto del graduado. |  |
| 7 | `uploaded_by` | `character varying(255)` | sí | Nombre de la persona que cargó el archivo del graduado; en los archivos copiados desde la revisión de una solicitud, nombre del aprobador o del revisor que la envió. |  |
| 8 | `uploaded_at` | `timestamp without time zone` | sí | Fecha y hora de la carga. |  |

## graduate_program_catalog

Catálogo central de programas usado por la gestión y revisión de graduados.

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla graduate_program_catalog. Se genera automáticamente. | PK |
| 2 | `name` | `character varying(255)` | no | Nombre del programa en el catálogo de programas de graduados. |  |
| 3 | `normalized_name` | `character varying(255)` | no | Clave normalizada del nombre del programa, única en el catálogo: mayúsculas en español, sin caracteres de control, sin tildes, en minúsculas, con todo carácter no alfanumérico convertido en espacio y espacios repetidos reducidos a uno. | única |
| 4 | `created_by` | `character varying(255)` | sí | Usuario que creó el registro. |  |
| 5 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## graduates

Graduates from the supported academic program types

- Clave primaria: `id`
- Filas: 10429

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla graduates. Se genera automáticamente. | PK |
| 2 | `person_id` | `uuid` | no | Identificador UUID de la persona graduada, generado aleatoriamente por el sistema al crear el graduado. |  |
| 3 | `full_name` | `character varying(255)` | no | Nombre completo del graduado. | Nombre de persona |
| 4 | `id_number` | `character varying(50)` | no | Número del documento de identidad del graduado; junto con program_name identifica de forma única el registro. |  |
| 5 | `email` | `character varying(255)` | sí | Correo electrónico del graduado. | Contacto |
| 6 | `phone` | `character varying(50)` | sí | Número de teléfono de contacto del graduado. | Contacto |
| 7 | `program_id` | `uuid` | no | Identificador del programa académico cursado por el graduado; referencia a auth.programas_academicos. |  |
| 8 | `program_name` | `character varying(255)` | no | Nombre del programa académico del que se graduó la persona. |  |
| 9 | `program_type` | `character varying(50)` | no | Tipo de programa académico del que se graduó la persona, por ejemplo Pregrado, Especialización o Maestría. |  |
| 10 | `enrollment_date` | `date` | sí | Fecha de ingreso registrada para el graduado; si no se digita, el sistema asigna la fecha de grado o la fecha de creación del registro. |  |
| 11 | `graduation_date` | `date` | no | Fecha de graduación del estudiante. |  |
| 12 | `ceremony_date` | `date` | sí | Fecha de la ceremonia de grado. |  |
| 13 | `degree_title` | `character varying(255)` | no | Título académico otorgado al graduado (por ejemplo, «Administrador Público»). |  |
| 14 | `diploma_number` | `character varying(100)` | sí | Número del diploma otorgado al graduado; valor único. | única |
| 15 | `registry_reference` | `character varying(100)` | sí | Composite registry, folio and book reference used by issued certificates |  |
| 16 | `resolution_number` | `character varying(100)` | sí | Número de la resolución que otorga el título. |  |
| 17 | `status` | `character varying(50)` | sí | Estado del registro del graduado. Valores permitidos: ACTIVE, REVOKED, SUSPENDED; por defecto ACTIVE. |  |
| 18 | `is_verified` | `boolean` | sí | Indica si el registro del graduado fue verificado. |  |
| 19 | `campus` | `character varying(100)` | sí | Sede donde se graduó la persona. |  |
| 20 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 21 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 22 | `created_by` | `character varying(255)` | sí | Usuario que creó el registro. |  |
| 23 | `updated_by` | `character varying(255)` | sí | Usuario que realizó la última actualización del registro. |  |
| 24 | `id_issue_date` | `date` | sí | Identity document issue date |  |
| 25 | `regional_office_name` | `character varying(255)` | sí | Regional office assigned to the graduate |  |
| 26 | `first_name` | `character varying(255)` | sí | Nombres del graduado. | Nombre de persona |
| 27 | `last_name` | `character varying(255)` | sí | Apellidos del graduado. | Nombre de persona |
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
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla graduation_certificate_requests. Se genera automáticamente. | PK |
| 2 | `request_number` | `character varying(100)` | no | Número único de la solicitud de certificado de grado, con formato GC-AAAA-NNNN (por ejemplo, GC-2025-0001). | única |
| 3 | `requester_type` | `character varying(50)` | no | Tipo de solicitante del certificado. Valores permitidos: GRADUATE (graduado), COMPANY (empresa). |  |
| 4 | `graduate_id` | `uuid` | sí | Identificador del graduado (graduates) al que corresponde la solicitud; nulo cuando la solicitud es externa. |  |
| 5 | `id_number` | `character varying(50)` | no | Número de cédula del graduado. |  |
| 6 | `full_name` | `character varying(255)` | no | Nombre completo del graduado sobre el que se solicita el certificado. | Nombre de persona |
| 7 | `program_name` | `character varying(255)` | no | Nombre del programa académico del graduado, registrado en la solicitud. |  |
| 8 | `graduation_date` | `date` | sí | Fecha de graduación del graduado registrada en la solicitud. |  |
| 9 | `requester_name` | `character varying(255)` | sí | Nombre de la persona que solicita el certificado cuando el solicitante es una empresa. |  |
| 10 | `requester_email` | `character varying(255)` | no | Correo electrónico del solicitante del certificado. | Contacto |
| 11 | `requester_phone` | `character varying(50)` | sí | Número de teléfono del solicitante del certificado. | Contacto |
| 12 | `company_name` | `character varying(255)` | sí | Nombre de la empresa solicitante, cuando la solicitud la hace una empresa. |  |
| 13 | `certificate_type` | `character varying(50)` | sí | Tipo de certificado solicitado. Valores permitidos: STANDARD, OFFICIAL, INTERNATIONAL; por defecto STANDARD. |  |
| 14 | `validation_code` | `character varying(10)` | sí | Código de validación enviado por correo electrónico al graduado que solicita el certificado por primera vez. |  |
| 15 | `validation_expires_at` | `timestamp without time zone` | sí | Fecha y hora en que vence el código de validación de seis dígitos generado para la solicitud del graduado (cinco minutos después de crearlo). |  |
| 16 | `is_validated` | `boolean` | sí | Indica si la solicitud de certificado de grado fue validada. |  |
| 17 | `status` | `character varying(50)` | sí | Estado de la solicitud de certificado. Valores permitidos: PENDING, VALIDATED, PROCESSING, COMPLETED, REJECTED, EXPIRED; por defecto PENDING. |  |
| 18 | `observations` | `text` | sí | Observaciones sobre la solicitud de certificado. |  |
| 19 | `rejection_reason` | `text` | sí | Motivo del rechazo de la solicitud. |  |
| 20 | `request_date` | `timestamp without time zone` | sí | Fecha y hora en que se registró la solicitud; por defecto el momento de creación. |  |
| 21 | `validation_date` | `timestamp without time zone` | sí | Fecha y hora en que se validó la solicitud: al ingresar el código de validación, en la validación automática de la solicitud o al aprobar una revisión manual. |  |
| 22 | `completion_date` | `timestamp without time zone` | sí | Fecha y hora de cierre de la solicitud: cuando se genera el certificado (estado COMPLETED), cuando se rechaza en revisión manual o cuando vence. |  |
| 23 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 24 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 25 | `id_issue_date` | `date` | sí | Fecha de expedición del documento de identidad del graduado. |  |
| 26 | `manual_review` | `boolean` | sí | Indica si la solicitud requiere revisión manual, en los casos en que el graduado no se encuentra en los registros; por defecto falso. |  |
| 27 | `reviewed_at` | `timestamp without time zone` | sí | Fecha y hora de la revisión. |  |
| 28 | `reviewed_by` | `character varying(100)` | sí | Identificador del usuario que revisó la solicitud, tal como lo envía la aplicación (reviewerId); el nombre se guarda aparte en reviewer_name. |  |
| 29 | `reviewer_name` | `character varying(255)` | sí | Nombre del usuario que revisó la solicitud. |  |
| 30 | `review_notes` | `text` | sí | Observaciones registradas en la revisión de la solicitud. |  |
| 31 | `review_resolution` | `character varying(50)` | sí | Resultado de la revisión manual: graduate_found (se encontró o aprobó el graduado), graduate_not_found (no se encontró o se rechazó) o expired (venció sin resolución). review_recommendation guarda la decisión del revisor (APPROVED o REJECTED) y approval_status el estado del flujo de aprobación. |  |
| 32 | `graduate_last_name` | `character varying(255)` | sí | Apellidos del graduado sobre el que se solicita el certificado. | Nombre de persona |
| 33 | `graduate_email` | `character varying(255)` | sí | Correo electrónico del graduado sobre el que se solicita el certificado. | Contacto |
| 34 | `graduate_phone` | `character varying(50)` | sí | Número de teléfono del graduado sobre el que se solicita el certificado. | Contacto |
| 35 | `company_tax_id` | `character varying(50)` | sí | Company tax identifier supplied by the requester |  |
| 36 | `contact_person` | `character varying(255)` | sí | Nombre de la persona que solicita en nombre de la empresa; obligatorio cuando el solicitante es una empresa (COMPANY). |  |
| 37 | `approval_status` | `character varying(50)` | sí | Workflow state: PENDING_APPROVAL, PENDING_HEAD_APPROVAL, APPROVED_FINAL, REJECTED_FINAL, OBSERVATION or HEAD_OBSERVATION |  |
| 38 | `review_recommendation` | `character varying(50)` | sí | Reviewer recommendation: APPROVED or REJECTED; OBSERVATION is reserved for the approver |  |
| 39 | `review_recommendation_reason` | `text` | sí | Justificación de la recomendación emitida en la revisión. |  |
| 40 | `review_payload` | `jsonb` | sí | Data verified by the reviewer before final approval |  |
| 41 | `review_submitted_at` | `timestamp without time zone` | sí | Fecha y hora en que el revisor envió su decisión al aprobador; la solicitud pasa a PENDING_APPROVAL. |  |
| 42 | `review_submitted_by` | `character varying(100)` | sí | Identificador del revisor que envió la revisión al aprobador, tal como lo envía la aplicación (reviewerId); el nombre se guarda en review_submitted_by_name. |  |
| 43 | `review_submitted_by_name` | `character varying(255)` | sí | Nombre del usuario que envió la revisión. |  |
| 44 | `approver_decision` | `character varying(50)` | sí | Decisión del aprobador sobre la revisión: APPROVED, REJECTED u OBSERVATION; se borra cuando el revisor envía una nueva revisión. |  |
| 45 | `approver_notes` | `text` | sí | Observaciones del aprobador sobre la solicitud. |  |
| 46 | `approved_at` | `timestamp without time zone` | sí | Fecha y hora de la aprobación. |  |
| 47 | `approved_by` | `character varying(100)` | sí | Identificador del aprobador que registró la decisión, tal como lo envía la aplicación (approverId); el nombre se guarda en approver_name. |  |
| 48 | `approver_name` | `character varying(255)` | sí | Nombre del usuario que aprobó la solicitud. |  |
| 49 | `review_timeline` | `jsonb` | no | Chronological reviewer and approver workflow trace |  |
| 50 | `head_decision` | `character varying(50)` | sí | Academic registration head decision: APPROVED, REJECTED or OBSERVATION |  |
| 51 | `head_notes` | `text` | sí | Notes or justification from the academic registration head |  |
| 52 | `head_reviewed_at` | `timestamp without time zone` | sí | Date and time when the academic registration head issued a final decision or observation |  |
| 53 | `head_reviewed_by` | `character varying(100)` | sí | Identifier of the academic registration head who issued the decision |  |
| 54 | `head_reviewer_name` | `character varying(255)` | sí | Name of the academic registration head who issued the decision |  |
| 55 | `requester_support_original_name` | `character varying(255)` | sí | Nombre original del archivo de soporte cargado por el solicitante. |  |
| 56 | `requester_support_stored_name` | `character varying(255)` | sí | Nombre con el que se guarda en el almacenamiento el archivo de soporte del solicitante. |  |
| 57 | `requester_support_mime_type` | `character varying(150)` | sí | Tipo MIME del archivo de soporte del solicitante. |  |
| 58 | `requester_support_size_bytes` | `integer` | sí | Tamaño en bytes del archivo de soporte del solicitante. |  |
| 59 | `requester_support_uploaded_at` | `timestamp without time zone` | sí | Fecha y hora de carga del archivo de soporte del solicitante. |  |

## graduation_certificates

Issued graduation certificates with valid QR codes

- Clave primaria: `id`
- Filas: 161
- Referencia a: `graduate_id` → `academic_registration.graduates` (0..* → 0..1); `request_id` → `academic_registration.graduation_certificate_requests` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla graduation_certificates. Se genera automáticamente. | PK |
| 2 | `request_id` | `uuid` | no | Referencia al registro de academic_registration.graduation_certificate_requests (id). | FK→academic_registration.graduation_certificate_requests.id |
| 3 | `graduate_id` | `uuid` | sí | Referencia al registro de academic_registration.graduates (id). | FK→academic_registration.graduates.id |
| 4 | `certificate_number` | `character varying(100)` | no | Número único del certificado de grado expedido, con formato CERT-GR-AAAA-NNNN (por ejemplo, CERT-GR-2025-0001). | única |
| 5 | `verification_code` | `character varying(50)` | no | Código de verificación único del certificado, contenido en el código QR. | única |
| 6 | `full_name` | `character varying(255)` | no | Nombre completo del graduado, registrado en el certificado. | Nombre de persona |
| 7 | `id_number` | `character varying(50)` | no | Número del documento de identidad del graduado al que se emite el certificado. |  |
| 8 | `program_name` | `character varying(255)` | no | Nombre del programa académico del graduado, registrado en el certificado. |  |
| 9 | `program_type` | `character varying(50)` | no | Tipo de programa académico del graduado (por ejemplo, Pregrado, Especializacion o Maestria); se toma del graduado y, si no se digita, se deduce del nombre del programa, con Pregrado por defecto. |  |
| 10 | `degree_title` | `character varying(255)` | no | Título académico otorgado que figura en el certificado. |  |
| 11 | `graduation_date` | `date` | no | Fecha de graduación que figura en el certificado. |  |
| 12 | `diploma_number` | `character varying(100)` | sí | Número del diploma del graduado que figura en el certificado. |  |
| 13 | `registry_reference` | `character varying(100)` | sí | Composite registry, folio and book reference stored when the certificate is issued |  |
| 14 | `campus` | `character varying(100)` | sí | Sede del graduado, registrada en el certificado. |  |
| 15 | `signer_name` | `character varying(255)` | no | Nombre del firmante del certificado. |  |
| 16 | `signer_position` | `character varying(255)` | no | Cargo del firmante del certificado. |  |
| 17 | `signature_url` | `text` | sí | URL de la imagen de la firma usada en el certificado. |  |
| 18 | `pdf_url` | `text` | sí | URL del archivo PDF del certificado. |  |
| 19 | `pdf_filename` | `character varying(255)` | sí | Nombre del archivo PDF del certificado emitido. |  |
| 20 | `status` | `character varying(50)` | sí | Estado del certificado emitido. Valores permitidos: VALID, REVOKED, EXPIRED; por defecto VALID. |  |
| 21 | `issue_date` | `date` | sí | Fecha de expedición del certificado; por defecto la fecha actual. |  |
| 22 | `expiry_date` | `date` | sí | Fecha de expiración del certificado, para los certificados que la tienen. |  |
| 23 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 24 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 25 | `created_by` | `character varying(255)` | sí | Usuario que creó el registro. |  |
| 26 | `regional_office_name` | `character varying(150)` | sí | Regional office associated with the certificate and persisted from manual approvals |  |
| 27 | `template_snapshot` | `jsonb` | sí | JSON snapshot of the template used when the certificate was issued |  |

## graduation_request_review_files

Archivos cargados durante la revisión de las solicitudes de certificado de grado. Un registro por archivo adjunto a una solicitud (academic_registration.graduation_certificate_requests), con su nombre original, nombre de almacenamiento, tipo MIME, tamaño, quién lo cargó y la fecha de carga.

- Clave primaria: `id`
- Filas: 30
- Referencia a: `request_id` → `academic_registration.graduation_certificate_requests` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla graduation_request_review_files. Se genera automáticamente. | PK |
| 2 | `request_id` | `uuid` | no | Referencia al registro de academic_registration.graduation_certificate_requests (id). | FK→academic_registration.graduation_certificate_requests.id |
| 3 | `original_name` | `character varying(255)` | no | Nombre original del archivo cargado en la revisión de la solicitud. |  |
| 4 | `stored_name` | `character varying(255)` | no | Nombre con el que se guarda el archivo en el almacenamiento del sistema. |  |
| 5 | `mime_type` | `character varying(150)` | no | Tipo MIME del archivo de revisión de la solicitud de certificado de grado. |  |
| 6 | `size_bytes` | `integer` | no | Tamaño en bytes del archivo de revisión de la solicitud de certificado de grado. |  |
| 7 | `uploaded_by` | `character varying(255)` | sí | Nombre de la persona que cargó el archivo de revisión de la solicitud; el correo se registra aparte en la línea de tiempo. |  |
| 8 | `uploaded_at` | `timestamp without time zone` | no | Fecha y hora de la carga. |  |

## signers

Authorized certificate signers

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla signers. Se genera automáticamente. | PK |
| 2 | `full_name` | `character varying(255)` | no | Nombre completo del firmante autorizado de certificados de grado. | Nombre de persona |
| 3 | `position` | `character varying(255)` | no | Cargo del firmante (por ejemplo, «Director de Verificación de títulos»). |  |
| 4 | `department` | `character varying(255)` | sí | Dependencia a la que pertenece el firmante. |  |
| 5 | `signature_url` | `text` | sí | URL de la imagen de la firma digital del firmante. |  |
| 6 | `is_active` | `boolean` | sí | Indica si el firmante está activo; por defecto verdadero. |  |
| 7 | `is_primary` | `boolean` | sí | Indica si es el firmante principal, usado por defecto; por defecto falso. |  |
| 8 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 9 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## template_config_changes

Certificate template change history

- Clave primaria: `id`
- Filas: 6
- Referencia a: `template_config_id` → `academic_registration.certificate_template_config` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla template_config_changes. Se genera automáticamente. | PK |
| 2 | `template_config_id` | `integer` | no | Referencia al registro de academic_registration.certificate_template_config (id). | FK→academic_registration.certificate_template_config.id |
| 3 | `change_type` | `character varying(50)` | no | Tipo de cambio registrado sobre la configuración de la plantilla de certificado. Valores esperados: CREATED, UPDATED, PUBLISHED, REVERTED. |  |
| 4 | `field_changed` | `character varying(100)` | sí | Campo de la plantilla que se modificó (por ejemplo, signer_name, logo, content). |  |
| 5 | `old_value` | `text` | sí | Valor del campo antes del cambio en la plantilla. |  |
| 6 | `new_value` | `text` | sí | Valor del campo después del cambio en la plantilla. |  |
| 7 | `changed_by` | `character varying(255)` | no | Usuario que realizó el cambio en la plantilla, según el valor updatedBy que envía la aplicación; «Sistema» si no se informa. |  |
| 8 | `change_date` | `timestamp without time zone` | sí | Fecha y hora del cambio; por defecto, la fecha y hora de registro. |  |
| 9 | `observations` | `text` | sí | Observaciones sobre el cambio realizado en la plantilla. |  |
