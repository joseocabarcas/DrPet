from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.

class UsuarioManager(BaseUserManager, models.Manager):

	def _create_user(self,username,email,nombre1,nombre2,apellido1,apellido2,
		sexo,celular,direccion,identificacion,tipo_identificacion ,password,is_staff,is_superuser, **extra_fields):
		email = self.normalize_email(email)
		if not email:
			raise ValueError('El email debe ser obligatorio')
		user = self.model(username = username, email = email,nombre1=nombre1,nombre2=nombre2,
			apellido1=apellido1,apellido2=apellido2,sexo=sexo,celular=celular,direccion=direccion,
			identificacion=identificacion,tipo_identificacion=tipo_identificacion 
			,is_active= True, is_staff= is_staff, is_superuser= is_superuser,
			**extra_fields)
		user.set_password(password)
		user.save(using = self._db)
		return user

	def _create_superuser(self,username,email,password,is_staff,is_superuser, **extra_fields):
		email = self.normalize_email(email)
		if not email:
			raise ValueError('El email debe ser obligatorio')
		user = self.model(username = username, email = email,is_active= True, is_staff= is_staff, is_superuser= is_superuser,
			**extra_fields)
		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_user(self, username, email, nombre1,nombre2,apellido1,apellido2,sexo,celular,direccion,identificacion,tipo_identificacion ,password=None,**extra_fields):
		return self._create_user(username,email,nombre1,nombre2,apellido1,apellido2,
		sexo,celular,direccion,identificacion,tipo_identificacion ,password,False,False, **extra_fields)

	def create_superuser(self, username, email,password=None,**extra_fields):
		return self._create_superuser(username,email,password,True,True, **extra_fields)
	
		
class Usuario(AbstractBaseUser, PermissionsMixin):
	nombre1  = models.CharField(max_length=100)
	nombre2  = models.CharField(max_length=100)
	apellido1  = models.CharField(max_length=100)
	apellido2  = models.CharField(max_length=100)
	sexo = models.CharField(max_length=1)
	celular = models.CharField(max_length=20)
	direccion = models.CharField(max_length=100)
	email = models.EmailField()
	identificacion = models.CharField(max_length=20)
	tipo_identificacion = models.CharField(max_length=3)
	username = models.CharField(max_length=100,unique=True)

	objects = UsuarioManager()

	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	USERNAME_FIELD ='username'
	REQUIRED_FIELDS = ['email']

	def get_short_name(self):
		return self.username


