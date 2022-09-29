#<<<<<<< HEAD
from io import UnsupportedOperation
from traceback import print_tb
from urllib import request
from django.shortcuts import render
from .models import *
from http.client import HTTPResponse
from pickletools import read_unicodestring1
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import permission_required


from Inmo_Coder_App.forms import Cargocasa,Deptocarga, CocherasFormulario
from Inmo_Coder_App.forms import Blog_formulario_carga
# from Inmo_Coder_App.models import Casas,Departamentos
#>>>>>>> fede-branch

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from .forms import AvatarForm, UserRegisterForm, UserEditForm
from AppMSN.views import mensajes, haymensaje
from .functions import loadavatar


# Create your views here.

def inicio (request):
    print(request.user)
    print(request.user.is_authenticated)

    if request.user.is_authenticated :#or request.user != "AnonymousUser":
    #if request.user is not None:
        return render (request, "Inmo_Coder_App/inicio.html",{"imagen":loadavatar(request),"chat":haymensaje(request)})
    else:
        return render (request, "Inmo_Coder_App/inicio.html")

################# Views referida a CASAS: ################
#DEJO TIPEADO EL PERMISO DE ADMIN EN CASO QUE SEA NECESARIO @permission_required("admin.create_post", login_url="/", raise_exception=True)
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
            return render(request,"Inmo_Coder_App/casas_cargar.html",{"miformulario":miformulario, "mensaje":mensaje,"imagen":loadavatar(request),"chat":haymensaje(request)})
        else:
            miformulario=Cargocasa()
            mensaje="Error al cargar"
            return render(request,"Inmo_Coder_App/casas_cargar.html",{"miformulario":miformulario, "mensaje":mensaje,"imagen":loadavatar(request),"chat":haymensaje(request)})
    else:
        miformulario=Cargocasa()
        return render(request,"Inmo_Coder_App/casas_cargar.html", {"miformulario":miformulario,"imagen":loadavatar(request),"chat":haymensaje(request)})

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

            if request.user.is_authenticated :#or request.user != "AnonymousUser":
                return render (request, "Inmo_Coder_App/casas_buscar.html", {"titulo":titulo, "mensaje":mensaje_alerta,"imagen":loadavatar(request),"chat":haymensaje(request)})
            else:
                return render (request, "Inmo_Coder_App/casas_buscar.html", {"titulo":titulo,"mensaje":mensaje_alerta})
        else:
            if request.user.is_authenticated :#or request.user != "AnonymousUser":
                return render (request, "Inmo_Coder_App/casas_buscar.html", {"titulo":titulo,"casas":casas, "mensaje":mensaje_alerta,"imagen":loadavatar(request),"chat":haymensaje(request)})
            else:
                return render (request, "Inmo_Coder_App/casas_buscar.html", {"titulo":titulo,"casas":casas})        

    else:
        ocultar_contenido_inicial=True

        if request.user.is_authenticated :#or request.user != "AnonymousUser":
            return render (request, "Inmo_Coder_App/casas_buscar.html", {"ocultar_contenido_inicial":ocultar_contenido_inicial,"imagen":loadavatar(request),"chat":haymensaje(request)})
        else:
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
            return render(request,"Inmo_Coder_App/departamentos_cargar.html",{"miformulario":miformulario, "mensaje":mensaje,"imagen":loadavatar(request),"chat":haymensaje(request)})
        else:
            miformulario=Deptocarga()
            mensaje="Error al cargar"
            return render(request,"Inmo_Coder_App/departamentos_cargar.html",{"miformulario":miformulario, "mensaje":mensaje,"imagen":loadavatar(request),"chat":haymensaje(request)})
    else:
        miformulario=Deptocarga()
        return render(request,"Inmo_Coder_App/departamentos_cargar.html", {"miformulario":miformulario,"imagen":loadavatar(request),"chat":haymensaje(request)})

