"""Tools module."""


from typing import Any


def translate_value(value: str) -> Any:
    """
    Get value as python from string.

    Args:
        value:

    Return:
        value in Python.
    """
    if type(value) == str:
        return eval(value)
    return value
