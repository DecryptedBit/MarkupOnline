import os
from pathlib import Path

class Config:
    DEBUG = False
    UPLOAD_FOLDER = 'marky/static/uploads/'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'please_change_later')

class DevConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(Path().resolve() / 'app' / 'database' / 'testing.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/marky_dev.db'

class ProdConfig(Config):
    pass

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/marky_testing.db'

configs = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'testing': TestingConfig,
    'default': DevConfig
}
