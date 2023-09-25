from django.db import models

# Create your models here.

class Medico(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    especialidad = models.CharField(max_length=60)

class Paciente(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()

class Turno(models.Model):
    prestador = models.CharField(max_length=60)
    solicitante = models.CharField(max_length=60)
    fecha = models.DateField()
