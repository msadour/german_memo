"""Urls module."""


from django.urls import path

from core.frontend.main.vocabulary_page import views

urlpatterns = [
    path("", views.vocabulary_page, name="vocabulary_page"),
    path("request_change/vocabulary/<pk>/", views.request_change, name="request_change"),
    path("perform_request_change/vocabulary/<pk>/", views.perform_request_change, name="perform_request_change"),
]
