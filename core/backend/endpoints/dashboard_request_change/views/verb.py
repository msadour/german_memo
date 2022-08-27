from core.backend.endpoints.dashboard_request_change.models import VerbRequest
from core.backend.endpoints.dashboard_request_change.serializers import VerbRequestChangeSerializer
from core.backend.endpoints.dashboard_request_change.views.base import RequestChangeBaseViewSet
from core.backend.endpoints.verb.models import Verb


class RequestChangeVerbViewSet(RequestChangeBaseViewSet):
    """Class ManageBaseViewSet."""

    model = VerbRequest
    model_item_to_change = Verb
    serializer_class = VerbRequestChangeSerializer
    queryset = VerbRequest.objects.all().order_by("date")
