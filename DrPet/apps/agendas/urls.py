from django.conf.urls import include, url
from .views import AgendaView
urlpatterns = [
  
    url(r'^agenda$', AgendaView.as_view(),name='agenda'),
    url(r'^agenda/listado$','apps.agendas.views.listadoAgendas',name='agenda/listado'),
   
]
