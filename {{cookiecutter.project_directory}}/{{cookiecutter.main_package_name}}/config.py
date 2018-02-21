"""Application configuration."""
import logging
import os


class Config(object):
    """Base configuration."""

    SECRET_KEY = os.environ.get('{{cookiecutter.main_package_name | upper}}_SECRET', 'default-secret-key')


class DevelopmentConfig(Config):
    """Development configuration."""

    ENV = 'development'
    DEBUG = True
    LOG_LEVEL = logging.DEBUG


class TestingConfig(Config):
    """Test configuration."""

    ENV = 'testing'
    DEBUG = True
    TESTING = True
    LOG_LEVEL = logging.DEBUG


class ProductionConfig(Config):
    """Production configuration."""

    ENV = 'production'
    DEBUG = False
    TESTING = False
    URL_PREFIX = os.environ.get('{{ cookiecutter.main_package_name | upper}}_URL_PREFIX',
                                '/{{ cookiecutter.main_package_name | lower }}')
    LOG_LEVEL = logging.WARNING
