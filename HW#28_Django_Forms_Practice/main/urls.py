from django.urls import path, include
from .views import home, signup, signin, logout_view

urlpatterns = [
    path('', home, name="home"),
    path('signup', signup, name="signup"),
    path('signin', signin, name="signin"),
    path('logout', logout_view, name="logout")
]
