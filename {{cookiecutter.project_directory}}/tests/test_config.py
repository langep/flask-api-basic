"""Test config.py."""
import logging

from {{cookiecutter.main_package_name}}.app import create_app
from {{cookiecutter.main_package_name}}.config import (
    DevelopmentConfig,
    ProductionConfig,
    TestingConfig
)


def test_production_config():
    """Production config."""
    app = create_app(ProductionConfig)
    assert app.config['ENV'] == 'production'
    assert app.config['DEBUG'] is False
    assert app.config['TESTING'] is False
    assert app.config['LOG_LEVEL'] in [logging.ERROR, logging.WARNING,
                                       logging.INFO, logging.DEBUG]
    assert app.config.get('URL_PREFIX', None)


def test_dev_config():
    """Development config."""
    app = create_app(DevelopmentConfig)
    assert app.config['ENV'] == 'development'
    assert app.config['DEBUG'] is True
    assert app.config['TESTING'] is False
    assert app.config['LOG_LEVEL'] in [logging.ERROR, logging.WARNING,
                                       logging.INFO, logging.DEBUG]
    assert app.config.get('URL_PREFIX', None) is None


def test_test_config():
    """Testing configuration."""
    app = create_app(TestingConfig)
    assert app.config['ENV'] == 'testing'
    assert app.config['DEBUG'] is True
    assert app.config['TESTING'] is True
    assert app.config['LOG_LEVEL'] in [logging.ERROR, logging.WARNING,
                                       logging.INFO, logging.DEBUG]
    assert app.config.get('URL_PREFIX', None) is None
