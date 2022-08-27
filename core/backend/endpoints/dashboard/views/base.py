from typing import Any

from rest_framework import viewsets, status, permissions
from rest_framework.request import Request
from rest_framework.response import Response

from core.backend.common.exceptions.handling_exceptions import wrapper_view_error
from core.backend.common.exceptions.user import UpdateError


class ManageBaseViewSet(viewsets.ModelViewSet):
    """Class ManageBaseViewSet."""

    model = None
    serializer_class = None
    queryset = None
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    @wrapper_view_error(class_exception=UpdateError, status=400)
    def list(self, request: Request) -> Response:
        """
        Get all items for approving.

        Args:
            request: request sent by the client.

        Returns:
            Response from the server.
        """
        items = self.model.objects.filter(approved=False)
        data = self.serializer_class(items, many=True).data
        return Response(data=data)
