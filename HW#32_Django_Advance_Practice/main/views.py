from django.shortcuts import render, redirect
from django.http import Http404
from products.models import Product, Order, OrderItem
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


def add_to_cart(request, id):
    if Product.objects.get(id=id):
        if id in request.session.get("products", []):
            return redirect("/")
        if request.session.get("products", False):
            request.session["products"].append(id)
            request.session.modified = True
        else:
            request.session["products"] = []
            request.session["products"].append(id)
        total_price = 0
        for id in request.session.get("products", []):
            total_price += Product.objects.get(id=id).price
        request.session["cart_total_price"] = total_price
    else:
        raise Http404()
    return redirect("/")


def cart(request):
    if request.session.get("products", False):
        products = Product.objects.filter(id__in=request.session.get("products"))
        return render(request, "main/cart.html",
                      {"products": products, "total_price": request.session.get("cart_total_price", 0)})
    else:
        return render(request, "main/cart.html", {})


def remove_from_cart(request, id):
    if request.session.get("products", False):
        for i in range(len(request.session.get("products"))):
            if request.session.get("products")[i] == id:
                del request.session.get("products")[i]
                request.session.modified = True
                product = Product.objects.get(id=id)
                request.session["cart_total_price"] -= product.price
                break
    return redirect("/cart")


def order(request):
    if request.session.get("products", False):
        if request.method == "GET":
            total_price = request.session.get("cart_total_price", 0)
            return render(request, "main/order.html", {"total_price": total_price})
        else:
            order = Order()
            order.user = request.user
            order.name = request.POST.get("name")
            order.email = request.POST.get("email")
            order.address = request.POST.get("address")
            order.message = request.POST.get("message")
            order.total_price = request.session.get("cart_total_price")
            order.save()
            for product_id in request.session.get("products", []):
                order_item = OrderItem()
                order_item.order = order
                order_item.product_id = product_id
                order_item.save()
            request.session["products"] = []
            request.session["cart_total_price"] = 0
            return redirect("/")
