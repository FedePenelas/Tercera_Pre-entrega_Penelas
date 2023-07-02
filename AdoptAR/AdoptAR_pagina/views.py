from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.template import Context, Template
from .forms import FormularioPersona, FormularioDonante, FormularioDarEnAdopcion, FormularioTransito, FormularioGenerico, BusquedaForm
from .models import *
from AdoptAR_login.models import Avatar, Comentario
from AdoptAR_login.views import obtener_contexto_avatar, agregar_comentario
from AdoptAR_login.forms import ComentarioForm

def index(request):
    contexto_avatar = obtener_contexto_avatar(request)
    contexto = {'variable': 'valor'}
    contexto.update(contexto_avatar)
    return render(request, 'index.html', contexto)
def adoptar(request):
    contexto_avatar = obtener_contexto_avatar(request)

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ComentarioForm(request.POST)
            if form.is_valid():
                contenido = form.cleaned_data['contenido']
                comentario = Comentario(usuario=request.user, contenido=contenido)
                comentario.save()
                return redirect('adoptar')
        else:
            return redirect('nombre_de_la_vista_de_inicio_de_sesion')

    else:
        form = ComentarioForm()

    comentarios = Comentario.objects.all()  # Obtener todos los comentarios

    contexto = {'form': form, 'comentarios': comentarios, **contexto_avatar}
    return render(request, 'adoptar.html', contexto)
def transito(request):
    contexto_avatar = obtener_contexto_avatar(request)
    contexto = {'variable': 'valor'}
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
    contexto = {'variable': 'valor', 'formulario': formulario, **contexto_avatar}
    documento = plantilla.render(contexto)
    return render(request, 'transito.html', contexto)
def darEnAdopcion(request):
    contexto_avatar = obtener_contexto_avatar(request)
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
    contexto = {'variable': 'valor', 'formulario': formulario, **contexto_avatar}
    documento = plantilla.render(contexto)
    return render(request, 'darenadopcion.html', contexto)
def sobrenosotros(request):
    contexto_avatar = obtener_contexto_avatar(request)
    plantilla = loader.get_template('sobrenosotros.html')
    contexto = {'variable': 'valor', **contexto_avatar}
    documento = plantilla.render(contexto)
    return render(request, 'sobrenosotros.html', contexto)
def contacto(request):
    contexto_avatar = obtener_contexto_avatar(request)
    plantilla = loader.get_template('contacto.html')
    contexto = {'variable': 'valor', **contexto_avatar}
    documento = plantilla.render(contexto)
    return render(request, 'contacto.html', contexto)
def donar(request):
    contexto_avatar = obtener_contexto_avatar(request)
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
    contexto = {'variable': 'valor', 'formulario': formulario, **contexto_avatar}
    documento = plantilla.render(contexto)
    return render(request, 'donar.html', contexto)

def listo(request):
    contexto_avatar = obtener_contexto_avatar(request)
    plantilla = loader.get_template('listo.html')
    contexto = {'variable': 'valor'}
    documento = plantilla.render(contexto)
    return HttpResponse(request)
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
    contexto_avatar = obtener_contexto_avatar(request)
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            criterio = form.cleaned_data['criterio']
            resultados = buscar_en_panel('Donante', criterio)  # Llamada a la función de búsqueda con el modelo 'Donante' y el criterio de búsqueda
            return render(request, 'resultado_busqueda.html', {'resultados': resultados, **contexto_avatar})
    else:
        form = BusquedaForm()

    return render(request, 'busqueda_donante.html', {'form': form, **contexto_avatar})
def buscar_transito(request):
    contexto_avatar = obtener_contexto_avatar(request)
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            criterio = form.cleaned_data['criterio']
            resultados = Transito.objects.filter(nombre__icontains=criterio)
            return render(request, 'resultado_busqueda.html', {'resultados': resultados, **contexto_avatar})
    else:
        form = BusquedaForm()

    return render(request, 'busqueda_transito.html', {'form': form, **contexto_avatar})

def mostrar_darEnAdopcion(request):
     contexto_avatar = obtener_contexto_avatar(request)
     darEnAdopcion = DarEnAdopcion.objects.all() #Trae los X que son CLASES y el objects esta definido dentro
     contexto = {"darenadopcion":darEnAdopcion, **contexto_avatar} #lo rojito es lo que tengo que llamar en el bucle for del html
     return render(request, "mostrar_darEnAdopcion.html", contexto)