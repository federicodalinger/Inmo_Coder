from django.shortcuts import render

# Create your views here.
from io import UnsupportedOperation
from urllib import request
from .models import *
from .forms import grabar_mensajes
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
            print(request.user.is_superuser)
            lista_mensajes=[]                         
            #lista=Mensajes.objects.filter(usuarioB = request.user, Leido=False)
            lista = Mensajes.objects.values_list("usuarioA","mensaje")
            for start in lista:
                print(start[0],start[1])
                lista_mensajes.append(start[0] +" " + start[1])

            print(lista_mensajes)
            if len(lista)==0:
                mensaje="Ustedes no tiene mensajes!"
                return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/inicio.html",{"mensajes":mensajes,"usuario": request.user,"imagen": loadavatar(request),"chat": haymensaje(request),"listamensajes":lista})
            else:
                print("hola"+haymensaje(request))
                Mensajes.objects.all().update(Leido=True)

                return render(request,"AppMSN/templates/mensajes.html",{"usuario": request.user,"imagen": loadavatar(request),"chat": haymensaje(request),"lista_mensajes":lista})
            return render(request,)
    else:
        print("Salio por el Else")
        return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/inicio.html",{"usuario": request.user,"imagen": loadavatar(request),"chat": haymensaje(request),"listamensajes":lista})

#def cargar_mensaje(request):
#        if request.method == "POST":
#            miformulario = grabar_mensajes(request.POST)
#            if miformulario.is_valid():
#                info = miformulario.cleaned_data
#                usuarioA=request.user
#                usuarioB=info.get("usuarioB")
#                mensaje=info.get("mensaje")
#                leido= False

#                text = Mensajes(usuarioA=usuarioA,usuarioB=usuarioB,mensaje=mensaje,Leidp=leido)
#                text.save()
#                miformulario=Cargocasa()
#                mensaje="Casa cargada"
#                return render(request,"Inmo_Coder_App/casas_cargar.html",{"miformulario":miformulario, "mensaje":mensaje,"imagen":loadavatar(request),"chat": haymensaje(request)})
#            else:
#                miformulario=Cargocasa()
#                mensaje="Error al cargar"
#                return render(request,"Inmo_Coder_App/casas_cargar.html",{"miformulario":miformulario, "mensaje":mensaje,"imagen":loadavatar(request),"chat": haymensaje(request)})
#        else:
#            miformulario=Cargocasa()
#            return render(request,"Inmo_Coder_App/casas_cargar.html", {"miformulario":miformulario,"imagen":loadavatar(request),"chat": haymensaje(request)})
