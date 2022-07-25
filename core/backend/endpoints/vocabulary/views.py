from rest_framework import viewsets, permissions

from core.backend.endpoints.vocabulary.models import Word
from core.backend.endpoints.vocabulary.serializer import WordSerializer


class VocabularyView(viewsets.ReadOnlyModelViewSet):
    """Class VoyageAvailableView."""

    serializer_class = WordSerializer
    queryset = Word.objects.all()
    permission_classes = [permissions.IsAuthenticated, ReadOnlyWithPost]
