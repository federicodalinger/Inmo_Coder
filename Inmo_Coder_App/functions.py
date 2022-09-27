from .models import Avatar

def loadavatar(request):
    if request.user is not None:
                    
        lista=Avatar.objects.filter(user = request.user)
    
        if len(lista)!=0:
            imagen=lista[0].imagen.url
        else:
            imagen=None
        return imagen