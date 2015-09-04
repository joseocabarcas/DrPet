from django.db import models
from apps.agendas.models import Agenda
from apps.pacientes.models import Paciente
from django.db import connection
from apps.agendas.functions import dictfetchall
# Create your models here.
class Cita(models.Model):

	hora_ini = models.TimeField()
	hora_fin = models.TimeField()
	fecha= models.DateField()
	estado = models.SmallIntegerField()
	agenda = models.ForeignKey(Agenda,verbose_name='agenda')
	paciente = models.ForeignKey(Paciente,verbose_name='paciente')

	class Meta:
		verbose_name = "Cita"
		verbose_name_plural = "Citas"

	def __unicode__(self):
		return "%s" % self.hora_ini

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
		cursor.execute("select * from Especialidad_Medicos(%s) as t (id integer,empresa character,descripcion character,id_usuario integer,nombre character,direccion character);", [id_especialidad])
		medicos=dictfetchall(cursor)
		cursor.close()
		#print medicos
		return medicos
	