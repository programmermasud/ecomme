from django.urls import path
from .views import *

urlpatterns = [
<<<<<<< HEAD
    path('',Home,name="Home"),
    path('contacts/', contacts, name="contacts"),
    path('about/',about,name="about"),
    path('contacts/details/<slug:slug>', details, name="details"),
    path('add_contact/', add_contact, name="add_contact"),
    path('delete-contact/<int:id>/', delete, name="delete-contact"),
    path('edit-contact/<int:id>/', edit_contact, name="edit-contact"),
    path('products/', products, name="products"),
    path('add-products/', add_products, name="add-products"),
    path('profile/', profile, name="profile"),
    path('sign-in/', sign_in, name="sign-in"),
    path('sign-up/', sign_up, name="sign-up"),
    path('logout/', logout_view, name="logout"),
    path('edit-profile/<int:id>/', edit_profile, name="edit-profile"),
=======
    path('',Home,name='Home'),
    path('contacts/', contacts, name='contacts'),
    path('about/',about,name='about'),
    path('contacts/details/<int:id>', details, name='details'),
>>>>>>> 89e6b39bc8b533e9968f609499c68fb3e1d5020d

]