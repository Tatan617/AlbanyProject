
"""
URL configuration for Albany project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin


from django.urls import path
from templatesApp import views

urlpatterns = [

    path('admin/', admin.site.urls),
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
