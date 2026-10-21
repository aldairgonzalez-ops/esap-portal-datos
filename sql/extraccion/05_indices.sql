-- 05 · Índices con su definición, columnas, tamaño y uso desde el último reinicio de estadísticas.
with d as (
  select n.nspname as s, t.relname as t, i.relname as n,
         x.indisunique as uni, x.indisprimary as pk,
         array(select a.attname from unnest(x.indkey) with ordinality u(num, o)
               join pg_attribute a on a.attrelid = x.indrelid and a.attnum = u.num order by u.o) as cols,
         pg_get_indexdef(x.indexrelid) as def,
         pg_relation_size(x.indexrelid) as bytes,
         su.idx_scan as usos
  from pg_index x
  join pg_class i on i.oid = x.indexrelid
  join pg_class t on t.oid = x.indrelid
  join pg_namespace n on n.oid = t.relnamespace
  left join pg_stat_user_indexes su on su.indexrelid = x.indexrelid
  where n.nspname not in ('pg_catalog', 'information_schema', 'pg_toast')
)
select x from (
  select row_to_json(r)::text as x, 0 as o from (select * from d order by s, t, n) r
  union all select json_build_object('_fin', (select count(*) from d))::text, 1
) z order by o;
