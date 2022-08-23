from core.backend.endpoints.dashboard.views.base import ManageBaseViewSet
from core.backend.endpoints.vocabulary.models import Word
from core.backend.endpoints.vocabulary.serializer import WordSerializer


class ManageWordViewSet(ManageBaseViewSet):
    """Class ManageWordViewSet."""

    model = Word
    queryset = Word.objects.filter(approved=False)
    serializer_class = WordSerializer
