from django import forms

class CocherasFormulario(forms.Form):
    ubicacion = forms.CharField(max_length=100)
    precio = forms.IntegerField() 
    contacto_nombre = forms.CharField(max_length=100)
    contacto_telefono = forms.IntegerField()
    contacto_email = forms.EmailField()
    fecha_de_alta = forms.DateField()

class ClientesFormulario(forms.Form):
    motivo_descripcion = forms.CharField(max_length=100) # Esto seria el motivo por el cual es nuestro cliente (por ejemplo: "venta de.../compra de.../alquiler de...").
    motivo_ubicacion = forms.CharField(max_length=100) # Aca indicamos la direccion de la operacion previa.
    motivo_precio = forms.IntegerField() # El monto por el cual se firmo la venta, compra, alquiler.
    contacto_nombre = forms.CharField(max_length=100)
    contacto_telefono = forms.IntegerField()
    contacto_email = forms.EmailField()
    fecha_de_alta = forms.DateField()