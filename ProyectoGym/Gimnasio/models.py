from django.db import models

# Create your models here.

class Clases(models.Model):

    nombreClase = models.CharField(max_length=40)
    profesor = models.CharField(max_length=40)
    dias = models.CharField(max_length=40)

class Profesor(models.Model):

    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    clase = models.IntegerField()


class Alumno(models.Model):

    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    clase = models.IntegerField()