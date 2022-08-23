from core.backend.endpoints.dashboard.views.base import ManageBaseViewSet
from core.backend.endpoints.verb.models import Verb
from core.backend.endpoints.verb.serializer import VerbSerializer


class ManageVerbViewSet(ManageBaseViewSet):
    """Class ManageVerbViewSet."""

    model = Verb
    queryset = Verb.objects.filter(approved=False)
    serializer_class = VerbSerializer
