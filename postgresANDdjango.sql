
/*
Creacion de tipos de retorno
*/
CREATE TYPE custom_type AS
   (id integer,
    hora_ini time,
    hora_fin  time,
    frecuencia integer,
    dia_id integer,
    medico_id integer);
ALTER TYPE custom_type 
  OWNER TO postgres;



/*
Primer SP con excepciones
Listado de Agendas Segun El Medico
*/
DROP FUNCTION listadoagendas(integer);
CREATE OR REPLACE FUNCTION listadoAgendas(idmedico integer)
RETURNS SETOF RECORD
AS $BODY$
BEGIN
	RETURN QUERY
    SELECT AG.ID,AG.HORA_INI,AG.HORA_FIN,AG.FRECUENCIA,AD.DIA 
    FROM AGENDAS_AGENDA AG INNER JOIN AGENDAS_DIA AD ON AG.DIA_ID=AD.ID 
    WHERE AG.MEDICO_ID = idmedico;
    IF NOT FOUND THEN
        RAISE EXCEPTION 'El Medico % no tiene Agendas  Asignadas.', $1;
    END IF;
END;
$BODY$ 
LANGUAGE plpgsql;

select * from listadoAgendas(1) as t (id integer,hora_ini time,hora_fin time,frecuencia integer,dia varchar(50));


/*
Primer SP con excepciones
*/




/*
Segundo SP con excepciones
Listado de Medicos Segun la Especialidad
*/

DROP FUNCTION Especialidad_Medicos(integer);
CREATE OR REPLACE FUNCTION Especialidad_Medicos (idespecialidad integer)
RETURNS SETOF RECORD
AS $BODY$
BEGIN
	RETURN QUERY 
	SELECT medicos_medico.id, medicos_medico.empresa, medicos_medico.descripcion, medicos_medico.usuario_id,  usuarios_usuario.nombre1, usuarios_usuario.direccion  
	FROM medicos_medico INNER JOIN usuarios_usuario ON ( medicos_medico.usuario_id = usuarios_usuario.id ) 
	WHERE medicos_medico.especialidad_id = idespecialidad;
	IF NOT FOUND THEN
        RAISE EXCEPTION 'No existe la Especialidad %.', $1;
    END IF;
END;
$BODY$ 
LANGUAGE plpgsql;

select * from Especialidad_Medicos(5) as t (id integer,empresa varchar(50),descripcion text,id_usuario integer,nombre varchar(100),direccion varchar);
/*
Segundo SP con excepciones
*/



/*
Tercer SP con excepciones
Listado de Medicos Segun la Especialidad
*/
DROP FUNCTION Medico_Agenda(integer,varchar);
CREATE OR REPLACE FUNCTION Medico_Agenda(idmedico integer, nom_dia varchar)
RETURNS SETOF RECORD
AS $BODY$
BEGIN
	RETURN QUERY 
    SELECT AG.ID,AG.HORA_INI,AG.HORA_FIN,AG.FRECUENCIA,AD.DIA 
    FROM AGENDAS_AGENDA AG INNER JOIN AGENDAS_DIA AD ON AG.DIA_ID=AD.ID 
    WHERE AG.MEDICO_ID = idmedico AND LOWER(AD.DIA)=LOWER(nom_dia);
	IF NOT FOUND THEN
        RAISE EXCEPTION 'No se encontraron datos %.', $1;
    END IF;
END;
$BODY$ 
LANGUAGE plpgsql;
select * from Medico_Agenda(1,'LuNeS') as t (id integer,hora_ini time,hora_fin time,frecuencia integer,dia varchar(50));
/*
Tercer SP con excepciones
*/




/*
CUARTO SP con excepciones
*/
DROP FUNCTION Citas_paciente(integer);
CREATE OR REPLACE FUNCTION Citas_paciente(idpaciente integer)
RETURNS SETOF RECORD
AS $BODY$
BEGIN
    RETURN QUERY 
    SELECT C.HORA_CITA,C.FECHA,AD.DIA,U.NOMBRE1,U.APELLIDO1 as nombrecompleto,E.NOMBRE
    FROM citas_cita C INNER JOIN AGENDAS_AGENDA A ON C.agenda_id=A.ID
    INNER JOIN AGENDAS_DIA AD ON A.dia_id=AD.ID
    INNER JOIN medicos_medico M ON A.medico_id=M.ID
    INNER JOIN usuarios_usuario U ON M.usuario_id=U.ID
    INNER JOIN medicos_especialidad E ON M.especialidad_id=E.ID
    WHERE C.paciente_id=idpaciente and C.ESTADO=2;
    IF NOT FOUND THEN
        RAISE EXCEPTION 'No se encontraron datos %.', $1;
    END IF;
