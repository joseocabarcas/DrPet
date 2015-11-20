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
from .forms import SeguimientoForm
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.core import serializers
from django.utils.timezone import now

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

def citas_horas(request):
	if request.method=='POST':
		procedimientos=Procedimientos()
		try:
			citas_hora=procedimientos.Citas_ocupadas(request.POST['fecha'])
		except Exception, e:
			citas_hora={}
		print citas_hora
		return JsonResponse({'citas_hora':citas_hora})
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
		return redirect('home')
	else:
		return render(request,'medico_agenda.html',{'time':now(),'medico_id':medico_id})

def listadoCitas(request):
	try:
		paciente=Paciente.objects.get(usuario=request.user.id)
		citas= Cita.objects.filter(paciente=paciente)
		print citas
		print paciente.id
		procedimientos= Procedimientos()
		try:
			citas=procedimientos.Citas_paciente(paciente.id)
		except Exception, e:
			citas={}
	except Cita.DoesNotExist:
		citas = None
	return render(request,'listado_citas.html',{'citas':citas})

@csrf_exempt
def aprobarCitas(request,cita_id):
	cita= Cita.objects.get(pk=cita_id)
	cita.estado=1
	cita.save()
	return JsonResponse({'mensaje':"Aprobada Exitosamente"},status=200)


@csrf_exempt
def cancelarCitas(request,cita_id):
	cita= Cita.objects.get(pk=cita_id)
	cita.delete()
	return JsonResponse({'mensaje':"Cancelada Exitosamente"},status=200)


def pendientes(request):
	paciente=Paciente.objects.get(usuario=request.user.id)
	procedimientos= Procedimientos()
	try:
		print paciente.id
		citas=procedimientos.Citas_paciente_pendientes(paciente.id)
	except Exception, e:
		print e
		citas={}
	return render(request,'pendientes.html',{'citas':citas})


def historial_medico(request):
	try:
		medico=Medico.objects.get(usuario=request.user.id)
		procedimientos= Procedimientos()
		try:
			citas=procedimientos.Citas_historial_medico(medico.id)
		except Exception, e:
			citas={}
	except Cita.DoesNotExist:
		citas = None
	return render(request,'historial_medico.html',{'citas':citas})

def buscar(request):
	return render(request,'buscar.html')


def pacientes(request):
	try:
		# usuario=Usuario.objects.get(identificacion=request.POST['identificacion'])
		# paciente=Paciente.objects.get(usuario=usuario)

		medico=Medico.objects.get(usuario=request.user.id)
		procedimientos= Procedimientos()
		try:
			citas=procedimientos.Citas_listado_paciente(medico.id,request.POST['identificacion'])
			return JsonResponse({'citas':citas})
		except Exception, e:
			citas={}
			print e
	except Usuario.DoesNotExist:
		citas = None
	return JsonResponse({'error':citas},status=500)


def seguimiento(request,cita_id):
	seguimientoform =SeguimientoForm()
	if request.method =="POST":
		seguimientoform=SeguimientoForm(request.POST)
		if seguimientoform.is_valid():
			seguimiento = seguimientoform.save(commit=False)
			cita = get_object_or_404(Cita, pk=cita_id)

			seguimiento.cita =cita
			seguimiento.save()

			cita.estado=2
			cita.save()

			return redirect('dashboard')
	return render(request,'seguimiento.html',{'seguimientoform':seguimientoform})

def pendientes_medico(request):
	medico=Medico.objects.get(usuario=request.user.id)
	procedimientos= Procedimientos()
	try:
		print medico.id
		citas=procedimientos.Citas_medico_pendientes(medico.id)
		print citas
	except Exception, e:
		print e
		citas={}
	return render(request,'pendientes-medico.html',{'citas':citas})