from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['user', 'producto', 'pedido', 'pago', 'cantidad', 'total_venta', 'cupon', 'estado_pedido', 'region', 'pais']
