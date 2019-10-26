from flask import Blueprint, make_response, request, jsonify, abort
from app.api.models.question import Question

# Define Question Blueprint
question_bp = Blueprint("question_api", __name__)


@question_bp.route("/questions", methods=["GET"])
def get_questions():
    """ Get all questions. """
    questions = Question.query.all()
    response = {"questions": [question.to_dict() for question in questions]}
    return make_response(jsonify(response), 200)


@question_bp.route("/questions/<int:id>", methods=["GET"])
def get_question(id):
    """ Get question. """
    question = Question.query.get(id)
    if question is not None:
        response = {"question": question.to_dict()}
        return make_response(jsonify(response), 200)
    abort(404)


@question_bp.route("/questions", methods=["POST"])
def create_question():
    """ Create new question. """
    if request.is_json:
        data = request.get_json()
        new_question = Question(
            data["question"],
            data["category_id"],
            data["level"],
            data["true_false_question"],
        )
        question = new_question.create()
        response = {"question": question.to_dict()}
        return make_response(jsonify(response), 201)
    abort(404)


@question_bp.route("/questions/<int:id>", methods=["PUT"])
def update_question(id):
    """ Update question. """
    question = Question.query.get(id)
    if request.is_json and question is not None:
        data = request.get_json()
        question.question = data["question"]
        question.category_id = data["category_id"]
        question.level = data["level"]
        question.true_false_question = data["true_false_question"]
        question.save()
        response = {"question": question.to_dict()}
        return make_response(jsonify(response), 201)
    abort(404)


@question_bp.route("/questions/<int:id>", methods=["DELETE"])
def delete_question(id):
    """ Delete question. """
    question = Question.query.get(id)
    if question is not None:
        question.delete()
        response = {"message": "Object deleted."}
        return make_response(jsonify(response), 200)
    abort(404)


@question_bp.errorhandler(404)
def not_found(error):
    """ Return message for not found. """
    return make_response(jsonify({"error": "Not found"}), 404)
