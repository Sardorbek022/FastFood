from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsWaiter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='waiter').exists()

class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and not request.user.is_staff and not request.user.groups.filter(name='waiter').exists()

class OrPermission(BasePermission):
    def __init__(self, *perms):
        self.perms = perms

    def has_permission(self, request, view):
        return any(perm().has_permission(request, view) for perm in self.perms)
