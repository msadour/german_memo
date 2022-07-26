# -*- coding: utf-8 -*-
"""Views module."""


from __future__ import unicode_literals

from typing import Any

from rest_framework import viewsets, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication


from core.backend.endpoints.user.serializers import AuthTokenSerializer
from core.backend.endpoints.user.utils.session import auth_user, logout
from core.backend.common.exceptions.user import AuthenticationError
from core.backend.common.exceptions.handling_exceptions import wrapper_view_error


@permission_classes((permissions.AllowAny,))
class CustomAuthToken(ObtainAuthToken):
    """Class CustomAuthToken."""

    authentication_classes = [TokenAuthentication]

    @wrapper_view_error(class_exception=AuthenticationError, status=401)
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Authenticate a user.

        Args:
            request: request sent by the client.
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.

        Returns:
            Response from the server.
        """
        serializer = AuthTokenSerializer()
        data = auth_user(request=request, serializer=serializer)
        return Response(data=data, status=201)


@permission_classes((permissions.AllowAny,))
class LogoutViewSet(viewsets.ViewSet):
    """Class LogoutViewSet."""

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Logout a user.

        Args:
            request: request sent by the client.
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.

        Returns:
            Response from the server.
        """
        return logout(request)
