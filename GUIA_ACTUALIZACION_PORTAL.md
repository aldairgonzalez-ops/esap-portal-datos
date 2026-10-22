# Guía para actualizar el Portal de Datos ESAP

Esta guía explica cómo poner al día el Portal de Datos, el resumen ejecutivo y el detalle técnico, en sus dos versiones:

- **Fase 2** (versión Lite): Programación académica, RUND, Contratación, Gestión de infraestructura, Viáticos y Chatbot. Usa `--alcance config/alcances/fase2.json`.
- **Base completa**: los 16 esquemas de `esap_db`. Usa los mismos comandos sin `--alcance`.

Cubre tres situaciones:

| Situación | Sección |
|---|---|
| La base de QA cambió (tablas, columnas, relaciones, filas) | [1. Actualizar los datos](#1-actualizar-los-datos-del-portal) |
| Hay descripciones nuevas o corregidas (columnas, tablas o dominios) | [2. Actualizar las descripciones](#2-actualizar-las-descripciones) |
| Se autorizó registrar las descripciones en la base | [3. Registrar las descripciones en la base](#3-registrar-las-descripciones-en-la-base-comment-on) |

Los comandos son para **PowerShell en Windows**, desde el clon del repositorio en `C:\proyectos\Portal_Datos_BD`.

---

## 0. Antes de empezar

1. **Traer la última versión del repositorio** y confirmar que quedó al día:
   ```powershell
   cd C:\proyectos\Portal_Datos_BD
   git pull
   git log -1 --oneline
   ```
   El commit que muestra `git log` debe ser el mismo que el último de GitHub (`main`). Si `git pull` muestra un error (cambios locales, conflicto, credenciales), resuélvalo antes de seguir. De lo contrario, el portal se genera con la versión anterior de las herramientas o de las descripciones.

2. **Elegir la versión nueva.** Cada cambio del portal es una versión nueva (`v1.3` → `v1.4`). No se sobrescriben versiones ya entregadas. Versiones vigentes:
   | Portal | Última versión | Carpeta |
   |---|---|---|
   | Fase 2 | v1.3 | `portal\fase2\` |
   | Base completa | v1.1 | `portal\` |

3. **Conexión a QA (solo para extraer).** Tailscale activo y la contraseña del usuario de la base a mano. La contraseña se escribe cada vez que `psql` la pide y **no se guarda** en ningún archivo ni variable.

---

## 1. Actualizar los datos del portal

Se hace cuando la base de QA cambió: tablas o columnas nuevas, relaciones, programables o número de filas.

### 1.1 Extraer de QA (solo lectura)

```powershell
python herramientas/extraer.py --verificar-conexion
python herramientas/extraer.py
```

- El primer comando deja `evidencias\<fecha>\verificacion_conexion.csv` y confirma que la conexión es a QA (`100.127.140.5`, base `esap_db`). Se detiene si apunta a otro servidor.
- El segundo deja la extracción en `extracciones\<fecha>\` (14 archivos JSONL). Toda la extracción corre en `BEGIN TRANSACTION READ ONLY`: no escribe en la base y no extrae valores de los registros, solo estructura y conteos.

Suba la extracción para que quede en el repositorio:
```powershell
git add evidencias extracciones
git commit -m "Extracción de QA del <fecha>"
git push
```

### 1.2 Generar el portal de Fase 2

Reemplace `<fecha>` por la fecha de la extracción nueva, `<anterior>` por la de la extracción previa y `vX.Y` por la versión nueva.

```powershell
$R = "https://github.com/aldairgonzalez-ops/esap-portal-datos"
$A = "config/alcances/fase2.json"

python herramientas/generar_portal.py --extraccion extracciones/<fecha> --version vX.Y --anterior extracciones/<anterior> --alcance $A --repo $R
python herramientas/generar_resumen.py --extraccion extracciones/<fecha> --version vX.Y --alcance $A --repo $R
python herramientas/generar_informe_interno.py --extraccion extracciones/<fecha> --version vX.Y --alcance $A
```

Salidas:
| Archivo | Para |
|---|---|
| `portal\fase2\Portal_de_Datos_ESAP_Fase2_vX.Y.html` | Cliente |
| `informe\fase2\Resumen_Ejecutivo_BD_ESAP_Fase2_vX.Y.docx` | Cliente |
| `docs\fase2\` (csv, catálogo por dominio, `informe_extraccion_Fase2_vX.Y.md`) | Cliente (detalle técnico) |
| `interno\fase2\` (portal interno, informe de hallazgos, csv de diagnóstico) | Solo personal del proyecto |

`--anterior` agrega al informe de extracción la sección «Cambios frente a la extracción anterior»: tablas, columnas, FK y programables nuevos o retirados.

### 1.3 Generar el portal de la base completa

Los mismos comandos, sin `--alcance`:

```powershell
python herramientas/generar_portal.py --extraccion extracciones/<fecha> --version vX.Y --anterior extracciones/<anterior> --repo $R
python herramientas/generar_resumen.py --extraccion extracciones/<fecha> --version vX.Y --repo $R
python herramientas/generar_informe_interno.py --extraccion extracciones/<fecha> --version vX.Y
```

Salidas: `portal\Portal_de_Datos_ESAP_vX.Y.html`, `informe\Resumen_Ejecutivo_BD_ESAP_vX.Y.docx`, `docs\` e `interno\`.

### 1.4 Revisar antes de entregar

1. Abra el portal en el navegador y recorra Inicio, el buscador, varias fichas de tabla, el Modelo ER de cada dominio y el Inventario de programables, en tema claro y oscuro.
2. En Inicio, revise los indicadores y la «Arquitectura Conceptual de Módulos»: cada dominio debe tener descripción.
3. Confirme que nada de `interno\` va al cliente.

Si se agregó una columna o tabla nueva, aparecerá sin descripción («Definición de negocio en construcción»). Para documentarla, siga la sección 2.

### 1.5 Copiar a Drive y subir al repositorio

```powershell
# Fase 2
robocopy portal\fase2  "G:\Mi unidad\SuperApp ESAP\Portal_Datos_BD\Entregable\Fase2" /E
robocopy informe\fase2 "G:\Mi unidad\SuperApp ESAP\Portal_Datos_BD\Entregable\Fase2" /E
robocopy docs\fase2    "G:\Mi unidad\SuperApp ESAP\Portal_Datos_BD\Entregable\Fase2\docs" /E
robocopy interno\fase2 "G:\Mi unidad\SuperApp ESAP\Portal_Datos_BD\Interno\Fase2" /E

# Base completa
robocopy portal  "G:\Mi unidad\SuperApp ESAP\Portal_Datos_BD\Entregable" Portal_de_Datos_ESAP_v*.html
robocopy informe "G:\Mi unidad\SuperApp ESAP\Portal_Datos_BD\Entregable" Resumen_Ejecutivo_BD_ESAP_v*.docx
robocopy interno "G:\Mi unidad\SuperApp ESAP\Portal_Datos_BD\Interno" *.html *.docx

git add portal informe docs config
git commit -m "Portal vX.Y"
git push
```

`interno\` no se sube a Git: solo se copia a la carpeta `Interno` de Drive.

---

## 2. Actualizar las descripciones

Las descripciones del portal tienen tres orígenes, en este orden de prioridad:

| Estado en el portal | Origen | Dónde se cambia |
|---|---|---|
| Sin etiqueta | Comentario registrado en la base (`COMMENT ON`) | En la base (sección 3) |
| «validada» | `config/descripciones.csv`, estado `validada` | Matriz de validación (2.1) o hoja de tablas (2.2) |
| «propuesta» | Dominios (`config/dominios.csv`, `config/alcances/fase2.json`) | Editando esos archivos (2.3) |

Las descripciones validadas **se ven en el portal, pero no están en la base** hasta que se aplique un lote `COMMENT ON` (sección 3).

### 2.1 Descripciones de columnas: matriz de validación

Matrices vigentes, en `config\propuestas\` y en Drive `Interno\Matrices`:

| Matriz | Contiene |
|---|---|
| `Matriz_Validacion_Descripciones_Fase2.xlsx` | Las columnas de Fase 2 que siguen pendientes (las aprobadas ya no aparecen) |
| `Matriz_Validacion_Descripciones_Completa.xlsx` | Las columnas pendientes de toda la base |

**Revisar.** En la hoja «Matriz», filtre por la columna «Decisión»:
- Las filas en **«Requiere aclaración»** traen una **pregunta para desarrollo**. Una vez resuelta, cambie la decisión a «Aprobada» o, si el texto debe cambiar, a «Aprobada con ajuste», y escriba el texto en «Descripción final».
- Las filas en **«Pendiente»** se revisan igual. La columna «Evidencia en código» muestra el archivo y la línea del backend donde se define el campo.
- La hoja «Métricas» muestra el avance y la cobertura que se alcanza al incorporar.

**Incorporar lo aprobado** (guarde el Excel antes):
```powershell
python herramientas/matriz_descripciones.py incorporar --matriz config/propuestas/Matriz_Validacion_Descripciones_Fase2.xlsx
python herramientas/matriz_descripciones.py incorporar --matriz config/propuestas/Matriz_Validacion_Descripciones_Completa.xlsx
```
Las filas aprobadas pasan a `config/descripciones.csv` con estado `validada`. Incorporar la misma matriz dos veces no duplica nada.

**Regenerar las matrices** para que queden solo las pendientes:
```powershell
python herramientas/matriz_descripciones.py contexto --extraccion extracciones/<fecha> --alcance config/alcances/fase2.json
python herramientas/matriz_descripciones.py matriz   --extraccion extracciones/<fecha> --alcance config/alcances/fase2.json
python herramientas/matriz_descripciones.py contexto --extraccion extracciones/<fecha>
python herramientas/matriz_descripciones.py matriz   --extraccion extracciones/<fecha>
```

Luego genere una versión nueva del portal (secciones 1.2 y 1.3; no hace falta extraer de nuevo si la base no cambió).

**Columnas nuevas.** Si una extracción trae columnas que no estaban, entran a la matriz sin propuesta semántica. Para redactarlas con el mismo método, primero actualice la evidencia del código. Se lee el repositorio de la aplicación (`hernan-Saroa/Plataformacomunidadesap`, rama `micro-frontend`) sin ejecutarlo:
```powershell
python herramientas/evidencia_codigo.py --repo <ruta del clon de la aplicación> --rama micro-frontend --alcance config/alcances/fase2.json
```
La redacción de las propuestas (`config/propuestas/<alcance>_semanticas.csv`, `_codigo.csv`, `_ajustes.csv`) se hace con apoyo de Claude, con el procedimiento descrito en `CLAUDE.md` (sección 4b).

### 2.2 Descripciones de tablas

Las de Fase 2 están en `config\propuestas\fase2_tablas.csv` (Excel, separador `;`), una fila por tabla, con propuesta, confianza, fundamento, pregunta y decisión.

1. Para cada tabla en «Requiere aclaración», resuelva la pregunta y cambie `decision` a `Aprobada`. Si el texto cambia, corríjalo en `propuesta`.
2. Incorpore:
   ```powershell
   python herramientas/matriz_descripciones.py incorporar --tablas config/propuestas/fase2_tablas.csv
   ```
3. Genere una versión nueva del portal.

### 2.3 Descripciones y nombres de dominio

- **Base completa y Fase 2:** `config\dominios.csv`, con las columnas `esquema;nombre;orden;descripcion`. Si el esquema tiene comentario en la base, el portal muestra ese comentario y no el del archivo.
- **RUND (solo Fase 2):** `config\alcances\fase2.json`, en `parciales` → `academic_work_plan` → `nombre` y `descripcion`.

Los nombres y descripciones de dominio se muestran como «propuesta» hasta que el cliente los valide.

### 2.4 Descripciones aplicadas a mano

Si una descripción se acuerda fuera de la matriz, puede agregarse directamente en `config\descripciones.csv`:
```
esquema;tabla;columna;descripcion;estado
hiring;contratos;valor;Valor total del contrato, en pesos colombianos.;validada
```
Deje `columna` vacía para describir una tabla. Use `validada` para lo acordado y `propuesta` para lo que falta confirmar.

---

## 3. Registrar las descripciones en la base (`COMMENT ON`)

Solo con **autorización explícita** para escribir en QA. El lote toca únicamente comentarios: no cambia datos ni restricciones, y siempre tiene reversa.

1. **Generar el lote** con las descripciones validadas, a partir de la extracción vigente (de ella se toma el comentario actual para la reversa):
   ```powershell
   python herramientas/generar_comentarios.py --extraccion extracciones/<fecha> --lote L00N
   ```
   Deja `sql\metadatos\L00N_aplicar_comentarios.sql` y `sql\metadatos\L00N_reversa_comentarios.sql`. Use un número de lote nuevo cada vez (L001 ya existe).

2. **Simular** (ejecuta todo y lo revierte):
   ```powershell
   mkdir evidencias\<hoy> -Force
   & "C:\Program Files\pgAdmin 4\runtime\psql.exe" -h 100.127.140.5 -p 5432 -U postgres -d esap_db -X -v aplicar=0 -f sql/metadatos/L00N_aplicar_comentarios.sql -L evidencias/<hoy>/L00N_simulacion.log
   ```
   Debe terminar con «SIMULACIÓN: todo se ejecutó y se revirtió». Suba el log al repositorio y revíselo antes de aplicar.

3. **Aplicar** (con aprobación):
   ```powershell
   & "C:\Program Files\pgAdmin 4\runtime\psql.exe" -h 100.127.140.5 -p 5432 -U postgres -d esap_db -X -v aplicar=1 -f sql/metadatos/L00N_aplicar_comentarios.sql -L evidencias/<hoy>/L00N_aplicacion.log
   ```
   Debe terminar con «APLICADO: cambios confirmados».

4. **Revertir**, si hace falta:
   ```powershell
   & "C:\Program Files\pgAdmin 4\runtime\psql.exe" -h 100.127.140.5 -p 5432 -U postgres -d esap_db -X -v aplicar=1 -f sql/metadatos/L00N_reversa_comentarios.sql -L evidencias/<hoy>/L00N_reversa.log
   ```

5. **Extraer de nuevo** (sección 1.1) y generar una versión nueva del portal. Las descripciones aparecen entonces como registradas en la base, sin etiqueta.

---

## 4. Problemas frecuentes

| Síntoma | Causa probable | Qué hacer |
|---|---|---|
| El portal no muestra un cambio que ya está en GitHub | El `git pull` no se completó | `git status` y `git log -1 --oneline`; resuelva el error del pull y genere de nuevo |
| `Select-String … -Quiet` responde `False` | El portal se generó con archivos anteriores | Igual que el anterior |
| `psql: … No such file or directory` | Se ejecutó desde otra carpeta o falta el `git pull` | `cd C:\proyectos\Portal_Datos_BD` y `git pull` |
| «Acceso denegado» al escribir en la carpeta de Drive | Drive bloquea archivos mientras sincroniza | Generar siempre en `C:\proyectos\…` y copiar con `robocopy` |
| `extraer.py` se detiene diciendo que el servidor no es el esperado | La conexión no va a QA | Verifique Tailscale y el host `100.127.140.5` |
| `generar_portal.py` se detiene por «textos de SIPAE» | Quedó un texto de la plantilla original | Avisar: hay que ajustar `herramientas/portal_sipae.py` |
| Una descripción aprobada no aparece en el portal | No se incorporó o el portal no se regeneró | Ejecutar `incorporar` (2.1 o 2.2) y generar una versión nueva |

---

## 5. Archivos clave

| Archivo | Contenido |
|---|---|
| `config/descripciones.csv` | Descripciones validadas y propuestas que usa el portal |
| `config/dominios.csv` | Nombre, orden y descripción de cada dominio |
| `config/alcances/fase2.json` | Esquemas y tablas de la Fase 2 |
| `config/propuestas/Matriz_Validacion_Descripciones_*.xlsx` | Matrices de validación de columnas |
| `config/propuestas/fase2_tablas.csv` | Propuestas y decisiones de las descripciones de tabla de Fase 2 |
| `config/propuestas/fase2_decisiones.csv` | Registro de las decisiones sobre columnas (quién, cuándo, criterio) |
| `sql/metadatos/` | Lotes `COMMENT ON` y su reversa |
| `CLAUDE.md` | Reglas de trabajo y contexto completo del proyecto |
