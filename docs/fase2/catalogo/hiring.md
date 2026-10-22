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
| 3 | `fecha_inicio` | `date` | no | _Por documentar_ |  |
| 4 | `temas_tratados` | `text` | no | _Por documentar_ |  |
| 5 | `asistentes` | `text` | sí | _Por documentar_ |  |
| 6 | `acta_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 7 | `acta_pactada` | `boolean` | no | _Por documentar_ |  |
| 8 | `registrado_por` | `character varying(200)` | sí | _Por documentar_ |  |
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
| 3 | `tipo` | `character varying(20)` | no | _Por documentar_ |  |
| 4 | `acta_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 5 | `fecha_acta` | `date` | no | _Por documentar_ |  |
| 6 | `balance` | `jsonb` | no | _Por documentar_ |  |
| 7 | `paz_y_salvo` | `boolean` | no | _Por documentar_ |  |
| 8 | `paz_y_salvo_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 9 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 10 | `fecha_terminacion` | `date` | sí | _Por documentar_ |  |
| 11 | `bilateral_hasta` | `date` | sí | _Por documentar_ |  |
| 12 | `unilateral_hasta` | `date` | sí | _Por documentar_ |  |
| 13 | `momento_del_plazo` | `character varying(20)` | sí | _Por documentar_ |  |
| 14 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 15 | `liquidado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 16 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 17 | `anulado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 18 | `anulado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 19 | `motivo_anulacion` | `text` | sí | _Por documentar_ |  |

## actividades

Catálogo de actividades de la matriz de flujo, por etapa y numeral.

