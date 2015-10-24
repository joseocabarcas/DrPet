from django import forms 
from .models import Usuario
from django.contrib.auth import login,authenticate


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
            'class':'form-control',
            }),
        'password':forms.TextInput(attrs=
            {
            'class':'form-control',
            'type':'password',
            }),
        'nombre1':forms.TextInput(attrs=
            {
            'class':'form-control',
            }),
        'nombre2':forms.TextInput(attrs=
            {
            'class':'form-control',
            }),
        'apellido1':forms.TextInput(attrs=
            {
            'class':'form-control',
            }),
        'apellido2':forms.TextInput(attrs=
            {
            'class':'form-control',
            }),
        'sexo':forms.Select(attrs=
            {
            'class':'form-control',
            },choices=SEXO_CHOICES),
        'celular':forms.TextInput(attrs=
            {
            'class':'form-control',
            }),
        'direccion':forms.TextInput(attrs=
            {
            'class':'form-control',
            }),
        'email':forms.EmailInput(attrs=
            {
            'class':'form-control',
            }),
        'identificacion':forms.NumberInput(attrs=
            {
            'class':'form-control',
            }),
        'tipo_identificacion':forms.Select(attrs=
            {
            'class':'form-control',
            },choices=TIPOIDENTIFICACION_CHOICES),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs=
            {
            'class':'form-control',
            }))
    password = forms.CharField(max_length=30, 
    	widget=forms.TextInput(attrs={
    		'type': 'password',
            'class':'form-control',
    		}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data
		