from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponse
from apps.agendas.models import Agenda,Dia
from apps.medicos.models import Especialidad,Medico
from apps.usuarios.models import Usuario
from apps.pacientes.models import Paciente
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
		#print fecha
		#print medico_id
		procedimientos= Procedimientos()
		try:
			agenda=procedimientos.Medico_Agenda(medico_id,fecha)
		except Exception, e:
			agenda={}
			#print e
		#agenda=procedimientos.Medico_Agenda(request.POST['medico_id'],request.POST['fecha'])
		#print agenda.agenda[0]
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
	if request.method =="POST":
		agenda=Agenda.objects.get(pk=request.POST['agenda'])
		paciente=Paciente.objects.get(usuario=request.user.id)
		print request.POST['hora_cita']
		print request.POST['fecha']
		cita= Cita.objects.create(hora_cita=(request.POST['hora_cita']),fecha=request.POST['fecha'],
			estado=0,agenda=agenda,paciente=paciente)
		cita.save
		return redirect('cita/listado')
	else:
		return render(request,'medico_agenda.html',{'medico_id':medico_id})

def listadoCitas(request):
	try:
		paciente=Paciente.objects.get(usuario=request.user.id)
		citas= Cita.objects.filter(paciente=paciente)
		print citas
	except Cita.DoesNotExist:
		citas = None
	return render(request,'listado_citas.html',{'citas':citas})

