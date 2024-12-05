from django.contrib import messages
from django.shortcuts import render
from .models import Productos
from django.db.models import Q, Sum, F
# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from templatesApp.models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def portal_login(request):
    if request.method == 'GET':
        return render(request, 'login.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], 
                                     password=request.POST['password1'])
            user.save()
    return HttpResponse('No coinciden')




def Index(request):
    productos = Productos.objects.all()
    data = {'productos': productos}
    return render(request, 'index.html', data)


@login_required
def Carrito(request):
    return render(request, 'carritodecompras.html')


def Gestionar_Productos(request):
    productos=Productos.objects.all()
    data={'productos':productos}
    return render(request, 'productos_gestion.html',data)

@login_required
def Agregar_Producto(request):    
    if request.method=='POST':
        form=ProductosForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            if 'imagen' in request.FILES:
                print("Archivo de imagen recibido:", request.FILES['imagen'])
                producto.imagen = request.FILES['imagen']
            producto.save()            
            return Gestionar_Productos(request)
        else:
            print("error", form.errors)
    else:
        form = ProductosForm()
    data={'form':form,'titulo':'Agregar Productos'}
    return render(request,'productos_save.html',data)

@login_required
def Ver_Producto(request,id):
    productos=Productos.objects.get(id=id)
    data={"productos":productos}
    return render(request,'productos_ver.html',data)


def Actualizar_Producto(request,id):
    productos=Productos.objects.get(id=id)
    form=ProductosForm(instance=productos)
    if request.method=="POST":
        form=ProductosForm(request.POST,request.FILES,instance=productos)
        if form.is_valid():
            form.save()
        return Gestionar_Productos(request)
    data={'form':form,'titulo':'Actualizar Producto'}
    return render(request,'productos_save.html',data)

@login_required
def Deshabilitar_Producto(request,id):
    try:
        productos = Productos.objects.get(id=id)
    except Productos.DoesNotExist:
        return redirect('../productos_gestion/')

    if request.method == 'POST':
        productos.delete()
        return redirect('../productos_gestion/')
    
    return render(request, 'productos_deshabilitar.html', {'productos': productos})

@login_required
def Gestionar_Categorias(request):
    categorias=Categoria.objects.all()
    data={'categorias':categorias}
    return render(request, 'categoria_gestion.html',data)

@login_required
def Agregar_Categoria(request):
    form=CategoriasForm()
    if request.method=='POST':
        form=CategoriasForm(request.POST)
        if form.is_valid():
            form.save()
        return Gestionar_Categorias(request)
    data={'form':form,'titulo':'Agregar Categorias'}
    return render(request,'categorias_save.html',data)

@login_required
def Ver_Categoria(request,id):
    categorias=Categoria.objects.get(id=id)
    data={"categorias":categorias}
    return render(request,'categorias_ver.html',data)

@login_required
def Actualizar_Categoria(request,id):
    categorias=Categoria.objects.get(id=id)
    form=CategoriasForm(instance=categorias)
    if request.method=="POST":
        form=CategoriasForm(request.POST,instance=categorias)
        if form.is_valid():
            form.save()
        return Gestionar_Categorias(request)
    data={'form':form,'titulo':'Actualizar Categoria'}
    return render(request,'categorias_save.html',data)

@login_required
def Buscar_producto(request):
    queryset = request.GET.get('buscar')
    productos  = Productos.objects.all()
    data={'productos':productos}
    if queryset:
        productos = Productos.objects.filter(
            Q(nombre = queryset)|
            Q(marca = queryset)
            ).distinct()
        data={'productos':productos}
    return render(request,'buscar.html',data)



