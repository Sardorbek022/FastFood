from django.db import models
from django.utils import timezone
from .user import UserModel
from .dish import DishModel

class OrderModel(models.Model):
    STATUS_CHOICES = (
        ('new', 'Yangi'),
        ('accepted', 'Qabul qilingan'),
        ('sent', 'Yuborilgan'),
    )

    user = models.ForeignKey(
        UserModel, 
        on_delete=models.CASCADE, 
        related_name='orders',
        verbose_name="Buyurtmachi",
        help_text="Buyurtmani bergan foydalanuvchi"
    )
    dishes = models.ManyToManyField(
        DishModel,
        verbose_name="Taomlar",
        help_text="Buyurtmaga qo‘shilgan taomlar"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name="Holati",
        help_text="Buyurtma holatini belgilang"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_distance_km = models.FloatField(
        verbose_name="Yetkazish masofasi (km)",
        help_text="Buyurtmachi bilan restoran orasidagi masofa"
    )
    estimated_delivery_time = models.PositiveIntegerField(
        verbose_name="Taxminiy yetkazib berish vaqti (minut)",
        help_text="Buyurtmaning tayyorlanishi va yetkazilishi uchun taxminiy vaqt",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Buyurtma #{self.id} - {self.user.username}"

    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"
        ordering = ['-created_at']
