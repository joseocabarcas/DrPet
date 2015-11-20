from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/auditoria/reporte/$', 'apps.usuarios.admin_views.report',name='admin/auditoria/reporte/'),
    url(r'^admin/auditoria/reporte-ajax/$', 'apps.usuarios.admin_views.reportesajax',name='admin/auditoria/reporte-ajax/'),
    url(r'^', include('apps.usuarios.urls')),
    url(r'^', include('apps.agendas.urls')),
    url(r'^', include('apps.citas.urls')),
]
