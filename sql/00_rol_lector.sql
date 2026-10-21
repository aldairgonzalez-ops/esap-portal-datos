/* Rol de solo lectura para el Portal de Datos ESAP. LO EJECUTA EL DBA en QA (no forma parte de la extracción).
   pg_read_all_data (PostgreSQL 14+) da SELECT sobre todas las tablas, vistas y secuencias, presentes y futuras.
   pg_read_all_stats permite leer estadísticas de uso (índices y tablas). Cambiar la contraseña antes de ejecutar. */
create role portal_lector login password 'CAMBIAR' connection limit 3;
grant pg_read_all_data to portal_lector;
grant pg_read_all_stats to portal_lector;
alter role portal_lector set default_transaction_read_only = on;
alter role portal_lector set statement_timeout = '20min';
