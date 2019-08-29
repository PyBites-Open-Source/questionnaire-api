import os

class Config(object):
    """Parent Configuration"""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv("SECRET")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


class DevelopmentConfig(Config):
    """Development Configuration"""
    DEBUG = True


class TestingConfig(Config):
    """Testing Configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/test_db"
    DEBUG = True


class StagingConfig(Config):
    """Staging Configuration"""
    DEBUG = True


class ProductionConfig(Config):
    """Production Configuration"""
    DEBUG = False
    TESTING = False


app_config = {
    "staging": StagingConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "development": DevelopmentConfig,
}