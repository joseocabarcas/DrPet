from django import forms 
from .models import Cita,Seguimiento

# class CitaForm(forms.ModelForm):
#     class Meta:
#         model = Cita


class SeguimientoForm(forms.ModelForm):
    class Meta:
        model = Seguimiento
        exclude=('cita',)

        widgets = {
        'titulo':forms.TextInput(attrs={
        	'class':'form-control'
        	}),
        'observaciones':forms.Textarea(attrs={
        	'class':'form-control',
        	'rows':'3'
        	}),
        'descripcion':forms.Textarea(attrs={
        	'class':'form-control',
        	'rows':'3'
        	}),
        }
