-- 12 · Relaciones implícitas: columnas que por su nombre apuntan a la clave de otra tabla pero no tienen FK.
-- Reglas (la tabla destino debe tener PK o UNIQUE de una columna y tipo de la misma categoría):
--   Solo se evalúan columnas con forma de clave: id_X, X_id, cod_X, X_code, X_codigo.
--   R1  la columna se llama igual que la clave de otra tabla           (id_sede -> sedes.id_sede)
--   R2  existe la tabla X, Xs o Xes con clave id/id_X (o code/codigo/cod_X) (programa_id -> programas.id)
-- Se valida con datos: cuántos valores encuentran a su padre y cuántos no (solo conteos).
with claves as (
  select n.nspname as s, c.relname as t, a.attname as col, a.atttypid as typ
  from pg_constraint k
  join pg_class c on c.oid = k.conrelid join pg_namespace n on n.oid = c.relnamespace
  join pg_attribute a on a.attrelid = k.conrelid and a.attnum = k.conkey[1]
  where k.contype in ('p', 'u') and array_length(k.conkey, 1) = 1
    and c.relkind in ('r', 'p') and n.nspname not in ('pg_catalog', 'information_schema')
), con_fk as (
  select k.conrelid, k.conkey[1] as attnum from pg_constraint k where k.contype = 'f' and array_length(k.conkey, 1) = 1
), cols as (
  select n.nspname as s, c.relname as t, a.attname as col, a.atttypid as typ,
         case when a.attname ~ '^id_.+' then substr(a.attname, 4)
              when a.attname ~ '.+_id$' then left(a.attname, -3)
              when a.attname ~ '^cod_.+' then substr(a.attname, 5)
              when a.attname ~ '.+_code$' then left(a.attname, -5)
              when a.attname ~ '.+_codigo$' then left(a.attname, -7) end as base,
         case when a.attname ~ '^id_.+|.+_id$' then 'id' else 'cod' end as forma
  from pg_attribute a
  join pg_class c on c.oid = a.attrelid join pg_namespace n on n.oid = c.relnamespace
  where a.attnum > 0 and not a.attisdropped and c.relkind in ('r', 'p')
    and n.nspname not in ('pg_catalog', 'information_schema', 'pg_toast')
    and a.attname ~ '^(id|cod)_.+|.+_(id|code|codigo)$'
    and not exists (select 1 from con_fk f where f.conrelid = c.oid and f.attnum = a.attnum)
    and not exists (select 1 from pg_constraint k where k.conrelid = c.oid and k.contype = 'p'
                    and array_length(k.conkey, 1) = 1 and k.conkey[1] = a.attnum)
), cand as (
  select distinct on (c.s, c.t, c.col, k.s, k.t)
         c.s, c.t, c.col, k.s as rs, k.t as rt, k.col as rcol,
         case when c.col = k.col then 'R1' else 'R2' end as regla,
         (c.s = k.s) as mismo_esquema
  from cols c
  join claves k on not (k.s = c.s and k.t = c.t)
   and (select t1.typcategory from pg_type t1 where t1.oid = c.typ) = (select t2.typcategory from pg_type t2 where t2.oid = k.typ)
   and (c.col = k.col
        or (k.t in (c.base, c.base || 's', c.base || 'es')
            and ((c.forma = 'id'  and k.col in ('id', 'id_' || c.base))
              or (c.forma = 'cod' and k.col in ('code', 'codigo', 'cod_' || c.base)))))
  order by c.s, c.t, c.col, k.s, k.t, (c.col = k.col) desc
), m as (
  select cand.*, query_to_xml(format(
    'select count(%3$I) as nn,
            count(*) filter (where %3$I is not null and exists (select 1 from %4$I.%5$I p where p.%6$I = c.%3$I)) as ok
       from %1$I.%2$I c', cand.s, cand.t, cand.col, cand.rs, cand.rt, cand.rcol), false, true, '') as x
  from cand
), d as (
  select s, t, col, rs, rt, rcol, regla, mismo_esquema,
         (xpath('/row/nn/text()', x))[1]::text::bigint as nn,
         (xpath('/row/ok/text()', x))[1]::text::bigint as ok
  from m
)
select x from (
  select row_to_json(r)::text as x, 0 as o from (select * from d order by s, t, col, rs, rt) r
  union all select json_build_object('_fin', (select count(*) from d))::text, 1
) z order by o;
