from rest_framework import viewsets, permissions
from rest_framework.request import Request
from rest_framework.response import Response

from core.backend.endpoints.verb.models import Verb
from core.backend.endpoints.verb.serializer import VerbSerializer


class VerbView(viewsets.ViewSet):
    """Class VerbView."""

    serializer_class = VerbSerializer
    queryset = Verb.objects.all().order_by("verb_in_present")
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
