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


def edit_product(request, id):
    if request.user.is_authenticated:
        all_categories = Category.objects.all()
        if request.method == 'GET':
            product = get_object_or_404(Product, id=id)
            list_categories = product.categories.filter()
            context = {"product": product, "all_categories": all_categories, "list_categories": list_categories}
            return render(request, "products/edit.html", context)
        else:
            product = get_object_or_404(Product, id=id)
            product.title = request.POST.get('title')
            product.description = request.POST.get('description')
            product.user = request.user
            product.save()
            for category in all_categories:
                if (str(category.id) in request.POST.getlist('categories[]')) \
                        and (category not in product.categories.all()):
                    product.categories.add(category)
                elif (str(category.id) not in request.POST.getlist('categories[]')) \
                        and (category in product.categories.all()):
                    product.categories.remove(category)
                else:
                    pass
            return redirect("/")
    else:
        return redirect("/")


def delete_product(request, id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=id)
        product.delete()
    return redirect("/")
