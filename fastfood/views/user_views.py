from rest_framework import viewsets, permissions
from ..models.user import UserModel
from ..serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
