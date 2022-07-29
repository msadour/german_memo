"""Perform actions for user module."""


import re
from typing import Dict

from core.backend.endpoints.user.models import UserProfile
from core.backend.common.exceptions.user import UpdateError
from core.backend.common.tools import translate_value


def check_email_format(email: str):
    """Check email format.

    Args:
        email:
    """
    regex_email = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    is_email = re.fullmatch(regex_email, email)
    if is_email is None:
        raise UpdateError("Wrong email format.")


def perform_create_user(username, email, password, password_again, first_name, last_name) -> None:
    """Create a user.

    Args:
        username:
        email:
        password:
        password_again:
        first_name:
        last_name:

    Returns:
        User created.
    """
    if len(password) <= 5:
        raise UpdateError("Passwords is too short. Password should contain minimum 6 character.")

    if password != password_again:
        raise UpdateError("Passwords doesn't match.")

    if len(email) > 0:
        if len(UserProfile.objects.filter(email=email)) > 0:
            raise UpdateError("This email is not available.")
    check_email_format(email)

    if len(UserProfile.objects.filter(username=username)) > 0:
        raise UpdateError("This username is not available.")
    elif len(username) <= 2:
        raise UpdateError("Username is too short.")

    UserProfile.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )


def perform_update_user(email, username, password, password_again, user) -> None:
    """Update a user.

    Args:
        email:
        username:
        password:
        password_again:
        user:
    """
    if len(password) > 0:
        if password != password_again:
            raise UpdateError("Passwords doesn't match.")

        if password != "" and password_again != "":
            user.set_password(password)

    if len(email) > 0:
        if user.email != email and len(UserProfile.objects.filter(email=email)) > 0:
            raise UpdateError("This email is not available.")
        check_email_format(email)
        user.email = email

    if len(username) > 0:
        if user.username != username and len(UserProfile.objects.filter(username=username)) > 0:
            raise UpdateError("This username is not available.")
        user.email = email

    user.save()


def perform_update_user_from_interface(data: Dict) -> UserProfile:
    """Update a user.

    Args:
        data:

    Returns:
        User updated.
    """
    user_id = data.get("user_id")
    user = UserProfile.objects.get(id=user_id)

    for field, value in data.items():
        if field == "password" and len(value) > 0:
            user.set_password(value)

        if field == "email":
            if len(UserProfile.objects.filter(email=value)) == 0:
                check_email_format(value)
                user.email = value

        if field == "is_active":
            user.is_active = translate_value(value)

        if field == "is_staff":
            user.is_staff = translate_value(value)

    user.save()
    return user
