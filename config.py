import os
import pathlib

from dotenv import load_dotenv

load_dotenv()


class BaseConfig(object):
    """Base Configuration"""

    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv("SECRET")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


class DevelopmentConfig(BaseConfig):
    """Development Configuration"""

    DEBUG = True
    DATABASE = pathlib.Path(__file__).parent.joinpath("instance/dev_opentrivia.db")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE}"


class TestingConfig(BaseConfig):
    """Testing Configuration"""

    TESTING = True
    DEBUG = True
    DB_USER = os.getenv("POSTGRES_USER")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    DB_DATABASE = os.getenv("POSTGRES_DB_TEST")
    DB_PORT = os.getenv("DB_PORT")
    DB_HOST = os.getenv("DB_HOST")
    URI = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    SQLALCHEMY_DATABASE_URI = URI


class ProductionConfig(BaseConfig):
    """Production Configuration"""

    DB_USER = os.getenv("POSTGRES_USER")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    DB_DATABASE = os.getenv("POSTGRES_DB_PROD")
    DB_PORT = os.getenv("DB_PORT")
    DB_HOST = os.getenv("DB_HOST")
    URI = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    SQLALCHEMY_DATABASE_URI = URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app_config = {
    "testing": TestingConfig,
    "production": ProductionConfig,
    "development": DevelopmentConfig,
}
