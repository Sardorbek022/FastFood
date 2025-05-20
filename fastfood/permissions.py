from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsWaiter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='waiter').exists()

class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and not request.user.is_staff and not request.user.groups.filter(name='waiter').exists()
