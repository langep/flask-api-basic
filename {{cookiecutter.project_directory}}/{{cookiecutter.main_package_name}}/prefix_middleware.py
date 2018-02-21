"""Prefix middleware module to serve application routes with URL prefix."""

from {{cookiecutter.main_package_name}}.constants import HTTP_CODES


class PrefixMiddleware(object):
    """Prefixes every route with `prefix`.

    Explained here:
    https://stackoverflow.com/questions/18967441/add-a-prefix-to-all-flask-routes/36033627#36033627

    """

    def __init__(self, app, prefix=''):
        """Construct PrefixMiddleware."""
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):
        """Prefix routes or return error information."""
        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response(
                HTTP_CODES['NOT_FOUND'],
                [('Content-Type', 'text/plain')]
            )
            return ['This app is submounted under prefix: [{0}]'
                    .format(self.prefix).encode()]
