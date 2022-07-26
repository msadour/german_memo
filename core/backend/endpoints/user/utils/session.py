"""Authentication module."""


from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import logout as django_logout
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from core.backend.endpoints.user.serializers import AuthTokenSerializer


def auth_user(request: Request, serializer: AuthTokenSerializer) -> dict:
    """Authenticate a user.

    Args:
        request:
        serializer:

    Returns:
        Response with user info.
    """
    user = serializer.validate(attrs=request.data)
    request.user = user
    token, created = Token.objects.get_or_create(user=user)
    return {
        "token": token.key,
        "email": user.email,
        "user_id": user.id,
        "is_admin": user.is_superuser,
        "is_staff": user.is_staff,
    }


def logout(request: Request) -> Response:
    """Logout a user.

    Args:
        request:

    Returns:
        Response.
    """
    try:
        request.user.auth_token.delete()
    except (AttributeError, ObjectDoesNotExist):
        pass
    if getattr(settings, "REST_SESSION_LOGIN", True):
        django_logout(request)

    return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
