from django.db import models

# Create your models here.

class Casas (models.Model):
    ubicacion = models.CharField(max_length=100)
    ambientes = models.IntegerField()
    
    contacto_nombre = models.CharField(max_length=100)
    contacto_telefono = models.IntegerField()
    contacto_email = models.EmailField()
    
    precio = models.IntegerField()

    fecha_de_alta = models.DateField()
    

class Departamentos (models.Model):
    ubicacion = models.CharField(max_length=100)
    ambientes = models.IntegerField()
    
    contacto_nombre = models.CharField(max_length=100)
    contacto_telefono = models.IntegerField()
    contacto_email = models.EmailField()
    
    precio = models.IntegerField()

    fecha_de_alta = models.DateField()

class Cocheras (models.Model):
    ubicacion = models.CharField(max_length=100)

    contacto_nombre = models.CharField(max_length=100)
    contacto_telefono = models.IntegerField()
    contacto_email = models.EmailField()
    
    precio = models.IntegerField() 

    fecha_de_alta = models.DateField()


class Clientes (models.Model):
    motivo_descripcion = models.CharField(max_length=100) # Esto seria el motivo por el cual es nuestro cliente (por ejemplo: "venta de.../compra de.../alquiler de...").
    motivo_ubicacion = models.CharField(max_length=100) # Aca indicamos la direccion de la operacion previa.
    motivo_precio = models.IntegerField() # El monto por el cual se firmo la venta, compra, alquiler.

    contacto_nombre = models.CharField(max_length=100)
    contacto_telefono = models.IntegerField()
    contacto_email = models.EmailField()

    fecha_de_alta = models.DateField()