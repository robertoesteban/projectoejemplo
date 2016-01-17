from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render_to_response, redirect, render
from preguntasyrespuestas.models import Pregunta
from preguntasyrespuestas.form import PreguntaForm
from django.template import RequestContext
from django.utils import timezone

def index(request):
    preguntas = Pregunta.objects.all()
    return render_to_response('preguntasyrespuestas/index.html', {'preguntas': preguntas})

def pregunta_detalle(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    return render_to_response('preguntasyrespuestas/pregunta_detalle.html', {'pregunta': pregunta})

def pregunta_crear(request):
    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            pregunta = Pregunta(asunto=form.cleaned_data['asunto'],descripcion=form.cleaned_data['descripcion'],fecha_publicacion=timezone.now())
            pregunta.save()
            return redirect('preguntas')
    else:
        form = PreguntaForm()
        return render_to_response('preguntasyrespuestas/pregunta_crear.html',{'form': form},RequestContext(request))


