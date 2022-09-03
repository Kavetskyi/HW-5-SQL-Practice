from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from products.models import Product
from .models import MenuItem
from django.contrib.auth import authenticate, login, logout

# from django.db.models import Q
#
#     products = Product.objects.filter(Q(display_on_main_page=True) | Q(approved=True))


def home(request):
    menu_items = MenuItem.objects.all()
    products = Product.objects.filter(display_on_main_page=True, approved=True).order_by("title")
    return render(request, "main/index.html", {"menu_items": menu_items, "products": products})


def signup(request):
    if request.method == 'POST':
        user = User()
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.set_password(request.POST.get('password'))
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.is_superuser = False
        user.is_staff = False
        user.is_active = True
        user.save()
        if user:
            login(request, user)
        return redirect("/")
    else:
        return render(request, "main/signup.html", {})


def signin(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
        return redirect("/")
    else:
        return render(request, "main/signin.html", {})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")
