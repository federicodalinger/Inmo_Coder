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

from .models import Blog

class CocherasFormulario(forms.Form):
    ubicacion = forms.CharField(max_length=100)
    precio = forms.IntegerField() 
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
        
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contrase??a", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contrase??a", widget=forms.PasswordInput)
    #image = forms.ImageField()

    class Meta:
        model = User
        fields = ["username","email", "password1","password2"]
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar Email",max_length=100)
    password1 = forms.CharField(label="Contrase??a", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contrase??a", widget=forms.PasswordInput)
    #image = forms.ImageField()
    last_name=forms.CharField(label="Modificar Last Name")
    first_name=forms.CharField(label="Modificar First Name")
    class Meta:
        model = User #"password1","password2",
        fields = ["email", "last_name","first_name","password1","password2"]
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
