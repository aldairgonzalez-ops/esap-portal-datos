-- 06 · Funciones y procedimientos (k: f=función, p=procedimiento, a=agregada, w=ventana).
-- Se excluyen los que pertenecen a extensiones (pg_depend deptype 'e').
with d as (
  select n.nspname as s, p.proname as n, p.prokind as k, l.lanname as lang,
         pg_get_function_identity_arguments(p.oid) as args,
         case when p.prokind = 'p' then null else pg_get_function_result(p.oid) end as ret,
         obj_description(p.oid, 'pg_proc') as d,
         p.prosecdef as secdef, p.provolatile as vol,
         case when l.lanname in ('sql', 'plpgsql') then p.prosrc end as src
  from pg_proc p
  join pg_namespace n on n.oid = p.pronamespace
  join pg_language l on l.oid = p.prolang
  where n.nspname not in ('pg_catalog', 'information_schema')
    and not exists (select 1 from pg_depend e where e.classid = 'pg_proc'::regclass and e.objid = p.oid and e.deptype = 'e')
)
select x from (
  select row_to_json(r)::text as x, 0 as o from (select * from d order by s, n, args) r
  union all select json_build_object('_fin', (select count(*) from d))::text, 1
) z order by o;