def departamentos_buscar(request):
    global imagen
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
            
            if request.user.is_authenticated :#or request.user != "AnonymousUser":
                return render (request, "Inmo_Coder_App/departamentos_buscar.html", {"titulo":titulo, "mensaje":mensaje_alerta,"imagen":loadavatar(request),"chat":haymensaje(request)})
            else:
                return render (request, "Inmo_Coder_App/departamentos_buscar.html", {"titulo":titulo, "mensaje":mensaje_alerta})
        else:
            if request.user.is_authenticated :#or request.user != "AnonymousUser":
                return render (request, "Inmo_Coder_App/departamentos_buscar.html", {"titulo":titulo,"deptos":deptos, "mensaje":mensaje_alerta,"imagen":loadavatar(request),"chat":haymensaje(request)})
            else:
                return render (request, "Inmo_Coder_App/departamentos_buscar.html", {"titulo":titulo,"deptos":deptos})

    else:
        ocultar_contenido_inicial=True

        if request.user.is_authenticated :#or request.user != "AnonymousUser":
            return render (request, "Inmo_Coder_App/departamentos_buscar.html", {"ocultar_contenido_inicial":ocultar_contenido_inicial,"imagen":loadavatar(request),"chat":haymensaje(request)})
        else:
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
            return render (request, "Inmo_Coder_App/cocheras_cargar.html", {"form_cocheras":form_cocheras, "mensaje":mensaje,"imagen":loadavatar(request),"chat":haymensaje(request)})
        else:
            form_cocheras = CocherasFormulario()
            mensaje="Error al cargar"
            return render (request, "Inmo_Coder_App/cocheras_cargar.html", {"form_cocheras":form_cocheras, "mensaje":mensaje,"imagen":loadavatar(request),"chat":haymensaje(request)})
    
    else:
        form_cocheras = CocherasFormulario()
        return render (request, "Inmo_Coder_App/cocheras_cargar.html", {"form_cocheras":form_cocheras,"imagen":loadavatar(request),"chat":haymensaje(request)})

def cocheras_buscar (request):
    global imagen
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

            if request.user.is_authenticated :#or request.user != "AnonymousUser":
                 return render (request, "Inmo_Coder_App/cocheras_buscar.html", {"titulo":titulo, "mensaje":mensaje_alerta,"imagen":loadavatar(request),"chat":haymensaje(request)})
            else:
                 return render (request, "Inmo_Coder_App/cocheras_buscar.html", {"titulo":titulo,"mensaje":mensaje_alerta}) 
        else:
            if request.user.is_authenticated :#or request.user != "AnonymousUser":
                return render (request, "Inmo_Coder_App/cocheras_buscar.html", {"titulo":titulo,"cocheras":cocheras, "mensaje":mensaje_alerta,"imagen":loadavatar(request),"chat":haymensaje(request)})
            else:
                return render (request, "Inmo_Coder_App/cocheras_buscar.html", {"titulo":titulo,"cocheras":cocheras}) 

    else:
        ocultar_contenido_inicial=True

        if request.user.is_authenticated :#or request.user != "AnonymousUser":
            return render (request, "Inmo_Coder_App/cocheras_buscar.html", {"ocultar_contenido_inicial":ocultar_contenido_inicial,"imagen":loadavatar(request),"chat":haymensaje(request)})
        else:
            return render (request, "Inmo_Coder_App/cocheras_buscar.html", {"ocultar_contenido_inicial":ocultar_contenido_inicial})


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
                if request.user.is_authenticated:
                    
                    lista=Avatar.objects.filter(user = request.user)
                    #print(len(lista))
                    if len(lista)!=0:
                        imagen=lista[0].imagen.url
                        #print(imagen)
                    else:
                        imagen=None
                    
                    return render(request, "Inmo_Coder_App/templates/Inmo_Coder_App/inicio.html",{"mensaje":f"Bienvenido {usuario}","usuario": usuario,"imagen": loadavatar(request),"chat":haymensaje(request)})
                else:
                    return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/login.html",{"mensaje":"Usuario o contraseña invalida"})                                    
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
    
            return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/inicio.html",{"mensaje":f"Usuario {username} creado","imagen": loadavatar(request),"chat":haymensaje(request)})
            #return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/inicio.html",{"mensaje":f"Usuario {username} creado"})
            return render(request,"Inmo_Coder_App/inicio.html", {"mensaje":f"Usuario {username} creado"})

    else:
        form = UserRegisterForm()
    #return render(request, "Inmo_Coder_App/templates/Inmo_Coder_App/signin.html",{"form": form,"imagen": loadavatar(request),"chat":haymensaje(request)})
    return render(request, "Inmo_Coder_App/signin.html", {"form":form, "imagen": loadavatar(request),"chat":haymensaje(request)})#,"imagen": loadavatar(request),"chat":haymensaje(request)})

