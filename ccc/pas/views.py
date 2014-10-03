# -*- coding: UTF-8 -*-

#         app: Planes de Acción y Seguimiento
#      modulo: ccc.pas.views
# descripcion: Vistas para manejar los planes de acción
#       autor: Javier Sanchez Toledano
#       fecha: miércoles, 1 de octubre de 2014



from annoying.decorators import render_to

# Create your views here.

@render_to('index.html')
def home(request):
    titulo = 'Control de Planes de Acción y Seguimiento'
    return {'title':titulo}