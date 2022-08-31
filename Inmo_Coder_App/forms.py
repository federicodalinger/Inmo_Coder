from datetime import datetime
from socket import fromshare
from django import forms
import datetime


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