
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


from django import forms

class SettingsForm(forms.Form):
    delivery_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))