import os 

from flask import Flask
from config import configs
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(configs['dev'])

    db.init_app(app)
    migrate.init_app(app, db)

    from marky.views.main import main
    from marky.views.editor import editor
    app.register_blueprint(main)
    app.register_blueprint(editor)

    return app
