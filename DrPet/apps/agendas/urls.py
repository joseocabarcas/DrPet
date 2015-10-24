from django.conf.urls import include, url
from .views import AgendaView
urlpatterns = [
  
    url(r'^agenda$', AgendaView.as_view(),name='agenda'),
    url(r'^frecuenciaInicio.json$', 'apps.agendas.views.frecuenciaInicio',name='frecuenciaInicio.json'),
    url(r'^frecuenciaFin.json$', 'apps.agendas.views.frecuenciaFin',name='frecuenciaFin.json'),
    url(r'^agenda/listado$','apps.agendas.views.listadoAgendas',name='agenda/listado'),
    url(r'^agenda/editar/(?P<agenda_id>\d+)/$','apps.agendas.views.editar_agenda',name='agenda/editar/'),
    url(r'^agenda/eliminar/(?P<agenda_id>\d+)/$','apps.agendas.views.eliminar_agenda',name='agenda/eliminar/'),


   
]
