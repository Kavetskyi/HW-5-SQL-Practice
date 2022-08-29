from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
from .models import MenuItem

# from django.db.models import Q
#
#     products = Product.objects.filter(Q(display_on_main_page=True) | Q(approved=True))


def home(request):
    menu_items = MenuItem.objects.all()
    products = Product.objects.filter(display_on_main_page=True, approved=True).order_by("title")
    return render(request, "main/index.html", {"menu_items": menu_items, "products": products})

