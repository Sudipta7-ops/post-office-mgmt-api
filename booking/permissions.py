from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class IsBPM(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['bpm', 'admin']

class IsABPM(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['abpm', 'bpm', 'admin']