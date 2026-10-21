-- 07 · Triggers de usuario con la función que ejecutan y su estado (O=activo, D=deshabilitado).
with d as (
  select n.nspname as s, c.relname as t, g.tgname as n,
         fn.nspname as fs, f.proname as fn, g.tgenabled as estado,
         pg_get_triggerdef(g.oid) as def
  from pg_trigger g
  join pg_class c on c.oid = g.tgrelid
  join pg_namespace n on n.oid = c.relnamespace
  join pg_proc f on f.oid = g.tgfoid
  join pg_namespace fn on fn.oid = f.pronamespace
  where not g.tgisinternal
    and n.nspname not in ('pg_catalog', 'information_schema')
)
select x from (
  select row_to_json(r)::text as x, 0 as o from (select * from d order by s, t, n) r
  union all select json_build_object('_fin', (select count(*) from d))::text, 1
) z order by o;
