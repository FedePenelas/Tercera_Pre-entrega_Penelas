from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    contacto = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    mensaje = models.CharField(max_length=120)

class DarEnAdopcion(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    contacto = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    mensaje = models.CharField(max_length=120, default='Valor predeterminado')

class Transito(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    contacto = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    mensaje = models.CharField(max_length=120, default='Valor predeterminado')

class Donante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    contacto = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    mensaje = models.CharField(max_length=120, default='Valor predeterminado')
