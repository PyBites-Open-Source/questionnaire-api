
from flask import Blueprint, abort, jsonify, make_response, request

from app.api.decorators import categories_validation
from app.api.models.category import Category

# Define category Blueprint
category_bp = Blueprint("category_api", __name__)


@category_bp.route("/categories", methods=["GET"])
def get_categories():
    """ Get all categories. """
    categories = Category.query.all()
    response = {"categories": [category.to_dict() for category in categories]}
    return make_response(jsonify(response), 200)


@category_bp.route("/categories/<int:id>", methods=["GET"])
def get_category(id):
    """ Get category. """
    category = Category.query.get(id)
    if category is not None:
        response = {"category": category.to_dict()}
        return make_response(jsonify(response), 200)
    abort(404)


@category_bp.route("/categories", methods=["POST"])
@categories_validation
def create_category():
    """ Create new category. """
    if request.is_json:
        data = request.get_json()
        categ = Category(data["name"])
        saved_category = categ.create()
        response = {"category": saved_category.to_dict()}
        return make_response(jsonify(response), 201)
    abort(404)


@category_bp.route("/categories/<int:id>", methods=["PUT"])
@categories_validation
def update_category(id):
    """ Update category. """
    category = Category.query.get(id)
    if request.is_json and category is not None:
        data = request.get_json()
        category.name = data["name"]
        category.save()
        response = {"category": category.to_dict()}
        return make_response(jsonify(response), 200)
    return make_response(jsonify({"message": "Object not found"}), 404)


@category_bp.route("/categories/<int:id>", methods=["DELETE"])
def delete_category(id):
    """ Delete category. """
    category = Category.query.get(id)
    if category is not None:
        category.delete()
        response = {"message": "Object deleted."}
        return make_response(jsonify(response), 200)
    abort(404)


@category_bp.errorhandler(404)
def not_found(error):
    """ Return message for not found. """
    return make_response(jsonify({"error": "Not found"}), 404)