- Clave primaria: `numeral`
- Filas: 63

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `numeral` | `character varying(20)` | no | Clave primaria de la tabla actividades: numeral. | PK |
| 2 | `etapa` | `integer` | no | _Por documentar_ |  |
| 3 | `nombre` | `character varying(200)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 5 | `orden` | `integer` | no | _Por documentar_ |  |
| 6 | `activa` | `boolean` | no | _Por documentar_ |  |
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
| 3 | `exige_soporte` | `boolean` | no | _Por documentar_ |  |
| 4 | `confirmado` | `boolean` | no | false mientras la exigencia de soporte sea suposición del equipo y no cita de la matriz. |  |
| 5 | `nota_fuente` | `text` | sí | _Por documentar_ |  |

## actividades_excluidas

Celdas marcadas NO en la matriz de flujo: la actividad no aplica a esa modalidad.

- Clave primaria: `numeral`, `modalidad`
- Filas: 161
- Referencia a: `modalidad` → `hiring.modalidades` (1..* → 1); `numeral` → `hiring.actividades` (0..* → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `numeral` | `character varying(20)` | no | Clave primaria de la tabla actividades_excluidas: numeral. | PK FK→hiring.actividades.numeral |
| 2 | `modalidad` | `character varying(60)` | no | Clave primaria de la tabla actividades_excluidas: modalidad. | PK FK→hiring.modalidades.codigo |
| 3 | `motivo` | `text` | sí | _Por documentar_ |  |

## actividades_salvedad

Celdas de la matriz donde la actividad aplica pero con una condición o una variante propia de la modalidad.

- Clave primaria: `numeral`, `modalidad`
- Filas: 0
- Referencia a: `modalidad` → `hiring.modalidades` (0..1 → 1); `numeral` → `hiring.actividades` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `numeral` | `character varying(20)` | no | Clave primaria de la tabla actividades_salvedad: numeral. | PK FK→hiring.actividades.numeral |
| 2 | `modalidad` | `character varying(60)` | no | Clave primaria de la tabla actividades_salvedad: modalidad. | PK FK→hiring.modalidades.codigo |
| 3 | `variante` | `text` | sí | _Por documentar_ |  |
| 4 | `nota` | `text` | no | _Por documentar_ |  |

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
| 5 | `numero_acto` | `character varying(60)` | no | _Por documentar_ |  |
| 6 | `fecha_acto` | `date` | no | _Por documentar_ |  |
| 7 | `valor_adjudicado` | `numeric(18,2)` | no | _Por documentar_ |  |
| 8 | `acto_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 9 | `notificado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 10 | `publicado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 11 | `evidencia_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 12 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 13 | `emitido_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 14 | `emitido_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 15 | `revocado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 16 | `revocado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 17 | `motivo_revocacion` | `text` | sí | _Por documentar_ |  |
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
| 3 | `numero` | `integer` | no | _Por documentar_ |  |
| 4 | `tipo` | `character varying(20)` | no | _Por documentar_ |  |
| 5 | `objeto` | `text` | no | _Por documentar_ |  |
| 6 | `documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 7 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 8 | `emitida_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 9 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 10 | `fecha_publicacion` | `date` | sí | _Por documentar_ |  |
| 11 | `evidencia_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 12 | `publicada_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 13 | `vencimiento_anterior` | `date` | sí | Vencimiento del plazo de publicidad antes de aplicar la adenda de cronograma. |  |
| 14 | `vencimiento_nuevo` | `date` | sí | _Por documentar_ |  |
| 15 | `anulada_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 16 | `anulada_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 17 | `motivo_anulacion` | `text` | sí | _Por documentar_ |  |

## afiliaciones_arl

Afiliación a riesgos laborales, exigida a los contratistas persona natural (EFDS-1164).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `contrato_id` → `hiring.contratos` (0..1 → 1); `soporte_documento_id` → `hiring.documentos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla afiliaciones_arl. Se genera automáticamente. | PK |
| 2 | `contrato_id` | `uuid` | no | Referencia al registro de hiring.contratos (id). | única FK→hiring.contratos.id |
| 3 | `afiliado_por` | `character varying(20)` | no | _Por documentar_ |  |
| 4 | `administradora` | `character varying(200)` | no | _Por documentar_ |  |
| 5 | `numero_afiliacion` | `character varying(80)` | sí | _Por documentar_ |  |
| 6 | `fecha_afiliacion` | `date` | no | _Por documentar_ |  |
| 7 | `soporte_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 8 | `registrada_por` | `character varying(200)` | sí | _Por documentar_ |  |
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
| 3 | `accion` | `character varying(10)` | no | _Por documentar_ |  |
| 4 | `etapa` | `smallint` | sí | _Por documentar_ |  |
| 5 | `numeral` | `character varying(20)` | sí | Referencia al registro de hiring.actividades (numeral). | FK→hiring.actividades.numeral |
| 6 | `tramite` | `character varying(10)` | sí | _Por documentar_ |  |
| 7 | `confirmado` | `boolean` | no | _Por documentar_ |  |
| 8 | `activo` | `boolean` | no | _Por documentar_ |  |
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
| 4 | `valor_asegurado` | `numeric(18,2)` | no | _Por documentar_ |  |
| 5 | `vigencia_desde` | `date` | no | _Por documentar_ |  |
| 6 | `vigencia_hasta` | `date` | no | _Por documentar_ |  |
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
| 3 | `resolucion_numero` | `character varying(80)` | no | _Por documentar_ |  |
| 4 | `resolucion_fecha` | `date` | no | _Por documentar_ |  |
| 5 | `resolucion_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 6 | `pliego_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 7 | `secop_url` | `text` | sí | _Por documentar_ |  |
| 8 | `abierto_por` | `character varying(200)` | sí | _Por documentar_ |  |
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
| 2 | `obligatoria` | `boolean` | no | _Por documentar_ |  |
| 3 | `fundamento` | `text` | sí | _Por documentar_ |  |
| 4 | `confirmado` | `boolean` | no | _Por documentar_ |  |
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
| 3 | `celebrada_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 4 | `presidida_por` | `character varying(200)` | no | _Por documentar_ |  |
| 5 | `acta_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 6 | `resumen` | `text` | sí | _Por documentar_ |  |
| 7 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 8 | `registrada_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 9 | `registrada_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 10 | `anulada_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 11 | `motivo_anulacion` | `text` | sí | _Por documentar_ |  |
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
| 3 | `fecha_celebracion` | `date` | no | _Por documentar_ |  |
| 4 | `acta_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 5 | `matriz_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 6 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 7 | `registrado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 8 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `anulada_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 10 | `anulada_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 11 | `motivo_anulacion` | `text` | sí | _Por documentar_ |  |

## audiencias_sancionatorias

Audiencias del trámite sancionatorio (EFDS-1181, RF-INC-02). La citación mira al futuro; el acta, al hecho ya ocurrido.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `acta_documento_id` → `hiring.documentos` (0..1 → 0..1); `caso_id` → `hiring.casos_incumplimiento` (0..1 → 1); `citacion_documento_id` → `hiring.documentos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla audiencias_sancionatorias. Se genera automáticamente. | PK |
| 2 | `caso_id` | `uuid` | no | Referencia al registro de hiring.casos_incumplimiento (id). | FK→hiring.casos_incumplimiento.id |
| 3 | `citada_para` | `timestamp with time zone` | no | _Por documentar_ |  |
| 4 | `citacion_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 5 | `objeto` | `text` | sí | _Por documentar_ |  |
| 6 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 7 | `celebrada_el` | `date` | sí | _Por documentar_ |  |
| 8 | `acta_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 9 | `resumen` | `text` | sí | _Por documentar_ |  |
| 10 | `motivo` | `text` | sí | _Por documentar_ |  |
| 11 | `citada_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 12 | `registrada_por` | `character varying(200)` | sí | _Por documentar_ |  |
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
| 3 | `activo` | `boolean` | no | _Por documentar_ |  |
| 4 | `papeles` | `jsonb` | no | _Por documentar_ |  |
| 5 | `roles` | `jsonb` | no | _Por documentar_ |  |
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
| 3 | `avisado_at` | `timestamp with time zone` | no | _Por documentar_ |  |

## campos_formulario

_Por documentar._

- Clave primaria: `id`
- Filas: 13

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla campos_formulario. Se genera automáticamente. | PK |
| 2 | `numeral` | `character varying(20)` | no | _Por documentar_ |  |
| 3 | `codigo` | `character varying(80)` | no | _Por documentar_ |  |
| 4 | `etiqueta` | `character varying(300)` | no | _Por documentar_ |  |
| 5 | `ayuda` | `text` | sí | _Por documentar_ |  |
| 6 | `tipo` | `character varying(30)` | no | _Por documentar_ |  |
| 7 | `obligatorio` | `boolean` | no | _Por documentar_ |  |
| 8 | `grupo` | `character varying(120)` | sí | _Por documentar_ |  |
| 9 | `orden` | `integer` | no | _Por documentar_ |  |
| 10 | `opciones` | `jsonb` | sí | _Por documentar_ |  |
| 11 | `activo` | `boolean` | no | _Por documentar_ |  |
| 12 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 13 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 14 | `requiere_documento` | `boolean` | no | Reservado para actividades cuyo entregable es un documento, no un dato. |  |
| 15 | `solo_lectura` | `boolean` | no | _Por documentar_ |  |

## casos_incumplimiento

Reportes de presunto incumplimiento del contrato (EFDS-1180, RF-INC-01).

- Clave primaria: `id`
- Filas: 0
- Referencia a: `contrato_id` → `hiring.contratos` (0..1 → 1); `documento_id` → `hiring.documentos` (0..1 → 0..1); `supervision_id` → `hiring.supervisiones_contrato` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla casos_incumplimiento. Se genera automáticamente. | PK |
| 2 | `contrato_id` | `uuid` | no | Referencia al registro de hiring.contratos (id). | FK→hiring.contratos.id |
| 3 | `motivo` | `text` | no | _Por documentar_ |  |
| 4 | `fecha_hecho` | `date` | no | _Por documentar_ |  |
| 5 | `documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 6 | `estado` | `character varying(20)` | no | REPORTADO lo abre el supervisor (EFDS-1180); EN_TRAMITE, DECIDIDO y ARCHIVADO los mueve el trámite sancionatorio (EFDS-1181). |  |
| 7 | `reportado_por` | `character varying(200)` | sí | _Por documentar_ |  |
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
| 3 | `nombre` | `character varying(300)` | no | _Por documentar_ |  |
| 4 | `referencia_normativa` | `character varying(200)` | no | _Por documentar_ |  |
| 5 | `orden` | `integer` | no | _Por documentar_ |  |
| 6 | `activa` | `boolean` | no | _Por documentar_ |  |
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
| 3 | `numero` | `character varying(60)` | sí | _Por documentar_ |  |
| 4 | `valor` | `numeric(18,2)` | sí | _Por documentar_ |  |
| 5 | `rubro` | `character varying(160)` | sí | Rubro presupuestal que respalda el gasto. Lo registra la Financiera al verificar (4.2) y puede corregirlo al expedir (4.3); el área puede adelantarlo si lo conoce. |  |
| 6 | `fecha_expedicion` | `date` | sí | _Por documentar_ |  |
| 7 | `vigencia_fiscal` | `integer` | sí | _Por documentar_ |  |
| 8 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 9 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 10 | `solicitado_por` | `character varying(160)` | sí | _Por documentar_ |  |
| 11 | `solicitado_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 12 | `expedido_por` | `character varying(160)` | sí | _Por documentar_ |  |
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
| 3 | `fecha_cierre` | `date` | no | _Por documentar_ |  |
| 4 | `amparos_verificados` | `jsonb` | no | _Por documentar_ |  |
| 5 | `ultimo_vencimiento` | `date` | sí | _Por documentar_ |  |
| 6 | `soporte_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 7 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 8 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 9 | `cerrado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 10 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 11 | `revertido_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 12 | `revertido_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 13 | `motivo_reversion` | `text` | sí | _Por documentar_ |  |

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
| 5 | `fecha_pago_final` | `date` | no | _Por documentar_ |  |
| 6 | `soporte_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 7 | `valor_rp` | `numeric(18,2)` | no | _Por documentar_ |  |
| 8 | `valor_pagado` | `numeric(18,2)` | no | _Por documentar_ |  |
| 9 | `valor_liberado` | `numeric(18,2)` | no | _Por documentar_ |  |
| 10 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 11 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 12 | `cerrado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 13 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 14 | `revertido_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 15 | `revertido_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 16 | `motivo_reversion` | `text` | sí | _Por documentar_ |  |

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
| 4 | `fecha_designacion` | `date` | no | _Por documentar_ |  |
| 5 | `designado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 6 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 7 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `revocado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 9 | `revocado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 10 | `motivo_revocacion` | `text` | sí | _Por documentar_ |  |

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
| 4 | `numero` | `character varying(60)` | no | _Por documentar_ | única |
| 5 | `objeto` | `text` | no | Qué se contrató. Inmutable desde que el contrato se suscribe (RF-MOD-04): ninguna modificación contractual lo cambia. |  |
| 6 | `valor` | `numeric(18,2)` | no | _Por documentar_ |  |
| 7 | `plazo_dias` | `integer` | sí | _Por documentar_ |  |
| 8 | `contratista_documento` | `character varying(40)` | no | _Por documentar_ | Identificación |
| 9 | `contratista_nombre` | `character varying(300)` | no | _Por documentar_ |  |
| 10 | `contratista_tipo` | `character varying(20)` | no | _Por documentar_ |  |
| 11 | `minuta_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 12 | `plantilla_id` | `uuid` | sí | Referencia al registro de hiring.plantillas (id). | FK→hiring.plantillas.id |
| 13 | `estado` | `character varying(20)` | no | Situación actual del contrato en su ciclo (EFDS-1184, RF-SIS-01). Las transiciones válidas las decide puedeTransicionar en contrato.entity.ts. |  |
| 14 | `generado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 15 | `generado_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 16 | `aceptado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 17 | `aceptado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 18 | `aceptado_observacion` | `text` | sí | _Por documentar_ |  |
| 19 | `rechazado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 20 | `rechazado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 21 | `motivo_rechazo` | `text` | sí | _Por documentar_ |  |
| 22 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 23 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 24 | `perfeccionado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 25 | `contrato_firmado_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 26 | `legalizado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
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
| 3 | `causal` | `character varying(30)` | no | _Por documentar_ |  |
| 4 | `motivo` | `text` | no | _Por documentar_ |  |
| 5 | `numero_acto` | `character varying(60)` | no | _Por documentar_ |  |
| 6 | `fecha_acto` | `date` | no | _Por documentar_ |  |
| 7 | `acto_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 8 | `informe_comite_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 9 | `ofertas_recibidas` | `integer` | no | _Por documentar_ |  |
| 10 | `resultado_contradicho_id` | `uuid` | sí | Referencia al registro de hiring.resultados_evaluacion (id). | FK→hiring.resultados_evaluacion.id |
| 11 | `notificada_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 12 | `publicada_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 13 | `evidencia_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 14 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 15 | `declarada_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 16 | `declarada_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 17 | `revocada_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 18 | `revocada_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 19 | `motivo_revocacion` | `text` | sí | _Por documentar_ |  |
| 20 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 21 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |

## dias_no_habiles

Días no laborables propios de la ESAP, adicionales a los festivos nacionales que el servicio calcula (EFDS-1150).

- Clave primaria: `fecha`
- Filas: 0

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `fecha` | `date` | no | Clave primaria de la tabla dias_no_habiles: fecha. | PK |
| 2 | `descripcion` | `character varying(120)` | no | _Por documentar_ |  |
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
| 3 | `numeral` | `character varying(20)` | sí | _Por documentar_ |  |
| 4 | `tipo` | `character varying(30)` | no | _Por documentar_ |  |
| 5 | `nombre` | `character varying(300)` | no | _Por documentar_ |  |
| 6 | `archivo_url` | `text` | sí | _Por documentar_ |  |
| 7 | `contenido_snapshot` | `jsonb` | sí | _Por documentar_ |  |
| 8 | `archivo_nombre_original` | `character varying(300)` | sí | _Por documentar_ |  |
| 9 | `archivo_mime_type` | `character varying(120)` | sí | _Por documentar_ |  |
| 10 | `archivo_tamano` | `bigint` | sí | _Por documentar_ |  |
| 11 | `hash_sha256` | `character(64)` | no | _Por documentar_ |  |
| 12 | `version` | `integer` | no | _Por documentar_ |  |
| 13 | `subido_por` | `character varying(120)` | sí | _Por documentar_ |  |
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
| 3 | `numeral` | `character varying(20)` | no | _Por documentar_ |  |
| 4 | `codigo` | `character varying(60)` | no | _Por documentar_ |  |
| 5 | `documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 6 | `cargado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 7 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 8 | `anulado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 9 | `anulado_por` | `character varying(200)` | sí | _Por documentar_ |  |

