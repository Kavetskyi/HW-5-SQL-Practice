from django.shortcuts import render, redirect
from products.models import Product
from .models import MenuItem
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, SigninForm

# from django.db.models import Q
#
#     products = Product.objects.filter(Q(display_on_main_page=True) | Q(approved=True))


def home(request):
    products = Product.objects.filter(display_on_main_page=True, approved=True).order_by("title")
    return render(request, "main/index.html", {"products": products})

    # menu_items_list = MenuItem.objects.all()
    # products = Product.objects.filter(display_on_main_page=True, approved=True).order_by("title")
    # return render(request, "main/index.html", {"menu_items_list": menu_items_list, "products": products})


def signup(request):
    if request.method == 'POST':
        # user = User()
        # user.username = request.POST.get('username')
        # user.email = request.POST.get('email')
        # user.set_password(request.POST.get('password'))
        # user.first_name = request.POST.get('first_name')
        # user.last_name = request.POST.get('last_name')
        # user.is_superuser = False
        # user.is_staff = False
        # user.is_active = True
        # user.save()
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get("password"))
            user = form.save()
            login(request, user)
            return redirect("/")
        else:
            return render(request, "main/signup.html", {"form": form})
    else:
        form = SignupForm()
        return render(request, "main/signup.html", {"form": form})


def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get("username"),
                                password=form.cleaned_data.get("password"))
            if user:
                login(request, user)
            return redirect("/")
        else:
            return render(request, "main/signin.html", {"form": form})
    else:
        form = SigninForm()
        return render(request, "main/signin.html", {"form": form})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")
