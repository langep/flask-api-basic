"""Track current version.

This module exists for version information only. It makes it easier to update
the version because we only need to change it in one place.
"""

__version__ = '{{cookiecutter.version}}'
VERSION = tuple(int(x) for x in __version__.split('.'))
