from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.Index, name='index'),
    path('mostrar_producto/<int:id>', views.Mostrar_Producto, name='mostrar'),
    path('PortalLogin/', views.Login),
    path('PortalRegister/', views.Registro, name='register'),
    path('buycar/', views.Carrito_de_Compras, name="buycar"),
    path('agregar/<int:producto_id>', views.agregar_al_carro, name="add"),
    path('eliminar/<int:producto_id>', views.eliminar_del_carro, name="del"),
    path('restar/<int:producto_id>', views.restar_del_carro, name="res"),
    path('limpiar/', views.limpiar_carro, name="clean"),
    path('productos_gestion/', views.Gestionar_Productos, name='producto_gestion'),
    path('agregar_producto/', views.Agregar_Producto),
    path('ver_producto/<int:id>', views.Ver_Producto),
    path('actualizar_producto/<int:id>', views.Actualizar_Producto),
    path('deshabilitar_producto/<int:id>', views.Deshabilitar_Producto),
    path('categorias_gestion/', views.Gestionar_Categorias),
    path('agregar_categoria/', views.Agregar_Categoria),
    path('ver_categoria/<int:id>', views.Ver_Categoria),
    path('actualizar_categoria/<int:id>', views.Actualizar_Categoria),
    path('marca_gestion/', views.Gestionar_Marca),
    path('agregar_marca/', views.Agregar_Marca),
    path('ver_marca/<int:id>', views.Ver_Marca),
    path('actualizar_marca/<int:id>', views.Actualizar_Marca),
    path('buscar_producto/',views.Buscar_producto),
    

]