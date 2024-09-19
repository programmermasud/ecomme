from django.urls import path
from .views import *

urlpatterns = [
<<<<<<< HEAD
    path('',home,name='product-home'),
=======
    path('',home,name='home'),
>>>>>>> 89e6b39bc8b533e9968f609499c68fb3e1d5020d
    path('contact/',contact,name='contact')
]


