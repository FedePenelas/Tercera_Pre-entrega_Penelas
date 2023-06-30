from django.urls import path
from .views import FormularioGenerico
from AdoptAR_pagina import views

urlpatterns = [
    path('', views.index),
    path("adoptar/", views.adoptar),
    path("transito/", views.transito),
    path("darenadopcion/", views.darEnAdopcion),
    path('sobrenosotros/', views.sobrenosotros),
    path('contacto/', views.contacto),
    path("donar/", views.donar),
    path("listo/", views.listo, name= 'listo'),
    path("listodonar/", views.listodonar, name= 'listodonar'),
    path('buscar_persona/', views.buscar_persona, name='buscar_persona'),
    path('buscar_transito/', views.buscar_transito, name='buscar_persona'),
    path('buscar_donante/', views.buscar_donante, name='buscar_persona'),
    path('mostrar_darEnAdopcion/', views.mostrar_darEnAdopcion, name='mostrar_darEnAdopcion'),
]
