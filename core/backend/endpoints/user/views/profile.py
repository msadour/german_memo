from typing import Any

from rest_framework import viewsets, status, permissions
from rest_framework.request import Request
from rest_framework.response import Response

from core.backend.common.exceptions.handling_exceptions import wrapper_view_error
from core.backend.common.exceptions.user import UpdateError
from core.backend.common.permissions.user import Profile
from core.backend.endpoints.user.models import UserProfile
from core.backend.endpoints.user.serializers import UserSerializer
from core.backend.endpoints.user.utils.perform_actions import perform_create_user, perform_update_user


class SubscriptionViewSet(viewsets.ViewSet):
    """Class SubscriptionViewSet."""

    @wrapper_view_error(class_exception=UpdateError, status=400)
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Subscription of a user.

        Args:
            request: request sent by the client.
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.

        Returns:
            Response from the server.
        """
        data = request.data
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        password_again = data.get("password_again")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        perform_create_user(username, email, password, password_again, first_name, last_name)
        return Response(status=status.HTTP_201_CREATED)


class UserViewSet(viewsets.ModelViewSet):
    """Class UserViewSe."""

    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, Profile]

    @wrapper_view_error(class_exception=UpdateError, status=400)
    def patch(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Update a user.

        Args:
            request: request sent by the client.
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.

        Returns:
            Response from the server.
        """
        email = request.data.get("email", "")
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        password_again = request.data.get("password_again", "")
        perform_update_user(email, username, password, password_again, request.user)
        return Response(status=200)

    def delete(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Delete an user.

        Args:
            request: request sent by the client.
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.

        Returns:
            Response from the server.
        """
        UserProfile.objects.filter(email=request.user.email).delete()
        return Response(status=204)
