import requests

from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.request import Request


def settings_page(request, error=None):
    user_data = requests.get(
        f"http://127.0.0.1:8000/api/user/profile/{request.session['user_id']}/",
        headers={"Authorization": "Token " + request.session.get("token", "")}
    ).json()
    data = {"error": error, "user": user_data}
    return render(request, "settings/page.html", data)


def perform_update(request):
    pass