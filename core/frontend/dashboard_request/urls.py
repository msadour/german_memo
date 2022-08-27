"""Urls module."""


from django.urls import path

from core.frontend.dashboard_request.views import approving, change_request

urlpatterns = []

urls_approving = [
    path("", approving.request_page, name="request_page"),

    path("approve/word/<pk>/", approving.approve_word, name="approve_word"),
    path("reject/word/<pk>/", approving.reject_word, name="reject_word"),

    path("approve/user/<pk>/", approving.approve_user, name="approve_user"),
    path("reject/user/<pk>/", approving.reject_user, name="reject_user"),

    path("approve/verb/<pk>/", approving.approve_verb, name="approve_verb"),
    path("reject/verb/<pk>/", approving.reject_verb, name="reject_verb"),
]

urls_request_change = [
    path("requests", change_request.change_request_page, name="request_page"),

    path("send_request/word/<pk>/", change_request.send_request_change_vocabulary, name="send_request_word"),
    path("send_request/verb/<pk>/", change_request.send_request_change_verb, name="send_request_verb"),

    path("update_request/word/<pk>/", change_request.update_request_change_vocabulary, name="update_request_vocabulary"),
    path("update_request/verb/<pk>/", change_request.update_request_change_verb, name="update_request_verb"),
]


urlpatterns += urls_approving
urlpatterns += urls_request_change
