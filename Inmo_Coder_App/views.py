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


from Inmo_Coder_App.forms import Cargocasa,Deptocarga, CocherasFormulario, ClientesFormulario
from Inmo_Coder_App.forms import Blog_formulario_carga
# from Inmo_Coder_App.models import Casas,Departamentos
#>>>>>>> fede-branch

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout, authenticate
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
            return render (request, "Inmo_Coder_App/clientes_cargar.html", {"form_clientes":form_clientes, "mensaje":mensaje,"imagen":loadavatar(request),"chat":haymensaje(request)})
        else:
            form_clientes = ClientesFormulario()
            mensaje="Error al cargar"
            return render (request, "Inmo_Coder_App/clientes_cargar.html", {"form_clientes":form_clientes, "mensaje":mensaje,"imagen":loadavatar(request),"chat":haymensaje(request)})
    
    else:
        form_clientes = ClientesFormulario()
        return render (request, "Inmo_Coder_App/clientes_cargar.html", {"form_clientes":form_clientes,"imagen":loadavatar(request),"chat":haymensaje(request)})

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

        return render (request, "Inmo_Coder_App/clientes_buscar.html", {"clientes":clientes, "titulo":titulo, "mensaje":mensaje_alerta,"imagen":loadavatar(request),"chat":haymensaje(request)})
    else:
        ocultar_contenido_inicial=True
        return render (request, "Inmo_Coder_App/clientes_buscar.html", {"ocultar_contenido_inicial":ocultar_contenido_inicial,"imagen":loadavatar(request),"chat":haymensaje(request)})


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
    
            return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/inicio.html",{"mensaje":f"Usuario {username} creado"})

    else:
        form = UserRegisterForm()
    return render(request, "Inmo_Coder_App/templates/Inmo_Coder_App/signin.html",{"form": form,"imagen": loadavatar(request),"chat":haymensaje(request)})

#@login_required
def editarperfil(request):

    usuario=request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            #informacion = form.cleaned_data
            usuario.email = form.cleaned_data["email"]
            usuario.password1 = form.cleaned_data["password1"]
            usuario.password2 = form.cleaned_data["password2"]
            usuario.last_name = form.cleaned_data["last_name"]
            usuario.first_name = form.cleaned_data["first_name"]
            usuario.save()

            return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/inicio.html",{"mensaje":f"Perfil de {usuario} editado","imagen":loadavatar(request),"chat":haymensaje(request)})

    else:
        form = UserEditForm(instance=usuario)
    return render(request,"Inmo_Coder_App/templates/Inmo_Coder_App/editarperfil.html",{"usuario":usuario,"form":form,"imagen":loadavatar(request),"chat":haymensaje(request)})

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


###PARA CLASES BASADAS EN VISTAS

class CasasList(ListView):
    model=Casas
    template_name="Inmo_Coder_App/leerCasas.html"


class CasasDetalle(DetailView):
    model=Casas
    template_name="Inmo_Coder_App/casas_detalle.html"

class CasasCreacion(CreateView):
    model = Casas
    success_url = reverse_lazy('casas_listar')
    fields=['ubicacion', 'ambientes', 'precio', 'contacto_nombre', 'contacto_telefono', 'contacto_email', 'fecha_de_alta']

class CasasUpdate(UpdateView):
    model = Casas
    success_url = reverse_lazy('casas_listar')
    fields=['ubicacion', 'ambientes', 'precio', 'contacto_nombre', 'contacto_telefono', 'contacto_email', 'fecha_de_alta']

class CasasDelete(DeleteView):
    model = Casas
    success_url = reverse_lazy('casas_listar')

class DepartamentosList(ListView):
    model=Departamentos
    template_name="Inmo_Coder_App/leerDepartamentos.html"

class DepartamentosDetalle(DetailView):
    model=Departamentos
    template_name="Inmo_Coder_App/departamentos_detalle.html"

class DepartamentosCreacion(CreateView):
    model = Departamentos
    success_url = reverse_lazy('departamentos_listar')
    fields=['ubicacion', 'ambientes', 'precio', 'contacto_nombre', 'contacto_telefono', 'contacto_email', 'fecha_de_alta']

class DepartamentosUpdate(UpdateView):
    model = Departamentos
    success_url = reverse_lazy('departamentos_listar')
    fields=['ubicacion', 'ambientes', 'precio', 'contacto_nombre', 'contacto_telefono', 'contacto_email', 'fecha_de_alta']

class DepartamentosDelete(DeleteView):
    model = Departamentos
    success_url = reverse_lazy('departamentos_listar')


class CocherasList(ListView):
    model=Cocheras
    template_name="Inmo_Coder_App/leerCocheras.html"

class CocherasDetalle(DetailView):
    model=Cocheras
    template_name="Inmo_Coder_App/cocheras_detalle.html"

class CocherasCreacion(CreateView):
    model = Cocheras
    success_url = reverse_lazy('cocheras_listar')
    fields=['ubicacion', 'precio', 'contacto_nombre', 'contacto_telefono', 'contacto_email', 'fecha_de_alta']

class CocherasUpdate(UpdateView):
    model = Cocheras
    success_url = reverse_lazy('cocheras_listar')
    fields=['ubicacion', 'precio', 'contacto_nombre', 'contacto_telefono', 'contacto_email', 'fecha_de_alta']

class CocherasDelete(DeleteView):
    model = Cocheras
    success_url = reverse_lazy('cocheras_listar')

class ClientesList(ListView):
    model=Clientes
    template_name="Inmo_Coder_App/leerClientes.html"

class ClientesDetalle(DetailView):
    model=Clientes
    template_name="Inmo_Coder_App/clientes_detalle.html"

class ClientesCreacion(CreateView):
    model = Clientes
    success_url = reverse_lazy('clientes_listar')
    fields=['motivo_descripcion', 'motivo_ubicacion', 'motivo_precio','contacto_nombre', 'contacto_telefono', 'contacto_email', 'fecha_de_alta']

class ClientesUpdate(UpdateView):
    model = Clientes
    success_url = reverse_lazy('clientes_listar')
    fields=['motivo_descripcion', 'motivo_ubicacion', 'motivo_precio','contacto_nombre', 'contacto_telefono', 'contacto_email', 'fecha_de_alta']

class ClientesDelete(DeleteView):
    model = Clientes
    success_url = reverse_lazy('clientes_listar')
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

        if request.user.is_authenticated :#or request.user != "AnonymousUser":
            return render (request, "Inmo_Coder_App/blog_ver.html",{"blog":blog, "imagen":loadavatar(request),"chat":haymensaje(request)})
        else:
            if request.user.is_authenticated :#or request.user != "AnonymousUser":
                return render (request, "Inmo_Coder_App/blog_ver.html",{"mensaje":"No hay información aún (cuerpo vacío).", "imagen":loadavatar(request),"chat":haymensaje(request)})
            else:
                return render (request, "Inmo_Coder_App/blog_ver.html")


    else:
        return render(request, "Inmo_Coder_App/blog_ver.html", {"mensaje":""})

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
