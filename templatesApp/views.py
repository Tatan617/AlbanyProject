from django.contrib import messages

from .models import *
from django.db.models import Q, Sum, F
from .carrito import Carrito
# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from templatesApp.models import *
from .forms import *

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



def Login(request):
    if request.method == "POST":
        form = FormLogin(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(perfil__rut=rut)
                if user.password == password:
                    login(request, user)
                    return redirect('../')
                else:
                    messages.error(request, "Contraseña incorrecta.")
            except User.DoesNotExist:
                messages.error(request, "RUT no encontrado.")
    else:
        form = FormLogin()
    return render(request, 'login.html', {'form': form})

def Registro(request):
    if request.method == "POST":
        form = FormRegistro(request.POST)
        if form.is_valid():
            rut_ingresado = form.cleaned_data.get('rut')
            if Perfil.objects.filter(rut=rut_ingresado).exists():
                messages.error(request, "El rut ya está ingresado. Use otro.")
            else: 
                user = form.save(commit=False)
                user.password = form.cleaned_data['password1']
                user.save()
                user.perfil.rut = form.cleaned_data.get('rut')
                user.perfil.save()
                messages.success(request, "Registro Exitoso. Puedes iniciar sesión ahora.")
                return redirect('../PortalLogin')
        else:
            messages.error(request, "Por favor, corrige los errores en el formulario.")
    else:
        form = FormRegistro()

    return render(request, 'register.html', {"form": form})


def Index(request):
    queryset = request.GET.get('buscar')
    productos  = Productos.objects.all()
    data={'productos':productos}
    if queryset:
        productos = Productos.objects.filter(
            Q(nombre__icontains = queryset)|
            Q(detalle__icontains = queryset)
            ).distinct()
        data={'productos':productos}
    return render(request,'index.html',data)

def Mostrar_Producto(request,id):
    productos=Productos.objects.get(id=id)
    form=MostrarProductosForm(instance=productos)
    if request.method=="POST":
        form=MostrarProductosForm(request.POST,request.FILES,instance=productos)
        if form.is_valid():
            form.save()
        return Index(request)
    data={'form':form,'titulo':'Actualizar Disponibilidad'}
    return render(request,'mostrar_producto.html',data)

def Carrito_de_Compras(request):
    productos = Productos.objects.all()
    data = {'productos': productos}
    return render(request, 'carritodecompras.html', data)

def agregar_al_carro(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.agregar(producto)
    return render(request, 'carritodecompras.html')

def eliminar_del_carro(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return render(request, 'carritodecompras.html')

def restar_del_carro(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.restar(producto)
    return render(request, 'carritodecompras.html')

def limpiar_carro(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'carritodecompras.html')

def Comprar(request):
    carrito = Carrito(request)
    if not carrito.carrito:
        messages.error(request, "El carrito está vacío. No puedes realizar una compra.")
        return redirect('buycar') 
    total = sum(item["acumulado"] for item in carrito.carrito.values())

    try:
        rut = request.user.perfil.rut
    except Perfil.DoesNotExist:
        messages.error(request, "No se encontró un RUT asociado al usuario.")
        return redirect('buycar')

    pedido = Pedido.objects.create(total=total)
    for item in carrito.carrito.values():
        producto = get_object_or_404(Productos, id=item["producto_id"])
        producto.stock -= item["cantidad"]
        producto.save()
        DetallePedido.objects.create(
            pedido=pedido,
            producto=producto,
            cantidad=item["cantidad"],
            subtotal=item["acumulado"],
            rut=rut
        )
    carrito.limpiar()
    messages.success(request, "Compra realizada con éxito. ¡Gracias por tu pedido!")
    return redirect('mostrar_pedido',pedido_id=pedido.id)

def mostrar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    detalles = DetallePedido.objects.filter(pedido=pedido)

    contexto = {
        'pedido': pedido,
        'detalles': detalles
    }

    return render(request, 'mostrar_pedido.html', contexto)

def registro_pedidos(request):
    queryset = request.GET.get('buscar')
    pedido = Pedido.objects.all()
    contexto = {'pedidos': pedido}
    if queryset:
         pedido = Pedido.objects.filter(
            Q(total__icontains = queryset)|
            Q(fecha__icontains = queryset)
            ).distinct()
         contexto = {'pedidos': pedido}
    return render(request,'registro_venta.html',contexto)


def Gestionar_Productos(request):
    queryset = request.GET.get('buscar')
    productos=Productos.objects.all()
    data={'productos':productos}
    if queryset:
        productos = Productos.objects.filter(
            Q(nombre__icontains = queryset)|
            Q(detalle__icontains = queryset)
            ).distinct()
        data={'productos':productos}
    return render(request,'productos_gestion.html',data)


def Agregar_Producto(request):
    if request.method == 'POST':
        form = ProductosForm(request.POST, request.FILES)  # Asegúrate de incluir request.FILES
        if form.is_valid():
            nombre_producto = form.cleaned_data['nombre']
            
            # Verificar duplicados por nombre
            if Productos.objects.filter(nombre=nombre_producto).exists():
                messages.error(request, f"El producto '{nombre_producto}' ya existe.")
            else:
                producto = form.save(commit=False)
                if 'imagen' in request.FILES:
                    producto.imagen = request.FILES['imagen']
                producto.save()
                messages.success(request, "Producto agregado con éxito.")
                return redirect('producto_gestion')  # Cambia a la vista correspondiente
        else:
            messages.error(request, "Error en el formulario. Por favor, corrige los errores.")
            print("Errores en el formulario:", form.errors)
    else:
        form = ProductosForm()

    data = {'form': form, 'titulo': 'Agregar Productos'}
    return render(request, 'productos_save.html', data)

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
    queryset = request.GET.get('buscar')
    categorias=Categoria.objects.all()
    data={'categorias':categorias}
    if queryset:
        categorias=Categoria.objects.filter(
            Q(nombre__icontains = queryset)
            )
        data={'categorias':categorias}
    return render(request, 'categoria_gestion.html',data)


def Agregar_Categoria(request):
    form=CategoriasForm()
    if request.method=='POST':
        form=CategoriasForm(request.POST)
        if form.is_valid():
            nombre_categoria = form.cleaned_data['nombre']
            if Categoria.objects.filter(nombre=nombre_categoria).exists():
                messages.error(request, "Ya existe una categoría con este nombre.")
            else:
                form.save()
                messages.success(request, "Categoría agregada con éxito.")
                return redirect('gestionar_categorias') 
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

def Gestionar_Marca(request):
    queryset = request.GET.get('buscar')
    marca=Marca.objects.all()
    data={'marca':marca}
    if queryset:
        marca=Marca.objects.filter(
            Q(nombre__icontains = queryset)
            )
        data={'marca':marca}
    return render(request, 'marca_gestion.html',data)


def Agregar_Marca(request):
    form=MarcaForm()
    if request.method=='POST':
        form=MarcaForm(request.POST)
        if form.is_valid():
            nombre_marca = form.cleaned_data['nombre']
            if Marca.objects.filter(nombre=nombre_marca).exists():
                messages.error(request, "Ya existe una marca con este nombre.")
            else:
                form.save()
                messages.success(request, "Marca agregada con éxito.")
                return redirect('gestionar_marca') 
    data={'form':form,'titulo':'Agregar Marca'}
    return render(request,'marca_save.html',data)


def Ver_Marca(request,id):
    marca=Marca.objects.get(id=id)
    data={"marca":marca}
    return render(request,'marca_ver.html',data)


def Actualizar_Marca(request,id):
    marca=Marca.objects.get(id=id)
    form=MarcaForm(instance=marca)
    if request.method=="POST":
        form=MarcaForm(request.POST,instance=marca)
        if form.is_valid():
            form.save()
        return Gestionar_Marca(request)
    data={'form':form,'titulo':'Actualizar Categoria'}
    return render(request,'marca_save.html',data)

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
    return render(request,'index.html',data)
