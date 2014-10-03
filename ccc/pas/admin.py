# -*- coding: utf-8 -*-
#    nombre: admin
#       app: pas
#      desc: interface de administración

from django.contrib import admin
from .models import Plan, Accion


# Register your models here.
class AccionInline(admin.StackedInline):
    model = Accion
    extra = 1


class PlanAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Identificación', {'fields': [
            'fecha_deteccion',
            'proceso', 'tipo',
            'deteccion', 'mejora',
            'slug'
        ]}),
        ('Revisión', {'fields': [
            'redaccion',
            'declaracion',
            'evidencia',
            'requisitos'], 'classes': ['collapse']}),
        ('Responsabilidades', {'fields': [
            'informacion', 'aplicacion',
            'responsable'], 'classes': ['collapse']}),
        ('Reacción', {'fields': [
            'correccion',
            'consecuencias'], 'classes': ['collapse']}),
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
