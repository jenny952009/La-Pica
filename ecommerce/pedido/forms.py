from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre', 'apellido', 'telefono', 'email', 'direccion_1', 'direccion_2', 'pais', 'ciudad', 'region', 'pedido_nota']

  