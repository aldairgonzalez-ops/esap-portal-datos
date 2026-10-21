-- 11 · Cardinalidad medida con datos para cada FK de una sola columna (solo conteos, ningún valor).
-- filas/nn: filas y filas con valor en la tabla hija · dist: padres distintos referenciados
-- maxh: máximo de hijos por padre · padres: filas de la tabla padre · huerf: valores sin padre (FK no validadas)
with fk as (
  select n.nspname as s, c.relname as t, k.conname as n, a.attname as col, a.attnotnull as obligatoria,
         rn.nspname as rs, rc.relname as rt, ra.attname as rcol
  from pg_constraint k
  join pg_class c on c.oid = k.conrelid join pg_namespace n on n.oid = c.relnamespace
  join pg_class rc on rc.oid = k.confrelid join pg_namespace rn on rn.oid = rc.relnamespace
  join pg_attribute a on a.attrelid = k.conrelid and a.attnum = k.conkey[1]
  join pg_attribute ra on ra.attrelid = k.confrelid and ra.attnum = k.confkey[1]
  where k.contype = 'f' and array_length(k.conkey, 1) = 1
    and n.nspname not in ('pg_catalog', 'information_schema')
), m as (
  select fk.*, query_to_xml(format(
    'select (select count(*) from %1$I.%2$I) as filas,
            (select count(%3$I) from %1$I.%2$I) as nn,
            (select count(distinct %3$I) from %1$I.%2$I) as dist,
            (select coalesce(max(k), 0) from (select count(*) as k from %1$I.%2$I where %3$I is not null group by %3$I) g) as maxh,
            (select count(*) from %4$I.%5$I) as padres,
            (select count(*) from %1$I.%2$I c where c.%3$I is not null
               and not exists (select 1 from %4$I.%5$I p where p.%6$I = c.%3$I)) as huerf',
    fk.s, fk.t, fk.col, fk.rs, fk.rt, fk.rcol), false, true, '') as x
  from fk
), d as (
  select s, t, n, col, obligatoria, rs, rt, rcol,
         (xpath('/row/filas/text()', x))[1]::text::bigint as filas,
         (xpath('/row/nn/text()', x))[1]::text::bigint as nn,
         (xpath('/row/dist/text()', x))[1]::text::bigint as dist,
         (xpath('/row/maxh/text()', x))[1]::text::bigint as maxh,
         (xpath('/row/padres/text()', x))[1]::text::bigint as padres,
         (xpath('/row/huerf/text()', x))[1]::text::bigint as huerf
  from m
)
select x from (
  select row_to_json(r)::text as x, 0 as o from (select * from d order by s, t, n) r
  union all select json_build_object('_fin', (select count(*) from d))::text, 1
) z order by o;
