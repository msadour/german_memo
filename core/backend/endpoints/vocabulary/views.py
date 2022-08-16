from rest_framework import viewsets, permissions
from rest_framework.request import Request
from rest_framework.response import Response

from core.backend.endpoints.vocabulary.models import Word
from core.backend.endpoints.vocabulary.serializer import WordSerializer


class VocabularyView(viewsets.ViewSet):
    """Class VocabularyView."""

    serializer_class = WordSerializer
    queryset = Word.objects.all().order_by("german_translation")
    permission_classes = []

    def list(self, request: Request) -> Response:
        """
        Get all words.

        Args:
            request: request sent by the client.

        Returns:
            Response from the server.
        """
        words = self.queryset.filter(approved=True)
        data = self.serializer_class(words, many=True).data
        return Response(data=data)

    def retrieve(self, request: Request, pk: str = None) -> Response:
        """
        Retrieve particular verb.

        Args:
            request: request sent by the client.
            pk:

        Returns:
            Response from the server.
        """
        word = self.queryset.get(id=pk)
        data = self.serializer_class(word).data
        return Response(data=data)
