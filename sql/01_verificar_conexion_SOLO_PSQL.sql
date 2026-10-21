-- NO ABRIR EN EL QUERY TOOL DE pgADMIN: usa comandos psql (\set, \echo). Para pgAdmin: sql/pgadmin/01_verificar_conexion_pgadmin.sql
/* Verificación previa a la extracción · SOLO LECTURA · ~segundos
   Confirma: a qué servidor y base estoy conectado, que la sesión es de solo lectura, que puedo leer
   todas las tablas, qué esquemas hay (para comparar con el diagnóstico de mayo: 162 tablas / 11 esquemas)
   y que existe la fuente maestra de identidad.
   Uso:  psql "service=esap_qa" -X -f sql/01_verificar_conexion_SOLO_PSQL.sql */
\set QUIET on
\pset pager off
\pset footer off
begin transaction read only;

\echo '== 1. Conexión'
select current_database() as base, coalesce(host(inet_server_addr()), 'socket local') as servidor,
       inet_server_port() as puerto, current_user as usuario, split_part(version(), ' on ', 1) as motor,
       pg_size_pretty(pg_database_size(current_database())) as tamano,
       current_setting('default_transaction_read_only') as sesion_solo_lectura,
       current_setting('transaction_read_only') as transaccion_solo_lectura;

\echo '== 2. Esquemas y objetos (comparar con: 162 tablas en 11 esquemas, mayo 2026)'
select n.nspname as esquema,
       count(*) filter (where c.relkind in ('r','p') and not c.relispartition) as tablas,
       count(*) filter (where c.relkind in ('v','m')) as vistas,
       count(*) filter (where c.relkind in ('r','p') and c.reltuples <= 0) as tablas_sin_filas_estimadas
from pg_namespace n
left join pg_class c on c.relnamespace = n.oid
where n.nspname not in ('pg_catalog','information_schema','pg_toast') and n.nspname not like 'pg_temp%' and n.nspname not like 'pg_toast_temp%'
group by n.nspname order by n.nspname;

\echo '== 3. Permisos de lectura (debe dar 0 tablas sin SELECT)'
select count(*) as tablas_total,
       count(*) filter (where not has_table_privilege(c.oid, 'SELECT')) as tablas_sin_select
from pg_class c join pg_namespace n on n.oid = c.relnamespace
where c.relkind in ('r','p','v','m') and n.nspname not in ('pg_catalog','information_schema','pg_toast');

\echo '== 4. Fuente maestra de identidad (auth.personas)'
select a.attname as columna, format_type(a.atttypid, a.atttypmod) as tipo
from pg_attribute a
where a.attrelid = to_regclass('auth.personas') and a.attname in ('dir_email','num_identificacion','id_person') and not a.attisdropped
order by a.attname;

\echo '== 5. Estadísticas del planificador (tablas nunca analizadas: el conteo exacto lo corrige la extracción)'
select count(*) filter (where coalesce(last_analyze, last_autoanalyze) is null) as nunca_analizadas, count(*) as tablas
from pg_stat_user_tables;
rollback;
