from django.contrib import messages
from django.shortcuts import render
from .models import Productos

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from templatesApp.models import Productos, Categoria, Usuario
from .forms import ProductosForm, UsuarioForm, CategoriasForm


def Index(request):
    productos = Productos.objects.all()
    data = {'productos': productos}
    return render(request, 'index.html', data)

def Index2(request):
    return render(request,"index2.html")

def Login(request):
    return render(request, 'login.html')

def Register(request, rut):
    form=UsuarioForm()
    usuarios=Usuario.objects.get(rut=rut)
    data={'usuarios':usuarios}
    if request.method=='POST':
        form=UsuarioForm(request.POST)
        #if form.is_valid():
            #if usuarios.rut:
                #messages.error(request, "Este RUT ya está registrado")
                #return Login(request)
            #else:
        form.save()
        return Login(request)
    data={'form':form,'titulo':'Registrarse'}
    return render(request, 'register.html', data)

def Carrito(request):
    return render(request, 'carritodecompras.html')

def Gestionar_Productos(request):
    productos=Productos.objects.all()
    data={'productos':productos}
    return render(request, 'productos_gestion.html',data)

def Agregar_Producto(request):
    form=ProductosForm()
    if request.method=='POST':
        form=ProductosForm(request.POST)
        if form.is_valid():
            form.save()
        return Gestionar_Productos(request)
    data={'form':form,'titulo':'Agregar Productos'}
    return render(request,'productos_save.html',data)

def Ver_Producto(request,id):
    productos=Productos.objects.get(id=id)
    data={"productos":productos}
    return render(request,'productos_ver.html',data)

def Actualizar_Producto(request,id):
    productos=Productos.objects.get(id=id)
    form=ProductosForm(instance=productos)
    if request.method=="POST":
        form=ProductosForm(request.POST,instance=productos)
        if form.is_valid():
            form.save()
        return Gestionar_Productos(request)
    data={'form':form,'titulo':'Actualizar Producto'}
    return render(request,'productos_save.html',data)


def Deshabilitar_Producto(request,id):
    try:
        productos = Productos.objects.get(id=id)
    except Productos.DoesNotExist:
        return redirect('../productos_gestion/')

    if request.method == 'POST':
        productos.delete()
        return redirect('../productos_gestion/')
    
    return render(request, 'productos_deshabilitar.html', {'productos': productos})

def Gestionar_Categorias(request):
    categorias=Categoria.objects.all()
    data={'categorias':categorias}
    return render(request, 'categoria_gestion.html',data)

def Agregar_Categoria(request):
    form=CategoriasForm()
    if request.method=='POST':
        form=CategoriasForm(request.POST)
        if form.is_valid():
            form.save()
        return Gestionar_Categorias(request)
    data={'form':form,'titulo':'Agregar Categorias'}
    return render(request,'categorias_save.html',data)

def Ver_Categoria(request,id):
    categorias=Categoria.objects.get(id=id)
    data={"categorias":categorias}
    return render(request,'categorias_ver.html',data)

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


