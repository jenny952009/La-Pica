from django import forms
from .models import Cuenta, UsuarioPerfil

class RegistrarForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese Contraseña',
        'class': 'form-control',
    }))
    confirmar_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirmar Contraseña',
        'class': 'form-control',
    }))

    class Meta:
        model = Cuenta
        fields = ['nombre', 'apellido', 'telefono', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrarForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['placeholder'] = 'Ingrese su nombre'
        self.fields['apellido'].widget.attrs['placeholder'] = 'Ingrese sus apellidos'
        self.fields['telefono'].widget.attrs['placeholder'] = 'Ingrese su número'
        self.fields['email'].widget.attrs['placeholder'] = 'Ingrese su email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrarForm, self).clean()
        password = cleaned_data.get('password')
        confirmar_password = cleaned_data.get('confirmar_password')

        if password != confirmar_password:
            raise forms.ValidationError(
                'Parece que la contraseña no coincide, verifique su información.'
            )


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ('nombre', 'apellido', 'telefono')

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class UsuarioPerfilForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False,error_messages={'invalid': ('Solo archivos de imagen.')}, widget=forms.FileInput )

    class Meta:
        model = UsuarioPerfil
        fields = ('direccion_1', 'direccion_2', 'ciudad', 'region', 'pais', 'profile_picture')

    def __init__(self, *args, **kwargs):
        super(UsuarioPerfilForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'



