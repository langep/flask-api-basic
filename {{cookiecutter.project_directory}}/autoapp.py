"""Create an application instance."""
import os

from {{cookiecutter.main_package_name}}.app import create_app
from {{cookiecutter.main_package_name}}.config import DevelopmentConfig

app_config = os.getenv('APP_CONFIG', DevelopmentConfig)
app = create_app(config_object=app_config)
