-- 03 · Columnas con tipo, nulabilidad, valor por defecto y comentario.
-- nf (fracción de nulos) y nd (n_distinct) salen de pg_stats: son estadísticas, no valores.
-- No se extraen valores frecuentes ni histogramas para no exponer datos personales.
with d as (
  select n.nspname as s, c.relname as t, a.attnum as o, a.attname as c,
         format_type(a.atttypid, a.atttypmod) as ty,
         not a.attnotnull as nul,
         pg_get_expr(ad.adbin, ad.adrelid) as def,
         col_description(c.oid, a.attnum) as d,
         nullif(a.attidentity, '') as ident,
         nullif(a.attgenerated, '') as gen,
         ps.null_frac as nf, ps.n_distinct as nd, ps.avg_width as aw
  from pg_attribute a
  join pg_class c on c.oid = a.attrelid
  join pg_namespace n on n.oid = c.relnamespace
  left join pg_attrdef ad on ad.adrelid = a.attrelid and ad.adnum = a.attnum
  left join pg_stats ps on ps.schemaname = n.nspname and ps.tablename = c.relname and ps.attname = a.attname
  where a.attnum > 0 and not a.attisdropped
    and c.relkind in ('r', 'p', 'v', 'm', 'f')
    and n.nspname not in ('pg_catalog', 'information_schema', 'pg_toast')
    and n.nspname not like 'pg_temp_%'
)
select x from (
  select row_to_json(r)::text as x, 0 as o from (select * from d order by s, t, o) r
  union all select json_build_object('_fin', (select count(*) from d))::text, 1
) z order by o;
