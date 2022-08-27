import requests

from django.shortcuts import render, redirect


def change_request_page(request):
    data_verbs = requests.get(
        f"http://127.0.0.1:8000/api/dashboard_request_change/verb/",
        headers={"Authorization": "Token " + request.session.get("token", "")}
    ).json()

    data_words = requests.get(
        f"http://127.0.0.1:8000/api/dashboard_request_change/word/",
        headers={"Authorization": "Token " + request.session.get("token", "")}
    ).json()

    data = {
        "verbs": data_verbs,
        "words": data_words
    }

    return render(request, "dashboard_request/request_changes.html", data)


def send_request_change_vocabulary(request, pk):
    data = {
        "id": pk,
        "direct_pronoun": request.POST.get("direct_pronoun"),
        "german_translation": request.POST.get("german_translation"),
        "english_translation": request.POST.get("english_translation"),
        "french_translation": request.POST.get("french_translation"),
    }

    requests.post(
        f"http://127.0.0.1:8000/api/dashboard_request_change/word/",
        headers={"Authorization": "Token " + request.session.get("token", "")},
        data=data
    )

    return redirect("/")


def update_request_change_vocabulary(request):
    pass


def send_request_change_verb(request, pk):
    data = {
        "id": pk,
        "verb_in_present": request.POST.get("username"),
        "english_translation": request.POST.get("first_name"),
        "french_translation": request.POST.get("last_name"),
        "past_participle": request.POST.get("password"),
        "simple_past": request.POST.get("password_again"),
    }
    requests.post(
        f"http://127.0.0.1:8000/api/dashboard_request_change/verb/",
        headers={"Authorization": "Token " + request.session.get("token", "")},
        data=data
    )

    return redirect("/")


def update_request_change_verb(request):
    pass