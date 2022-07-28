from rest_framework import viewsets
from core.backend.endpoints.user.models import UserProfile
from core.backend.endpoints.user.serializers import UserSerializer


class ManageUserProfileViewSet(viewsets.ViewSet):
    """Class ManageUserProfileViewSet."""

    model = UserProfile
    serializer_class = UserSerializer
