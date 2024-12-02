from django import forms
from .models import Productos, Categoria
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductosForm(forms.ModelForm):
    class Meta:
        model=Productos
        fields = [
            'nombre',
            'categoria',
            'imagen',
            'detalle',
            'precio',
            'marca',
            'disponible',
            'stock',
        ]

class ProductosHabilitadosForm(forms.ModelForm):
    class Meta:
        model=Productos
        fields = [
            'habilitado',
        ]

class CategoriasForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields = [
            'nombre',
        ]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

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
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user