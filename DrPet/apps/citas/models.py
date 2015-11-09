from django.db import models
from apps.agendas.models import Agenda
from apps.pacientes.models import Paciente
from django.db import connection
from apps.agendas.functions import dictfetchall
# Create your models here.
class Cita(models.Model):

	hora_cita = models.TimeField()
	#hora_fin = models.TimeField()
	fecha= models.DateField()
	estado = models.SmallIntegerField()
	agenda = models.ForeignKey(Agenda,verbose_name='agenda')
	paciente = models.ForeignKey(Paciente,verbose_name='paciente')

	class Meta:
		verbose_name = "Cita"
		verbose_name_plural = "Citas"

	def __unicode__(self):
		return "%s" % self.hora_cita

class Seguimiento(models.Model):

	titulo = models.CharField(max_length=50)
	descripcion = models.TextField()
	observaciones = models.TextField()
	cita = models.ForeignKey(Cita,verbose_name='cita')

	class Meta:
		verbose_name = "Seguimiento"
		verbose_name_plural = "Seguimientos"

	def __unicode__(self):
		return "%s" % self.titulo

class Procedimientos():

	def Especialidad_Medicos(self,id_especialidad):
		cursor = connection.cursor()
		#cursor.execute("select * from Especialidad_Medicos(%s) as t (id integer,empresa character,descripcion character,id_usuario integer,nombre character,direccion character);", [id_especialidad])
		cursor.execute("select * from Especialidad_Medicos(%s) as t (id integer,empresa varchar(50),descripcion text,id_usuario integer,nombre varchar(100),direccion varchar);", [id_especialidad])
		medicos=dictfetchall(cursor)
		cursor.close()
		#print medicos
		return medicos

	def Medico_Agenda(self,idmedico,nomdia):
		cursor = connection.cursor()
		#cursor.execute("select * from Medico_Agenda(1,'LuNeS') as t (id integer,hora_ini time,hora_fin time,frecuencia integer,dia character);", [idmedico,nomdia])
		cursor.execute("select * from Medico_Agenda(%s, %s) as t (id integer,hora_ini time,hora_fin time,frecuencia integer,dia varchar(50));", [idmedico,nomdia])
		agenda=dictfetchall(cursor)
		cursor.close()
		print agenda
		return agenda

	def Citas_paciente(self,idpaciente):
		cursor=connection.cursor()
		cursor.execute("select * from Citas_paciente(%s) as t (HORA_CITA time,FECHA date,DIA varchar(50),nombre1 varchar(100),apellido1 varchar(100),especialidad varchar(50));",[idpaciente])
		citas=dictfetchall(cursor)
		cursor.close()
		print citas
		return citas


	def Citas_paciente_sin_asignar(self,idpaciente):
		cursor=connection.cursor()
		cursor.execute("select * from Citas_paciente_sin_asignar(%s) as t (HORA_CITA time,FECHA date,DIA varchar(50),nombre1 varchar(100),apellido1 varchar(100),especialidad varchar(50));",[idpaciente])
		citas=dictfetchall(cursor)
		cursor.close()
		print citas
		return citas

	def Citas_ocupadas(self,fecha):
		cursor=connection.cursor()
		cursor.execute("select * from citas_ocupadas(%s) as t (HORA_CITA time);",[fecha])
		citas=dictfetchall(cursor)
		cursor.close()
		print citas
		return citas
	