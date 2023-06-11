from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context, Template
from .forms import FormularioPersona, FormularioDonante, FormularioDarEnAdopcion, FormularioTransito

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
    plantilla = loader.get_template('transito.html')
    contexto = {'variable': 'valor'}
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
def darEnAdopcion(request):
    plantilla = loader.get_template('darenadopcion.html')
    contexto = {'variable': 'valor'}
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
    plantilla = loader.get_template('donar.html')
    contexto = {'variable': 'valor'}
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def formularioPersona(request):
    form = FormularioPersona()
    return render(request, 'formularios.html', {'form':form})

def formularioDonante(request):
    form = FormularioDonante()
    return render(request, 'formularios.html', {'form':form})

def formularioDarEnAdopcion(request):
    form = FormularioDarEnAdopcion()
    return render(request, 'formularios.html', {'form':form})

def formularioTransito(request):
    form = FormularioTransito()
    return render(request, 'formularios.html', {'form':form})