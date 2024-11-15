from django import forms
from .models import Productos, Categoria, Usuario

class ProductosForm(forms.ModelForm):
    class Meta:
        model=Productos
        fields = [
            'nombre',
            'categoria',
            'imagen',
            'detalle',
            'precio',
            'disponible',
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
        model=Usuario
        fields = [
            'rut',
            'nombre',
            'apellido',
            'correo',
            'contraseña'
        ]