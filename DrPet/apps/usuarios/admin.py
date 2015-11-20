# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from .models import Usuario,Auditoria
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Usuario
# Register your models here.
class UserCreationForm(forms.ModelForm):
	'''Una forma de crear nuevos usuarios. Incluyendo los campos necesarios
	además de repetir la contraseña. '''
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirmar Password', widget=forms.PasswordInput)

	class Meta:
		model = Usuario
		fields = ('username',)

	def clean_password2(self):
	#Comprueba que las dos contraseñas coinciden
	    password1 = self.cleaned_data.get('password1')
	    password2 = self.cleaned_data.get('password2')
	    if password1 and password2 and password1 != password2:
	    	raise forms.ValidationError('Las contraseñas no coinciden')
	    return password2

	def save(self, commit=True):
		#Guardar la contraseña proporcionada en formato hash
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user



class UserChangeForm(forms.ModelForm):
	''' Una formulario para la actualización de los usuarios. Incluye todos los campos en 
	el usuario, pero sustituye el campo de contraseña del azdministrador por el campo 
	de visualización hash de contraseña. '''

	# password = ReadOnlyPasswordHashField(label=("password"),
	# 	help_text= ("Las contraseñas en crudo no se almacenan, así que no hay manera "
	# 		"de ver la contraseña de este usuario, pero puedo cambiar la contraseña "
	# 		"usando <a href=\"password/\"> este formulario</a>."))

	class Meta:
		model = Usuario
		fields = ('username', 'email', 'password', 'is_active',)

	def clean_password(self):
		#Independientemente de lo que ofrece al usuario, devuelve el valor inicial.
		#Esto se hace aquí, en lugar de en el campo, 
		#porque el campo no tiene acceso al valor inicial.
		return self.initial["password"]



class UsuarioAdmin(UserAdmin):
	#Este formulario agrega y modifica instacias de usuario.
	form = UserChangeForm
	add_form =UserCreationForm
	list_display = ('username','nombre1','apellido1','email',)
	search_fields= ('username','email',)
	list_filter= ('is_superuser',)
	ordering= ('username',)
	filter_horizontal = ('groups','user_permissions')
	fieldsets = (
			('Usuario',{'fields':('username','password',)}),
			('Personal Info',{'fields':('nombre1',
										'nombre2',
										'apellido1',
										'apellido2',
										'sexo',
										'celular',
										'direccion',
										'email',
										'identificacion',
										'tipo_identificacion',)}),
			('Permissions',{'fields':(
										'is_active',
										'is_staff',
										'is_superuser',
										'groups',
										'user_permissions',)}),
		)


from django.conf.urls import patterns

class AuditoriaAdmin(admin.ModelAdmin):
	def get_urls(self):
		urls = super(AuditoriaAdmin, self).get_urls()
		my_urls = patterns('',(r'^admin/auditoria/reporte/$', self.my_view))
		return my_urls + urls


	def my_view(self, request):
		#custom view which should return an HttpResponse
		return render_to_response("reporte.html",{},RequestContext(request, {}),)



admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Auditoria,AuditoriaAdmin)