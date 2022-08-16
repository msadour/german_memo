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
