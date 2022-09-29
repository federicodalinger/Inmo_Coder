from django.shortcuts import render

# Create your views here.
from io import UnsupportedOperation
from urllib import request
from .models import *
from .forms import grabar_mensajes, mensaje_temp
# from Inmo_Coder_App.forms import CocherasFormulario, ClientesFormulario
#=======
from http.client import HTTPResponse
from pickletools import read_unicodestring1
from django.shortcuts import render, HttpResponse

#from Inmo_Coder_App.views import loadavatar
# from Inmo_Coder_App.models import Casas,Departamentos
#>>>>>>> fede-branch

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout, authenticate
from Inmo_Coder_App.functions import loadavatar

# Create your views here.

def haymensaje(request):
    if request.user is not None:
                    
        lista=Mensajes.objects.filter(usuarioB = request.user, Leido=False)
    
        if len(lista)!=0:
            imagenmensaje="/media/imagenes/conmensaje.png"
        else:
            imagenmensaje="/media/imagenes/sinmensaje.png"
        return imagenmensaje


def mensajes(request):
    print("Entro a Mensajes de APPMSN")
    if request.method=="POST":  
        if request.user is not None:
            usuario_receptor=request.user
            mensajes_filtrados = Mensajes.objects.filter(usuarioB = usuario_receptor)

            if len(mensajes_filtrados)==0:
                mensaje="Usted no tiene mensajes!"
                return render(request,"AppMSN/templates/mensajes.html",{"mensaje":mensaje,"usuario": request.user,"imagen": loadavatar(request),"chat": haymensaje(request),"lista_mensajes":mensajes_filtrados})
            else:
                #print("hola"+haymensaje(request))
                Mensajes.objects.all().update(Leido=True)

                return render(request,"AppMSN/templates/mensajes.html",{"usuario": request.user,"imagen": loadavatar(request),"chat": haymensaje(request),"lista_mensajes":mensajes_filtrados})
            #return render(request,)
    else:
        #print("Salio por el Else")
        return render(request,"AppMSN/templates/mensajes.html",{"usuario": request.user,"imagen": loadavatar(request),"chat": haymensaje(request),"lista_mensajes":mensajes_filtrados})

def enviarmensaje(request):
        
        if request.method == "POST":
            miformulario = mensaje_temp(request.POST)
            if miformulario.is_valid():
                info = miformulario.cleaned_data
                usuarioA=request.user
                usuarioB=info.get("usuarioB")
                mensaje=info.get("mensaje")
                leido= False

                text = Mensajes(usuarioA=usuarioA,usuarioB=usuarioB,mensaje=mensaje,Leido=leido)
                text.save()
                miformulario=grabar_mensajes()
                mensaje="Mensaje Cargado"
                return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/inicio.html",{"miformulario":miformulario, "mensaje":mensaje,"imagen":loadavatar(request),"chat": haymensaje(request)})
            else:
                miformulario=grabar_mensajes()
                mensaje="Error al cargar"
                return render(request,"AppMSN/templates/enviar_mensaje.html",{"miformulario":miformulario, "mensaje":mensaje,"imagen":loadavatar(request),"chat": haymensaje(request)})
        else:
            miformulario=mensaje_temp()

            return render(request,"AppMSN/templates/enviar_mensaje.html", {"miformulario":miformulario,"imagen":loadavatar(request),"chat": haymensaje(request)})

def mensaje_eliminar(request, id):
    mensaje=Mensajes.objects.get(id=id)
    mensaje.delete()
    usuario_receptor=request.user
    mensajes_filtrados = Mensajes.objects.filter(usuarioB = usuario_receptor)
    if len(mensajes_filtrados)!=0:
        return render(request,"AppMSN/templates/mensajes.html",{"usuario": request.user,"imagen": loadavatar(request),"chat": haymensaje(request),"lista_mensajes":mensajes_filtrados})
    else:
        return render(request, "AppMSN/templates/mensajes.html", {"usuario": request.user, "imagen":loadavatar(request),  "mensaje":"Se borraron todos los mensajes.","chat":haymensaje(request)})

def mensaje_responder(request, id):
        mensaje=Mensajes.objects.get(id=id)
        persona_a_responder=mensaje.usuarioA
        print(persona_a_responder)

        if request.method == "POST":
            miformulario = mensaje_temp(request.POST)
            if miformulario.is_valid():
                info = miformulario.cleaned_data
                usuarioA=request.user
                usuarioB=info.get("usuarioB")
                mensaje=info.get("mensaje")
                leido= False

                text = Mensajes(usuarioA=usuarioA,usuarioB=usuarioB,mensaje=mensaje,Leido=leido)
                text.save()
                miformulario=grabar_mensajes()
                mensaje="Mensaje Cargado"
                return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/inicio.html",{"miformulario":miformulario, "mensaje":mensaje,"imagen":loadavatar(request),"chat": haymensaje(request)})
            else:
                miformulario=grabar_mensajes()
                mensaje="Error al cargar"
                return render(request,"AppMSN/templates/enviar_mensaje.html",{"miformulario":miformulario, "mensaje":mensaje,"imagen":loadavatar(request),"chat": haymensaje(request)})
        else:
            miformulario=mensaje_temp(
                initial={
                    "usuarioB":persona_a_responder,
                    "mensaje":"",
                }
            )

            return render(request,"AppMSN/templates/enviar_mensaje.html", {"miformulario":miformulario,"imagen":loadavatar(request),"chat": haymensaje(request)})
