-- 09 · Tipos enumerados definidos por el usuario y sus valores (dominios de valores).
with d as (
  select n.nspname as s, t.typname as n,
         array(select e.enumlabel from pg_enum e where e.enumtypid = t.oid order by e.enumsortorder) as vals,
         obj_description(t.oid, 'pg_type') as d
  from pg_type t
  join pg_namespace n on n.oid = t.typnamespace
  where t.typtype = 'e'
    and n.nspname not in ('pg_catalog', 'information_schema')
)
select x from (
  select row_to_json(r)::text as x, 0 as o from (select * from d order by s, n) r
  union all select json_build_object('_fin', (select count(*) from d))::text, 1
) z order by o;
