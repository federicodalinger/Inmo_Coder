#<<<<<<< HEAD
from urllib import request
from django.shortcuts import render
from .models import *
# from Inmo_Coder_App.forms import CocherasFormulario, ClientesFormulario
#=======
from http.client import HTTPResponse
from pickletools import read_unicodestring1
from django.shortcuts import render, HttpResponse

from Inmo_Coder_App.forms import Cargocasa,Deptocarga, CocherasFormulario, ClientesFormulario
# from Inmo_Coder_App.models import Casas,Departamentos
#>>>>>>> fede-branch

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm





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
                        
            casa = Casas(ubicacion=v_ubicacion,ambientes=v_ambientes,precio=v_precio,contacto_nombre=v_contacto,contacto_telefono=v_telefono,contacto_email=v_email,fecha_de_alta=v_fecha)
            casa.save()
            miformulario=Cargocasa()
            mensaje="Casa cargada"
            return render(request,"Inmo_Coder_App/casas_cargar.html",{"miformulario":miformulario, "mensaje":mensaje})
        else:
            miformulario=Cargocasa()
            mensaje="Error al cargar"
            return render(request,"Inmo_Coder_App/casas_cargar.html",{"miformulario":miformulario, "mensaje":mensaje})
    else:
        miformulario=Cargocasa()
        return render(request,"Inmo_Coder_App/casas_cargar.html", {"miformulario":miformulario})

def casas_buscar(request):
    if request.method == "POST":
        respuesta=request.POST.get('ubicacion')
        casas = Casas.objects.filter(ubicacion=respuesta)
        titulo = {
                "contacto_nombre":"Nombre", 
                "contacto_telefono":"Teléfono",
                "contacto_email":"E-mail",
                "ambientes":"Ambientes",
                "precio":"Precio", 
                "ubicacion":"Ubicación",
                "fecha_de_alta":"Fecha de inscripción"
                }
        
        mensaje_alerta=""
        if len(casas)==0:
            titulo = {}
            mensaje_alerta="Casa inexistente en la base de datos."

        return render (request, "Inmo_Coder_App/casas_buscar.html", {"titulo":titulo,"casas":casas, "mensaje":mensaje_alerta})
    else:
        ocultar_contenido_inicial=True
        return render (request, "Inmo_Coder_App/casas_buscar.html", {"ocultar_contenido_inicial":ocultar_contenido_inicial})

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
            miformulario=Deptocarga()
            mensaje="Departamento cargado"
            return render(request,"Inmo_Coder_App/departamentos_cargar.html",{"miformulario":miformulario, "mensaje":mensaje})
        else:
            miformulario=Deptocarga()
            mensaje="Error al cargar"
            return render(request,"Inmo_Coder_App/departamentos_cargar.html",{"miformulario":miformulario, "mensaje":mensaje})
    else:
        miformulario=Deptocarga()
        return render(request,"Inmo_Coder_App/departamentos_cargar.html", {"miformulario":miformulario})

def departamentos_buscar(request):
    if request.method == "POST":
        respuesta=request.POST.get('ubicacion')
        deptos = Departamentos.objects.filter(ubicacion=respuesta)
        titulo = {
                "contacto_nombre":"Nombre", 
                "contacto_telefono":"Teléfono",
                "contacto_email":"E-mail",
                "ambientes":"Ambientes",
                "precio":"Precio", 
                "ubicacion":"Ubicación",
                "fecha_de_alta":"Fecha de inscripción"
                }

        mensaje_alerta=""
        if len(deptos)==0:
            titulo = {}
            mensaje_alerta="Departamento inexistente en la base de datos."
        
        return render (request, "Inmo_Coder_App/departamentos_buscar.html", {"titulo":titulo,"deptos":deptos, "mensaje":mensaje_alerta})
    else:
        ocultar_contenido_inicial=True
        return render (request, "Inmo_Coder_App/departamentos_buscar.html", {"ocultar_contenido_inicial":ocultar_contenido_inicial})

################# Views referida a COCHERAS: ################
def cocheras_cargar (request):

    if request.method == 'POST':

        form_cocheras = CocherasFormulario(request.POST)

        if form_cocheras.is_valid():
            informacion = form_cocheras.cleaned_data
            cochera = Cocheras(ubicacion=informacion['ubicacion'], precio=informacion['precio'], contacto_nombre=informacion['contacto_nombre'], contacto_telefono=informacion['contacto_telefono'], contacto_email=informacion['contacto_email'], fecha_de_alta=informacion['fecha_de_alta'])
            cochera.save()
            form_cocheras = CocherasFormulario()
            mensaje="Cochera cargada"
            return render (request, "Inmo_Coder_App/cocheras_cargar.html", {"form_cocheras":form_cocheras, "mensaje":mensaje})
        else:
            form_cocheras = CocherasFormulario()
            mensaje="Error al cargar"
            return render (request, "Inmo_Coder_App/cocheras_cargar.html", {"form_cocheras":form_cocheras, "mensaje":mensaje})
    
    else:
        form_cocheras = CocherasFormulario()
        return render (request, "Inmo_Coder_App/cocheras_cargar.html", {"form_cocheras":form_cocheras})

