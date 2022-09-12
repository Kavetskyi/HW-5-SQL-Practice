from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Product, Category
from .forms import ProductForm


def add_product(request):
    if request.user.is_authenticated:
        categories = Category.objects.all()
        if request.method == 'GET':
            form = ProductForm(initial={"user": request.user})
            return render(request, "products/add.html", {"categories": categories, "form": form})
        else:
            form = ProductForm(request.POST)
            if form.is_valid():
                product = form.save(user=request.user, commit=True)
                for category in request.POST.getlist('categories[]'):
                    product.categories.add(int(category))
                form.save(user=request.user, commit=True)
                return redirect("/")
            else:
                return render(request, "products/add.html", {"categories": categories, "form": form})
    else:
        return redirect("/")


def product_details(request, id):
    product_in_cart = False
    product = get_object_or_404(Product, id=id)
    if id in request.session.get("products", []):
        product_in_cart = True
    return render(request, "products/details.html", {"product": product, "product_in_cart": product_in_cart})


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


def add_category(request):
    if request.user.is_authenticated:
        categories = Category.objects.order_by("name")
        if request.method == 'POST':
            if request.POST.get("name"):
                category = Category()
                category.user = request.user
                category.name = request.POST.get("name")
                category.parent_id = request.POST.get("parent_category")
                category.save()
            return redirect("/")
        else:
            return render(request, "products/category/add.html", {"categories": categories})
    else:
        return redirect("/")


def category_page(request, slug):
    try:
        category = Category.objects.get(slug=slug)
        products = Product.objects.filter(categories=category.id, display_on_main_page=True, approved=True)\
            .order_by("title")
    except Category.DoesNotExist:
        raise Http404()
    return render(request, "products/category/category_page.html", {"category": category.name, "products": products})
