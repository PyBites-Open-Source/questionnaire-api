from flask_sqlalchemy import SQLAlchemy
from flask_api import FlaskAPI
from instance.config import app_config #local

#initialize sql alchemy
db = SQLAlchemy()

def create_app(config_name):
    """wraps creation of new flask object"""
    
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("config.py")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app) #connects app to db
    return app