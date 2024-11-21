from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.Index, name='index'),
    path('indexadmin/', views.Index2),
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