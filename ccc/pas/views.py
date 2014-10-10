# -*- coding: UTF-8 -*-

#         app: Planes de Acción y Seguimiento
#      modulo: ccc.pas.views
# descripcion: Vistas para manejar los planes de acción
#       autor: Javier Sanchez Toledano
#       fecha: miércoles, 1 de octubre de 2014


from .models import Plan
from .forms import PlanForm
from annoying.decorators import render_to
from django.http import HttpResponseRedirect


@render_to('index.html')
def home(request):
    planes = Plan.objects.all()
    titulo = u'Control de Planes de Acción y Seguimiento'
    return {
        'planes': planes,
        'title': titulo
    }


@render_to('plan.html')
def plan(request, id):
    plan = Plan.objects.get(pk=id)
    titulo = u'%s | Plan de Acción y Seguimiento' % plan.nombre
    return {
        'title': titulo,
        'plan': plan
    }


@render_to('add.html')
def add(request, pas_id=None):
    if pas_id:
        pas = Plan.objects.get(pk=pas_id)
    else:
        pas = Plan()
    if request.method == 'POST':
        form = PlanForm(request.POST, instance=pas)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            ruta = '/pas/'
            return HttpResponseRedirect(ruta)

    else:
        form = PlanForm(instance=pas)

    return {
        'title': 'Agregar nuevo PAS',
        'form': form
    }
