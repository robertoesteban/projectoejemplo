from django.conf.urls import url

from . import views

urlpatterns = [
        #ex: /preguntas/
        url(r'^$', views.index, name='index'),
        #ex: /pregunta/1/
        url(r'^(?P<pregunta_id>[0-9]+)/$', views.pregunta_detalle, name='pregunta_detalle'),
        url(r'^crear/$', views.pregunta_crear, name='pregunta_crear'),
        ]
