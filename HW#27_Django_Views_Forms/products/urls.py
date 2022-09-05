from django.urls import path, include
from .views import add_product, product_details, product_by_category, edit_product, delete_product

urlpatterns = [
    path('/add', add_product, name="add_product"),
    path('/<int:id>', product_details, name="product_details"),
    path('/category', product_by_category, name="product_by_category"),
    path('/edit/<int:id>', edit_product, name="edit_product"),
    path('/delete/<int:id>', delete_product, name="delete_product")
]
