import requests

from django.shortcuts import render


def verb_page(request):
    verbs = requests.get("http://127.0.0.1:8000/api/verb/").json()
    data = {"verbs": verbs}
    return render(request, "verb_page/verbs.html", data)


def request_change(request, pk: str = None):
    verb = requests.get(f"http://127.0.0.1:8000/api/verb/{pk}/").json()
    data = {"verb": verb}
    return render(request, "verb_page/verb_request_change.html", data)
