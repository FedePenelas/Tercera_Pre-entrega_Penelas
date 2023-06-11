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
    path('formularioGenerico/<str:modelo>/', FormularioGenerico, name='formulario_generico'),
    path("formulariofede/", views.formulariofede, name= 'Formulario'),
    path("listo/", views.listo),
]
