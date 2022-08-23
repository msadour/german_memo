from rest_framework import serializers

from core.backend.endpoints.dashboard.utils import approve
from core.backend.endpoints.verb.models import Verb


class VerbSerializer(serializers.ModelSerializer):
    """Class VerbSerializer."""

    approved = serializers.BooleanField()

    def update(self, instance, validated_data):
        is_approved = validated_data.pop("approved")
        approve(instance, is_approved)
        return instance

    class Meta:
        """Class Meta."""

        model = Verb
        fields = "__all__"
