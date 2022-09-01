#<<<<<<< HEAD
from django.shortcuts import render
from .models import *
from Inmo_Coder_App.forms import CocherasFormulario, ClientesFormulario
#=======
from http.client import HTTPResponse
from pickletools import read_unicodestring1
from django.shortcuts import render, HttpResponse

from Inmo_Coder_App.forms import Cargocasa,Deptocarga
from Inmo_Coder_App.models import Casas,Departamentos
#>>>>>>> fede-branch

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
    titulo="Ubicacion, Cantidad Ambientes, Precio, Nombre de Contacto, Telefono de Contacto, Email, Fecha de Alta"
    return render(request, "Inmo_Coder_App/templates/Inmo_Coder_App/casas_buscar.html",{"titulo":titulo,"ubicacion":casas})
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

################################################################

def departamentos_buscar (request):
    return render (request, "Inmo_Coder_App/departamentos_buscar.html")

def buscardepto(request):
    respuesta=request.GET.get('ubicacion')
    depto = Departamentos.objects.filter(ubicacion=respuesta)
    #return render(request, "Inmo_Coder_App/templates/Inmo_Coder_App/resultado_deptos.html", {"ubicacion":depto})
    titulo="Ubicacion, Cantidad Ambientes, Precio, Nombre de Contacto, Telefono de Contacto, Email, Fecha de Alta"
    
    return render(request, "Inmo_Coder_App/departamentos_buscar.html",{"titulo":titulo,"ubicacion":depto})

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
    titulo = "Ubicación, Precio, Nombre, teléfono, E-mail"
    ubi=request.GET.get("ubicacion")
    cocheras=Cocheras.objects.filter(ubicacion=ubi)
    return render(request, "Inmo_Coder_App/cocheras_buscar.html", {"ubicacion":cocheras, "titulo":titulo})
    




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
    cabecera = "Busqueda de Clientes"
    return render (request, "Inmo_Coder_App/clientes_buscar.html", {"busqueda_nombre":cabecera})

def buscarclientes (request):
    cabecera = "Resultado de Búsqueda de Clientes"
    titulo = "Nombre, teléfono, E-mail"
    contacto=request.GET.get("contacto_nombre")
    cliente=Clientes.objects.filter(contacto_nombre=contacto)
    return render(request, "Inmo_Coder_App/clientes_buscar.html", {"contacto_nombre":cliente, "busqueda_nombre":cabecera, "titulo":titulo})

