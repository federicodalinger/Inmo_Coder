from http.client import HTTPResponse
from pickletools import read_unicodestring1
from django.shortcuts import render, HttpResponse

from Inmo_Coder_App.forms import Cargocasa,Deptocarga
from Inmo_Coder_App.models import Casas,Departamentos

# Create your views here.

def inicio (request):
    return render (request, "Inmo_Coder_App/inicio.html")


################# Views referida a CASAS: ################
def casas_cargar (request):
    if request.method == "POST":
        miformulario = Cargocasa(request.POST)
        if miformulario.is_valid():
            info = miformulario.cleaned_data
            v_ubicacion=info.get("ubicacion")
            v_ambientes=info.get("ambientes")
            v_precio=info.get("precio")
            v_contacto=info.get("contacto_nombre")
            v_telefono=info.get("contacto_telefono")
            v_email=info.get("contacto_email")
            v_fecha=info.get("fecha_alta")
            print("Entro")
                        
            casa = Casas(ubicacion=v_ubicacion,ambientes=v_ambientes,precio=v_precio,contacto_nombre=v_contacto,contacto_telefono=v_telefono,contacto_email=v_email,fecha_de_alta=v_fecha)
            casa.save()
            return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/inicio.html",{"mensaje":"Casa creada"})
        else:
            return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/inicio.html",{"mensaje":"Error en la carga del form"})
    else:
        miformulario=Cargocasa()
        print("hola")
        return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/casas_cargar.html", {"miformulario":miformulario})

#############################################################################

def casas_buscar (request):

    return render (request, "Inmo_Coder_App/templates/Inmo_Coder_App/casas_buscar.html")

def buscarcasa(request):
    respuesta=request.GET.get('ubicacion')
    casas = Casas.objects.filter(ubicacion=respuesta)
    print("HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    return render(request, "Inmo_Coder_App/templates/Inmo_Coder_App/resultado_casas.html", {"ubicacion":casas})
    #return HttpResponse(f"Casas con la ubicacion en: {respuesta}")


################# Views referida a DEPARTAMENTOS: ################
def departamentos_cargar (request):
    if request.method == "POST":
        miformulario = Deptocarga(request.POST)
        if miformulario.is_valid():
            info = miformulario.cleaned_data
            v_ubicacion=info.get("ubicacion")
            v_ambientes=info.get("ambientes")
            v_precio=info.get("precio")
            v_contacto=info.get("contacto_nombre")
            v_telefono=info.get("contacto_telefono")
            v_email=info.get("contacto_email")
            v_fecha=info.get("fecha_alta")

                        
            casa = Departamentos(ubicacion=v_ubicacion,ambientes=v_ambientes,precio=v_precio,contacto_nombre=v_contacto,contacto_telefono=v_telefono,contacto_email=v_email,fecha_de_alta=v_fecha)
            casa.save()
            return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/inicio.html",{"mensaje":"Departamento Creado"})
        else:
            return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/inicio.html",{"mensaje":"Error en creacion de departamento"})
    else:
        miformulario=Deptocarga()
        print("hola")
        return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/departamentos_cargar.html", {"miformulario":miformulario})



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