## documentos_requeridos

Catálogo de documentos que exige cada actividad, filtrado por modalidad (EFDS-1149).

- Clave primaria: `id`
- Filas: 23

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla documentos_requeridos. Se genera automáticamente. | PK |
| 2 | `numeral` | `character varying(20)` | no | _Por documentar_ |  |
| 3 | `codigo` | `character varying(60)` | no | _Por documentar_ |  |
| 4 | `nombre` | `character varying(200)` | no | _Por documentar_ |  |
| 5 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 6 | `modalidades` | `jsonb` | no | _Por documentar_ |  |
| 7 | `obligatorio` | `boolean` | no | _Por documentar_ |  |
| 8 | `orden` | `integer` | no | _Por documentar_ |  |
| 9 | `activo` | `boolean` | no | _Por documentar_ |  |
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
| 3 | `descripcion` | `character varying(500)` | no | _Por documentar_ |  |
| 4 | `fecha_entrega` | `date` | sí | _Por documentar_ |  |
| 5 | `observacion` | `text` | sí | _Por documentar_ |  |
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
| 4 | `descripcion` | `character varying(300)` | no | _Por documentar_ |  |
| 5 | `cargada_por` | `character varying(200)` | sí | _Por documentar_ |  |
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
| 3 | `numero_expediente` | `character varying(60)` | no | _Por documentar_ | única |
| 4 | `estado` | `character varying(40)` | no | _Por documentar_ |  |
| 5 | `fecha_apertura` | `timestamp with time zone` | no | _Por documentar_ |  |
| 6 | `archivado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 7 | `archivado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 8 | `indice_documental` | `jsonb` | sí | Índice congelado: qué documentos tenía el expediente el día en que se archivó (EFDS-1174). |  |
| 9 | `radicado_active_document` | `character varying(120)` | sí | _Por documentar_ |  |
| 10 | `observaciones_archivo` | `text` | sí | _Por documentar_ |  |
| 11 | `reabierto_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 12 | `reabierto_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 13 | `motivo_reapertura` | `text` | sí | _Por documentar_ |  |

## firmas_contrato

Firmas del ordenador del gasto y del contratista, con su evidencia (EFDS-1162).

