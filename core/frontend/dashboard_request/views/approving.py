import requests

from django.shortcuts import render


def request_page(request):
    verbs = requests.get("http://127.0.0.1:8000/api/dashboard/verb/", headers={"Authorization": "Token " + request.session.get("token", "")}).json()
    users = requests.get("http://127.0.0.1:8000/api/dashboard/user/", headers={"Authorization": "Token " + request.session.get("token", "")}).json()
    words = requests.get("http://127.0.0.1:8000/api/dashboard/vocabulary/", headers={"Authorization": "Token " + request.session.get("token", "")}).json()

    data = {"verbs": verbs, "users": users, "words": words}
    return render(request, "dashboard_request/approving.html", data)


def approve_word(request, pk):
    requests.patch(
        f"http://127.0.0.1:8000/api/dashboard/vocabulary/{pk}/",
        headers={"Authorization": "Token " + request.session.get("token", "")},
        data={"approved": True}
    )
    return request_page(request)


def reject_word(request, pk):
    requests.patch(
        f"http://127.0.0.1:8000/api/dashboard/vocabulary/{pk}/",
        headers={"Authorization": "Token " + request.session.get("token", "")},
        data={"approved": False}
    )
    return request_page(request)


def approve_user(request, pk):
    requests.patch(
        f"http://127.0.0.1:8000/api/dashboard/user/{pk}/",
        headers={"Authorization": "Token " + request.session.get("token", "")},
        data={"approved": True}
    )
    return request_page(request)


def reject_user(request, pk):
    requests.patch(
        f"http://127.0.0.1:8000/api/dashboard/user/{pk}/",
        headers={"Authorization": "Token " + request.session.get("token", "")},
        data={"approved": False}
    )
    return request_page(request)


def approve_verb(request, pk):
    requests.patch(
        f"http://127.0.0.1:8000/api/dashboard/verb/{pk}/",
        headers={"Authorization": "Token " + request.session.get("token", "")},
        data={"approved": False}
    )
    return request_page(request)


def reject_verb(request, pk):
    requests.patch(
        f"http://127.0.0.1:8000/api/dashboard/verb/{pk}/",
        headers={"Authorization": "Token " + request.session.get("token", "")},
        data={"approved": False}
    )
    return request_page(request)
