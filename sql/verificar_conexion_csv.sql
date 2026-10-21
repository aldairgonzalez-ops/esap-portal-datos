/* Verificación previa en CSV (evidencia). La lanza:  python herramientas/extraer.py --verificar-conexion
   Reutiliza la consulta de pgAdmin; solo cambia el formato de salida. Solo lectura. */
\set ON_ERROR_STOP on
\pset format csv
begin transaction read only;
\set f :salida/verificacion_conexion.csv
\o :f
\ir pgadmin/01_verificar_conexion_pgadmin.sql
\o
rollback;
