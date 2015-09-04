from django import forms
from .models import Medico

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'
        exclude= ('usuario',)

        widgets={
        'descripcion':forms.Textarea(attrs={
        	'class':'materialize-textarea',
        	'rows':'3'
        	}),
        'empresa':forms.TextInput(attrs={
        	'class':'form-control',
        	}),
        'reg_medico':forms.TextInput(attrs={
        	'class':'form-control',
        	}),
        'especialidad':forms.Select(attrs={
        	'class':'form-control',
        	}),
        }
    