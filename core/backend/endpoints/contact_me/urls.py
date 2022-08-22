"""Urls module."""


from rest_framework.routers import DefaultRouter

from core.backend.endpoints.contact_me.views import SendMailViewSet


router = DefaultRouter()
router.register(r"", SendMailViewSet, basename="send_email")

urlpatterns = router.urls
