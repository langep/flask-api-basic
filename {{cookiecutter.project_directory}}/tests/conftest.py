"""Defines fixtures available to all tests."""

import pytest
from webtest import TestApp

from {{cookiecutter.main_package_name}}.app import create_app
from {{cookiecutter.main_package_name}}.config import TestingConfig


@pytest.fixture
def app():
    """Application for the tests."""
    _app = create_app(TestingConfig)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture
def testapp(app):
    """A Webtest app."""
    return TestApp(app)
