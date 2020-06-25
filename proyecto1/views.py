"""
Este archivo sera una vista que se llamara para poder mostrar datos en la vista web.
Los metodos aqui son basicos y no tiene parametro de entreda.

"""

from django.http import HttpResponse
import datetime
from django.template import loader  # Esto es para poder cargar las plantillas (templates) => metodo saludo6
# from django.template.loader import get_template  # Asi se llama al metodo 'get_template' para usar muchos templates
from django.template import Template, Context  # para poder usar las plantilla y su contexto


# Este es un ejm de como pasar html
#  Este sera su enlaca en la web ==>> http://localhost:8000/saludo/
# def saludo(request):  # primera vista
#     return HttpResponse("""
#     <html>
#         <body>
#             <h1>Hola a todos mi primera pagina con django</h1>
#         </body>
#     </html>""")

# Este es otro ejm de pasar html
documento = """ <html>
                    <body>
                        <h1>Hola a todos mi primera pagina con django</h1>
                    </body>
                </html>"""


def saludo(request):  # primera vista
    return HttpResponse(documento)


#  Este sera su enlaca en la web ==>> http://localhost:8000/despedida/
def despedida(request):
    return HttpResponse("Hasta luego people.")


# ======================================================================================================================
# ======================================================================================================================

# Muestra la fecha del sistema
def dame_fecha(request):
    dame_actual = datetime.datetime.now()  # Obtiene la fecha del sistema
    documento_fecha = """ <html>
                        <body>
                            <h1>Fecha y hora actuales: %s</h1>
                        </body>
                    </html>""" % dame_actual
    return HttpResponse(documento_fecha)


# ======================================================================================================================
# ======================================================================================================================

# Aqui se le esta pasando un parametro 'anyo' para que este se reciba en la url path
def calcula_edad1(request, anyo):
    edad_actual = 40
    periodo = anyo - 2020
    edad_futura = edad_actual + periodo

    documento_fecha = """ <html>
                          <body>
                              <h1>En el año %s tendrás %s</h1>
                          </body>
                      </html>""" % (anyo, edad_futura)
    return HttpResponse(documento_fecha)


# Aqui se pasan dos parametros para que los reciba la url del path
def calcula_edad2(request, edad, anyo):
    edad_actual = edad
    periodo = anyo - 2020
    edad_futura = edad_actual + periodo

    documento_fecha = """ <html>
                          <body>
                              <h1>En el año %s tendrás %s</h1>
                          </body>
                      </html>""" % (anyo, edad_futura)
    return HttpResponse(documento_fecha)


# ======================================================================================================================
# ======================================================================================================================
# PLANTILLAS 1
# Aqui se cargara una plantilla al metodo que actua como una vista


def saludo2(request):
    # doc_externo = open("C:\D\Lenguajes\Django\proyecto1\proyecto1\templates\miplantilla.html")  # Se carga la plantilla
    doc_externo = open("C:/D/Lenguajes/Django/proyecto1/proyecto1/templates/miplantilla.html")  # Se carga la plantilla

    plt = Template(doc_externo.read())  # Se crea un objeto de tipo templates para cargar la plantilla
    doc_externo.close()  # Se cierra el documento

    ctx = Context()  # Se crea el contexto para la plantilla

    documento_p = plt.render(ctx)  # se crea el renderizado de la pagina y se le pasa el contexto

    return HttpResponse(documento_p)


#  C:\D\Lenguajes\Django\proyecto1\proyecto1\templates

# ======================================================================================================================
# ======================================================================================================================
# PLANTILLAS 2

#  Aqui se trabajara con templates dinamicas

