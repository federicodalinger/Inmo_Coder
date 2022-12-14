from distutils.command.upload import upload
from django.db import models
from ckeditor.fields import RichTextField

from django.contrib.auth.models import User
# Create your models here.

class Casas(models.Model):
    ubicacion = models.CharField(max_length=100)
    ambientes = models.IntegerField()
    precio = models.IntegerField()
    contacto_nombre = models.CharField(max_length=100)
    contacto_telefono = models.IntegerField()
    contacto_email = models.EmailField()
    fecha_de_alta = models.DateField()

    def __str__(self):
        #ESTO ES COMO VOY A VER MI BASE DE DATOS EN "ADMIN":
        return "Ubicacion: " + self.ubicacion + " | Ambientes: " + str(self.ambientes) + " | Precio: " + str(self.precio) + " | Contacto -> Nombre: " + self.contacto_nombre + ", Teléfono: " + str(self.contacto_telefono) + ", E-mail: " + self.contacto_email + " | Fecha de publicación: " + str(self.fecha_de_alta)  + " |"

class Departamentos (models.Model):
    ubicacion = models.CharField(max_length=100)
    ambientes = models.IntegerField()
    precio = models.IntegerField()
    
    contacto_nombre = models.CharField(max_length=100)
    contacto_telefono = models.IntegerField()
    contacto_email = models.EmailField()

    fecha_de_alta = models.DateField()

    def __str__(self):
        #ESTO ES COMO VOY A VER MI BASE DE DATOS EN "ADMIN":
        return "Ubicacion: " + self.ubicacion + " | Ambientes: " + str(self.ambientes) + " | Precio: " + str(self.precio) + " | Contacto -> Nombre: " + self.contacto_nombre + ", Teléfono: " + str(self.contacto_telefono) + ", E-mail: " + self.contacto_email + " | Fecha de publicación: " + str(self.fecha_de_alta)  + " |"

class Cocheras (models.Model):
    ubicacion = models.CharField(max_length=100)
    precio = models.IntegerField() 

    contacto_nombre = models.CharField(max_length=100)
    contacto_telefono = models.IntegerField()
    contacto_email = models.EmailField()
    
    fecha_de_alta = models.DateField()

    def __str__(self):
        #ESTO ES COMO VOY A VER MI BASE DE DATOS EN "ADMIN":
        return "Ubicacion: " + self.ubicacion + " | Precio: " + str(self.precio) + " | Contacto -> Nombre: " + self.contacto_nombre + ", Teléfono: " + str(self.contacto_telefono) + ", E-mail: " + self.contacto_email + " | Fecha de publicación: " + str(self.fecha_de_alta)  + " |"

class Blog (models.Model): # El .Models es para que herede el "models"
    titulo = models.CharField(max_length=50)
    sub_titulo = models.CharField(max_length=50)
    cuerpo_texto = RichTextField(blank=True, null=True)
    # cuerpo_texto = models.CharField(max_length=200)
    autor = models.CharField(max_length=50) 
    fecha_creacion = models.DateField() 
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True)

    def __str__(self):
        return "Título: " + self.titulo + " | Autor: " + str(self.autor) + " | Fecha creacion: " + str(self.fecha_creacion) + " |"

class Avatar (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