- Clave primaria: `id`
- Filas: 2
- Referencia a: `contrato_id` → `hiring.contratos` (1..* → 1); `evidencia_documento_id` → `hiring.documentos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla firmas_contrato. Se genera automáticamente. | PK |
| 2 | `contrato_id` | `uuid` | no | Referencia al registro de hiring.contratos (id). | FK→hiring.contratos.id |
| 3 | `parte` | `character varying(20)` | no | _Por documentar_ |  |
| 4 | `firmante_nombre` | `character varying(300)` | no | _Por documentar_ |  |
| 5 | `firmante_documento` | `character varying(40)` | sí | _Por documentar_ | Identificación |
| 6 | `registrada_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 7 | `fecha_firma` | `date` | no | _Por documentar_ |  |
| 8 | `evidencia_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 9 | `hash_documento` | `character(64)` | sí | _Por documentar_ |  |
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
| 3 | `aseguradora` | `character varying(200)` | no | _Por documentar_ |  |
| 4 | `numero_poliza` | `character varying(80)` | no | _Por documentar_ |  |
| 5 | `documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 6 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 7 | `cargada_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 8 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 9 | `revisada_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 10 | `revisada_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 11 | `motivo_rechazo` | `text` | sí | _Por documentar_ |  |

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
| 5 | `resultado` | `jsonb` | no | _Por documentar_ |  |
| 6 | `cambios` | `jsonb` | no | _Por documentar_ |  |
| 7 | `ofertas_recibidas` | `integer` | no | _Por documentar_ |  |
| 8 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 9 | `informe_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 10 | `evidencia_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 11 | `generado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 12 | `generado_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 13 | `publicado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 14 | `publicado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 15 | `anulado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 16 | `motivo_anulacion` | `text` | sí | _Por documentar_ |  |
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
| 3 | `numero` | `integer` | no | _Por documentar_ |  |
| 4 | `resultado_id` | `uuid` | no | Referencia al registro de hiring.resultados_evaluacion (id). | FK→hiring.resultados_evaluacion.id |
| 5 | `resultado` | `jsonb` | no | _Por documentar_ |  |
| 6 | `ofertas_recibidas` | `integer` | no | _Por documentar_ |  |
| 7 | `observacion_entidad` | `text` | sí | _Por documentar_ |  |
| 8 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 9 | `informe_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 10 | `evidencia_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 11 | `generado_por` | `character varying(120)` | sí | _Por documentar_ |  |
| 12 | `generado_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 13 | `trasladado_por` | `character varying(120)` | sí | _Por documentar_ |  |
| 14 | `trasladado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 15 | `plazo_dias_habiles` | `integer` | sí | _Por documentar_ |  |
| 16 | `vence_el` | `date` | sí | _Por documentar_ |  |
| 17 | `cerrado_por` | `character varying(120)` | sí | _Por documentar_ |  |
| 18 | `cerrado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 19 | `nota_cierre` | `text` | sí | _Por documentar_ |  |
| 20 | `anulado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 21 | `motivo_anulacion` | `text` | sí | _Por documentar_ |  |
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
| 4 | `fecha_elaboracion` | `date` | no | _Por documentar_ |  |
| 5 | `conclusion` | `text` | no | _Por documentar_ |  |
| 6 | `balance` | `jsonb` | no | _Por documentar_ |  |
| 7 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 8 | `elaborado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 9 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 10 | `anulado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 11 | `anulado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 12 | `motivo_anulacion` | `text` | sí | _Por documentar_ |  |

## limitaciones_mipyme

Decisión de limitar o no la convocatoria a MIPYME, con las condiciones que se evaluaron (EFDS-1151).

- Clave primaria: `id`
- Filas: 2
- Referencia a: `proceso_id` → `hiring.procesos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla limitaciones_mipyme. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | no | Referencia al registro de hiring.procesos (id). | única FK→hiring.procesos.id |
| 3 | `limitado` | `boolean` | no | _Por documentar_ |  |
| 4 | `condiciones_cumplidas` | `boolean` | no | Lo que arrojó el cálculo. Puede diferir de `limitado`: la entidad decide, no el sistema. |  |
| 5 | `manifestaciones_contadas` | `integer` | no | _Por documentar_ |  |
| 6 | `valor_proceso` | `numeric(18,2)` | sí | _Por documentar_ |  |
| 7 | `tope_valor_aplicado` | `numeric(18,2)` | sí | _Por documentar_ |  |
| 8 | `unidad_tope_aplicada` | `character varying(10)` | sí | _Por documentar_ |  |
| 9 | `minimo_manifestaciones` | `integer` | sí | _Por documentar_ |  |
| 10 | `motivo` | `text` | sí | _Por documentar_ |  |
| 11 | `documento_id` | `uuid` | sí | _Por documentar_ |  |
| 12 | `decidido_por` | `character varying(160)` | sí | _Por documentar_ |  |
| 13 | `decidido_at` | `timestamp with time zone` | no | _Por documentar_ |  |
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
| 3 | `nombre` | `character varying(200)` | no | _Por documentar_ |  |
| 4 | `identificacion` | `character varying(60)` | no | _Por documentar_ |  |
| 5 | `fecha_presentacion` | `date` | no | _Por documentar_ |  |
| 6 | `documento_id` | `uuid` | sí | _Por documentar_ |  |
| 7 | `registrado_por` | `character varying(160)` | sí | _Por documentar_ |  |
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
| 3 | `persona_id` | `uuid` | no | _Por documentar_ |  |
| 4 | `nombre` | `character varying(200)` | no | _Por documentar_ |  |
| 5 | `rol` | `character varying(20)` | no | _Por documentar_ |  |
| 6 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## modalidades

_Por documentar._

