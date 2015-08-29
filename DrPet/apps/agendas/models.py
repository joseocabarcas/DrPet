from django.db import models
from apps.medicos.models import Medico

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




	