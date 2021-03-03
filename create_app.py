from flask import Flask
from databases.sql_db import db
from configs.app_configs.config import app_config


def create_app(config_name):
    flask_app = Flask(__name__)
    flask_app.config.from_object(app_config[config_name])
    flask_app.config.from_pyfile('configs/app_configs/config.py')

    db.init_app(flask_app)

    flask_app.secret_key = flask_app.config['SECRET']

    return flask_app
