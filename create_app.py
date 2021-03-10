from flask import Flask
from flask_cors import CORS
from databases.sql_db import db
from configs.app_configs.config import app_config

from search_app.views import search_page
from job_app.views import job_page


def create_app(config_name):
    flask_app = Flask(__name__)
    flask_app.config.from_object(app_config[config_name])
    flask_app.config.from_pyfile('configs/app_configs/config.py')

    db.init_app(flask_app)

    flask_app.secret_key = flask_app.config['SECRET']

    CORS(flask_app)

    flask_app.register_blueprint(search_page)
    flask_app.register_blueprint(job_page)

    return flask_app
