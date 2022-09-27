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

# Create your views here.

def inicio (request):
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
            return render(request,"Inmo_Coder_App/blog_crear.html",{"miformulario":miformulario, "mensaje":mensaje})
        else:
            miformulario=Blog_formulario_carga()
            mensaje="Error al cargar"
            return render(request,"Inmo_Coder_App/blog_crear.html",{"miformulario":miformulario, "mensaje":mensaje})
    else:
        miformulario=Blog_formulario_carga()
        return render(request,"Inmo_Coder_App/blog_crear.html", {"miformulario":miformulario})

def blog_listar(request):
    blogs=Blog.objects.all()

    if len(blogs)!=0:
        return render(request, "Inmo_Coder_App/pages.html", {"blogs": blogs})
    
    else:
        return render(request, "Inmo_Coder_App/pages.html", {"mensaje":"No hay páginas aún."})

def blog_ver(request, id):
    blog=Blog.objects.get(id=id)

    if blog.cuerpo_texto!="":
        return render(request, "Inmo_Coder_App/blog_ver.html", {"blog": blog})
    else:
        return render(request, "Inmo_Coder_App/blog_ver.html", {"mensaje":"No hay información aún (cuerpo vacío)."})

def blog_eliminar(request, id):
    blog=Blog.objects.get(id=id)
    blog.delete()
    blogs=Blog.objects.all()
    return render(request, "Inmo_Coder_App/pages.html", {"blogs": blogs})

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
            return render(request, "Inmo_Coder_App/pages.html", {"blogs": blogs})

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
        return render(request, "Inmo_Coder_App/blog_editar.html", {"miformulario":miformulario, "titulo":blog.titulo, "id": blog.id})
