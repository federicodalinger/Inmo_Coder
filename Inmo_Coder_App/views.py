from django.shortcuts import render
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
    return render (request, "Inmo_Coder_App/cocheras_cargar.html")

def cocheras_buscar (request):
    return render (request, "Inmo_Coder_App/cocheras_buscar.html")


################# Views referida a CLIENTES: ################
def clientes_cargar (request):
    return render (request, "Inmo_Coder_App/clientes_cargar.html")

def clientes_buscar (request):
    return render (request, "Inmo_Coder_App/clientes_buscar.html")



    '''    if request.method == 'POST':

        form_cocheras = CocherasFormulario(request.POST)

        if form_cocheras.is_valid:

            informacion = form_cocheras.cleaned_data

            cochera = Cocheras '''