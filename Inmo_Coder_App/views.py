from django.shortcuts import render
from .models import *
from Inmo_Coder_App.forms import CocherasFormulario, ClientesFormulario

# Create your views here.

def inicio (request):
    return render (request, "Inmo_Coder_App/inicio.html")


################# Views referida a CASAS: ################
def casas_cargar (request):
    return render (request, "Inmo_Coder_App/casas_cargar.html")

def casas_buscar (request):
    return render (request, "Inmo_Coder_App/casas_buscar.html")


################# Views referida a DEPARTAMENTOS: ################
def departamentos_cargar (request):
    return render (request, "Inmo_Coder_App/departamentos_cargar.html")

def departamentos_buscar (request):
    return render (request, "Inmo_Coder_App/departamentos_buscar.html")


################# Views referida a COCHERAS: ################
def cocheras_cargar (request):

    if request.method == 'POST':

        form_cocheras = CocherasFormulario(request.POST)

        if form_cocheras.is_valid:

            informacion = form_cocheras.cleaned_data

            cochera = Cocheras(ubicacion=informacion['ubicacion'], precio=informacion['precio'], contacto_nombre=informacion['contacto_nombre'], contacto_telefono=informacion['contacto_telefono'], contacto_email=informacion['contacto_email'], fecha_de_alta=informacion['fecha_de_alta'])

            cochera.save()

    else:
        form_cocheras = CocherasFormulario()

    return render (request, "Inmo_Coder_App/cocheras_cargar.html", {"form_cocheras":form_cocheras})

def cocheras_buscar (request):
    return render (request, "Inmo_Coder_App/cocheras_buscar.html")


################# Views referida a CLIENTES: ################
def clientes_cargar (request):
    return render (request, "Inmo_Coder_App/clientes_cargar.html")

def clientes_buscar (request):
    return render (request, "Inmo_Coder_App/clientes_buscar.html")

