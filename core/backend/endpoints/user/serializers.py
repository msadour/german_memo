"""User serializer module."""


from typing import Any

from django.contrib.auth.hashers import check_password
from django.http import QueryDict
from django.db.models import Q
from rest_framework import serializers

from core.backend.endpoints.dashboard.utils import approve
from core.backend.endpoints.user.models import UserProfile
from core.backend.common.exceptions.user import AuthenticationError


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object."""

    username = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )

    def authenticate_user(self, email: str = None, username: str = None, password: str = None) -> Any:
        """Authenticate with username and password.

        Args:
            email:
            username:
            password:

        Returns:
            User.
        """
        user = UserProfile.objects.filter(Q(email=email) | Q(username=username)).first()

        if user is None:
            raise AuthenticationError("Not user found with this email.")

        if not user.is_active:
            raise AuthenticationError("This account is deactivate.")

        if not user.approved:
            raise AuthenticationError("This account is not yet approved. Please contact the administrator.")

        if not check_password(password, user.password):
            raise AuthenticationError("Email/Password doesn't match.")

        return user

    def validate(self, attrs: Any) -> UserProfile:
        """Validate a member with credentials.

        Args:
            attrs: Datas from the view.

        Returns:
            User authenticate.
        """
        if type(attrs) == QueryDict:
            attrs = attrs.dict()
        email = attrs.get("email")
        password = attrs.get("password")
        user = self.authenticate_user(email=email, password=password)
        return user


class UserSerializer(serializers.ModelSerializer):
    """Class UserSerializer."""

    class Meta:
        """Class Meta."""

        model = UserProfile
        fields = "__all__"


class UserInterfaceSerializer(serializers.ModelSerializer):
    """Class UserInterfaceSerializer."""

    approved = serializers.BooleanField()

    def update(self, instance, validated_data):
        is_approved = validated_data.pop("approved")
        approve(instance, is_approved)
        return instance

    class Meta:
        """Class Meta."""

        model = UserProfile
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "approved"
        ]
