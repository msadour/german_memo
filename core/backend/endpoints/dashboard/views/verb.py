from rest_framework import viewsets
from core.backend.endpoints.verb.models import Verb
from core.backend.endpoints.verb.serializer import VerbSerializer


class ManageVerbViewSet(viewsets.ViewSet):
    """Class ManageVerbViewSet."""

    model = Verb
    serializer_class = VerbSerializer
