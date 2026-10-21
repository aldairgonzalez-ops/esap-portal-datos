-- 01 · Esquemas de usuario con su propietario y comentario.
with d as (
  select n.nspname as s, pg_get_userbyid(n.nspowner) as owner,
         obj_description(n.oid, 'pg_namespace') as d
  from pg_namespace n
  where n.nspname not in ('pg_catalog', 'information_schema', 'pg_toast')
    and n.nspname not like 'pg_temp_%' and n.nspname not like 'pg_toast_temp_%'
)
select x from (
  select row_to_json(r)::text as x, 0 as o from (select * from d order by s) r
  union all select json_build_object('_fin', (select count(*) from d))::text, 1
) z order by o;
