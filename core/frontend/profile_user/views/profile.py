import requests
import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def settings_page(request, error=None):
    user_data = requests.get(
        f"http://127.0.0.1:8000/api/user/profile/{request.session['user_id']}/",
        headers={"Authorization": "Token " + request.session.get("token", "")}
    ).json()

    data = {"error": error, "user": user_data}
    return render(request, "settings/page.html", data)


@csrf_exempt
def perform_update(request):
    data = {
        "email": request.POST.get("email"),
        "username": request.POST.get("username"),
        "first_name": request.POST.get("first_name"),
        "last_name": request.POST.get("last_name"),
        "password": request.POST.get("password"),
        "password_again": request.POST.get("password_again"),
    }
    response = requests.patch(
        f"http://127.0.0.1:8000/api/user/profile/",
        headers={"Authorization": "Token " + request.session.get("token", "")},
        data=data
    )

    if response.status_code != 200:
        error = json.loads(response.content).get("error")
        return settings_page(request, error)

    return settings_page(request)
