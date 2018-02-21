"""Health check view module."""
from flask import Blueprint

from {{cookiecutter.main_package_name}}.responses import success_response

health_check_blueprint = Blueprint('health_check', __name__)


@health_check_blueprint.route('/health_check')
def health_check():
    """Return HTTP 200 OK message.

    This route can be used to check if the service is still up and running.

    """
    return success_response()
