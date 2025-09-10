from django.urls import path, include
# from django.contrib import admin
from rest_framework import routers
# from restaurant.views import BookingViewSet, MenuViewSet, UserViewSet
from . import views

# router = routers.DefaultRouter()
# router.register(r'bookings', BookingViewSet)
# router.register(r'menus', MenuViewSet)
# router.register(r'users', UserViewSet)

router = routers.DefaultRouter()
router.register(r"tables", views.BookingViewSet, basename="booking")

urlpatterns = [

    path('ping/', views.ping, name='restaurant-ping'),
    path('restomenu/', views.menu, name='restaurant-menu'),
    path('index/', views.index, name='index'),
    # path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls')),

    path('menu/', views.MenuItemsView.as_view(), name='menu-list-create'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('booking/', include(router.urls)),

]
