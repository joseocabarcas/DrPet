from django import forms 
from .models import Usuario


TIPOIDENTIFICACION_CHOICES=(('CC','Cedula Ciudadania'),('CE','Cedua Extranjeria')
    ,('PP','Pasaporte'),('TI','Tarjeta de Identidad'),('RC','Registro Civil'))
SEXO_CHOICES=(('M','M'),('F','F'))

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username','password','nombre1','nombre2','apellido1','apellido2','sexo','celular',
				'direccion','email','identificacion',
				'tipo_identificacion')
        widgets={
        'username':forms.TextInput(attrs=
            {
            
            }),
        'password':forms.TextInput(attrs=
            {
            
            'type':'password'
            }),
        'nombre1':forms.TextInput(attrs=
            {
            }),
        'nombre2':forms.TextInput(attrs=
            {
            }),
        'apellido1':forms.TextInput(attrs=
            {
            }),
        'apellido2':forms.TextInput(attrs=
            {
            }),
        'sexo':forms.Select(attrs=
            {
            },choices=SEXO_CHOICES),
        'celular':forms.TextInput(attrs=
            {
            }),
        'direccion':forms.TextInput(attrs=
            {
            }),
        'email':forms.EmailInput(attrs=
            {
            }),
        'identificacion':forms.NumberInput(attrs=
            {
            }),
        'tipo_identificacion':forms.Select(attrs=
            {
            },choices=TIPOIDENTIFICACION_CHOICES),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs=
            {
            
            }))
    password = forms.CharField(max_length=30, 
    	widget=forms.TextInput(attrs={
    		'type': 'password',
            
    		}))
    
		