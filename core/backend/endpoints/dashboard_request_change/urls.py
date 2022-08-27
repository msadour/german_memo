"""Urls module."""


from rest_framework.routers import DefaultRouter

from .views.verb import RequestChangeVerbViewSet
from .views.word import RequestChangeWordViewSet


router = DefaultRouter()
router.register(r"verb", RequestChangeVerbViewSet, basename="verb")
router.register(r"word", RequestChangeWordViewSet, basename="word")


urlpatterns = router.urls
