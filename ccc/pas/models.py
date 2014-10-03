# -*- coding: UTF-8 -*-

#         app: Control de Planes de Acción
#      modulo: pas.models
# descripcion: Modelos para Control de Planes de Acción
#       autor: Javier Sanchez Toledano
#       fecha: jueves, 2 de octubre de 2014


from django.db import models
from tinymce.models import HTMLField


class TrackingFields(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

PROCESO = (
    ('1', 'Planeación'),
    ('2', 'Apoyo Soporte'),
    ('3', 'Clave'),
    ('4', 'MSA'),
    ('5', 'SGC'),
)

TIPO = (
    ('1', 'Reactivo'),
    ('2', 'Incremental'),
    ('3', 'Innovación'),
    ('4', 'Avance'),
    ('5', 'Transformación'),
)

DETECCION = (
    ('1', 'Auditoria Interna'),
    ('2', 'Auditoria Externa'),
    ('3', 'Revisión por los Vocales'),
    ('4', 'Quejas'),
    ('5', 'Otros'),
)

MEJORA = (
    ('1', 'Procesos'),
    ('2', 'Servicio'),
    ('3', 'Sistema')
)

A_ESTADO = (
    ('1', 'Abierta'),
    ('2', 'En Seguimiento'),
    ('3', 'Quemada'),
    ('4', 'Cerrada'),
    ('5', 'Cerrada fuera de tiempo')
)


class Plan(TrackingFields, models.Model):
    # #################################### #
    # I. Identificación del plan
    fecha_deteccion = models.DateField('Fecha de Detección')
    proceso = models.PositiveSmallIntegerField(choices=PROCESO)
    tipo = models.PositiveSmallIntegerField(choices=TIPO)
    deteccion = models.PositiveSmallIntegerField(choices=DETECCION)
    mejora = models.PositiveSmallIntegerField(choices=MEJORA)
    slug = models.SlugField(unique_for_year=True)

    # #################################### #
    # II. Revisión
    redaccion = HTMLField()
    declaracion = HTMLField()
    evidencia = HTMLField()
    requisitos = HTMLField()

    # #################################### #
    # III. Responsabilidades
    informacion = models.CharField(max_length=30)
    aplicacion = models.CharField(max_length=30)
    responsable = models.CharField(max_length=30)

    # #################################### #
    # IV. Reacción
    correccion = HTMLField()
    consecuencias = models.FileField(blank=True, null=True)

    # #################################### #
    # V. Determinación de las Causas
    pescadito = models.FileField(blank=True, null=True)
    cincopq = models.FileField('5 Por qués', blank=True, null=True)
    causa_raiz = HTMLField()

    # #################################### #
    # VI. Implementación de Acciones

    # #################################### #
    # VII. Revisión de la eficacia de las acciones

    # #################################### #
    # VIII. Cierre
    eliminacion = models.BooleanField(default=False)
    txt_eliminacion = HTMLField(blank=True, null=True)
    recurrencia = models.BooleanField(default=False)
    txt_recuerrencia = HTMLField(blank=True, null=True)

    def __unicode__(self):
        return self.slug


class Accion(TrackingFields, models.Model):
    plan = models.ForeignKey(Plan)
    accion = HTMLField()
    recursos = HTMLField(blank=True, null=True)
    fecha = models.DateField()
    estado = models.PositiveSmallIntegerField(choices=A_ESTADO)

    def __unicode__(self):
        return '%s - %s' % (self.id, self.plan)


class Seguimiento(TrackingFields, models.Model):
    accion = models.ForeignKey(Accion)
    descripcion = HTMLField()
    fecha = models.DateField()
    evidencia = models.FileField()
    responsable = models.CharField(max_length=30)

    def __unicode__(self):
        return self.id
