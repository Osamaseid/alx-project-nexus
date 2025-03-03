from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    """Allow only Admins to manage job postings."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class IsJobApplicant(BasePermission):
    """Allow only registered users to apply for jobs."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'user'
