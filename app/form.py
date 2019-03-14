from django import forms
from .models import Tecnico, Cliente, Orden


class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = ('usuario', 'password', 'es_tecnico')


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'direccion', 'ciudad', 'comuna',
                  'telefono', 'correo', 'tecnicoAsignado')


class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ('cliente', 'fecha', 'horaInicio', 'horaTermino', 'idAscensor',
                  'modelo', 'fallas', 'reparaciones', 'piezasCambiadas', 'tecnico')

# ------------------------------------------------------------------
