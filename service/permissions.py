from rest_framework import permissions


class ServiceAccessPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.has_perm('service.view_service') or request.user.is_staff

        if request.user.is_superuser:
            return True

        if request.user.is_staff and request.method == 'POST':
            return request.user.has_perm('service.add_service')

        return False