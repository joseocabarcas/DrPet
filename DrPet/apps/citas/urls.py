from django.conf.urls import include, url
from .views import CitaView
urlpatterns = [
    
    url(r'^cita$', CitaView.as_view(),name='cita'),
   
]
