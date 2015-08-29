from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class CitaView(TemplateView):

    def get(self,request):
    	return render(request,'cita.html')