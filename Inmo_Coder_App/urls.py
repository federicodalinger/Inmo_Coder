from django.urls import path
from .views import *

# Aca vinculamos las urls con las views.

urlpatterns = [
    path("", inicio, name="inicio"), #para que no falle en el inicio

    path("casas_buscar/", casas_buscar, name="casas_buscar"),
    path("casas_cargar/", casas_cargar, name="casas_cargar"),
    path('buscarcasa/',buscarcasa, name='buscarcasa'),

    path("departamentos_buscar/", departamentos_buscar, name="departamentos_buscar"),
    path("departamentos_cargar/", departamentos_cargar, name="departamentos_cargar"),
    path('buscardepto/',buscardepto, name='buscardepto'),

    path("cocheras_buscar/", cocheras_buscar, name="cocheras_buscar"),
    path("cocheras_cargar/", cocheras_cargar, name="cocheras_cargar"),

    path("clientes_buscar/", clientes_buscar, name="clientes_buscar"),
    path("clientes_cargar/", clientes_buscar, name="clientes_cargar"),

]