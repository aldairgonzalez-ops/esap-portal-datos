-- 00 · Contexto de la extracción (servidor, base, versión, tamaño). Solo lectura.
with d as (
  select current_database()                       as db,
         coalesce(host(inet_server_addr()), 'socket') as srv,
         inet_server_port()                        as puerto,
         current_user                              as usuario,
         split_part(version(), ',', 1)             as version,
         current_setting('server_version_num')::int as version_num,
         pg_database_size(current_database())      as bytes,
         to_char(now() at time zone 'America/Bogota', 'YYYY-MM-DD"T"HH24:MI:SS') as fecha,
         current_setting('TimeZone')               as zona
)
select x from (
  select row_to_json(r)::text as x, 0 as o from d r
  union all select json_build_object('_fin', (select count(*) from d))::text, 1
) z order by o;
