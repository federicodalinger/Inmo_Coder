from django.http import HttpResponse

def saludo(reauest): #En "reauest" va toda la info que trae del cliente
    return HttpResponse(
        '''Buenas!''')