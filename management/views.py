from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import Http404

# Create your views here.


def Home(request):

    # List of dictionaries containing information about people
    people = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"},
        {"name": "Charlie", "age": 35, "city": "Chicago"}
    ]

    context = {
        
        'people': people

    }


    return render(request, 'management/home.html',context)

def contacts(request):
    contacts = Contact.objects.all()

    context = {
        'contacts': contacts
    }

    return render(request, 'management/contacts.html',context)

def details(request, id):
    detail= None

    try:
        detail = Contact.objects.get(id=id)
    except Contact.DoesNotExist:
        pass

    context = {
        'detail': detail
    }

    return render(request,'management/details.html',context)


def about(request):

    return render(request, 'management/about.html')


def test(request):
    HttpResponse("test")