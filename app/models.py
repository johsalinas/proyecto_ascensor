from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.

class Tecnico(models.Model):
    usuario = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    es_tecnico = models.BooleanField(default=False)
    es_administrador = models.BooleanField(default=False)

    def __str__(self):
        return '{} {} {} {}'.format(self.usuario, self.password, self.es_tecnico, self.es_administrador)

    class Meta:
        permissions = (
            ('es_tecnico', _('es tecnico')),
            ('es_administrador', _('es administrador')),
        )

class Cliente(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    telefono = models.PositiveIntegerField()
    correo = models.CharField(max_length=50)
    tecnicoAsignado = models.ManyToManyField(Tecnico)

    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.nombre, self.direccion, self.ciudad, self.comuna, self.telefono, self.correo, self.tecnicoAsignado)

class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, to_field="nombre", on_delete=models.CASCADE)
    fecha = models.DateField()
    horaInicio = models.TimeField()
    horaTermino = models.TimeField()
    idAscensor = models.PositiveIntegerField()
    modelo = models.PositiveIntegerField()
    fallas = models.CharField(max_length=100)
    reparaciones = models.CharField(max_length=100)
    piezasCambiadas = models.CharField(max_length=100)
    tecnico = models.ForeignKey(Tecnico, to_field="usuario", on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {} {}'.format(self.cliente, self.fecha, self.horaInicio, self.horaTermino, self.idAscensor, self.modelo, self.fallas, self.reparaciones, self.piezasCambiadas, self.tecnico)
