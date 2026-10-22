# Viáticos y gastos de viaje (`travel_expenses`)

_Descripción del dominio por documentar._

30 tablas · 0 vistas · 402 columnas · 208 filas · 7 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`analistas_viaticos`](#analistas_viaticos) | Tabla | 0 | Catalogo de analistas del Grupo de Viaticos para asignacion de comisiones y calculo de carga laboral |
| [`comisionados`](#comisionados) | Tabla | 4 | Personas que pueden recibir una comisión de servicio de la ESAP: contratistas, docentes, estudiantes, funcionarios e investigadores. Un registro por persona, identificada por su número de documento, con nombres, contacto, tipo de vinculación, origen de los datos, autorización de tratamiento de datos personales, vigencia del contrato, cuentas bancarias y cargos. Es referenciada por las solicitudes de comisión y los paz y salvos. |
| [`config_campos_formulario`](#config_campos_formulario) | Tabla | 19 | Catálogo de los campos configurables del formulario de solicitud de comisión. Un registro por campo, con su clave, etiqueta, tipo de control, opciones, sección (comisionado, comisión, valores o soportes), orden y límite de caracteres. Sus claves se usan en config_tipo_comisionado y en los campos adicionales de solicitudes_comision. |
| [`config_jornada_laboral`](#config_jornada_laboral) | Tabla | 1 | _Por documentar_ |
| [`config_legalizacion`](#config_legalizacion) | Tabla | 2 | EFDS-1309 — Disparador, plazo (días hábiles) y aviso de la legalización por modalidad de pago. |
| [`config_legalizacion_documentos`](#config_legalizacion_documentos) | Tabla | 42 | EFDS-1309 — Soportes exigidos para legalizar, por tipo de comisionado. Configuración, no código (D-2). |
| [`config_tipo_comisionado`](#config_tipo_comisionado) | Tabla | 7 | Configuración del formulario de solicitud de comisión por tipo de comisionado. Un registro por tipo, con el código del formulario y las listas de campos obligatorios, opcionales y ocultos (claves de config_campos_formulario). Se relaciona con los documentos de soporte exigidos (config_tipo_comisionado_documentos) y con config_legalizacion_documentos. |
| [`config_tipo_comisionado_documentos`](#config_tipo_comisionado_documentos) | Tabla | 24 | Documentos de soporte exigidos por tipo de comisionado. Un registro por combinación de tipo de comisionado y tipo de documento de soporte, que indica si el documento es obligatorio u opcional. Relaciona config_tipo_comisionado con tipos_documento_soporte. |
| [`configuraciones_globales`](#configuraciones_globales) | Tabla | 6 | Parámetros globales del módulo de viáticos. Un registro por parámetro, identificado por su clave, con su valor guardado como texto (correos, horas, números o listas JSON) y su descripción. |
| [`documentos_soporte`](#documentos_soporte) | Tabla | 0 | Archivos de soporte adjuntos a las solicitudes de comisión, como CDP, certificación bancaria, contrato SECOP, RUT o seguridad social. Un registro por archivo, con su tipo de documento, nombre original, nombre de almacenamiento, ruta y tipo MIME. Se relaciona con travel_expenses.solicitudes_comision. |
| [`escalas_viaticos`](#escalas_viaticos) | Tabla | 11 | Escalas de viáticos por rango salarial fijadas por decreto. Un registro por rango de asignación básica y año de vigencia, con la tarifa diaria base que se aplica en la liquidación de las comisiones. |
| [`excepciones_autorizadas_tiquetes`](#excepciones_autorizadas_tiquetes) | Tabla | 0 | Excepciones autorizadas por la Dirección Nacional o el Sindicato para omitir la restricción de ruta corta o de presupuesto agotado en la compra de tiquetes (RF-LIQ-003, RF-LIQ-004). Un registro por excepción, con la solicitud de comisión a la que aplica, el tipo de excepción, la instancia que la autoriza y el documento de soporte. |
| [`legalizacion_reversiones`](#legalizacion_reversiones) | Tabla | 0 | EFDS-1310 — Solicitudes de reversión de una revisión de legalización aprobada. La solicita el analista y la resuelve otra persona; solo antes del registro en SIIF. |
| [`legalizacion_revisiones`](#legalizacion_revisiones) | Tabla | 0 | EFDS-1310 — Trazabilidad de la revisión de la legalización (quién, qué, cuándo). Solo inserción. |
| [`legalizacion_soportes`](#legalizacion_soportes) | Tabla | 0 | EFDS-1309 — PDF de soporte de la legalización, validados por contenido (%PDF-), no por extensión. |
| [`legalizaciones_comision`](#legalizaciones_comision) | Tabla | 0 | EFDS-1309 — Legalización de una comisión: plazo en días hábiles y envío a revisión. |
| [`liquidation_params`](#liquidation_params) | Tabla | 5 | Parámetros configurables de la autoliquidación de viáticos, como los factores por tipo de comisionado y por pernocta. Un registro por parámetro, con su clave, valor guardado como texto, tipo de dato (NUMBER o STRING) y descripción. |
| [`parametros_globales`](#parametros_globales) | Tabla | 1 | Parametros globales configurables del modulo de viaticos y comisiones |
| [`paz_y_salvo_eventos`](#paz_y_salvo_eventos) | Tabla | 0 | Historial de eventos sobre los paz y salvos de los comisionados. Un registro por acción (solicitado, OTP solicitado, firma verificada, consultado o descargado), con el usuario que la realizó, la fecha y el detalle. Se relaciona con travel_expenses.paz_y_salvos. |
| [`paz_y_salvos`](#paz_y_salvos) | Tabla | 0 | _Por documentar_ |
| [`reintegros_comision`](#reintegros_comision) | Tabla | 0 | Reintegros de comisiones pagadas por avance no realizadas o ejecutadas por menos días (RF-PAG-004). |
| [`rutas_restringidas`](#rutas_restringidas) | Tabla | 4 | Catálogo de rutas entre ciudades cuya conexión aérea está restringida (RF-LIQ-003), como las rutas cortas que requieren autorización del Director Nacional o del Sindicato. Un registro por ruta de origen y destino, con la descripción de la restricción y su estado activo. Se consulta al validar los tiquetes de una solicitud de comisión. |
| [`saldos_tiquetes`](#saldos_tiquetes) | Tabla | 0 | Cupo presupuestal de cada dependencia para la compra de tiquetes aéreos. Un registro por dependencia, con el presupuesto inicial, reservado y disponible, y el porcentaje de holgura que se suma al reservar para cubrir la variación del precio del tiquete entre la radicación y la emisión (RF-LIQ-004). |
| [`solicitudes_comision`](#solicitudes_comision) | Tabla | 3 | Solicitudes de comisión de servicio de los comisionados de la ESAP. Un registro por solicitud, con destino, fechas, objeto, itinerario, liquidación de viáticos y gastos de viaje, y los datos de cada etapa del trámite: revisión, autorización, registro presupuestal, obligación, pago o cancelación. Su ciclo se registra en estado_solicitud (BORRADOR, RADICADA, EN_VERIFICACION, DEVUELTA, PAGADA, entre otros); se relaciona con comisionados, auth.user, documentos_soporte, legalizaciones_comision, reintegros_comision y solicitudes_historial_estados. |
| [`solicitudes_historial_estados`](#solicitudes_historial_estados) | Tabla | 0 | Auditoría append-only de transiciones de estado del expediente de comisión (RF-SIS-001 / RF-LIQ-004). |
| [`tarifas_investigadores`](#tarifas_investigadores) | Tabla | 3 | Tarifas diarias de viáticos por categoría de investigador (JUNIOR, ASOCIADO o SENIOR). Un registro por categoría, con la tarifa diaria base que se aplica a los comisionados de tipo INVESTIGADOR. |
| [`tarifas_referencia_tiquetes`](#tarifas_referencia_tiquetes) | Tabla | 42 | Matriz de tarifas de referencia de tiquetes aéreos por ruta, para vuelos nacionales e internacionales. Un registro por ruta de origen y destino, con códigos IATA, tarifa estimada, mínima y máxima de un tiquete de ida, y la fuente de la tarifa (paramétrica, manual o API). Se actualiza por sincronización con API o por parametrización institucional. |
| [`tarifas_regionales_excepcion`](#tarifas_regionales_excepcion) | Tabla | 8 | Tarifas de viáticos de excepción por departamento, según el artículo 5 del Decreto 314 de 2026 para departamentos nuevos. Un registro por departamento, con la tarifa diaria, el decreto de referencia y su estado activo. |
| [`tarifas_transporte_terminal`](#tarifas_transporte_terminal) | Tabla | 11 | Valores máximos reconocidos por trayecto para el desplazamiento a terminales aéreos. Un registro por departamento y ciudad del aeropuerto, con el valor máximo por trayecto que se usa en la liquidación de los gastos de viaje de la comisión. |
| [`tipos_documento_soporte`](#tipos_documento_soporte) | Tabla | 15 | Catálogo de tipos de documento de soporte del trámite de comisiones. Un registro por tipo, con su código, nombre, descripción, instrucciones de validación para quien revisa y campos del formulario que se cotejan con el documento. Se usa en la configuración de documentos por tipo de comisionado, en la de legalización y en los soportes de legalización. |

## analistas_viaticos

Catalogo de analistas del Grupo de Viaticos para asignacion de comisiones y calculo de carga laboral

- Clave primaria: `id`
- Filas: 0
- Referencia a: `usuario_id` → `auth.user` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla analistas_viaticos. Se genera automáticamente. | PK |
| 2 | `usuario_id` | `uuid` | no | Referencia al usuario del sistema (auth.user.id_user) | única FK→auth.user.id_user |
| 3 | `id_persona` | `uuid` | sí | Referencia a la persona en auth.personas |  |
| 4 | `identificacion` | `character varying(50)` | sí | Numero de identificacion del analista | única |
| 5 | `nombre_completo` | `character varying(255)` | no | Nombre completo del analista | Nombre de persona |
| 6 | `username` | `character varying(100)` | no | Usuario de acceso del analista |  |
| 7 | `email` | `character varying(255)` | sí | Correo electrónico del analista de viáticos. | Contacto |
| 8 | `telefono` | `character varying(50)` | sí | Número de teléfono del analista de viáticos. | Contacto |
| 9 | `cargo` | `character varying(255)` | sí | _Por documentar_ |  |
| 10 | `activo` | `boolean` | sí | Indica si el analista esta activo para recibir asignaciones |  |
| 11 | `created_at` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 12 | `updated_at` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 13 | `dependencia_id` | `bigint` | sí | ID de la dependencia a la que pertenece el analista (auth.dependencias.id_dependencia). |  |

## comisionados

Personas que pueden recibir una comisión de servicio de la ESAP: contratistas, docentes, estudiantes, funcionarios e investigadores. Un registro por persona, identificada por su número de documento, con nombres, contacto, tipo de vinculación, origen de los datos, autorización de tratamiento de datos personales, vigencia del contrato, cuentas bancarias y cargos. Es referenciada por las solicitudes de comisión y los paz y salvos.

- Clave primaria: `id`
- Filas: 4

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla comisionados. Se genera automáticamente. | PK |
| 2 | `numero_documento` | `character varying(20)` | no | Número del documento de identidad del comisionado. Es único. | única Identificación |
| 3 | `primer_nombre` | `character varying(100)` | no | Primer nombre del comisionado. | Nombre de persona |
| 4 | `segundo_nombre` | `character varying(100)` | sí | Segundo nombre del comisionado. | Nombre de persona |
| 5 | `primer_apellido` | `character varying(100)` | no | Primer apellido del comisionado. | Nombre de persona |
| 6 | `segundo_apellido` | `character varying(100)` | sí | Segundo apellido del comisionado. | Nombre de persona |
| 7 | `email` | `character varying(150)` | no | Correo electrónico del comisionado. | Contacto |
| 8 | `telefono_contacto` | `character varying(150)` | no | _Por documentar_ | Contacto |
| 9 | `tipo_comisionado` | `character varying(50)` | no | Tipo de vinculación del comisionado con la ESAP. Valores permitidos: CONTRATISTA, DOCENTE, ESTUDIANTE, FUNCIONARIO, INVESTIGADOR. |  |
| 10 | `origen_datos` | `character varying(50)` | no | Fuente de la que se obtuvieron los datos del comisionado: HUMANO (API de Talento Humano), ESAP (auth.personas) o SECOP. |  |
| 11 | `autorizacion_habeas_data` | `boolean` | no | Indica si el comisionado autorizó el tratamiento de datos personales (habeas data). |  |
| 12 | `fecha_autorizacion_habeas_data` | `timestamp without time zone` | sí | Fecha y hora en que el comisionado autorizó el tratamiento de datos personales (habeas data). |  |
| 13 | `ip_registro_habeas_data` | `character varying(45)` | sí | Dirección IP desde la que se registró la autorización de tratamiento de datos personales (habeas data). Admite IPv4 e IPv6. | Identificador en línea (IP) |
| 14 | `creado_en` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 15 | `actualizado_en` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 16 | `id_dependencia` | `bigint` | sí | ID de la dependencia institucional (auth.dependencias) del comisionado. Se obtiene desde auth.personas.id_dependencia al consultar por número de documento. |  |
| 17 | `es_facturador_electronico` | `boolean` | no | Indica si el comisionado contratista es facturador electrónico registrado ante la DIAN. |  |
| 18 | `fecha_inicio_contrato` | `date` | sí | Fecha de inicio de la vinculación contractual o laboral. |  |
| 19 | `fecha_fin_contrato` | `date` | sí | Fecha de terminación o vencimiento del contrato/vinculación laboral. |  |
| 20 | `cuentas_bancarias` | `jsonb` | sí | Historial y lista de cuentas bancarias del comisionado (banco, tipo_cuenta, numero_cuenta, url_certificado, etc.). |  |
| 21 | `cargos` | `jsonb` | sí | Historial y asignación de cargos del comisionado con su respectivo salario relacional (formato JSONB). Reemplaza y unifica las columnas cargo y salario_basico. |  |

## config_campos_formulario

Catálogo de los campos configurables del formulario de solicitud de comisión. Un registro por campo, con su clave, etiqueta, tipo de control, opciones, sección (comisionado, comisión, valores o soportes), orden y límite de caracteres. Sus claves se usan en config_tipo_comisionado y en los campos adicionales de solicitudes_comision.

- Clave primaria: `id`
- Filas: 19

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla config_campos_formulario. Se genera automáticamente. | PK |
| 2 | `clave` | `character varying(100)` | no | Identificador único del campo del formulario. | única |
| 3 | `etiqueta` | `character varying(200)` | no | Texto que se muestra como rótulo del campo en el formulario. |  |
| 4 | `tipo_campo` | `character varying(50)` | no | Tipo de control del campo en el formulario: TEXT, TEXTAREA, SELECT, DATE, NUMBER, BOOLEAN, CURRENCY o DOCUMENT. |  |
| 5 | `placeholder` | `character varying(200)` | sí | Texto de ayuda que se muestra dentro del campo vacío. |  |
| 6 | `opciones` | `jsonb` | sí | Opciones de los campos de selección, en JSON: lista de objetos {value, label}. |  |
| 7 | `grupo` | `character varying(50)` | sí | Sección del formulario a la que pertenece el campo: comisionado, comision, valores o soportes. Los campos se ordenan por grupo y por orden. |  |
| 8 | `orden` | `integer` | no | Posición del campo en el orden de presentación del formulario. |  |
| 9 | `activo` | `boolean` | no | Indica si el campo de formulario está activo. |  |
| 10 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 11 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 12 | `limite_caracteres` | `integer` | sí | Límite máximo de caracteres permitido para el campo. Por defecto 250 caracteres, configurable por administrador. |  |

## config_jornada_laboral

_Por documentar._

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla config_jornada_laboral. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(50)` | no | Código único de la jornada laboral. | única |
| 3 | `nombre` | `character varying(100)` | no | Nombre de la jornada laboral. |  |
| 4 | `hora_inicio` | `character varying(5)` | no | Hora de inicio de la jornada laboral, en formato HH:MM. |  |
| 5 | `hora_fin` | `character varying(5)` | no | Hora de fin de la jornada laboral, en formato HH:MM. |  |
| 6 | `dias_laborales` | `jsonb` | no | Días hábiles de la semana, en formato JSON (lista de números: 0 = domingo, 1 = lunes … 6 = sábado). Por defecto, [1, 2, 3, 4, 5] (lunes a viernes). |  |
| 7 | `dias_anticipacion_minima` | `integer` | no | Días hábiles mínimos de anticipación para radicar una comisión ordinaria (RF-EXT-001); por defecto, 14. Una solicitud radicada con menos días hábiles queda marcada como extemporánea y requiere autorización de la Dirección Nacional. |  |
| 8 | `dias_umbral_avance` | `integer` | no | Días hábiles de umbral para definir la modalidad de pago al expedir el registro presupuestal: con días hábiles previos iguales o mayores, AVANCE; con menos, RECONOCIMIENTO_POSTERIOR (RF-PRE-003). Por defecto, 5. |  |
| 9 | `activo` | `boolean` | no | Indica si la configuración de jornada laboral está activa. |  |
| 10 | `descripcion` | `text` | sí | Descripción de la jornada laboral. |  |
| 11 | `creado_en` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 12 | `actualizado_en` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 13 | `actualizado_por` | `character varying(100)` | sí | Usuario que realizó la última actualización del registro. |  |

## config_legalizacion

EFDS-1309 — Disparador, plazo (días hábiles) y aviso de la legalización por modalidad de pago.

- Clave primaria: `modalidad_pago`
- Filas: 2

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `modalidad_pago` | `character varying(50)` | no | Clave primaria de la tabla config_legalizacion: modalidad pago. | PK |
| 2 | `estado_disparador` | `character varying(50)` | no | Estado de la solicitud a partir del cual se abre la legalización. Pendiente D-1 para RECONOCIMIENTO_POSTERIOR. |  |
| 3 | `plazo_dias_habiles` | `integer` | no | Plazo en días hábiles para legalizar la comisión según la modalidad de pago. |  |
| 4 | `dias_aviso_por_vencer` | `integer` | no | Días hábiles restantes del plazo de legalización a partir de los cuales la legalización se marca POR_VENCER y se envía el aviso. No puede ser negativo; por defecto, 2. |  |
| 5 | `hora_corte` | `character varying(5)` | no | Hora (Colombia, HH:MM) en que vence el último día hábil del plazo. Alineada con el corte de jornada de 16:30. |  |
| 6 | `activo` | `boolean` | no | Indica si la configuración de legalización está activa. |  |
| 7 | `actualizado_por_id` | `uuid` | sí | Identificador (auth."user".id_user) del usuario autenticado que actualizó por última vez la configuración de legalización. |  |
| 8 | `creado_en` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `actualizado_en` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## config_legalizacion_documentos

EFDS-1309 — Soportes exigidos para legalizar, por tipo de comisionado. Configuración, no código (D-2).

- Clave primaria: `id`
- Filas: 42
- Referencia a: `config_tipo_comisionado_id` → `travel_expenses.config_tipo_comisionado` (1..* → 1); `tipo_documento_soporte_id` → `travel_expenses.tipos_documento_soporte` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla config_legalizacion_documentos. Se genera automáticamente. | PK |
| 2 | `config_tipo_comisionado_id` | `uuid` | no | Referencia al registro de travel_expenses.config_tipo_comisionado (id). | FK→travel_expenses.config_tipo_comisionado.id |
| 3 | `tipo_documento_soporte_id` | `uuid` | no | Referencia al registro de travel_expenses.tipos_documento_soporte (id). | FK→travel_expenses.tipos_documento_soporte.id |
| 4 | `tipo_requisito` | `character varying(20)` | no | Indica si el soporte es obligatorio u opcional para legalizar. Valores permitidos: OBLIGATORIO, OPCIONAL. |  |
| 5 | `condicion` | `character varying(40)` | sí | Cuándo aplica: NULL = siempre; TRANSPORTE_AEREO = solo con tramo aéreo; COMISION_EXTERNA = solo si se cumplió fuera de la ESAP. |  |
| 6 | `orden` | `integer` | no | Posición del soporte exigido en el orden de presentación. |  |
| 7 | `activo` | `boolean` | no | Indica si el soporte exigido para legalizar está activo. |  |
| 8 | `creado_en` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `actualizado_en` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## config_tipo_comisionado

Configuración del formulario de solicitud de comisión por tipo de comisionado. Un registro por tipo, con el código del formulario y las listas de campos obligatorios, opcionales y ocultos (claves de config_campos_formulario). Se relaciona con los documentos de soporte exigidos (config_tipo_comisionado_documentos) y con config_legalizacion_documentos.

- Clave primaria: `id`
- Filas: 7

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla config_tipo_comisionado. Se genera automáticamente. | PK |
| 2 | `tipo_comisionado` | `character varying(50)` | no | Tipo de comisionado al que aplica la configuración. Es único. | única |
| 3 | `codigo_formulario` | `character varying(50)` | no | _Por documentar_ |  |
| 4 | `campos_obligatorios` | `jsonb` | no | Lista JSON de claves de campos obligatorios para el tipo de comisionado. Las claves coinciden con config_campos_formulario.clave y con las propiedades de la solicitud; un campo que también figure como opcional u oculto no se exige. |  |
| 5 | `campos_opcionales` | `jsonb` | no | Lista JSON de claves de campos opcionales para el tipo de comisionado, con las mismas claves de config_campos_formulario.clave. Un campo opcional no se exige aunque esté en campos_obligatorios. |  |
| 6 | `campos_ocultos` | `jsonb` | no | Lista JSON de claves de campos que no se muestran en el formulario para el tipo de comisionado, con las mismas claves de config_campos_formulario.clave. Un campo oculto no se exige. |  |
| 7 | `activo` | `boolean` | no | Indica si la configuración del tipo de comisionado está activa. |  |
| 8 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## config_tipo_comisionado_documentos

Documentos de soporte exigidos por tipo de comisionado. Un registro por combinación de tipo de comisionado y tipo de documento de soporte, que indica si el documento es obligatorio u opcional. Relaciona config_tipo_comisionado con tipos_documento_soporte.

- Clave primaria: `id`
- Filas: 24
- Referencia a: `config_tipo_comisionado_id` → `travel_expenses.config_tipo_comisionado` (1..* → 1); `tipo_documento_soporte_id` → `travel_expenses.tipos_documento_soporte` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla config_tipo_comisionado_documentos. Se genera automáticamente. | PK |
| 2 | `config_tipo_comisionado_id` | `uuid` | no | Referencia al registro de travel_expenses.config_tipo_comisionado (id). | FK→travel_expenses.config_tipo_comisionado.id |
| 3 | `tipo_documento_soporte_id` | `uuid` | no | Referencia al registro de travel_expenses.tipos_documento_soporte (id). | FK→travel_expenses.tipos_documento_soporte.id |
| 4 | `tipo_requisito` | `character varying(20)` | no | Indica si el documento de soporte es obligatorio u opcional para el tipo de comisionado. Valores permitidos: OBLIGATORIO, OPCIONAL. |  |
| 5 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 6 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## configuraciones_globales

Parámetros globales del módulo de viáticos. Un registro por parámetro, identificado por su clave, con su valor guardado como texto (correos, horas, números o listas JSON) y su descripción.

- Clave primaria: `clave`
- Filas: 6

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `clave` | `character varying(100)` | no | Clave primaria de la tabla configuraciones_globales: clave. | PK |
| 2 | `valor` | `text` | no | Valor del parámetro identificado por la clave, guardado como texto. Hay valores de correo, hora (HH:MM), número y lista JSON (DIAS_LABORALES_SEMANA); el servicio solo lee CORREO_DESTINO_SST como texto. |  |
| 3 | `descripcion` | `text` | sí | Descripción de la configuración global. |  |
| 4 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 5 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## documentos_soporte

Archivos de soporte adjuntos a las solicitudes de comisión, como CDP, certificación bancaria, contrato SECOP, RUT o seguridad social. Un registro por archivo, con su tipo de documento, nombre original, nombre de almacenamiento, ruta y tipo MIME. Se relaciona con travel_expenses.solicitudes_comision.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `solicitud_id` → `travel_expenses.solicitudes_comision` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla documentos_soporte. Se genera automáticamente. | PK |
| 2 | `solicitud_id` | `uuid` | no | Referencia al registro de travel_expenses.solicitudes_comision (id). | FK→travel_expenses.solicitudes_comision.id |
| 3 | `tipo_documento` | `character varying(50)` | no | Tipo de documento de soporte de la solicitud. Valores permitidos: CDP, CERT_BANCARIA, CONTRATO_SECOP, RUT, SEGURIDAD_SOCIAL. |  |
| 4 | `nombre_archivo_original` | `character varying(255)` | no | Nombre del archivo tal como lo cargó el usuario. |  |
| 5 | `nombre_archivo_seguro` | `character varying(255)` | no | Nombre con el que se guarda el archivo en el almacenamiento, generado por el sistema a partir del nombre original sin caracteres especiales y una marca de tiempo (por ejemplo, pago_<timestamp>_<nombre>.pdf). |  |
| 6 | `url_repositorio` | `character varying(512)` | no | Ruta relativa del archivo en el almacenamiento local del servicio (/uploads/<solicitud_id>/<nombre_archivo_seguro>), servida por el mismo servicio bajo /uploads. En el reporte de revocatoria guarda el PDF en base64. |  |
| 7 | `creado_en` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 8 | `tipo_mime` | `character varying(100)` | sí | Tipo MIME del archivo (por ejemplo, application/pdf). |  |

## escalas_viaticos

Escalas de viáticos por rango salarial fijadas por decreto. Un registro por rango de asignación básica y año de vigencia, con la tarifa diaria base que se aplica en la liquidación de las comisiones.

- Clave primaria: `id`
- Filas: 11

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla escalas_viaticos. Se genera automáticamente. | PK |
| 2 | `decreto_vigente` | `character varying(50)` | no | Decreto que fija la escala de viáticos. |  |
| 3 | `ano_vigencia` | `integer` | no | Año de vigencia de la escala de viáticos. |  |
| 4 | `rango_minimo` | `numeric(12,2)` | no | Límite inferior, inclusivo, del rango de asignación básica al que aplica la tarifa. Para estudiantes se compara con el SMMLV. |  |
| 5 | `rango_maximo` | `numeric(12,2)` | no | Límite superior, inclusivo, del rango de asignación básica al que aplica la tarifa. Para estudiantes se compara con el SMMLV. |  |
| 6 | `tarifa_diaria` | `numeric(12,2)` | no | Valor diario de viáticos para el rango, en pesos colombianos; es la tarifa diaria base de la liquidación. |  |
| 7 | `creado_en` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 8 | `activo` | `boolean` | no | Indica si la escala de viáticos está activa. |  |

## excepciones_autorizadas_tiquetes

Excepciones autorizadas por la Dirección Nacional o el Sindicato para omitir la restricción de ruta corta o de presupuesto agotado en la compra de tiquetes (RF-LIQ-003, RF-LIQ-004). Un registro por excepción, con la solicitud de comisión a la que aplica, el tipo de excepción, la instancia que la autoriza y el documento de soporte.

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla excepciones_autorizadas_tiquetes. Se genera automáticamente. | PK |
| 2 | `solicitud_id` | `uuid` | no | Identificador de la solicitud de comisión a la que aplica la excepción. |  |
| 3 | `tipo_excepcion` | `character varying(50)` | no | Restricción de tiquetes que se exceptúa: RUTA_CORTA o PRESUPUESTO_AGOTADO (RF-LIQ-003, RF-LIQ-004). |  |
| 4 | `autorizado_por` | `character varying(150)` | no | Instancia que autoriza la excepción de tiquetes: DIRECTOR_NACIONAL o SINDICATO. |  |
| 5 | `numero_documento_soporte` | `character varying(100)` | no | _Por documentar_ |  |
| 6 | `documento_soporte_url` | `character varying(500)` | sí | URL o ruta del documento que soporta la excepción. |  |
| 7 | `comentarios` | `text` | sí | Comentarios sobre la excepción autorizada. |  |
| 8 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |

## legalizacion_reversiones

EFDS-1310 — Solicitudes de reversión de una revisión de legalización aprobada. La solicita el analista y la resuelve otra persona; solo antes del registro en SIIF.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `legalizacion_id` → `travel_expenses.legalizaciones_comision` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla legalizacion_reversiones. Se genera automáticamente. | PK |
| 2 | `legalizacion_id` | `uuid` | no | Referencia al registro de travel_expenses.legalizaciones_comision (id). | FK→travel_expenses.legalizaciones_comision.id |
| 3 | `estado` | `character varying(20)` | no | Estado de la solicitud de reversión: pendiente, aprobada o rechazada. |  |
| 4 | `motivo` | `text` | no | Motivo de la solicitud de reversión. Debe tener al menos 10 caracteres. |  |
| 5 | `solicitada_por_id` | `uuid` | no | Identificador (auth."user".id_user) del usuario autenticado que solicita la reversión. |  |
| 6 | `solicitada_en` | `timestamp with time zone` | no | Fecha y hora de la solicitud. |  |
| 7 | `resuelta_por_id` | `uuid` | sí | Identificador (auth."user".id_user) del usuario autenticado que resuelve la reversión. Debe ser distinto de quien la solicitó. |  |
| 8 | `resuelta_en` | `timestamp with time zone` | sí | Fecha y hora en que se resolvió la reversión. |  |
| 9 | `observacion_resolucion` | `text` | sí | Observación registrada al resolver la reversión. Es obligatoria al rechazarla (mínimo 10 caracteres) y opcional al aprobarla. |  |

## legalizacion_revisiones

EFDS-1310 — Trazabilidad de la revisión de la legalización (quién, qué, cuándo). Solo inserción.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `legalizacion_id` → `travel_expenses.legalizaciones_comision` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla legalizacion_revisiones. Se genera automáticamente. | PK |
| 2 | `legalizacion_id` | `uuid` | no | Referencia al registro de travel_expenses.legalizaciones_comision (id). | FK→travel_expenses.legalizaciones_comision.id |
| 3 | `soporte_id` | `uuid` | sí | Identificador del soporte de legalización revisado (legalizacion_soportes.id), en las acciones SOPORTE_APROBADO y SOPORTE_RECHAZADO; nulo en las demás. |  |
| 4 | `accion` | `character varying(40)` | no | Acción registrada en la revisión de la legalización. Valores permitidos: APROBACION, DEVOLUCION, EXPORTACION_SIIF, REGISTRO_SIIF_Y_CIERRE, REVERSION_APROBADA, REVERSION_RECHAZADA, REVERSION_SOLICITADA, SOPORTE_APROBADO, SOPORTE_RECHAZADO. |  |
| 5 | `observacion` | `text` | sí | Observación registrada en la revisión de la legalización. |  |
| 6 | `detalle` | `jsonb` | sí | Información adicional de la acción, en JSON. Según la acción: SOPORTE_APROBADO/RECHAZADO {nombreArchivo, sha256}; DEVOLUCION {numeroDevolucion, motivo, valorPagado, valorLegalizado}; APROBACION {soportesAprobados}; REGISTRO_SIIF_Y_CIERRE {numeroRegistroSiif, fechaRegistroSiif, valores, días y fechas reales}; reversiones {reversionId, solicitadaPorId}. |  |
| 7 | `usuario_id` | `uuid` | no | Identificador (auth."user".id_user) del usuario autenticado que realizó la acción. |  |
| 8 | `creado_en` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## legalizacion_soportes

EFDS-1309 — PDF de soporte de la legalización, validados por contenido (%PDF-), no por extensión.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `legalizacion_id` → `travel_expenses.legalizaciones_comision` (0..1 → 1); `tipo_documento_soporte_id` → `travel_expenses.tipos_documento_soporte` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla legalizacion_soportes. Se genera automáticamente. | PK |
| 2 | `legalizacion_id` | `uuid` | no | Referencia al registro de travel_expenses.legalizaciones_comision (id). | FK→travel_expenses.legalizaciones_comision.id |
| 3 | `tipo_documento_soporte_id` | `uuid` | no | Referencia al registro de travel_expenses.tipos_documento_soporte (id). | FK→travel_expenses.tipos_documento_soporte.id |
| 4 | `nombre_archivo_original` | `character varying(255)` | no | Nombre del archivo PDF tal como lo cargó el usuario. |  |
| 5 | `ruta_relativa` | `character varying(512)` | no | Ruta del archivo PDF relativa a la raíz de almacenamiento del servicio, con la forma <solicitud_id>/legalizacion/<uuid>.pdf. No se entrega al cliente; el archivo se descarga por un endpoint autenticado. |  |
| 6 | `tamano_bytes` | `integer` | no | Tamaño en bytes del archivo PDF de soporte de la legalización. |  |
| 7 | `sha256` | `character(64)` | no | Huella SHA-256 del archivo, en hexadecimal (64 caracteres). |  |
| 8 | `cargado_por_id` | `uuid` | no | Identificador (auth."user".id_user) del usuario autenticado que cargó el soporte. |  |
| 9 | `creado_en` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 10 | `revision` | `character varying(20)` | sí | Resultado de la revisión del soporte por parte del analista: APROBADO o RECHAZADO (EFDS-1310). Nulo mientras el soporte no se ha revisado. |  |
| 11 | `observacion_revision` | `text` | sí | Observación del analista en la revisión del soporte (EFDS-1310). |  |
| 12 | `revisado_por_id` | `uuid` | sí | Identificador del analista que revisó el soporte (EFDS-1310). |  |
| 13 | `revisado_en` | `timestamp with time zone` | sí | Fecha y hora en que el analista revisó el soporte (EFDS-1310). |  |

## legalizaciones_comision

EFDS-1309 — Legalización de una comisión: plazo en días hábiles y envío a revisión.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `solicitud_id` → `travel_expenses.solicitudes_comision` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla legalizaciones_comision. Se genera automáticamente. | PK |
| 2 | `solicitud_id` | `uuid` | no | Referencia al registro de travel_expenses.solicitudes_comision (id). | única FK→travel_expenses.solicitudes_comision.id |
| 3 | `modalidad_pago` | `character varying(50)` | no | Modalidad de pago de la comisión (AVANCE o RECONOCIMIENTO_POSTERIOR), copiada de solicitudes_comision.modalidad_pago al abrir la legalización; selecciona la configuración de legalización. |  |
| 4 | `estado_disparador` | `character varying(50)` | no | Estado de la solicitud que abrió la legalización (AUTORIZADA, COMPROMETIDA, OBLIGADA o PAGADA), copiado de config_legalizacion al abrirla. |  |
| 5 | `fecha_disparo` | `timestamp with time zone` | no | Fecha y hora en que se disparó la legalización de la comisión. |  |
| 6 | `fecha_base_plazo` | `timestamp with time zone` | no | Desde cuándo corre el plazo: el fin del día más tardío entre el regreso planeado (fecha_fin) y el pago (fecha_pago), en hora de Colombia. Migración 453. |  |
| 7 | `plazo_dias_habiles` | `integer` | no | Plazo en días hábiles para legalizar la comisión. |  |
| 8 | `hora_corte` | `character varying(5)` | no | Hora límite del último día del plazo de legalización, en formato HH:MM. Se copia de config_legalizacion al abrir la legalización y no cambia si la configuración cambia después. |  |
| 9 | `fecha_limite` | `timestamp with time zone` | no | Fecha y hora límite para legalizar la comisión. |  |
| 10 | `calendario_incompleto` | `boolean` | no | TRUE si el plazo cruzó un año sin festivos cargados en auth.festivos_colombia: la fecha límite puede adelantarse. |  |
| 11 | `fecha_envio` | `timestamp with time zone` | sí | Momento en que el comisionado envió la legalización completa a revisión. NULL = aún en cargue. |  |
| 12 | `enviada_por_id` | `uuid` | sí | Identificador (auth."user".id_user) del usuario autenticado que envió la legalización a revisión. Se registra junto con fecha_envio y se borra si la legalización se devuelve. |  |
| 13 | `notificado_por_vencer_en` | `timestamp with time zone` | sí | Fecha y hora en que se notificó que el plazo de legalización estaba por vencer. |  |
| 14 | `notificado_vencido_en` | `timestamp with time zone` | sí | Fecha y hora en que se notificó que el plazo de legalización venció. |  |
| 15 | `creado_en` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 16 | `actualizado_en` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 17 | `revision_aprobada_en` | `timestamp with time zone` | sí | Fecha y hora en que el analista aprobó la revisión de los soportes de la legalización (EFDS-1310). Es obligatoria para exportar a SIIF y cerrar; se borra si la legalización se devuelve o se aprueba una reversión. |  |
| 18 | `revision_aprobada_por_id` | `uuid` | sí | Identificador del usuario que aprobó la revisión de la legalización (EFDS-1310). |  |
| 19 | `devuelta_en` | `timestamp with time zone` | sí | EFDS-1310 — Última devolución al comisionado. La solicitud sigue en PENDIENTE_LEGALIZACION (C-2). |  |
| 20 | `devuelta_por_id` | `uuid` | sí | Identificador del usuario que devolvió la legalización (EFDS-1310). |  |
| 21 | `observacion_devolucion` | `text` | sí | Observación registrada al devolver la legalización (EFDS-1310). |  |
| 22 | `numero_devoluciones` | `integer` | no | Número de veces que se ha devuelto la legalización. Por defecto, 0 (EFDS-1310). |  |
| 23 | `siif_exportado_en` | `timestamp with time zone` | sí | Fecha y hora de exportación de la legalización al SIIF (EFDS-1310). |  |
| 24 | `siif_exportado_por_id` | `uuid` | sí | Identificador del usuario que exportó la legalización al SIIF (EFDS-1310). |  |
| 25 | `numero_registro_siif` | `character varying(100)` | sí | Número del registro de la legalización en el SIIF (EFDS-1310). |  |
| 26 | `fecha_registro_siif` | `date` | sí | Fecha del registro de la legalización en el SIIF (EFDS-1310). |  |
| 27 | `registrado_siif_por_id` | `uuid` | sí | Identificador del usuario que registró la legalización en el SIIF (EFDS-1310). |  |
| 28 | `valor_pagado` | `numeric(14,2)` | sí | Valor pagado de la comisión, copiado de solicitudes_comision.valor_pagado (pago registrado por Tesorería) al registrar la legalización en SIIF y cerrarla; base para calcular el reintegro. |  |
| 29 | `valor_legalizado` | `numeric(14,2)` | sí | Valor legalizado de la comisión, digitado por el analista al registrar la legalización en SIIF, después de aprobar la revisión de los soportes. No puede superar el valor pagado; si lo supera, la legalización se devuelve al comisionado. |  |
| 30 | `valor_reintegro` | `numeric(14,2)` | sí | EFDS-1310 — valor_pagado - valor_legalizado cuando el viaje fue menor; > 0 dispara el evento de reintegro (EFDS-1308). |  |
| 31 | `dias_reales` | `numeric(6,2)` | sí | Número de días reales de la comisión. Con las fechas reales del GF-FO-032 se calcula como noches reales más uno; si no hay fechas reales, lo digita el analista (número mayor o igual a cero). |  |
| 32 | `observaciones_cierre` | `text` | sí | Observaciones registradas al cerrar la legalización (EFDS-1310). |  |
| 33 | `cerrada_en` | `timestamp with time zone` | sí | EFDS-1310 — Expediente de legalización cerrado: la fila y sus soportes quedan inmutables (triggers). |  |
| 34 | `cerrada_por_id` | `uuid` | sí | Identificador del usuario que cerró la legalización (EFDS-1310). |  |
| 35 | `fecha_inicio_real` | `date` | sí | Fecha en que el comisionado realmente inició la comisión, según el GF-FO-032 V2. |  |
| 36 | `fecha_fin_real` | `date` | sí | Fecha en que el comisionado realmente terminó la comisión, según el GF-FO-032 V2. No cambia el plazo, que sale de la fecha planeada. |  |
| 37 | `comision_externa` | `boolean` | sí | TRUE si la comisión se cumplió fuera de la ESAP: exige el certificado de la entidad externa. NULL = no declarado. |  |
| 38 | `entidad_externa` | `character varying(200)` | sí | Nombre de la entidad externa donde se cumplió la comisión, cuando se cumplió fuera de la ESAP (comision_externa verdadero); entre 2 y 200 caracteres. En ese caso se exige el certificado de la entidad externa. |  |
| 39 | `cumplimiento_registrado_en` | `timestamp with time zone` | sí | Fecha y hora en que el comisionado registró los datos de cumplimiento del formato GF-FO-032 (fechas reales de la comisión y si se cumplió fuera de la ESAP). Es requisito para enviar la legalización. |  |
| 40 | `cumplimiento_registrado_por_id` | `uuid` | sí | Identificador del usuario que registró el cumplimiento de la comisión (EFDS-1310). |  |
| 41 | `reintegro_viaje_corto` | `numeric(14,2)` | sí | Al cerrar: parte del reintegro por los días no viajados, con las tarifas de la liquidación pagada. |  |

## liquidation_params

Parámetros configurables de la autoliquidación de viáticos, como los factores por tipo de comisionado y por pernocta. Un registro por parámetro, con su clave, valor guardado como texto, tipo de dato (NUMBER o STRING) y descripción.

- Clave primaria: `id`
- Filas: 5

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla liquidation_params. Se genera automáticamente. | PK |
| 2 | `clave` | `character varying(50)` | no | Nombre único del parámetro de liquidación. | única |
| 3 | `valor` | `character varying(255)` | no | Valor del parámetro de liquidación, guardado como texto; la columna tipo indica NUMBER o STRING. Los parámetros numéricos se convierten con Number() (FACTOR_CONTRATISTA, FACTOR_SIN_PERNOCTA, ANO_VIGENCIA_ESCALAS, HOLGURA_TIQUETES_PORCENTAJE). |  |
| 4 | `tipo` | `character varying(20)` | no | Tipo de dato del parámetro de liquidación. |  |
| 5 | `descripcion` | `character varying(255)` | sí | Descripción del parámetro de liquidación. |  |
| 6 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 7 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## parametros_globales

Parametros globales configurables del modulo de viaticos y comisiones

- Clave primaria: `clave`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `clave` | `character varying(100)` | no | Clave primaria de la tabla parametros_globales: clave. | PK |
| 2 | `valor` | `character varying(255)` | no | Valor del parámetro global, guardado como texto; la columna tipo indica el tipo (number). LIMITE_CARGA_SATURACION se convierte a entero (por defecto, 12). |  |
| 3 | `tipo` | `character varying(50)` | no | Tipo de dato del parámetro global. |  |
| 4 | `descripcion` | `text` | sí | Descripción del parámetro global. |  |
| 5 | `editable` | `boolean` | sí | Indica si el parámetro global puede modificarse. |  |
| 6 | `creado_en` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 7 | `actualizado_en` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |

## paz_y_salvo_eventos

Historial de eventos sobre los paz y salvos de los comisionados. Un registro por acción (solicitado, OTP solicitado, firma verificada, consultado o descargado), con el usuario que la realizó, la fecha y el detalle. Se relaciona con travel_expenses.paz_y_salvos.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `paz_y_salvo_id` → `travel_expenses.paz_y_salvos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | Identificador único del registro en la tabla paz_y_salvo_eventos. Se genera automáticamente. | PK |
| 2 | `paz_y_salvo_id` | `uuid` | no | Referencia al registro de travel_expenses.paz_y_salvos (id). | FK→travel_expenses.paz_y_salvos.id |
| 3 | `usuario_id` | `uuid` | no | Identificador (auth."user".id_user) del usuario autenticado que realizó la acción sobre el paz y salvo. |  |
| 4 | `accion` | `character varying(30)` | no | Acción registrada sobre el paz y salvo. Valores permitidos: CONSULTADO, DESCARGADO, FIRMA_VERIFICADA, OTP_SOLICITADO, SOLICITADO. |  |
| 5 | `creado_en` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 6 | `detalle` | `jsonb` | no | Información adicional del evento, en JSON. Vacío ({}) en SOLICITADO, OTP_SOLICITADO y CONSULTADO; en FIRMA_VERIFICADA guarda evidencia, metodo, context, verificadoEn y archivoSha256; en DESCARGADO, archivoSha256. |  |

## paz_y_salvos

_Por documentar._

- Clave primaria: `id`
- Filas: 0
- Referencia a: `comisionado_id` → `travel_expenses.comisionados` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla paz_y_salvos. | PK |
| 2 | `comisionado_id` | `uuid` | no | Referencia al registro de travel_expenses.comisionados (id). | FK→travel_expenses.comisionados.id |
| 3 | `solicitado_por_id` | `uuid` | no | Identificador (auth."user".id_user) del usuario autenticado que solicitó el paz y salvo. Solo esa persona puede firmarlo. |  |
| 4 | `contenido` | `jsonb` | no | Contenido del paz y salvo, en JSON: id, comisionadoId, nombre, documento, coordinadoraId, coordinadoraNombre, territorialId, cargoFirmante y solicitadoEn. Se guarda con su hash en contenido_sha256. |  |
| 5 | `contenido_sha256` | `character varying(64)` | no | Huella SHA-256 del contenido del paz y salvo, en hexadecimal. |  |
| 6 | `creado_en` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 7 | `firma` | `jsonb` | sí | Datos de la firma electrónica por código OTP enviado al correo, en JSON: id, email, fechaFirma, metodo (OTP_EMAIL) y context. Se registra junto con firmado_en y archivo_sha256. |  |
| 8 | `firmado_en` | `timestamp with time zone` | sí | Fecha y hora de la firma. |  |
| 9 | `archivo_sha256` | `character varying(64)` | sí | Huella SHA-256 del archivo firmado del paz y salvo, en hexadecimal. Se registra junto con la firma. |  |

## reintegros_comision

Reintegros de comisiones pagadas por avance no realizadas o ejecutadas por menos días (RF-PAG-004).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `solicitud_id` → `travel_expenses.solicitudes_comision` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla reintegros_comision. Se genera automáticamente. | PK |
| 2 | `solicitud_id` | `uuid` | no | Referencia al registro de travel_expenses.solicitudes_comision (id). | FK→travel_expenses.solicitudes_comision.id |
| 3 | `origen` | `character varying(30)` | no | COMISION_NO_REALIZADA: la comisión pagada se canceló sin viajar. VIAJE_MENOR: se ejecutaron menos días de los pagados. |  |
| 4 | `estado` | `character varying(20)` | no | Estado del reintegro de la comisión: pendiente o registrado. |  |
| 5 | `valor_pagado` | `numeric(14,2)` | no | Valor pagado por la comisión, en pesos colombianos, copiado de solicitudes_comision.valor_pagado al generar el reintegro. |  |
| 6 | `valor_a_reintegrar` | `numeric(14,2)` | no | Valor calculado según los días efectivamente ejecutados. |  |
| 7 | `dias_comision` | `numeric(6,2)` | sí | _Por documentar_ |  |
| 8 | `dias_ejecutados` | `numeric(6,2)` | sí | _Por documentar_ |  |
| 9 | `valor_reintegrado` | `numeric(14,2)` | sí | Valor efectivamente reintegrado por el comisionado, en pesos colombianos. Debe ser igual a valor_a_reintegrar. |  |
| 10 | `fecha_reintegro` | `date` | sí | Fecha del reintegro de la comisión. |  |
| 11 | `soporte_path` | `character varying(255)` | sí | Ruta del soporte de la consignación del reintegro. |  |
| 12 | `observaciones` | `text` | sí | Observaciones sobre el reintegro de la comisión. |  |
| 13 | `registrado_por_id` | `uuid` | sí | Identificador (auth."user".id_user) del usuario autenticado que registró el reintegro. |  |
| 14 | `fecha_registro` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 15 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 16 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## rutas_restringidas

Catálogo de rutas entre ciudades cuya conexión aérea está restringida (RF-LIQ-003), como las rutas cortas que requieren autorización del Director Nacional o del Sindicato. Un registro por ruta de origen y destino, con la descripción de la restricción y su estado activo. Se consulta al validar los tiquetes de una solicitud de comisión.

- Clave primaria: `id`
- Filas: 4

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla rutas_restringidas. Se genera automáticamente. | PK |
| 2 | `origen_ciudad` | `character varying(100)` | no | Ciudad de origen de la ruta restringida. |  |
| 3 | `destino_ciudad` | `character varying(100)` | no | Ciudad de destino de la ruta restringida. |  |
| 4 | `descripcion_restriccion` | `character varying(255)` | sí | Texto que describe la restricción de la ruta aérea (por ejemplo, ruta corta que requiere autorización del Director Nacional o del Sindicato). Se muestra al validar el tiquete. |  |
| 5 | `activo` | `boolean` | no | Indica si la restricción de la ruta está activa. |  |
| 6 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |

## saldos_tiquetes

Cupo presupuestal de cada dependencia para la compra de tiquetes aéreos. Un registro por dependencia, con el presupuesto inicial, reservado y disponible, y el porcentaje de holgura que se suma al reservar para cubrir la variación del precio del tiquete entre la radicación y la emisión (RF-LIQ-004).

- Clave primaria: `id`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla saldos_tiquetes. Se genera automáticamente. | PK |
| 2 | `dependencia_id` | `character varying(100)` | no | Código (auth.dependencias.cod_dependencia) o identificador (auth.dependencias.id_dependencia) de la dependencia dueña del cupo de tiquetes, guardado como texto. Es único. | única |
| 3 | `nombre_dependencia` | `character varying(150)` | no | Nombre de la dependencia. |  |
| 4 | `presupuesto_inicial` | `numeric(12,2)` | no | _Por documentar_ |  |
| 5 | `presupuesto_reservado` | `numeric(12,2)` | no | Presupuesto reservado para tiquetes de solicitudes en trámite, en pesos colombianos: se suma al reservar el valor estimado del tiquete más la holgura y se resta al liberar la reserva cuando la solicitud se rechaza, anula o cancela. No puede ser negativo. |  |
| 6 | `presupuesto_disponible` | `numeric(12,2)` | no | Presupuesto disponible para tiquetes, en pesos colombianos. Lo actualiza la aplicación: inicial al crear, menos cada reserva, más cada liberación y más la diferencia si cambia el presupuesto inicial. |  |
| 7 | `holgura_porcentaje` | `numeric(5,2)` | no | Porcentaje que se suma al valor estimado del tiquete al reservar presupuesto, para cubrir la variación del precio entre la radicación y la emisión del pasaje. Por defecto, el parámetro HOLGURA_TIQUETES_PORCENTAJE (15). |  |
| 8 | `activo` | `boolean` | no | Indica si el saldo de tiquetes de la dependencia está activo. |  |
| 9 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 10 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## solicitudes_comision

Solicitudes de comisión de servicio de los comisionados de la ESAP. Un registro por solicitud, con destino, fechas, objeto, itinerario, liquidación de viáticos y gastos de viaje, y los datos de cada etapa del trámite: revisión, autorización, registro presupuestal, obligación, pago o cancelación. Su ciclo se registra en estado_solicitud (BORRADOR, RADICADA, EN_VERIFICACION, DEVUELTA, PAGADA, entre otros); se relaciona con comisionados, auth.user, documentos_soporte, legalizaciones_comision, reintegros_comision y solicitudes_historial_estados.

- Clave primaria: `id`
- Filas: 3
- Referencia a: `autorizador_id` → `auth.user` (0..1 → 0..1); `cancelado_por_usuario_id` → `auth.user` (0..1 → 0..1); `revisor_control_id` → `auth.user` (0..1 → 0..1); `enviado_presupuesto_por_id` → `auth.user` (0..1 → 0..1); `expedido_rp_por_id` → `auth.user` (0..1 → 0..1); `obligado_por_id` → `auth.user` (0..1 → 0..1); `pagado_por_id` → `auth.user` (0..1 → 0..1); `comisionado_id` → `travel_expenses.comisionados` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla solicitudes_comision. Se genera automáticamente. | PK |
| 2 | `consecutivo_unico` | `character varying(50)` | no | Consecutivo único de la solicitud de comisión. | única |
| 3 | `comisionado_id` | `uuid` | no | Referencia al registro de travel_expenses.comisionados (id). | FK→travel_expenses.comisionados.id |
| 4 | `destino_ciudad` | `text` | no | Ciudad de destino de la comisión. |  |
| 5 | `destino_departamento` | `text` | no | Departamento de destino de la comisión. |  |
| 6 | `fecha_inicio` | `timestamp without time zone` | no | Fecha y hora de inicio de la comisión. |  |
| 7 | `fecha_fin` | `timestamp without time zone` | no | Fecha y hora de finalización de la comisión. |  |
| 8 | `objeto_comision` | `text` | no | Objeto o propósito de la comisión de servicio. |  |
| 9 | `prioridad` | `character varying(10)` | no | Prioridad de la solicitud. Valores permitidos: ALTA, BAJA, MEDIA. |  |
| 10 | `rubro_presupuestal` | `text` | no | Rubro presupuestal con cargo al cual se financia la comisión. |  |
| 11 | `requiere_tiquetes` | `boolean` | no | Indica si la comisión requiere tiquetes. |  |
| 12 | `estado_solicitud` | `character varying(50)` | no | Estado de la solicitud en el flujo de trámite. Valores: BORRADOR, PENDIENTE, PENDIENTE_FIRMAS, RADICADA, EXTEMPORANEA, DEVUELTA, SOLICITADO, EN_VERIFICACION, VERIFICADA, APROBADO_JEFE, APROBADO_TALENTO_HUMANO, RESOLUCION_EMITIDA, TIQUETES_COMPRADOS, EN_COMISION, PENDIENTE_LEGALIZACION, LEGALIZADO, RECHAZADO, SOLICITADA_SIIF, AUTORIZACION_DIRECCION, EN_AUTORIZACION, AUTORIZADA, EN_REVOCATORIA, REVOCADA, CANCELADA, EN_PRESUPUESTO, COMPROMETIDA, OBLIGADA, PAGADA. Al crearse queda en RADICADA, o en PENDIENTE si se guarda como borrador. |  |
| 13 | `radicado_fuera_jornada` | `boolean` | no | Indica si la solicitud de comisión se radicó fuera de la jornada laboral. |  |
| 14 | `creado_por_usuario_id` | `uuid` | no | Identificador (auth."user".id_user) del usuario autenticado que creó la solicitud. |  |
| 15 | `creado_en` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 16 | `actualizado_en` | `timestamp without time zone` | sí | Fecha y hora de la última actualización del registro. |  |
| 17 | `monto_viaticos` | `numeric(12,2)` | no | Valor total de los viáticos de la comisión, en pesos colombianos; corresponde a total_pernoctados más total_no_pernoctados. |  |
| 18 | `monto_gastos_viaje` | `numeric(12,2)` | no | Valor de los gastos de desplazamiento de la comisión, en pesos colombianos: transporte a terminales aéreos más transporte terrestre o fluvial. No incluye el costo de los tiquetes aéreos, que va en costo_estimado_tiquete. |  |
| 19 | `dias_comision` | `numeric(5,2)` | no | Número de días de la comisión con soporte decimal (ej: 0.5, 1.5, 2.0). |  |
| 20 | `extemporanea` | `boolean` | no | Indica si la solicitud de comisión es extemporánea. |  |
| 21 | `tipo_comision` | `character varying(50)` | sí | Tipo de comisión: TERRESTRE, AEREO, MIXTO, INTERNACIONAL o ACTO_ADMINISTRATIVO. Valor por defecto: TERRESTRE; si la comisión es internacional se guarda INTERNACIONAL. |  |
| 22 | `es_internacional` | `boolean` | no | Indica si la comisión es internacional. |  |
| 23 | `motivo_devolucion` | `text` | sí | Motivo de la devolución del expediente por parte del secretario o analista (RF-REC-001). |  |
| 24 | `fecha_revision` | `timestamp without time zone` | sí | Marca temporal de la primera revisión del expediente por parte del secretario/a (RF-REC-001). |  |
| 25 | `salario_basico` | `numeric(12,2)` | no | Salario básico mensual del comisionado (mayor salario en caso de doble rol). Se usa para cálculos de liquidación y consulta en detalle. |  |
| 26 | `costo_estimado_tiquete` | `numeric(12,2)` | no | Costo estimado del tiquete aéreo ingresado por el usuario en la solicitud. |  |
| 27 | `analista_asignado_id` | `uuid` | sí | ID del usuario analista asignado para resolver la comision (auth.user.id_user) |  |
| 28 | `siif_exportado` | `boolean` | no | Indica si la solicitud ya fue exportada a SIIF Nacion. |  |
| 29 | `fecha_exportacion_siif` | `timestamp without time zone` | sí | Marca temporal en que se exporto la solicitud a SIIF. |  |
| 30 | `usuario_exportador_id` | `uuid` | sí | ID del usuario que exporto la solicitud a SIIF. |  |
| 31 | `consulta_rut_facturador` | `boolean` | no | Indica si el analista consulto el RUT del comisionado durante la verificacion. |  |
| 32 | `id_dependencia` | `bigint` | sí | Identificador de la dependencia (auth.dependencias.id_dependencia) de la comisión; si no se envía, se toma la del comisionado. Se usa para el saldo presupuestal de tiquetes. |  |
| 33 | `revisor_control_id` | `uuid` | sí | ID del usuario de Control Viaticos que ejecuta la segunda revision. | FK→auth.user.id_user |
| 34 | `fecha_segunda_revision` | `timestamp without time zone` | sí | Marca temporal de la aprobacion o devolucion en la segunda revision. |  |
| 35 | `observaciones_segunda_revision` | `text` | sí | Hallazgos u observaciones registrados cuando la solicitud se devuelve al analista. |  |
| 36 | `autorizador_id` | `uuid` | sí | ID del usuario de la Subdirección de Gestión Corporativa que autoriza la comisión. | FK→auth.user.id_user |
| 37 | `fecha_autorizacion` | `timestamp without time zone` | sí | Marca temporal en la que la Subdirección emite la autorización o devolución. |  |
| 38 | `observaciones_autorizacion` | `text` | sí | Observaciones, justificación o reparos de la Subdirección de Gestión Corporativa. |  |
| 39 | `autorizador_direccion_id` | `uuid` | sí | ID del usuario de Dirección Nacional o delegado que autorizó/negó la extemporaneidad (auth.user.id_user). |  |
| 40 | `fecha_autorizacion_direccion` | `timestamp with time zone` | sí | Marca temporal en que la Dirección Nacional emitió la decisión (Etapa 6 - RF-AUT-002). |  |
| 41 | `decision_direccion` | `character varying(20)` | sí | Resultado de la decisión de Dirección Nacional: AUTORIZADA o RECHAZADA. |  |
| 42 | `justificacion_direccion` | `text` | sí | Justificación motivada de la decisión emitida por Dirección Nacional. |  |
| 43 | `es_delegado_direccion` | `boolean` | sí | Indica si la autorización/negación fue emitida por un delegado formal de la Dirección Nacional. |  |
| 44 | `motivo_cancelacion` | `text` | sí | Motivo obligatorio detallado de la cancelación de la comisión (RF-AUT-003). |  |
| 45 | `fecha_cancelacion` | `timestamp with time zone` | sí | Marca temporal (UTC) en la que se confirmó la cancelación de la comisión. |  |
| 46 | `cancelado_por_usuario_id` | `uuid` | sí | ID del usuario del sistema que ejecutó y confirmó la cancelación (auth.user.id_user). | FK→auth.user.id_user |
| 47 | `responsable_cancelacion` | `character varying(255)` | sí | Nombre, cargo o dependencia solicitante/responsable de la orden de cancelación. |  |
| 48 | `pendiente_reintegro` | `boolean` | no | Indica si la comisión contaba con recursos comprometidos (SIIF/RP/Tiquetes) y requiere reintegro/liberación en Etapa 8. |  |
| 49 | `enviado_presupuesto` | `boolean` | no | Indica si la solicitud autorizada se envió al Grupo de Presupuesto para expedir el registro presupuestal (etapa 7, RF-PRE-001). Se marca al enviar el paquete; la solicitud sigue en AUTORIZADA. |  |
| 50 | `fecha_envio_presupuesto` | `timestamp with time zone` | sí | Fecha y hora en que la solicitud de comisión se envió a presupuesto. |  |
| 51 | `enviado_presupuesto_por_id` | `uuid` | sí | Referencia al registro de auth.user (id_user). | FK→auth.user.id_user |
| 52 | `observaciones_envio_presupuesto` | `text` | sí | Observaciones registradas al enviar la solicitud al área de presupuesto. |  |
| 53 | `numero_rp` | `character varying(50)` | sí | Número del registro presupuestal (RP) de la comisión. |  |
| 54 | `fecha_rp` | `date` | sí | Fecha del registro presupuestal (RP) de la comisión. |  |
| 55 | `valor_comprometido` | `numeric(14,2)` | sí | Valor comprometido en el registro presupuestal, en pesos colombianos. Mayor que cero. |  |
| 56 | `rubro_rp` | `character varying(100)` | sí | Rubro presupuestal del registro presupuestal. |  |
| 57 | `soporte_rp_path` | `character varying(255)` | sí | Ruta del archivo de soporte del registro presupuestal. |  |
| 58 | `fecha_expedicion_rp` | `timestamp with time zone` | sí | Fecha y hora de expedición del registro presupuestal (RP) de la comisión. |  |
| 59 | `expedido_rp_por_id` | `uuid` | sí | Referencia al registro de auth.user (id_user). | FK→auth.user.id_user |
| 60 | `codigo_rp` | `character varying(150)` | sí | Código oficial del RP con nomenclatura Fecha_RP_Número expedido en SIIF Nación. |  |
| 61 | `observaciones_rp` | `text` | sí | Observaciones del registro presupuestal. |  |
| 62 | `modalidad_pago` | `character varying(50)` | no | Modalidad de pago de la comisión: AVANCE o RECONOCIMIENTO_POSTERIOR (etapa 7, RF-PRE-003). Por defecto, AVANCE. |  |
| 63 | `dias_habiles_previos` | `integer` | no | Días hábiles entre la fecha del registro presupuestal y el inicio de la comisión (sin contar ninguna de las dos fechas, ni sábados, domingos o festivos). Se calcula al expedir el RP y define la modalidad de pago. |  |
| 64 | `fecha_calculo_modalidad` | `timestamp without time zone` | sí | Fecha y hora en que se calculó la modalidad de pago de la comisión. |  |
| 65 | `numero_obligacion` | `character varying(100)` | sí | Número de la obligación presupuestal de la comisión en SIIF Nación (etapa 8, RF-PAG-001). |  |
| 66 | `fecha_obligacion` | `date` | sí | Fecha de la obligación presupuestal de la comisión. |  |
| 67 | `valor_obligacion` | `numeric(12,2)` | sí | Valor de la obligación presupuestal registrada en SIIF Nación, en pesos colombianos. Mayor que cero. |  |
| 68 | `observaciones_obligacion` | `text` | sí | Observaciones de la obligación presupuestal. |  |
| 69 | `soporte_obligacion_path` | `character varying(255)` | sí | Ruta del archivo de soporte de la obligación presupuestal. |  |
| 70 | `obligado_por_id` | `uuid` | sí | Referencia al registro de auth.user (id_user). | FK→auth.user.id_user |
| 71 | `fecha_registro_obligacion` | `timestamp with time zone` | sí | Fecha y hora en que se registró la obligación presupuestal de la comisión. |  |
| 72 | `notificado_sst` | `boolean` | no | Indica si se envió la notificación automática a Seguridad y Salud en el Trabajo (SST) sobre la comisión (etapa 8, RF-PAG-002). Se envía al pasar la solicitud a COMPROMETIDA, OBLIGADA o PAGADA, si no se había notificado; incluye nombre y documento del comisionado, destino, fechas, objeto y estado. |  |
| 73 | `fecha_pago` | `date` | sí | Fecha efectiva de pago o desembolso de la comisión por Tesorería (etapa 8, RF-PAG-003). Se registra al pasar la solicitud a PAGADA. |  |
| 74 | `valor_pagado` | `numeric(12,2)` | sí | Valor total pagado o desembolsado al comisionado, en pesos colombianos. Mayor que cero. |  |
| 75 | `soporte_pago_path` | `character varying(255)` | sí | Ruta del archivo de soporte del pago. |  |
| 76 | `numero_orden_pago` | `character varying(100)` | sí | Número de la orden de pago de la comisión. |  |
| 77 | `observaciones_pago` | `text` | sí | Observaciones del pago. |  |
| 78 | `pagado_por_id` | `uuid` | sí | Referencia al registro de auth.user (id_user). | FK→auth.user.id_user |
| 79 | `fecha_registro_pago` | `timestamp with time zone` | sí | Fecha y hora en que se registró el pago de la comisión. |  |
| 80 | `campos_adicionales` | `jsonb` | no | Metadatos y campos dinámicos configurables gobernados por travel_expenses.config_campos_formulario (JSONB). |  |
| 81 | `itinerario` | `jsonb` | no | Arreglo de tramos/rutas de la comisión (RutaItinerario[]) con origen, destino, trayecto, fechas, días y horario militar estimado. |  |
| 82 | `dias_pernoctados` | `numeric(5,2)` | sí | _Por documentar_ |  |
| 83 | `tarifa_dia_pernoctado` | `numeric(14,2)` | sí | Tarifa diaria aplicada a las noches con pernocta, en pesos colombianos: tarifa diaria base por el factor del comisionado. |  |
| 84 | `total_pernoctados` | `numeric(14,2)` | sí | Valor total de las noches con pernocta, en pesos colombianos: días pernoctados por la tarifa del día pernoctado. |  |
| 85 | `dias_no_pernoctados` | `numeric(5,2)` | sí | Días de la comisión sin pernocta. |  |
| 86 | `tarifa_dia_no_pernoctado` | `numeric(14,2)` | sí | Tarifa del día sin pernocta, en pesos colombianos: 50 % de la tarifa del día pernoctado. |  |
| 87 | `total_no_pernoctados` | `numeric(14,2)` | sí | Valor total de los días sin pernocta, en pesos colombianos. La liquidación reconoce un día sin pernocta (el único día o el de regreso) a la tarifa del día no pernoctado. |  |
| 88 | `factor_comisionado` | `numeric(4,2)` | sí | Factor multiplicador de la tarifa según el tipo de comisionado: para CONTRATISTA, el parámetro FACTOR_CONTRATISTA de liquidation_params (por defecto 0,8); para los demás tipos, 1,0. |  |
| 89 | `factor_pernocta` | `numeric(4,2)` | sí | Factor de la tarifa según haya o no pernocta: 1,0 con pernocta; sin pernocta, el parámetro FACTOR_SIN_PERNOCTA de liquidation_params (por defecto 0,5). |  |
| 90 | `tarifa_diaria_base` | `numeric(14,2)` | sí | Tarifa diaria de viáticos antes de aplicar factores, en pesos colombianos. Se toma de tarifas_investigadores para INVESTIGADOR y de escalas_viaticos para los demás tipos (para ESTUDIANTE, con el SMMLV); no se toma de tarifas_regionales_excepcion. |  |
| 91 | `tarifa_final_aplicada_dia` | `numeric(14,2)` | sí | Tarifa diaria final aplicada, en pesos colombianos: con pernocta, la tarifa del día pernoctado (tarifa base por factor del comisionado); sin pernocta, la tarifa del día no pernoctado (50 %). |  |
| 92 | `salario_base_aplicado` | `numeric(14,2)` | sí | Valor base usado en la liquidación para ubicar la escala de viáticos: la mayor asignación básica del comisionado; para ESTUDIANTE, el SMMLV; para INVESTIGADOR, la tarifa diaria de la categoría. A diferencia de salario_basico, que guarda el salario del comisionado. |  |
| 93 | `decreto_aplicado` | `character varying(100)` | sí | Decreto de escala de viáticos aplicado en la liquidación. Valor por defecto: Decreto 314 de 2026. |  |
| 94 | `numero_cdp` | `text` | sí | Número del certificado de disponibilidad presupuestal (CDP). |  |
| 95 | `fecha_cdp` | `text` | sí | _Por documentar_ |  |
| 96 | `fecha_radicacion` | `timestamp without time zone` | sí | Marca temporal en la que la solicitud se radicó e ingresó por primera vez a la bandeja del Grupo de Viáticos. |  |
| 97 | `cargo` | `text` | sí | Cargo institucional asignado a la comisión GF-FO-023 para trazabilidad, liquidación y KPIs de analítica. |  |
| 98 | `id_cargo` | `bigint` | sí | Identificador referencial del cargo institucional (auth.cargos). |  |

## solicitudes_historial_estados

Auditoría append-only de transiciones de estado del expediente de comisión (RF-SIS-001 / RF-LIQ-004).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `solicitud_id` → `travel_expenses.solicitudes_comision` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla solicitudes_historial_estados. Se genera automáticamente. | PK |
| 2 | `solicitud_id` | `uuid` | no | Referencia al registro de travel_expenses.solicitudes_comision (id). | FK→travel_expenses.solicitudes_comision.id |
| 3 | `estado_anterior` | `character varying(50)` | sí | Estado del expediente de comisión antes de la transición (por ejemplo, RADICADA). Nulo cuando es la primera acción sobre el expediente. |  |
| 4 | `estado_nuevo` | `character varying(50)` | no | Estado posterior a la transición. Ej: SOLICITADO (la solicitud queda consolidada y en revisión del Grupo de Viáticos). |  |
| 5 | `usuario_id` | `uuid` | no | Identificador (auth."user".id_user) del usuario autenticado que ejecutó la transición de estado. Si no hay usuario se guarda el UUID 00000000-0000-0000-0000-000000000000. |  |
| 6 | `comentarios` | `character varying(255)` | sí | Justificación u observación de la transición de estado. Opcional, de hasta 255 caracteres. |  |
| 7 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |

## tarifas_investigadores

Tarifas diarias de viáticos por categoría de investigador (JUNIOR, ASOCIADO o SENIOR). Un registro por categoría, con la tarifa diaria base que se aplica a los comisionados de tipo INVESTIGADOR.

- Clave primaria: `id`
- Filas: 3

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla tarifas_investigadores. Se genera automáticamente. | PK |
| 2 | `categoria_investigador` | `character varying(50)` | no | Categoría del investigador a la que aplica la tarifa: JUNIOR, ASOCIADO o SENIOR. Es única. | única |
| 3 | `tarifa_diaria` | `numeric(12,2)` | no | Valor diario de viáticos para la categoría de investigador, en pesos colombianos; se usa como tarifa diaria base para comisionados INVESTIGADOR. |  |
| 4 | `creado_en` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |
| 5 | `activo` | `boolean` | no | Indica si la tarifa de investigadores está activa. |  |

## tarifas_referencia_tiquetes

Matriz de tarifas de referencia de tiquetes aéreos por ruta, para vuelos nacionales e internacionales. Un registro por ruta de origen y destino, con códigos IATA, tarifa estimada, mínima y máxima de un tiquete de ida, y la fuente de la tarifa (paramétrica, manual o API). Se actualiza por sincronización con API o por parametrización institucional.

- Clave primaria: `id`
- Filas: 42

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla tarifas_referencia_tiquetes. Se genera automáticamente. | PK |
| 2 | `origen_ciudad` | `character varying(100)` | no | Ciudad de origen de la ruta. |  |
| 3 | `destino_ciudad` | `character varying(100)` | no | Ciudad de destino de la ruta. |  |
| 4 | `origen_iata` | `character varying(10)` | no | Código IATA del aeropuerto de origen. |  |
| 5 | `destino_iata` | `character varying(10)` | no | Código IATA del aeropuerto de destino. |  |
| 6 | `tarifa_estimada` | `numeric(14,2)` | no | Tarifa estimada de un tiquete de ida para la ruta (origen-destino), en pesos colombianos. Para viajes de ida y regreso la aplicación la multiplica por dos. |  |
| 7 | `tarifa_minima` | `numeric(14,2)` | sí | Tarifa mínima de referencia de un tiquete de ida para la ruta, en pesos colombianos. |  |
| 8 | `tarifa_maxima` | `numeric(14,2)` | sí | Tarifa máxima de referencia de un tiquete de ida para la ruta, en pesos colombianos. |  |
| 9 | `fuente` | `character varying(50)` | no | Fuente de la tarifa de referencia: PARAMETRICO_ESAP (por defecto), MANUAL, API_AMADEUS o ESTIMADOR_REFERENCIA_ESAP. |  |
| 10 | `notas` | `character varying(255)` | sí | Notas sobre la tarifa de referencia. |  |
| 11 | `ultima_actualizacion` | `timestamp without time zone` | no | Fecha y hora de la última actualización de los valores de la tarifa. La aplicación la fija al crear, editar o sincronizar la tarifa; actualizado_en cambia con cualquier modificación del registro. |  |
| 12 | `activo` | `boolean` | no | Indica si la tarifa de referencia de tiquetes está activa. |  |
| 13 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 14 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## tarifas_regionales_excepcion

Tarifas de viáticos de excepción por departamento, según el artículo 5 del Decreto 314 de 2026 para departamentos nuevos. Un registro por departamento, con la tarifa diaria, el decreto de referencia y su estado activo.

- Clave primaria: `id`
- Filas: 8

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla tarifas_regionales_excepcion. Se genera automáticamente. | PK |
| 2 | `departamento` | `character varying(100)` | no | Departamento al que aplica la tarifa de excepción. Es único. | única |
| 3 | `es_nuevo_departamento` | `boolean` | no | Indica si la tarifa regional de excepción corresponde a un nuevo departamento. |  |
| 4 | `tarifa_diaria` | `numeric(12,2)` | no | _Por documentar_ |  |
| 5 | `decreto_referencia` | `character varying(100)` | sí | Decreto que establece la tarifa de excepción. |  |
| 6 | `activo` | `boolean` | no | Indica si la tarifa regional de excepción está activa. |  |
| 7 | `creado_en` | `timestamp without time zone` | sí | Fecha y hora de creación del registro. |  |

## tarifas_transporte_terminal

Valores máximos reconocidos por trayecto para el desplazamiento a terminales aéreos. Un registro por departamento y ciudad del aeropuerto, con el valor máximo por trayecto que se usa en la liquidación de los gastos de viaje de la comisión.

- Clave primaria: `id`
- Filas: 11

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla tarifas_transporte_terminal. Se genera automáticamente. | PK |
| 2 | `departamento` | `character varying(100)` | no | Nombre del departamento al que aplica la tarifa de transporte. |  |
| 3 | `departamento_id` | `integer` | sí | _Por documentar_ |  |
| 4 | `ciudad` | `character varying(100)` | sí | Ciudad a la que aplica la tarifa de transporte. |  |
| 5 | `ciudad_aeropuerto` | `character varying(150)` | no | Nombre del departamento con el municipio del aeropuerto entre paréntesis, por ejemplo ANTIOQUIA (Rionegro). |  |
| 6 | `valor_maximo` | `numeric(12,2)` | no | Valor máximo reconocido por trayecto de transporte a la terminal aérea, en pesos colombianos. Para tramos de ida y regreso la liquidación lo multiplica por dos. |  |
| 7 | `activo` | `boolean` | no | Indica si la tarifa de transporte a terminal está activa. |  |
| 8 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |

## tipos_documento_soporte

Catálogo de tipos de documento de soporte del trámite de comisiones. Un registro por tipo, con su código, nombre, descripción, instrucciones de validación para quien revisa y campos del formulario que se cotejan con el documento. Se usa en la configuración de documentos por tipo de comisionado, en la de legalización y en los soportes de legalización.

- Clave primaria: `id`
- Filas: 15

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla tipos_documento_soporte. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(50)` | no | Código único del tipo de documento de soporte. | única |
| 3 | `nombre` | `character varying(100)` | no | Nombre del tipo de documento de soporte. |  |
| 4 | `descripcion` | `character varying(255)` | sí | Descripción del tipo de documento de soporte. |  |
| 5 | `activo` | `boolean` | no | Indica si el tipo de documento de soporte está activo. |  |
| 6 | `creado_en` | `timestamp without time zone` | no | Fecha y hora de creación del registro. |  |
| 7 | `actualizado_en` | `timestamp without time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 8 | `instrucciones_validacion` | `text` | sí | Instrucciones de validación del documento de soporte, dirigidas a quien revisa (por ejemplo, vigencia y coincidencia del titular). El servicio solo las guarda y las devuelve; no las aplica un proceso automático. |  |
| 9 | `campos_a_validar` | `jsonb` | sí | Lista JSON de claves de los campos del formulario que se deben cotejar con el documento (por ejemplo, nombreComisionado, numeroDocumento, numeroCuenta). |  |
