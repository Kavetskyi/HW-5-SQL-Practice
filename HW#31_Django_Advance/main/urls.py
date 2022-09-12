from django.urls import path, include
from .views import home, signup, signin, logout_view, add_to_cart, cart, remove_from_cart

urlpatterns = [
    path('', home, name="home"),
    path('signup', signup, name="signup"),
    path('signin', signin, name="signin"),
    path('logout', logout_view, name="logout"),
    path('add-to-cart/<int:id>', add_to_cart, name="add_to_cart"),
    path('cart', cart, name="cart"),
    path('remove-from-cart/<int:id>', remove_from_cart, name="remove_from_cart")
]
