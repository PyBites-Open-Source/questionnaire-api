from flask import Blueprint

# Define answer Blueprint
answer_bp = Blueprint("answer_api", __name__)


@answer_bp.route("/answers/<int:id>", methods=["GET"])
def get_answer(id):
    """ Get answer. """
    pass


@answer_bp.route("/answers/<int:question_id>", methods=["POST"])
def create_answer():
    """ Create new answer. """
    pass


@answer_bp.route("/answers/<int:id>", methods=["PUT"])
def update_answer(id):
    """ Update answer. """
    pass


@answer_bp.route("/answers/<int:id>", methods=["DELETE"])
def delete_answer(id):
    """ Delete answer. """
    pass
