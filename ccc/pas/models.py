# -*- coding: UTF-8 -*-

#         app: Control de Planes de Acción
#      modulo: pas.models
# descripcion: Modelos para Control de Planes de Acción
#       autor: Javier Sanchez Toledano
#       fecha: jueves, 2 de octubre de 2014


from django.db import models
from tinymce.models import HTMLField
import datetime
import magic
from django.utils.translation import ugettext as _


class Pipol (models.Model):
    class Meta:
        verbose_name = _('Pipol')
        verbose_name_plural = _('Personas')

    nombre = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s' % self.nombre


class TrackingFields(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

PROCESO = (
    (1, 'Planeación'),
    (2, 'Apoyo Soporte'),
    (3, 'Clave'),
    (4, 'MSA'),
    (5, 'SGC'),
)

TIPO = (
    (1, 'Reactivo'),
    (2, 'Incremental'),
    (3, 'Innovación'),
    (4, 'Avance'),
    (5, 'Transformación'),
)

DETECCION = (
    (1, 'Auditoria Interna'),
    (2, 'Auditoria Externa'),
    (3, 'Revisión por los Vocales'),
    (4, 'Quejas'),
    (5, 'Otros'),
)

MEJORA = (
    (1, 'Procesos'),
    (2, 'Servicio'),
    (3, 'Sistema')
)

A_ESTADO = (
    (1, 'Abierta'),
    (2, 'En Seguimiento'),
    (3, 'Quemada'),
    (4, 'Cerrada'),
    (5, 'Cerrada fuera de tiempo')
)


JPG = 'image/jpeg'
PDF = 'application/pdf'
PNG = 'image/png'


class Plan(models.Model):
    # #################################### #
    # I. Identificación del plan
    fecha_llenado = models.DateField(
        'Fecha de Llenado',
        default=datetime.date.today()
    )
    fecha_deteccion = models.DateField('Fecha de Detección')
    proceso = models.PositiveSmallIntegerField(choices=PROCESO)
    tipo = models.PositiveSmallIntegerField(choices=TIPO)
    deteccion = models.PositiveSmallIntegerField(choices=DETECCION)
    mejora = models.PositiveSmallIntegerField(choices=MEJORA)
    nombre = models.CharField(max_length=40)

    # #################################### #
    # II. Revisión
    redaccion = HTMLField(default='', blank=True, null=True)
    declaracion = HTMLField(default='', blank=True, null=True)
    evidencia = HTMLField(default='', blank=True, null=True)
    requisitos = HTMLField(default='', blank=True, null=True)
    relacionadas = HTMLField(default='', blank=True, null=True)

    # #################################### #
    # III. Responsabilidades
    informacion = models.CharField(max_length=30, blank=True, null=True)
    aplicacion = models.CharField(max_length=30, blank=True, null=True)
    responsable = models.CharField(max_length=30, blank=True, null=True)

    # #################################### #
    # IV. Reacción
    correccion = HTMLField(default="", blank=True, null=True)
    consecuencias = models.FileField(blank=True, null=True)
    reaccion_responsable = models.ForeignKey(
        Pipol, blank=True, null=True)
    reaccion_evidencia = models.FileField(blank=True, null=True)

    # #################################### #
    # V. Determinación de las Causas
    pescadito = models.FileField(blank=True, null=True)
    cincopq = models.FileField('5 Por qués', blank=True, null=True)
    causa_raiz = HTMLField(default='', blank=True, null=True)

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
        return u'%s' % self.nombre

    def tipo_mime(self):
        return magic.from_file(self.reaccion_evidencia.file.name, mime=True)


class Accion(models.Model):
    plan = models.ForeignKey(Plan)
    accion = HTMLField()
    recursos = HTMLField(blank=True, null=True)
    fecha = models.DateField()
    estado = models.PositiveSmallIntegerField(choices=A_ESTADO)
    responsable = models.ForeignKey(Pipol)

    def __unicode__(self):
        return u'%s - %s' % (self.id, self.plan)


class Seguimiento(TrackingFields, models.Model):
    accion = models.ForeignKey(Accion)
    descripcion = HTMLField()
    fecha = models.DateField()
    evidencia = models.FileField()
    responsable = models.CharField(max_length=30)

    def __unicode__(self):
        return self.id
