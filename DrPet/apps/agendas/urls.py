from django.conf.urls import include, url
from .views import AgendaView
urlpatterns = [
  
    url(r'^agenda$', AgendaView.as_view(),name='agenda'),
    url(r'^agenda/listado$','apps.agendas.views.listadoAgendas',name='agenda/listado'),
    url(r'^agenda/editar/(?P<agenda_id>\d+)/$','apps.agendas.views.editar_agenda',name='agenda/editar/'),
    url(r'^agenda/eliminar/(?P<agenda_id>\d+)/$','apps.agendas.views.eliminar_agenda',name='agenda/eliminar/'),


   
]
