from django.contrib import messages
from django.shortcuts import render
from .models import Productos

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from templatesApp.models import Productos, Categoria
from .forms import ProductosForm, LoginForm, CategoriasForm, UserRegisterForm

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def User_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username = cd['username'],
                                password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Usuario Autenticado')
                else:
                    return HttpResponse('El usuario no está activo')
            else:
                return HttpResponse('La informacion no es correcta')
    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})
    
def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user':new_user})
    else:
        user_form = UserRegisterForm()
    return render(request, 
                      'account/register.html',
                      {'user_form': user_form})

@login_required
def Index(request):
    productos = Productos.objects.all()
    data = {'productos': productos}
    return render(request, 'index.html', data)


@login_required
def Carrito(request):
    return render(request, 'carritodecompras.html')

@login_required
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

@login_required
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


