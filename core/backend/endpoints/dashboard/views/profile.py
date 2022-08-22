from core.backend.endpoints.dashboard.views.base import ManageBaseViewSet
from core.backend.endpoints.user.models import UserProfile
from core.backend.endpoints.user.serializers import UserSerializer


class ManageUserProfileViewSet(ManageBaseViewSet):
    """Class ManageUserProfileViewSet."""

    model = UserProfile
    serializer_class = UserSerializer