##@login_required
def editarperfil(request):
    usuario=request.user
    if request.method == "POST":
        form=UserEditForm(request.POST) #, instance=usuario
        if form.is_valid():
            informacion = form.cleaned_data
            usuario.email = informacion["email"]
            usuario.password=make_password(informacion["password1"])
            #usuario.password1 = form.cleaned_data["password1"]
            #usuario.password2 = form.cleaned_data["password2"]
            usuario.first_name = form.cleaned_data["first_name"]
            usuario.last_name = form.cleaned_data["last_name"]
            usuario.save()

            return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/inicio.html",{"mensaje":f"Perfil de {usuario} editado","imagen":loadavatar(request),"chat":haymensaje(request)})
        else:
            return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/inicio.html",{"mensaje":f"Error en la edicion del perfil","imagen":loadavatar(request),"chat":haymensaje(request)})
    else:

        formulario = UserEditForm(instance=usuario)
        
        return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/editarperfil.html",{"usuario":usuario,"form":formulario,"imagen":loadavatar(request),"chat":haymensaje(request)})


######################################################################################

def cargaravatar(request):

    if request.method == "POST":
        
        miformulario = AvatarForm(request.POST, request.FILES)
        if miformulario.is_valid():
                if Avatar.objects.filter(user=request.user).exists() :
                   
                    avatarviejo = Avatar.objects.get(user=request.user)
                    print(avatarviejo.imagen)
                    if (avatarviejo.imagen):
                        avatarviejo.delete()
                    avatar=Avatar(user=request.user,imagen=miformulario.cleaned_data["imagen"])
                    avatar.save()
                    return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/inicio.html",{"mensaje":f"Avatar agregado con Exito","imagen":loadavatar(request),"chat":haymensaje(request)})
                else:
                    avatar=Avatar(user=request.user,imagen=miformulario.cleaned_data["imagen"])
                    avatar.save()
                    
                    return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/inicio.html",{"mensaje":f"Avatar agregado con Exito","imagen":loadavatar(request),"chat":haymensaje(request)})
    else:
        miformulario=AvatarForm()
    return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/cargaravatar.html",{"miformulario":miformulario,"imagen":loadavatar(request),"chat":haymensaje(request)})


###COMPLEMENTOS DE 1er PRE ENTREGA - CASAS

def casas_listar(request):
    casas=Casas.objects.all()
    if len(casas)!=0:
        if request.user.is_authenticated :#or request.user != "AnonymousUser":
            return render (request, "Inmo_Coder_App/casas_listar.html",{"casas":casas, "imagen":loadavatar(request),"chat":haymensaje(request)})
        else:
            return render (request, "Inmo_Coder_App/casas_listar.html", {"casas":casas})
    else:
        if request.user.is_authenticated :#or request.user != "AnonymousUser":
            return render (request, "Inmo_Coder_App/casas_listar.html",{"mensaje":"No hay casas registradas.", "imagen":loadavatar(request),"chat":haymensaje(request)})
        else:
            return render (request, "Inmo_Coder_App/casas_listar.html", {"mensaje":"No hay casas registradas."})

