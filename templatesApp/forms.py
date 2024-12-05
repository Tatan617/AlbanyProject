from django import forms
from .models import Productos, Categoria, Usuario
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

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'contraseña']