from django.db import models
from apps.usuarios.models import Usuario
from django.conf import settings

# Create your models here.
class Especialidad(models.Model):
	nombre = models.CharField(max_length=50)
	class Meta:
		verbose_name = "Especialidad"
		verbose_name_plural = "Especialidades"

	def __unicode__(self):
		return "%s" % self.nombre
		
class Medico(models.Model):
	descripcion = models.TextField()
	empresa = models.CharField(max_length=50)
	reg_medico = models.CharField(max_length=50)
	usuario = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, related_name='medico')
	especialidad = models.ForeignKey(Especialidad,verbose_name='especialidad')


	class Meta:
		verbose_name = "Medico"
		verbose_name_plural = "Medicos"

	def __unicode__ (self):
		return "%s" % self.usuario


	

	

