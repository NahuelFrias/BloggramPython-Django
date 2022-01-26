from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static # para ver las imagenes en el admin
from django.conf import settings # para ver las imagenes en el admin


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(('posts.urls', 'posts'), namespace='posts')), # dentro de la tupla: url y aplicacion
    path('users/', include(('users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # para ver las imagenes en el admin
