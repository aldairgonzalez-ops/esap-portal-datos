-- 04 · Restricciones: p=PK, u=única, f=FK, c=check, x=exclusión.
-- Para FK: tabla y columnas referenciadas, acciones y si está validada.
with d as (
  select n.nspname as s, c.relname as t, k.conname as n, k.contype as ty,
         array(select a.attname from unnest(k.conkey) with ordinality u(num, i)
               join pg_attribute a on a.attrelid = k.conrelid and a.attnum = u.num order by u.i) as cols,
         rn.nspname as rs, rc.relname as rt,
         array(select a.attname from unnest(k.confkey) with ordinality u(num, i)
               join pg_attribute a on a.attrelid = k.confrelid and a.attnum = u.num order by u.i) as rcols,
         nullif(k.confupdtype, ' ') as on_upd, nullif(k.confdeltype, ' ') as on_del,
         k.convalidated as validada, k.condeferrable as diferible,
         pg_get_constraintdef(k.oid) as def
  from pg_constraint k
  join pg_class c on c.oid = k.conrelid
  join pg_namespace n on n.oid = c.relnamespace
  left join pg_class rc on rc.oid = k.confrelid
  left join pg_namespace rn on rn.oid = rc.relnamespace
  where k.contype in ('p', 'u', 'f', 'c', 'x')
    and n.nspname not in ('pg_catalog', 'information_schema', 'pg_toast')
)
select x from (
  select row_to_json(r)::text as x, 0 as o from (select * from d order by s, t, n) r
  union all select json_build_object('_fin', (select count(*) from d))::text, 1
) z order by o;
