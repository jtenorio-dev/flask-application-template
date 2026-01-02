from dynaconf import FlaskDynaconf
from flask import Flask
from app.models import *

def create_app(**config):
    app = Flask(__name__)
    FlaskDynaconf(app, extensions_list="EXTENSIONS", **config)
    app.json.sort_keys = False
    app.config.update(config)
    return app

def create_app_wsgi():
    return create_app()