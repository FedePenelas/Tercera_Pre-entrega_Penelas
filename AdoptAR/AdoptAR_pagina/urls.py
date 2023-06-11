from django.urls import path
from .views import formularioPersona, formularioDonante, formularioTransito, formularioDarEnAdopcion
from AdoptAR_pagina import views

urlpatterns = [
    path('', views.index),
    path("adoptar/", views.adoptar),
    path("transito/", views.transito),
    path("darenadopcion/", views.darEnAdopcion),
    path('sobrenosotros/', views.sobrenosotros),
    path('contacto/', views.contacto),
    path("donar/", views.donar),
    path('formularioPersona/', formularioPersona, name='Formulario'),
    path('formularioDonante/', formularioDonante, name='Formulario de donante'),
    path('formularioTransito/', formularioTransito, name='Formulario para transito'),
    path('formularioDarEnAdopcion/', formularioDarEnAdopcion, name='Formulario para dar en adopción'),
]
