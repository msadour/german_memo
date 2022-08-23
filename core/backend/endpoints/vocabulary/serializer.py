from rest_framework import serializers

from core.backend.endpoints.dashboard.utils import approve
from core.backend.endpoints.vocabulary.models import Word


class WordSerializer(serializers.ModelSerializer):
    """Class WordSerializer."""

    approved = serializers.BooleanField()

    def update(self, instance, validated_data):
        is_approved = validated_data.pop("approved")
        approve(instance, is_approved)
        return instance

    class Meta:
        """Class Meta."""

        model = Word
        fields = "__all__"
