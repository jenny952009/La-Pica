from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'entrada': forms.TimeInput(attrs={'type': 'time'}),
            'salida': forms.TimeInput(attrs={'type': 'time'}),
            'entrada_almuerzo': forms.TimeInput(attrs={'type': 'time'}),
            'salida_almuerzo': forms.TimeInput(attrs={'type': 'time'}),
        }
