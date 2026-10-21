-- 10 · Conteo EXACTO de filas por tabla (count(*) vía query_to_xml, sin escribir nada).
-- Es la consulta más pesada de la extracción; en una base de ~160 tablas toma segundos o pocos minutos.
with d as (
  select n.nspname as s, c.relname as t,
         (xpath('/row/n/text()',
                query_to_xml(format('select count(*) as n from %I.%I', n.nspname, c.relname), false, true, '')))[1]::text::bigint as filas
  from pg_class c
  join pg_namespace n on n.oid = c.relnamespace
  where c.relkind in ('r', 'p', 'm', 'f') and not c.relispartition
    and n.nspname not in ('pg_catalog', 'information_schema', 'pg_toast')
    and n.nspname not like 'pg_temp_%'
)
select x from (
  select row_to_json(r)::text as x, 0 as o from (select * from d order by s, t) r
  union all select json_build_object('_fin', (select count(*) from d))::text, 1
) z order by o;
