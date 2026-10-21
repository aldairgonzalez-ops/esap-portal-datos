-- Esquema sintético que imita la estructura ESAP (solo para probar el pipeline)
create schema auth; create schema academic_registration; create schema certification;
create schema legal_management; create schema control_interno; create schema notifications; create schema audit;

create table auth.users(id bigserial primary key, email varchar(150) not null unique, document_number varchar(20),
  first_name varchar(80), last_name varchar(80), phone varchar(20), is_active boolean default true,
  created_at timestamptz default now());
comment on table auth.users is 'Usuarios del sistema con acceso a la SuperApp';
comment on column auth.users.email is 'Correo electrónico institucional o personal del usuario';
create table auth.roles(id serial primary key, name varchar(50) not null unique, description text);
create table auth.user_roles(user_id bigint not null references auth.users(id), role_id int not null references auth.roles(id), primary key(user_id, role_id));

create table academic_registration.students(id bigserial primary key, user_id bigint, email varchar(150), document_number varchar(20),
  birth_date date, program_code varchar(20), status varchar(20) default 'ACTIVO', created_at timestamptz default now());
create index on academic_registration.students(user_id);
create table academic_registration.programs(code varchar(20) primary key, name varchar(200) not null, faculty varchar(100));
create table academic_registration.enrollments(id bigserial primary key, student_id bigint not null references academic_registration.students(id),
  period varchar(10) not null, program_code varchar(20) references academic_registration.programs(code), enrolled_at date);

create table certification.certificates(id bigserial primary key, email varchar(150), full_name varchar(200), certificate_type varchar(50),
  issued_at timestamptz, file_url text);
create table certification.certificates_bkp_20260501 as select * from certification.certificates;

create table legal_management.lawyers(id bigserial primary key, user_id bigint references auth.users(id), email varchar(150), professional_card varchar(30));
create table legal_management.cases(id bigserial primary key, lawyer_id bigint references legal_management.lawyers(id), case_number varchar(50), opened_at date, status varchar(20));

create table control_interno.audits_plan(id serial primary key, year int, description text);
create table control_interno.findings(id serial primary key, audit_plan_id int, severity varchar(10), description text);
create table control_interno.followups(audit_finding_id int, note text, created_at timestamptz);

create table notifications.messages(id bigserial primary key, recipient_email varchar(150), subject varchar(200), body text, sent_at timestamptz);

create table audit.log(id bigserial primary key, schema_name text, table_name text, operation char(1), changed_by bigint, changed_at timestamptz default now(), payload jsonb);

create function audit.fn_log() returns trigger language plpgsql as $$
begin insert into audit.log(schema_name, table_name, operation, payload) values (TG_TABLE_SCHEMA, TG_TABLE_NAME, left(TG_OP,1), to_jsonb(NEW)); return NEW; end $$;
create trigger trg_users_audit after insert or update on auth.users for each row execute function audit.fn_log();
create function academic_registration.get_student_by_email(p_email text) returns setof academic_registration.students language sql as $$ select * from academic_registration.students where email = p_email $$;
create procedure certification.sp_issue_certificate(p_email text, p_type text) language plpgsql as $$ begin insert into certification.certificates(email, certificate_type, issued_at) values (p_email, p_type, now()); end $$;
create view academic_registration.vw_students_active as select s.id, s.email, p.name as program from academic_registration.students s join academic_registration.programs p on p.code = s.program_code where s.status = 'ACTIVO';

insert into auth.roles(name) values ('ESTUDIANTE'),('ABOGADO'),('ADMIN');
insert into auth.users(email, document_number, first_name, last_name) select 'user'||g||'@esap.test', (1000000+g)::text, 'N'||g, 'A'||g from generate_series(1,500) g;
insert into auth.user_roles select id, 1 from auth.users where id <= 400;
insert into academic_registration.programs values ('ADP','Administración Pública','FAC1'),('ESP','Especialización Gestión','FAC2');
insert into academic_registration.students(user_id, email, document_number, program_code) select g, 'user'||g||'@esap.test', (1000000+g)::text, case when g%2=0 then 'ADP' else 'ESP' end from generate_series(1,400) g;
insert into academic_registration.students(user_id, email, document_number, program_code) select null, 'externo'||g||'@mail.test', (2000000+g)::text, 'ADP' from generate_series(1,50) g;
insert into academic_registration.enrollments(student_id, period, program_code) select id, '2026-1', program_code from academic_registration.students;
insert into certification.certificates(email, full_name, certificate_type, issued_at) select 'user'||g||'@esap.test', 'N A', 'NOTAS', now() from generate_series(1,700) g;
insert into legal_management.lawyers(user_id, email) select g, 'user'||g||'@esap.test' from generate_series(401,420) g;
insert into legal_management.cases(lawyer_id, case_number) select (g%20)+1, 'C-'||g from generate_series(1,60) g;
insert into notifications.messages(recipient_email, subject) select 'user'||g||'@esap.test', 'Hola' from generate_series(1,300) g;
analyze;
create table auth.sedes(id_sede bigint primary key, nom_sede varchar(50) not null, email_sede varchar(100));
create table auth.personas(num_identificacion varchar(30) not null, tip_identificacion varchar(6) not null, nom_tercero varchar(250) not null,
  pri_apellido varchar(250), fec_nacimiento date, dir_email varchar(100), tel_celular varchar(20), id_sede bigint references auth.sedes(id_sede),
  id_person uuid default gen_random_uuid() not null unique);
create table academic_registration.inscripciones(id bigserial primary key, id_sede bigint, num_identificacion varchar(30), dir_email varchar(100), programa_id bigint);
insert into auth.sedes values (1,'Bogotá','bogota@esap.test'),(2,'Medellín','med@esap.test');
insert into auth.personas(num_identificacion, tip_identificacion, nom_tercero, dir_email, id_sede) select (1000000+g)::text,'CC','N'||g,'user'||g||'@esap.test', 1+g%2 from generate_series(1,450) g;
insert into academic_registration.inscripciones(id_sede, num_identificacion, dir_email) select case when g%10=0 then 9 else 1 end, (1000000+g)::text, case when g%3=0 then 'otro'||g||'@mail.test' else 'user'||g||'@esap.test' end from generate_series(1,600) g;
analyze;
