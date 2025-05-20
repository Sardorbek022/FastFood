from rest_framework import viewsets, permissions
from ..models.order import OrderModel
from ..serializers import OrderSerializer
from fastfood.permissions import IsAdmin, IsWaiter, IsUser

class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated(), IsUser()]
        elif self.action in ['list', 'retrieve', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsAdmin() | IsWaiter()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
