from rest_framework import viewsets, permissions
from ..models.dish import DishModel
from ..serializers import DishSerializer
from fastfood.permissions import IsAdmin, IsWaiter, IsUser, OrPermission  


class DishViewSet(viewsets.ModelViewSet):
    queryset = DishModel.objects.all()
    serializer_class = DishSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated(), IsUser()]
        elif self.action in ['list', 'retrieve', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), OrPermission(IsAdmin, IsWaiter)]
        return [permissions.IsAuthenticated()]
