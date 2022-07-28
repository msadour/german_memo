from typing import Any

from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet


class IsAdminApprove(permissions.BasePermission):
    """Class BasicOnly."""

    def has_permission(self, request: Request, view: ModelViewSet) -> bool:
        """Check if user is admin or method is post.

        Args:
            request:
            view:

        Returns:
            Is permitted or not.
        """
        if request.user.is_authenticated:
            return request.method == "POST"
        return request.user.is_staff

    def has_object_permission(
            self, request: Request, view: ModelViewSet, obj: Any
    ) -> bool:
        """Check if user is admin or method is post.

        Args:
            request:
            view:
            obj:

        Returns:
            Is permitted or not.
        """
        return request.user.is_authenticated and request.user.is_staff


class IsAdmin(permissions.BasePermission):
    """Class BasicOnly."""

    def has_permission(self, request: Request, view: ModelViewSet) -> bool:
        """Check if user is admin.

        Args:
            request:
            view:

        Returns:
            Is permitted or not.
        """
        return request.user.is_authenticated and request.user.is_staff

    def has_object_permission(
            self, request: Request, view: ModelViewSet, obj: Any
    ) -> bool:
        """Check if user is admin.

        Args:
            request:
            view:
            obj:

        Returns:
            Is permitted or not.
        """
        return request.user.is_authenticated and request.user.is_staff
