from re import template
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
# Aca vinculamos las urls con las views.

urlpatterns = [
    path("", inicio, name="inicio"), 

    path("casas_buscar/", casas_buscar, name="casas_buscar"),
    path("casas_cargar/", casas_cargar, name="casas_cargar"),

    path("departamentos_buscar/", departamentos_buscar, name="departamentos_buscar"),
    path("departamentos_cargar/", departamentos_cargar, name="departamentos_cargar"),

    path("cocheras_buscar/", cocheras_buscar, name="cocheras_buscar"),
    path("cocheras_cargar/", cocheras_cargar, name="cocheras_cargar"),

    path("clientes_buscar/", clientes_buscar, name="clientes_buscar"),
    path("clientes_cargar/", clientes_cargar, name="clientes_cargar"),

    path("about/", about, name="about"),
    path("casas/list/", CasasList.as_view(), name="casas_listar"),
    path("casas/<pk>", CasasDetalle.as_view(), name="casas_detalle"),
    path("casas/nuevo/", CasasCreacion.as_view(), name='casas_crear'),
    path("casas/editar/<pk>", CasasUpdate.as_view(), name='casas_editar'),
    #path("^editar/(?P<id_casas>\d+)$", CasasUpdate.as_view(), name='casas_editar'),
    path("casas/borrar/<pk>", CasasDelete.as_view(), name='casas_borrar'),

    path("departamentos/list/", DepartamentosList.as_view(), name="departamentos_listar"),
    path("departamentos/<pk>", DepartamentosDetalle.as_view(), name="departamentos_detalle"),
    path("departamentos/nuevo/", DepartamentosCreacion.as_view(), name='departamentos_crear'),
    path("departamentos/editar/<pk>", DepartamentosUpdate.as_view(), name='departamentos_editar'),
    path("departamentos/borrar/<pk>", DepartamentosDelete.as_view(), name='departamentos_borrar'),

    path("cocheras/list/", CocherasList.as_view(), name="cocheras_listar"),
    path("cocheras/<pk>", CocherasDetalle.as_view(), name="cocheras_detalle"),
    path("cocheras/nuevo/", CocherasCreacion.as_view(), name='cocheras_crear'),
    path("cocheras/editar/<pk>", CocherasUpdate.as_view(), name='cocheras_editar'),
    path("cocheras/borrar/<pk>", CocherasDelete.as_view(), name='cocheras_borrar'),

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