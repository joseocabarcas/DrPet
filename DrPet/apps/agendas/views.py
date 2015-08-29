from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import AgendaForm
from .models import Dia,Agenda
from apps.medicos.models import Medico
from django.db import connection
# Create your views here.
class AgendaView(TemplateView):

    def get(self,request):
    	agenda_form=AgendaForm()
    	medico= Medico.objects.get(usuario=request.user.id)
    	#dias = Dia.objects.filter(agenda__isnull=True,agenda__medico=medico)
    	dias = Dia.objects.raw('select AGENDAS_DIA.ID, AGENDAS_DIA.DIA FROM MEDICOS_MEDICO INNER JOIN AGENDAS_AGENDA ON (AGENDAS_AGENDA.MEDICO_ID= %s) RIGHT OUTER JOIN  AGENDAS_DIA ON (AGENDAS_DIA.ID = AGENDAS_AGENDA.DIA_ID) WHERE (AGENDAS_AGENDA.ID IS NULL) ORDER BY AGENDAS_DIA.ID;',[medico.id])
    	print dias.query
    	print dias
    	return render(request,'agenda.html',{'agenda_form':agenda_form,'dias':dias})

    def post(self, request, *args, **kwargs):
    	agenda_form=AgendaForm(request.POST)
    	if agenda_form.is_valid:
    		agenda=agenda_form.save(commit=False)
    		medico= Medico.objects.get(usuario=request.user.id)
    		dia=Dia.objects.get(pk=request.POST['dia'])
    		agenda.dia=dia
    		agenda.medico=medico
    		agenda.save()
    		return redirect('agenda')

def listadoAgendas(request):
	medico= Medico.objects.get(usuario=request.user.id)
	agendas=Agenda.objects.filter(medico=medico)
	print agendas.query
	return render(request,'listadoAgenda.html',{'agendas':agendas})