from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.template import Context, Template
from .forms import FormularioPersona, FormularioDonante, FormularioDarEnAdopcion, FormularioTransito, FormularioGenerico, BusquedaForm
from .models import *

def index(request):
    # Obtener la plantilla utilizando loader.get_template()
    plantilla = loader.get_template('index.html')
    # Realizar cualquier lógica adicional o procesamiento de datos aquí

    # Renderizar la plantilla con un contexto y obtener el documento resultante
    contexto = {'variable': 'valor'}
    documento = plantilla.render(contexto)
    # Retornar el documento como una respuesta HTTP
    return render(request, 'index.html', contexto)
def adoptar(request):
    plantilla = loader.get_template('adoptar.html')
    contexto = {'variable': 'valor'}
    documento = plantilla.render(contexto)
    return render(request, 'adoptar.html', contexto)
def transito(request):
    if request.method == 'POST':
        formulario = FormularioTransito(request.POST)
        if formulario.is_valid():
            # Procesar los datos del formulario
            formulario.save()
            # Redirigir a otra vista
            return redirect('listo')
    else:
        formulario = FormularioTransito()
    plantilla = loader.get_template('transito.html')
    contexto = {'variable': 'valor', 'formulario': formulario}
    documento = plantilla.render(contexto)
    return render(request, 'transito.html', contexto)
def darEnAdopcion(request):
    if request.method == 'POST':
        formulario = FormularioDarEnAdopcion(request.POST)
        if formulario.is_valid():
            # Procesar los datos del formulario
            formulario.save()
            # Redirigir a otra vista
            return redirect('listo')
    else:
        formulario = FormularioDarEnAdopcion()
    plantilla = loader.get_template('darenadopcion.html')
    contexto = {'variable': 'valor', 'formulario': formulario}
    documento = plantilla.render(contexto)
    return render(request, 'darenadopcion.html', contexto)
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
            formulario.save()
            # Redirigir a otra vista
            return redirect('listodonar')
    else:
        formulario = FormularioDonante()
    plantilla = loader.get_template('donar.html')
    contexto = {'variable': 'valor', 'formulario': formulario}
    documento = plantilla.render(contexto)
    return render(request, 'donar.html', contexto)

def listo(request):
    plantilla = loader.get_template('listo.html')
    contexto = {'variable': 'valor'}
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
def listodonar(request):
    plantilla = loader.get_template('listodonar.html')
    contexto = {'variable': 'valor'}
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def buscar_persona(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            criterio = form.cleaned_data['criterio']
            resultados = buscar_en_panel(criterio)  # Llamada a la función de búsqueda
            return render(request, 'resultado_busqueda.html', {'resultados': resultados})
    else:
        form = BusquedaForm()

    return render(request, 'busqueda_persona.html', {'form': form})
def buscar_en_panel(model, nombre):
    if model == 'Donante':
        resultados = Donante.objects.filter(nombre__icontains=nombre)
    elif model == 'Transito':
        resultados = Transito.objects.filter(nombre__icontains=nombre)
    elif model == 'Persona':
        resultados = Persona.objects.filter(nombre__icontains=nombre)
    else:
        resultados = []  # Modelo no válido, se devuelve una lista vacía
    return resultados
def buscar_donante(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            criterio = form.cleaned_data['criterio']
            resultados = buscar_en_panel('Donante', criterio)  # Llamada a la función de búsqueda con el modelo 'Donante' y el criterio de búsqueda
            return render(request, 'resultado_busqueda.html', {'resultados': resultados})
    else:
        form = BusquedaForm()

    return render(request, 'busqueda_donante.html', {'form': form})
def buscar_transito(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            criterio = form.cleaned_data['criterio']
            resultados = Transito.objects.filter(nombre__icontains=criterio)
            return render(request, 'resultado_busqueda.html', {'resultados': resultados})
    else:
        form = BusquedaForm()

    return render(request, 'busqueda_transito.html', {'form': form})

def mostrar_darEnAdopcion(request):
     darEnAdopcion = DarEnAdopcion.objects.all() #Trae los X que son CLASES y el objects esta definido dentro
     contexto = {"darenadopcion":darEnAdopcion} #lo rojito es lo que tengo que llamar en el bucle for del html
     return render(request, "mostrar_darEnAdopcion.html", contexto)