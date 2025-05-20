from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models.order import OrderModel


@receiver(m2m_changed, sender=OrderModel.dishes.through)
def update_estimated_delivery_time(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        dish_count = instance.dishes.count()
        preparation_time = (dish_count / 4) * 5 
        delivery_time = instance.delivery_distance_km * 3
        instance.estimated_delivery_time = round(preparation_time + delivery_time)
        instance.save(update_fields=['estimated_delivery_time'])
