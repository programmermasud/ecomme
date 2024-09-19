
from django.contrib import admin
from django.urls import path,include
<<<<<<< HEAD

from django.conf import settings
from django.conf.urls.static import static

=======
from management.views import *
>>>>>>> 89e6b39bc8b533e9968f609499c68fb3e1d5020d

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('management.urls')),
    path('product/',include('product.urls'))

]
<<<<<<< HEAD

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
=======
>>>>>>> 89e6b39bc8b533e9968f609499c68fb3e1d5020d
