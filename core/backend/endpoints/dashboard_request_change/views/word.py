from core.backend.endpoints.dashboard_request_change.models import WordRequest
from core.backend.endpoints.dashboard_request_change.serializers import WordRequestChangeSerializer
from core.backend.endpoints.dashboard_request_change.views.base import RequestChangeBaseViewSet
from core.backend.endpoints.vocabulary.models import Word


class RequestChangeWordViewSet(RequestChangeBaseViewSet):
    """Class RequestChangeWordViewSet."""

    model = WordRequest
    model_item_to_change = Word
    serializer_class = WordRequestChangeSerializer
    queryset = WordRequest.objects.all().order_by("date")
