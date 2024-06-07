from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):

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

def about(request):

    return render(request, 'management/about.html')
