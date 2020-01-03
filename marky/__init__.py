import os 

from flask import Flask
from config import configs

def create_app():
    app = Flask(__name__)
    app.config.from_object(configs['dev'])

    from marky.views.main import main
    from marky.views.editor import editor
    app.register_blueprint(main)
    app.register_blueprint(editor)

    return app