def casas_ver(request, id):
    casa=Casas.objects.get(id=id)
    if request.user.is_authenticated :#or request.user != "AnonymousUser":
        return render (request, "Inmo_Coder_App/casas_ver.html",{"casa":casa, "imagen":loadavatar(request),"chat":haymensaje(request)})
    else:
        return render (request, "Inmo_Coder_App/casas_ver.html",{"casa":casa})

def casas_confirm_delete(request, id):
    casa=Casas.objects.get(id=id)
    return render(request, "Inmo_Coder_App/casas_confirm_delete.html", {"casa": casa, "imagen":loadavatar(request),"chat":haymensaje(request)})

def casas_eliminar(request, id):
    casa=Casas.objects.get(id=id)
    casa.delete()
    casas=Casas.objects.all()
    if len(casas)!=0:
        return render(request, "Inmo_Coder_App/casas_listar.html", {"casas": casas, "imagen":loadavatar(request),"chat":haymensaje(request)})
    else:
        return render(request, "Inmo_Coder_App/casas_listar.html", {"mensaje":"Se borraron todas las casas.", "imagen":loadavatar(request),"chat":haymensaje(request)})

def casas_editar(request, id):
    casa=Casas.objects.get(id=id)
    if request.method=="POST":
        miformulario=Cargocasa(request.POST)
        if miformulario.is_valid():
            info=miformulario.cleaned_data
            casa.ubicacion=info["ubicacion"]
            casa.ambientes=info["ambientes"]
            casa.precio=info["precio"]
            casa.contacto_nombre=info["contacto_nombre"]
            casa.contacto_telefono=info["contacto_telefono"]
            casa.contacto_email=info["contacto_email"]
            casa.fecha_de_alta=info["fecha_alta"]
            casa.save()
            ### Muestro de nuevo haciendo un render de lo restante.
            casas=Casas.objects.all()
            return render(request, "Inmo_Coder_App/casas_listar.html", {"casas": casas, "imagen":loadavatar(request),"chat":haymensaje(request)})
    else:
        miformulario=Cargocasa(
            initial={
                "ubicacion":casa.ubicacion, "ambientes":casa.ambientes, "precio":casa.precio,
                "contacto_nombre":casa.contacto_nombre, "contacto_telefono":casa.contacto_telefono,
                "contacto_email":casa.contacto_email, "fecha_alta":casa.fecha_de_alta,})
        return render(request, "Inmo_Coder_App/casas_editar.html", {"miformulario":miformulario, "id": casa.id, "imagen":loadavatar(request),"chat":haymensaje(request)})

###COMPLEMENTOS DE 1er PRE ENTREGA - DEPARTAMENTOS

def departamentos_listar(request):
    departamentos=Departamentos.objects.all()
    if len(departamentos)!=0:
        if request.user.is_authenticated :#or request.user != "AnonymousUser":
            return render (request, "Inmo_Coder_App/departamentos_listar.html",{"departamentos":departamentos, "imagen":loadavatar(request),"chat":haymensaje(request)})
        else:
            return render (request, "Inmo_Coder_App/departamentos_listar.html", {"departamentos":departamentos})
    else:
        if request.user.is_authenticated :#or request.user != "AnonymousUser":
            return render (request, "Inmo_Coder_App/departamentos_listar.html",{"mensaje":"No hay departamentos registrados.", "imagen":loadavatar(request),"chat":haymensaje(request)})
        else:
            return render (request, "Inmo_Coder_App/departamentos_listar.html", {"mensaje":"No hay departamentos registrados."})

def departamentos_ver(request, id):
    departamento=Departamentos.objects.get(id=id)
    if request.user.is_authenticated :#or request.user != "AnonymousUser":
        return render (request, "Inmo_Coder_App/departamentos_ver.html",{"departamento":departamento, "imagen":loadavatar(request),"chat":haymensaje(request)})
    else:
        return render (request, "Inmo_Coder_App/departamentos_ver.html",{"departamento":departamento})

