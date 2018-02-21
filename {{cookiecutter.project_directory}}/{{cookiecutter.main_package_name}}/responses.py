"""Utility functions."""
import json

from {{cookiecutter.main_package_name}}.constants import HTTP_CODES


def success_response():
    """Return HTTP OK message."""
    payload = {'success': True}
    return _json_response(payload, HTTP_CODES['OK'])


def error_response(error):
    """Return standard error response to user."""
    payload = {'error': {'code': error.code, 'message': error.message}}
    return _json_response(payload, error.code)


def _json_response(payload, code):
    """Return payload as JSON. Sets correct Content-Type header.

    Args:
        payload (dict): The payload to return
        code (int): HTTP response code

    Returns:
        The HTTP response to return from a view or errorhandler.

    """
    return json.dumps(payload), code, {'Content-Type': 'application/json'}
