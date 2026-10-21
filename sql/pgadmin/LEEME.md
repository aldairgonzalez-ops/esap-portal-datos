# Trabajar desde pgAdmin

| Paso | Herramienta de pgAdmin | Archivo |
|---|---|---|
| Verificar la conexión | **Query Tool** | `01_verificar_conexion_pgadmin.sql` (SQL puro, una sola consulta) |
| Extraer el catálogo | **PSQL Tool** | `../extraccion/extraer_todo.sql` (usa comandos psql: `\o`, `\ir`, `\if`) |

El Query Tool no entiende los comandos que empiezan con `\`. Por eso la extracción se hace en la PSQL Tool, que es el `psql` que trae pgAdmin, ya conectado con la configuración del servidor en pgAdmin.

## 1. Verificación (Query Tool)
1. En el árbol de pgAdmin, sobre la base de **QA**, abre el menú contextual y elige *Query Tool*.
2. Abre `sql/pgadmin/01_verificar_conexion_pgadmin.sql` (o pega su contenido) y ejecútalo con F5.
3. Revisa que el servidor sea el de QA, que «sin permiso SELECT» sea 0 y que la fuente maestra `auth.personas` aparezca.

## 2. Extracción (PSQL Tool)
1. Crea la carpeta de salida dentro del repositorio, por ejemplo `extracciones\2026-10-22`.
2. Sobre la base de **QA**, abre el menú contextual y elige *PSQL Tool*.
3. Pega estas líneas. Ajusta la ruta del repositorio (con `/`), la fecha y el nombre de la base:
```
\cd 'G:/Mi unidad/SuperApp ESAP/Portal_Datos_BD'
\set salida extracciones/2026-10-22
\set bd_esperada esap_db
\set maestro_email auth.personas.dir_email
\set maestro_doc auth.personas.num_identificacion
\i sql/extraccion/extraer_todo.sql
```
4. Debe terminar con `OK: extracción completa en 'extracciones/2026-10-22'`. Si aparece `ALTO`, la base conectada no es la indicada en `bd_esperada`.
5. Verifica los 14 archivos desde una terminal en la raíz del repositorio:
```
python herramientas/extraer.py --solo-verificar extracciones/2026-10-22
```

La carpeta de salida no puede tener espacios, y la ruta del repositorio en `\cd` va entre comillas simples y con `/`.
