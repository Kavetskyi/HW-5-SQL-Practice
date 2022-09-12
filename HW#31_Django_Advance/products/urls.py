from django.urls import path, include
from .views import add_product, product_details, product_by_category, \
    edit_product, delete_product, add_category, category_page

urlpatterns = [
    path('/add', add_product, name="add_product"),
    path('/<int:id>', product_details, name="product_details"),
    path('/category', product_by_category, name="product_by_category"),
    path('/edit/<int:id>', edit_product, name="edit_product"),
    path('/delete/<int:id>', delete_product, name="delete_product"),
    path('/category/add', add_category, name="add_category"),
    path('/category/<str:slug>', category_page, name="category_page")
]
