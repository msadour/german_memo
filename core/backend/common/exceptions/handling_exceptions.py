"""Optimization exceptions."""

import functools
from typing import Any

from rest_framework.response import Response


def wrapper_view_error(
    view: Any = None, class_exception: Any = None, status: int = None
) -> Any:
    """Wrapp a view for handling exception.

    Args:
        view:
        class_exception:
        status:

    Returns:
        Bad containers
    """

    def _decorate(function):
        @functools.wraps(function)
        def wrapped_function(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except class_exception as obj_exception:
                return Response(data={"error": obj_exception.message}, status=status)

        return wrapped_function

    if view:
        return _decorate(view)
    return _decorate
