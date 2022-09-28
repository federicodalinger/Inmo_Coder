#<<<<<<< HEAD
#<<<<<<< HEAD
#=======
#>>>>>>> feligoi
from datetime import datetime
from email.errors import MessageError
from email.policy import default
from django import forms
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    #image = forms.ImageField()

    class Meta:
        model = User
        fields = ["username","email", "password1","password2"]
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar Email",max_length=100)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    #image = forms.ImageField()
    last_name=forms.CharField(label="Modificar Last Name")
    first_name=forms.CharField(label="Modificar First Name")
    class Meta:
       model = User
       fields = ["email", "password1","password2","last_name","first_name"]
       help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
#class AvatarForm(forms.Form):
    imagen = forms.ImageField( error_messages={
               'required': 'Seleccione el Avatar', 'empty':'','invalid_image':'','missing':'','invalid':''
                })
    class Meta:
        model = forms
        fields=("imagen")
        help_texts = {k:"" for k in fields}