import os
import pathlib


class BaseConfig(object):
    """Base Configuration"""

    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv("SECRET")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


class DevelopmentConfig(BaseConfig):
    """Development Configuration"""

    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing Configuration"""

    TESTING = True
    DEBUG = True
    DATABASE = pathlib.Path(__file__).parent.joinpath("instance/tododev.db")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE}"


class StagingConfig(BaseConfig):
    """Staging Configuration"""

    DEBUG = True


class ProductionConfig(BaseConfig):
    """Production Configuration"""

    DEBUG = False
    TESTING = False


app_config = {
    "staging": StagingConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "development": DevelopmentConfig,
}
