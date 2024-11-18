from rest_framework import permissions


class VisitAccessPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.has_perm('visit.view_visit') or request.user.is_staff

        if request.user.is_superuser:
            return True

        if request.user.is_staff and request.method == 'POST':
            return request.user.has_perm('visit.add_visit')

        return False
    

    