- Clave primaria: `codigo`
- Filas: 11

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `codigo` | `character varying(60)` | no | Clave primaria de la tabla modalidades: código. | PK |
| 2 | `nombre` | `character varying(160)` | no | _Por documentar_ |  |
| 3 | `orden` | `integer` | no | _Por documentar_ |  |
| 4 | `activa` | `boolean` | no | _Por documentar_ |  |
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
| 3 | `tipo` | `character varying(30)` | no | _Por documentar_ |  |
| 4 | `numero` | `character varying(80)` | sí | _Por documentar_ |  |
| 5 | `fecha_suscripcion` | `date` | sí | _Por documentar_ |  |
| 6 | `justificacion` | `text` | no | _Por documentar_ |  |
| 7 | `documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 8 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 9 | `valor_adicionado` | `numeric(18,2)` | sí | _Por documentar_ |  |
| 10 | `cdp_id` | `uuid` | sí | Referencia al registro de hiring.cdp (id). | FK→hiring.cdp.id |
| 11 | `rp_id` | `uuid` | sí | Referencia al registro de hiring.registros_presupuestales (id). | FK→hiring.registros_presupuestales.id |
| 12 | `valor_contrato_antes` | `numeric(18,2)` | sí | _Por documentar_ |  |
| 13 | `valor_contrato_despues` | `numeric(18,2)` | sí | _Por documentar_ |  |
| 14 | `tope_porcentaje` | `numeric(5,2)` | sí | _Por documentar_ |  |
| 15 | `solicitada_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 16 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 17 | `aprobada_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 18 | `aprobada_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 19 | `revocada_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 20 | `revocada_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 21 | `motivo_revocacion` | `text` | sí | _Por documentar_ |  |
| 22 | `dias_prorroga` | `integer` | sí | Días que la prórroga añade al plazo. La reanudación no lo usa: los suyos se derivan de las fechas. |  |
| 23 | `plazo_dias_antes` | `integer` | sí | _Por documentar_ |  |
| 24 | `plazo_dias_despues` | `integer` | sí | _Por documentar_ |  |
| 25 | `suspension_desde` | `date` | sí | _Por documentar_ |  |
| 26 | `suspension_hasta` | `date` | sí | _Por documentar_ |  |
| 27 | `reanuda_modificacion_id` | `uuid` | sí | Referencia al registro de hiring.modificaciones_contrato (id). | FK→hiring.modificaciones_contrato.id |
| 28 | `reanudada_el` | `date` | sí | _Por documentar_ |  |
| 29 | `cedente_documento` | `character varying(40)` | sí | _Por documentar_ | Identificación |
| 30 | `cedente_nombre` | `character varying(300)` | sí | _Por documentar_ |  |
| 31 | `cedente_tipo` | `character varying(20)` | sí | _Por documentar_ |  |
| 32 | `cesionario_documento` | `character varying(40)` | sí | _Por documentar_ | Identificación |
| 33 | `cesionario_nombre` | `character varying(300)` | sí | _Por documentar_ |  |
| 34 | `cesionario_tipo` | `character varying(20)` | sí | _Por documentar_ |  |
| 35 | `terminacion_causal` | `character varying(20)` | sí | MUTUO_ACUERDO o UNILATERAL, las dos que define la fuente. El incumplimiento no está aquí: es el proceso sancionatorio (EFDS-1181). |  |
| 36 | `terminacion_el` | `date` | sí | _Por documentar_ |  |
| 37 | `estado_contrato_antes` | `character varying(20)` | sí | _Por documentar_ |  |
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
| 4 | `presentado_por` | `character varying(200)` | no | _Por documentar_ |  |
| 5 | `identificacion` | `character varying(60)` | sí | _Por documentar_ |  |
| 6 | `fecha_presentacion` | `date` | no | _Por documentar_ |  |
| 7 | `asunto` | `character varying(300)` | no | _Por documentar_ |  |
| 8 | `contenido` | `text` | no | _Por documentar_ |  |
| 9 | `fuera_de_termino` | `boolean` | no | Congelado al registrar: si la fecha de presentación superó el vencimiento de la publicidad. |  |
| 10 | `documento_id` | `uuid` | sí | _Por documentar_ | ↝hiring.documentos.id |
| 11 | `registrado_por` | `character varying(160)` | sí | _Por documentar_ |  |
| 12 | `respuesta` | `text` | sí | _Por documentar_ |  |
| 13 | `respondida_por` | `character varying(160)` | sí | _Por documentar_ |  |
| 14 | `respondida_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 15 | `modifico_pliego` | `boolean` | sí | _Por documentar_ |  |
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
| 3 | `numero` | `integer` | no | _Por documentar_ |  |
| 4 | `nombre` | `character varying(200)` | no | _Por documentar_ |  |
| 5 | `identificacion` | `character varying(40)` | no | _Por documentar_ |  |
| 6 | `fecha_radicacion` | `timestamp with time zone` | no | Fecha y hora en que la oferta se radicó ante la entidad, no la del registro en la plataforma. |  |
| 7 | `soporte_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 8 | `registrado_por` | `character varying(200)` | sí | _Por documentar_ |  |
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
| 3 | `numero` | `integer` | no | _Por documentar_ |  |
| 4 | `periodo_desde` | `date` | no | _Por documentar_ |  |
| 5 | `periodo_hasta` | `date` | no | _Por documentar_ |  |
| 6 | `valor` | `numeric(18,2)` | no | _Por documentar_ |  |
| 7 | `factura_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 8 | `informe_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 9 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 10 | `radicado_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 11 | `radicado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 12 | `avalado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 13 | `avalado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 14 | `observacion_aval` | `text` | sí | _Por documentar_ |  |
| 15 | `devuelto_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 16 | `devuelto_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 17 | `motivo_devolucion` | `text` | sí | _Por documentar_ |  |
| 18 | `tramitado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 19 | `tramitado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 20 | `referencia_pago` | `character varying(120)` | sí | _Por documentar_ |  |
| 21 | `anulado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 22 | `anulado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 23 | `motivo_anulacion` | `text` | sí | _Por documentar_ |  |
| 24 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## parametros_alerta

Plazos que gobiernan las alertas de contratación: anticipación por vencimiento, tolerancia sin abogado y hora del aviso diario.

- Clave primaria: `clave`
- Filas: 6

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `clave` | `character varying(60)` | no | Clave primaria de la tabla parametros_alerta: clave. | PK |
| 2 | `valor` | `integer` | no | _Por documentar_ |  |
| 3 | `minimo` | `integer` | no | _Por documentar_ |  |
| 4 | `maximo` | `integer` | no | _Por documentar_ |  |
| 5 | `descripcion` | `text` | no | _Por documentar_ |  |
| 6 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 7 | `updated_by` | `character varying(120)` | sí | Usuario que realizó la última actualización del registro. |  |

## parametros_mipyme

Condiciones que habilitan la limitación a MIPYME. Parametrizables (EFDS-1393).

