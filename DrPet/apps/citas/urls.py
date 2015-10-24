from django.conf.urls import include, url
from .views import CitaView
urlpatterns = [
    
    url(r'^cita$', CitaView.as_view(),name='cita'),
    url(r'^cita/listado$','apps.citas.views.listadoCitas',name='cita/listado'),
    url(r'^cita/agenda-disp$', 'apps.citas.views.fecha_agenda_disp',name='cita/agenda-disp'),
    url(r'^cita/agenda-disp-medico/(?P<medico_id>\d+)/$', 'apps.citas.views.agenda_disp_medico',name='cita/agenda-disp-medico'),
    url(r'^cita/especialidad-medico$', 'apps.citas.views.especialidad_medicos',name='cita/especialidad-medico'),


   
]
