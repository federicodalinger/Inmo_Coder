from re import template
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
# Aca vinculamos las urls con las views.

urlpatterns = [
    path("", inicio, name="inicio"), 

    path("casas_buscar/", casas_buscar, name="casas_buscar"),
    path("casas_cargar/", casas_cargar, name="casas_cargar"),
    path("casas_listar/", casas_listar, name="casas_listar"),
    path("casas_ver/<id>", casas_ver, name="casas_ver"),
    path("casas_confirm_delete/<id>", casas_confirm_delete, name="casas_confirm_delete"),
    path("casas_eliminar/<id>", casas_eliminar, name="casas_eliminar"),
    path("casas_editar/<id>", casas_editar, name="casas_editar"),

    path("departamentos_buscar/", departamentos_buscar, name="departamentos_buscar"),
    path("departamentos_cargar/", departamentos_cargar, name="departamentos_cargar"),
    path("departamentos_listar/", departamentos_listar, name="departamentos_listar"),
    path("departamentos_ver/<id>", departamentos_ver, name="departamentos_ver"),
    path("departamentos_confirm_delete/<id>", departamentos_confirm_delete, name="departamentos_confirm_delete"),
    path("departamentos_eliminar/<id>", departamentos_eliminar, name="departamentos_eliminar"),
    path("departamentos_editar/<id>", departamentos_editar, name="departamentos_editar"),

    path("cocheras_buscar/", cocheras_buscar, name="cocheras_buscar"),
    path("cocheras_cargar/", cocheras_cargar, name="cocheras_cargar"),
    path("cocheras_listar/", cocheras_listar, name="cocheras_listar"),
    path("cocheras_ver/<id>", cocheras_ver, name="cocheras_ver"),
    path("cocheras_confirm_delete/<id>", cocheras_confirm_delete, name="cocheras_confirm_delete"),
    path("cocheras_eliminar/<id>", cocheras_eliminar, name="cocheras_eliminar"),
    path("cocheras_editar/<id>", cocheras_editar, name="cocheras_editar"),

    path("clientes_buscar/", clientes_buscar, name="clientes_buscar"),
    path("clientes_cargar/", clientes_cargar, name="clientes_cargar"),

    path("about/", about, name="about"),



    # path("cocheras/list/", CocherasList.as_view(), name="cocheras_listar"),
    # path("cocheras/<pk>", CocherasDetalle.as_view(), name="cocheras_detalle"),
    # path("cocheras/nuevo/", CocherasCreacion.as_view(), name='cocheras_crear'),
    # path("cocheras/editar/<pk>", CocherasUpdate.as_view(), name='cocheras_editar'),
    # path("cocheras/borrar/<pk>", CocherasDelete.as_view(), name='cocheras_borrar'),

    path("clientes/list/", ClientesList.as_view(), name="clientes_listar"),
    path("clientes/<pk>", ClientesDetalle.as_view(), name="clientes_detalle"),
    path("clientes/nuevo/", ClientesCreacion.as_view(), name='clientes_crear'),
    path("clientes/editar/<pk>", ClientesUpdate.as_view(), name='clientes_editar'),
    path("clientes/borrar/<pk>", ClientesDelete.as_view(), name='clientes_borrar'),


    path("blog_crear/", blog_crear, name="blog_crear"),
    path("pages/", blog_listar, name="blog_listar"),
    path("blog_ver/<id>", blog_ver, name="blog_ver"),
    path("blog_confirm_eliminar/<id>", blog_confirm_eliminar, name="blog_confirm_eliminar"),
    path("blog_eliminar/<id>", blog_eliminar, name="blog_eliminar"),
    path("blog_editar/<id>", blog_editar, name="blog_editar"),
    path("login/", login_request, name="login_request"),
    path("signin/", signin_request, name="signin_request"),
    path("logout/", LogoutView.as_view(template_name="Inmo_Coder_App/templates/Inmo_Coder_App/logout.html"),name="logout"),
    path("editarperfil/", editarperfil, name="editarperfil"),
    path("cargaravatar/", cargaravatar, name="cargaravatar"),
]