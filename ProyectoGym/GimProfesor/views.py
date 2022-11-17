from django.shortcuts import render
from .models import Profesor
# Create your views here.

def mostrar_profesores(request):
    profesor = Profesor(nombre='Pepe', email='Pepe@test', clase='Funcional') 
    return render(request, '', {'nombre': profesor.nombre, 'email':profesor.email, 'clase':profesor.clase})