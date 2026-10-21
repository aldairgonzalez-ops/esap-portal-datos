/* =====================================================================================
   EXTRACCIÓN DEL CATÁLOGO DE LA BASE ESAP (QA) PARA EL PORTAL DE DATOS
   SOLO LECTURA: todo corre dentro de una transacción READ ONLY. Ninguna consulta escribe.
   No extrae valores de datos: solo estructura, estadísticas y conteos.

   Se lanza con herramientas/extraer.py, que fija las variables:
     salida         carpeta relativa de salida, con barras "/" (ej. extracciones/2026-10-21)
     bd_esperada    nombre de la base que debe estar conectada (guarda contra conectarse a DEV)
     maestro_email  fuente maestra del correo      (esquema.tabla.columna)
     maestro_doc    fuente maestra del documento   (esquema.tabla.columna)
     srv_esperado   (opcional) IP que debe reportar el servidor; '' para no comprobar
   ===================================================================================== */
\set ON_ERROR_STOP on
\set QUIET on
\pset pager off
\pset format unaligned
\pset tuples_only on
\pset footer off
set client_encoding = 'UTF8';
begin transaction isolation level repeatable read read only;
set local statement_timeout = '20min';
set local lock_timeout = '5s';

select current_database() = :'bd_esperada' as es_la_base_esperada \gset
\if :es_la_base_esperada
  select coalesce(host(inet_server_addr()), 'socket local') as srv, coalesce(inet_server_port()::text, '-') as puerto,
         split_part(version(), ' ', 2) as motor, current_user as usr \gset
  \echo 'OK: conectado a' :'bd_esperada' 'en' :'srv' 'puerto' :'puerto' '· PostgreSQL' :'motor' '· usuario' :'usr'
  \if :{?srv_esperado}
    select :'srv_esperado' = '' or :'srv_esperado' = :'srv' as es_el_servidor_esperado \gset
    \if :es_el_servidor_esperado
    \else
      \echo 'ALTO: el servidor es' :'srv' 'y se esperaba' :'srv_esperado' '(QA). No se extrae nada.'
      do $$ begin raise exception 'Servidor distinto del esperado: extracción detenida'; end $$;
    \endif
  \else
    \echo '    Confirma que ese servidor es el de QA (no DEV) antes de usar la extracción.'
  \endif
\else
  \echo 'ALTO: la base conectada no es' :'bd_esperada' '. No se extrae nada.'
  do $$ begin raise exception 'Base distinta de la esperada: extracción detenida'; end $$;
\endif

\set f :salida/00_contexto.jsonl
\o :f
\ir 00_contexto.sql
\set f :salida/01_esquemas.jsonl
\o :f
\ir 01_esquemas.sql
\set f :salida/02_tablas.jsonl
\o :f
\ir 02_tablas.sql
\set f :salida/03_columnas.jsonl
\o :f
\ir 03_columnas.sql
\set f :salida/04_restricciones.jsonl
\o :f
\ir 04_restricciones.sql
\set f :salida/05_indices.jsonl
\o :f
\ir 05_indices.sql
\set f :salida/06_programables.jsonl
\o :f
\ir 06_programables.sql
\set f :salida/07_triggers.jsonl
\o :f
\ir 07_triggers.sql
\set f :salida/08_vistas.jsonl
\o :f
\ir 08_vistas.sql
\set f :salida/09_tipos.jsonl
\o :f
\ir 09_tipos.sql
\o
\echo '... catálogo listo; contando filas y midiendo relaciones (puede tardar unos minutos)'
\set f :salida/10_conteo_filas.jsonl
\o :f
\ir 10_conteo_filas.sql
\set f :salida/11_cardinalidad_fk.jsonl
\o :f
\ir 11_cardinalidad_fk.sql
\set f :salida/12_relaciones_implicitas.jsonl
\o :f
\ir 12_relaciones_implicitas.sql
\set f :salida/13_identidad.jsonl
\o :f
\ir 13_identidad.sql
\o
rollback;
\echo 'OK: extracción completa en' :'salida'