def saludo3(request):
    nombre = "tomas"
    apellido = "estrada"
    mi_fecha = datetime.datetime.now()

    doc_externo = open("C:/D/Lenguajes/Django/proyecto1/proyecto1/templates/miplantilla2.html")  # Se carga la plantilla

    plt = Template(doc_externo.read())  # Se crea un objeto de tipo templates para cargar la plantilla
    doc_externo.close()  # Se cierra el documento

    # Se crea el contexto para la plantilla y un diccionario para poder pasar los datos a la pagina miplantilla2.html
    diccionario1 = {"nombre_persona": nombre, "apellido": apellido, "fecha": mi_fecha}
    ctx = Context(diccionario1)

    documento_p = plt.render(ctx)  # se crea el renderizado de la pagina y se le pasa el contexto

    return HttpResponse(documento_p)


# ===========================================================
#  Trabajando con una clase para pasarle los valores a la pagina

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo4(request):
    p1 = Persona("Enrique", "Torres")

    mi_fecha = datetime.datetime.now()

    doc_externo = open("C:/D/Lenguajes/Django/proyecto1/proyecto1/templates/miplantilla2.html")  # Se carga la plantilla

    plt = Template(doc_externo.read())  # Se crea un objeto de tipo templates para cargar la plantilla
    doc_externo.close()  # Se cierra el documento

    # Se crea el contexto para la plantilla y un diccionario para poder pasar los datos a la pagina miplantilla2.html
    diccionario1 = {"nombre_persona": p1.nombre, "apellido": p1.apellido, "fecha": mi_fecha}
    ctx = Context(diccionario1)

    documento_p = plt.render(ctx)  # se crea el renderizado de la pagina y se le pasa el contexto

    return HttpResponse(documento_p)


# ======================================================================================================================
# ======================================================================================================================
# PLANTILLAS 3

#  Aqui se pasaran listas de datos a la pagina

def saludo5(request):
    p2 = Persona("Luis", "Silva")
    lista1 = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    lista2 = []

    mi_fecha = datetime.datetime.now()

    doc_externo = open("C:/D/Lenguajes/Django/proyecto1/proyecto1/templates/miplantilla2.html")  # Se carga la plantilla
    plt = Template(doc_externo.read())  # Se crea un objeto de tipo templates para cargar la plantilla
    doc_externo.close()  # Se cierra el documento

    # Se crea el contexto para la plantilla y un diccionario para poder pasar los datos a la pagina miplantilla2.html
    diccionario1 = {"nombre_persona": p2.nombre, "apellido": p2.apellido, "fecha": mi_fecha, "temas": lista1,
                    "temas2": lista2}
    ctx = Context(diccionario1)

    documento_p = plt.render(ctx)  # se crea el renderizado de la pagina y se le pasa el contexto

    return HttpResponse(documento_p)


# ======================================================================================================================
# ======================================================================================================================
# PLANTILLAS 4 - CARGADORES DE PLANTILLAS

"""Aqui se vera como cargar una o varias templates de forma mas optima para no usar 'close()' o el 'open()' que son 
metodos que estan consumiento muchos recursos.

Para ello hay que ir al archivo 'setting.py' y buscar la lista 'TEMPLATES' y dentro de el se vera otra lista interna
llamada 'DIRS' que aqui se contendra todos los directorios que contengan las paginas web(plantillas - templates) 

Usando esta forma se ahorra varias lineas de codigo y se optimiza todo ya que aqui ya no se usaria un contexto
"""


def saludo6(request):
    p3 = Persona("Esther", "Galdeano")
    lista1 = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    lista2 = []

    mi_fecha = datetime.datetime.now()

    # Aqui se ubica el template por medio del archivo 'setting.py' y el metodo indicado
    doc_externo = loader.get_template('miplantilla2.html')

    # Se crea el contexto para la plantilla y un diccionario para poder pasar los datos a la pagina miplantilla2.html
    diccionario1 = {"nombre_persona": p3.nombre, "apellido": p3.apellido, "fecha": mi_fecha, "temas": lista1,
                    "temas2": lista2}

    documento_p = doc_externo.render(diccionario1)  # se crea el renderizado de la pagina y se le pasa el contexto

    return HttpResponse(documento_p)

# ======================================================================================================================
# ======================================================================================================================
