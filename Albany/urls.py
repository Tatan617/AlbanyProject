from django.contrib import admin


from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from django.urls import path, include

from templatesApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('templatesApp.urls')),
    
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    


