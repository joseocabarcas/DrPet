
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
Primer SP
Listado de Agendas Segun El Medico
*/

DROP FUNCTION listadoagendas(integer);
CREATE OR REPLACE FUNCTION listadoAgendas
(IN idmedico integer)
RETURNS SETOF RECORD
AS $$
    SELECT AG.ID,AG.HORA_INI,AG.HORA_FIN,AG.FRECUENCIA,AD.DIA FROM AGENDAS_AGENDA AG INNER JOIN AGENDAS_DIA AD ON AG.DIA_ID=AD.ID WHERE AG.MEDICO_ID = idmedico;
$$ LANGUAGE SQL;

select * from listadoAgendas(1) as t (id integer,hora_ini time,hora_fin time,frecuencia integer,dia character);

/*
Primer SP
*/


/*
Segundo SP
Listado de Medicos Segun la Especialidad
*/
DROP FUNCTION Especialidad_Medicos(integer);
CREATE OR REPLACE FUNCTION Especialidad_Medicos
(IN idespecialidad integer)
RETURNS SETOF RECORD
AS $$
    SELECT medicos_medico.id, medicos_medico.empresa, medicos_medico.descripcion, medicos_medico.usuario_id,  usuarios_usuario.nombre1||' '||usuarios_usuario.nombre2||' '||usuarios_usuario.apellido1||' '||usuarios_usuario.apellido2 as nombre, usuarios_usuario.direccion  
    FROM medicos_medico INNER JOIN usuarios_usuario ON ( medicos_medico.usuario_id = usuarios_usuario.id ) 
    WHERE medicos_medico.especialidad_id = idespecialidad;
$$ LANGUAGE SQL;

select * from Especialidad_Medicos(1) as t (id integer,empresa character,descripcion character,id_usuario integer,nombre character,direccion character);
/*
Segundo SP
*/


/*
Tercer SP
Listado de Medicos Segun la Especialidad
*/
DROP FUNCTION Medico_Agenda(integer,varchar);
CREATE OR REPLACE FUNCTION Medico_Agenda
(IN idmedico integer,IN dia varchar)
RETURNS SETOF RECORD
AS $$
    SELECT AG.ID,AG.HORA_INI,AG.HORA_FIN,AG.FRECUENCIA,AD.DIA 
    FROM AGENDAS_AGENDA AG INNER JOIN AGENDAS_DIA AD ON AG.DIA_ID=AD.ID 
    WHERE AG.MEDICO_ID = idmedico AND LOWER(AD.DIA)=LOWER(dia);
$$ LANGUAGE SQL;

select * from Medico_Agenda(1,'LuNeS') as t (id integer,hora_ini time,hora_fin time,frecuencia integer,dia character);
/*
Tercer SP
*/



/*
Primer SP con excepciones
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
    WHERE C.paciente_id=idpaciente and C.ESTADO=1;
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








from django import forms

class SettingsForm(forms.Form):
    delivery_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))



