from django.template import Template, Context, loader
from django.http import HttpResponse
import datetime
from family.models import *

def bienvenida(responser):
    return HttpResponse("¡Bienvenido/a al curso de Django!")

def bienvenida_html(responser):
    return HttpResponse("<html><h1>Bienvenidos al curso de Django!!</h1></html>")

def bienvenida_html2(responser):
    response = """"
    <html>
    <h1>Bienvenidos al curso de Django!!</h1>
    <h2>¡Vamo' arriba!</h2>
    </html>
    """
    return HttpResponse(response)

def bienvenida_html3(responser):
    hoy = datetime.datetime.now()
    response = f"""
    <html>
    <h1>Bienvenidos al curso de Django!!</h1>
    <h2>¡Vamo' arriba!</h2>
    <h3>Hoy es {hoy}</h3>
    </html>
    """
    return HttpResponse(response)


def bienvenida_nombre(request, nombre, apellido):
    hoy = datetime.datetime.now()
    response = f"""
    <html>
    <h1>Bienvenido {nombre} {apellido} al curso de Django!!</h1>
    <h2>¡Vamo' arriba!</h2>
    <h3>Hoy es {hoy}</h3>
    </html>
    """
    return HttpResponse(response)

def nueva_entrada_info_familia_template(request,
                                        nombres,
                                        apellidos,
                                        fechaNacimiento,
                                        DNI,
                                        nombres_madre,
                                        apellidos_madre,
                                        nombres_padre,
                                        apellidos_padre):
    diccionario = {"nombres": nombres,
                   "apellidos": apellidos,
                   "fechaNacimiento": fechaNacimiento,
                   "DNI": int(DNI),
                   "nombres_madre": nombres_madre,
                   "apellidos_madre": apellidos_madre,
                   "nombres_padre": nombres_padre,
                   "apellidos_padre": apellidos_padre,} 
    plantilla = loader.get_template('C:/Users/danie/Dropbox/_coderhouse/2023/Python/Scripts/Clase_17/proyecto/proyecto/templates/msj_nueva_entrada_info_familia.html/msj_nueva_entrada_info_familia.html')
    nuevo_familiar = Familiar(nombres=nombres,
                              apellidos=apellidos,
                              fechaNacimiento=fechaNacimiento,
                              DNI=DNI, 
                              nombres_madre=nombres_madre,
                              apellidos_madre=apellidos_madre,
                              nombres_padre=nombres_padre,
                              apellidos_padre=apellidos_padre)
    nuevo_familiar.save()
    documento = plantilla.render(diccionario)
    return HttpResponse(documento) #ahora agregar a urls y despues: >python manage.py runserver
