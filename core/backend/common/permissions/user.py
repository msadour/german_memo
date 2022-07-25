from typing import Any

from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet


class BasicOnly(permissions.BasePermission):
    """Class BasicOnly."""

    def has_permission(self, request: Request, view: ModelViewSet) -> bool:
        """Check if the method is only GET or admin.

        Args:
            request:
            view:

        Returns:
            Is permitted or not.
        """
        if request.user.is_authenticated:
            if request.user.is_staff:
                return True
        return request.method == "GET"

    def has_object_permission(
        self, request: Request, view: ModelViewSet, obj: Any
    ) -> bool:
        """Check if the method is only GET/POST or admin for an object.

        Args:
            request:
            view:
            obj:

        Returns:
            Is permitted or not.
        """
        if request.user.is_authenticated:
            if request.user.is_staff:
                return True
        return request.method == "GET"


class SubmitRequestChange(permissions.BasePermission):
    """Class ReadOnly."""

    def has_permission(self, request: Request, view: ModelViewSet) -> bool:
        """Check if admin or patch method.

        Args:
            request:
            view:

        Returns:
            Is permitted or not.
        """
        if request.user.is_authenticated:
            if request.user.is_staff:
                return True
            return request.method == "PATCH"
        return False

    def has_object_permission(
        self, request: Request, view: ModelViewSet, obj: Any
    ) -> bool:
        """Check if admin or patch method.

        Args:
            request:
            view:
            obj:

        Returns:
            Is permitted or not.
        """
        if request.user.is_authenticated:
            if request.user.is_staff:
                return True
            return request.method == "PATCH"
        return False
