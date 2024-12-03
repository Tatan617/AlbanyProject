from django import forms
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductosForm(forms.ModelForm):
    class Meta:
        model=Productos
        fields = [
            'nombre',
            'categoria',
            'marca',
            'imagen',
            'detalle',
            'precio',
            'marca',
            'stock',
        ]


class CategoriasForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields = [
            'nombre',
        ]

class MarcaForm(forms.ModelForm):
    class Meta:
        model=Marca
        fields = [
            'nombre',
        ]

class FormLogin(forms.Form):
    rut = forms.CharField(
        label="RUT",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 12345678-9',
            'required': 'true'
        })
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu contraseña',
            'required': 'true'
        })
    )

class FormRegistro(UserCreationForm):
    rut = forms.CharField(
        max_length=12,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 12345678-9',
            'oninput': 'formatRut(this)'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'rut', 'password1', 'password2']

    def init(self, args, **kwargs):
        super().init(args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user