from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path

from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'AppMSN'

urlpatterns = [
    path("mensajes/", mensajes, name="mensajes"), 
    path("enviarmensaje/", enviarmensaje, name="enviarmensaje"),
    path("mensaje_eliminar/<id>", mensaje_eliminar, name="mensaje_eliminar"),
    path("mensaje_responder/<id>", mensaje_responder, name="mensaje_responder"),
    ]