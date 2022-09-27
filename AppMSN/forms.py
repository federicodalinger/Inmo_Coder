from email.policy import default
from django import forms

class grabar_mensajes(forms.Form):
    usuarioA = forms.CharField(max_length=50)
    usuarioB = forms.CharField(max_length=50)
    mensaje = forms.CharField(max_length=500)
    leido = forms.BooleanField()

    
class mensaje_temp(forms.Form):
    usuarioB = forms.CharField(max_length=50, label="Usuario destinatario")
    mensaje = forms.CharField(max_length=500)
    