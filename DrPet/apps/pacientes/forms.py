from django import forms
from .models import Paciente


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        exclude= ('usuario',)
        widgets={
        'fecha_nacimiento':forms.DateInput(attrs={
        	'class':'',
        	}),
        }
