from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['usuario', 'pedido', 'pago', 'total', 'estado']