- Clave primaria: `clave`
- Filas: 2

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `clave` | `character varying(40)` | no | Clave primaria de la tabla parametros_mipyme: clave. | PK |
| 2 | `valor` | `numeric(18,2)` | no | _Por documentar_ |  |
| 3 | `unidad` | `character varying(10)` | sí | _Por documentar_ |  |
| 4 | `descripcion` | `character varying(200)` | no | _Por documentar_ |  |
| 5 | `fundamento` | `text` | sí | _Por documentar_ |  |
| 6 | `confirmado` | `boolean` | no | _Por documentar_ |  |
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
| 3 | `papel` | `character varying(20)` | no | _Por documentar_ |  |
| 4 | `usuario_id` | `uuid` | sí | _Por documentar_ |  |
| 5 | `usuario_nombre` | `character varying(120)` | no | _Por documentar_ |  |
| 6 | `persona_id` | `uuid` | sí | _Por documentar_ |  |
| 7 | `nombre` | `character varying(200)` | no | _Por documentar_ |  |
| 8 | `cargo` | `character varying(200)` | sí | _Por documentar_ |  |
| 9 | `email` | `character varying(200)` | sí | _Por documentar_ | Contacto |
| 10 | `asignado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 11 | `asignado_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 12 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 13 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 14 | `relevado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 15 | `relevado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 16 | `motivo_relevo` | `text` | sí | _Por documentar_ |  |

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
| 4 | `tipo` | `character varying(20)` | no | _Por documentar_ |  |
| 5 | `descripcion` | `character varying(300)` | no | _Por documentar_ |  |
| 6 | `cargada_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 7 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## plantillas

_Por documentar._

- Clave primaria: `id`
- Filas: 10

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla plantillas. Se genera automáticamente. | PK |
| 2 | `codigo` | `character varying(40)` | no | _Por documentar_ |  |
| 3 | `nombre` | `character varying(400)` | no | _Por documentar_ |  |
| 4 | `numeral` | `character varying(20)` | no | _Por documentar_ |  |
| 5 | `version` | `character varying(10)` | no | _Por documentar_ |  |
| 6 | `fecha_aprobacion` | `date` | sí | _Por documentar_ |  |
| 7 | `modalidades` | `jsonb` | no | _Por documentar_ |  |
| 8 | `archivo_url` | `text` | sí | _Por documentar_ |  |
| 9 | `activo` | `boolean` | no | _Por documentar_ |  |
| 10 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## plazo_publicacion_acta

Plazo para publicar el acta de liquidación, parametrizable y marcado si está sin confirmar (EFDS-1174).

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla plazo_publicacion_acta. | PK |
| 2 | `dias_habiles` | `integer` | no | _Por documentar_ |  |
| 3 | `fundamento` | `text` | sí | _Por documentar_ |  |
| 4 | `confirmado` | `boolean` | no | _Por documentar_ |  |
| 5 | `actualizado_at` | `timestamp with time zone` | no | _Por documentar_ |  |

## plazo_publicacion_contrato

Plazo para publicar el contrato, parametrizable y marcado si está sin confirmar (EFDS-1166).

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla plazo_publicacion_contrato. | PK |
| 2 | `dias_habiles` | `integer` | no | _Por documentar_ |  |
| 3 | `fundamento` | `text` | sí | _Por documentar_ |  |
| 4 | `confirmado` | `boolean` | no | _Por documentar_ |  |
| 5 | `actualizado_at` | `timestamp with time zone` | no | _Por documentar_ |  |

## plazos_ofertas

Días hábiles de recepción de ofertas por modalidad, contados desde la apertura (EFDS-1155).

- Clave primaria: `modalidad`
- Filas: 7
- Referencia a: `modalidad` → `hiring.modalidades` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `modalidad` | `character varying(60)` | no | Clave primaria de la tabla plazos_ofertas: modalidad. | PK FK→hiring.modalidades.codigo |
| 2 | `dias_habiles` | `integer` | no | _Por documentar_ |  |
| 3 | `fundamento` | `text` | sí | _Por documentar_ |  |
| 4 | `confirmado` | `boolean` | no | _Por documentar_ |  |
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
| 2 | `dias_habiles` | `integer` | no | _Por documentar_ |  |
| 3 | `fundamento` | `text` | sí | _Por documentar_ |  |
| 4 | `confirmado` | `boolean` | no | _Por documentar_ |  |
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
| 2 | `dias_habiles` | `integer` | no | _Por documentar_ |  |
| 3 | `fundamento` | `text` | sí | _Por documentar_ |  |
| 4 | `confirmado` | `boolean` | no | _Por documentar_ |  |
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
| 3 | `numeral` | `character varying(20)` | no | _Por documentar_ |  |
| 4 | `estado` | `character varying(30)` | no | _Por documentar_ |  |
| 5 | `datos` | `jsonb` | no | _Por documentar_ |  |
| 6 | `version` | `integer` | no | _Por documentar_ |  |
| 7 | `enviado_por` | `character varying(120)` | sí | _Por documentar_ |  |
| 8 | `enviado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 9 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 10 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 11 | `revisado_por` | `character varying(120)` | sí | _Por documentar_ |  |
| 12 | `revisado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 13 | `documento_requerido` | `boolean` | no | _Por documentar_ |  |
| 14 | `enviado_por_id` | `character varying(120)` | sí | Id del usuario que envió a aprobación. Permite impedir que quien ejecutó la actividad se la apruebe. |  |

## procesos

_Por documentar._

- Clave primaria: `id`
- Filas: 10
- Referencia a: `causal` → `hiring.causales_contratacion` (0..1 → 0..1); `modalidad` → `hiring.modalidades` (0..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla procesos. Se genera automáticamente. | PK |
| 2 | `radicado` | `character varying(60)` | no | _Por documentar_ | única |
| 3 | `objeto` | `text` | no | _Por documentar_ |  |
| 4 | `etapa` | `integer` | no | _Por documentar_ |  |
| 5 | `fecha_radicacion` | `timestamp with time zone` | no | _Por documentar_ |  |
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
| 3 | `destino` | `character varying(20)` | no | _Por documentar_ |  |
| 4 | `fecha_publicacion` | `date` | no | _Por documentar_ |  |
| 5 | `plazo_dias_habiles` | `integer` | sí | _Por documentar_ |  |
| 6 | `fecha_limite` | `date` | sí | _Por documentar_ |  |
| 7 | `secop_numero` | `character varying(80)` | sí | _Por documentar_ |  |
| 8 | `secop_url` | `text` | sí | _Por documentar_ |  |
| 9 | `documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 10 | `publicado_por` | `character varying(200)` | sí | _Por documentar_ |  |
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
| 3 | `destino` | `character varying(20)` | no | _Por documentar_ |  |
| 4 | `fecha_publicacion` | `date` | no | _Por documentar_ |  |
| 5 | `plazo_dias_habiles` | `integer` | sí | _Por documentar_ |  |
| 6 | `fecha_limite` | `date` | sí | _Por documentar_ |  |
| 7 | `secop_numero` | `character varying(80)` | sí | _Por documentar_ |  |
| 8 | `secop_url` | `text` | sí | _Por documentar_ |  |
| 9 | `documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 10 | `publicado_por` | `character varying(200)` | sí | _Por documentar_ |  |
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
| 3 | `fecha_publicacion` | `date` | no | _Por documentar_ |  |
| 4 | `secop_numero` | `character varying(80)` | sí | _Por documentar_ |  |
| 5 | `secop_url` | `text` | sí | _Por documentar_ |  |
| 6 | `documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 7 | `publicada_por` | `character varying(200)` | sí | _Por documentar_ |  |
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
| 5 | `fecha_vencimiento` | `date` | sí | _Por documentar_ |  |
| 6 | `secop_numero` | `character varying(60)` | sí | _Por documentar_ |  |
| 7 | `secop_url` | `text` | sí | _Por documentar_ |  |
| 8 | `documento_id` | `uuid` | no | _Por documentar_ | ↝hiring.documentos.id |
| 9 | `publicado_por` | `character varying(160)` | sí | _Por documentar_ |  |
| 10 | `anulada_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 11 | `anulada_por` | `character varying(160)` | sí | _Por documentar_ |  |
| 12 | `motivo_anulacion` | `text` | sí | _Por documentar_ |  |
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
| 4 | `plazo_dias_habiles` | `integer` | sí | _Por documentar_ |  |
| 5 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 6 | `cerrada_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 7 | `cerrada_por` | `character varying(200)` | sí | _Por documentar_ |  |
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
| 5 | `nota` | `text` | no | _Por documentar_ |  |
| 6 | `documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 7 | `datos` | `jsonb` | no | _Por documentar_ |  |
| 8 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 9 | `registrado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 10 | `registrado_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 11 | `anulado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 12 | `anulado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 13 | `motivo_anulacion` | `text` | sí | _Por documentar_ |  |

## registros_presupuestales

Registros presupuestales que comprometen los recursos del contrato (EFDS-1163).

- Clave primaria: `id`
- Filas: 1
- Referencia a: `contrato_id` → `hiring.contratos` (0..1 → 1); `documento_id` → `hiring.documentos` (0..1 → 0..1); `modificacion_id` → `hiring.modificaciones_contrato` (0..1 → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla registros_presupuestales. Se genera automáticamente. | PK |
| 2 | `contrato_id` | `uuid` | no | Referencia al registro de hiring.contratos (id). | FK→hiring.contratos.id |
| 3 | `numero` | `character varying(60)` | sí | _Por documentar_ |  |
| 4 | `valor` | `numeric(18,2)` | sí | _Por documentar_ |  |
| 5 | `rubro` | `character varying(160)` | sí | _Por documentar_ |  |
| 6 | `fecha_expedicion` | `date` | sí | _Por documentar_ |  |
| 7 | `vigencia_fiscal` | `integer` | sí | _Por documentar_ |  |
| 8 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 9 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 10 | `documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 11 | `solicitado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 12 | `solicitado_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 13 | `expedido_por` | `character varying(200)` | sí | _Por documentar_ |  |
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
| 4 | `tipo` | `character varying(30)` | no | _Por documentar_ |  |
| 5 | `config` | `jsonb` | no | _Por documentar_ |  |
| 6 | `mensaje` | `text` | sí | _Por documentar_ |  |
| 7 | `orden` | `integer` | no | _Por documentar_ |  |
| 8 | `vigente_desde` | `timestamp with time zone` | no | _Por documentar_ |  |
| 9 | `vigente_hasta` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 10 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 11 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
| 12 | `condiciones` | `jsonb` | no | Cuando aplica: [{campo, operador, valor}]. Vacio = siempre. |  |
| 13 | `acciones` | `jsonb` | no | Que hace: [{accion, objetivo, valor}]. accion es EXIGIR_CAMPO, MOSTRAR_CAMPO, OCULTAR_CAMPO, EXIGIR_DOCUMENTO, BLOQUEAR_AVANCE. |  |
| 14 | `conector` | `character varying(3)` | no | _Por documentar_ |  |

