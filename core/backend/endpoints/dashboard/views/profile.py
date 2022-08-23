from core.backend.endpoints.dashboard.views.base import ManageBaseViewSet
from core.backend.endpoints.user.models import UserProfile
from core.backend.endpoints.user.serializers import UserInterfaceSerializer


class ManageUserProfileViewSet(ManageBaseViewSet):
    """Class ManageUserProfileViewSet."""

    model = UserProfile
    queryset = UserProfile.objects.filter(approved=False)
    serializer_class = UserInterfaceSerializer
