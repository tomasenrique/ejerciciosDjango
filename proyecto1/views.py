"""
Este archivo sera una vista que se llamara para poder mostrar datos en la vista web.
Los metodos aqui son basicos y no tiene parametro de entreda.

"""

from django.http import HttpResponse


#  Este sera su enlaca en la web ==>> http://localhost:8000/saludo/
def saludo(request):  # primera vista
    return HttpResponse("Hola a todos mi primera pagina con django")


#  Este sera su enlaca en la web ==>> http://localhost:8000/despedida/
def despedida(request):
    return HttpResponse("Hasta luego people.")
