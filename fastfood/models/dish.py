from django.db import models


class DishModel(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Taom nomi",
        help_text="Taomning aniq va qisqa nomi"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Taom tavsifi",
        help_text="Taom haqida qo‘shimcha ma’lumot (ixtiyoriy)"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Narxi",
        help_text="Taomning narxi (so‘mda)"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Taom"
        verbose_name_plural = "Taomlar"
        ordering = ['-created_at'] 

    def __str__(self):
            return self.name