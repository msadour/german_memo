"""Urls module."""


from rest_framework.routers import DefaultRouter

from core.backend.endpoints.verb.views import VerbView


router = DefaultRouter()
router.register(r"", VerbView, basename="")

urlpatterns = router.urls
