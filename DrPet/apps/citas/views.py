from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponse
from apps.agendas.models import Agenda,Dia
from apps.medicos.models import Especialidad,Medico
from apps.usuarios.models import Usuario
from .models import Cita,Procedimientos
import json
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.core import serializers
# Create your views here.
class CitaView(TemplateView):

    def get(self,request):
    	especialidades = Especialidad.objects.all()
    	return render(request,'cita.html',{'especialidades':especialidades})

@login_required(login_url='/')
def fecha_agenda_disp(request):
	if request.method =="POST":
		#fecha=json.loads(request.body)['fecha']
		#print request.body
		#print request.POST
		#print request.META['CONTENT_TYPE']
		#print fecha
		fecha= request.POST['fecha']
		medico_id= request.POST['medico_id']
		print fecha
		print medico_id
		procedimientos= Procedimientos()
		try:
			agenda=procedimientos.Medico_Agenda(medico_id,fecha)
		except Exception, e:
			agenda={}
			print e
		#agenda=procedimientos.Medico_Agenda(request.POST['medico_id'],request.POST['fecha'])
		print agenda
		return JsonResponse({'fecha':fecha,'agenda':agenda})
	else:
		return HttpResponse({'error':request})

@login_required(login_url='/')
def especialidad_medicos(request):
	if request.method=='POST':
		# medico=Medico.objects.filter(especialidad=request.POST['especialidad']).select_related('usuario')
		# print medico.query
		# data = serializers.serialize("json", medico)
		# return HttpResponse(data)
		procedimientos=Procedimientos()
		try:
			medicos=procedimientos.Especialidad_Medicos(request.POST['especialidad'])
		except Exception, e:
			medicos={}
		
		print medicos
		return JsonResponse({'medicos':medicos})
		#data = serializers.serialize("json", medicos)
		#return HttpResponse(data)
	else:
		return HttpResponse({'error':request})


def agenda_disp_medico(request,medico_id):
	print medico_id
	return render(request,'medico_agenda.html',{'medico_id':medico_id})

