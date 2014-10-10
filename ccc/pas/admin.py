# -*- coding: utf-8 -*-
#    nombre: admin
#       app: pas
#      desc: interface de administración

from django.contrib import admin
from .models import Plan, Accion, Pipol


# Register your models here.
class PipolAdmin(admin.ModelAdmin):
    fields = ('nombre', )


class AccionInline(admin.TabularInline):
    model = Accion
    extra = 1


class PlanAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Identificación', {'fields': [
            'fecha_llenado',
            'fecha_deteccion',
            'proceso', 'tipo',
            'deteccion', 'mejora',
            'nombre'
        ]}),
        ('Reacción', {'fields': [
            'correccion',
            'consecuencias',
            'reaccion_responsable',
            'reaccion_evidencia'], 'classes': ['collapse']}),
        ('Revisión', {'fields': [
            'redaccion',
            'declaracion',
            'evidencia',
            'requisitos',
            'relacionadas'], 'classes': ['collapse']}),
        ('Responsabilidades', {'fields': [
            'informacion', 'aplicacion',
            'responsable'], 'classes': ['collapse']}),
        ('Determinación de las Causas', {'fields': [
            'pescadito', 'cincopq', 'causa_raiz'],
            'classes': ['collapse']}),
        ('Acciones', {'fields': [], 'classes': ['collapse']}),
        ('Seguimiento', {'fields': [], 'classes': ['collapse']}),
        ('Cierre', {'fields': [
            'eliminacion',
            'txt_eliminacion',
            'recurrencia',
            'txt_recuerrencia'], 'classes': ['collapse']}),
    )
    inlines = [AccionInline]

admin.site.register(Plan, PlanAdmin)
admin.site.register(Pipol, PipolAdmin)
