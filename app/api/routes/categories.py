from flask import Blueprint

# Define category Blueprint
category_bp = Blueprint("category_api", __name__)


@category_bp.route("/categories", methods=["GET"])
def get_categories():
    """ Get all categories. """
    pass


@category_bp.route("/categories/<int:id>", methods=["GET"])
def get_category(id):
    """ Get category. """
    pass


@category_bp.route("/categories", methods=["POST"])
def create_category():
    """ Create new category. """
    pass


@category_bp.route("/categories/<int:id>", methods=["PUT"])
def update_category(id):
    """ Update category. """
    pass
