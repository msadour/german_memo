"""Urls module."""


from django.urls import path
from rest_framework.routers import DefaultRouter

from core.backend.endpoints.user.views.session import LogoutViewSet, CustomAuthToken


router = DefaultRouter()
router.register(r"logout", LogoutViewSet, basename="logout")

urlpatterns = router.urls

urlpatterns += [path("api-token-auth/", CustomAuthToken.as_view())]
