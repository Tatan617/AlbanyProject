from django.contrib import admin
<<<<<<< Updated upstream

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
=======
from django.urls import path, include
>>>>>>> Stashed changes
from templatesApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< Updated upstream
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

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('account/', include('templatesApp.urls')),
]
>>>>>>> Stashed changes
