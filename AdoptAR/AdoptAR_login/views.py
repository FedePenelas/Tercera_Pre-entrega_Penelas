from AdoptAR_login import forms, models
from .models import Account
from .forms import UserEditForm
from django.contrib.auth import login, authenticate
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
            form.save()
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
            return render(request, 'editar_account.html', {'form': form})

    form = forms.EditarUsuarioForm(
        initial={
            'email': usuario.email,
            'first_name': usuario.first_name,
            'last_name': usuario.last_name,
            'avatar': modelo_perfil.avatar
        }
    )
    return render(request, 'editar_account.html', {'form': form})

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
    template_name = 'logout_account.html'



@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})