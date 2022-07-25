from rest_framework import serializers

from core.backend.endpoints.vocabulary.models import Word


class WordSerializer(serializers.ModelSerializer):
    """Class WordSerializer."""

    class Meta:
        """Class Meta."""

        model = Word
        fields = "__all__"