def departamentos_confirm_delete(request, id):
    departamento=Departamentos.objects.get(id=id)
    return render(request, "Inmo_Coder_App/departamentos_confirm_delete.html", {"departamento": departamento, "imagen":loadavatar(request),"chat":haymensaje(request)})

def departamentos_eliminar(request, id):
    departamento=Departamentos.objects.get(id=id)
    departamento.delete()
    departamentos=Departamentos.objects.all()
    if len(departamentos)!=0:
        return render(request, "Inmo_Coder_App/departamentos_listar.html", {"departamentos": departamentos, "imagen":loadavatar(request),"chat":haymensaje(request)})
    else:
        return render(request, "Inmo_Coder_App/departamentos_listar.html", {"mensaje":"Se borraron todos los departamentos.", "imagen":loadavatar(request),"chat":haymensaje(request)})

def departamentos_editar(request, id):
    departamento=Departamentos.objects.get(id=id)
    if request.method=="POST":
        miformulario=Deptocarga(request.POST)
        if miformulario.is_valid():
            info=miformulario.cleaned_data
            departamento.ubicacion=info["ubicacion"]
            departamento.ambientes=info["ambientes"]
            departamento.precio=info["precio"]
            departamento.contacto_nombre=info["contacto_nombre"]
            departamento.contacto_telefono=info["contacto_telefono"]
            departamento.contacto_email=info["contacto_email"]
            departamento.fecha_de_alta=info["fecha_alta"]
            departamento.save()
            ### Muestro de nuevo haciendo un render de lo restante.
            departamentos=Departamentos.objects.all()
            return render(request, "Inmo_Coder_App/departamentos_listar.html", {"departamentos": departamentos, "imagen":loadavatar(request),"chat":haymensaje(request)})
    else:
        miformulario=Deptocarga(
            initial={
                "ubicacion":departamento.ubicacion, "ambientes":departamento.ambientes, "precio":departamento.precio,
                "contacto_nombre":departamento.contacto_nombre, "contacto_telefono":departamento.contacto_telefono,
                "contacto_email":departamento.contacto_email, "fecha_alta":departamento.fecha_de_alta,})
        return render(request, "Inmo_Coder_App/departamentos_editar.html", {"miformulario":miformulario, "id": departamento.id, "imagen":loadavatar(request),"chat":haymensaje(request)})

###COMPLEMENTOS DE 1er PRE ENTREGA - COCHERAS

def cocheras_listar(request):
    cocheras=Cocheras.objects.all()
    if len(cocheras)!=0:
        if request.user.is_authenticated :#or request.user != "AnonymousUser":
            return render (request, "Inmo_Coder_App/cocheras_listar.html",{"cocheras":cocheras, "imagen":loadavatar(request),"chat":haymensaje(request)})
        else:
            return render (request, "Inmo_Coder_App/cocheras_listar.html", {"cocheras":cocheras})
    else:
        if request.user.is_authenticated :#or request.user != "AnonymousUser":
            return render (request, "Inmo_Coder_App/cocheras_listar.html",{"mensaje":"No hay cocheras registradas.", "imagen":loadavatar(request),"chat":haymensaje(request)})
        else:
            return render (request, "Inmo_Coder_App/cocheras_listar.html", {"mensaje":"No hay cocheras registradas."})

def cocheras_ver(request, id):
    cochera=Cocheras.objects.get(id=id)
    if request.user.is_authenticated :#or request.user != "AnonymousUser":
        return render (request, "Inmo_Coder_App/cocheras_ver.html",{"cochera":cochera, "imagen":loadavatar(request),"chat":haymensaje(request)})
    else:
        return render (request, "Inmo_Coder_App/cocheras_ver.html",{"cochera":cochera})

def cocheras_confirm_delete(request, id):
    cochera=Cocheras.objects.get(id=id)
    return render(request, "Inmo_Coder_App/cocheras_confirm_delete.html", {"cochera": cochera, "imagen":loadavatar(request),"chat":haymensaje(request)})

