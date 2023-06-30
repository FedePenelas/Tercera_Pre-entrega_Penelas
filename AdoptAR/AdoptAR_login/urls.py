#URLS.PY DE LA APP=
from django.urls import path
from AdoptAR_login import models
from .models import Account
from .views import *
from AdoptAR_login import views


urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('crear_cuenta/', views.register, name='crear_cuenta'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('perfil/', views.mostrar_perfil, name='mostrar_perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/cambiar-password/', views.CambiarPassword.as_view(), name='cambiar_password'),
    path('perfil/eliminar/<int:pk>/', views.EliminarPerfil.as_view(), name='eliminar_perfil'),
]