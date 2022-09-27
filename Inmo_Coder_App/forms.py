#<<<<<<< HEAD
#<<<<<<< HEAD
#=======
#>>>>>>> feligoi
from datetime import datetime
from django import forms
import datetime

from .models import Blog

class CocherasFormulario(forms.Form):
    ubicacion = forms.CharField(max_length=100)
    precio = forms.IntegerField() 
    contacto_nombre = forms.CharField(max_length=100)
    contacto_telefono = forms.IntegerField()
    contacto_email = forms.EmailField()
    fecha_de_alta = forms.DateField(initial=datetime.date.today)

class ClientesFormulario(forms.Form):
    motivo_descripcion = forms.CharField(max_length=100) # Esto seria el motivo por el cual es nuestro cliente (por ejemplo: "venta de.../compra de.../alquiler de...").
    motivo_ubicacion = forms.CharField(max_length=100) # Aca indicamos la direccion de la operacion previa.
    motivo_precio = forms.IntegerField() # El monto por el cual se firmo la venta, compra, alquiler.
    contacto_nombre = forms.CharField(max_length=100)
    contacto_telefono = forms.IntegerField()
    contacto_email = forms.EmailField()
    fecha_de_alta = forms.DateField(initial=datetime.date.today)
#=======
# from datetime import datetime
# from django import forms
# import datetime


class Cargocasa(forms.Form):
    ubicacion=forms.CharField(max_length=50)
    ambientes=forms.IntegerField()
    precio=forms.IntegerField()
    contacto_nombre=forms.CharField(max_length=50)
    contacto_telefono=forms.IntegerField()
    contacto_email=forms.EmailField()
    fecha_alta=forms.DateField(initial=datetime.date.today) 


class Deptocarga(forms.Form):
    ubicacion=forms.CharField(max_length=50)
    ambientes=forms.IntegerField()
    precio=forms.IntegerField()
    contacto_nombre=forms.CharField(max_length=50)
    contacto_telefono=forms.IntegerField()
    contacto_email=forms.EmailField()
    fecha_alta=forms.DateField(initial=datetime.date.today)
#>>>>>>> fede-branch

# PARA CKEDITOR ES NECESARIO USAR CLASES POR LO QUE ANDUVE VIENDO, POR ESO SE DEJA COMENTADO:
# class Blog_formulario_carga(forms.Form):
#     titulo = forms.CharField(max_length=50) 
#     sub_titulo = forms.CharField(max_length=50) 
#     cuerpo_texto = forms.CharField(max_length=200) 
#     autor = forms.CharField(max_length=50) 
#     fecha_creacion = forms.DateField(initial=datetime.date.today) 
#     imagen = forms.ImageField(label="Imagen") 

class DatePickerInput(forms.DateInput):
        input_type = 'date'

class Blog_formulario_carga(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('titulo','sub_titulo','cuerpo_texto', 'autor', 'fecha_creacion', 'imagen' )
        widgets = {'fecha_creacion' : DatePickerInput()}