def cocheras_eliminar(request, id):
    cochera=Cocheras.objects.get(id=id)
    cochera.delete()
    cocheras=Cocheras.objects.all()
    if len(cocheras)!=0:
        return render(request, "Inmo_Coder_App/cocheras_listar.html", {"cocheras": cocheras, "imagen":loadavatar(request),"chat":haymensaje(request)})
    else:
        return render(request, "Inmo_Coder_App/cocheras_listar.html", {"mensaje":"Se borraron todas las cocheras.", "imagen":loadavatar(request),"chat":haymensaje(request)})

def cocheras_editar(request, id):
    cochera=Cocheras.objects.get(id=id)
    if request.method=="POST":
        miformulario=CocherasFormulario(request.POST)
        if miformulario.is_valid():
            info=miformulario.cleaned_data
            cochera.ubicacion=info["ubicacion"]
            cochera.precio=info["precio"]
            cochera.contacto_nombre=info["contacto_nombre"]
            cochera.contacto_telefono=info["contacto_telefono"]
            cochera.contacto_email=info["contacto_email"]
            cochera.fecha_de_alta=info["fecha_de_alta"]
            cochera.save()
            ### Muestro de nuevo haciendo un render de lo restante.
            cocheras=Cocheras.objects.all()
            return render(request, "Inmo_Coder_App/cocheras_listar.html", {"cocheras": cocheras, "imagen":loadavatar(request),"chat":haymensaje(request)})
    else:
        miformulario=CocherasFormulario(
            initial={
                "ubicacion":cochera.ubicacion, "precio":cochera.precio,
                "contacto_nombre":cochera.contacto_nombre, "contacto_telefono":cochera.contacto_telefono,
                "contacto_email":cochera.contacto_email, "fecha_de_alta":cochera.fecha_de_alta,})
        return render(request, "Inmo_Coder_App/cocheras_editar.html", {"miformulario":miformulario, "id": cochera.id, "imagen":loadavatar(request),"chat":haymensaje(request)})

################# Views referida a ABOUT (acerca de mi): ################

def about (request):
    if request.user.is_authenticated :#or request.user != "AnonymousUser":
        return render (request, "Inmo_Coder_App/about.html",{"imagen":loadavatar(request),"chat":haymensaje(request)})
    else:
        return render (request, "Inmo_Coder_App/about.html")

##################### Views referida a BLOGS ############################

def blog_crear(request):

    if request.method=="POST":
        miformulario = Blog_formulario_carga(request.POST, request.FILES)
        if miformulario.is_valid():
            info= miformulario.cleaned_data
            titulo= info["titulo"]
            sub_titulo= info["sub_titulo"]
            cuerpo_texto= info["cuerpo_texto"]
            autor= info["autor"]
            fecha_creacion= info["fecha_creacion"]
            imagen= info["imagen"]

            blog=Blog(titulo=titulo, sub_titulo=sub_titulo, cuerpo_texto=cuerpo_texto, autor=autor, fecha_creacion=fecha_creacion, imagen=imagen)
            blog.save()

            miformulario=Blog_formulario_carga()
            mensaje="Blog creado."
            return render(request,"Inmo_Coder_App/blog_crear.html",{"miformulario":miformulario, "mensaje":mensaje, "imagen":loadavatar(request),"chat":haymensaje(request)} )
        else:
            miformulario=Blog_formulario_carga()
            mensaje="Error al cargar"
            return render(request,"Inmo_Coder_App/blog_crear.html",{"miformulario":miformulario, "mensaje":mensaje, "imagen":loadavatar(request),"chat":haymensaje(request)})
    else:
        miformulario=Blog_formulario_carga()
        return render(request,"Inmo_Coder_App/blog_crear.html", {"miformulario":miformulario, "imagen":loadavatar(request),"chat":haymensaje(request)})

