from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DishViewSet, OrderViewSet, UserViewSet


router = DefaultRouter()
router.register(r'dishes', DishViewSet)
router.register(r'users', UserViewSet)
router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('api/', include(router.urls)),
]

