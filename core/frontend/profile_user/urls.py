"""Urls module."""


from django.urls import path

from core.frontend.profile_user.views import subscription, authentication, profile

urlpatterns = [
    path("subscription/", subscription.subscription_page, name="subscription"),
    path("perform_subscription/", subscription.perform_subscription, name="perform_subscription"),

    path("login/", authentication.login_page, name="login"),
    path("perform_login/", authentication.perform_login, name="perform_login"),
    path("logout/", authentication.perform_logout, name="logout"),

    path("settings/", profile.settings_page, name="settings"),
    path("update_user_info/", profile.perform_update, name="update_user_info"),
]
