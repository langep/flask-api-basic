"""The app module, containing the app factory function."""
import logging

from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

import {{cookiecutter.main_package_name}}.commands as commands
from {{cookiecutter.main_package_name}}.config import DevelopmentConfig
from {{cookiecutter.main_package_name}}.constants import HTTP_CODES
from {{cookiecutter.main_package_name}}.errorhandlers import handle_api_error, handle_http_error
from {{cookiecutter.main_package_name}}.exceptions import ApiError
from {{cookiecutter.main_package_name}}.prefix_middleware import PrefixMiddleware


def create_app(config_object=DevelopmentConfig):
    """Return WSGI application.

    Application factories are  explained here:
        http://flask.pocoo.org/docs/patterns/appfactories

    Args:
        config_object: The configuration object to use.

    Returns:
        The Flask application object implementing a WSGI application.

    """
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)

    register_middleware(app)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_logginghandlers(app)
    register_commands(app)

    return app


def register_blueprints(app):
    """Register Flask Blueprints."""
    # Import Blueprints here to prevent issues with imports
    from {{cookiecutter.main_package_name}}.blueprints.health_check import health_check_blueprint
    app.register_blueprint(health_check_blueprint)
    return None


def register_errorhandlers(app):
    """Register custom error handlers."""
    app.errorhandler(ApiError)(handle_api_error)
    app.errorhandler(HTTP_CODES['BAD_REQUEST'])(handle_http_error)
    app.errorhandler(HTTP_CODES['NOT_FOUND'])(handle_http_error)
    app.errorhandler(HTTP_CODES['METHOD_NOT_ALLOWED'])(handle_http_error)
    app.errorhandler(HTTP_CODES['INTERNAL_SERVER_ERROR'])(handle_http_error)


def register_extensions(app):
    """Register Flask extensions."""
    return None


def register_middleware(app):
    """Register middleware."""
    # Fix request.remote_addr when behind proxy e.g. NGINX
    # If you won't use a proxy/loadbalancer in production disable this
    # for security reasons.
    app.wsgi_app = ProxyFix(app.wsgi_app)
    # Prefix URL with 'URL_PREFIX'
    if app.config.get('URL_PREFIX', None):
        app.wsgi_app = PrefixMiddleware(
            app.wsgi_app,
            prefix=app.config['URL_PREFIX']
        )

    return None


def register_logginghandlers(app):
    """Register logging handlers."""
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(app.config['LOG_LEVEL'])

    app.logger.addHandler(stream_handler)
    return None


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.lint)
    app.cli.add_command(commands.clean)
    app.cli.add_command(commands.urls)
    return None
