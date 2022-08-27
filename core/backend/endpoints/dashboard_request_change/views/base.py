from rest_framework import viewsets, status, permissions
from rest_framework.request import Request
from rest_framework.response import Response

from core.backend.common.exceptions.handling_exceptions import wrapper_view_error
from core.backend.common.exceptions.user import UpdateError
from core.backend.endpoints.dashboard_request_change.utils import perform_update_change_request
from core.backend.endpoints.verb.models import Verb
from core.backend.endpoints.vocabulary.models import Word


class RequestChangeBaseViewSet(viewsets.ModelViewSet):
    """Class RequestChangeBaseViewSet."""

    model = None
    model_item_to_change = None
    serializer_class = None
    queryset = None
    permission_classes = [permissions.IsAuthenticated,]

    @wrapper_view_error(class_exception=UpdateError, status=400)
    def list(self, request: Request) -> Response:
        """
        Get all items for approving.

        Args:
            request: request sent by the client.

        Returns:
            Response from the server.
        """
        items = self.model.objects.all()
        data = self.serializer_class(items, many=True).data
        return Response(data=data)

    def create(self, request, *args, **kwargs):
        data = request.data.dict()
        id_item_to_change = data.pop("id")
        item = self.model_item_to_change.objects.get(id=id_item_to_change)
        self.model.objects.create(
            item=item,
            data=data
        )
        return Response(status=status.HTTP_201_CREATED)

    def patch(self, request, pk):
        data = request.data
        request_change = self.model.objects.get(id=pk)
        perform_update_change_request(data, request_change)
        return Response(status=status.HTTP_200_OK)
