import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import configs

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(configs['dev'])

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    with app.app_context():
        from marky.views.main import main
        from marky.views.editor import editor
        from marky.views.auth import auth
        app.register_blueprint(main)
        app.register_blueprint(editor)
        app.register_blueprint(auth)

        db.create_all()

        return app
