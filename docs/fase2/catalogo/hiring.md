# Contratación (`hiring`)

_Descripción del dominio por documentar._

84 tablas · 1 vistas · 952 columnas · 1.961 filas · 1 funciones o procedimientos

| Tabla | Tipo | Filas | Descripción |
|---|---|--:|---|
| [`actas_inicio`](#actas_inicio) | Tabla | 1 | Reunión de inicio y su acta, cuando el contrato la pactó (EFDS-1167, actividad 9.1). |
| [`actas_liquidacion`](#actas_liquidacion) | Tabla | 0 | Acta de liquidación bilateral o unilateral, con balance financiero y paz y salvo (EFDS-1172). |
| [`actividades`](#actividades) | Tabla | 63 | Catálogo de actividades de la matriz de flujo, por etapa y numeral. |
| [`actividades_con_soporte`](#actividades_con_soporte) | Tabla | 14 | Las actividades de la matriz que se cumplen registrando lo que pasó afuera, y si exigen soporte. |
| [`actividades_excluidas`](#actividades_excluidas) | Tabla | 161 | Celdas marcadas NO en la matriz de flujo: la actividad no aplica a esa modalidad. |
| [`actividades_salvedad`](#actividades_salvedad) | Tabla | 0 | Celdas de la matriz donde la actividad aplica pero con una condición o una variante propia de la modalidad. |
| [`actos_adjudicacion`](#actos_adjudicacion) | Tabla | 1 | Acto administrativo de adjudicación del Ordenador del Gasto, con su notificación y publicación (EFDS-1159). |
| [`adendas`](#adendas) | Tabla | 3 | Adendas de fondo y de cronograma del proceso, con su emisión y su publicación (EFDS-1154). |
| [`afiliaciones_arl`](#afiliaciones_arl) | Tabla | 0 | Afiliación a riesgos laborales, exigida a los contratistas persona natural (EFDS-1164). |
| [`alcances_permiso`](#alcances_permiso) | Tabla | 313 | _Por documentar_ |
| [`amparos`](#amparos) | Tabla | 1 | Coberturas de cada garantía con su vigencia, para controlar vencimientos (EFDS-1164). |
| [`aperturas_proceso`](#aperturas_proceso) | Tabla | 3 | Resolución de apertura y pliego definitivo de cada proceso (EFDS-1152). |
| [`audiencia_riesgos_config`](#audiencia_riesgos_config) | Tabla | 1 | En qué modalidades la audiencia de riesgos es obligatoria (EFDS-1153, RF-PUB-04). |
| [`audiencias_adjudicacion`](#audiencias_adjudicacion) | Tabla | 1 | Audiencia de adjudicación del proceso, con su acta y lo que en ella se resolvió (EFDS-1159). |
| [`audiencias_riesgos`](#audiencias_riesgos) | Tabla | 3 | Audiencias de asignación de riesgos celebradas, con su acta y su matriz consolidada. |
| [`audiencias_sancionatorias`](#audiencias_sancionatorias) | Tabla | 0 | Audiencias del trámite sancionatorio (EFDS-1181, RF-INC-02). La citación mira al futuro; el acta, al hecho ya ocurrido. |
| [`avisos`](#avisos) | Tabla | 0 | Lo que cambió la Dirección sobre los avisos de cada actividad. Sin fila, la actividad avisa con lo sugerido. |
| [`avisos_habilitacion`](#avisos_habilitacion) | Tabla | 156 | Actividades de cada proceso de las que ya salió el aviso de «te toca». Evita repetirlo. |
| [`campos_formulario`](#campos_formulario) | Tabla | 13 | _Por documentar_ |
| [`casos_incumplimiento`](#casos_incumplimiento) | Tabla | 0 | Reportes de presunto incumplimiento del contrato (EFDS-1180, RF-INC-01). |
| [`causales_contratacion`](#causales_contratacion) | Tabla | 14 | Actividad 3.6 (3.5.1 de la matriz): causales que habilitan contratar por una modalidad. La matriz la describe como «filtro según la modalidad» y solo la marca aplicable en selección abreviada de menor cuantía y en contratación directa. |
| [`cdp`](#cdp) | Tabla | 4 | Certificado de Disponibilidad Presupuestal del proceso. Requisito previo a la apertura (EFDS-1148). |
| [`cierres_contrato`](#cierres_contrato) | Tabla | 0 | Cierre definitivo del contrato tras vencer los amparos de estabilidad y calidad (EFDS-1175). |
| [`cierres_financieros`](#cierres_financieros) | Tabla | 0 | Pago final y liberación del saldo no comprometido del RP (EFDS-1173). |
| [`comites_evaluadores`](#comites_evaluadores) | Tabla | 3 | Comités evaluadores designados por memorando, vigentes y revocados (EFDS-1156). |
| [`contratos`](#contratos) | Tabla | 1 | Contratos generados a partir del formato de su tipología, con la aceptación del proponente (EFDS-1161). |
| [`declaratorias_desiertas`](#declaratorias_desiertas) | Tabla | 0 | Declaratoria desierta del proceso: causal, motivación, acto firmado, notificación y publicación (EFDS-1160, RF-ADJ-02). |
| [`dias_no_habiles`](#dias_no_habiles) | Tabla | 0 | Días no laborables propios de la ESAP, adicionales a los festivos nacionales que el servicio calcula (EFDS-1150). |
| [`documentos`](#documentos) | Tabla | 130 | _Por documentar_ |
| [`documentos_proceso`](#documentos_proceso) | Tabla | 40 | _Por documentar_ |
| [`documentos_requeridos`](#documentos_requeridos) | Tabla | 23 | Catálogo de documentos que exige cada actividad, filtrado por modalidad (EFDS-1149). |
| [`entregables_informe`](#entregables_informe) | Tabla | 0 | Consolidado de entregables del informe final (EFDS-1171). |
| [`evidencias_evaluacion`](#evidencias_evaluacion) | Tabla | 0 | Documentos con que el comité sustenta su evaluación: verificaciones, cuadro comparativo, actas (EFDS-1157). |
| [`expedientes`](#expedientes) | Tabla | 10 | _Por documentar_ |
| [`firmas_contrato`](#firmas_contrato) | Tabla | 2 | Firmas del ordenador del gasto y del contratista, con su evidencia (EFDS-1162). |
| [`garantias`](#garantias) | Tabla | 1 | Pólizas constituidas por el contratista, con su revisión y aprobación (EFDS-1164). |
| [`informes_definitivos`](#informes_definitivos) | Tabla | 1 | Informe de evaluación definitivo, con el resultado congelado y lo que cambió desde el preliminar (EFDS-1159). |
| [`informes_evaluacion`](#informes_evaluacion) | Tabla | 2 | Informe de evaluación del proceso, con el resultado del comité congelado al momento de trasladarlo (EFDS-1158). |
| [`informes_finales`](#informes_finales) | Tabla | 0 | Informe final del supervisor con el balance congelado de la ejecución (EFDS-1171). |
| [`limitaciones_mipyme`](#limitaciones_mipyme) | Tabla | 2 | Decisión de limitar o no la convocatoria a MIPYME, con las condiciones que se evaluaron (EFDS-1151). |
| [`manifestaciones_mipyme`](#manifestaciones_mipyme) | Tabla | 0 | Manifestaciones de interés de MIPYME en participar; su número decide la limitación (EFDS-1151). |
| [`miembros_comite`](#miembros_comite) | Tabla | 3 | Integrantes del comité evaluador con su dimensión de evaluación (EFDS-1156). |
| [`modalidades`](#modalidades) | Tabla | 11 | _Por documentar_ |
| [`modificaciones_contrato`](#modificaciones_contrato) | Tabla | 0 | Modificaciones contractuales de la actividad 9.5; hoy solo la adición tiene trámite (EFDS-1176). |
| [`observaciones_pliego`](#observaciones_pliego) | Tabla | 4 | Observaciones de interesados al proyecto de pliego publicado, con su respuesta (EFDS-1151). |
| [`oferentes`](#oferentes) | Tabla | 4 | Ofertas recibidas dentro del plazo, con su soporte. Al cerrar la recepción componen la lista publicada (EFDS-1155). |
| [`pagos_contrato`](#pagos_contrato) | Tabla | 2 | Cuentas de cobro del contrato, su aval y su trámite (EFDS-1170). |
| [`parametros_alerta`](#parametros_alerta) | Tabla | 6 | Plazos que gobiernan las alertas de contratación: anticipación por vencimiento, tolerancia sin abogado y hora del aviso diario. |
| [`parametros_mipyme`](#parametros_mipyme) | Tabla | 2 | Condiciones que habilitan la limitación a MIPYME. Parametrizables (EFDS-1393). |
| [`participaciones_proceso`](#participaciones_proceso) | Tabla | 17 | Quién está en cada proceso y con qué papel, vigentes y relevados, con el motivo del cambio (EFDS-1183). |
| [`piezas_audiencia`](#piezas_audiencia) | Tabla | 0 | Acta, grabaciones, observaciones y anexos que documentan la audiencia de adjudicación (EFDS-1159). |
| [`plantillas`](#plantillas) | Tabla | 10 | _Por documentar_ |
| [`plazo_publicacion_acta`](#plazo_publicacion_acta) | Tabla | 1 | Plazo para publicar el acta de liquidación, parametrizable y marcado si está sin confirmar (EFDS-1174). |
| [`plazo_publicacion_contrato`](#plazo_publicacion_contrato) | Tabla | 1 | Plazo para publicar el contrato, parametrizable y marcado si está sin confirmar (EFDS-1166). |
| [`plazos_ofertas`](#plazos_ofertas) | Tabla | 7 | Días hábiles de recepción de ofertas por modalidad, contados desde la apertura (EFDS-1155). |
| [`plazos_publicacion`](#plazos_publicacion) | Tabla | 7 | Días hábiles de publicidad del proyecto de pliego, por modalidad. Parametrizables (EFDS-1150). |
| [`plazos_traslado`](#plazos_traslado) | Tabla | 7 | Días hábiles de traslado del informe de evaluación por modalidad, contados desde su publicación (EFDS-1158). |
| [`proceso_actividades`](#proceso_actividades) | Tabla | 590 | _Por documentar_ |
| [`procesos`](#procesos) | Tabla | 10 | _Por documentar_ |
| [`publicaciones_acta`](#publicaciones_acta) | Tabla | 0 | Publicaciones del acta de liquidación con su destino, evidencia y control de plazo (EFDS-1174). |
| [`publicaciones_contrato`](#publicaciones_contrato) | Tabla | 1 | Publicaciones del contrato con su destino, evidencia y control de plazo (EFDS-1166). |
| [`publicaciones_modificacion`](#publicaciones_modificacion) | Tabla | 0 | Publicación de la modificación en SECOP II, con su evidencia (EFDS-1176, RF-MOD-05). |
| [`publicaciones_pliego`](#publicaciones_pliego) | Tabla | 3 | Registro de la publicación del proyecto de pliego en SECOP II y su plazo de publicidad (EFDS-1150). |
| [`recepciones_ofertas`](#recepciones_ofertas) | Tabla | 3 | Plazo de recepción de ofertas de cada proceso y su cierre (EFDS-1155). |
| [`registros_actividad`](#registros_actividad) | Tabla | 2 | Constancia de que una actividad sin historia propia ocurrió, con su fecha, su nota y su soporte. |
| [`registros_presupuestales`](#registros_presupuestales) | Tabla | 1 | Registros presupuestales que comprometen los recursos del contrato (EFDS-1163). |
| [`reglas_actividad`](#reglas_actividad) | Tabla | 13 | _Por documentar_ |
| [`resoluciones_sancionatorias`](#resoluciones_sancionatorias) | Tabla | 0 | Actos administrativos del trámite sancionatorio (EFDS-1181, RF-INC-02): el que lo abre y el que lo decide, incluida la caducidad. |
| [`resultados_evaluacion`](#resultados_evaluacion) | Tabla | 2 | Resultado de la evaluación hecha por el comité fuera de la plataforma: oferta ganadora, su valoración y el informe que la sustenta (EFDS-1157). |
| [`revisiones`](#revisiones) | Tabla | 12 | _Por documentar_ |
| [`roles_del_modulo`](#roles_del_modulo) | Vista |  | Roles que trabajan en contratación: los que tienen al menos un permiso del módulo. Alimenta el selector de aprobadores. |
| [`seguimientos_contrato`](#seguimientos_contrato) | Tabla | 1 | Informes, actas y soportes de la ejecución del contrato (EFDS-1168, actividad 9.2). |
| [`sesiones_comite_contratacion`](#sesiones_comite_contratacion) | Tabla | 4 | Sesiones del comité de contratación sobre un proceso (actividad 3.7). Una por sesión: observar devuelve el proceso al comité, y las dos quedan. |
| [`smmlv`](#smmlv) | Tabla | 2 | Salario mínimo mensual legal vigente por año. Base de los umbrales expresados en SMMLV (EFDS-1147). |
| [`sobres_economicos`](#sobres_economicos) | Tabla | 1 | Apertura del sobre económico en la audiencia de adjudicación, donde la modalidad lo exige (EFDS-1159). |
| [`soportes_pago`](#soportes_pago) | Tabla | 4 | Documentos que acompañan la cuenta de cobro. Se cargan a mano mientras no exista la integración con Click (EFDS-1170). |
| [`subsanaciones`](#subsanaciones) | Tabla | 1 | Subsanaciones y observaciones que presentan los oferentes durante el traslado del informe (EFDS-1158). |
| [`supervisiones_contrato`](#supervisiones_contrato) | Tabla | 1 | Supervisores designados por acto administrativo, vigentes y relevados (EFDS-1165). |
| [`suscripciones_acta_inicio`](#suscripciones_acta_inicio) | Tabla | 1 | Acta de inicio suscrita por la entidad y el contratista (actividad 8.7). La reunión (9.1) va en actas_inicio. |
| [`tipologias_contrato`](#tipologias_contrato) | Tabla | 12 | Tipologías de contrato y el formato del SIG que sirve de minuta (EFDS-1161). |
| [`tipos_amparo`](#tipos_amparo) | Tabla | 7 | Coberturas que puede incluir una garantía, para controlar sus vencimientos (EFDS-1164). |
| [`tope_adicion`](#tope_adicion) | Tabla | 1 | Tope legal de la adición como porcentaje del valor inicial del contrato (EFDS-1176). |
| [`trazabilidad`](#trazabilidad) | Tabla | 236 | _Por documentar_ |
| [`umbrales_comite_contratacion`](#umbrales_comite_contratacion) | Tabla | 1 | Condición de cuantía para pasar por el comité de contratación (actividad 3.7). La modalidad sin fila va a comité siempre que la matriz la marque. |
| [`umbrales_modalidad`](#umbrales_modalidad) | Tabla | 3 | Rangos de cuantía que sugieren cada modalidad. Parametrizables por administrador (EFDS-1147). |

## actas_inicio

Reunión de inicio y su acta, cuando el contrato la pactó (EFDS-1167, actividad 9.1).

- Clave primaria: `id`
- Filas: 1
- Referencia a: `acta_documento_id` → `hiring.documentos` (0..1 → 0..1); `contrato_id` → `hiring.contratos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla actas_inicio. Se genera automáticamente. | PK |
| 2 | `contrato_id` | `uuid` | no | Referencia al registro de hiring.contratos (id). | FK→hiring.contratos.id |
| 3 | `fecha_inicio` | `date` | no | Fecha real de la reunión de inicio, no la del registro; marca el inicio de la ejecución del contrato y desde ella corre su plazo. Formato YYYY-MM-DD (EFDS-1167). |  |
| 4 | `temas_tratados` | `text` | no | Temas socializados en la reunión de inicio del contrato: alcance, cronograma y entregables. Entre 10 y 4.000 caracteres. |  |
| 5 | `asistentes` | `text` | sí | Personas que asistieron a la reunión de inicio, en texto libre: por la entidad, el supervisor, el ordenador o su delegado, y por el contratista, su representante. Hasta 2.000 caracteres. |  |
| 6 | `acta_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 7 | `acta_pactada` | `boolean` | no | Indica si el contrato pactó acta de inicio. Se fija al registrar, porque de él depende que el acta fuera exigible en ese momento. |  |
| 8 | `registrado_por` | `character varying(200)` | sí | Usuario que realizó el registro. |  |
| 9 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## actas_liquidacion

Acta de liquidación bilateral o unilateral, con balance financiero y paz y salvo (EFDS-1172).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `acta_documento_id` → `hiring.documentos` (0..1 → 1); `contrato_id` → `hiring.contratos` (0..1 → 1); `paz_y_salvo_documento_id` → `hiring.documentos` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla actas_liquidacion. Se genera automáticamente. | PK |
| 2 | `contrato_id` | `uuid` | no | Referencia al registro de hiring.contratos (id). | FK→hiring.contratos.id |
| 3 | `tipo` | `character varying(20)` | no | Tipo de liquidación del contrato: BILATERAL (de común acuerdo entre las partes) o UNILATERAL (por acto de la entidad); cada una tiene requisitos y plazos distintos (RF-LIQ-02). |  |
| 4 | `acta_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 5 | `fecha_acta` | `date` | no | Fecha del acta de liquidación. |  |
| 6 | `balance` | `jsonb` | no | Balance financiero del contrato congelado al liquidar, en formato JSON con valorContrato, valorPagado (suma de los pagos en estado TRAMITADO), saldo (valor del contrato menos lo pagado; negativo si se pagó de más), cuentasTramitadas y cuentasPendientes. Lo calcula el sistema. |  |
| 7 | `paz_y_salvo` | `boolean` | no | Indica si las partes se declaran a paz y salvo. El soporte se registra aparte del acta. |  |
| 8 | `paz_y_salvo_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 9 | `observaciones` | `text` | sí | Observaciones sobre el acta de liquidación. |  |
| 10 | `fecha_terminacion` | `date` | sí | Fecha de terminación del contrato con la que se calculó la ventana de liquidación, guardada tal como estaba vigente el día en que se liquidó. La calcula el sistema como la fecha de inicio del acta de inicio más contratos.plazo_dias; no se diligencia en el acta. |  |
| 11 | `bilateral_hasta` | `date` | sí | Fecha límite para liquidar el contrato de mutuo acuerdo (bilateral). |  |
| 12 | `unilateral_hasta` | `date` | sí | Fecha límite para liquidar el contrato de forma unilateral. |  |
| 13 | `momento_del_plazo` | `character varying(20)` | sí | Momento del plazo de liquidación en que se firmó el acta: BILATERAL, UNILATERAL o VENCIDO. Se guarda resuelto al registrar, no se deriva después. |  |
| 14 | `estado` | `character varying(20)` | no | Estado del acta de liquidación: vigente o anulado. |  |
| 15 | `liquidado_por` | `character varying(200)` | sí | Usuario que realizó la liquidación. |  |
| 16 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 17 | `anulado_at` | `timestamp with time zone` | sí | Fecha y hora de la anulación. |  |
| 18 | `anulado_por` | `character varying(200)` | sí | Usuario que realizó la anulación. |  |
| 19 | `motivo_anulacion` | `text` | sí | Motivo de la anulación. |  |

## actividades

Catálogo de actividades de la matriz de flujo, por etapa y numeral.

- Clave primaria: `numeral`
- Filas: 63

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `numeral` | `character varying(20)` | no | Clave primaria de la tabla actividades: numeral. | PK |
| 2 | `etapa` | `integer` | no | _Por documentar_ |  |
| 3 | `nombre` | `character varying(200)` | no | Nombre de la actividad de la matriz de flujo. |  |
| 4 | `descripcion` | `text` | sí | Descripción de la actividad de la matriz de flujo. |  |
| 5 | `orden` | `integer` | no | Posición de la actividad en el orden de presentación dentro de su etapa. |  |
| 6 | `activa` | `boolean` | no | Indica si la actividad de la matriz de flujo está activa; es falso cuando la actividad no aplica a alguna modalidad. El detalle por modalidad está en actividades_modalidad. |  |
| 7 | `plazo_dias` | `integer` | sí | Días hábiles previstos para completar la actividad. Nulo = sin plazo definido. |  |
| 8 | `responsable_cargo` | `character varying(200)` | sí | Cargo que responde por la actividad, no la persona: quien lo ocupa cambia sin que cambie el proceso. |  |
| 9 | `alerta_dias_antes` | `integer` | sí | Cuántos días antes del vencimiento avisar. Nulo = sin aviso. |  |
| 10 | `avisos_por_correo` | `boolean` | no | Si los avisos de la actividad llegan también al correo institucional de quien los recibe. |  |

## actividades_con_soporte

Las actividades de la matriz que se cumplen registrando lo que pasó afuera, y si exigen soporte.

- Clave primaria: `numeral`
- Filas: 14

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `numeral` | `character varying(20)` | no | Clave primaria de la tabla actividades_con_soporte: numeral. | PK |
| 2 | `etapa` | `integer` | no | _Por documentar_ |  |
| 3 | `exige_soporte` | `boolean` | no | Indica si la actividad exige soporte documental. |  |
| 4 | `confirmado` | `boolean` | no | false mientras la exigencia de soporte sea suposición del equipo y no cita de la matriz. |  |
| 5 | `nota_fuente` | `text` | sí | Texto de la matriz de flujo sobre la actividad (lo que dice la matriz que se hace o se adjunta), del que sale la exigencia de soporte; se muestra en la pantalla del registro. |  |

## actividades_excluidas

Celdas marcadas NO en la matriz de flujo: la actividad no aplica a esa modalidad.

- Clave primaria: `numeral`, `modalidad`
- Filas: 161
- Referencia a: `modalidad` → `hiring.modalidades` (1..* → 1); `numeral` → `hiring.actividades` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `numeral` | `character varying(20)` | no | Clave primaria de la tabla actividades_excluidas: numeral. | PK FK→hiring.actividades.numeral |
| 2 | `modalidad` | `character varying(60)` | no | Clave primaria de la tabla actividades_excluidas: modalidad. | PK FK→hiring.modalidades.codigo |
| 3 | `motivo` | `text` | sí | Motivo por el que la actividad no aplica a la modalidad. |  |

## actividades_salvedad

Celdas de la matriz donde la actividad aplica pero con una condición o una variante propia de la modalidad.

- Clave primaria: `numeral`, `modalidad`
- Filas: 0
- Referencia a: `modalidad` → `hiring.modalidades` (0..1 → 1); `numeral` → `hiring.actividades` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `numeral` | `character varying(20)` | no | Clave primaria de la tabla actividades_salvedad: numeral. | PK FK→hiring.actividades.numeral |
| 2 | `modalidad` | `character varying(60)` | no | Clave primaria de la tabla actividades_salvedad: modalidad. | PK FK→hiring.modalidades.codigo |
| 3 | `variante` | `text` | sí | Texto de la celda de la matriz tal como lo escribió Contratación cuando no dice SI (por ejemplo, TVEC o Comunicación de aceptación). Vacío cuando la celda es «si*», que marca una condición sin redactar. |  |
| 4 | `nota` | `text` | no | Explicación de por qué la actividad aplica con una condición o variante en la modalidad; es lo que se muestra al administrador en la celda de la matriz. Siempre presente. |  |

## actos_adjudicacion

Acto administrativo de adjudicación del Ordenador del Gasto, con su notificación y publicación (EFDS-1159).

- Clave primaria: `id`
- Filas: 1
- Referencia a: `acto_documento_id` → `hiring.documentos` (0..1 → 1); `evidencia_documento_id` → `hiring.documentos` (0..1 → 0..1); `informe_definitivo_id` → `hiring.informes_definitivos` (0..1 → 1); `oferente_id` → `hiring.oferentes` (0..1 → 1); `proceso_id` → `hiring.procesos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla actos_adjudicacion. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | FK→hiring.procesos.id |
| 3 | `informe_definitivo_id` | `uuid` | no | Referencia al registro de hiring.informes_definitivos (id). | FK→hiring.informes_definitivos.id |
| 4 | `oferente_id` | `uuid` | no | Referencia al registro de hiring.oferentes (id). | FK→hiring.oferentes.id |
| 5 | `numero_acto` | `character varying(60)` | no | Número de la resolución de adjudicación del Ordenador del Gasto, tal como figura en el acto firmado (EFDS-1159). |  |
| 6 | `fecha_acto` | `date` | no | Fecha del acto administrativo de adjudicación. |  |
| 7 | `valor_adjudicado` | `numeric(18,2)` | no | _Por documentar_ |  |
| 8 | `acto_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 9 | `notificado_at` | `timestamp with time zone` | sí | Fecha y hora de notificación del acto de adjudicación; la notificación y la publicación en SECOP II se registran por separado, cada una con su evidencia. |  |
| 10 | `publicado_at` | `timestamp with time zone` | sí | Fecha y hora de la publicación. |  |
| 11 | `evidencia_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 12 | `estado` | `character varying(20)` | no | Estado del acto de adjudicación: vigente o revocado. |  |
| 13 | `emitido_por` | `character varying(200)` | sí | Usuario que registró la emisión del acto de adjudicación; se guarda el nombre de usuario de la cuenta autenticada (username del token; si falta, su correo o su identificador; «Sistema» si no hay ninguno). |  |
| 14 | `emitido_at` | `timestamp with time zone` | no | Fecha y hora en que se registró la emisión del acto de adjudicación. |  |
| 15 | `revocado_at` | `timestamp with time zone` | sí | Fecha y hora de revocación del acto de adjudicación. Revocar no borra el registro. |  |
| 16 | `revocado_por` | `character varying(200)` | sí | Usuario que realizó la revocación. |  |
| 17 | `motivo_revocacion` | `text` | sí | Motivo de la revocación. |  |
| 18 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 19 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 20 | `correo_contratista` | `character varying(200)` | sí | Correo del adjudicatario, para notificarle desde la plataforma. Su registro maestro vive en Click. | Contacto |

## adendas

Adendas de fondo y de cronograma del proceso, con su emisión y su publicación (EFDS-1154).

- Clave primaria: `id`
- Filas: 3
- Referencia a: `documento_id` → `hiring.documentos` (0..1 → 1); `evidencia_documento_id` → `hiring.documentos` (0..1 → 0..1); `proceso_id` → `hiring.procesos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla adendas. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | FK→hiring.procesos.id |
| 3 | `numero` | `integer` | no | Número consecutivo de la adenda dentro del proceso, con el que se cita (por ejemplo, «adenda 2»); no es global. |  |
| 4 | `tipo` | `character varying(20)` | no | Tipo de adenda: de fondo o de cronograma. |  |
| 5 | `objeto` | `text` | no | Descripción de lo que cambia la adenda; es el texto que se muestra en el listado del expediente. |  |
| 6 | `documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 7 | `estado` | `character varying(20)` | no | Estado de la adenda: emitida, publicada o anulada. |  |
| 8 | `emitida_por` | `character varying(200)` | sí | Usuario que emitió la adenda; se guarda el nombre de usuario de la cuenta autenticada (username del token; si falta, su correo o su identificador; «Sistema» si no hay ninguno). |  |
| 9 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 10 | `fecha_publicacion` | `date` | sí | _Por documentar_ |  |
| 11 | `evidencia_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 12 | `publicada_por` | `character varying(200)` | sí | Usuario que realizó la publicación. |  |
| 13 | `vencimiento_anterior` | `date` | sí | Vencimiento del plazo de publicidad antes de aplicar la adenda de cronograma. |  |
| 14 | `vencimiento_nuevo` | `date` | sí | Nueva fecha de vencimiento del plazo de publicidad fijada por una adenda de tipo CRONOGRAMA; se registra al emitirla y, al publicarla, reemplaza la fecha de vencimiento de la publicación del pliego. Vacía en las adendas de FONDO y obligatoria cuando la adenda es de CRONOGRAMA y está PUBLICADA. |  |
| 15 | `anulada_at` | `timestamp with time zone` | sí | Fecha y hora de la anulación. |  |
| 16 | `anulada_por` | `character varying(200)` | sí | Usuario que realizó la anulación. |  |
| 17 | `motivo_anulacion` | `text` | sí | Motivo de la anulación. |  |

## afiliaciones_arl

Afiliación a riesgos laborales, exigida a los contratistas persona natural (EFDS-1164).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `contrato_id` → `hiring.contratos` (0..1 → 1); `soporte_documento_id` → `hiring.documentos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla afiliaciones_arl. Se genera automáticamente. | PK |
| 2 | `contrato_id` | `uuid` | no | Referencia al registro de hiring.contratos (id). | única FK→hiring.contratos.id |
| 3 | `afiliado_por` | `character varying(20)` | no | Quién realizó la afiliación del contratista a riesgos laborales: ENTIDAD o CONTRATISTA (EFDS-1164). |  |
| 4 | `administradora` | `character varying(200)` | no | Nombre de la administradora de riesgos laborales (ARL). |  |
| 5 | `numero_afiliacion` | `character varying(80)` | sí | Número de la afiliación o certificado expedido por la ARL. |  |
| 6 | `fecha_afiliacion` | `date` | no | Fecha de afiliación a riesgos laborales (ARL). |  |
| 7 | `soporte_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 8 | `registrada_por` | `character varying(200)` | sí | Usuario que realizó el registro. |  |
| 9 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## alcances_permiso

_Por documentar._

- Clave primaria: `id`
- Filas: 313
- Referencia a: `numeral` → `hiring.actividades` (0..* → 0..1); `rol_id` → `auth.role` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla alcances_permiso. Se genera automáticamente. | PK |
| 2 | `rol_id` | `uuid` | no | Referencia al registro de auth.role (id). | FK→auth.role.id |
| 3 | `accion` | `character varying(10)` | no | Acción que el permiso habilita al rol. Valores permitidos: aprobar, decidir, editar, ver. |  |
| 4 | `etapa` | `smallint` | sí | Etapa del proceso contractual a la que se limita el permiso, de 1 a 10. Solo se diligencia uno entre etapa, numeral y trámite. |  |
| 5 | `numeral` | `character varying(20)` | sí | Referencia al registro de hiring.actividades (numeral). | FK→hiring.actividades.numeral |
| 6 | `tramite` | `character varying(10)` | sí | Trámite al que se limita el permiso, para los que no tienen numeral en la matriz: INC.1 (reporte de presunto incumplimiento) o INC.2 (trámite sancionatorio). Vacío cuando el permiso se da por etapa, por numeral o para todo el módulo. |  |
| 7 | `confirmado` | `boolean` | no | Indica si el alcance del permiso está confirmado. |  |
| 8 | `activo` | `boolean` | no | Indica si el alcance del permiso está activo. |  |
| 9 | `created_by` | `character varying(150)` | sí | Usuario que creó el registro. |  |
| 10 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 11 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## amparos

Coberturas de cada garantía con su vigencia, para controlar vencimientos (EFDS-1164).

- Clave primaria: `id`
- Filas: 1
- Referencia a: `garantia_id` → `hiring.garantias` (0..1 → 1); `tipo` → `hiring.tipos_amparo` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla amparos. Se genera automáticamente. | PK |
| 2 | `garantia_id` | `uuid` | no | Referencia al registro de hiring.garantias (id). | FK→hiring.garantias.id |
| 3 | `tipo` | `character varying(60)` | no | Referencia al registro de hiring.tipos_amparo (codigo). | FK→hiring.tipos_amparo.codigo |
| 4 | `valor_asegurado` | `numeric(18,2)` | no | Valor asegurado por el amparo de la garantía, en pesos; lo digita el usuario al legalizar el contrato y debe ser mayor que cero. |  |
| 5 | `vigencia_desde` | `date` | no | Fecha de inicio de la vigencia del amparo; cada amparo de la garantía tiene su propia vigencia porque no todos vencen a la vez. |  |
| 6 | `vigencia_hasta` | `date` | no | Fecha de fin de la vigencia del amparo. Debe ser posterior a vigencia_desde. |  |
| 7 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## aperturas_proceso

Resolución de apertura y pliego definitivo de cada proceso (EFDS-1152).

- Clave primaria: `id`
- Filas: 3
- Referencia a: `pliego_documento_id` → `hiring.documentos` (0..1 → 1); `proceso_id` → `hiring.procesos` (0..1 → 1); `resolucion_documento_id` → `hiring.documentos` (0..1 → 1); `evidencia_documento_id` → `hiring.documentos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla aperturas_proceso. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | única FK→hiring.procesos.id |
| 3 | `resolucion_numero` | `character varying(80)` | no | Número del acto administrativo (resolución) con el que se abre formalmente el proceso (actividad 5.7). |  |
| 4 | `resolucion_fecha` | `date` | no | Fecha del acto administrativo de apertura del proceso, no la del registro en el sistema; cuenta para los términos siguientes. |  |
| 5 | `resolucion_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 6 | `pliego_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 7 | `secop_url` | `text` | sí | Dirección web del proceso publicado en SECOP. |  |
| 8 | `abierto_por` | `character varying(200)` | sí | Usuario que registró la apertura del proceso; se guarda el nombre de usuario de la cuenta autenticada (username del token; si falta, su correo o su identificador; «Sistema» si no hay ninguno). |  |
| 9 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 10 | `evidencia_documento_id` | `uuid` | no | Soporte de que el pliego definitivo se publicó; admite captura de pantalla (EFDS-1399). | FK→hiring.documentos.id |

## audiencia_riesgos_config

En qué modalidades la audiencia de riesgos es obligatoria (EFDS-1153, RF-PUB-04).

- Clave primaria: `modalidad`
- Filas: 1
- Referencia a: `modalidad` → `hiring.modalidades` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `modalidad` | `character varying(60)` | no | Clave primaria de la tabla audiencia_riesgos_config: modalidad. | PK FK→hiring.modalidades.codigo |
| 2 | `obligatoria` | `boolean` | no | Indica si en la modalidad la audiencia de riesgos es obligatoria: sin ella celebrada el proceso no puede abrirse. Si la actividad aplica sin ser obligatoria, la audiencia se puede registrar pero no bloquea la apertura (RF-PUB-04). |  |
| 3 | `fundamento` | `text` | sí | Fundamento normativo o razón por la que la audiencia de riesgos es o no obligatoria en la modalidad. |  |
| 4 | `confirmado` | `boolean` | no | Indica si la obligatoriedad de la audiencia de riesgos para la modalidad está confirmada. |  |
| 5 | `updated_by` | `character varying(200)` | sí | Usuario que realizó la última actualización del registro. |  |
| 6 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## audiencias_adjudicacion

Audiencia de adjudicación del proceso, con su acta y lo que en ella se resolvió (EFDS-1159).

- Clave primaria: `id`
- Filas: 1
- Referencia a: `acta_documento_id` → `hiring.documentos` (0..1 → 1); `proceso_id` → `hiring.procesos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla audiencias_adjudicacion. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | FK→hiring.procesos.id |
| 3 | `celebrada_at` | `timestamp with time zone` | no | Fecha y hora en que se celebró la audiencia de adjudicación, como consta en el acta. |  |
| 4 | `presidida_por` | `character varying(200)` | no | Persona que presidió la audiencia de adjudicación, en texto tal como firma el acta; puede no tener cuenta en la plataforma. |  |
| 5 | `acta_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 6 | `resumen` | `text` | sí | Resumen del desarrollo de la audiencia de adjudicación que la entidad quiera dejar registrado. |  |
| 7 | `estado` | `character varying(20)` | no | Estado de la audiencia de adjudicación: celebrada o anulada. |  |
| 8 | `registrada_por` | `character varying(200)` | sí | Usuario que realizó el registro. |  |
| 9 | `registrada_at` | `timestamp with time zone` | no | Fecha y hora del registro. |  |
| 10 | `anulada_at` | `timestamp with time zone` | sí | Fecha y hora de la anulación. |  |
| 11 | `motivo_anulacion` | `text` | sí | Motivo de la anulación. |  |
| 12 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 13 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## audiencias_riesgos

Audiencias de asignación de riesgos celebradas, con su acta y su matriz consolidada.

- Clave primaria: `id`
- Filas: 3
- Referencia a: `acta_documento_id` → `hiring.documentos` (0..1 → 1); `matriz_documento_id` → `hiring.documentos` (0..1 → 1); `proceso_id` → `hiring.procesos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla audiencias_riesgos. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | FK→hiring.procesos.id |
| 3 | `fecha_celebracion` | `date` | no | Fecha de celebración de la audiencia de riesgos, no la del registro; de ella depende que el proceso pueda abrirse. |  |
| 4 | `acta_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 5 | `matriz_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 6 | `observaciones` | `text` | sí | Observaciones sobre la audiencia de asignación de riesgos. |  |
| 7 | `registrado_por` | `character varying(200)` | sí | Usuario que realizó el registro. |  |
| 8 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `anulada_at` | `timestamp with time zone` | sí | Fecha y hora de anulación de la audiencia de riesgos. Corregir una audiencia mal registrada la anula y obliga a registrarla de nuevo; el acta anterior queda en el expediente. |  |
| 10 | `anulada_por` | `character varying(200)` | sí | Usuario que realizó la anulación. |  |
| 11 | `motivo_anulacion` | `text` | sí | Motivo de la anulación. |  |

## audiencias_sancionatorias

Audiencias del trámite sancionatorio (EFDS-1181, RF-INC-02). La citación mira al futuro; el acta, al hecho ya ocurrido.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `acta_documento_id` → `hiring.documentos` (0..1 → 0..1); `caso_id` → `hiring.casos_incumplimiento` (0..1 → 1); `citacion_documento_id` → `hiring.documentos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla audiencias_sancionatorias. Se genera automáticamente. | PK |
| 2 | `caso_id` | `uuid` | no | Referencia al registro de hiring.casos_incumplimiento (id). | FK→hiring.casos_incumplimiento.id |
| 3 | `citada_para` | `timestamp with time zone` | no | Fecha y hora para la que se citó la audiencia del trámite sancionatorio (EFDS-1181). |  |
| 4 | `citacion_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 5 | `objeto` | `text` | sí | Propósito para el que se cita la audiencia sancionatoria, cuando se precisa. |  |
| 6 | `estado` | `character varying(20)` | no | Estado de la audiencia sancionatoria: citada, celebrada, suspendida o cancelada. |  |
| 7 | `celebrada_el` | `date` | sí | Fecha en que se celebró la audiencia sancionatoria. Obligatoria cuando el estado es CELEBRADA, junto con el acta y un resumen. |  |
| 8 | `acta_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 9 | `resumen` | `text` | sí | Resumen de lo ocurrido en la audiencia celebrada; es lo que la decisión posterior debe poder citar. Celebrar la audiencia exige acta y resumen. |  |
| 10 | `motivo` | `text` | sí | Motivo por el que la audiencia no se celebró, cuando no se celebró. |  |
| 11 | `citada_por` | `character varying(200)` | sí | Usuario que registró la citación a la audiencia; se guarda el nombre de usuario de la cuenta autenticada (username del token; si falta, su correo o su identificador; «Sistema» si no hay ninguno). |  |
| 12 | `registrada_por` | `character varying(200)` | sí | Usuario que realizó el registro. |  |
| 13 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## avisos

Lo que cambió la Dirección sobre los avisos de cada actividad. Sin fila, la actividad avisa con lo sugerido.

- Clave primaria: `numeral`, `evento`
- Filas: 0
- Referencia a: `numeral` → `hiring.actividades` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `numeral` | `character varying(10)` | no | Clave primaria de la tabla avisos: numeral. | PK FK→hiring.actividades.numeral |
| 2 | `evento` | `character varying(40)` | no | Clave primaria de la tabla avisos: evento. | PK |
| 3 | `activo` | `boolean` | no | Indica si el aviso de la actividad está activo. |  |
| 4 | `papeles` | `jsonb` | no | Papeles en el proceso que reciben el aviso, como lista en formato JSON: ABOGADO, CONTRATACION, RADICADOR, QUIEN_ENVIO o QUIEN_APRUEBA. Se resuelven para cada proceso en el momento del aviso. |  |
| 5 | `roles` | `jsonb` | no | Códigos de rol de auth.role (columna code) que reciben el aviso, como lista JSON; el aviso llega a todas las cuentas que tengan el rol en auth.user_roles. |  |
| 6 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 7 | `updated_by` | `character varying(120)` | sí | Usuario que realizó la última actualización del registro. |  |
| 8 | `personas` | `jsonb` | no | Ids de persona (auth.personas.id_person) a los que además llega el aviso. |  |
| 9 | `dependencias` | `jsonb` | no | Ids de auth.dependencias: el aviso llega a todas las personas de cada una. |  |
| 10 | `titulo` | `character varying(120)` | sí | Título del aviso con variables ({actividad}, {proceso}…). Nulo: el de siempre. |  |
| 11 | `mensaje` | `text` | sí | Cuerpo del aviso con variables ({actividad}, {proceso}, {quien}…). Nulo: el de siempre. |  |
| 12 | `correos_externos` | `jsonb` | no | Direcciones de correo de fuera de la plataforma que también reciben el aviso, solo por correo. | Contacto |
| 13 | `al_contratista` | `boolean` | no | Si el aviso llega también al correo del contratista, tomado del acto de adjudicación vigente. |  |

## avisos_habilitacion

Actividades de cada proceso de las que ya salió el aviso de «te toca». Evita repetirlo.

- Clave primaria: `proceso_id`, `numeral`
- Filas: 156
- Referencia a: `numeral` → `hiring.actividades` (0..* → 1); `proceso_id` → `hiring.procesos` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `proceso_id` | `uuid` | no | Identificador único del registro en la tabla avisos_habilitacion. | PK FK→hiring.procesos.id |
| 2 | `numeral` | `character varying(10)` | no | Clave primaria de la tabla avisos_habilitacion: numeral. | PK FK→hiring.actividades.numeral |
| 3 | `avisado_at` | `timestamp with time zone` | no | Fecha y hora en que se envió el aviso de habilitación de la actividad. |  |

## campos_formulario

_Por documentar._

- Clave primaria: `id`
- Filas: 13

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla campos_formulario. Se genera automáticamente. | PK |
| 2 | `numeral` | `character varying(20)` | no | Numeral de la actividad de la matriz de flujo a cuyo formulario pertenece el campo. |  |
| 3 | `codigo` | `character varying(80)` | no | Código del campo de formulario. |  |
| 4 | `etiqueta` | `character varying(300)` | no | Texto que se muestra como etiqueta del campo en el formulario. |  |
| 5 | `ayuda` | `text` | sí | Texto de ayuda que se muestra junto al campo. |  |
| 6 | `tipo` | `character varying(30)` | no | Tipo de campo de formulario: texto, texto largo, número, moneda, fecha, casilla, selección, archivo o responsable. |  |
| 7 | `obligatorio` | `boolean` | no | Indica si el campo de formulario es obligatorio. |  |
| 8 | `grupo` | `character varying(120)` | sí | Grupo o sección del formulario en la que se muestra el campo. |  |
| 9 | `orden` | `integer` | no | Posición del campo en el orden de presentación del formulario. |  |
| 10 | `opciones` | `jsonb` | sí | Valores admitidos para el campo cuando su tipo es seleccion, como lista JSON de textos. Obligatoria cuando el tipo es seleccion. |  |
| 11 | `activo` | `boolean` | no | Indica si el campo de formulario está activo. |  |
| 12 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 13 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 14 | `requiere_documento` | `boolean` | no | Reservado para actividades cuyo entregable es un documento, no un dato. |  |
| 15 | `solo_lectura` | `boolean` | no | Indica si el campo se muestra sin poder editarse porque su valor se captura fuera del formulario; hoy aplica solo a valor_estimado, que se registra al crear el proceso para determinar la modalidad por cuantía (EFDS-1147). |  |

## casos_incumplimiento

Reportes de presunto incumplimiento del contrato (EFDS-1180, RF-INC-01).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `contrato_id` → `hiring.contratos` (0..1 → 1); `documento_id` → `hiring.documentos` (0..1 → 0..1); `supervision_id` → `hiring.supervisiones_contrato` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla casos_incumplimiento. Se genera automáticamente. | PK |
| 2 | `contrato_id` | `uuid` | no | Referencia al registro de hiring.contratos (id). | FK→hiring.contratos.id |
| 3 | `motivo` | `text` | no | Descripción de lo observado como presunto incumplimiento; es lo que el área jurídica lee para decidir si abre trámite. Obligatoria y de al menos 10 caracteres (EFDS-1180). |  |
| 4 | `fecha_hecho` | `date` | no | Fecha en que ocurrió el hecho, no la de su registro; de ella dependen los términos del trámite sancionatorio. |  |
| 5 | `documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 6 | `estado` | `character varying(20)` | no | REPORTADO lo abre el supervisor (EFDS-1180); EN_TRAMITE, DECIDIDO y ARCHIVADO los mueve el trámite sancionatorio (EFDS-1181). |  |
| 7 | `reportado_por` | `character varying(200)` | sí | Usuario que reportó el presunto incumplimiento; con el dato de en calidad de qué lo hizo, deja constancia de quién supervisaba el día en que se constató el hecho. Se guarda el nombre de usuario de la cuenta autenticada (username del token; si falta, su correo o su identificador; «Sistema» si no hay ninguno). |  |
| 8 | `supervision_id` | `uuid` | sí | Referencia al registro de hiring.supervisiones_contrato (id). | FK→hiring.supervisiones_contrato.id |
| 9 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## causales_contratacion

Actividad 3.6 (3.5.1 de la matriz): causales que habilitan contratar por una modalidad. La matriz la describe como «filtro según la modalidad» y solo la marca aplicable en selección abreviada de menor cuantía y en contratación directa.

- Clave primaria: `codigo`
- Filas: 14
- Referencia a: `modalidad` → `hiring.modalidades` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `codigo` | `character varying(60)` | no | Clave primaria de la tabla causales_contratacion: código. | PK |
| 2 | `modalidad` | `character varying(60)` | no | Referencia al registro de hiring.modalidades (codigo). | FK→hiring.modalidades.codigo |
| 3 | `nombre` | `character varying(300)` | no | Nombre de la causal de contratación. |  |
| 4 | `referencia_normativa` | `character varying(200)` | no | Disposición normativa que sustenta la causal, tal como se cita en el expediente. |  |
| 5 | `orden` | `integer` | no | Posición de la causal de contratación en el orden de presentación. |  |
| 6 | `activa` | `boolean` | no | Indica si la causal se sigue ofreciendo; las derogadas se desactivan sin afectar los procesos que las usaron. |  |
| 7 | `confirmada` | `boolean` | no | False mientras la Dirección de Contratación no ratifique la fila. La semilla sale de la lectura del equipo sobre la Ley 1150 de 2007, no de un anexo firmado. |  |
| 8 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## cdp

Certificado de Disponibilidad Presupuestal del proceso. Requisito previo a la apertura (EFDS-1148).

- Clave primaria: `id`
- Filas: 4
- Referencia a: `documento_id` → `hiring.documentos` (0..1 → 0..1); `modificacion_id` → `hiring.modificaciones_contrato` (0..1 → 0..1); `proceso_id` → `hiring.procesos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla cdp. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | FK→hiring.procesos.id |
| 3 | `numero` | `character varying(60)` | sí | Número del Certificado de Disponibilidad Presupuestal, asignado por la Dirección Financiera al expedirlo; vacío mientras el CDP está solicitado. |  |
| 4 | `valor` | `numeric(18,2)` | sí | Valor del certificado de disponibilidad presupuestal, en pesos. Se registra el valor solicitado y, al expedir, se reemplaza por el valor certificado por la Dirección Financiera. Obligatorio cuando el estado es EXPEDIDO y mayor que cero. |  |
| 5 | `rubro` | `character varying(160)` | sí | Rubro presupuestal que respalda el gasto. Lo registra la Financiera al verificar (4.2) y puede corregirlo al expedir (4.3); el área puede adelantarlo si lo conoce. |  |
| 6 | `fecha_expedicion` | `date` | sí | Fecha de expedición del certificado de disponibilidad presupuestal (CDP). |  |
| 7 | `vigencia_fiscal` | `integer` | sí | Año de la vigencia fiscal a la que se imputa el CDP; un CDP no cruza vigencias. |  |
| 8 | `estado` | `character varying(20)` | no | Estado del CDP en su flujo: SOLICITADO, VERIFICADO, EXPEDIDO o RECHAZADO (sin disponibilidad en el rubro). ANULADO está fuera del flujo normal y corresponde al CDP que se deja sin efecto. |  |
| 9 | `observaciones` | `text` | sí | Motivo por el que la Dirección Financiera rechazó el CDP. |  |
| 10 | `solicitado_por` | `character varying(160)` | sí | Usuario que realizó la solicitud. |  |
| 11 | `solicitado_at` | `timestamp with time zone` | no | Fecha y hora de la solicitud. |  |
| 12 | `expedido_por` | `character varying(160)` | sí | Usuario que registró la expedición del CDP en la plataforma, no el funcionario que lo firma; se guarda el nombre de usuario de la cuenta autenticada (username del token; si falta, su correo o su identificador; «Sistema» si no hay ninguno). |  |
| 13 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 14 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 15 | `documento_id` | `uuid` | sí | Soporte documental del CDP en el expediente (actividad 4.4). | FK→hiring.documentos.id |
| 16 | `modificacion_id` | `uuid` | sí | La adición que este CDP respalda; nulo si es el CDP del proceso (EFDS-1176). | FK→hiring.modificaciones_contrato.id |

## cierres_contrato

Cierre definitivo del contrato tras vencer los amparos de estabilidad y calidad (EFDS-1175).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `contrato_id` → `hiring.contratos` (0..1 → 1); `soporte_documento_id` → `hiring.documentos` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla cierres_contrato. Se genera automáticamente. | PK |
| 2 | `contrato_id` | `uuid` | no | Referencia al registro de hiring.contratos (id). | FK→hiring.contratos.id |
| 3 | `fecha_cierre` | `date` | no | Fecha de cierre definitivo del contrato. |  |
| 4 | `amparos_verificados` | `jsonb` | no | Amparos de estabilidad y calidad (ESTABILIDAD_OBRA, CALIDAD_SERVICIO, CALIDAD_BIENES) de las garantías aprobadas, revisados para el cierre y guardados como estaban al cerrar, en una lista JSON con tipo, nombre, numeroPoliza, vigenciaHasta y vencido (EFDS-1175). Lo calcula el sistema. |  |
| 5 | `ultimo_vencimiento` | `date` | sí | Fecha en que vence o venció el último amparo de estabilidad o calidad del contrato. La calcula el sistema a partir de hiring.amparos (la mayor vigencia_hasta de esos amparos en garantías aprobadas). Vacía cuando el contrato no tenía ninguno, como suele ocurrir en los contratos de servicios profesionales. |  |
| 6 | `soporte_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 7 | `observaciones` | `text` | sí | Observaciones sobre el cierre del contrato. |  |
| 8 | `estado` | `character varying(20)` | no | Estado del cierre del contrato: vigente o revertido. |  |
| 9 | `cerrado_por` | `character varying(200)` | sí | Usuario que realizó el cierre. |  |
| 10 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 11 | `revertido_at` | `timestamp with time zone` | sí | Fecha y hora en que se revirtió el cierre del contrato. |  |
| 12 | `revertido_por` | `character varying(200)` | sí | Usuario que revirtió el cierre del contrato; se guarda el nombre de usuario de la cuenta autenticada (username del token; si falta, su correo o su identificador; «Sistema» si no hay ninguno). |  |
| 13 | `motivo_reversion` | `text` | sí | Motivo de la reversión. |  |

## cierres_financieros

Pago final y liberación del saldo no comprometido del RP (EFDS-1173).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `contrato_id` → `hiring.contratos` (0..1 → 1); `rp_id` → `hiring.registros_presupuestales` (0..1 → 1); `soporte_documento_id` → `hiring.documentos` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla cierres_financieros. Se genera automáticamente. | PK |
| 2 | `contrato_id` | `uuid` | no | Referencia al registro de hiring.contratos (id). | FK→hiring.contratos.id |
| 3 | `rp_id` | `uuid` | no | Referencia al registro de hiring.registros_presupuestales (id). | FK→hiring.registros_presupuestales.id |
| 4 | `referencia_pago_final` | `character varying(120)` | no | _Por documentar_ |  |
| 5 | `fecha_pago_final` | `date` | no | Fecha del pago final del contrato. |  |
| 6 | `soporte_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 7 | `valor_rp` | `numeric(18,2)` | no | Respaldo presupuestal total del contrato al cierre, en pesos: suma de los valores de todos los registros presupuestales expedidos del contrato, incluidos los de las adiciones. Lo calcula el sistema; no se digita. |  |
| 8 | `valor_pagado` | `numeric(18,2)` | no | Valor total pagado al contratista al cierre, en pesos: suma de los pagos del contrato en estado TRAMITADO (lo tramitado, no lo cobrado). Lo calcula el sistema. |  |
| 9 | `valor_liberado` | `numeric(18,2)` | no | Saldo del respaldo presupuestal que volvió al presupuesto en el cierre financiero: valor_rp menos valor_pagado, o cero si lo pagado supera el RP. Se guarda calculado en ese momento y no cambia si después entra un pago rezagado. No puede ser negativo. |  |
| 10 | `observaciones` | `text` | sí | Observaciones sobre el cierre financiero del contrato. |  |
| 11 | `estado` | `character varying(20)` | no | Estado del cierre financiero: vigente o revertido. |  |
| 12 | `cerrado_por` | `character varying(200)` | sí | Usuario que realizó el cierre. |  |
| 13 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 14 | `revertido_at` | `timestamp with time zone` | sí | Fecha y hora en que se revirtió el cierre financiero. |  |
| 15 | `revertido_por` | `character varying(200)` | sí | Usuario que revirtió el cierre financiero; se guarda el nombre de usuario de la cuenta autenticada (username del token; si falta, su correo o su identificador; «Sistema» si no hay ninguno). |  |
| 16 | `motivo_reversion` | `text` | sí | Motivo de la reversión. |  |

## comites_evaluadores

Comités evaluadores designados por memorando, vigentes y revocados (EFDS-1156).

- Clave primaria: `id`
- Filas: 3
- Referencia a: `memorando_documento_id` → `hiring.documentos` (0..1 → 1); `proceso_id` → `hiring.procesos` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla comites_evaluadores. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | FK→hiring.procesos.id |
| 3 | `memorando_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 4 | `fecha_designacion` | `date` | no | Fecha del memorando de designación del comité evaluador, no la del registro. |  |
| 5 | `designado_por` | `character varying(200)` | sí | Usuario que registró la designación del comité evaluador en la plataforma, no quien firma el memorando; se guarda el nombre de usuario de la cuenta autenticada (username del token; si falta, su correo o su identificador; «Sistema» si no hay ninguno). |  |
| 6 | `estado` | `character varying(20)` | no | Estado del comité evaluador: vigente o revocado. |  |
| 7 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `revocado_at` | `timestamp with time zone` | sí | Fecha y hora de la revocación. |  |
| 9 | `revocado_por` | `character varying(200)` | sí | Usuario que realizó la revocación. |  |
| 10 | `motivo_revocacion` | `text` | sí | Motivo de la revocación. |  |

## contratos

Contratos generados a partir del formato de su tipología, con la aceptación del proponente (EFDS-1161).

- Clave primaria: `id`
- Filas: 1
- Referencia a: `contrato_firmado_documento_id` → `hiring.documentos` (0..1 → 0..1); `minuta_documento_id` → `hiring.documentos` (0..1 → 1); `plantilla_id` → `hiring.plantillas` (0..1 → 0..1); `proceso_id` → `hiring.procesos` (0..1 → 1); `tipologia` → `hiring.tipologias_contrato` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla contratos. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | FK→hiring.procesos.id |
| 3 | `tipologia` | `character varying(60)` | no | Referencia al registro de hiring.tipologias_contrato (codigo). | FK→hiring.tipologias_contrato.codigo |
| 4 | `numero` | `character varying(60)` | no | Número de contrato de la entidad, el que figura en la minuta. Único en el sistema. | única |
| 5 | `objeto` | `text` | no | Qué se contrató. Inmutable desde que el contrato se suscribe (RF-MOD-04): ninguna modificación contractual lo cambia. |  |
| 6 | `valor` | `numeric(18,2)` | no | _Por documentar_ |  |
| 7 | `plazo_dias` | `integer` | sí | Plazo de ejecución del contrato, en días calendario contados desde la fecha del acta de inicio (ese día es el primero). Entero entre 1 y 999; lo actualizan las prórrogas y las suspensiones aprobadas. |  |
| 8 | `contratista_documento` | `character varying(40)` | no | Número del documento de identificación del contratista adjudicatario, copiado al contratar y no referenciado al oferente, para conservar lo que dice la minuta. | Identificación |
| 9 | `contratista_nombre` | `character varying(300)` | no | Nombre o razón social del contratista. |  |
| 10 | `contratista_tipo` | `character varying(20)` | no | Tipo de persona del contratista al momento de contratar: NATURAL o JURIDICA. Determina si en la legalización se exige ARL (EFDS-1164). |  |
| 11 | `minuta_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 12 | `plantilla_id` | `uuid` | sí | Referencia al registro de hiring.plantillas (id). | FK→hiring.plantillas.id |
| 13 | `estado` | `character varying(20)` | no | Situación actual del contrato en su ciclo (EFDS-1184, RF-SIS-01). Las transiciones válidas las decide puedeTransicionar en contrato.entity.ts. |  |
| 14 | `generado_por` | `character varying(200)` | sí | Usuario que realizó la generación. |  |
| 15 | `generado_at` | `timestamp with time zone` | no | Fecha y hora de la generación. |  |
| 16 | `aceptado_at` | `timestamp with time zone` | sí | Fecha y hora en que el proponente aceptó el contrato. |  |
| 17 | `aceptado_por` | `character varying(200)` | sí | Nombre de la persona que aceptó el contrato en nombre del proponente; lo digita el usuario y no se toma de la cuenta autenticada. |  |
| 18 | `aceptado_observacion` | `text` | sí | Observación registrada al aceptar el contrato. |  |
| 19 | `rechazado_at` | `timestamp with time zone` | sí | Fecha y hora del rechazo. |  |
| 20 | `rechazado_por` | `character varying(200)` | sí | Usuario que realizó el rechazo. |  |
| 21 | `motivo_rechazo` | `text` | sí | Motivo del rechazo. |  |
| 22 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 23 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 24 | `perfeccionado_at` | `timestamp with time zone` | sí | Fecha y hora en que entró la segunda firma y el contrato quedó suscrito (EFDS-1162). |  |
| 25 | `contrato_firmado_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 26 | `legalizado_at` | `timestamp with time zone` | sí | Fecha y hora en que el contrato quedó legalizado, con todas las garantías aprobadas y, si el contratista es persona natural, la ARL registrada. La calcula el servicio (EFDS-1164). |  |
| 27 | `ejecucion_desde` | `date` | sí | Fecha de la reunión de inicio: desde cuándo el contrato está en ejecución (EFDS-1167). |  |

## declaratorias_desiertas

Declaratoria desierta del proceso: causal, motivación, acto firmado, notificación y publicación (EFDS-1160, RF-ADJ-02).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `acto_documento_id` → `hiring.documentos` (0..1 → 1); `evidencia_documento_id` → `hiring.documentos` (0..1 → 0..1); `informe_comite_documento_id` → `hiring.documentos` (0..1 → 0..1); `proceso_id` → `hiring.procesos` (0..1 → 1); `resultado_contradicho_id` → `hiring.resultados_evaluacion` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla declaratorias_desiertas. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | FK→hiring.procesos.id |
| 3 | `causal` | `character varying(30)` | no | Causal de la declaratoria desierta: SIN_OFERTAS (la recepción cerró sin ofertas) o SIN_OFERTAS_HABILITADAS (el comité no habilitó ninguna de las presentadas) (EFDS-1160). |  |
| 4 | `motivo` | `text` | no | Motivación del acto administrativo que declara desierto el proceso. Obligatoria. |  |
| 5 | `numero_acto` | `character varying(60)` | no | Número de la resolución que declara desierto el proceso, tal como figura en el acto firmado. |  |
| 6 | `fecha_acto` | `date` | no | Fecha del acto administrativo de declaratoria desierta. |  |
| 7 | `acto_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 8 | `informe_comite_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 9 | `ofertas_recibidas` | `integer` | no | Número de ofertas que había el día de la declaratoria, guardado como estaba en ese momento. Debe ser cero cuando la causal es SIN_OFERTAS y mayor que cero cuando es SIN_OFERTAS_HABILITADAS. |  |
| 10 | `resultado_contradicho_id` | `uuid` | sí | Referencia al registro de hiring.resultados_evaluacion (id). | FK→hiring.resultados_evaluacion.id |
| 11 | `notificada_at` | `timestamp with time zone` | sí | Fecha y hora de notificación de la declaratoria desierta; la notificación y la publicación se registran por separado, cada una con su evidencia. |  |
| 12 | `publicada_at` | `timestamp with time zone` | sí | Fecha y hora de la publicación. |  |
| 13 | `evidencia_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 14 | `estado` | `character varying(20)` | no | Estado de la declaratoria desierta: vigente o revocada. |  |
| 15 | `declarada_por` | `character varying(200)` | sí | Usuario que registró la declaratoria desierta; se guarda el nombre de usuario de la cuenta autenticada (username del token; si falta, su correo o su identificador; «Sistema» si no hay ninguno). |  |
| 16 | `declarada_at` | `timestamp with time zone` | no | Fecha y hora en que se registró la declaratoria desierta. |  |
| 17 | `revocada_at` | `timestamp with time zone` | sí | Fecha y hora de revocación de la declaratoria desierta. Revocar no borra el registro. |  |
| 18 | `revocada_por` | `character varying(200)` | sí | Usuario que realizó la revocación. |  |
| 19 | `motivo_revocacion` | `text` | sí | Motivo de la revocación. |  |
| 20 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 21 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## dias_no_habiles

Días no laborables propios de la ESAP, adicionales a los festivos nacionales que el servicio calcula (EFDS-1150).

- Clave primaria: `fecha`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `fecha` | `date` | no | Clave primaria de la tabla dias_no_habiles: fecha. | PK |
| 2 | `descripcion` | `character varying(120)` | no | Descripción del día no hábil. |  |
| 3 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## documentos

_Por documentar._

- Clave primaria: `id`
- Filas: 130
- Referencia a: `expediente_id` → `hiring.expedientes` (0..* → 1); `plantilla_id` → `hiring.plantillas` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla documentos. Se genera automáticamente. | PK |
| 2 | `expediente_id` | `uuid` | no | Referencia al registro de hiring.expedientes (id). | FK→hiring.expedientes.id |
| 3 | `numeral` | `character varying(20)` | sí | Numeral de la actividad de la matriz de flujo a la que corresponde el documento. |  |
| 4 | `tipo` | `character varying(30)` | no | Tipo de documento del expediente: ADJUNTO (archivo subido, en archivo_url) o SNAPSHOT_FORMULARIO (copia inmutable del formulario del estudio previo al momento del envío). |  |
| 5 | `nombre` | `character varying(300)` | no | Nombre del documento del expediente. |  |
| 6 | `archivo_url` | `text` | sí | Ruta interna del archivo adjunto en el almacenamiento del servicio (hiring/files/ o /files/ seguido de un nombre aleatorio); no es una URL pública. Obligatoria cuando el tipo es ADJUNTO. |  |
| 7 | `contenido_snapshot` | `jsonb` | sí | Copia inmutable de los datos del formulario en el momento de enviarlo, en formato JSON. Obligatoria cuando el tipo es SNAPSHOT_FORMULARIO. |  |
| 8 | `archivo_nombre_original` | `character varying(300)` | sí | Nombre original del archivo cargado. |  |
| 9 | `archivo_mime_type` | `character varying(120)` | sí | Tipo MIME del archivo cargado (por ejemplo, application/pdf). |  |
| 10 | `archivo_tamano` | `bigint` | sí | Tamaño del archivo cargado, en bytes (máximo 25 MB por archivo). |  |
| 11 | `hash_sha256` | `character(64)` | no | Hash SHA-256 del contenido del documento, en 64 caracteres hexadecimales, para garantizar la integridad probatoria del expediente ante entes de control. |  |
| 12 | `version` | `integer` | no | Número de versión del documento del expediente. |  |
| 13 | `subido_por` | `character varying(120)` | sí | Usuario que realizó la carga. |  |
| 14 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 15 | `plantilla_id` | `uuid` | sí | Formato del SIG del que salió este documento. NULL = adjunto adicional, no exigido por ningún formato. | FK→hiring.plantillas.id |

## documentos_proceso

_Por documentar._

- Clave primaria: `id`
- Filas: 40
- Referencia a: `documento_id` → `hiring.documentos` (0..1 → 1); `proceso_id` → `hiring.procesos` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla documentos_proceso. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | FK→hiring.procesos.id |
| 3 | `numeral` | `character varying(20)` | no | Numeral de la actividad de la matriz de flujo a la que corresponde el documento del proceso. |  |
| 4 | `codigo` | `character varying(60)` | no | Código del requisito de documentos_requeridos que cubre el documento cargado por el proceso. |  |
| 5 | `documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 6 | `cargado_por` | `character varying(200)` | sí | Usuario que realizó la carga. |  |
| 7 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `anulado_at` | `timestamp with time zone` | sí | Fecha y hora de anulación del documento del proceso. Un documento sustituido no se borra: se anula y se carga otro, y la versión anterior queda en el expediente. |  |
| 9 | `anulado_por` | `character varying(200)` | sí | Usuario que realizó la anulación. |  |

## documentos_requeridos

Catálogo de documentos que exige cada actividad, filtrado por modalidad (EFDS-1149).

- Clave primaria: `id`
- Filas: 23

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla documentos_requeridos. Se genera automáticamente. | PK |
| 2 | `numeral` | `character varying(20)` | no | Numeral de la actividad de la matriz de flujo que exige el documento (por ejemplo, 5.1). |  |
| 3 | `codigo` | `character varying(60)` | no | Código de negocio del documento requerido (por ejemplo, AVISO_CONVOCATORIA o PROYECTO_PLIEGO). |  |
| 4 | `nombre` | `character varying(200)` | no | Nombre del documento requerido. |  |
| 5 | `descripcion` | `text` | sí | Descripción del documento requerido. |  |
| 6 | `modalidades` | `jsonb` | no | Códigos de las modalidades de contratación en las que se exige el documento, como lista en formato JSON; una lista vacía significa que aplica a todas. |  |
| 7 | `obligatorio` | `boolean` | no | Indica si el documento requerido es obligatorio. |  |
| 8 | `orden` | `integer` | no | Posición del documento requerido en el orden de presentación. |  |
| 9 | `activo` | `boolean` | no | Indica si el documento requerido está activo. |  |
| 10 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 11 | `confirmado` | `boolean` | no | false mientras el requisito sea lectura del procedimiento por parte del equipo y no cita del formato de lista de chequeo. |  |
| 12 | `nota_fuente` | `text` | sí | De dónde sale el requisito, para poder contrastarlo cuando llegue el formato oficial. |  |
| 13 | `plantilla_codigo` | `character varying(40)` | sí | Código del formato de hiring.plantillas que se descarga para diligenciar el documento. Se ofrece la versión activa más reciente. |  |
| 14 | `tipologias` | `jsonb` | no | Valores de tipologia_contractual (3.1) a los que aplica el requisito; vacío = todas. |  |
| 15 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 16 | `informativo` | `boolean` | no | Solo de consulta: se ofrece su plantilla para descargar y no se carga nada (095). |  |

## entregables_informe

Consolidado de entregables del informe final (EFDS-1171).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `documento_id` → `hiring.documentos` (0..1 → 0..1); `informe_id` → `hiring.informes_finales` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla entregables_informe. Se genera automáticamente. | PK |
| 2 | `informe_id` | `uuid` | no | Referencia al registro de hiring.informes_finales (id). | FK→hiring.informes_finales.id |
| 3 | `descripcion` | `character varying(500)` | no | Descripción del entregable incluido en el informe final. |  |
| 4 | `fecha_entrega` | `date` | sí | Fecha en que se recibió el entregable. Vacía cuando el entregable se pactó y no se cumplió. |  |
| 5 | `observacion` | `text` | sí | Observación sobre el entregable del informe final. |  |
| 6 | `documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 7 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## evidencias_evaluacion

Documentos con que el comité sustenta su evaluación: verificaciones, cuadro comparativo, actas (EFDS-1157).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `documento_id` → `hiring.documentos` (0..1 → 1); `resultado_id` → `hiring.resultados_evaluacion` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla evidencias_evaluacion. Se genera automáticamente. | PK |
| 2 | `resultado_id` | `uuid` | no | Referencia al registro de hiring.resultados_evaluacion (id). | FK→hiring.resultados_evaluacion.id |
| 3 | `documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 4 | `descripcion` | `character varying(300)` | no | Descripción obligatoria de lo que se carga como evidencia de la evaluación del comité (por ejemplo, verificación jurídica, cuadro comparativo o acta de reunión) (EFDS-1157). |  |
| 5 | `cargada_por` | `character varying(200)` | sí | Usuario que realizó la carga. |  |
| 6 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## expedientes

_Por documentar._

- Clave primaria: `id`
- Filas: 10
- Referencia a: `proceso_id` → `hiring.procesos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla expedientes. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | única FK→hiring.procesos.id |
| 3 | `numero_expediente` | `character varying(60)` | no | Número único del expediente contractual. | única |
| 4 | `estado` | `character varying(40)` | no | Estado del expediente: abierto o archivado. |  |
| 5 | `fecha_apertura` | `timestamp with time zone` | no | Fecha y hora de apertura del expediente. |  |
| 6 | `archivado_at` | `timestamp with time zone` | sí | Fecha y hora en que se archivó el expediente en la plataforma (RF-SIS-04); la registra el sistema al archivar. El trámite en Active Document se identifica aparte con radicado_active_document. |  |
| 7 | `archivado_por` | `character varying(200)` | sí | Usuario que archivó el expediente; se guarda el nombre de usuario de la cuenta autenticada (username del token; si falta, su correo o su identificador; «Sistema» si no hay ninguno). |  |
| 8 | `indice_documental` | `jsonb` | sí | Índice congelado: qué documentos tenía el expediente el día en que se archivó (EFDS-1174). |  |
| 9 | `radicado_active_document` | `character varying(120)` | sí | Radicado que devuelve el sistema de gestión documental Active Document, transcrito manualmente porque no hay integración; es la prueba de que el archivo documental se tramitó (RF-SIS-04). |  |
| 10 | `observaciones_archivo` | `text` | sí | Observaciones registradas al archivar el expediente. |  |
| 11 | `reabierto_at` | `timestamp with time zone` | sí | Fecha y hora de la última reapertura del expediente archivado; el historial completo está en trazabilidad. Si tiene valor, motivo_reapertura es obligatorio. |  |
| 12 | `reabierto_por` | `character varying(200)` | sí | Usuario que hizo la última reapertura del expediente; se guarda el nombre de usuario de la cuenta autenticada (username del token; si falta, su correo o su identificador; «Sistema» si no hay ninguno). |  |
| 13 | `motivo_reapertura` | `text` | sí | Motivo de la reapertura del expediente. |  |

## firmas_contrato

Firmas del ordenador del gasto y del contratista, con su evidencia (EFDS-1162).

- Clave primaria: `id`
- Filas: 2
- Referencia a: `contrato_id` → `hiring.contratos` (1..* → 1); `evidencia_documento_id` → `hiring.documentos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla firmas_contrato. Se genera automáticamente. | PK |
| 2 | `contrato_id` | `uuid` | no | Referencia al registro de hiring.contratos (id). | FK→hiring.contratos.id |
| 3 | `parte` | `character varying(20)` | no | Parte del contrato que firma: ORDENADOR (la entidad) o CONTRATISTA. El contrato no se perfecciona hasta que firman ambas (EFDS-1162). |  |
| 4 | `firmante_nombre` | `character varying(300)` | no | Nombre de quien firma, copiado al registrar: por el ordenador, quien ejerce la competencia ese día; por el contratista, su representante. |  |
| 5 | `firmante_documento` | `character varying(40)` | sí | Número del documento de identificación de la persona que firma. | Identificación |
| 6 | `registrada_por` | `character varying(200)` | sí | Cuenta que registró la firma, que puede no ser la del firmante (por ejemplo, el gestor registra la del contratista con su evidencia). |  |
| 7 | `fecha_firma` | `date` | no | Fecha del acto de firma, no la del registro. Formato YYYY-MM-DD. |  |
| 8 | `evidencia_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 9 | `hash_documento` | `character(64)` | sí | Hash SHA-256, en 64 caracteres hexadecimales, del archivo cargado como evidencia de la firma; es el mismo que se guarda en hiring.documentos y permite demostrar que no cambió después. |  |
| 10 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## garantias

Pólizas constituidas por el contratista, con su revisión y aprobación (EFDS-1164).

- Clave primaria: `id`
- Filas: 1
- Referencia a: `contrato_id` → `hiring.contratos` (0..1 → 1); `documento_id` → `hiring.documentos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla garantias. Se genera automáticamente. | PK |
| 2 | `contrato_id` | `uuid` | no | Referencia al registro de hiring.contratos (id). | FK→hiring.contratos.id |
| 3 | `aseguradora` | `character varying(200)` | no | Nombre de la compañía aseguradora que expidió la póliza. |  |
| 4 | `numero_poliza` | `character varying(80)` | no | Número de la póliza de garantía. |  |
| 5 | `documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 6 | `estado` | `character varying(20)` | no | Estado de la garantía: cargada, aprobada o rechazada. |  |
| 7 | `cargada_por` | `character varying(200)` | sí | Usuario que realizó la carga. |  |
| 8 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `revisada_por` | `character varying(200)` | sí | Usuario que aprobó o rechazó la garantía en su revisión. |  |
| 10 | `revisada_at` | `timestamp with time zone` | sí | Fecha y hora de la revisión. |  |
| 11 | `motivo_rechazo` | `text` | sí | Motivo del rechazo. |  |

## informes_definitivos

Informe de evaluación definitivo, con el resultado congelado y lo que cambió desde el preliminar (EFDS-1159).

- Clave primaria: `id`
- Filas: 1
- Referencia a: `evidencia_documento_id` → `hiring.documentos` (0..1 → 0..1); `informe_documento_id` → `hiring.documentos` (0..1 → 0..1); `informe_preliminar_id` → `hiring.informes_evaluacion` (0..1 → 1); `proceso_id` → `hiring.procesos` (0..1 → 1); `resultado_id` → `hiring.resultados_evaluacion` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla informes_definitivos. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | FK→hiring.procesos.id |
| 3 | `informe_preliminar_id` | `uuid` | no | Referencia al registro de hiring.informes_evaluacion (id). | FK→hiring.informes_evaluacion.id |
| 4 | `resultado_id` | `uuid` | no | Referencia al registro de hiring.resultados_evaluacion (id). | FK→hiring.resultados_evaluacion.id |
| 5 | `resultado` | `jsonb` | no | Resultado vigente de la evaluación, congelado al generar el informe definitivo, en formato JSON con modalidad, resultadoId, ganadora (oferenteId, nombre, identificación), puntaje obtenido y máximo, valor evaluado, justificación, documento del informe del comité, evidencias y ofertas (número, nombre, identificación, valor ofertado y si es la ganadora). |  |
| 6 | `cambios` | `jsonb` | no | Cambios del informe definitivo respecto del preliminar, en formato JSON con huboRectificacion, motivoRectificacion, cambioLaGanadora, subsanacionesAceptadas (id, oferente, asunto) y escritosPresentados. Se guarda resuelto (EFDS-1159). |  |
| 7 | `ofertas_recibidas` | `integer` | no | Número de ofertas recibidas en el proceso. |  |
| 8 | `estado` | `character varying(20)` | no | Estado del informe de evaluación definitivo: borrador, publicado o anulado. |  |
| 9 | `informe_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 10 | `evidencia_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 11 | `generado_por` | `character varying(200)` | sí | Usuario que realizó la generación. |  |
| 12 | `generado_at` | `timestamp with time zone` | no | Fecha y hora de la generación. |  |
| 13 | `publicado_por` | `character varying(200)` | sí | Usuario que realizó la publicación. |  |
| 14 | `publicado_at` | `timestamp with time zone` | sí | Fecha y hora de la publicación. |  |
| 15 | `anulado_at` | `timestamp with time zone` | sí | Fecha y hora de la anulación. |  |
| 16 | `motivo_anulacion` | `text` | sí | Motivo de la anulación. |  |
| 17 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 18 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## informes_evaluacion

Informe de evaluación del proceso, con el resultado del comité congelado al momento de trasladarlo (EFDS-1158).

- Clave primaria: `id`
- Filas: 2
- Referencia a: `evidencia_documento_id` → `hiring.documentos` (0..1 → 0..1); `informe_documento_id` → `hiring.documentos` (0..1 → 0..1); `proceso_id` → `hiring.procesos` (0..1 → 1); `resultado_id` → `hiring.resultados_evaluacion` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla informes_evaluacion. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | FK→hiring.procesos.id |
| 3 | `numero` | `integer` | no | Número consecutivo del informe de evaluación dentro del proceso; distingue un informe anulado de su reemplazo. |  |
| 4 | `resultado_id` | `uuid` | no | Referencia al registro de hiring.resultados_evaluacion (id). | FK→hiring.resultados_evaluacion.id |
| 5 | `resultado` | `jsonb` | no | Resultado de la evaluación tal como estaba al generar el informe, en formato JSON: la oferta ganadora, su valoración, la justificación, las evidencias y las ofertas recibidas. No cambia si el comité rectifica después (EFDS-1158). |  |
| 6 | `ofertas_recibidas` | `integer` | no | Número de ofertas recibidas por el proceso al generar el informe; no son las habilitadas. Decide si el proceso sigue o se declara desierto (EFDS-1160). |  |
| 7 | `observacion_entidad` | `text` | sí | _Por documentar_ |  |
| 8 | `estado` | `character varying(20)` | no | Estado del informe de evaluación: borrador, trasladado, cerrado o anulado. |  |
| 9 | `informe_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 10 | `evidencia_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 11 | `generado_por` | `character varying(120)` | sí | Usuario que realizó la generación. |  |
| 12 | `generado_at` | `timestamp with time zone` | no | Fecha y hora de la generación. |  |
| 13 | `trasladado_por` | `character varying(120)` | sí | Usuario que dio traslado del informe de evaluación; se guarda el nombre de usuario de la cuenta autenticada (username del token; si falta, su correo o su identificador; «Sistema» si no hay ninguno). |  |
| 14 | `trasladado_at` | `timestamp with time zone` | sí | Fecha y hora en que se dio traslado del informe de evaluación; la registra el sistema al trasladar. Obligatoria cuando el estado es TRASLADADO o CERRADO. |  |
| 15 | `plazo_dias_habiles` | `integer` | sí | Plazo de traslado aplicado, en días hábiles, fijado al trasladar el informe; no cambia si después se corrige el plazo de la modalidad. |  |
| 16 | `vence_el` | `date` | sí | Fecha hasta la que se reciben subsanaciones; el término se cuenta en días hábiles y vence al final del día. Se fija al trasladar el informe. |  |
| 17 | `cerrado_por` | `character varying(120)` | sí | Usuario que realizó el cierre. |  |
| 18 | `cerrado_at` | `timestamp with time zone` | sí | Fecha y hora del cierre. |  |
| 19 | `nota_cierre` | `text` | sí | Nota del cierre del traslado con lo que no cabe en las respuestas, por ejemplo, que nadie presentó subsanaciones o que el comité rectificó a raíz de una subsanación aceptada. |  |
| 20 | `anulado_at` | `timestamp with time zone` | sí | Fecha y hora de la anulación. |  |
| 21 | `motivo_anulacion` | `text` | sí | Motivo de la anulación. |  |
| 22 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 23 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## informes_finales

Informe final del supervisor con el balance congelado de la ejecución (EFDS-1171).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `contrato_id` → `hiring.contratos` (0..1 → 1); `informe_documento_id` → `hiring.documentos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla informes_finales. Se genera automáticamente. | PK |
| 2 | `contrato_id` | `uuid` | no | Referencia al registro de hiring.contratos (id). | FK→hiring.contratos.id |
| 3 | `informe_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 4 | `fecha_elaboracion` | `date` | no | Fecha del informe final de ejecución, no la del registro (EFDS-1171). |  |
| 5 | `conclusion` | `text` | no | Conclusión del supervisor sobre la ejecución del contrato; es lo que la liquidación consulta sin abrir el documento. Entre 20 y 4.000 caracteres. |  |
| 6 | `balance` | `jsonb` | no | Balance de la ejecución del contrato congelado al elaborar el informe, en formato JSON con valorContrato, valorPagado (pagos en estado TRAMITADO), saldo, cuentasTramitadas, cuentasPendientes y fechaInicio (del acta de inicio). Lo calcula el sistema. |  |
| 7 | `estado` | `character varying(20)` | no | Estado del informe final del supervisor: vigente o anulado. |  |
| 8 | `elaborado_por` | `character varying(200)` | sí | Usuario que elaboró el informe final; se guarda el nombre de usuario de la cuenta autenticada (username del token; si falta, su correo o su identificador; «Sistema» si no hay ninguno). |  |
| 9 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 10 | `anulado_at` | `timestamp with time zone` | sí | Fecha y hora de la anulación. |  |
| 11 | `anulado_por` | `character varying(200)` | sí | Usuario que realizó la anulación. |  |
| 12 | `motivo_anulacion` | `text` | sí | Motivo de la anulación. |  |

## limitaciones_mipyme

Decisión de limitar o no la convocatoria a MIPYME, con las condiciones que se evaluaron (EFDS-1151).

- Clave primaria: `id`
- Filas: 2
- Referencia a: `proceso_id` → `hiring.procesos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla limitaciones_mipyme. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | única FK→hiring.procesos.id |
| 3 | `limitado` | `boolean` | no | Indica si la entidad decidió limitar la convocatoria a MIPYME; puede diferir del resultado del cálculo del sistema (EFDS-1151). |  |
| 4 | `condiciones_cumplidas` | `boolean` | no | Lo que arrojó el cálculo. Puede diferir de `limitado`: la entidad decide, no el sistema. |  |
| 5 | `manifestaciones_contadas` | `integer` | no | Número de manifestaciones de interés de MIPYME que entraron en el cálculo, guardado como estaba el día de la decisión. No puede ser negativo. |  |
| 6 | `valor_proceso` | `numeric(18,2)` | sí | Valor del proceso de contratación usado en el cálculo de la limitación a MIPYME, tal como regía al momento de la decisión (EFDS-1151). |  |
| 7 | `tope_valor_aplicado` | `numeric(18,2)` | sí | Tope de valor aplicado en el cálculo de la limitación a MIPYME, expresado en la unidad de unidad_tope_aplicada (SMMLV o PESOS), tal como regía al momento de la decisión (EFDS-1151). Se copia de hiring.parametros_mipyme. |  |
| 8 | `unidad_tope_aplicada` | `character varying(10)` | sí | Unidad del tope de valor aplicado en el cálculo, tal como regía al momento de la decisión (EFDS-1151). Valores: SMMLV o PESOS. |  |
| 9 | `minimo_manifestaciones` | `integer` | sí | Número mínimo de manifestaciones de interés exigido en el cálculo de la limitación a MIPYME, tal como regía al momento de la decisión (EFDS-1151). |  |
| 10 | `motivo` | `text` | sí | Motivo de la decisión sobre la limitación a MIPYME; es obligatorio cuando la decisión se aparta del cálculo del sistema. |  |
| 11 | `documento_id` | `uuid` | sí | Identificador del documento en hiring.documentos con el acto administrativo que sustenta la decisión de limitar o no la convocatoria a MIPYME; opcional. La migración no declara la FK. |  |
| 12 | `decidido_por` | `character varying(160)` | sí | Usuario que registró la decisión de limitar o no la convocatoria a MIPYME; se guarda el nombre de usuario de la cuenta autenticada (username del token; si falta, su correo o su identificador; «Sistema» si no hay ninguno). |  |
| 13 | `decidido_at` | `timestamp with time zone` | no | Fecha y hora de la decisión de limitar o no la convocatoria a MIPYME. Por defecto, la fecha y hora de creación del registro. |  |
| 14 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 15 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 16 | `smmlv_aplicado` | `numeric(18,2)` | sí | Salario mínimo con el que se convirtió el tope a pesos. Null si el tope se aplicó en pesos o si la decisión es anterior a esta columna. |  |

## manifestaciones_mipyme

Manifestaciones de interés de MIPYME en participar; su número decide la limitación (EFDS-1151).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `proceso_id` → `hiring.procesos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla manifestaciones_mipyme. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | FK→hiring.procesos.id |
| 3 | `nombre` | `character varying(200)` | no | Nombre de la MIPYME que manifiesta interés en participar. |  |
| 4 | `identificacion` | `character varying(60)` | no | Número de identificación (NIT o documento) de la MIPYME que manifiesta interés. Obligatorio para no contar dos veces la misma empresa. |  |
| 5 | `fecha_presentacion` | `date` | no | Fecha de presentación de la manifestación de interés de la MIPYME. |  |
| 6 | `documento_id` | `uuid` | sí | Identificador del documento en hiring.documentos que soporta la manifestación de interés presentada; opcional. La migración no declara la FK. |  |
| 7 | `registrado_por` | `character varying(160)` | sí | Usuario que realizó el registro. |  |
| 8 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## miembros_comite

Integrantes del comité evaluador con su dimensión de evaluación (EFDS-1156).

- Clave primaria: `id`
- Filas: 3
- Referencia a: `comite_id` → `hiring.comites_evaluadores` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla miembros_comite. Se genera automáticamente. | PK |
| 2 | `comite_id` | `uuid` | no | Referencia al registro de hiring.comites_evaluadores (id). | FK→hiring.comites_evaluadores.id |
| 3 | `persona_id` | `uuid` | no | Identificador (id_person) de auth.personas de la persona designada en el comité evaluador, sin llave foránea; permite enlazarla con la cuenta que evalúa (auth.user.id_person). |  |
| 4 | `nombre` | `character varying(200)` | no | Nombre del miembro del comité, copiado al momento de la designación tal como figura en el memorando. |  |
| 5 | `rol` | `character varying(20)` | no | Dimensión de evaluación a cargo del integrante. Valores permitidos: FINANCIERO, JURIDICO, TECNICO. |  |
| 6 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## modalidades

_Por documentar._

- Clave primaria: `codigo`
- Filas: 11

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `codigo` | `character varying(60)` | no | Clave primaria de la tabla modalidades: código. | PK |
| 2 | `nombre` | `character varying(160)` | no | Nombre de la modalidad de contratación. |  |
| 3 | `orden` | `integer` | no | Posición de la modalidad como columna en la matriz de flujo; define el orden de lectura de las columnas. |  |
| 4 | `activa` | `boolean` | no | Indica si la modalidad de selección se sigue ofreciendo. Las modalidades derogadas se desactivan sin afectar los procesos que ya las usan. |  |
| 5 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 6 | `determinada_por_cuantia` | `boolean` | no | False cuando la modalidad se elige por causal y no por monto (directa, 092/2017, enajenación). |  |

## modificaciones_contrato

Modificaciones contractuales de la actividad 9.5; hoy solo la adición tiene trámite (EFDS-1176).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `cdp_id` → `hiring.cdp` (0..1 → 0..1); `contrato_id` → `hiring.contratos` (0..1 → 1); `documento_id` → `hiring.documentos` (0..1 → 0..1); `reanuda_modificacion_id` → `hiring.modificaciones_contrato` (0..1 → 0..1); `rp_id` → `hiring.registros_presupuestales` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla modificaciones_contrato. Se genera automáticamente. | PK |
| 2 | `contrato_id` | `uuid` | no | Referencia al registro de hiring.contratos (id). | FK→hiring.contratos.id |
| 3 | `tipo` | `character varying(30)` | no | Tipo de modificación contractual, según los tipos que lista la matriz de flujo. A la fecha del código solo ADICION tiene implementación; los demás quedan declarados para historias posteriores (EFDS-1177, EFDS-1178). |  |
| 4 | `numero` | `character varying(80)` | sí | Consecutivo con el que la entidad identifica la modificación contractual. |  |
| 5 | `fecha_suscripcion` | `date` | sí | Fecha de suscripción de la modificación del contrato. |  |
| 6 | `justificacion` | `text` | no | Justificación de la modificación contractual: por qué se modifica el contrato. |  |
| 7 | `documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 8 | `estado` | `character varying(20)` | no | Estado de la modificación contractual. Flujo: EN_TRAMITE → APROBADA → REVOCADA; RECHAZADA es una salida temprana desde EN_TRAMITE. |  |
| 9 | `valor_adicionado` | `numeric(18,2)` | sí | Valor que se adiciona al contrato con una modificación de tipo ADICION, en la misma unidad que el valor del contrato (pesos), al que se suma cuando se aprueba. Obligatorio y mayor que cero cuando el tipo es ADICION; vacío en las prórrogas y las terminaciones anticipadas. |  |
| 10 | `cdp_id` | `uuid` | sí | Referencia al registro de hiring.cdp (id). | FK→hiring.cdp.id |
| 11 | `rp_id` | `uuid` | sí | Referencia al registro de hiring.registros_presupuestales (id). | FK→hiring.registros_presupuestales.id |
| 12 | `valor_contrato_antes` | `numeric(18,2)` | sí | Valor del contrato, en pesos, antes de aplicar la adición; se copia de contratos.valor al aprobarla y queda congelado para conservar sobre qué valor se calculó, aunque luego entren otras adiciones o cambie el tope. |  |
| 13 | `valor_contrato_despues` | `numeric(18,2)` | sí | Valor del contrato después de la adición. |  |
| 14 | `tope_porcentaje` | `numeric(5,2)` | sí | Porcentaje máximo de adición, sobre el valor inicial y acumulado, con el que se juzgó la adición; se copia al aprobarla del tope configurado en tope_adicion.porcentaje (sembrado en 50 % por la Ley 80 de 1993, art. 40). |  |
| 15 | `solicitada_por` | `character varying(200)` | sí | Nombre de usuario (username) de la cuenta autenticada que solicitó la modificación contractual; si el token no lo trae, se guarda el correo o el identificador. |  |
| 16 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 17 | `aprobada_por` | `character varying(200)` | sí | Nombre de usuario (username) de la cuenta autenticada que aprobó la modificación contractual; si el token no lo trae, se guarda el correo o el identificador. |  |
| 18 | `aprobada_at` | `timestamp with time zone` | sí | Fecha y hora de aprobación de la modificación contractual. |  |
| 19 | `revocada_at` | `timestamp with time zone` | sí | Fecha y hora de revocación de la modificación contractual. |  |
| 20 | `revocada_por` | `character varying(200)` | sí | Nombre de usuario (username) de la cuenta autenticada que revocó la modificación contractual; si el token no lo trae, se guarda el correo o el identificador. |  |
| 21 | `motivo_revocacion` | `text` | sí | Motivo de la revocación de la modificación contractual. |  |
| 22 | `dias_prorroga` | `integer` | sí | Días que la prórroga añade al plazo. La reanudación no lo usa: los suyos se derivan de las fechas. |  |
| 23 | `plazo_dias_antes` | `integer` | sí | Plazo del contrato en días calendario antes de la modificación; se llena al aprobar una prórroga o una reanudación y permite revocarla devolviendo el plazo anterior. contratos.plazo_dias guarda el plazo vigente. |  |
| 24 | `plazo_dias_despues` | `integer` | sí | Plazo del contrato en días después de la modificación. Se llena en la prórroga (plazo_dias_antes + dias_prorroga) y en la reanudación (plazo_dias_antes + días suspendidos en calendario); queda vacío si el contrato no tenía plazo. |  |
| 25 | `suspension_desde` | `date` | sí | Fecha de inicio de la suspensión del contrato, en formato AAAA-MM-DD. |  |
| 26 | `suspension_hasta` | `date` | sí | Fecha prevista de fin de la suspensión del contrato. Admite nulos porque hay suspensiones indefinidas; cuando se diligencia no puede ser anterior a suspension_desde. |  |
| 27 | `reanuda_modificacion_id` | `uuid` | sí | Referencia al registro de hiring.modificaciones_contrato (id). | FK→hiring.modificaciones_contrato.id |
| 28 | `reanudada_el` | `date` | sí | Fecha en que efectivamente se reanuda el contrato suspendido; prevalece sobre la fecha prevista de fin de la suspensión. Es obligatoria cuando el tipo es REANUDACION y no puede ser anterior a la fecha de suspensión. |  |
| 29 | `cedente_documento` | `character varying(40)` | sí | Número de documento de identificación del cedente, es decir, del contratista anterior en una cesión del contrato. La tabla contratos queda con los datos del cesionario. | Identificación |
| 30 | `cedente_nombre` | `character varying(300)` | sí | Nombre del cedente en la cesión del contrato. |  |
| 31 | `cedente_tipo` | `character varying(20)` | sí | Tipo de persona (NATURAL o JURIDICA) del cedente en una cesión del contrato; el sistema lo copia de contratos.contratista_tipo al aprobar la cesión. De él depende la exigencia de ARL (EFDS-1164) y se restaura si se revoca la cesión. |  |
| 32 | `cesionario_documento` | `character varying(40)` | sí | Número del documento de identificación del cesionario en la cesión del contrato. | Identificación |
| 33 | `cesionario_nombre` | `character varying(300)` | sí | Nombre del cesionario en la cesión del contrato. |  |
| 34 | `cesionario_tipo` | `character varying(20)` | sí | Tipo de persona del cesionario. Valores permitidos: NATURAL, JURIDICA. |  |
| 35 | `terminacion_causal` | `character varying(20)` | sí | MUTUO_ACUERDO o UNILATERAL, las dos que define la fuente. El incumplimiento no está aquí: es el proceso sancionatorio (EFDS-1181). |  |
| 36 | `terminacion_el` | `date` | sí | Fecha desde la cual el contrato deja de ejecutarse por terminación anticipada; no corresponde a la fecha de firma. Es obligatoria cuando el tipo es TERMINACION_ANTICIPADA, con causal MUTUO_ACUERDO o UNILATERAL. |  |
| 37 | `estado_contrato_antes` | `character varying(20)` | sí | Estado que tenía el contrato antes de la terminación anticipada (EJECUCION o SUSPENDIDO). Se guarda para que, al revocarla, el contrato vuelva a ese estado. |  |
| 38 | `objeto_contrato` | `text` | sí | El objeto del contrato el día en que se solicitó la modificación (RF-MOD-04). Aprobarla exige que siga siendo el mismo. |  |

## observaciones_pliego

Observaciones de interesados al proyecto de pliego publicado, con su respuesta (EFDS-1151).

- Clave primaria: `id`
- Filas: 4
- Referencia a: `proceso_id` → `hiring.procesos` (0..* → 1); `publicacion_id` → `hiring.publicaciones_pliego` (1..* → 1)
- Relaciones implícitas: `documento_id` ↝ `hiring.documentos` (100.0 % con padre)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla observaciones_pliego. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | FK→hiring.procesos.id |
| 3 | `publicacion_id` | `uuid` | no | Referencia al registro de hiring.publicaciones_pliego (id). | FK→hiring.publicaciones_pliego.id |
| 4 | `presentado_por` | `character varying(200)` | no | Nombre de la persona o empresa interesada que presenta la observación al proyecto de pliego. |  |
| 5 | `identificacion` | `character varying(60)` | sí | NIT o cédula de quien presenta la observación al proyecto de pliego. Opcional: las observaciones anónimas también se registran y se responden. |  |
| 6 | `fecha_presentacion` | `date` | no | Fecha en que el interesado presentó la observación, no la de su registro en la plataforma; determina si llegó en término. |  |
| 7 | `asunto` | `character varying(300)` | no | Asunto de la observación. |  |
| 8 | `contenido` | `text` | no | Texto de la observación presentada al proyecto de pliego. |  |
| 9 | `fuera_de_termino` | `boolean` | no | Congelado al registrar: si la fecha de presentación superó el vencimiento de la publicidad. |  |
| 10 | `documento_id` | `uuid` | sí | Referencia al documento soporte de la observación tal como llegó (hiring.documentos.id); relación sin llave foránea declarada. Opcional, porque la observación puede llegar por un canal que no deja documento. | ↝hiring.documentos.id |
| 11 | `registrado_por` | `character varying(160)` | sí | Usuario que realizó el registro. |  |
| 12 | `respuesta` | `text` | sí | Respuesta de la entidad a la observación presentada al proyecto de pliego. Se registra junto con respondida_at y modifico_pliego: las tres quedan vacías o las tres diligenciadas, y una vez respondida no se reescribe. |  |
| 13 | `respondida_por` | `character varying(160)` | sí | Nombre de usuario (username) de la cuenta autenticada que registró la respuesta a la observación; si el token no lo trae, se guarda el correo o el identificador. |  |
| 14 | `respondida_at` | `timestamp with time zone` | sí | Fecha y hora en que se respondió la observación. Se registra junto con respuesta y modifico_pliego. |  |
| 15 | `modifico_pliego` | `boolean` | sí | Indica si la observación llevó a cambiar el pliego; sustenta una adenda posterior (EFDS-1154). |  |
| 16 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 17 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## oferentes

Ofertas recibidas dentro del plazo, con su soporte. Al cerrar la recepción componen la lista publicada (EFDS-1155).

- Clave primaria: `id`
- Filas: 4
- Referencia a: `recepcion_id` → `hiring.recepciones_ofertas` (1..* → 1); `soporte_documento_id` → `hiring.documentos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla oferentes. Se genera automáticamente. | PK |
| 2 | `recepcion_id` | `uuid` | no | Referencia al registro de hiring.recepciones_ofertas (id). | FK→hiring.recepciones_ofertas.id |
| 3 | `numero` | `integer` | no | Consecutivo de la oferta dentro de la recepción, por orden de llegada; es relativo al proceso y es el que numera la lista publicada de oferentes. |  |
| 4 | `nombre` | `character varying(200)` | no | Nombre del oferente. |  |
| 5 | `identificacion` | `character varying(40)` | no | Número de identificación del oferente (NIT o documento). |  |
| 6 | `fecha_radicacion` | `timestamp with time zone` | no | Fecha y hora en que la oferta se radicó ante la entidad, no la del registro en la plataforma. |  |
| 7 | `soporte_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 8 | `registrado_por` | `character varying(200)` | sí | Usuario que realizó el registro. |  |
| 9 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 10 | `valor_ofertado` | `numeric(18,2)` | sí | Valor de la oferta tal como se presentó. Dato de la oferta, no base de cálculo: la evaluación se hace por fuera (EFDS-1157). |  |

## pagos_contrato

Cuentas de cobro del contrato, su aval y su trámite (EFDS-1170).

- Clave primaria: `id`
- Filas: 2
- Referencia a: `contrato_id` → `hiring.contratos` (1..* → 1); `factura_documento_id` → `hiring.documentos` (0..1 → 1); `informe_documento_id` → `hiring.documentos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla pagos_contrato. Se genera automáticamente. | PK |
| 2 | `contrato_id` | `uuid` | no | Referencia al registro de hiring.contratos (id). | FK→hiring.contratos.id |
| 3 | `numero` | `integer` | no | Consecutivo de la cuenta de cobro dentro del contrato (por ejemplo, «el pago 3 de 8»). Lo asigna el servicio. |  |
| 4 | `periodo_desde` | `date` | no | Fecha de inicio del periodo que se cobra en la cuenta de cobro, expresado como rango con periodo_hasta. No puede ser posterior a periodo_hasta. |  |
| 5 | `periodo_hasta` | `date` | no | Fecha de fin del periodo que cubre la cuenta de cobro. No puede ser anterior a periodo_desde. |  |
| 6 | `valor` | `numeric(18,2)` | no | Valor cobrado en la cuenta de cobro, en pesos. Debe ser mayor que cero. |  |
| 7 | `factura_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 8 | `informe_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 9 | `estado` | `character varying(20)` | no | Estado de la cuenta de cobro: radicado, avalado, devuelto, tramitado o anulado. |  |
| 10 | `radicado_at` | `timestamp with time zone` | no | Fecha y hora de la radicación. |  |
| 11 | `radicado_por` | `character varying(200)` | sí | Usuario que realizó la radicación. |  |
| 12 | `avalado_at` | `timestamp with time zone` | sí | Fecha y hora en que el supervisor vigente del contrato avaló la cuenta de cobro. Se borra si la cuenta se devuelve y es obligatoria cuando el estado es TRAMITADO. |  |
| 13 | `avalado_por` | `character varying(200)` | sí | Nombre de usuario (username) de la cuenta autenticada del supervisor vigente del contrato que avaló la cuenta de cobro; si el token no lo trae, se guarda el correo o el identificador. Se borra si la cuenta se devuelve. |  |
| 14 | `observacion_aval` | `text` | sí | Observación registrada al avalar la cuenta de cobro. |  |
| 15 | `devuelto_at` | `timestamp with time zone` | sí | Fecha y hora en que se devolvió la cuenta de cobro. Un CHECK la relaciona con el estado DEVUELTO. |  |
| 16 | `devuelto_por` | `character varying(200)` | sí | Nombre de usuario (username) de la cuenta autenticada que devolvió la cuenta de cobro (el supervisor vigente del contrato); si el token no lo trae, se guarda el correo o el identificador. |  |
| 17 | `motivo_devolucion` | `text` | sí | Motivo de la devolución. |  |
| 18 | `tramitado_at` | `timestamp with time zone` | sí | Fecha y hora en que la Dirección Financiera tramitó el pago de la cuenta de cobro avalada. Es obligatoria cuando el estado es TRAMITADO. |  |
| 19 | `tramitado_por` | `character varying(200)` | sí | Nombre de usuario (username) de la cuenta autenticada que tramitó la cuenta de cobro; si el token no lo trae, se guarda el correo o el identificador. |  |
| 20 | `referencia_pago` | `character varying(120)` | sí | Referencia con la que la Dirección Financiera tramitó el pago; permite ubicar el pago fuera de la plataforma. |  |
| 21 | `anulado_at` | `timestamp with time zone` | sí | Fecha y hora de la anulación. |  |
| 22 | `anulado_por` | `character varying(200)` | sí | Usuario que realizó la anulación. |  |
| 23 | `motivo_anulacion` | `text` | sí | Motivo de la anulación. |  |
| 24 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## parametros_alerta

Plazos que gobiernan las alertas de contratación: anticipación por vencimiento, tolerancia sin abogado y hora del aviso diario.

- Clave primaria: `clave`
- Filas: 6

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `clave` | `character varying(60)` | no | Clave primaria de la tabla parametros_alerta: clave. | PK |
| 2 | `valor` | `integer` | no | Valor vigente del parámetro de alerta; debe estar entre minimo y maximo. La unidad depende de la clave: días en las anticipaciones y en la tolerancia sin abogado, y hora de Bogotá (0 a 23) en hora_aviso. |  |
| 3 | `minimo` | `integer` | no | Valor mínimo que admite el parámetro de alerta. La pantalla lo muestra a quien edita y el servicio lo usa para rechazar valores fuera del rango. |  |
| 4 | `maximo` | `integer` | no | Valor máximo permitido para el parámetro. |  |
| 5 | `descripcion` | `text` | no | Descripción del parámetro de alerta. |  |
| 6 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 7 | `updated_by` | `character varying(120)` | sí | Usuario que realizó la última actualización del registro. |  |

## parametros_mipyme

Condiciones que habilitan la limitación a MIPYME. Parametrizables (EFDS-1393).

- Clave primaria: `clave`
- Filas: 2

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `clave` | `character varying(40)` | no | Clave primaria de la tabla parametros_mipyme: clave. | PK |
| 2 | `valor` | `numeric(18,2)` | no | Valor de la condición que habilita la limitación a MIPYME, expresado en la unidad indicada. Debe ser mayor que cero. |  |
| 3 | `unidad` | `character varying(10)` | sí | Unidad en que se expresa el valor del parámetro: SMMLV o PESOS para el tope; nula para el mínimo de manifestaciones, que es un conteo. |  |
| 4 | `descripcion` | `character varying(200)` | no | Descripción de la condición para la limitación a MIPYME. |  |
| 5 | `fundamento` | `text` | sí | Origen de la cifra del parámetro. En el tope, el decreto lo expresa en dólares y el valor registrado es una equivalencia derivada. |  |
| 6 | `confirmado` | `boolean` | no | Indica si la Dirección de Contratación confirmó la cifra del parámetro; es falso mientras no se confirme. |  |
| 7 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## participaciones_proceso

Quién está en cada proceso y con qué papel, vigentes y relevados, con el motivo del cambio (EFDS-1183).

- Clave primaria: `id`
- Filas: 17
- Referencia a: `proceso_id` → `hiring.procesos` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla participaciones_proceso. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | FK→hiring.procesos.id |
| 3 | `papel` | `character varying(20)` | no | Papel de la persona en el proceso. Valores permitidos: ABOGADO, CONTRATACION, FINANCIERA. |  |
| 4 | `usuario_id` | `uuid` | sí | Identificador de la cuenta de usuario asignada al proceso (id_user de auth."user", el valor que el token JWT trae en sub). Sin llave foránea declarada, por tratarse de un esquema de otro equipo. |  |
| 5 | `usuario_nombre` | `character varying(120)` | no | Nombre de usuario (username) de la cuenta asignada al proceso. Es el identificador que usan los listados y coincide con el que guarda procesos.created_by. |  |
| 6 | `persona_id` | `uuid` | sí | Identificador de la persona en el directorio (id_person) asociada a la cuenta asignada; permite mostrar cargo o dependencia. Nulo si la cuenta no tiene persona enlazada. |  |
| 7 | `nombre` | `character varying(200)` | no | Nombre de la persona asignada al proceso, copiado en el momento de la asignación. |  |
| 8 | `cargo` | `character varying(200)` | sí | Cargo de la persona asignada al proceso. |  |
| 9 | `email` | `character varying(200)` | sí | Correo electrónico del participante en el proceso. | Contacto |
| 10 | `asignado_por` | `character varying(200)` | sí | Usuario que asignó a la persona al proceso. En el papel CONTRATACION es la misma persona, que toma el proceso de la bandeja compartida. |  |
| 11 | `asignado_at` | `timestamp with time zone` | no | Fecha y hora de la asignación. |  |
| 12 | `estado` | `character varying(20)` | no | Estado de la participación en el proceso: vigente o relevado. |  |
| 13 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 14 | `relevado_at` | `timestamp with time zone` | sí | Fecha y hora en que la persona fue relevada del proceso. Un CHECK la relaciona con el estado RELEVADO. |  |
| 15 | `relevado_por` | `character varying(200)` | sí | Nombre de usuario (username) de la cuenta autenticada que registró el relevo; si el token no lo trae, se guarda el correo o el identificador. |  |
| 16 | `motivo_relevo` | `text` | sí | Motivo del relevo. |  |

## piezas_audiencia

Acta, grabaciones, observaciones y anexos que documentan la audiencia de adjudicación (EFDS-1159).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `audiencia_id` → `hiring.audiencias_adjudicacion` (0..1 → 1); `documento_id` → `hiring.documentos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla piezas_audiencia. Se genera automáticamente. | PK |
| 2 | `audiencia_id` | `uuid` | no | Referencia al registro de hiring.audiencias_adjudicacion (id). | FK→hiring.audiencias_adjudicacion.id |
| 3 | `documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 4 | `tipo` | `character varying(20)` | no | Tipo de pieza que documenta la audiencia además del acta: GRABACION (registro audiovisual), OBSERVACION (lo planteado en la audiencia y su respuesta) o ANEXO (otro documento que la entidad quiera dejar). |  |
| 5 | `descripcion` | `character varying(300)` | no | Descripción de la pieza que documenta la audiencia de adjudicación. |  |
| 6 | `cargada_por` | `character varying(200)` | sí | Usuario que realizó la carga. |  |
| 7 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## plantillas

_Por documentar._

- Clave primaria: `id`
- Filas: 10

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla plantillas. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(40)` | no | Código del formato en el Sistema Integrado de Gestión (Isolución), por ejemplo BS-FO-047. |  |
| 3 | `nombre` | `character varying(400)` | no | Nombre de la plantilla. |  |
| 4 | `numeral` | `character varying(20)` | no | Numeral de la actividad de la matriz de flujo de contratación a la que corresponde el formato (por ejemplo, 3.1). El código del formato en el Sistema Integrado de Gestión va en la columna codigo. |  |
| 5 | `version` | `character varying(10)` | no | Versión de la plantilla. |  |
| 6 | `fecha_aprobacion` | `date` | sí | Fecha de aprobación de la plantilla. |  |
| 7 | `modalidades` | `jsonb` | no | Modalidades de contratación a las que aplica el formato, en formato JSON (lista). Una lista vacía significa que aplica a todas. |  |
| 8 | `archivo_url` | `text` | sí | URL del archivo de la plantilla. |  |
| 9 | `activo` | `boolean` | no | Indica si la plantilla está activa. |  |
| 10 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## plazo_publicacion_acta

Plazo para publicar el acta de liquidación, parametrizable y marcado si está sin confirmar (EFDS-1174).

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla plazo_publicacion_acta. | PK |
| 2 | `dias_habiles` | `integer` | no | Número de días hábiles del plazo para publicar el acta de liquidación. |  |
| 3 | `fundamento` | `text` | sí | Origen de la cifra del plazo para publicar el acta: norma o acta que la respalda. |  |
| 4 | `confirmado` | `boolean` | no | Indica si la Dirección de Contratación validó el plazo para publicar el acta; es falso mientras no se valide. |  |
| 5 | `actualizado_at` | `timestamp with time zone` | no | Fecha y hora de la actualización. |  |

## plazo_publicacion_contrato

Plazo para publicar el contrato, parametrizable y marcado si está sin confirmar (EFDS-1166).

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla plazo_publicacion_contrato. | PK |
| 2 | `dias_habiles` | `integer` | no | Número de días hábiles del plazo para publicar el contrato. |  |
| 3 | `fundamento` | `text` | sí | Origen de la cifra del plazo para publicar el contrato: norma o acta que la respalda. |  |
| 4 | `confirmado` | `boolean` | no | Indica si la Dirección de Contratación validó el plazo para publicar el contrato; es falso mientras no se valide, y un plazo sin confirmar se muestra con advertencia. |  |
| 5 | `actualizado_at` | `timestamp with time zone` | no | Fecha y hora de la actualización. |  |

## plazos_ofertas

Días hábiles de recepción de ofertas por modalidad, contados desde la apertura (EFDS-1155).

- Clave primaria: `modalidad`
- Filas: 7
- Referencia a: `modalidad` → `hiring.modalidades` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `modalidad` | `character varying(60)` | no | Clave primaria de la tabla plazos_ofertas: modalidad. | PK FK→hiring.modalidades.codigo |
| 2 | `dias_habiles` | `integer` | no | Número de días hábiles de recepción de ofertas para la modalidad. |  |
| 3 | `fundamento` | `text` | sí | Origen del número de días del plazo de recepción de ofertas: norma o acta que lo respalda. |  |
| 4 | `confirmado` | `boolean` | no | Indica si la Dirección de Contratación confirmó el plazo de recepción de ofertas; es falso mientras no se confirme, y los plazos se cargan sin confirmar. |  |
| 5 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 6 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## plazos_publicacion

Días hábiles de publicidad del proyecto de pliego, por modalidad. Parametrizables (EFDS-1150).

- Clave primaria: `modalidad`
- Filas: 7
- Referencia a: `modalidad` → `hiring.modalidades` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `modalidad` | `character varying(60)` | no | Clave primaria de la tabla plazos_publicacion: modalidad. | PK FK→hiring.modalidades.codigo |
| 2 | `dias_habiles` | `integer` | no | Número de días hábiles de publicidad del proyecto de pliego para la modalidad. |  |
| 3 | `fundamento` | `text` | sí | Origen del número de días del plazo de publicidad del proyecto de pliego (por ejemplo, el decreto o un supuesto del equipo). |  |
| 4 | `confirmado` | `boolean` | no | Indica si la Dirección de Contratación confirmó el plazo de publicidad del proyecto de pliego; es falso mientras no se confirme. |  |
| 5 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 6 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## plazos_traslado

Días hábiles de traslado del informe de evaluación por modalidad, contados desde su publicación (EFDS-1158).

- Clave primaria: `modalidad`
- Filas: 7
- Referencia a: `modalidad` → `hiring.modalidades` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `modalidad` | `character varying(60)` | no | Clave primaria de la tabla plazos_traslado: modalidad. | PK FK→hiring.modalidades.codigo |
| 2 | `dias_habiles` | `integer` | no | Número de días hábiles de traslado del informe de evaluación para la modalidad. |  |
| 3 | `fundamento` | `text` | sí | Texto libre que sustenta el plazo de traslado de la modalidad (norma o supuesto). La siembra inicial lo registra como «Supuesto del equipo, sin validar». |  |
| 4 | `confirmado` | `boolean` | no | Indica si la Dirección de Contratación confirmó el plazo de traslado del informe de evaluación; es falso mientras no se confirme, y los plazos se cargan sin confirmar (RF-PUB-08, EFDS-1467). |  |
| 5 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 6 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## proceso_actividades

_Por documentar._

- Clave primaria: `id`
- Filas: 590
- Referencia a: `proceso_id` → `hiring.procesos` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla proceso_actividades. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | FK→hiring.procesos.id |
| 3 | `numeral` | `character varying(20)` | no | Numeral de la actividad dentro del procedimiento de contratación. Es único por proceso. |  |
| 4 | `estado` | `character varying(30)` | no | Estado de la actividad del proceso: borrador, en revisión, aprobado, devuelto, negado o no aplica. |  |
| 5 | `datos` | `jsonb` | no | Valores del formulario diligenciado en la actividad, en formato JSON, con la estructura que define campos_formulario. |  |
| 6 | `version` | `integer` | no | Versión del registro para control de concurrencia optimista: se incrementa en cada guardado y, si la versión que envía el cliente no coincide, la operación se rechaza (409) en lugar de sobrescribir cambios. |  |
| 7 | `enviado_por` | `character varying(120)` | sí | Usuario que realizó el envío. |  |
| 8 | `enviado_at` | `timestamp with time zone` | sí | Fecha y hora del envío. |  |
| 9 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 10 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 11 | `revisado_por` | `character varying(120)` | sí | Usuario que realizó la revisión. |  |
| 12 | `revisado_at` | `timestamp with time zone` | sí | Fecha y hora de la revisión. |  |
| 13 | `documento_requerido` | `boolean` | no | Indica si la actividad del proceso requiere documento. |  |
| 14 | `enviado_por_id` | `character varying(120)` | sí | Id del usuario que envió a aprobación. Permite impedir que quien ejecutó la actividad se la apruebe. |  |

## procesos

_Por documentar._

- Clave primaria: `id`
- Filas: 10
- Referencia a: `causal` → `hiring.causales_contratacion` (0..1 → 0..1); `modalidad` → `hiring.modalidades` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla procesos. Se genera automáticamente. | PK |
| 2 | `radicado` | `character varying(60)` | no | Número de radicado del proceso de contratación. Es único. | única |
| 3 | `objeto` | `text` | no | Objeto del proceso de contratación. |  |
| 4 | `etapa` | `integer` | no | Número de la etapa del proceso en la matriz de flujo (1 a 10, el mismo de hiring.actividades.etapa); por defecto 3, Estudios Previos. Etapas: 4 CDP, 5 elaboración y publicación, 6 recepción y evaluación de ofertas, 7 adjudicación, 8 contrato y legalización, 9 ejecución y 10 seguimiento, control y liquidación. |  |
| 5 | `fecha_radicacion` | `timestamp with time zone` | no | Fecha y hora de radicación del proceso. |  |
| 6 | `created_by` | `character varying(120)` | sí | Usuario que creó el registro. |  |
| 7 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 9 | `modalidad` | `character varying(60)` | sí | Referencia al registro de hiring.modalidades (codigo). | FK→hiring.modalidades.codigo |
| 10 | `valor_estimado` | `numeric(18,2)` | sí | Valor estimado del contrato en pesos. Base para determinar la modalidad por cuantía (EFDS-1147). |  |
| 11 | `estado` | `character varying(20)` | no | Desenlace del proceso: en curso, adjudicado, desierto o negado en la revisión (EFDS-1183). |  |
| 12 | `causal` | `character varying(60)` | sí | Causal elegida en la 3.6 por el abogado que lleva el proceso. Nula en las nueve modalidades donde la matriz no marca la actividad. | FK→hiring.causales_contratacion.codigo |
| 13 | `causal_sustento` | `text` | sí | Por qué el objeto encaja en esa causal, en las palabras del abogado. Opcional: la causal es el dato, esto es la motivación que alimenta el acto de justificación. |  |
| 14 | `radicado_gestion_documental` | `character varying(120)` | sí | Consecutivo de Active Document con el que el área remitió el paquete a la Dirección de Contratación (actividad 3.3). Nulo cuando se remitió por una vía que no genera radicado. |  |

## publicaciones_acta

Publicaciones del acta de liquidación con su destino, evidencia y control de plazo (EFDS-1174).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `acta_id` → `hiring.actas_liquidacion` (0..1 → 1); `documento_id` → `hiring.documentos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla publicaciones_acta. Se genera automáticamente. | PK |
| 2 | `acta_id` | `uuid` | no | Referencia al registro de hiring.actas_liquidacion (id). | FK→hiring.actas_liquidacion.id |
| 3 | `destino` | `character varying(20)` | no | Medio donde se publica el acta de liquidación: SECOP_II o WEB_ESAP (página web de la ESAP). Se registra el sitio de cada publicación. |  |
| 4 | `fecha_publicacion` | `date` | no | Fecha real de publicación del acta de liquidación, no la de su registro en la plataforma; es la que cuenta para el plazo. |  |
| 5 | `plazo_dias_habiles` | `integer` | sí | Plazo en días hábiles vigente el día del registro, congelado: si después cambia el parámetro, la publicación conserva el plazo con que se juzgó. |  |
| 6 | `fecha_limite` | `date` | sí | Fecha límite para publicar el acta de liquidación. |  |
| 7 | `secop_numero` | `character varying(80)` | sí | Número con el que quedó publicada el acta de liquidación en SECOP II. Es opcional, también cuando el destino es SECOP_II. |  |
| 8 | `secop_url` | `text` | sí | URL de la publicación en SECOP II. |  |
| 9 | `documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 10 | `publicado_por` | `character varying(200)` | sí | Usuario que realizó la publicación. |  |
| 11 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## publicaciones_contrato

Publicaciones del contrato con su destino, evidencia y control de plazo (EFDS-1166).

- Clave primaria: `id`
- Filas: 1
- Referencia a: `contrato_id` → `hiring.contratos` (0..1 → 1); `documento_id` → `hiring.documentos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla publicaciones_contrato. Se genera automáticamente. | PK |
| 2 | `contrato_id` | `uuid` | no | Referencia al registro de hiring.contratos (id). | FK→hiring.contratos.id |
| 3 | `destino` | `character varying(20)` | no | Medio donde se publica el contrato: SECOP_II o WEB_ESAP (página web de la ESAP). |  |
| 4 | `fecha_publicacion` | `date` | no | Fecha real de publicación del contrato, no la de su registro en la plataforma; es la que cuenta para el plazo. |  |
| 5 | `plazo_dias_habiles` | `integer` | sí | Plazo en días hábiles vigente el día del registro, congelado: si después cambia el parámetro, la publicación conserva el plazo con que se juzgó. |  |
| 6 | `fecha_limite` | `date` | sí | Fecha límite para publicar el contrato. |  |
| 7 | `secop_numero` | `character varying(80)` | sí | Número del proceso en SECOP II asociado a la publicación del contrato. Es opcional, también cuando el destino es SECOP_II. |  |
| 8 | `secop_url` | `text` | sí | URL de la publicación en SECOP II. |  |
| 9 | `documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 10 | `publicado_por` | `character varying(200)` | sí | Usuario que realizó la publicación. |  |
| 11 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## publicaciones_modificacion

Publicación de la modificación en SECOP II, con su evidencia (EFDS-1176, RF-MOD-05).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `documento_id` → `hiring.documentos` (0..1 → 1); `modificacion_id` → `hiring.modificaciones_contrato` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla publicaciones_modificacion. Se genera automáticamente. | PK |
| 2 | `modificacion_id` | `uuid` | no | Referencia al registro de hiring.modificaciones_contrato (id). | única FK→hiring.modificaciones_contrato.id |
| 3 | `fecha_publicacion` | `date` | no | Fecha real de publicación de la modificación contractual en SECOP II, no la de su registro en la plataforma (RF-MOD-05). |  |
| 4 | `secop_numero` | `character varying(80)` | sí | Número con el que quedó publicada la modificación en SECOP II; opcional. |  |
| 5 | `secop_url` | `text` | sí | URL de la publicación de la modificación en SECOP II. |  |
| 6 | `documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 7 | `publicada_por` | `character varying(200)` | sí | Usuario que realizó la publicación. |  |
| 8 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## publicaciones_pliego

Registro de la publicación del proyecto de pliego en SECOP II y su plazo de publicidad (EFDS-1150).

- Clave primaria: `id`
- Filas: 3
- Referencia a: `proceso_id` → `hiring.procesos` (0..1 → 1)
- Relaciones implícitas: `documento_id` ↝ `hiring.documentos` (100.0 % con padre)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla publicaciones_pliego. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | FK→hiring.procesos.id |
| 3 | `fecha_publicacion` | `date` | no | Fecha real de publicación en SECOP II. Arranca el conteo del plazo legal. |  |
| 4 | `plazo_dias_habiles` | `integer` | sí | Plazo vigente el día del registro, congelado. Null si la modalidad no lo tiene parametrizado. |  |
| 5 | `fecha_vencimiento` | `date` | sí | Fecha de vencimiento del plazo de publicidad del proyecto de pliego. |  |
| 6 | `secop_numero` | `character varying(60)` | sí | Número del proceso en SECOP II asociado a la publicación del proyecto de pliego; se digita a mano porque no hay integración con SECOP II. |  |
| 7 | `secop_url` | `text` | sí | URL de la publicación del proyecto de pliego en SECOP II; permite verificar la publicación desde el expediente. |  |
| 8 | `documento_id` | `uuid` | no | Referencia al documento que evidencia la publicación del pliego (hiring.documentos.id); relación sin llave foránea declarada. Es obligatoria: no se admite una publicación sin evidencia. | ↝hiring.documentos.id |
| 9 | `publicado_por` | `character varying(160)` | sí | Usuario que realizó la publicación. |  |
| 10 | `anulada_at` | `timestamp with time zone` | sí | Fecha y hora en que se anuló la publicación. Una publicación con datos errados no se borra: se anula y se registra la correcta, y cada una conserva su evidencia. |  |
| 11 | `anulada_por` | `character varying(160)` | sí | Usuario que realizó la anulación. |  |
| 12 | `motivo_anulacion` | `text` | sí | Motivo de la anulación. |  |
| 13 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 14 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## recepciones_ofertas

Plazo de recepción de ofertas de cada proceso y su cierre (EFDS-1155).

- Clave primaria: `id`
- Filas: 3
- Referencia a: `proceso_id` → `hiring.procesos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla recepciones_ofertas. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | única FK→hiring.procesos.id |
| 3 | `vencimiento` | `timestamp with time zone` | no | Fecha y hora hasta la que se reciben ofertas. Se fija en la apertura del proceso. |  |
| 4 | `plazo_dias_habiles` | `integer` | sí | Plazo en días hábiles aplicado a la recepción de ofertas, congelado al fijarse. Nulo cuando la modalidad no tiene plazo parametrizado y el vencimiento se fijó a mano en la apertura. |  |
| 5 | `estado` | `character varying(20)` | no | Estado de la recepción de ofertas: abierta o cerrada. |  |
| 6 | `cerrada_at` | `timestamp with time zone` | sí | Fecha y hora de cierre de la recepción de ofertas; es la fecha con la que se publica la lista de oferentes. |  |
| 7 | `cerrada_por` | `character varying(200)` | sí | Usuario que realizó el cierre. |  |
| 8 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## registros_actividad

Constancia de que una actividad sin historia propia ocurrió, con su fecha, su nota y su soporte.

- Clave primaria: `id`
- Filas: 2
- Referencia a: `documento_id` → `hiring.documentos` (0..1 → 0..1); `numeral` → `hiring.actividades_con_soporte` (0..1 → 1); `proceso_id` → `hiring.procesos` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla registros_actividad. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | FK→hiring.procesos.id |
| 3 | `numeral` | `character varying(20)` | no | Referencia al registro de hiring.actividades_con_soporte (numeral). | FK→hiring.actividades_con_soporte.numeral |
| 4 | `fecha` | `date` | no | Cuándo ocurrió el hecho, no cuándo se transcribió. |  |
| 5 | `nota` | `text` | no | Nota que describe la actividad registrada. |  |
| 6 | `documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 7 | `datos` | `jsonb` | no | Datos propios de cada actividad registrada, en formato JSON libre (por ejemplo, el resultado sí/no del sorteo o el radicado de la actividad 3.3); si la actividad exige firma, incluye la clave firma. No tiene esquema fijo por numeral. |  |
| 8 | `estado` | `character varying(20)` | no | Estado del registro de la actividad: vigente o anulado. |  |
| 9 | `registrado_por` | `character varying(200)` | sí | Usuario que realizó el registro. |  |
| 10 | `registrado_at` | `timestamp with time zone` | no | Fecha y hora del registro. |  |
| 11 | `anulado_at` | `timestamp with time zone` | sí | Fecha y hora de la anulación. |  |
| 12 | `anulado_por` | `character varying(200)` | sí | Usuario que realizó la anulación. |  |
| 13 | `motivo_anulacion` | `text` | sí | Motivo de la anulación. |  |

## registros_presupuestales

Registros presupuestales que comprometen los recursos del contrato (EFDS-1163).

- Clave primaria: `id`
- Filas: 1
- Referencia a: `contrato_id` → `hiring.contratos` (0..1 → 1); `documento_id` → `hiring.documentos` (0..1 → 0..1); `modificacion_id` → `hiring.modificaciones_contrato` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla registros_presupuestales. Se genera automáticamente. | PK |
| 2 | `contrato_id` | `uuid` | no | Referencia al registro de hiring.contratos (id). | FK→hiring.contratos.id |
| 3 | `numero` | `character varying(60)` | sí | Número del registro presupuestal, que asigna la Dirección Financiera al expedirlo; es nulo mientras el registro está solicitado. |  |
| 4 | `valor` | `numeric(18,2)` | sí | Valor comprometido en el registro presupuestal, en pesos; al solicitar se toma el del contrato si no se indica y se compara con él. Mayor que cero y obligatorio cuando el estado es EXPEDIDO. |  |
| 5 | `rubro` | `character varying(160)` | sí | _Por documentar_ |  |
| 6 | `fecha_expedicion` | `date` | sí | Fecha de expedición del registro presupuestal. |  |
| 7 | `vigencia_fiscal` | `integer` | sí | Año de la vigencia fiscal a la que se imputa el registro presupuestal. Un registro presupuestal no cruza vigencias. |  |
| 8 | `estado` | `character varying(20)` | no | Estado del registro presupuestal. Flujo: SOLICITADO → VERIFICADO → EXPEDIDO; RECHAZADO cuando no hay disponibilidad para comprometer; ANULADO cuando se deja sin efecto después de expedido. |  |
| 9 | `observaciones` | `text` | sí | Motivo por el que la Dirección Financiera rechazó el registro presupuestal. |  |
| 10 | `documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 11 | `solicitado_por` | `character varying(200)` | sí | Usuario que realizó la solicitud. |  |
| 12 | `solicitado_at` | `timestamp with time zone` | no | Fecha y hora de la solicitud. |  |
| 13 | `expedido_por` | `character varying(200)` | sí | Nombre de usuario (username) de la cuenta autenticada que expidió el registro presupuestal; si el token no lo trae, se guarda el correo o el identificador. |  |
| 14 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 15 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 16 | `modificacion_id` | `uuid` | sí | La adición que este RP compromete; nulo si es el RP del contrato (EFDS-1176). | FK→hiring.modificaciones_contrato.id |

## reglas_actividad

_Por documentar._

- Clave primaria: `id`
- Filas: 13
- Referencia a: `modalidad` → `hiring.modalidades` (0..1 → 0..1); `numeral` → `hiring.actividades` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla reglas_actividad. Se genera automáticamente. | PK |
| 2 | `numeral` | `character varying(10)` | no | Referencia al registro de hiring.actividades (numeral). | FK→hiring.actividades.numeral |
| 3 | `modalidad` | `character varying(60)` | sí | Referencia al registro de hiring.modalidades (codigo). | FK→hiring.modalidades.codigo |
| 4 | `tipo` | `character varying(30)` | no | Tipo de regla de la actividad. |  |
| 5 | `config` | `jsonb` | no | Detalle de la condición de la regla según su tipo, en formato JSON (un umbral lleva max, un plazo lleva dias y un campo obligatorio lleva codigo). Es la forma original de las reglas; condiciones y acciones, agregadas después, expresan reglas condicionales del formulario reactivo. |  |
| 6 | `mensaje` | `text` | sí | Mensaje que ve el gestor cuando la regla no se cumple. Lo redacta la Dirección de Contratación. |  |
| 7 | `orden` | `integer` | no | Orden en que se evalúan las reglas y se muestran sus incumplimientos. |  |
| 8 | `vigente_desde` | `timestamp with time zone` | no | Fecha y hora desde la cual la regla está vigente; por defecto, la fecha de creación. Permite auditar cada proceso con las reglas vigentes al momento de su aprobación. |  |
| 9 | `vigente_hasta` | `timestamp with time zone` | sí | Fecha y hora hasta la cual la regla está vigente; vacía si sigue vigente y posterior a vigente_desde. Una regla derogada se cierra con esta fecha en lugar de borrarse. |  |
| 10 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 11 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 12 | `condiciones` | `jsonb` | no | Cuando aplica: [{campo, operador, valor}]. Vacio = siempre. |  |
| 13 | `acciones` | `jsonb` | no | Que hace: [{accion, objetivo, valor}]. accion es EXIGIR_CAMPO, MOSTRAR_CAMPO, OCULTAR_CAMPO, EXIGIR_DOCUMENTO, BLOQUEAR_AVANCE. |  |
| 14 | `conector` | `character varying(3)` | no | Operador lógico con que se combinan entre sí las condiciones de la regla: AND u OR. Por defecto, AND. |  |

## resoluciones_sancionatorias

Actos administrativos del trámite sancionatorio (EFDS-1181, RF-INC-02): el que lo abre y el que lo decide, incluida la caducidad.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `caso_id` → `hiring.casos_incumplimiento` (0..1 → 1); `documento_id` → `hiring.documentos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla resoluciones_sancionatorias. Se genera automáticamente. | PK |
| 2 | `caso_id` | `uuid` | no | Referencia al registro de hiring.casos_incumplimiento (id). | FK→hiring.casos_incumplimiento.id |
| 3 | `tipo` | `character varying(20)` | no | Tipo de resolución sancionatoria: de apertura o de decisión. |  |
| 4 | `numero` | `character varying(80)` | no | Número de la resolución sancionatoria. |  |
| 5 | `fecha_expedicion` | `date` | no | Fecha de expedición de la resolución sancionatoria. |  |
| 6 | `documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 7 | `sentido` | `character varying(30)` | sí | DECLARA_CADUCIDAD termina el contrato: es la caducidad como causal contractual que pide el bloque de Presunto Incumplimiento. |  |
| 8 | `valor_sancion` | `numeric(18,2)` | sí | _Por documentar_ |  |
| 9 | `estado_contrato_antes` | `character varying(20)` | sí | Estado que tenía el contrato (EJECUCION o SUSPENDIDO) antes de la declaratoria de caducidad, única decisión que lo termina; al revocar la resolución el contrato vuelve a ese estado. |  |
| 10 | `notificada_el` | `date` | sí | Fecha de notificación de la resolución, posterior a su expedición. Se registra; no se usa para calcular términos. |  |
| 11 | `firme_el` | `date` | sí | Fecha en que la resolución quedó en firme. Requiere fecha de notificación y no puede ser anterior a ella. |  |
| 12 | `expedida_por` | `character varying(200)` | sí | Nombre de usuario (username) de la cuenta autenticada que registró la resolución; si el token no lo trae, se guarda el correo o el identificador. |  |
| 13 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 14 | `revocada_at` | `timestamp with time zone` | sí | Fecha y hora de la revocación. |  |
| 15 | `revocada_por` | `character varying(200)` | sí | Usuario que realizó la revocación. |  |
| 16 | `motivo_revocacion` | `text` | sí | Motivo de la revocación. |  |

## resultados_evaluacion

Resultado de la evaluación hecha por el comité fuera de la plataforma: oferta ganadora, su valoración y el informe que la sustenta (EFDS-1157).

- Clave primaria: `id`
- Filas: 2
- Referencia a: `informe_documento_id` → `hiring.documentos` (0..1 → 1); `oferente_id` → `hiring.oferentes` (0..1 → 1); `proceso_id` → `hiring.procesos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla resultados_evaluacion. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | FK→hiring.procesos.id |
| 3 | `oferente_id` | `uuid` | no | Referencia al registro de hiring.oferentes (id). | FK→hiring.oferentes.id |
| 4 | `informe_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 5 | `puntaje_obtenido` | `numeric(6,2)` | sí | Puntaje obtenido por la oferta ganadora, tal como lo reporta el comité evaluador. Se registra junto con puntaje_maximo, no puede ser negativo y es nulo cuando la modalidad no asigna puntaje (por ejemplo, mínima cuantía). |  |
| 6 | `puntaje_maximo` | `numeric(6,2)` | sí | Puntaje máximo posible en la evaluación. Se registra junto con puntaje_obtenido y debe ser mayor que cero. |  |
| 7 | `valor_evaluado` | `numeric(18,2)` | sí | _Por documentar_ |  |
| 8 | `justificacion` | `text` | no | Justificación del comité evaluador para elegir la oferta ganadora; se muestra a los demás oferentes en el traslado del informe (actividad 6.4). |  |
| 9 | `estado` | `character varying(20)` | no | Estado del resultado de la evaluación: vigente o rectificado. |  |
| 10 | `registrado_por` | `character varying(200)` | sí | Usuario que realizó el registro. |  |
| 11 | `registrado_at` | `timestamp with time zone` | no | Fecha y hora del registro. |  |
| 12 | `rectificado_at` | `timestamp with time zone` | sí | Fecha y hora en que se rectificó el resultado de la evaluación. Un CHECK la relaciona con el estado RECTIFICADO. |  |
| 13 | `rectificado_por` | `character varying(200)` | sí | Nombre de usuario (username) de la cuenta autenticada que rectificó el resultado; si el token no lo trae, se guarda el correo o el identificador. |  |
| 14 | `motivo_rectificacion` | `text` | sí | Motivo de la rectificación. |  |
| 15 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 16 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## revisiones

_Por documentar._

- Clave primaria: `id`
- Filas: 12
- Referencia a: `proceso_actividad_id` → `hiring.proceso_actividades` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla revisiones. Se genera automáticamente. | PK |
| 2 | `proceso_actividad_id` | `uuid` | no | Referencia al registro de hiring.proceso_actividades (id). | FK→hiring.proceso_actividades.id |
| 3 | `decision` | `character varying(20)` | no | Decisión de la revisión de la actividad. Valores permitidos: APROBADO, DEVUELTO, NEGADO. |  |
| 4 | `observaciones` | `text` | sí | Motivo de la decisión del revisor sobre la actividad. Obligatorio salvo cuando se aprueba. |  |
| 5 | `version_revisada` | `integer` | no | Número de versión de la actividad sobre la que se pronunció el revisor, aunque el gestor la haya corregido después. |  |
| 6 | `revisado_por` | `character varying(120)` | no | Usuario que realizó la revisión. |  |
| 7 | `revisado_por_id` | `character varying(120)` | sí | Identificador del usuario que hizo la revisión: el id_user de auth."user", tomado del token de sesión (sin llave foránea). |  |
| 8 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `soportes_documento_ids` | `uuid[]` | no | Archivos que acompañan una devolución, en el orden en que se adjuntaron: las correcciones marcadas sobre los documentos. Solo los adjunta quien devolvió. |  |

## roles_del_modulo

Roles que trabajan en contratación: los que tienen al menos un permiso del módulo. Alimenta el selector de aprobadores.

- Clave primaria: no declarada
- Filas: —
- Vista que usa: `auth.module`, `auth.permission`, `auth.role`, `auth.role_permissions`

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `code` | `character varying(50)` | sí | _Por documentar_ |  |
| 2 | `name` | `character varying(100)` | sí | _Por documentar_ |  |
| 3 | `type` | `character varying(20)` | sí | _Por documentar_ |  |

## seguimientos_contrato

Informes, actas y soportes de la ejecución del contrato (EFDS-1168, actividad 9.2).

- Clave primaria: `id`
- Filas: 1
- Referencia a: `contrato_id` → `hiring.contratos` (0..1 → 1); `documento_id` → `hiring.documentos` (0..1 → 1); `supervision_id` → `hiring.supervisiones_contrato` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla seguimientos_contrato. Se genera automáticamente. | PK |
| 2 | `contrato_id` | `uuid` | no | Referencia al registro de hiring.contratos (id). | FK→hiring.contratos.id |
| 3 | `tipo` | `character varying(20)` | no | Clase de soporte del seguimiento a la ejecución: INFORME, ACTA o SOPORTE (otros documentos, como certificaciones o comunicaciones). |  |
| 4 | `descripcion` | `text` | no | Descripción de lo que acredita el soporte del seguimiento. Es obligatoria. |  |
| 5 | `periodo_desde` | `date` | sí | Fecha de inicio del periodo de la ejecución que cubre el soporte. Se registra junto con periodo_hasta, no puede ser posterior a ella y es nula cuando el soporte corresponde a un hecho puntual. |  |
| 6 | `periodo_hasta` | `date` | sí | Fecha de fin del periodo que cubre el seguimiento. Se registra junto con periodo_desde. |  |
| 7 | `fecha_soporte` | `date` | no | Fecha del soporte, no la de su registro en la plataforma (un informe de enero cargado en febrero conserva la fecha de enero). |  |
| 8 | `documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 9 | `registrado_por` | `character varying(200)` | sí | Nombre de usuario (username) de la cuenta autenticada que cargó el soporte del seguimiento; si el token no lo trae, se guarda el correo o el identificador. La calidad en que actuó se guarda en supervision_id, la supervisión vigente ese día. |  |
| 10 | `supervision_id` | `uuid` | sí | Referencia al registro de hiring.supervisiones_contrato (id). | FK→hiring.supervisiones_contrato.id |
| 11 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## sesiones_comite_contratacion

Sesiones del comité de contratación sobre un proceso (actividad 3.7). Una por sesión: observar devuelve el proceso al comité, y las dos quedan.

- Clave primaria: `id`
- Filas: 4
- Referencia a: `acta_documento_id` → `hiring.documentos` (0..1 → 0..1); `proceso_id` → `hiring.procesos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla sesiones_comite_contratacion. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | FK→hiring.procesos.id |
| 3 | `fecha` | `date` | no | Fecha de la sesión del comité de contratación, no la de su registro en la plataforma. |  |
| 4 | `decision` | `character varying(30)` | no | Decisión del comité en la sesión. Valores permitidos: APROBADO, APROBADO_CON_CONDICIONES, OBSERVADO, RECHAZADO. |  |
| 5 | `condiciones` | `text` | sí | Condiciones a las que queda sujeta la aprobación condicionada del comité. Un CHECK la relaciona con la decisión APROBADO_CON_CONDICIONES. |  |
| 6 | `observaciones` | `text` | sí | Lo que el comité objetó: obligatorio al observar y al rechazar, y también cuando aprueba pero reabre alguna actividad para que se la validen. |  |
| 7 | `acta_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 8 | `registrado_por` | `character varying(120)` | sí | Usuario que realizó el registro. |  |
| 9 | `registrado_por_id` | `character varying(120)` | sí | Identificador del usuario que registró la sesión: el id_user de auth."user", tomado del token de sesión (sin llave foránea). |  |
| 10 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## smmlv

Salario mínimo mensual legal vigente por año. Base de los umbrales expresados en SMMLV (EFDS-1147).

- Clave primaria: `anio`
- Filas: 2

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `anio` | `integer` | no | Clave primaria de la tabla smmlv: año. | PK |
| 2 | `valor` | `numeric(18,2)` | no | Valor del salario mínimo mensual legal vigente del año, en pesos colombianos. Debe ser mayor que cero. |  |
| 3 | `confirmado` | `boolean` | no | Indica si el valor del salario mínimo está verificado; mientras sea falso, el valor es un supuesto del equipo de desarrollo. |  |
| 4 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 5 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## sobres_economicos

Apertura del sobre económico en la audiencia de adjudicación, donde la modalidad lo exige (EFDS-1159).

- Clave primaria: `id`
- Filas: 1
- Referencia a: `audiencia_id` → `hiring.audiencias_adjudicacion` (0..1 → 1); `evidencia_documento_id` → `hiring.documentos` (0..1 → 0..1); `oferente_id` → `hiring.oferentes` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla sobres_economicos. Se genera automáticamente. | PK |
| 2 | `audiencia_id` | `uuid` | no | Referencia al registro de hiring.audiencias_adjudicacion (id). | FK→hiring.audiencias_adjudicacion.id |
| 3 | `oferente_id` | `uuid` | no | Referencia al registro de hiring.oferentes (id). | FK→hiring.oferentes.id |
| 4 | `valor_ofertado` | `numeric(18,2)` | no | _Por documentar_ |  |
| 5 | `evidencia_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 6 | `observacion` | `text` | sí | Observación sobre la apertura del sobre económico. |  |
| 7 | `abierto_por` | `character varying(200)` | sí | Nombre de usuario (username) de la cuenta autenticada que registró la apertura del sobre económico en la audiencia; si el token no lo trae, se guarda el correo o el identificador. |  |
| 8 | `abierto_at` | `timestamp with time zone` | no | Fecha y hora de apertura del sobre económico. Por defecto, la fecha del registro. |  |
| 9 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## soportes_pago

Documentos que acompañan la cuenta de cobro. Se cargan a mano mientras no exista la integración con Click (EFDS-1170).

- Clave primaria: `id`
- Filas: 4
- Referencia a: `documento_id` → `hiring.documentos` (0..1 → 1); `pago_id` → `hiring.pagos_contrato` (1..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla soportes_pago. Se genera automáticamente. | PK |
| 2 | `pago_id` | `uuid` | no | Referencia al registro de hiring.pagos_contrato (id). | FK→hiring.pagos_contrato.id |
| 3 | `documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 4 | `tipo` | `character varying(30)` | no | Tipo de documento que acompaña la cuenta de cobro: SEGURIDAD_SOCIAL, RUT, CERTIFICACION_BANCARIA u OTRO. |  |
| 5 | `descripcion` | `character varying(300)` | sí | Descripción del soporte de la cuenta de cobro. |  |
| 6 | `cargado_por` | `character varying(200)` | sí | Usuario que realizó la carga. |  |
| 7 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## subsanaciones

Subsanaciones y observaciones que presentan los oferentes durante el traslado del informe (EFDS-1158).

- Clave primaria: `id`
- Filas: 1
- Referencia a: `informe_id` → `hiring.informes_evaluacion` (0..1 → 1); `oferente_id` → `hiring.oferentes` (0..1 → 1); `respuesta_documento_id` → `hiring.documentos` (0..1 → 0..1); `soporte_documento_id` → `hiring.documentos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla subsanaciones. Se genera automáticamente. | PK |
| 2 | `informe_id` | `uuid` | no | Referencia al registro de hiring.informes_evaluacion (id). | FK→hiring.informes_evaluacion.id |
| 3 | `oferente_id` | `uuid` | no | Referencia al registro de hiring.oferentes (id). | FK→hiring.oferentes.id |
| 4 | `tipo` | `character varying(20)` | no | Tipo de lo presentado por el oferente durante el traslado del informe: SUBSANACION (aporta lo que faltaba y puede cambiar la habilitación) u OBSERVACION (cuestiona la evaluación, propia o de otro oferente). |  |
| 5 | `presentado_por` | `character varying(200)` | no | Nombre de quien presenta la subsanación u observación. |  |
| 6 | `identificacion` | `character varying(60)` | sí | Número de identificación de quien presenta la subsanación. |  |
| 7 | `fecha_presentacion` | `date` | no | Fecha en que el oferente presentó la subsanación u observación, no la de su registro; determina si llegó en término. |  |
| 8 | `extemporanea` | `boolean` | no | Indica si la subsanación u observación se presentó fuera de término. Se calcula al registrar y queda fija. No implica rechazo: la entidad decide si la acepta. |  |
| 9 | `asunto` | `character varying(300)` | no | Asunto de la subsanación u observación. |  |
| 10 | `contenido` | `text` | no | Texto de la subsanación u observación presentada por el oferente. |  |
| 11 | `soporte_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 12 | `respuesta` | `text` | sí | Respuesta de la entidad a la subsanación u observación del oferente. Es obligatoria cuando se registra la decisión (aceptada) y la fecha de respuesta, y no se reescribe una vez cerrado el traslado, porque queda notificada. |  |
| 13 | `respuesta_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 14 | `aceptada` | `boolean` | sí | Decisión de la entidad sobre lo presentado: nulo mientras no se responde; verdadero si se aceptó, caso en que el comité puede corregir su evaluación con lo aportado. |  |
| 15 | `respondida_por` | `character varying(120)` | sí | Nombre de usuario (username) de la cuenta autenticada que registró la respuesta; si el token no lo trae, se guarda el correo o el identificador. |  |
| 16 | `respondida_at` | `timestamp with time zone` | sí | Fecha y hora de la respuesta. Se registra junto con aceptada. |  |
| 17 | `registrado_por` | `character varying(120)` | sí | Usuario que realizó el registro. |  |
| 18 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 19 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## supervisiones_contrato

Supervisores designados por acto administrativo, vigentes y relevados (EFDS-1165).

- Clave primaria: `id`
- Filas: 1
- Referencia a: `acto_documento_id` → `hiring.documentos` (0..1 → 1); `contrato_id` → `hiring.contratos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla supervisiones_contrato. Se genera automáticamente. | PK |
| 2 | `contrato_id` | `uuid` | no | Referencia al registro de hiring.contratos (id). | FK→hiring.contratos.id |
| 3 | `acto_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 4 | `fecha_designacion` | `date` | no | Fecha del acto administrativo de designación del supervisor, no la de su registro. |  |
| 5 | `persona_id` | `uuid` | no | Identificador de la persona designada como supervisora (id_person de auth.personas). Sin llave foránea declarada, por tratarse de un esquema de otro equipo. |  |
| 6 | `nombre` | `character varying(200)` | no | Nombre del supervisor, copiado al momento de la designación; conserva el nombre que registró el acto aunque luego cambie en el directorio. |  |
| 7 | `cargo` | `character varying(200)` | sí | Cargo del supervisor designado. |  |
| 8 | `email` | `character varying(200)` | sí | Correo electrónico del supervisor del contrato. | Contacto |
| 9 | `designado_por` | `character varying(200)` | sí | Nombre de usuario (username) de la cuenta autenticada que registró la designación del supervisor (no el ordenador del gasto); si el token no lo trae, se guarda el correo o el identificador. |  |
| 10 | `estado` | `character varying(20)` | no | Estado de la supervisión del contrato: vigente o relevado. |  |
| 11 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 12 | `alerta_enviada_at` | `timestamp with time zone` | sí | Fecha y hora en que se avisó al supervisor de su designación (matriz, actividad 8.2). Es nula mientras el aviso esté pendiente; a la fecha del código el módulo no envía correos. |  |
| 13 | `relevado_at` | `timestamp with time zone` | sí | Fecha y hora en que el supervisor fue relevado. Un CHECK la relaciona con el estado RELEVADO. |  |
| 14 | `relevado_por` | `character varying(200)` | sí | Nombre de usuario (username) de la cuenta autenticada que registró el relevo del supervisor; si el token no lo trae, se guarda el correo o el identificador. |  |
| 15 | `motivo_relevo` | `text` | sí | Motivo del relevo. |  |

## suscripciones_acta_inicio

Acta de inicio suscrita por la entidad y el contratista (actividad 8.7). La reunión (9.1) va en actas_inicio.

- Clave primaria: `id`
- Filas: 1
- Referencia a: `acta_documento_id` → `hiring.documentos` (0..1 → 1); `contrato_id` → `hiring.contratos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla suscripciones_acta_inicio. Se genera automáticamente. | PK |
| 2 | `contrato_id` | `uuid` | no | Referencia al registro de hiring.contratos (id). | FK→hiring.contratos.id |
| 3 | `fecha_suscripcion` | `date` | no | Fecha en que las dos partes firmaron el acta de inicio, no la fecha en que se cargó. |  |
| 4 | `acta_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 5 | `registrado_por` | `character varying(200)` | sí | Usuario que realizó el registro. |  |
| 6 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## tipologias_contrato

Tipologías de contrato y el formato del SIG que sirve de minuta (EFDS-1161).

- Clave primaria: `codigo`
- Filas: 12

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `codigo` | `character varying(60)` | no | Clave primaria de la tabla tipologias_contrato: código. | PK |
| 2 | `nombre` | `character varying(200)` | no | Nombre de la tipología de contrato. |  |
| 3 | `descripcion` | `text` | sí | Descripción de la tipología de contrato. |  |
| 4 | `numeral_formato` | `character varying(20)` | no | Numeral de la matriz cuyo formato del SIG sirve de minuta para la tipología de contrato; por defecto, 8.1. Remite a la biblioteca de formatos (hiring.plantillas) sin llave foránea declarada, porque el formato puede no estar cargado aún. |  |
| 5 | `exige_garantias` | `boolean` | no | Indica si la tipología de contrato exige garantías; lo usa la legalización del contrato (EFDS-1164). |  |
| 6 | `activo` | `boolean` | no | Indica si la tipología de contrato está activa. |  |
| 7 | `orden` | `integer` | no | Posición de la tipología de contrato en el orden de presentación. |  |

## tipos_amparo

Coberturas que puede incluir una garantía, para controlar sus vencimientos (EFDS-1164).

- Clave primaria: `codigo`
- Filas: 7

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `codigo` | `character varying(60)` | no | Clave primaria de la tabla tipos_amparo: código. | PK |
| 2 | `nombre` | `character varying(200)` | no | Nombre del tipo de amparo. |  |
| 3 | `descripcion` | `text` | sí | Descripción del tipo de amparo. |  |
| 4 | `activo` | `boolean` | no | Indica si el tipo de amparo está activo. |  |
| 5 | `orden` | `integer` | no | Posición del tipo de amparo en el orden de presentación. |  |

## tope_adicion

Tope legal de la adición como porcentaje del valor inicial del contrato (EFDS-1176).

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla tope_adicion. | PK |
| 2 | `porcentaje` | `numeric(5,2)` | no | Porcentaje máximo de adición sobre el valor inicial del contrato. Mayor que 0 y hasta 100. |  |
| 3 | `fundamento` | `text` | sí | Texto que sustenta el tope de adición: la norma y su alcance. La siembra cita la Ley 80 de 1993, art. 40, parágrafo (50 % del valor inicial). |  |
| 4 | `confirmado` | `boolean` | no | Indica si la Dirección de Contratación ratificó la cifra del tope legal de la adición; es falso mientras no se ratifique. |  |
| 5 | `actualizado_at` | `timestamp with time zone` | no | Fecha y hora de la actualización. |  |

## trazabilidad

_Por documentar._

- Clave primaria: `id`
- Filas: 236
- Referencia a: `proceso_id` → `hiring.procesos` (1..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | Identificador único del registro en la tabla trazabilidad. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | sí | Referencia al registro de hiring.procesos (id). | FK→hiring.procesos.id |
| 3 | `entidad` | `character varying(80)` | no | Nombre funcional, en singular y snake_case, del objeto afectado por la acción (por ejemplo, modificacion_contrato, pago_contrato, cdp); no coincide siempre con el nombre de la tabla. |  |
| 4 | `entidad_id` | `uuid` | sí | Identificador del registro afectado por la acción. |  |
| 5 | `accion` | `character varying(60)` | no | Acción realizada sobre el registro, de una lista definida en el código (CREAR, GUARDAR, ENVIAR, ADJUNTAR, APROBAR, DEVOLVER, SOLICITAR, VERIFICAR, EXPEDIR, RECHAZAR, PUBLICAR, ANULAR, DESIGNAR, REVOCAR, ADJUDICAR, INICIAR, ARCHIVAR, CONSULTAR, entre otras). La columna no tiene CHECK. |  |
| 6 | `detalle` | `jsonb` | sí | Detalle de la acción en formato JSON, sin estructura fija: cada módulo guarda los datos propios del hecho (por ejemplo, la actividad, el contrato, el tipo y los valores antes y después de una adición). |  |
| 7 | `usuario_id` | `character varying(120)` | sí | Identificador del usuario que hizo la acción: el id_user de auth."user", tomado del token de sesión (sin llave foránea). El nombre va en usuario_nombre. |  |
| 8 | `usuario_nombre` | `character varying(200)` | sí | Nombre del usuario que hizo la acción. |  |
| 9 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## umbrales_comite_contratacion

Condición de cuantía para pasar por el comité de contratación (actividad 3.7). La modalidad sin fila va a comité siempre que la matriz la marque.

- Clave primaria: `modalidad`
- Filas: 1
- Referencia a: `modalidad` → `hiring.modalidades` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `modalidad` | `character varying(60)` | no | Clave primaria de la tabla umbrales_comite_contratacion: modalidad. | PK FK→hiring.modalidades.codigo |
| 2 | `valor` | `numeric(18,2)` | no | Cuantía por encima de la cual el proceso pasa por el comité de contratación, expresada en la unidad indicada (SMMLV o PESOS); un valor igual al umbral no pasa. Debe ser mayor que cero. |  |
| 3 | `unidad` | `character varying(10)` | no | Unidad en que se expresa el valor del umbral: SMMLV o PESOS. Por defecto, SMMLV, para que el umbral siga el salario mínimo de cada año. |  |
| 4 | `fundamento` | `text` | sí | Origen de la cifra del umbral, para leerlo junto al valor al validarlo. |  |
| 5 | `confirmado` | `boolean` | no | Indica si la Dirección de Contratación confirmó la cifra del umbral; es falso mientras no se confirme. |  |
| 6 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 7 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## umbrales_modalidad

Rangos de cuantía que sugieren cada modalidad. Parametrizables por administrador (EFDS-1147).

- Clave primaria: `id`
- Filas: 3
- Referencia a: `modalidad` → `hiring.modalidades` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla umbrales_modalidad. Se genera automáticamente. | PK |
| 2 | `modalidad` | `character varying(60)` | no | Referencia al registro de hiring.modalidades (codigo). | FK→hiring.modalidades.codigo |
| 3 | `limite_inferior` | `numeric(18,2)` | sí | Límite inferior del rango de cuantía de la modalidad, en la unidad indicada. El intervalo es semiabierto [inferior, superior): el límite inferior está incluido y el superior pertenece al tramo siguiente. Nulo significa sin piso; debe registrarse al menos uno de los dos límites. |  |
| 4 | `limite_superior` | `numeric(18,2)` | sí | Límite superior, exclusivo, del rango de cuantía de la modalidad en la unidad indicada: el valor exacto pertenece al tramo siguiente. Vacío si el rango no tiene tope. |  |
| 5 | `unidad` | `character varying(10)` | no | Unidad en que se expresan los límites: SMMLV para lo que la ley define en salarios (Ley 1150 de 2007) o PESOS para topes que la entidad fije en cifra cerrada. Por defecto, SMMLV. |  |
| 6 | `vigencia_desde` | `date` | no | Fecha desde la cual rige el umbral; por defecto, la fecha del registro. Los umbrales no se editan: se cierra el vigente y se abre otro. |  |
| 7 | `vigencia_hasta` | `date` | sí | Fecha hasta la cual rige el umbral. Nula mientras esté vigente; no puede ser anterior a vigencia_desde. |  |
| 8 | `confirmado` | `boolean` | no | Indica si la Dirección de Contratación confirmó la cifra del umbral; es falso mientras no se confirme. |  |
| 9 | `created_by` | `character varying(160)` | sí | Usuario que creó el registro. |  |
| 10 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 11 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
