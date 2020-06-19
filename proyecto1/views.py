"""
Este archivo sera una vista que se llamara para poder mostrar datos en la vista web.
Los metodos aqui son basicos y no tiene parametro de entreda.

"""

from django.http import HttpResponse
import datetime

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
