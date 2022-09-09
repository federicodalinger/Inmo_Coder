from re import template
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
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

    path("login/", login_request, name="login_request"),
    path("signin/", signin_request, name="signin_request"),
    path("logout/", LogoutView.as_view(template_name="Inmo_Coder_App/templates/Inmo_Coder_App/logout.html"),name="logout")

]