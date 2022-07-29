import requests

from django.shortcuts import render, redirect


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
        return redirect("/")
    else:
        data_error = response.json()
        message = data_error["error"]
        return login_page(request, message=message)
