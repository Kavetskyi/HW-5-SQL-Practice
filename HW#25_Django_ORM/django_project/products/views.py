from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category


def add_product(request):
    if request.user.is_authenticated:
        categories = Category.objects.all()
        if request.method == 'GET':
            return render(request, "products/add.html", {"categories": categories})
        else:
            product = Product()
            product.title = request.POST.get('title')
            product.description = request.POST.get('description')
            product.user = request.user
            product.save()
            for category in request.POST.getlist('categories[]'):
                product.categories.add(int(category))
            return redirect("/")
    else:
        return redirect("/")


def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "products/details.html", {"product": product})


def product_by_category(request):
    categories = Category.objects.all()
    if request.method == 'GET':
        selected_category = "All"
        products = Product.objects.filter(display_on_main_page=True, approved=True).order_by("title")
        return render(request, "products/category.html",
                      {"categories": categories, "products": products, "selected_category": selected_category})
    else:
        selected_category = int(request.POST.get('categories'))
        products = Product.objects.filter(categories=selected_category, display_on_main_page=True, approved=True)\
            .order_by("title")
    return render(request, "products/category.html",
                  {"categories": categories, "products": products, "selected_category": selected_category})