## resoluciones_sancionatorias

Actos administrativos del trámite sancionatorio (EFDS-1181, RF-INC-02): el que lo abre y el que lo decide, incluida la caducidad.

- Clave primaria: `id`
- Filas: 0
- Referencia a: `caso_id` → `hiring.casos_incumplimiento` (0..1 → 1); `documento_id` → `hiring.documentos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla resoluciones_sancionatorias. Se genera automáticamente. | PK |
| 2 | `caso_id` | `uuid` | no | Referencia al registro de hiring.casos_incumplimiento (id). | FK→hiring.casos_incumplimiento.id |
| 3 | `tipo` | `character varying(20)` | no | _Por documentar_ |  |
| 4 | `numero` | `character varying(80)` | no | _Por documentar_ |  |
| 5 | `fecha_expedicion` | `date` | no | _Por documentar_ |  |
| 6 | `documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 7 | `sentido` | `character varying(30)` | sí | DECLARA_CADUCIDAD termina el contrato: es la caducidad como causal contractual que pide el bloque de Presunto Incumplimiento. |  |
| 8 | `valor_sancion` | `numeric(18,2)` | sí | _Por documentar_ |  |
| 9 | `estado_contrato_antes` | `character varying(20)` | sí | _Por documentar_ |  |
| 10 | `notificada_el` | `date` | sí | _Por documentar_ |  |
| 11 | `firme_el` | `date` | sí | _Por documentar_ |  |
| 12 | `expedida_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 13 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 14 | `revocada_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 15 | `revocada_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 16 | `motivo_revocacion` | `text` | sí | _Por documentar_ |  |

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
| 5 | `puntaje_obtenido` | `numeric(6,2)` | sí | _Por documentar_ |  |
| 6 | `puntaje_maximo` | `numeric(6,2)` | sí | _Por documentar_ |  |
| 7 | `valor_evaluado` | `numeric(18,2)` | sí | _Por documentar_ |  |
| 8 | `justificacion` | `text` | no | _Por documentar_ |  |
| 9 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 10 | `registrado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 11 | `registrado_at` | `timestamp with time zone` | no | _Por documentar_ |  |
| 12 | `rectificado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 13 | `rectificado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 14 | `motivo_rectificacion` | `text` | sí | _Por documentar_ |  |
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
| 3 | `decision` | `character varying(20)` | no | _Por documentar_ |  |
| 4 | `observaciones` | `text` | sí | _Por documentar_ |  |
| 5 | `version_revisada` | `integer` | no | _Por documentar_ |  |
| 6 | `revisado_por` | `character varying(120)` | no | _Por documentar_ |  |
| 7 | `revisado_por_id` | `character varying(120)` | sí | _Por documentar_ |  |
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
| 3 | `tipo` | `character varying(20)` | no | _Por documentar_ |  |
| 4 | `descripcion` | `text` | no | _Por documentar_ |  |
| 5 | `periodo_desde` | `date` | sí | _Por documentar_ |  |
| 6 | `periodo_hasta` | `date` | sí | _Por documentar_ |  |
| 7 | `fecha_soporte` | `date` | no | _Por documentar_ |  |
| 8 | `documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 9 | `registrado_por` | `character varying(200)` | sí | _Por documentar_ |  |
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
| 3 | `fecha` | `date` | no | _Por documentar_ |  |
| 4 | `decision` | `character varying(30)` | no | _Por documentar_ |  |
| 5 | `condiciones` | `text` | sí | _Por documentar_ |  |
| 6 | `observaciones` | `text` | sí | Lo que el comité objetó: obligatorio al observar y al rechazar, y también cuando aprueba pero reabre alguna actividad para que se la validen. |  |
| 7 | `acta_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 8 | `registrado_por` | `character varying(120)` | sí | _Por documentar_ |  |
| 9 | `registrado_por_id` | `character varying(120)` | sí | _Por documentar_ |  |
| 10 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## smmlv

Salario mínimo mensual legal vigente por año. Base de los umbrales expresados en SMMLV (EFDS-1147).

