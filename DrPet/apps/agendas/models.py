from django.db import models
from apps.medicos.models import Medico
from django.db import connection
from .functions import dictfetchall

# Create your models here.
class Dia(models.Model):
	dia = models.CharField(max_length=50)

	class Meta:
		verbose_name = "Dia"
		verbose_name_plural = "Dias"

	def __unicode__(self):
		return "%s" % self.dia
		
class Agenda(models.Model):
	hora_ini = models.TimeField()
	hora_fin = models.TimeField()
	frecuencia = models.IntegerField()
	dia = models.ForeignKey(Dia,verbose_name='dia')
	medico = models.ForeignKey(Medico,verbose_name='medico')
	class Meta:
		verbose_name = "Agenda"
		verbose_name_plural = "Agendas"

	def __unicode__(self):
		return "%s" % self.dia


class Procedimientos():

	def listadoAgendas(self,id_medico):
		cursor = connection.cursor()
		#cursor.execute("select * from listadoAgendas(%s) as t (id integer,hora_ini time,hora_fin time,frecuencia integer,dia character)", [id_medico])
		cursor.execute("select * from listadoAgendas(%s) as t (id integer,hora_ini time,hora_fin time,frecuencia integer,dia varchar(50));", [id_medico])
		agendas=dictfetchall(cursor)
		cursor.close()
		print agendas
		return agendas
		




	