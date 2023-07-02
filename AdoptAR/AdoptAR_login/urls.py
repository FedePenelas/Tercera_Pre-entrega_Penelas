#URLS.PY DE LA APP=
from django.urls import path
from AdoptAR_login import models
from .models import Account
from .views import *
from AdoptAR_login import views


urlpatterns = [
    path('iniciar_sesion/', views.login_request, name='iniciar_sesion'),
    path('crear_cuenta/', views.register, name='crear_cuenta'),
    path('cerrar_sesion/', views.Logout.as_view(), name='cerrar_sesion'),
    path('perfil/', views.mostrar_perfil, name='mostrar_perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/cambiar_contraseña/', views.CambiarPassword.as_view(), name='cambiar_contraseña'),
    path('perfil/eliminar/<int:pk>/', views.EliminarPerfil.as_view(), name='eliminar_perfil'),
]