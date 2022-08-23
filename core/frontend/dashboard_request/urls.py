"""Urls module."""


from django.urls import path

from core.frontend.dashboard_request import views

urlpatterns = [
    path("", views.request_page, name="request_page"),

    path("approve/word/<pk>/", views.approve_word, name="approve_word"),
    path("reject/word/<pk>/", views.reject_word, name="reject_word"),

    path("approve/user/<pk>/", views.approve_user, name="approve_user"),
    path("reject/user/<pk>/", views.reject_user, name="reject_user"),

    path("approve/verb/<pk>/", views.approve_verb, name="approve_verb"),
    path("reject/verb/<pk>/", views.reject_verb, name="reject_verb"),
]