def blog_listar(request):
    blogs=Blog.objects.all()

    if len(blogs)!=0:

        if request.user.is_authenticated :#or request.user != "AnonymousUser":
            return render (request, "Inmo_Coder_App/pages.html",{"blogs":blogs, "imagen":loadavatar(request),"chat":haymensaje(request)})
        else:
            return render (request, "Inmo_Coder_App/pages.html", {"blogs":blogs})
    
    else:

        if request.user.is_authenticated :#or request.user != "AnonymousUser":
            return render (request, "Inmo_Coder_App/pages.html",{"mensaje":"No hay páginas aún.", "imagen":loadavatar(request),"chat":haymensaje(request)})
        else:
            return render (request, "Inmo_Coder_App/pages.html", {"mensaje":"No hay páginas aún."})

def blog_ver(request, id):
    blog=Blog.objects.get(id=id)

    if blog.cuerpo_texto!="":
        print("hay info en el cuerpo")
        if request.user.is_authenticated :#or request.user != "AnonymousUser":
            print("entre con usuario al render")
            return render (request, "Inmo_Coder_App/blog_ver.html",{"blog":blog, "imagen":loadavatar(request),"chat":haymensaje(request)})
        else:
            print("entre SIN usuario al render")
            return render (request, "Inmo_Coder_App/blog_ver.html",{"blog":blog})

    else:
        print("NO hay info en el cuerpo")
        if request.user.is_authenticated :#or request.user != "AnonymousUser":
            return render(request, "Inmo_Coder_App/blog_ver.html", {"mensaje":"No hay información aún (cuerpo vacío).", "imagen":loadavatar(request),"chat":haymensaje(request)})
        else:
            return render (request, "Inmo_Coder_App/blog_ver.html",{"mensaje":"No hay información aún (cuerpo vacío)."})


def blog_confirm_eliminar(request, id):
    blog=Blog.objects.get(id=id)
    return render(request, "Inmo_Coder_App/blog_confirm_eliminar.html", {"blog": blog, "imagen":loadavatar(request),"chat":haymensaje(request)})

def blog_eliminar(request, id):
    blog=Blog.objects.get(id=id)
    blog.delete()
    blogs=Blog.objects.all()
    if len(blogs)!=0:
        return render(request, "Inmo_Coder_App/pages.html", {"blogs": blogs, "imagen":loadavatar(request),"chat":haymensaje(request)})
    else:
        return render(request, "Inmo_Coder_App/pages.html", {"mensaje":"Se borraron todas las páginas.", "imagen":loadavatar(request),"chat":haymensaje(request)})

def blog_editar(request, id):
    blog=Blog.objects.get(id=id)

    if request.method=="POST":
        miformulario=Blog_formulario_carga(request.POST)
        if miformulario.is_valid():
            print("form is valid")
            info=miformulario.cleaned_data
            blog.titulo=info["titulo"]
            blog.sub_titulo=info["sub_titulo"]
            blog.cuerpo_texto=info["cuerpo_texto"]
            blog.autor=info["autor"]
            blog.fecha_creacion=info["fecha_creacion"]
            blog.imagen=info["imagen"]
            blog.save()
            print("guarda blog")
            print ("blog.imagen")

            ### Muestro de nuevo haciendo un render de lo restante.
            blogs=Blog.objects.all()
            return render(request, "Inmo_Coder_App/pages.html", {"blogs": blogs, "imagen":loadavatar(request),"chat":haymensaje(request)})

    else:
        miformulario=Blog_formulario_carga(
            initial={
                "titulo":blog.titulo,
                "sub_titulo":blog.sub_titulo,
                "cuerpo_texto":blog.cuerpo_texto,
                "autor":blog.autor,
                "fecha_creacion":blog.fecha_creacion,
                "imagen":blog.imagen,
            }
        )
        return render(request, "Inmo_Coder_App/blog_editar.html", {"miformulario":miformulario, "titulo":blog.titulo, "id": blog.id, "imagen":loadavatar(request),"chat":haymensaje(request)})



