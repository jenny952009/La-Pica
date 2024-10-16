from django import forms
from .models import RevisarRating


class RevisarForm(forms.ModelForm):
    class Meta:
        model = RevisarRating
        fields = ['subject', 'review', 'rating']