END;
$BODY$ 
LANGUAGE plpgsql;
select * from Citas_paciente(1) as t (HORA_CITA time,FECHA date,DIA varchar(50),nombre1 varchar(100),apellido1 varchar(100),especialidad varchar(50));
/*
CUARTO SP con excepciones
*/



/*
QUINTO SP con excepciones
*/
DROP FUNCTION citas_ocupadas(date);
CREATE OR REPLACE FUNCTION citas_ocupadas(fecha_sel date)
RETURNS SETOF RECORD
AS $BODY$
BEGIN
    RETURN QUERY 
   select HORA_CITA from citas_cita c where c.FECHA=fecha_sel;
    IF NOT FOUND THEN
        RAISE EXCEPTION 'No se encontraron datos %.', $1;
    END IF;
END;
$BODY$ 
LANGUAGE plpgsql;
select * from citas_ocupadas('16/10/2015') as t (HORA_CITA time);
/*
QUINTO SP con excepciones
*/



/*
SEXTO SP con excepciones
*/
DROP FUNCTION Citas_paciente_sin_asignar(integer);
CREATE OR REPLACE FUNCTION Citas_paciente_sin_asignar(idpaciente integer)
RETURNS SETOF RECORD
AS $BODY$
BEGIN
    RETURN QUERY 
    SELECT C.HORA_CITA,C.FECHA,AD.DIA,U.NOMBRE1,U.APELLIDO1 as nombrecompleto,E.NOMBRE
    FROM citas_cita C INNER JOIN AGENDAS_AGENDA A ON C.agenda_id=A.ID
    INNER JOIN AGENDAS_DIA AD ON A.dia_id=AD.ID
    INNER JOIN medicos_medico M ON A.medico_id=M.ID
    INNER JOIN usuarios_usuario U ON M.usuario_id=U.ID
    INNER JOIN medicos_especialidad E ON M.especialidad_id=E.ID
    WHERE C.paciente_id=idpaciente and C.ESTADO=0;
    IF NOT FOUND THEN
        RAISE EXCEPTION 'No se encontraron datos %.', $1;
    END IF;
END;
$BODY$ 
LANGUAGE plpgsql;
select * from Citas_paciente_sin_asignar(1) as t (HORA_CITA time,FECHA date,DIA varchar(50),nombre1 varchar(100),apellido1 varchar(100),especialidad varchar(50));
/*
SEXTO SP con excepciones
*/




/*
Septimo SP con excepciones
*/
DROP FUNCTION Citas_paciente_pendientes(integer);
CREATE OR REPLACE FUNCTION Citas_paciente_pendientes(idpaciente integer)
RETURNS SETOF RECORD
AS $BODY$
BEGIN
    RETURN QUERY 
    SELECT C.ID,C.HORA_CITA,C.FECHA,AD.DIA,U.NOMBRE1,U.APELLIDO1 as nombrecompleto,E.NOMBRE
    FROM citas_cita C INNER JOIN AGENDAS_AGENDA A ON C.agenda_id=A.ID
    INNER JOIN AGENDAS_DIA AD ON A.dia_id=AD.ID
    INNER JOIN medicos_medico M ON A.medico_id=M.ID
    INNER JOIN usuarios_usuario U ON M.usuario_id=U.ID
    INNER JOIN medicos_especialidad E ON M.especialidad_id=E.ID
    WHERE C.paciente_id=idpaciente and C.ESTADO=1 AND C.fecha>=NOW();
    IF NOT FOUND THEN
        RAISE EXCEPTION 'No se encontraron datos %.', $1;
    END IF;
END;
$BODY$ 
LANGUAGE plpgsql;
select * from Citas_paciente_pendientes(1) as t (ID integer,HORA_CITA time,FECHA date,DIA varchar(50),nombre1 varchar(100),apellido1 varchar(100),especialidad varchar(50));
/*
Septimo SP con excepciones
*/




/*
Octavo SP con excepciones
*/
DROP FUNCTION Citas_historial_medico(integer);
CREATE OR REPLACE FUNCTION Citas_historial_medico(idmedico integer)
RETURNS SETOF RECORD
AS $BODY$
BEGIN
    RETURN QUERY 
    SELECT C.HORA_CITA,C.FECHA,AD.DIA,U.NOMBRE1,U.APELLIDO1,U.IDENTIFICACION
    FROM citas_cita C INNER JOIN AGENDAS_AGENDA A ON C.agenda_id=A.ID
    INNER JOIN AGENDAS_DIA AD ON A.dia_id=AD.ID
    INNER JOIN pacientes_paciente P ON P.id=C.paciente_id
    INNER JOIN usuarios_usuario U ON P.usuario_id=U.ID
    WHERE A.medico_id=idmedico and C.ESTADO=2;
    IF NOT FOUND THEN
        RAISE EXCEPTION 'No se encontraron datos %.', $1;
    END IF;
