from django.urls import path
from .views import *

urlpatterns = [
    path('',Home,name="Home"),
    path('contacts/', contacts, name="contacts"),
    path('about/',about,name="about"),
    path('contacts/details/<int:id>', details, name="details"),

]