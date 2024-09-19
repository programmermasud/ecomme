<<<<<<< HEAD
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.http import Http404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required(login_url='sign-in')
def Home(request):


    return render(request, 'management/home.html')

@login_required(login_url='sign-in')
def contacts(request):
    contacts = Contact.objects.all().order_by('-id')

    search = request.GET.get('search')
    if search:
        contacts = Contact.objects.filter( Q(name__icontains = search) | Q(phone = search))
=======
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

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
>>>>>>> 89e6b39bc8b533e9968f609499c68fb3e1d5020d

    context = {
        'contacts': contacts
    }

    return render(request, 'management/contacts.html',context)

<<<<<<< HEAD
@login_required(login_url='sign-in')

def details(request, slug):

    contact = Contact.objects.filter(slug=slug).first()
    family = FamilyMember.objects.filter(contact=contact)

    print(family)
    context = {
        'contact': contact,
        'family': family
=======
def details(request, id):

    detail = Contact.objects.get(id=id)

    context = {
        'detail': detail
>>>>>>> 89e6b39bc8b533e9968f609499c68fb3e1d5020d
    }

    return render(request,'management/details.html',context)

<<<<<<< HEAD
@login_required(login_url='sign-in')
=======

>>>>>>> 89e6b39bc8b533e9968f609499c68fb3e1d5020d
def about(request):

    return render(request, 'management/about.html')


<<<<<<< HEAD
@login_required(login_url='sign-in')
def add_contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        age  = request.POST.get('age')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        if name and age and phone and address:
            Contact.objects.create(
                name = name,
                age = age,
                phone = phone,
                address = address
            )
            messages.success(request, f"contact { name } added successfull")
            return redirect('contacts')
        else:
            messages.error(request, f"contact { name } not added")


    return render(request,'management/add_contact.html')

@login_required(login_url='sign-in')
def delete(request,id):

    contacts = Contact.objects.get(id=id)
    contacts.delete()
    messages.success(request, f"contact delete successfull")
    return redirect('contacts')

@login_required(login_url='sign-in')
def edit_contact(request, id):

    contact = Contact.objects.get(id=id)

    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        contact.name = name
        contact.age = age
        contact.phone = phone
        contact.address = address
        contact.save()
        messages.success(request, f"contact { name } update successfull")

        return redirect('contacts')

    context = {
        'contact': contact
    }

    return render(request, 'management/edit.html',context)

@login_required(login_url='sign-in')
def products(request):

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'management/products.html',context)

@login_required(login_url='sign-in')
def add_products(request):
    catagory = Catagory.objects.all()

    if request.method == 'POST':
        catagory_id = request.POST.get('catagory_id')
        name = request.POST.get('name')
        price = request.POST.get('price')
        decription = request.POST.get('decription')

        Product.objects.create(
            catagory_id = catagory_id,
            name = name,
            price = price,
            decription = decription
        )
        messages.success(request, f"product added successfull")
        return redirect('products')

    context = {
        'catagory': catagory
    }

    return render(request, 'management/add_products.html', context)

@login_required(login_url='sign-in')
def profile(request):

    return render(request, 'management/profile.html')

def edit_profile(request,id):

    profile = Profile.objects.get(id=id)
    user = User.objects.filter(profile=profile)

    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        image = request.POST.get('profile_image')

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        profile.address = address
        profile.phone = phone
        profile.image = image
        profile.save()
        messages.success(request, f"profile update successfull")
        return redirect('profile')

    context = {
        'profile': profile
    }

    return render(request, 'management/edit_profile.html', context)




def sign_in(request):

    if request.user.is_authenticated:
        return redirect('Home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username , password = password)

        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, f"Invaild username and password")


    return render(request, 'management/sign_in.html')

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('Home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confrom_password = request.POST.get('confrom_password')

        if username and email and password and confrom_password:
            if password != confrom_password:
                messages.error(request, f"password don not match!")

            elif User.objects.filter(email = email).exists():
                messages.error(request, f"email already exists")

            else:
                user = User.objects.create_user(
                        username = username,
                        email = email,
                        password = password
                    )
                messages.success(request, f"Account create successfully")
                return redirect('sign-in')
        else:
            return redirect('sign-up')


    return render(request, 'management/sign_up.html')




def logout_view(request):
    logout(request)
    return redirect('sign-in')


=======
def test(request):
    HttpResponse("test")
>>>>>>> 89e6b39bc8b533e9968f609499c68fb3e1d5020d