- Clave primaria: `anio`
- Filas: 2

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `anio` | `integer` | no | Clave primaria de la tabla smmlv: año. | PK |
| 2 | `valor` | `numeric(18,2)` | no | _Por documentar_ |  |
| 3 | `confirmado` | `boolean` | no | _Por documentar_ |  |
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
| 6 | `observacion` | `text` | sí | _Por documentar_ |  |
| 7 | `abierto_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 8 | `abierto_at` | `timestamp with time zone` | no | _Por documentar_ |  |
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
| 4 | `tipo` | `character varying(30)` | no | _Por documentar_ |  |
| 5 | `descripcion` | `character varying(300)` | sí | _Por documentar_ |  |
| 6 | `cargado_por` | `character varying(200)` | sí | _Por documentar_ |  |
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
| 4 | `tipo` | `character varying(20)` | no | _Por documentar_ |  |
| 5 | `presentado_por` | `character varying(200)` | no | _Por documentar_ |  |
| 6 | `identificacion` | `character varying(60)` | sí | _Por documentar_ |  |
| 7 | `fecha_presentacion` | `date` | no | _Por documentar_ |  |
| 8 | `extemporanea` | `boolean` | no | _Por documentar_ |  |
| 9 | `asunto` | `character varying(300)` | no | _Por documentar_ |  |
| 10 | `contenido` | `text` | no | _Por documentar_ |  |
| 11 | `soporte_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 12 | `respuesta` | `text` | sí | _Por documentar_ |  |
| 13 | `respuesta_documento_id` | `uuid` | sí | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 14 | `aceptada` | `boolean` | sí | _Por documentar_ |  |
| 15 | `respondida_por` | `character varying(120)` | sí | _Por documentar_ |  |
| 16 | `respondida_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 17 | `registrado_por` | `character varying(120)` | sí | _Por documentar_ |  |
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
| 4 | `fecha_designacion` | `date` | no | _Por documentar_ |  |
| 5 | `persona_id` | `uuid` | no | _Por documentar_ |  |
| 6 | `nombre` | `character varying(200)` | no | _Por documentar_ |  |
| 7 | `cargo` | `character varying(200)` | sí | _Por documentar_ |  |
| 8 | `email` | `character varying(200)` | sí | _Por documentar_ | Contacto |
| 9 | `designado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 10 | `estado` | `character varying(20)` | no | _Por documentar_ |  |
| 11 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 12 | `alerta_enviada_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 13 | `relevado_at` | `timestamp with time zone` | sí | _Por documentar_ |  |
| 14 | `relevado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 15 | `motivo_relevo` | `text` | sí | _Por documentar_ |  |

## suscripciones_acta_inicio

Acta de inicio suscrita por la entidad y el contratista (actividad 8.7). La reunión (9.1) va en actas_inicio.

- Clave primaria: `id`
- Filas: 1
- Referencia a: `acta_documento_id` → `hiring.documentos` (0..1 → 1); `contrato_id` → `hiring.contratos` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `uuid` | no | Identificador único del registro en la tabla suscripciones_acta_inicio. Se genera automáticamente. | PK |
| 2 | `contrato_id` | `uuid` | no | Referencia al registro de hiring.contratos (id). | FK→hiring.contratos.id |
| 3 | `fecha_suscripcion` | `date` | no | _Por documentar_ |  |
| 4 | `acta_documento_id` | `uuid` | no | Referencia al registro de hiring.documentos (id). | FK→hiring.documentos.id |
| 5 | `registrado_por` | `character varying(200)` | sí | _Por documentar_ |  |
| 6 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## tipologias_contrato

Tipologías de contrato y el formato del SIG que sirve de minuta (EFDS-1161).

- Clave primaria: `codigo`
- Filas: 12

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `codigo` | `character varying(60)` | no | Clave primaria de la tabla tipologias_contrato: código. | PK |
| 2 | `nombre` | `character varying(200)` | no | _Por documentar_ |  |
| 3 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 4 | `numeral_formato` | `character varying(20)` | no | _Por documentar_ |  |
| 5 | `exige_garantias` | `boolean` | no | _Por documentar_ |  |
| 6 | `activo` | `boolean` | no | _Por documentar_ |  |
| 7 | `orden` | `integer` | no | _Por documentar_ |  |

## tipos_amparo

Coberturas que puede incluir una garantía, para controlar sus vencimientos (EFDS-1164).

- Clave primaria: `codigo`
- Filas: 7

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `codigo` | `character varying(60)` | no | Clave primaria de la tabla tipos_amparo: código. | PK |
| 2 | `nombre` | `character varying(200)` | no | _Por documentar_ |  |
| 3 | `descripcion` | `text` | sí | _Por documentar_ |  |
| 4 | `activo` | `boolean` | no | _Por documentar_ |  |
| 5 | `orden` | `integer` | no | _Por documentar_ |  |

## tope_adicion

Tope legal de la adición como porcentaje del valor inicial del contrato (EFDS-1176).

- Clave primaria: `id`
- Filas: 1

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `integer` | no | Identificador único del registro en la tabla tope_adicion. | PK |
| 2 | `porcentaje` | `numeric(5,2)` | no | _Por documentar_ |  |
| 3 | `fundamento` | `text` | sí | _Por documentar_ |  |
| 4 | `confirmado` | `boolean` | no | _Por documentar_ |  |
| 5 | `actualizado_at` | `timestamp with time zone` | no | _Por documentar_ |  |

## trazabilidad

_Por documentar._

- Clave primaria: `id`
- Filas: 236
- Referencia a: `proceso_id` → `hiring.procesos` (1..* → 0..1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `id` | `bigint` | no | Identificador único del registro en la tabla trazabilidad. Se genera automáticamente. | PK |
| 2 | `proceso_id` | `uuid` | sí | Referencia al registro de hiring.procesos (id). | FK→hiring.procesos.id |
| 3 | `entidad` | `character varying(80)` | no | _Por documentar_ |  |
| 4 | `entidad_id` | `uuid` | sí | _Por documentar_ |  |
| 5 | `accion` | `character varying(60)` | no | _Por documentar_ |  |
| 6 | `detalle` | `jsonb` | sí | _Por documentar_ |  |
| 7 | `usuario_id` | `character varying(120)` | sí | _Por documentar_ |  |
| 8 | `usuario_nombre` | `character varying(200)` | sí | _Por documentar_ |  |
| 9 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |

## umbrales_comite_contratacion

Condición de cuantía para pasar por el comité de contratación (actividad 3.7). La modalidad sin fila va a comité siempre que la matriz la marque.

- Clave primaria: `modalidad`
- Filas: 1
- Referencia a: `modalidad` → `hiring.modalidades` (0..1 → 1)

| # | Columna | Tipo | Nulos | Descripción | Marcas |
|--:|---|---|---|---|---|
| 1 | `modalidad` | `character varying(60)` | no | Clave primaria de la tabla umbrales_comite_contratacion: modalidad. | PK FK→hiring.modalidades.codigo |
| 2 | `valor` | `numeric(18,2)` | no | _Por documentar_ |  |
| 3 | `unidad` | `character varying(10)` | no | _Por documentar_ |  |
| 4 | `fundamento` | `text` | sí | _Por documentar_ |  |
| 5 | `confirmado` | `boolean` | no | _Por documentar_ |  |
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
| 3 | `limite_inferior` | `numeric(18,2)` | sí | _Por documentar_ |  |
| 4 | `limite_superior` | `numeric(18,2)` | sí | _Por documentar_ |  |
| 5 | `unidad` | `character varying(10)` | no | _Por documentar_ |  |
| 6 | `vigencia_desde` | `date` | no | _Por documentar_ |  |
| 7 | `vigencia_hasta` | `date` | sí | _Por documentar_ |  |
| 8 | `confirmado` | `boolean` | no | _Por documentar_ |  |
| 9 | `created_by` | `character varying(160)` | sí | Usuario que creó el registro. |  |
| 10 | `created_at` | `timestamp with time zone` | no | Fecha y hora de creación del registro. |  |
| 11 | `updated_at` | `timestamp with time zone` | no | Fecha y hora de la última actualización del registro. |  |
