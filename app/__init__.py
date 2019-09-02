from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_restful import Api
from config import app_config  # local
from app.api.resources import Question

# initialize sql alchemy
db = SQLAlchemy()


def create_app(config_name):
    """wraps creation of new flask object"""

    # Define app object
    app = Flask(__name__, instance_relative_config=True)

    # Load config
    app.config.from_object(app_config[config_name])
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Init database
    db.init_app(app)  # connects app to db

    # Init API
    api = Api(app)

    # Define routes
    api.add_resource(Question, "/<question_id>")

    # Import blueprints
    from app.api.endpoints import api_endpoints

    # Register blueprints
    app.register_blueprint(api_endpoints)

    return app
