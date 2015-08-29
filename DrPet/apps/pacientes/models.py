from django.db import models
from apps.usuarios.models import Usuario
from django.conf import settings

# Create your models here.
class Paciente(models.Model):
	fecha_nacimiento = models.DateField(null=True, blank=True)
	usuario = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, related_name='paciente')

	class Meta:
		verbose_name = "Paciente"
		verbose_name_plural = "Pacientes"

	def __unicode__ (self):
		return "%s" % self.usuario


    

    