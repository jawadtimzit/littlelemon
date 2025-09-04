from django.urls import path
from . import views

urlpatterns = [

    path('ping/', views.ping, name='restaurant-ping'),
    path('menu/', views.menu, name='restaurant-menu'),
    path('index/', views.index, name='index'),
]
