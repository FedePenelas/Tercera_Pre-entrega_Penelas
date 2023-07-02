from AdoptAR_login import forms, models
from .models import Account
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView, LogoutView
from django.views.generic import DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from AdoptAR_login.forms import RegistroUsuarioForm, EditarUsuarioForm
from AdoptAR_pagina.forms import FormularioTransito, FormularioDonante, FormularioDarEnAdopcion, FormularioPersona
from AdoptAR_login.models import Avatar, Comentario
from .forms import ComentarioForm

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return render(request, "iniciar_sesion.html", {"mensaje":"Datos incorrectos"})

    form = AuthenticationForm()
    return render(request, "iniciar_sesion.html", {"form": form})

def register(request):
    if request.method == 'POST':
        form = forms.RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            account = Account(user=user)
            account.save()
            
            return redirect("listo")
        else:
            return render(request, "crear_cuenta.html", {"form":form})

    form = forms.RegistroUsuarioForm()
    return render(request, "crear_cuenta.html", {"form":form})

@login_required
def editar_perfil(request):
    usuario = request.user
    modelo_perfil, _ = models.Account.objects.get_or_create(user=usuario)
    if request.method == "POST":
        form = forms.EditarUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if data.get('first_name'):
                usuario.first_name = data.get('first_name')
            if data.get('last_name'):
                usuario.last_name = data.get('last_name')
            usuario.email = data.get('email') if data.get('email') else usuario.email
            modelo_perfil.avatar = data.get('avatar') if data.get('avatar') else modelo_perfil.avatar

            modelo_perfil.save()
            usuario.save()
            return redirect("mostrar_perfil")
        else:
            return render(request, 'editar_cuenta.html', {'form': form})

    form = forms.EditarUsuarioForm(
        initial={
            'email': usuario.email,
            'first_name': usuario.first_name,
            'last_name': usuario.last_name,
            'avatar': modelo_perfil.avatar
        }
    )
    return render(request, 'editar_cuenta.html', {'form': form})

@login_required
def mostrar_perfil(request):
    return render(request, 'mostrar_cuenta.html')

class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'cambiar_contraseña.html'
    success_url = reverse_lazy("mostrar_cuenta")

class EliminarPerfil(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("index")
    template_name = 'eliminar_account.html'

class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'cerrar_sesion.html'



def obtener_contexto_avatar(request):
    avatar_url = None
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.filter(user=request.user).first()
            if avatar:
                avatar_url = avatar.imagen.url
        except Avatar.DoesNotExist:
            pass
    return {'avatar_url': avatar_url}


@login_required
def logout_request(request):
    logout(request)
    return redirect("index")

@login_required
def agregar_comentario(request):
    contexto_avatar = obtener_contexto_avatar(request)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            contenido = form.cleaned_data['contenido']
            # Guarda el comentario en la base de datos o realiza cualquier otra lógica
            comentario = Comentario(usuario=request.user, contenido=contenido)
            comentario.save()
            return redirect('adoptar.html')
    else:
        form = ComentarioForm()
    return render(request, 'adoptar.html', {'form': form, **contexto_avatar})