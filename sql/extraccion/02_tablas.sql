-- 02 · Tablas, vistas, vistas materializadas y tablas foráneas/particionadas.
-- k: r=tabla, p=particionada, v=vista, m=vista materializada, f=foránea.
-- est = filas estimadas por el planificador (reltuples; -1 si nunca se analizó).
with d as (
  select n.nspname as s, c.relname as t, c.relkind as k,
         obj_description(c.oid, 'pg_class') as d,
         c.reltuples::bigint as est,
         st.n_live_tup as vivas,
         pg_total_relation_size(c.oid) as bytes,
         c.relispartition as particion,
         exists (select 1 from pg_constraint p where p.conrelid = c.oid and p.contype = 'p') as pk,
         pg_get_userbyid(c.relowner) as owner,
         greatest(st.last_analyze, st.last_autoanalyze) as analizada,
         st.n_tup_ins as ins, st.n_tup_upd as upd, st.n_tup_del as del,
         st.seq_scan as seq_scan, st.idx_scan as idx_scan
  from pg_class c
  join pg_namespace n on n.oid = c.relnamespace
  left join pg_stat_user_tables st on st.relid = c.oid
  where c.relkind in ('r', 'p', 'v', 'm', 'f')
    and n.nspname not in ('pg_catalog', 'information_schema', 'pg_toast')
    and n.nspname not like 'pg_temp_%'
)
select x from (
  select row_to_json(r)::text as x, 0 as o from (select * from d order by s, t) r
  union all select json_build_object('_fin', (select count(*) from d))::text, 1
) z order by o;
