from django import forms
from .models import Productos, Categoria
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

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password',
                               widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','first_name','email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            return forms.ValidationError('Las contraseñas no coinciden')
        return cd['password2']