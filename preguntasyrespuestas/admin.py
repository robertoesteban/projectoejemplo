from django.contrib import admin
from preguntasyrespuestas.models import Pregunta, Respuesta
# Register your models here.

class RespuestaInline(admin.StackedInline):
    model =  Respuesta
    extra = 1


class PreguntaAdmin(admin.ModelAdmin):
    inlines = [RespuestaInline]
    list_display = ('asunto', 'fecha_publicacion', 'publicado_hoy')
    list_filter = ['fecha_publicacion']

admin.site.register(Pregunta, PreguntaAdmin)
