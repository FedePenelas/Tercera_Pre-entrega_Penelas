from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.template import Context, Template
from .forms import FormularioPersona, FormularioDonante, FormularioDarEnAdopcion, FormularioTransito, FormularioGenerico
from .models import *

def index(request):
    # Obtener la plantilla utilizando loader.get_template()
    plantilla = loader.get_template('index.html')
    # Realizar cualquier lógica adicional o procesamiento de datos aquí

    # Renderizar la plantilla con un contexto y obtener el documento resultante
    contexto = {'variable': 'valor'}
    documento = plantilla.render(contexto)
    # Retornar el documento como una respuesta HTTP
    return HttpResponse(documento)
def adoptar(request):
    plantilla = loader.get_template('adoptar.html')
    contexto = {'variable': 'valor'}
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
def transito(request):
    if request.method == 'POST':
        formulario = FormularioTransito(request.POST)
        if formulario.is_valid():
            # Procesar los datos del formulario
            # ...
            # Redirigir a otra vista
            return redirect('listo.html')
    else:
        formulario = FormularioTransito()
    plantilla = loader.get_template('transito.html')
    contexto = {'variable': 'valor', 'formulario': formulario}
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
def darEnAdopcion(request):
    if request.method == 'POST':
        formulario = FormularioDarEnAdopcion(request.POST)
        if formulario.is_valid():
            # Procesar los datos del formulario
            # ...
            # Redirigir a otra vista
            return redirect('listo.html')
    else:
        formulario = FormularioDarEnAdopcion()
    plantilla = loader.get_template('darenadopcion.html')
    contexto = {'variable': 'valor', 'formulario': formulario}
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
def sobrenosotros(request):
    plantilla = loader.get_template('sobrenosotros.html')
    contexto = {'variable': 'valor'}
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
def contacto(request):
    plantilla = loader.get_template('contacto.html')
    contexto = {'variable': 'valor'}
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
def donar(request):
    if request.method == 'POST':
        formulario = FormularioDonante(request.POST)
        if formulario.is_valid():
            # Procesar los datos del formulario
            # ...
            # Redirigir a otra vista
            return redirect('listo.html')
    else:
        formulario = FormularioDonante()
    plantilla = loader.get_template('donar.html')
    contexto = {'variable': 'valor', 'formulario': formulario}
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
def listo(request):

    plantilla = loader.get_template('listo.html')
    contexto = {'variable': 'valor'}
    documento = plantilla.render(contexto)
    return HttpResponse(documento)


def formularioGenerico(request, modelo):
    # Determina el modelo específico basado en el parámetro recibido
    if modelo == 'persona':
        modelo = Persona
    elif modelo == 'darenadopcion':
        modelo = DarEnAdopcion
    elif modelo == 'transito':
        modelo = Transito
    elif modelo == 'donante':
        modelo = Donante
    else:
        # Manejo de caso inválido, como redirección a una página de error
        return redirect('pagina_error')

    if request.method == 'POST':
        form = FormularioGenerico(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmacion')
    else:
        form = FormularioGenerico()

    return render(request, 'formulario_generico.html', {'form': form})

def formulariofede(request):
    if request.method == "POST":
        formulario = FormularioDarEnAdopcion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return render(request, 'listo.html')
    else:
        formulario = FormularioDarEnAdopcion()
    return render(request, 'formularios.html', {'formulario': formulario})