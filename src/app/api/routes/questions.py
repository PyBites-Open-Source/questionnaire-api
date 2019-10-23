from flask import Blueprint

# Define Question Blueprint
question_bp = Blueprint("question_api", __name__)


@question_bp.route("/questions", methods=["GET"])
def get_questions():
    """ Get all questions. """
    return "Hello World!"


@question_bp.route("/questions/<int:id>", methods=["GET"])
def get_question(id):
    """ Get question. """
    pass


@question_bp.route("/questions", methods=["POST"])
def create_question():
    """ Create new question. """
    pass


@question_bp.route("/questions/<int:id>", methods=["PUT"])
def update_question(id):
    """ Update question. """
    pass
