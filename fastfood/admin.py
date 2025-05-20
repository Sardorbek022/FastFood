from django.contrib import admin
from .models import UserModel, DishModel, OrderModel


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role', 'created_at')
    list_filter = ('role', 'is_active', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('-created_at',)


@admin.register(DishModel)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'created_at')
    search_fields = ('name',)
    ordering = ('-created_at',)


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'status', 'created_at', 'delivery_distance_km', 'estimated_delivery_time'
    )
    list_filter = ('status',)
    search_fields = ('user__username',)
    ordering = ('-created_at',)
