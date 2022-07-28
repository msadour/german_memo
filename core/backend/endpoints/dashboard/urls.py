"""Urls module."""


from rest_framework.routers import DefaultRouter

from core.backend.endpoints.dashboard.views.profile import ManageUserProfileViewSet
from core.backend.endpoints.dashboard.views.verb import ManageVerbViewSet
from core.backend.endpoints.dashboard.views.vocabulary import ManageWordViewSet


router = DefaultRouter()
router.register(r"user", ManageUserProfileViewSet, basename="user")
router.register(r"verb", ManageVerbViewSet, basename="verb")
router.register(r"vocabulary", ManageWordViewSet, basename="vocabulary")

urlpatterns = router.urls
