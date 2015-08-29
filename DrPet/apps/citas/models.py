from django.db import models
from apps.agendas.models import Agenda
from apps.pacientes.models import Paciente

# Create your models here.
class Cita(models.Model):

	hora_ini = models.TimeField()
	hora_fin = models.TimeField()
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
	