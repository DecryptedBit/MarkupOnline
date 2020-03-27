import os
from pathlib import Path

class Config:
    DEBUG = False
    UPLOAD_FOLDER = 'mark_one/static/uploads/'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'please_change_later')

class DevConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(Path().resolve() / 'marky' / 'database' / 'testing.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/mark_one_dev.db'

class ProdConfig(Config):
    pass

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/mark_one_testing.db'

configs = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'testing': TestingConfig,
    'default': DevConfig
}
