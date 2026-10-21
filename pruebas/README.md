# Base sintética de prueba

`esquema_prueba.sql` crea una base con la forma de ESAP: esquemas `auth`, `academic_registration`, `certification` y otros; correos y documentos replicados; tablas sin filas; un respaldo `_bkp_`; una tabla sin PK; relaciones sin FK; triggers, funciones y vistas. Sirve para probar el flujo completo sin tocar QA.

```bash
createdb esap_qa_prueba
psql -d esap_qa_prueba -f pruebas/esquema_prueba.sql
python herramientas/extraer.py --host localhost --usuario postgres --bd esap_qa_prueba --salida extracciones/prueba
python herramientas/generar_portal.py --extraccion extracciones/prueba --version v0.0-prueba --entorno "QA (prueba)"
```
