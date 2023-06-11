from django.urls import path
from AdoptAR_pagina import views

urlpatterns = [
    path('', views.index),
    path("adoptar/", views.adoptar),
    path("transito/", views.transito),
    path("darenadopcion/", views.darEnAdopcion),
    path('sobrenosotros/', views.sobrenosotros),
    path('contacto/', views.contacto),
]
