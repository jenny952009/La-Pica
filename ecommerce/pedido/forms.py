from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre', 'apellido', 'telefono', 'email', 'direccion_1', 'direccion_2', 'pais', 'ciudad', 'region', 'pedido_nota']

    
    def __init__(self, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)
        # Define cada campo como requerido
        for field in self.fields.values():
            field.required = True

#---------------admin--------dashboard--------

class FiltroVentasForm(forms.Form):
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Desde",
        required=False
    )
    fecha_fin = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Hasta",
        required=False
    )
    estado = forms.ChoiceField(
        choices=[
            ('', 'Todos'),
            ('New', 'Nuevo'),
            ('Accepted', 'Aceptado'),
            ('Completed', 'Completado'),
            ('Cancelled', 'Cancelado'),
        ],
        
        label="Estado",
        required=False
    )
