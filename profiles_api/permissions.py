from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        # Safe methods are HTTP methods that do not modify the database
        # (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # If the user is trying to edit their own profile, allow it
        return obj.id == request.user.id
