from django.shortcuts import render
from .models import Productos

# Create your views here.

def Index(request):
    return render(request,"index.html")

def Login(request):
    return render(request, 'login.html')

def Register(request):
    return render(request, 'register.html')

def Carrito(request):
    return render(request, 'carritodecompras.html')

def lista_productos(request):
    productos = Productos.objects.all()
    data = {'productos': productos}
    return render(request, "index.html", data)