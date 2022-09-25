from django.urls import path
from .views import *

# Aca vinculamos las urls con las views.

urlpatterns = [
    path("", inicio, name="inicio"), #para que no falle en el inicio

    path("casas_buscar/", casas_buscar, name="casas_buscar"),
    path("casas_cargar/", casas_cargar, name="casas_cargar"),

    path("departamentos_buscar/", departamentos_buscar, name="departamentos_buscar"),
    path("departamentos_cargar/", departamentos_cargar, name="departamentos_cargar"),

    path("cocheras_buscar/", cocheras_buscar, name="cocheras_buscar"),
    path("cocheras_cargar/", cocheras_cargar, name="cocheras_cargar"),

    path("clientes_buscar/", clientes_buscar, name="clientes_buscar"),
    path("clientes_cargar/", clientes_cargar, name="clientes_cargar"),

    path("casas/list/", CasasList.as_view(), name="casas_listar"),
    #path("casas/<pk>", CasasDetalle.as_view(), name="casas_detalle"),
    path("casas/nuevo/", CasasCreacion.as_view(), name='casas_crear'),
    path("casas/editar/<pk>", CasasUpdate.as_view(), name='casas_editar'),
    path("casas/borrar/<pk>", CasasDelete.as_view(), name='casas_borrar'),

    path("departamentos/list/", DepartamentosList.as_view(), name="departamentos_listar"),
    path("departamentos/nuevo/", DepartamentosCreacion.as_view(), name='departamentos_crear'),
    path("departamentos/editar/<pk>", DepartamentosUpdate.as_view(), name='departamentos_editar'),
    path("departamentos/borrar/<pk>", DepartamentosDelete.as_view(), name='departamentos_borrar'),

    path("cocheras/list/", CocherasList.as_view(), name="cocheras_listar"),
    path("cocheras/nuevo/", CocherasCreacion.as_view(), name='cocheras_crear'),
    path("cocheras/editar/<pk>", CocherasUpdate.as_view(), name='cocheras_editar'),
    path("cocheras/borrar/<pk>", CocherasDelete.as_view(), name='cocheras_borrar'),

    path("clientes/list/", ClientesList.as_view(), name="clientes_listar"),
    path("clientes/nuevo/", ClientesCreacion.as_view(), name='clientes_crear'),
    path("clientes/editar/<pk>", ClientesUpdate.as_view(), name='clientes_editar'),
    path("clientes/borrar/<pk>", ClientesDelete.as_view(), name='clientes_borrar'),


]