from django.urls import path
from templatesApp import views

urlpatterns = [
    path('', views.Index),
    path('indexadmin/', views.Index2),
    path('login/', views.Login),
    path('register/', views.Register),
    path('buycar/', views.Carrito),
    path('productos_gestion/', views.Gestionar_Productos),
    path('agregar_producto/', views.Agregar_Producto),
    path('ver_producto/<int:id>', views.Ver_Producto),
    path('actualizar_producto/<int:id>', views.Actualizar_Producto),
    path('deshabilitar_producto/<int:id>', views.Deshabilitar_Producto),
    path('categorias_gestion/', views.Gestionar_Categorias),
    path('agregar_categoria/', views.Agregar_Categoria),
    path('ver_categoria/<int:id>', views.Ver_Categoria),
    path('actualizar_categoria/<int:id>', views.Actualizar_Categoria),
]
