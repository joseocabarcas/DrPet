from django.conf.urls import include, url
from .views import DashboardView
urlpatterns = [
    url(r'^$', 'apps.usuarios.views.index',name='/'),
    url(r'^logout$', 'apps.usuarios.views.Logout',name='logout'),
    url(r'^inicio$', 'apps.usuarios.views.inicio',name='inicio'),
    url(r'^dashboard$', DashboardView.as_view(),name='dashboard'),
    url(r'^home$', 'apps.usuarios.views.home',name='home'),
    url(r'^register/medico$', 'apps.usuarios.views.register_medico',name='register/medico'),
    url(r'^register/paciente$', 'apps.usuarios.views.register_paciente',name='register/paciente'),
]
