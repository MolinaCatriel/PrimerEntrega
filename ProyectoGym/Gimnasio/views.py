from django.shortcuts import render
from django.http import HttpResponse
from .models import Clases
# Create your views here.


def mostrar_clases (request):
    clases = Clases(nombreClase='Funcional', profesor='Pepe', dias='Lunes')
    #mensaje = f'Hola, esta es la clase de {clases.nombreClase}, que la da el profesor {clases.profesor}, los dias {clases.dias}'
    return render(request, 'gimnasio.html', {'nombreClase': clases.nombreClase, 'profesor':clases.profesor, 'dias':clases.dias})