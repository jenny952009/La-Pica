from django import forms
from .models import Reserva  # Asegúrate de que el modelo esté correctamente importado



class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['codigo_reserva', 'nombre', 'apellido', 'email', 'telefono', 'numero_mesa', 'hora_comienzo', 'personas']

