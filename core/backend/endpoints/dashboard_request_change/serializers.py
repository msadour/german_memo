from rest_framework import serializers

from core.backend.endpoints.dashboard_request_change.models import WordRequest, VerbRequest
from core.backend.endpoints.verb.serializer import VerbSerializer
from core.backend.endpoints.vocabulary.serializer import WordSerializer


class WordRequestChangeSerializer(serializers.ModelSerializer):
    """Class WordRequestChange."""

    item = WordSerializer()

    class Meta:
        """Class Meta."""

        model = WordRequest
        fields = "__all__"


class VerbRequestChangeSerializer(serializers.ModelSerializer):
    """Class VerbRequestChange."""

    item = VerbSerializer()

    class Meta:
        """Class Meta."""

        model = VerbRequest
        fields = "__all__"
