from rest_framework import serializers
from .models.user import UserModel
from .models.dish import DishModel
from .models.order import OrderModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email']


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishModel
        fields = ['id', 'name', 'description', 'price', 'created_at']


from rest_framework import serializers
from .models.order import OrderModel
from .models.dish import DishModel
from .serializers import UserSerializer 

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    dishes = serializers.PrimaryKeyRelatedField(queryset=DishModel.objects.all(), many=True)
    estimated_delivery_time = serializers.IntegerField(read_only=True)

    class Meta:
        model = OrderModel
        fields = [
            'id', 'user', 'dishes', 'status',
            'created_at', 'delivery_distance_km',
            'estimated_delivery_time',
        ]

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None

        dishes = validated_data.pop('dishes')
        order = OrderModel.objects.create(user=user, **validated_data)
        order.dishes.set(dishes)
        return order

    def update(self, instance, validated_data):
        dishes = validated_data.pop('dishes', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if dishes is not None:
            instance.dishes.set(dishes)
        instance.save()
        return instance

