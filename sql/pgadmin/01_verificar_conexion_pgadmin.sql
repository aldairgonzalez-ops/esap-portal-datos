/* Verificación previa a la extracción · versión para el QUERY TOOL de pgAdmin · SOLO LECTURA
   Es una sola consulta: pegar completa y ejecutar con F5. Devuelve una tabla "verificación / resultado".
   (La versión con comandos psql está en sql/01_verificar_conexion_SOLO_PSQL.sql.) */
with esquemas as (
  select n.nspname as esquema,
         count(c.oid) filter (where c.relkind in ('r','p') and not c.relispartition) as tablas,
         count(c.oid) filter (where c.relkind in ('v','m')) as vistas,
         count(c.oid) filter (where c.relkind in ('r','p') and not c.relispartition and c.reltuples <= 0) as sin_filas_est
  from pg_namespace n
  left join pg_class c on c.relnamespace = n.oid
  where n.nspname not in ('pg_catalog','information_schema','pg_toast')
    and n.nspname not like 'pg_temp%' and n.nspname not like 'pg_toast_temp%'
  group by n.nspname
), permisos as (
  select count(*) as total, count(*) filter (where not has_table_privilege(c.oid, 'SELECT')) as sin_select
  from pg_class c join pg_namespace n on n.oid = c.relnamespace
  where c.relkind in ('r','p','v','m') and n.nspname not in ('pg_catalog','information_schema','pg_toast')
), maestra as (
  select string_agg(a.attname || ' ' || format_type(a.atttypid, a.atttypmod), ', ' order by a.attname) as cols
  from pg_attribute a
  where a.attrelid = to_regclass('auth.personas') and not a.attisdropped
    and a.attname in ('dir_email','num_identificacion','id_person')
), filas as (
  select 1 as orden, '1. Base' as verificacion, current_database()::text as resultado
  union all select 2, '1. Servidor y puerto', coalesce(host(inet_server_addr()), 'socket local') || ':' || coalesce(inet_server_port()::text, '-')
  union all select 3, '1. Usuario', current_user::text
  union all select 4, '1. Motor', split_part(version(), ' on ', 1)
  union all select 5, '1. Tamaño de la base', pg_size_pretty(pg_database_size(current_database()))
  union all select 6, '1. Sesión de solo lectura (default_transaction_read_only)', current_setting('default_transaction_read_only')
  union all select 7, '2. Total esquemas / tablas / vistas',
        (select count(*) from esquemas)::text || ' esquemas · ' || (select sum(tablas) from esquemas)::text || ' tablas · '
        || (select sum(vistas) from esquemas)::text || ' vistas   (mayo 2026: 162 tablas en 11 esquemas)'
  union all select 8, '2. Esquema: ' || esquema, tablas || ' tablas · ' || vistas || ' vistas · ' || sin_filas_est || ' sin filas (estimado)' from esquemas
  union all select 100, '3. Tablas y vistas sin permiso SELECT (debe ser 0)', sin_select || ' de ' || total from permisos
  union all select 101, '4. Fuente maestra auth.personas', coalesce((select cols from maestra), 'NO ENCONTRADA')
  union all select 102, '5. Tablas nunca analizadas (estadísticas)',
        (select count(*) filter (where coalesce(last_analyze, last_autoanalyze) is null) || ' de ' || count(*) from pg_stat_user_tables)
)
select verificacion, resultado from filas order by orden, verificacion;
