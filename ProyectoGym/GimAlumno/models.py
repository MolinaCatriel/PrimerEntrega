from django.db import models

# Create your models here.

class Alumno(models.Model):

    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    clase = models.IntegerField()