from datetime import datetime
from socket import fromshare
from django import forms
import datetime


class Cargocasa(forms.Form):
    c_ubicacion=forms.CharField(max_length=50)
    c_ambientes=forms.IntegerField()
    c_precio=forms.IntegerField()
    c_contacto_nombre=forms.CharField(max_length=50)
    c_contacto_telefono=forms.IntegerField()
    c_contacto_email=forms.EmailField()
    c_fecha_alta=forms.DateField(initial=datetime.date.today) 


class Deptocarga(forms.Form):
    c_ubicacion=forms.CharField(max_length=50)
    c_ambientes=forms.IntegerField()
    c_precio=forms.IntegerField()
    c_contacto_nombre=forms.CharField(max_length=50)
    c_contacto_telefono=forms.IntegerField()
    c_contacto_email=forms.EmailField()
    c_fecha_alta=forms.DateField(initial=datetime.date.today)