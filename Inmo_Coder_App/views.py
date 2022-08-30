from django.shortcuts import render

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