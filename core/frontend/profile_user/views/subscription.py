import requests

from django.shortcuts import render


def subscription_page(request, message=None):
    data = {"message": message}
    return render(request, "subscription/subscription.html", data)


def perform_subscription(request):
    email = request.GET.get("emailaddress")
    username = request.GET.get("username")
    password = request.GET.get("password")
    password_again = request.GET.get("password_again")
    first_name = request.GET.get("first_name")
    last_name = request.GET.get("last_name")

    data = {
        "email": email,
        "username": username,
        "password": password,
        "password_again": password_again,
        "first_name": first_name,
        "last_name": last_name,
    }

    response = requests.post(
        "http://127.0.0.1:8000/api/user/subscription/",
        data=data,
    )

    if response.status_code == 201:
        message = "Your account is created. The admin will validated soon your account."
    else:
        data_error = response.json()
        message = data_error["error"]
    return subscription_page(request, message=message)
