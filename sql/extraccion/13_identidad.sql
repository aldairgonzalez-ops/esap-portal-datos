-- 13 · Identidad replicada: columnas de correo y de documento de identidad en todos los esquemas,
-- comparadas con la fuente maestra (por defecto auth.personas.dir_email y auth.personas.num_identificacion).
-- Solo conteos: valores no nulos, distintos, cuántos existen en la fuente maestra y cuántos no.
-- Variables psql (se pueden cambiar al lanzar): maestro_email, maestro_doc  (formato esquema.tabla.columna)
with maestro as (
  select 'email' as tipo, split_part(:'maestro_email', '.', 1) as s, split_part(:'maestro_email', '.', 2) as t, split_part(:'maestro_email', '.', 3) as col
  union all
  select 'documento', split_part(:'maestro_doc', '.', 1), split_part(:'maestro_doc', '.', 2), split_part(:'maestro_doc', '.', 3)
), existe as (
  select m.* from maestro m
  join pg_namespace n on n.nspname = m.s
  join pg_class c on c.relnamespace = n.oid and c.relname = m.t
  join pg_attribute a on a.attrelid = c.oid and a.attname = m.col and not a.attisdropped
), cols as (
  select n.nspname as s, c.relname as t, a.attname as col,
         case when a.attname ~* '(^|_)(e_?mail|correo)' then 'email' else 'documento' end as tipo
  from pg_attribute a
  join pg_class c on c.oid = a.attrelid join pg_namespace n on n.oid = c.relnamespace
  join pg_type ty on ty.oid = a.atttypid
  where a.attnum > 0 and not a.attisdropped and c.relkind in ('r', 'p')
    and ty.typcategory = 'S'
    and n.nspname not in ('pg_catalog', 'information_schema', 'pg_toast')
    and (a.attname ~* '(^|_)(e_?mail|correo)'
         or a.attname ~* '(num_identificacion|identificacion|document_number|num_documento|nro_documento|numero_documento|documento|cedula|dni)')
    and a.attname !~* '^(tip|tipo|type)_'
), m as (
  select c.*, (c.s = e.s and c.t = e.t and c.col = e.col) as es_maestro,
         e.s as ms, e.t as mt, e.col as mcol,
         query_to_xml(format(
           'select count(%3$I) as nn, count(distinct lower(trim(%3$I))) as dist,
                   (select count(*) from (select distinct lower(trim(c.%3$I)) v from %1$I.%2$I c where c.%3$I is not null) u
                     where exists (select 1 from %4$I.%5$I p where lower(trim(p.%6$I)) = u.v)) as en_maestro
              from %1$I.%2$I', c.s, c.t, c.col, e.s, e.t, e.col), false, true, '') as x
  from cols c join existe e on e.tipo = c.tipo
), d as (
  select tipo, s, t, col, es_maestro, ms || '.' || mt || '.' || mcol as maestro,
         (xpath('/row/nn/text()', x))[1]::text::bigint as nn,
         (xpath('/row/dist/text()', x))[1]::text::bigint as dist,
         (xpath('/row/en_maestro/text()', x))[1]::text::bigint as en_maestro
  from m
)
select x from (
  select row_to_json(r)::text as x, 0 as o from (select * from d order by tipo, s, t, col) r
  union all select json_build_object('_fin', (select count(*) from d))::text, 1
) z order by o;
