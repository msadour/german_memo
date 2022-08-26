import requests

from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.request import Request


def login_page(request, message=None):
    data = {"message": message}
    return render(request, "authentication/auth-login.html", data)


def perform_login(request):
    email = request.GET.get("emailaddress")
    password = request.GET.get("password")
    data = {
        "email": email,
        "password": password,
    }

    response = requests.post(
        "http://127.0.0.1:8000/api/user/api-token-auth/",
        data=data,
    )

    if response.status_code == 201:
        data = response.json()
        request.session["token"] = data["token"]
        request.session["user_id"] = data["user_id"]
        request.session["email"] = data["email"]
        request.session["is_staff"] = data["is_staff"]
        return redirect("/")
    else:
        data_error = response.json()
        message = data_error["error"]
        return login_page(request, message=message)


def perform_logout(request: Request) -> HttpResponse:
    """Logout a user.

    Args:
        request: request sent by the client.

    Returns:
        Auth page.
    """
    requests.post(
        f"http://127.0.0.1:8000/api/user/logout/",
        headers={"Authorization": "Token " + request.session.get("token", "")}
    )
    request.session.clear()
    logout(request)
    return redirect("/")
