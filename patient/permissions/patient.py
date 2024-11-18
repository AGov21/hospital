from rest_framework import permissions


class PatientAccessPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.has_perm('patient.view_patient') or request.user.is_staff

        if request.user.is_superuser:
            return True

        if request.user.is_staff and request.method == 'POST':
            return request.user.has_perm('patient.add_patient')

        return False
