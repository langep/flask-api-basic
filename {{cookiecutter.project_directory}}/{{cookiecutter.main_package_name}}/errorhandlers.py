"""Functions to gracefully handle errors."""
from collections import namedtuple

from flask import current_app

from {{cookiecutter.main_package_name}}.responses import error_response

Error = namedtuple('Error', 'code message')


def handle_api_error(error):
    """Handle ApiError gracefully."""
    current_app.logger.error(error.message)
    return error_response(error)


def handle_http_error(error):
    """Handle generic http errors."""
    code, _, short = str(error).split(':')[0].partition(' ')
    e = Error(code=int(code), message=short)
    return error_response(e)
