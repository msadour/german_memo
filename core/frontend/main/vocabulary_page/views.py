import requests

from django.shortcuts import render


def vocabulary_page(request):
    words = requests.get("http://127.0.0.1:8000/api/vocabulary/").json()
    data = {"words": words}
    return render(request, "vocabulary_page/vocabulary.html", data)


def request_change(request, pk: str = None):
    word = requests.get(f"http://127.0.0.1:8000/api/vocabulary/{pk}/").json()
    data = {"word": word}
    return render(request, "vocabulary_page/vocabulary_request_change.html", data)


def perform_request_change(request, pk: str = None):
    data = {
        "direct_pronoun": request.POST.get("direct_pronoun"),
        "german_translation": request.POST.get("german_translation"),
        "english_translation": request.POST.get("english_translation"),
        "french_translation": request.POST.get("french_translation"),
    }
    requests.post(
        f"http://127.0.0.1:8000/api/vocabulary/",
        headers={"Authorization": "Token " + request.session.get("token", "")},
        data=data
    )
    return render(request, "vocabulary_page/vocabulary.html", data)
