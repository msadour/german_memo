import requests

from django.shortcuts import render


def verb_page(request):
    verbs = requests.get("http://127.0.0.1:8000/api/verb/").json()
    data = {"verbs": verbs}
    return render(request, "verb_page/verbs.html", data)
