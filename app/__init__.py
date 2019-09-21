from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.api.resources import Question
from config import app_config

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
    migrate = Migrate(app=app, db=db)

    # Init API
    api = Api(app)

    # Define routes
    api.add_resource(Question, "/api/v1/question/<question_id>")

    # Import blueprints
    from app.views import webapp

    # Register blueprints
    app.register_blueprint(webapp)

    return app
