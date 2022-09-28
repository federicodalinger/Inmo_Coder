from .models import Avatar

def loadavatar(request):
    if request.user is not None:
                    
        lista=Avatar.objects.filter(user = request.user)
    
        if len(lista)!=0:
            imagen=lista[0].imagen.url
        else:
            imagen="https://static.thenounproject.com/png/801390-200.png"
        return imagen