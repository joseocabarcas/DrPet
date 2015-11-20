from django.conf.urls import include, url
from .views import CitaView
urlpatterns = [
    url(r'^cita$', CitaView.as_view(),name='cita'),
    url(r'^cita/listado$','apps.citas.views.listadoCitas',name='cita/listado'),
    url(r'^cita/pendientes$','apps.citas.views.pendientes',name='cita/pendientes'),
    url(r'^cita/pendientes-medico$','apps.citas.views.pendientes_medico',name='cita/pendientes-medico'),

    url(r'^cita/aprobar/(?P<cita_id>\d+)$','apps.citas.views.aprobarCitas',name='cita/aprobar'),
    url(r'^cita/cancelar/(?P<cita_id>\d+)$','apps.citas.views.cancelarCitas',name='cita/cancelar'),
    url(r'^cita/agenda-disp$', 'apps.citas.views.fecha_agenda_disp',name='cita/agenda-disp'),
    url(r'^cita/citas-hora$', 'apps.citas.views.citas_horas',name='cita/citas-hora'),
    url(r'^cita/agenda-disp-medico/(?P<medico_id>\d+)/$', 'apps.citas.views.agenda_disp_medico',name='cita/agenda-disp-medico'),
    url(r'^cita/especialidad-medico$', 'apps.citas.views.especialidad_medicos',name='cita/especialidad-medico'),

    url(r'^cita/historial-medico$','apps.citas.views.historial_medico',name='cita/historial-medico'),
    url(r'^cita/buscar$','apps.citas.views.buscar',name='cita/buscar'),
    url(r'^cita/pacientes$','apps.citas.views.pacientes',name='cita/pacientes'),
    url(r'^cita/seguimiento/(?P<cita_id>\d+)$','apps.citas.views.seguimiento',name='cita/seguimiento/'),   
]