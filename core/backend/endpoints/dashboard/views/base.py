from typing import Any

from rest_framework import viewsets, status, permissions
from rest_framework.request import Request
from rest_framework.response import Response

from core.backend.common.exceptions.handling_exceptions import wrapper_view_error
from core.backend.common.exceptions.user import UpdateError
from core.backend.endpoints.dashboard.utils import approve


class ManageBaseViewSet(viewsets.ViewSet):
    """Class ManageBaseViewSet."""

    model = None
    serializer_class = None
    permission_classes = [permissions.IsAdminUser]

    @wrapper_view_error(class_exception=UpdateError, status=400)
    def list(self, request: Request) -> Response:
        """
        Get all items for approving.

        Args:
            request: request sent by the client.

        Returns:
            Response from the server.
        """
        items = self.model.objects.filter(approve=False)
        data = self.serializer_class(items, many=True).data
        return Response(data=data)

    @wrapper_view_error(class_exception=UpdateError, status=400)
    def update(self, request: Request, pk: str = None, *args: Any, **kwargs: Any) -> Response:
        """Approve (or not) an item.

        Args:
            request: request sent by the client.
            pk:
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.

        Returns:
            Response from the server.
        """
        item = self.model.objects.get(id=pk)
        is_approved = request.data.get("is_approved")
        approve(item, is_approved)
        return Response(status=status.HTTP_200_OK)
