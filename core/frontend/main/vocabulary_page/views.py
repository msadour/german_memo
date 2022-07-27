import requests

from django.shortcuts import render


def vocabulary_page(request):
    words = requests.get("http://127.0.0.1:8000/api/vocabulary/").json()
    data = {"words": words}
    return render(request, "vocabulary_page/vocabulary.html", data)
