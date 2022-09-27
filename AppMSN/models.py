from django.db import models
from distutils.command.upload import upload
from django.contrib.auth.models import User
# Create your models here.

class Mensajes(models.Model):
    usuarioA = models.CharField(max_length=50)
    usuarioB = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=500)
    Leido = models.BooleanField(default=False)

def __str__(self):
        #ESTO ES COMO VOY A VER MI BASE DE DATOS EN "ADMIN":
        return "usuarioA: " + self.usuarioA + " | usuarioB: " + str(self.usuarioB) + " | mensaje: " + str(self.mensaje) + " | Leido: " + self.Leido+ " |"