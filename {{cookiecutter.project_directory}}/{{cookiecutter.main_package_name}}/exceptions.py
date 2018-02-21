"""Custom exceptions module."""

from {{cookiecutter.main_package_name}}.constants import HTTP_CODES


class ApiError(Exception):
    """Base exception."""

    def __init__(self, message, code=HTTP_CODES['BAD_REQUEST']):
        """Construct ApiError object.

        Args:
            message (str): Explanation of error
            code (int): HTTP reponse code
        """
        self.code = code
        self.message = message
