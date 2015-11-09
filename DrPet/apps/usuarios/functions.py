from django.contrib.auth import login,authenticate
from django.shortcuts import render,redirect
from .forms import LoginForm
from django.template import RequestContext, loader

def LogIn(request,username,password):
	usuario= authenticate(username=username,password=password)
	if usuario is not None:
		if usuario.is_active:
			login(request,usuario)
			print "1"
			return redirect('/')
		else:
			print "2"
			return HttpResponse("You're account is disabled.")
	else:
		print  "invalid login details " + username + " " + password
		return render(request,'login.html',{},context_instance=RequestContext(request))