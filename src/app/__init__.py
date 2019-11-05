from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

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
    
    # Swagger
    SWAGGER_URL = "/swagger"
    API_URL = "/static/swagger.json"
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={"app_name": "Questionnaire API"})

    with app.app_context():
        # Import blueprints
        from manage import bp_manage
        from app.core.views import webapp
        from app.api.routes.questions import question_bp
        from app.api.routes.answers import answer_bp
        from app.api.routes.categories import category_bp
        API_URL_PREFIX = "/api/v1"

        # Register blueprints
        app.register_blueprint(bp_manage)
        app.register_blueprint(webapp)
        app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
        app.register_blueprint(question_bp, url_prefix=API_URL_PREFIX)
        app.register_blueprint(answer_bp, url_prefix=API_URL_PREFIX)
        app.register_blueprint(category_bp, url_prefix=API_URL_PREFIX)

        return app
