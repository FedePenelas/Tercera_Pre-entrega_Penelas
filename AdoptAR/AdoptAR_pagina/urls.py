from django.urls import path
from AdoptAR_pagina import views
from views import inicio, mascota, adoptante, transito

urlpatterns = [
    path('', views.inicio),
    path("inicio/", views.inicio),
    path("mascota/", views.mascota),
    path("adoptante/", views.adoptante),
    path("transito/", views.transito),
    path("prueba/", views.prueba),
]
