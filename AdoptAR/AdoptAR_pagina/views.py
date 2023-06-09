from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context, Template

def inicio(request):
    return HttpResponse("Vista inicial")

def mascota(request):
    return HttpResponse("Vista mascota")

def adoptante(request):
    return HttpResponse("Vista adoptante")

def transito(request):
    return HttpResponse("Vista transito")

def prueba(request):
    nom = "Fede"
    ap = "Pene"
    diccionario = {"nombre":nom, "apellido":ap}
    html = open("C:\\Users\\Fede\\Desktop\\Fede\\Fede\\Programacion\\Coderhouse\\Python\\Pre-entregas\\Tercera Pre-entrega\\Tercera_Pre-entrega+PENELAS\\AdoptAR\\Plantillas\\template1.html")
    plantilla = Template(html.read())
    contexto = Context()
    html.close()
    contexto = Context(diccionario)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def prueba2(request):
    # Obtener la plantilla utilizando loader.get_template()
    plantilla = loader.get_template('index.html')
    # Realizar cualquier lógica adicional o procesamiento de datos aquí
    # Renderizar la plantilla con un contexto y obtener el documento resultante
    contexto = {'variable': 'valor'}
    documento = plantilla.render(contexto)
    # Retornar el documento como una respuesta HTTP
    return HttpResponse(documento)