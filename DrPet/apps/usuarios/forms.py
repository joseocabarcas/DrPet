from django import forms 
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username','password','nombre1','nombre2','apellido1','apellido2','sexo','celular',
				'direccion','email','identificacion',
				'tipo_identificacion')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, 
    	widget=forms.TextInput(attrs={
    		'type': 'password'
    		}))
    
		