END;
$BODY$ 
LANGUAGE plpgsql;
select * from Citas_historial_medico(1) as t (HORA_CITA time,FECHA date,DIA varchar(50),nombre1 varchar(100),apellido1 varchar(100),identificacion varchar(20));
/*
Octavo SP con excepciones
*/




/*
Noveno SP con excepciones
*/
DROP FUNCTION Citas_listado_paciente(integer,varchar(20));
CREATE OR REPLACE FUNCTION Citas_listado_paciente(idmedico integer,identi varchar(20))
RETURNS SETOF RECORD
AS $BODY$
BEGIN
    RETURN QUERY 
    SELECT C.ID,C.HORA_CITA,C.FECHA,AD.DIA,U.NOMBRE1,U.APELLIDO1,U.IDENTIFICACION
    FROM citas_cita C INNER JOIN AGENDAS_AGENDA A ON C.agenda_id=A.ID
    INNER JOIN AGENDAS_DIA AD ON A.dia_id=AD.ID
    INNER JOIN pacientes_paciente P ON P.id=C.paciente_id
    INNER JOIN usuarios_usuario U ON P.usuario_id=U.ID
    WHERE A.medico_id=idmedico and C.ESTADO=1 and C.fecha>=NOW() and U.IDENTIFICACION=identi;
    IF NOT FOUND THEN
        RAISE EXCEPTION 'No se encontraron datos %.', $1;
    END IF;
END;
$BODY$ 
LANGUAGE plpgsql;
select * from Citas_listado_paciente(1,'65446546') as t (ID integer,HORA_CITA time,FECHA date,DIA varchar(50),nombre1 varchar(100),apellido1 varchar(100),identificacion varchar(20));
/*
Noveno SP con excepciones
*/



/*
Decimo SP con excepciones
*/
DROP FUNCTION Citas_medico_pendientes(integer);
CREATE OR REPLACE FUNCTION Citas_medico_pendientes(idmedico integer)
RETURNS SETOF RECORD
AS $BODY$
BEGIN
    RETURN QUERY 
    SELECT C.ID,C.HORA_CITA,C.FECHA,AD.DIA,U.NOMBRE1,U.APELLIDO1,U.IDENTIFICACION
    FROM citas_cita C INNER JOIN AGENDAS_AGENDA A ON C.agenda_id=A.ID
    INNER JOIN AGENDAS_DIA AD ON A.dia_id=AD.ID
    INNER JOIN pacientes_paciente P ON P.id=C.paciente_id
    INNER JOIN usuarios_usuario U ON P.usuario_id=U.ID
    WHERE A.medico_id=idmedico and C.ESTADO=1 and date(C.fecha)>=current_date;
    IF NOT FOUND THEN
        RAISE EXCEPTION 'No se encontraron datos %.', $1;
    END IF;
END;
$BODY$ 
LANGUAGE plpgsql;
select * from Citas_medico_pendientes(3) as t (ID integer,HORA_CITA time,FECHA date,DIA varchar(50),nombre1 varchar(100),apellido1 varchar(100),identificacion varchar(20));
/*
Decimo SP con excepciones
*/



/*
Undecimo SP con excepciones
*/
DROP FUNCTION Auditorias_total();
CREATE OR REPLACE FUNCTION Auditorias_total()
RETURNS SETOF RECORD
AS $BODY$
BEGIN
    RETURN QUERY 
    select count(operacion) total_operaciones,  operacion, extract (month from fechahora) as fecha 
    from usuarios_auditoria 
    group by operacion, fecha
    order by operacion;
    IF NOT FOUND THEN
        RAISE EXCEPTION 'No se encontraron datos %.', $1;
    END IF;
END;
$BODY$ 
LANGUAGE plpgsql;
select * from Auditorias_total() as t (total_operaciones bigint,operacion varchar(50),fecha float);
/*
Undecimo SP con excepciones
*/






CREATE OR REPLACE FUNCTION insert_auditoria() RETURNS trigger AS $$
    BEGIN
        INSERT INTO usuarios_auditoria 
                    (operacion, fechahora, usuario) 
                    VALUES ('INSERT',current_date,NEW.paciente_id);

        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION delete_auditoria() RETURNS trigger AS $$
    BEGIN
        INSERT INTO usuarios_auditoria 
                    (operacion, fechahora, usuario) 
                    VALUES ('DELETE',current_date,OLD.paciente_id);


        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER insert_auditoria AFTER INSERT ON CITAS_CITA
    FOR EACH ROW EXECUTE PROCEDURE insert_auditoria();


CREATE TRIGGER delete_auditoria AFTER DELETE ON CITAS_CITA
    FOR EACH ROW EXECUTE PROCEDURE delete_auditoria();





/*
from django import forms

class SettingsForm(forms.Form):
    delivery_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
*/


