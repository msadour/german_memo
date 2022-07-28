from rest_framework import serializers

from core.backend.endpoints.verb.models import Verb


class VerbSerializer(serializers.ModelSerializer):
    """Class VerbSerializer."""

    class Meta:
        """Class Meta."""

        model = Verb
        fields = "__all__"
