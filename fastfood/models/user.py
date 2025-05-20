from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('waiter', 'Ofitsiant'),
        ('customer', 'User'),
    )
    role = models.CharField(
        max_length=20, 
        choices=ROLE_CHOICES, 
        default='customer',
        verbose_name="Foydalanuvchi roli",
        help_text="Foydalanuvchi tizimdagi rolini tanlang"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.username} ({self.role})"

