from django import forms 
from .models import Agenda


FRECUENCIA_CHOICES=(('10','10'),('20','20'),('30','30'),('40','40'),('50','50'),('60','60')
    ,('70','70'),('80','80'),('90','90'),('100','100'),('110','110'),('120','120'))


class AgendaForm(forms.ModelForm):
    
    class Meta:
        model = Agenda
        fields = ('hora_ini','hora_fin','frecuencia',)
        exclude=('dia','medico',)

        dateTimeOptions = {
        'format': 'hh:ii',
        'autoclose': True,
        'pick12HourFormat': True,
        'pickDate': False,
        }

        widgets= {
        	'hora_ini':forms.TimeInput(attrs=
                {
                'class':'pick-a-time'
                },),
        	'hora_fin':forms.TimeInput(attrs=
        		{
        		
        		},),
        	'frecuencia':forms.Select(choices=FRECUENCIA_CHOICES,attrs={
                
                }),
        	
        }