from django.shortcuts import render
from .models import Alumno
# Create your views here.

def mostrar_Alumno(request):
    alumno = Alumno(nombre='Jose', email='Jose@test', clase='Funcional') 
    return render(request, '', {'nombre': alumno.nombre, 'email':alumno.email, 'clase':alumno.clase})