from rest_framework import viewsets
from core.backend.endpoints.vocabulary.models import Word
from core.backend.endpoints.vocabulary.serializer import WordSerializer


class ManageWordViewSet(viewsets.ViewSet):
    """Class ManageWordViewSet."""

    model = Word
    serializer_class = WordSerializer
