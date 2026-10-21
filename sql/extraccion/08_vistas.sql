-- 08 · Vistas y vistas materializadas: definición y tablas de las que dependen.
with dep as (
  select distinct v.oid as vid, rn.nspname || '.' || rc.relname as ref
  from pg_class v
  join pg_rewrite r on r.ev_class = v.oid
  join pg_depend dp on dp.objid = r.oid and dp.classid = 'pg_rewrite'::regclass and dp.refclassid = 'pg_class'::regclass
  join pg_class rc on rc.oid = dp.refobjid and rc.oid <> v.oid
  join pg_namespace rn on rn.oid = rc.relnamespace
  where v.relkind in ('v', 'm')
), d as (
  select n.nspname as s, v.relname as t, v.relkind as k,
         pg_get_viewdef(v.oid, true) as def,
         array(select ref from dep where dep.vid = v.oid order by ref) as usa
  from pg_class v
  join pg_namespace n on n.oid = v.relnamespace
  where v.relkind in ('v', 'm')
    and n.nspname not in ('pg_catalog', 'information_schema')
)
select x from (
  select row_to_json(r)::text as x, 0 as o from (select * from d order by s, t) r
  union all select json_build_object('_fin', (select count(*) from d))::text, 1
) z order by o;
