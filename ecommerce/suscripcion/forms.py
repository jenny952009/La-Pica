from django import forms
from .models import Suscripcion

class SuscripcionForm(forms.ModelForm):
    class Meta:
        model = Suscripcion
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Suscripcion.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo ya está suscrito.")
        return email
