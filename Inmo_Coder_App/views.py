from django.shortcuts import render

from Inmo_Coder_App.forms import Cargocasa
from Inmo_Coder_App.models import Casas

# Create your views here.

def inicio (request):
    return render (request, "Inmo_Coder_App/inicio.html")


################# Views referida a CASAS: ################
def casas_cargar (request):
    if request.method == "POST":
        miformulario = Cargocasa(request.POST)
        if miformulario.is_valid():
            info = miformulario.cleaned_data
            print(info)
            v_ubicacion=info.get("c_ubicacion")
            v_ambientes=info.get("c_ambientes")
            v_precio=info.get("c_precio")
            v_contacto=info.get("c_contacto_nombre")
            v_telefono=info.get("c_contacto_telefono")
            v_email=info.get("c_contacto_email")
            v_fecha=info.get("c_fecha_alta")

                        
            casa = Casas(ubicacion=v_ubicacion,ambientes=v_ambientes,precio=v_precio,contacto_nombre=v_contacto,contacto_telefono=v_telefono,contacto_email=v_email,fecha_de_alta=v_fecha)
            casa.save()
            return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/inicio.html")
    else:
        miformulario=Cargocasa()
        print("hola")
        return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/casas_cargar.html", {"miformulario":miformulario})



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