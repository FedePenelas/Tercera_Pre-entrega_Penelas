from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    contacto = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    mensaje = models.CharField(max_length=120)
    def __str__(self):
        return f"Persona registrada: {self.nombre} {self.apellido}"

class DarEnAdopcion(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    contacto = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    mensaje = models.CharField(max_length=120, default='Valor predeterminado')
    def __str__(self):
        return f"Esta persona tiene una mascota para dar en adopción: {self.nombre} {self.apellido} {self.contacto}"

class Transito(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    contacto = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    mensaje = models.CharField(max_length=120, default='Valor predeterminado')
    def __str__(self):
        return f"Esta persona está interesada en prestar transito: {self.nombre} {self.apellido} {self.contacto}"

class Donante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    contacto = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    mensaje = models.CharField(max_length=120, default='Valor predeterminado')
    def __str__(self):
        return f"Esta persona es donante en AdoptAR: {self.nombre} {self.apellido}"
