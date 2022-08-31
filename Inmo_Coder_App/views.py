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

        if form_cocheras.is_valid():
            informacion = form_cocheras.cleaned_data
            cochera = Cocheras(ubicacion=informacion['ubicacion'], precio=informacion['precio'], contacto_nombre=informacion['contacto_nombre'], contacto_telefono=informacion['contacto_telefono'], contacto_email=informacion['contacto_email'], fecha_de_alta=informacion['fecha_de_alta'])
            cochera.save()
            return render (request, "Inmo_Coder_App/inicio.html", {"mensaje":"Cochera Cargada"})
        else:
            return render (request, "Inmo_Coder_App/inicio.html", {"mensaje":"Error al cargar"})
    
    else:
        form_cocheras = CocherasFormulario()
        return render (request, "Inmo_Coder_App/cocheras_cargar.html", {"form_cocheras":form_cocheras})

def cocheras_buscar (request):
    return render (request, "Inmo_Coder_App/cocheras_buscar.html")

def buscarcocheras (request):
    ubi=request.GET["ubicacion"]
    cocheras=Cocheras.objects.filter(ubicacion=ubi)
    return render(request, "Inmo_Coder_App/cocheras_resultado.html", {"ubicacion":cocheras})
    




################# Views referida a CLIENTES: ################
def clientes_cargar (request):
    if request.method == 'POST':

        form_clientes = ClientesFormulario(request.POST)

        if form_clientes.is_valid():
            informacion = form_clientes.cleaned_data
            cliente = Clientes(motivo_descripcion=informacion['motivo_descripcion'], motivo_ubicacion=informacion['motivo_ubicacion'], motivo_precio=informacion['motivo_precio'], contacto_nombre=informacion['contacto_nombre'], contacto_telefono=informacion['contacto_telefono'], contacto_email=informacion['contacto_email'], fecha_de_alta=informacion['fecha_de_alta'])
            cliente.save()
            return render (request, "Inmo_Coder_App/inicio.html", {"mensaje":"Cliente Cargado"})
        else:
            return render (request, "Inmo_Coder_App/inicio.html", {"mensaje":"Error al cargar"})
    
    else:
        form_clientes = ClientesFormulario()
        return render (request, "Inmo_Coder_App/clientes_cargar.html", {"form_clientes":form_clientes})

def clientes_buscar (request):
    return render (request, "Inmo_Coder_App/clientes_buscar.html")

def buscarclientes (request):
    contacto=request.GET["contacto_nombre"]
    cliente=Clientes.objects.filter(contacto_nombre=contacto)
    return render(request, "Inmo_Coder_App/clientes_resultado.html", {"contacto_nombre":cliente})

