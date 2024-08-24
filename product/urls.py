from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='product-home'),
    path('contact/',contact,name='contact')
]


