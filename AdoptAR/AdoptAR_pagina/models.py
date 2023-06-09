from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=40)
    especie = models.CharField(max_length=40)
    edad = models.IntegerField()

class Adoptante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    contacto = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)

class Transito(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    contacto = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
