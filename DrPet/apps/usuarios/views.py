from .forms import UsuarioForm,LoginForm
from apps.medicos.forms import MedicoForm
from apps.pacientes.forms import PacienteForm
from django.shortcuts import redirect,render
from django.http import HttpResponse
from .models import Usuario
from apps.pacientes.models import Paciente
from apps.medicos.models import Medico
from django.template import RequestContext, loader
from django.contrib.auth import  logout
from .functions import LogIn
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from DrPet.roles import MedicoRol,PacienteRol
from rolepermissions.shortcuts import get_user_role
# Create your views here.
def index(request):
	if request.method =="POST":
		login_form=LoginForm(request.POST)
		if login_form.is_valid():
			LogIn(request,login_form.cleaned_data['username'],
				login_form.cleaned_data['password'],login_form)
			
		else:
			print "45"
			return render(request,'login.html',{'login_form':login_form},context_instance=RequestContext(request))
	if request.user.is_authenticated:
		if Paciente.objects.filter(usuario__id=request.user.id):
			role = get_user_role(request.user)
			print role
			return redirect('home')
		elif Medico.objects.filter(usuario__id=request.user.id):
			role = get_user_role(request.user)
			print role
			return redirect('dashboard')
	login_form=LoginForm()
	return render(request,'login.html',{'login_form':login_form})

@login_required(login_url='/')
def Logout(request):
	logout(request)
	request.session.flush()
	return redirect('/')


class DashboardView(TemplateView):

	def get(self,request):
		return render(request,'dashboard.html')




@login_required(login_url='/')
def home(request):
	return render(request,'home.html')


def inicio(request):
	usuarios = Usuario.objects.filter().select_related()
	print usuarios
	return render(request,'inicio.html',{'usuarios':usuarios})


def register_medico(request):
	if request.method == 'POST':
		usuario_register = UsuarioForm(request.POST)
		medico_register = MedicoForm(request.POST)

		if usuario_register.is_valid() and medico_register.is_valid():
			usuario=Usuario.objects.create_user(username=usuario_register.cleaned_data['username'],
				email=usuario_register.cleaned_data['email'],nombre1=usuario_register.cleaned_data['nombre1'],
				nombre2=usuario_register.cleaned_data['nombre2'],apellido1=usuario_register.cleaned_data['apellido1'],
				apellido2=usuario_register.cleaned_data['apellido2'],sexo=usuario_register.cleaned_data['sexo'],
				celular=usuario_register.cleaned_data['celular'],direccion=usuario_register.cleaned_data['direccion'],
				identificacion=usuario_register.cleaned_data['identificacion'],tipo_identificacion=usuario_register.cleaned_data['tipo_identificacion']
				,password=usuario_register.cleaned_data['password'])
			medico=medico_register.save(commit=False)
			medico.usuario =usuario
			medico.save()
			MedicoRol.assign_role_to_user(usuario)
			LogIn(request,usuario_register.cleaned_data['username'],usuario_register.cleaned_data['password'])
			return redirect('dashboard')
		else:
			return render(request,'register.html',{'usuario_register':usuario_register,'medico_register':medico_register},context_instance=RequestContext(request))
	else:
		usuario_register = UsuarioForm()
		medico_register = MedicoForm()
		
	return render(request,'register.html',{'usuario_register':usuario_register,'medico_register':medico_register},context_instance=RequestContext(request))




def register_paciente(request):
	if request.method == 'POST':
		usuario_register = UsuarioForm(request.POST)
		paciente_register = PacienteForm(request.POST)

		if usuario_register.is_valid() and paciente_register.is_valid():
			usuario=Usuario.objects.create_user(username=usuario_register.cleaned_data['username'],
				email=usuario_register.cleaned_data['email'],nombre1=usuario_register.cleaned_data['nombre1'],
				nombre2=usuario_register.cleaned_data['nombre2'],apellido1=usuario_register.cleaned_data['apellido1'],
				apellido2=usuario_register.cleaned_data['apellido2'],sexo=usuario_register.cleaned_data['sexo'],
				celular=usuario_register.cleaned_data['celular'],direccion=usuario_register.cleaned_data['direccion'],
				identificacion=usuario_register.cleaned_data['identificacion'],tipo_identificacion=usuario_register.cleaned_data['tipo_identificacion']
				,password=usuario_register.cleaned_data['password'])
			paciente=paciente_register.save(commit=False)
			paciente.usuario =usuario
			paciente.save()
			PacienteRol.assign_role_to_user(usuario)
			LogIn(request,usuario_register.cleaned_data['username'],usuario_register.cleaned_data['password'])
			return redirect('home')
		else:
			return render(request,'register.html',{'usuario_register':usuario_register,'paciente_register':paciente_register},
			context_instance=RequestContext(request))
	else:
		usuario_register = UsuarioForm()
		paciente_register = PacienteForm()
	return render(request,'register.html',{'usuario_register':usuario_register,'paciente_register':paciente_register},
			context_instance=RequestContext(request))