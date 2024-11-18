from django import forms
from .models import ReseñaRating

# Formulario para agregar una reseña al producto
class ReseñaForm(forms.ModelForm):
    class Meta:
        model = ReseñaRating   # Utiliza el modelo ReseñaRating
        fields = ['titulo', 'reseña', 'rating']
        
