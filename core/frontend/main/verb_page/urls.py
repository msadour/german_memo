"""Urls module."""


from django.urls import path

from core.frontend.main.verb_page import views

urlpatterns = [
    path("", views.verb_page, name="verb_page"),
]
