import os
from pathlib import Path

class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'please_change_later')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class DevConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(Path().resolve() / 'app' / 'database' / 'testing.db')

class ProdConfig(Config):
    pass

class TestingConfig(Config):
    pass

configs = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'testing': TestingConfig,
    'default': ProdConfig
}
