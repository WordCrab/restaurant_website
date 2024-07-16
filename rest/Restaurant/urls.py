from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name = "home"),
    path('menu/', views.menu, name = "menu"),
    path('login/', views.login, name = "login")
]