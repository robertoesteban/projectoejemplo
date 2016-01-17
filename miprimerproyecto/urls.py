from django.conf.urls import  include, url
from django.contrib import admin

urlpatterns = [
        url(r'^preguntas/',include('preguntasyrespuestas.urls')),
        url(r'^admin/',admin.site.urls),
        ]
