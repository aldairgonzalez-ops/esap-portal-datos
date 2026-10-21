# Portal de Datos · Base de datos SuperApp ESAP

Documentación entregable de la base de datos de la SuperApp ESAP (entorno QA):

- **Portal de Datos** (`portal/`): un HTML autónomo que se abre en cualquier navegador sin conexión. Incluye catálogo con buscador, ficha de cada tabla, modelo entidad-relación por dominio, relaciones con multiplicidad UML medida con datos, funciones y triggers, indicadores de calidad, identidad replicada y datos personales.
- **Resumen ejecutivo** (`informe/`): documento Word para el cliente que cita el portal y este repositorio.
- **Detalle técnico** (`docs/`): el mismo contenido en CSV y Markdown, más el informe de cada extracción.

Todo sale de una **extracción de solo lectura** que no exporta valores de datos: solo estructura, estadísticas y conteos.

## Requisitos
- Python 3.10 o superior, con `python-docx` (`pip install -r requirements.txt`).
- `psql`. Ya viene con pgAdmin 4, en `C:\Program Files\pgAdmin 4\runtime\psql.exe`; `extraer.py` lo busca solo.
- Tailscale conectado y acceso a la base QA.

## 1. Configurar la conexión (una sola vez)
1. Copia `config/pg_service.conf.example` a `%APPDATA%\postgresql\.pg_service.conf` en Windows, o a `~/.pg_service.conf` en Linux y macOS. Completa el host de Tailscale, la base y el usuario.
2. Guarda la contraseña en `%APPDATA%\postgresql\pgpass.conf` con el formato `host:puerto:base:usuario:contraseña`. Si no lo haces, psql la pide en cada ejecución.
3. Prueba la conexión: `psql "service=esap_qa" -c "select current_database(), inet_server_addr(), version()"`.

> Lo recomendable es pedir al DBA un rol de solo lectura con `sql/00_rol_lector.sql`. Aun sin ese rol, la extracción corre en una transacción `READ ONLY` y el servicio fuerza `default_transaction_read_only`.

## 2. Generar los entregables
```powershell
python herramientas/extraer.py                                  # crea extracciones/AAAA-MM-DD
python herramientas/generar_portal.py  --extraccion extracciones/AAAA-MM-DD --version v1.0 --repo <url-repo>
python herramientas/generar_resumen.py --extraccion extracciones/AAAA-MM-DD --version v1.0 --url-portal <url-portal> --repo <url-repo>
```
- `extraer.py` imprime el servidor al que se conectó. **Confirma que es QA y no DEV.**
- Para comparar con un corte anterior, agrega `--anterior extracciones/<fecha previa>` a `generar_portal.py`. El informe listará las tablas, columnas, FK y programables que cambiaron.
- Para ver el portal, abre el HTML o sirve la carpeta con `python -m http.server 8765` y entra a `http://localhost:8765/portal/`.

## 3. Documentar descripciones (opcional, con aprobación)
1. Registra las descripciones en `config/descripciones.csv` (separador `;`) con el estado `propuesta` o `validada`. El portal las muestra con su marca.
2. Genera el lote con `python herramientas/generar_comentarios.py --extraccion extracciones/AAAA-MM-DD --lote L001`.
3. Simula con `psql "service=esap_qa" -X -v aplicar=0 -f sql/metadatos/L001_aplicar_comentarios.sql`.
4. Aplica, solo con aprobación: el mismo comando con `-v aplicar=1`. Para deshacer está `L001_reversa_comentarios.sql`.

> El servicio `esap_qa` es de solo lectura. Para aplicar comentarios hace falta un usuario con permiso de `COMMENT` (dueño de los objetos), sin `default_transaction_read_only`.

## Contenido
| Ruta | Qué es |
|---|---|
| `sql/extraccion/00…13_*.sql` | Consultas de catálogo, conteo exacto, cardinalidad de FK, relaciones implícitas e identidad |
| `herramientas/` | Lanzador de la extracción y generadores del portal, el resumen y los lotes de comentarios |
| `config/` | Nombres de dominio, propuestas de descripción y plantilla de conexión |
| `extracciones/` | Cortes de la base (JSONL) |
| `portal/` · `docs/` · `informe/` | Entregables generados |
| `pruebas/` | Base sintética para probar el flujo sin tocar QA |

## Indicadores del portal
| Id | Indicador | Dimensión (ISO/IEC 25012) |
|---|---|---|
| K01 / K02 | Tablas y columnas con descripción | Comprensibilidad |
| K03 | Tablas con clave primaria | Unicidad |
| K04 | Relaciones declaradas como FK frente a implícitas confirmadas | Integridad referencial |
| K05 | FK con índice en la columna hija | Eficiencia |
| K06 | Valores sin registro padre en FK | Consistencia |
| K07 | Tablas operativas con datos | Actualidad |
| K08 | Tablas de apoyo (respaldos, copias, migraciones) | Mantenibilidad |
| K09 | Columnas de correo o documento con datos fuera de la fuente maestra | Consistencia |
| K10 | Columnas con datos personales (Ley 1581 de 2012) | Confidencialidad |
