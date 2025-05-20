from rest_framework import viewsets, permissions
from ..models.dish import DishModel
from ..serializers import DishSerializer
from fastfood.permissions import IsAdmin, IsWaiter  # permissions.py dagi klasslar

class DishViewSet(viewsets.ModelViewSet):
    queryset = DishModel.objects.all()
    serializer_class = DishSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsAdmin() | IsWaiter()]
        else:
            return [permissions.AllowAny()]
