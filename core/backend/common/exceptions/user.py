"""User exceptions module."""


class AuthenticationError(Exception):
    """Class AuthenticationError."""

    def __init__(self, message):
        """Check email format.

        Args:
            message:
        """
        self.message = message
        super().__init__(self.message)


class UpdateError(Exception):
    """Class UpdateError."""

    def __init__(self, message):
        """Check email format.

        Args:
            message:
        """
        self.message = message
        super().__init__(self.message)