def cocheras_buscar (request):
    if request.method == "POST":
        ubi=request.POST.get("ubicacion")
        cocheras=Cocheras.objects.filter(ubicacion=ubi)
        titulo = {
                "contacto_nombre":"Nombre", 
                "contacto_telefono":"Teléfono",
                "contacto_email":"E-mail",
                "precio":"Precio", 
                "ubicacion":"Ubicación",
                "fecha_de_alta":"Fecha de inscripción"
                }

        mensaje_alerta=""
        if len(cocheras)==0:
            titulo = {}
            mensaje_alerta="Cochera inexistente en la base de datos."

        return render (request, "Inmo_Coder_App/cocheras_buscar.html", {"cocheras":cocheras, "titulo":titulo, "mensaje":mensaje_alerta})
    else:
        ocultar_contenido_inicial=True
        return render (request, "Inmo_Coder_App/cocheras_buscar.html", {"ocultar_contenido_inicial":ocultar_contenido_inicial})

################# Views referida a CLIENTES: ################
def clientes_cargar (request):
    if request.method == 'POST':

        form_clientes = ClientesFormulario(request.POST)

        if form_clientes.is_valid():
            informacion = form_clientes.cleaned_data
            cliente = Clientes(motivo_descripcion=informacion['motivo_descripcion'], motivo_ubicacion=informacion['motivo_ubicacion'], motivo_precio=informacion['motivo_precio'], contacto_nombre=informacion['contacto_nombre'], contacto_telefono=informacion['contacto_telefono'], contacto_email=informacion['contacto_email'], fecha_de_alta=informacion['fecha_de_alta'])
            cliente.save()
            form_clientes = ClientesFormulario()
            mensaje="Cliente cargado"
            return render (request, "Inmo_Coder_App/clientes_cargar.html", {"form_clientes":form_clientes, "mensaje":mensaje})
        else:
            form_clientes = ClientesFormulario()
            mensaje="Error al cargar"
            return render (request, "Inmo_Coder_App/clientes_cargar.html", {"form_clientes":form_clientes, "mensaje":mensaje})
    
    else:
        form_clientes = ClientesFormulario()
        return render (request, "Inmo_Coder_App/clientes_cargar.html", {"form_clientes":form_clientes})

def clientes_buscar (request):
    if request.method == "POST":
        contacto=request.POST.get("contacto_nombre")
        clientes=Clientes.objects.filter(contacto_nombre=contacto)
        # titulo = "Nombre, teléfono, E-mail"
        titulo = {
                "contacto_nombre":"Nombre", 
                "contacto_telefono":"Teléfono",
                "contacto_email":"E-mail",
                "motivo_descripcion":"Descripción de operación", 
                "motivo_ubicacion":"Ubicación",
                "fecha_de_alta":"Fecha de operación"
                }                              
                    
        mensaje_alerta=""
        if len(clientes)==0:
            titulo = {}
            mensaje_alerta="Cliente inexistente en la base de datos."

        return render (request, "Inmo_Coder_App/clientes_buscar.html", {"clientes":clientes, "titulo":titulo, "mensaje":mensaje_alerta})
    else:
        ocultar_contenido_inicial=True
        return render (request, "Inmo_Coder_App/clientes_buscar.html", {"ocultar_contenido_inicial":ocultar_contenido_inicial})


def login_request(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        print(form.error_messages)
        if form.is_valid():
            user = request.POST["username"]
            clave = request.POST["password"]

            usuario=authenticate(username=user, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "Inmo_Coder_App/templates/Inmo_Coder_App/inicio.html",{"mensaje":f"Bienvenido {usuario}"})
                #print("OK")
            else:
                return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/login.html",{"mensaje":"Usuario o contraseña invalida"})
                #print("usuario incorreto")
        else:
            return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/login.html",{"mensaje":"Usuario o contraseña invalida"})
            #print("formulario invalido")
    else:
        form = AuthenticationForm()
        #print("get")
        return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/login.html",{"form":form})

def signin_request(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/inicio.html",{"mensaje":f"Usuario {username} creado"})

    else:
        form = UserRegisterForm()
    return render(request, "Inmo_Coder_App/templates/Inmo_Coder_App/signin.html",{"form": form})
