from django.contrib.auth import login,authenticate
def LogIn(request,username,password):
	usuario= authenticate(username=username,password=password)
	if usuario is not None:
		if usuario.is_active:
			login(request,usuario)
					