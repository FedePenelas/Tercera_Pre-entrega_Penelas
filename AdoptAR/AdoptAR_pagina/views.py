from django.shortcuts import render
from django.http import HttpResponse
from AdoptAR_pagina import models
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