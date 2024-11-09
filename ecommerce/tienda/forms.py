from django import forms
from .models import ReseñaRating


class ReseñaForm(forms.ModelForm):
    class Meta:
        model = ReseñaRating
        fields = ['titulo', 'reseña', 'rating']
        widgets = {
            'reseña': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu reseña aquí...'}),
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)], attrs={'class': 'form-control'})
        }
    
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if not (1 <= rating <= 5):
            raise forms.ValidationError("La calificación debe estar entre 1 y 5")
        return rating
    
""""
# codigo antiguo
class RevisarForm(forms.ModelForm):
    class Meta:
        model = RevisarRating
        fields = ['subject', 'review', 'rating']
"""