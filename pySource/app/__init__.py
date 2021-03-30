import os
from os import path
from flask import Flask

from flask_moment import Moment
from config import config
from flask_uploads import patch_request_class


moment = Moment()

basedir = path.abspath(path.dirname(__file__))

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    basedir = path.abspath(path.dirname(__file__))

    MUSIC_FOLDER = os.path.join(basedir, 'static/musics')
    app.config['MUSIC_FOLDER'] = MUSIC_FOLDER

    moment.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from . import db
    db.init_app(app)
    if not os.path.exists("flaskr.sqlite"):
        with app.app_context():
            db.init_db()

    return app
