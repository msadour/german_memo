"""Urls module."""


from rest_framework.routers import DefaultRouter

from core.backend.endpoints.vocabulary.views import VocabularyView


router = DefaultRouter()
router.register(r"", VocabularyView, basename="")

urlpatterns = router.urls
